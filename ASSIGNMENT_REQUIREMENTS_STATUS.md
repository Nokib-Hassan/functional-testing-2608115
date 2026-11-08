# Assignment Requirements Status

This report compares the supplied `instructions.md` requirements with the
current project and GitHub evidence. The three assignment-source files
(`instructions.md`, `prompt.md`, and `Practical Assignment Functional Testing,
CI CD and Live Deployment.pdf`) are intentionally kept local only and are not
part of the GitHub repository after the cleanup change.

## Completed requirements

### Functional testing

- All 16 functions in `target.py` have dedicated tests in
  `tests/test_target.py`.
- Valid values, boundaries, invalid values, wrong types, and suspected
  original-source behaviors are covered.
- `pytest.mark.parametrize` is used extensively.
- Expected failures use exact exception classes and message matching.
- Return types are checked where relevant.
- No `skip`, `xfail`, or coverage exclusions are used.
- Local verification: **111 tests passed**.
- Local coverage verification: **100% line and 100% branch coverage for
  `target.py`**.
- `target.py` remains unchanged.

### Repository and version control

- The repository is named
  [functional-testing-2608115](https://github.com/Nokib-Hassan/functional-testing-2608115),
  matching the required naming pattern.
- The repository contains at least 10 meaningful commits; GitHub currently
  contains 20 commits.
- `.gitignore`, pinned `requirements.txt`, README documentation, and no
  committed credentials are present.
- Three feature branches were merged through pull requests:
  [PR #1](https://github.com/Nokib-Hassan/functional-testing-2608115/pull/1),
  [PR #2](https://github.com/Nokib-Hassan/functional-testing-2608115/pull/2),
  and
  [PR #3](https://github.com/Nokib-Hassan/functional-testing-2608115/pull/3).
- The deployment repair was merged through
  [PR #4](https://github.com/Nokib-Hassan/functional-testing-2608115/pull/4).
- The `main` branch has an active protection ruleset requiring pull requests
  and the Python 3.10, 3.11, and 3.12 status checks.

### CI/CD

- `.github/workflows/ci.yml` runs on pushes and pull requests targeting
  `main`.
- The required `test` job uses Python 3.10, 3.11, and 3.12 with pip caching.
- Ruff linting, pytest, line coverage, branch coverage, and a 100% coverage
  threshold are enforced.
- Coverage HTML reports are uploaded as workflow artifacts.
- `deploy` depends on `test` and runs only for pushes to `main`.
- Deployment credentials are read from the `DEPLOY_HOOK_URL` GitHub secret.
- `smoke-test` depends on `deploy`, waits for the expected commit SHA, and
  makes three real HTTP checks.
- A genuine failed CI run is recorded:
  [failed run 42455573631](https://github.com/Nokib-Hassan/functional-testing-2608115/actions/runs/42455573631).
- A subsequent successful main run is recorded:
  [successful run 42466254098](https://github.com/Nokib-Hassan/functional-testing-2608115/actions/runs/42466254098).
- Pull request workflows skip deployment and smoke testing, so pull requests
  cannot publish to production.

### Frontend and backend

- A Flask backend executes the original functions in `target.py`.
- The frontend exposes all 16 functions with input fields, execute buttons,
  clear buttons, result areas, and error display.
- JSON arrays support numbers, strings, booleans, lists, dictionaries, and
  tagged tuples, sets, and `None` values.
- User input is parsed without unrestricted `eval()`.
- API errors preserve the distinction between successful results and errors.
- The frontend displays the deployed commit SHA from `/health`.
- Input examples are documented in `FRONTEND_INPUT_VALUES.md`.

### Deployment and live verification

- The public application is configured at
  [functional-testing-2608115.onrender.com](https://functional-testing-2608115.onrender.com).
- `/health` returns a structured status and deployed commit SHA.
- Render's `RENDER_GIT_COMMIT` is preferred for the runtime SHA, followed by
  local/CI fallbacks.
- The last verified deployment run reported:
  `d5c927790ef8d62d03c21ff482d4bad6aa98e127`.
- That run passed the test matrix, deploy job, and smoke-test job.
- The last successful live checks verified the frontend, `/health`,
  `is_adult`, and `celsius_to_fahrenheit`.
- The deployment smoke requests have connection and total timeouts, so an
  unavailable or sleeping service fails promptly instead of hanging forever.

## Remaining or manual requirements

### Live service availability

- A later direct probe timed out while the service was sleeping or unavailable.
  The latest successful GitHub deployment and smoke-test evidence is valid,
  but the live URL should be opened again before the final demonstration to
  confirm the Render service has woken and responds.
- If the service remains unavailable, inspect Render service health, build logs,
  start command (`gunicorn app:app`), and the deployment hook configuration.

### Deployment-provider configuration

- The repository workflow uses `DEPLOY_HOOK_URL` and `LIVE_URL`; the actual
  Render dashboard setting that disables automatic deploys must be retained
  and shown during the demonstration.
- Secret values are intentionally not documented or exposed. Verify that both
  repository secrets still exist before submission.

### Demonstration evidence

- `docs/DEMO_SCRIPT.md` and the README contain the required 3–5 minute
  demonstration script.
- An actual recording has not been committed or verified. Record the test
  coverage, matrix CI, live frontend, matching SHA, and a temporary failing
  branch that is blocked before deployment.
- Do not leave a failing change on `main`.

### Instructor access

- The README states that instructor access is confirmed. If the instructor
  needs a new invitation or a different username, verify that directly in
  GitHub before submission.

### Assignment bonus evidence

- Three feature PRs and active branch protection are configured.
- The final submission should capture screenshots or links showing the
  required status checks and branch rules if the grading process requires
  visual evidence.

## Files intentionally local only

The following files are not project deliverables and must remain outside the
GitHub repository:

1. `instructions.md`
2. `prompt.md`
3. `Practical Assignment Functional Testing, CI CD and Live Deployment.pdf`

They remain in the local Assignment folder for reference.
