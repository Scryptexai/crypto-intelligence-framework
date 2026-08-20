# reset/systemd — running the repair programme unattended

Runs `reset/run_pipeline_stages.sh` on the VPS as a systemd unit, so the remaining repair work
finishes on its own over the day or two it needs instead of holding a terminal open.

What one run does, in order:

| stage | what it does |
|---|---|
| **repair** | every project `--audit-json` reports as broken → targeted `--redo-phases` regeneration |
| **publish** | `./run.sh build`, `git commit`, `git push`, `./run.sh sync` |
| **phase11** | Phase 11 (Validation & QA) for projects already clear on phases 1-10 |
| **publish** | again, so the audits reach `poc/qa.json` and the database too |

Phase 11 runs last and only over `phase11_todo` — projects that pass all of phases 1-10 and
have no real `11-conflict.docx` yet. A project still broken, or never started, is not audited.

## Install

```bash
# 1. Put the repo where the unit expects it (or edit the four marked lines in the .service).
sudo mkdir -p /opt && sudo git clone <repo> /opt/crypto-intelligence-framework
sudo chown -R cif:cif /opt/crypto-intelligence-framework

# 2. Credentials — plain KEY=value, one per line, mode 600. Never commit this file.
#    ANTHROPIC_BASE_URL / ANTHROPIC_AUTH_TOKEN / ANTHROPIC_MODEL
#    SUPABASE_URL / SUPABASE_SERVICE_ROLE_KEY
#    DEEPSEEK_API_KEY   (optional — adds the heavy-capable fallback provider)
sudo -u cif install -m 600 /dev/null /opt/crypto-intelligence-framework/.env
sudo -u cif editor /opt/crypto-intelligence-framework/.env

# 3. Install the units.
sudo cp /opt/crypto-intelligence-framework/reset/systemd/cif-pipeline.{service,timer} \
        /etc/systemd/system/
sudo systemctl daemon-reload

# 4. Prove the wiring before letting it spend anything.
sudo -u cif /opt/crypto-intelligence-framework/reset/run_pipeline_stages.sh --dry-run

# 5. Enable.
sudo systemctl enable --now cif-pipeline.timer
```

Run step 4 first, always. It prints the exact plan — which projects, which phases, in what
order — and makes no API call, no commit and no database write.

## Watching it

```bash
systemctl status cif-pipeline.service       # running or not, and for how long
journalctl -u cif-pipeline -f               # live log
systemctl list-timers cif-pipeline.timer    # when it next fires
sudo systemctl start cif-pipeline.service   # start a run now, outside the schedule
sudo systemctl stop cif-pipeline.service    # stop; it resumes cleanly next time
```

Progress at a glance, without reading the log:

```bash
cd /opt/crypto-intelligence-framework && python3 reset/run_deepseek_reset.py --audit
```

## Four things that will bite you if you don't know them

**`TimeoutStartSec=infinity` is load-bearing.** systemd's default start timeout is 90 seconds
and it applies to the whole of a `Type=oneshot` `ExecStart`. Without that line the run is
SIGTERMed a minute and a half in, every time, and the log looks like a gateway problem rather
than a unit misconfiguration.

**Don't run the manual loop and the timer at the same time.** Both write the same
`data_project/<Project>/NN-*.docx` files. The script takes an `flock` and a second *scripted*
run exits immediately, but a hand-typed `run_deepseek_reset.py` does not participate in that
lock. Finish or stop the manual loop before `systemctl enable --now`.

**Pushing needs non-interactive git credentials** for the `cif` user — a deploy key, or a
token in the remote URL. Without them the commit still lands locally and the log says so; it
just never reaches GitHub. Set `PIPELINE_PUSH=0` in the unit if you would rather push by hand.
The commit also needs an identity: `sudo -u cif git config --global user.email ...`.

**A project that fails three times is dropped, on purpose.** Attempts are recorded in
`reset/stage_attempts.log`, and past `PIPELINE_MAX_ATTEMPTS` (default 3) the project is
reported and skipped instead of retried. A format the model gets wrong three times is a prompt
bug in `reset/phase_NN_*.txt` — on a daily timer, retrying it forever is a standing token bill
for a known-broken prompt. After fixing the prompt, delete that project's lines from the log to
let it back in.

## Why there is no state file

Every stage recomputes its work from `--audit-json`, which reads the files on disk. The disk is
the state. So a run killed halfway simply doesn't see the projects it already repaired, nothing
is redone or skipped, and a hardcoded project list can never go stale between the day the unit
is written and the day it finishes.
