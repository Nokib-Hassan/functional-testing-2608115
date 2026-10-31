# Functional Testing Lab

An end-to-end Python functional-testing project built around the instructor-provided
`target.py`. The original source is intentionally unchanged. A Flask application exposes
all 16 functions through a safe JSON API and a responsive browser interface.

[![CI](https://github.com/OWNER/functional-testing-STUDENT-ID/actions/workflows/ci.yml/badge.svg)](https://github.com/OWNER/functional-testing-STUDENT-ID/actions/workflows/ci.yml)

## Stack and structure

- Python 3.10–3.12, Flask, Gunicorn
- pytest, pytest-cov, Ruff
- GitHub Actions matrix CI and gated deployment
- `target.py`: original source, never modify
- `tests/test_target.py`: parametrized functional tests for all 16 functions
- `app.py`: API, frontend serving, health endpoint, and safe tagged-value decoding
- `templates/`, `static/`: accessible interactive frontend
- `.github/workflows/ci.yml`: test, deploy, and smoke-test jobs

## Local setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
flask --app app run
```

Open `http://127.0.0.1:5000`. The app displays the deployed SHA from `COMMIT_SHA`,
`GITHUB_SHA`, or `local` when run locally.

## Tests and coverage

```bash
ruff check .
pytest --cov=target --cov-branch --cov-report=term-missing --cov-report=html --cov-fail-under=100
```

The test suite checks valid inputs, boundaries, wrong types, exact exception classes and
messages, return types, and additional behavior for all 16 functions. The API tests are
separate so the coverage gate remains specifically about the original target module.

## API

`GET /health` returns the running version:

```json
{"status": "healthy", "commit_sha": "actual-deployed-sha"}
```

Call a function with a JSON array of arguments:

```bash
curl -X POST http://127.0.0.1:5000/api/functions/is_adult \
  -H 'Content-Type: application/json' -d '{"args":[18]}'
```

Structured Python values use tagged objects: `{"type":"tuple","value":[1,2]}`,
`{"type":"set","value":[1,2]}`, `{"type":"none","value":null}`, or
`{"type":"json","value":"{\"key\": \"value\"}"}`.

## CI/CD and deployment

Every push and pull request to `main` runs linting and the Python 3.10/3.11/3.12 test
matrix with branch and line coverage enforced at 100%. Coverage HTML reports are uploaded
as artifacts. Only a successful push to `main` can run `deploy`; pull requests never deploy.

Configure a hosting provider with automatic deploy disabled, then add these repository
secrets:

- `DEPLOY_HOOK_URL`: provider deploy-hook URL
- `LIVE_URL`: public application URL

The deployment job triggers the provider hook, and `smoke-test` waits for `/health` to
report `${GITHUB_SHA}` before making three real HTTP checks. No credentials are committed.

## Suspected original-source limitations

`greet()` calls `.strip()` for any non-`None` input, so non-string values raise the
natural `AttributeError` rather than a dedicated `TypeError`. `find_max`, `common_items`,
and `average` rely on Python's native operations and therefore expose native type errors
for incompatible inputs. These behaviors are documented and tested without changing
`target.py`, as required by the assignment.

## Repository and live URL

Replace the placeholders in this section and the badge after creating the repository:

- Repository: `https://github.com/OWNER/functional-testing-STUDENT-ID`
- Live application: `https://YOUR-HOST.example`
- Health: `https://YOUR-HOST.example/health`

The student ID and public URLs were not available in the supplied project, so they cannot
be invented safely.

## 3–5 minute demonstration script

1. (0:00–0:45) Show `target.py`, the parametrized tests, and run the test command; point out
   the 100% line and branch coverage.
2. (0:45–1:30) Open `ci.yml`; show the Python matrix, lint/coverage gate, artifact, and the
   `needs: test` deploy condition. Show one genuine failed test run followed by the green
   correction in Actions.
3. (1:30–2:30) Open the live app, run one data function and one math function, then submit
   invalid input to show a useful error.
4. (2:30–3:30) Push a valid change to `main`, show test → deploy → smoke-test, and compare
   the pushed SHA with `/health` and the frontend SHA.
5. (3:30–4:15) Push a temporary failing test, show CI failing with no deploy job, restore
   the working state, and show the final green pipeline.

## GitHub setup checklist

Create the repository as `functional-testing-<student-id>`, add instructor access, and
replace the placeholders above. The supplied folder was not a Git repository and no
student ID, GitHub account, hosting account, or instructor identity was provided, so
repository creation, branch protection, PRs, and live deployment remain external setup
actions.
