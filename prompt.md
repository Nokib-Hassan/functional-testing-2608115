# MASTER PROMPT: End-to-End Implementation of Functional Testing, CI/CD, Frontend Integration & Live Deployment

## 1. Your Role and Objective

Act as a Senior Python Software Engineer, QA Automation Engineer, DevOps Engineer, and Full-Stack Developer.

Your responsibility is to implement the complete practical assignment described in the provided `instructions.md`,`Practical Assignment Functional Testing, CI CD and Live Deployment.pdf` file.

This is not merely a coding exercise. It is an end-to-end software engineering project that must demonstrate:

- Professional Python functional testing.
- Comprehensive edge-case and negative testing.
- Git and GitHub repository management.
- Continuous Integration (CI) using GitHub Actions.
- Frontend and backend integration.
- Continuous Deployment (CD).
- Public hosting and live application verification.
- Automated post-deployment smoke testing.

**Primary objective:** Deliver a fully functional, professionally structured, tested, documented, and publicly deployable application that satisfies every requirement in `instructions.md`.

Do not simply generate code snippets or explain what should be done. Work directly with the existing project files, implement the required components, execute commands, inspect results, identify problems, and fix them.

---

## 2. Mandatory Initial Inspection

Before making any modifications:

1. Read `instructions.md` completely.
2. Inspect the entire existing project directory and understand its structure.
3. Locate and inspect the original `target.py`.
4. Identify existing Python versions, installed dependencies, Git configuration, and available deployment configuration.
5. Check whether a GitHub repository already exists or needs to be created.
6. Identify existing tests, frontend files, configuration files, and documentation.
7. Prepare a clear implementation plan based on the assignment requirements.

Do not overwrite or unnecessarily recreate existing working files.

If the project already contains implementation work, preserve it and improve it where necessary.

**Critical restriction: Never modify `target.py`.**

The instructor will restore the original `target.py` during grading. All testing and application integration must work against the original implementation.

If you discover potential defects in `target.py`, document them in the README rather than changing the source code.

---

# 3. Part One: Comprehensive Functional Testing (8 Points)

## 3.1 Testing framework

Use:

- Python.
- pytest.
- pytest-cov.
- Appropriate linting tools.
- Python standard library wherever possible.

Create the following test file:

`tests/test_target.py`

The test suite must comprehensively cover all 16 functions implemented in `target.py`.

## 3.2 Function-by-function testing

Test every function independently.

### Data-type functions

1. `is_adult(age)`
   - Negative ages.
   - Zero.
   - Ages immediately below, at, and above 18.
   - Larger valid integer values.
   - Appropriate invalid input types.

2. `celsius_to_fahrenheit(celsius)`
   - Zero Celsius.
   - Freezing and boiling points.
   - Negative temperatures.
   - Positive decimal temperatures.
   - Values requiring rounding.
   - Appropriate boundary and invalid-type cases.

3. `count_vowels(text)`
   - Empty strings.
   - Uppercase and lowercase vowels.
   - Mixed-case strings.
   - Strings without vowels.
   - Repeated vowels.
   - Spaces, punctuation, numbers, and Unicode characters.
   - Non-string inputs.

4. `invert(flag)`
   - True and False.
   - Integer values 0 and 1.
   - Strings.
   - None.
   - Other invalid types.

5. `greet(name=None)`
   - None.
   - Empty strings.
   - Whitespace-only strings.
   - Normal names.
   - Leading and trailing whitespace.
   - Names containing multiple words.
   - Appropriate invalid-type behavior.

6. `find_max(numbers)`
   - Single-element lists.
   - Multiple positive numbers.
   - Negative numbers.
   - Mixed positive and negative values.
   - Duplicate maximum values.
   - Decimal values.
   - Empty lists.
   - Appropriate invalid-input behavior.

7. `get_price(prices, item)`
   - Existing dictionary keys.
   - Missing keys.
   - Empty dictionaries.
   - Different value types.
   - Appropriate dictionary and key edge cases.

8. `swap(pair)`
   - Two-element lists.
   - Two-element tuples.
   - Strings or other valid two-element sequences.
   - Empty sequences.
   - Single-element sequences.
   - More than two elements.

9. `common_items(set_a, set_b)`
   - Identical sets.
   - Partially overlapping sets.
   - Disjoint sets.
   - Empty sets.
   - One empty set.
   - Different valid set contents.

10. `is_leap_year(year)`
    - Year 1.
    - Year 4.
    - Non-leap years.
    - Century years.
    - Years divisible by 400.
    - Negative years.
    - Year zero.
    - Relevant invalid types.

11. `to_int(value)`
    - Integers.
    - Valid integer strings.
    - Positive and negative numeric strings.
    - Floating-point values.
    - Boolean values.
    - None.
    - Invalid strings.
    - Other supported and unsupported conversions.

### Mathematical functions

12. `divide(a, b)`
    - Positive division.
    - Negative division.
    - Decimal division.
    - Division by zero.
    - Negative denominators.
    - Zero numerators.
    - Appropriate numeric types.

13. `power(base, exponent)`
    - Positive exponents.
    - Zero exponents.
    - Negative exponents.
    - Positive and negative bases.
    - Fractional exponents.
    - Relevant mathematical edge cases.

14. `square_root(x)`
    - Zero.
    - Positive integers.
    - Positive decimals.
    - Negative values.
    - Boundary cases.
    - Appropriate invalid-type behavior.

15. `factorial(n)`
    - Zero factorial.
    - One factorial.
    - Small positive integers.
    - Larger integers.
    - Negative integers.
    - Appropriate invalid-type cases.

16. `average(numbers)`
    - Single-element lists.
    - Multiple positive values.
    - Negative values.
    - Mixed positive and negative values.
    - Decimal values.
    - Zero values.
    - Empty lists.
    - Appropriate invalid-input behavior.

The above are minimum testing considerations, not an exhaustive limit. Identify additional meaningful corner cases from the actual implementation.

## 3.3 Testing quality requirements

Implement the following:

- Use `pytest.mark.parametrize` to reduce repetitive test code.
- Use `pytest.raises` for expected exceptions.
- Assert the exact exception class.
- Use `match=` where appropriate to validate exception messages.
- Verify result types wherever relevant.
- Use `pytest.approx()` only when floating-point precision makes exact comparison inappropriate.
- Verify both return values and relevant behavioral characteristics.
- Avoid overly broad assertions.
- Avoid tests that pass without actually validating the intended behavior.

Do not introduce:

- `skip`
- `xfail`
- Hidden failures.
- Artificial coverage exclusions.
- Tests that modify the original implementation.
- Unnecessary mocking that bypasses the actual functions.

## 3.4 Coverage requirements

The final test suite must achieve:

- 100% line coverage of `target.py`.
- 100% branch coverage of `target.py`.

Use:

```bash
pytest --cov=target --cov-branch --cov-report=term-missing
```

Also generate an HTML coverage report:

```bash
pytest --cov=target --cov-branch --cov-report=html
```

Investigate every uncovered line and branch.

Do not claim 100% coverage unless the actual test execution confirms it.

Remember that 100% coverage does not automatically mean all possible logical behaviors have been tested.

---

# 4. Part Two: GitHub Repository and Version Control (3 Points + 2 Bonus)

## 4.1 Repository setup

Create a GitHub repository using the required naming convention:

`functional-testing-<student-id>`

Use the actual student ID supplied by the project owner. Never invent one.

The repository must contain the complete working project.

Configure instructor access if the instructor's GitHub username or invitation details are available. If not, document the required manual action.

## 4.2 Repository structure

Use a clean, maintainable project structure. A suggested starting point is:

```text
functional-testing-<student-id>/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── tests/
│   ├── __init__.py
│   └── test_target.py
│
├── frontend/
│   └── [frontend application files]
│
├── target.py
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── [additional configuration files]
```

Adapt this structure to the selected frontend and backend architecture.

Do not create unnecessary folders or duplicate application files.

## 4.3 Git commit requirements

Make at least 10 focused commits with meaningful commit messages.

Each commit should represent a logical development milestone.

Suggested sequence:

1. Initial project structure and configuration.
2. Add initial functional tests.
3. Expand boundary and negative test coverage.
4. Complete testing for all 16 functions.
5. Achieve 100% line and branch coverage.
6. Add linting and dependency configuration.
7. Implement frontend functionality.
8. Integrate frontend with Python backend.
9. Configure GitHub Actions CI.
10. Implement deployment and health-check functionality.
11. Add smoke testing and deployment documentation.
12. Final validation and README improvements.

These are suggested milestones, not permission to create meaningless commits. Make real, focused commits based on actual completed work.

Never fabricate commit history.

## 4.4 GitHub bonus requirements

Where GitHub access permits, implement:

- At least three feature branches.
- Pull requests from those branches into `main`.
- Successful CI checks on the pull requests.
- Branch protection for `main`.
- Required CI status checks before merging.

Use meaningful branch names, for example:

- `feature/functional-tests`
- `feature/frontend`
- `feature/deployment-pipeline`

Do not merge untested changes merely to satisfy the branch requirement.

## 4.5 Repository configuration

Include:

- `.gitignore`
- Pinned `requirements.txt`
- Appropriate project configuration.
- Clean Git history.
- No API keys, passwords, tokens, or other secrets committed to Git.

Use environment variables and GitHub Secrets for sensitive configuration.

---

# 5. Part Three: GitHub Actions Continuous Integration (3 Points)

Create:

`.github/workflows/ci.yml`

## 5.1 Workflow triggers

The workflow must execute:

- On every push.
- On pull requests targeting `main`.

Use a job named:

`test`

## 5.2 Python compatibility

Test the project against:

- Python 3.10
- Python 3.11
- Python 3.12

Use a GitHub Actions matrix strategy.

Enable pip dependency caching.

## 5.3 CI execution sequence

The workflow must perform the following steps:

1. Check out the repository.
2. Configure the appropriate Python version.
3. Enable pip caching.
4. Install pinned dependencies.
5. Run linting.
6. Execute the complete pytest suite.
7. Generate line and branch coverage.
8. Enforce 100% coverage of `target.py`.
9. Upload the coverage report as a GitHub Actions artifact.

The workflow must fail if:

- Linting fails.
- Any test fails.
- Coverage falls below 100%.
- Required dependencies cannot be installed.

Use an appropriate coverage threshold configuration, such as:

```bash
pytest --cov=target --cov-branch --cov-fail-under=100
```

Ensure the coverage configuration checks both line and branch coverage, rather than relying on a line-only threshold.

## 5.4 Required red and green CI history

Demonstrate the CI pipeline working in both failure and success scenarios.

The GitHub repository must contain:

- At least one genuine red CI run caused by a failing test.
- A subsequent correction.
- A successful green CI run.

Do not fabricate GitHub Actions results or intentionally leave broken code in the final application.

## 5.5 README integration

Add a GitHub Actions status badge to the README.

The badge must reflect the actual workflow status.

---

# 6. Part Four: Interactive Frontend Development (3 Points)

Build a functional web frontend that allows users to interact with all 16 functions in `target.py`.

The instructor will evaluate this application directly.

## 6.1 Technology selection

Choose an appropriate frontend architecture that integrates reliably with Python.

Preferred considerations:

- Python backend.
- HTML, CSS, and JavaScript frontend.
- Flask or FastAPI as the backend framework.
- Responsive and accessible user interface.

Select the architecture based on simplicity, maintainability, deployment compatibility, and reliability.

Do not introduce unnecessary complexity.

## 6.2 Functional requirements

The frontend must provide access to all 16 functions.

Organize the functions into understandable categories:

**Data-type operations:**
1. is_adult
2. celsius_to_fahrenheit
3. count_vowels
4. invert
5. greet
6. find_max
7. get_price
8. swap
9. common_items
10. is_leap_year
11. to_int

**Mathematical operations:**
12. divide
13. power
14. square_root
15. factorial
16. average

For each function:

- Provide an appropriate input interface.
- Accept user-provided values.
- Send inputs to the Python backend.
- Execute the original `target.py` function.
- Display the actual returned result.
- Display meaningful errors when an exception occurs.
- Preserve the distinction between valid results and errors.

Do not hardcode example results in place of executing the actual functions.

## 6.3 Input handling

Implement appropriate input handling for:

- Integers.
- Floating-point numbers.
- Strings.
- Booleans.
- Lists.
- Dictionaries.
- Tuples.
- Sets.
- None values.

For structured inputs, provide a user-friendly input mechanism, such as JSON input with appropriate validation.

Do not silently convert every input into a string if the original function expects another type.

Ensure that JSON parsing and Python type conversion do not accidentally change the behavior being demonstrated.

For example, Python tuples and sets require special consideration because ordinary JSON does not represent them as native Python types.

## 6.4 User interface and experience

Develop a professional, modern, responsive interface.

Include:

- Clear application title.
- Navigation or categorized function selection.
- Individual function panels or cards.
- Input labels and helpful examples.
- Execute buttons.
- Result display areas.
- Error display areas.
- Loading indicators where appropriate.
- Reset or clear functionality.
- Responsive layouts for desktop and mobile.

Use consistent colors, typography, spacing, and component design.

Avoid excessive animations and unnecessary visual complexity.

The application should be intuitive enough for an instructor to test all functions without technical assistance.

## 6.5 Backend architecture

The frontend must communicate with the Python backend through appropriate API endpoints.

Keep the original `target.py` functions as the execution source.

Use a safe input-parsing approach. Never use unrestricted `eval()` to convert user-provided input into Python objects.

Handle exceptions gracefully without exposing internal stack traces or sensitive server information to frontend users.

---

# 7. Part Five: Public Deployment, CI/CD Integration and Automated Smoke Testing (3 Points)

This is a critical part of the assignment.

Implement a genuine push-to-live deployment pipeline.

The expected pipeline must contain three jobs and one deployment gate.

## 7.1 Public deployment

Deploy the application using an appropriate hosting provider, for example:

- Render.
- Railway.
- PythonAnywhere.
- Another suitable public hosting service.

Choose a provider that supports the selected Python backend and the required deployment workflow.

**Important:** Disable automatic deployment through the hosting provider.

GitHub Actions must control when a new version is deployed.

Do not allow a failed CI run to bypass the deployment gate.

## 7.2 Deployment job

Extend the GitHub Actions workflow with a deployment job.

Required behavior:

- The deployment job must depend on the `test` job using `needs: test`.
- It must execute only for pushes to `main`.
- It must use GitHub Secrets for deployment credentials.
- It must deploy the application only after successful CI execution.

Conceptually:

```yaml
deploy:
  needs: test
  if: github.event_name == 'push' && github.ref == 'refs/heads/main'
```

Adapt the implementation to the selected hosting provider.

Never hardcode deployment credentials.

## 7.3 Health endpoint and commit SHA

Implement:

`/health`

The endpoint must return the commit SHA of the version currently running in production.

The SHA must represent the deployed application version, not merely the latest commit currently present in GitHub.

Expose this information in a structured response.

For example:

```json
{
  "status": "healthy",
  "commit_sha": "actual-deployed-commit-sha"
}
```

The frontend must also display the deployed commit SHA.

This is essential for demonstrating that the running application matches the GitHub commit.

## 7.4 Smoke-test job

Create a third GitHub Actions job:

`smoke-test`

The job must:

- Depend on the deployment job.
- Wait until the newly deployed commit SHA becomes available through `/health`.
- Compare the live SHA with the expected GitHub commit SHA.
- Fail if the expected SHA does not appear within a reasonable timeout.
- Perform three actual HTTP requests against the live application.

The three requests should validate meaningful application functionality.

For example:

1. Check the `/health` endpoint.
2. Execute a valid function through the public API.
3. Execute another valid function or validate the frontend availability.

Use actual expected responses and HTTP status codes.

Do not treat a successful HTTP connection alone as proof that the application works correctly.

## 7.5 Required deployment pipeline

The final workflow should follow this dependency structure:

```text
                 GitHub Push / Pull Request
                            |
                            v
                       TEST JOB
                  Python 3.10 / 3.11 / 3.12
                            |
                 +----------+----------+
                 |                     |
              Success                Failure
                 |                     |
                 v                     v
          PUSH TO MAIN ONLY       STOP PIPELINE
                 |
                 v
             DEPLOY JOB
                 |
                 v
           LIVE APPLICATION
                 |
                 v
           SMOKE-TEST JOB
                 |
          +------+------+
          |             |
        Pass           Fail
          |             |
          v             v
     Deployment      Pipeline
      Verified       Failure
```

Pull requests must run tests but must never deploy.

Failed test runs must block deployment.

---

# 8. Demonstration Requirements (3–5 Minutes)

Prepare a practical demonstration plan that proves the complete system works.

The demonstration must cover:

### Demonstration 1: Functional testing

- Show the test suite.
- Run pytest.
- Show 100% line and branch coverage.

### Demonstration 2: GitHub Actions

- Show the workflow configuration.
- Show the Python version matrix.
- Show a genuine failing CI run.
- Show the subsequent successful CI run.

### Demonstration 3: Frontend

- Open the publicly deployed application.
- Execute representative data-type and mathematical functions.
- Demonstrate a successful result.
- Demonstrate appropriate error handling.

### Demonstration 4: Successful deployment

- Make a small valid change.
- Commit and push it to `main`.
- Show CI passing.
- Show the deployment job executing.
- Show the smoke-test job passing.
- Verify that the live application's SHA matches the pushed GitHub commit.

### Demonstration 5: Failed deployment prevention

- Introduce a controlled failing test in a temporary test commit.
- Push the change through the normal workflow.
- Show that CI fails.
- Verify that deployment does not execute.
- Restore the working state and show the successful pipeline again.

Do not leave the production branch in a failing state.

Provide a concise, timed 3–5 minute recording script and checklist.

If you cannot access screen-recording software, prepare the complete recording instructions rather than claiming to have recorded the video.

---

# 9. README Documentation

Create a professional and comprehensive `README.md`.

It must include:

1. Project title and overview.
2. Assignment objectives.
3. Technology stack.
4. Project directory structure.
5. Installation prerequisites.
6. Local setup instructions.
7. Dependency installation instructions.
8. How to run the application.
9. How to execute tests.
10. How to generate coverage reports.
11. Explanation of the GitHub Actions workflow.
12. GitHub Actions status badge.
13. Public deployment URL.
14. API endpoints and example requests.
15. Health endpoint and commit SHA explanation.
16. Deployment and smoke-testing process.
17. Suspected bugs or limitations identified in the original `target.py`.
18. GitHub repository URL.
19. Instructions for reproducing the demonstration.

Include actual URLs only after they have been verified.

Clearly document any suspected defects without changing the original source code.

---

# 10. Code Quality and Engineering Standards

Follow these engineering principles throughout the implementation:

- Write readable, maintainable Python code.
- Use meaningful variable and function names.
- Follow PEP 8 conventions.
- Keep application logic separate from frontend presentation.
- Avoid unnecessary code duplication.
- Use pinned dependencies.
- Validate user inputs.
- Handle exceptions appropriately.
- Avoid exposing secrets.
- Use appropriate HTTP status codes.
- Keep API responses consistent.
- Ensure frontend and backend integration works.
- Make configuration environment-based.
- Document important architectural decisions.
- Avoid unnecessary dependencies and abstractions.

Do not sacrifice maintainability just to satisfy individual grading requirements.

---

# 11. Implementation and Execution Strategy

Work in the following order.

**Phase 1 — Inspection and planning**

Inspect the repository and source instructions. Establish the implementation plan and identify missing prerequisites.

**Phase 2 — Testing**

Create comprehensive tests for all 16 functions. Run them repeatedly until all requirements are satisfied.

**Phase 3 — Quality and configuration**

Add linting, pinned dependencies, project configuration, and `.gitignore`.

**Phase 4 — Frontend and backend**

Build the API and interactive frontend. Test every function through the application.

**Phase 5 — GitHub and CI**

Configure GitHub Actions, the Python matrix, coverage enforcement, artifacts, and README badge.

**Phase 6 — Deployment**

Configure public hosting, deployment secrets, manual deployment control, and the `/health` endpoint.

**Phase 7 — Smoke testing**

Implement the third job, verify deployment SHA synchronization, and test three live requests.

**Phase 8 — GitHub bonus requirements**

Create feature branches, pull requests, and branch protection where permissions allow.

**Phase 9 — Final validation**

Perform a complete local and remote validation of the project.

**Phase 10 — Documentation and handover**

Complete the README, prepare the demo script, and provide a final implementation report.

Do not skip ahead while essential dependencies from an earlier phase remain broken.

---

# 12. Mandatory Verification Checklist

Before declaring the project complete, verify every item below.

## Functional testing

- [ ] All 16 original functions are tested.
- [ ] Valid inputs are covered.
- [ ] Boundary cases are covered.
- [ ] Invalid inputs and wrong types are covered where relevant.
- [ ] Parametrization is used appropriately.
- [ ] Exact exception classes are asserted.
- [ ] Exception messages are checked where appropriate.
- [ ] Result types are validated where necessary.
- [ ] 100% line coverage is achieved.
- [ ] 100% branch coverage is achieved.
- [ ] No skipped or xfailed tests.

## GitHub

- [ ] Repository has the correct name.
- [ ] At least 10 meaningful commits exist.
- [ ] `.gitignore` is present.
- [ ] `requirements.txt` is pinned.
- [ ] No secrets are committed.
- [ ] README is complete.
- [ ] Instructor access is configured or documented.
- [ ] Three feature branches and PRs are completed where possible.
- [ ] Branch protection is configured where possible.

## CI/CD

- [ ] GitHub Actions workflow exists.
- [ ] Push trigger works.
- [ ] Pull request trigger works.
- [ ] Python 3.10 matrix works.
- [ ] Python 3.11 matrix works.
- [ ] Python 3.12 matrix works.
- [ ] Pip caching is enabled.
- [ ] Linting works.
- [ ] Tests execute successfully.
- [ ] Branch and line coverage are enforced.
- [ ] Coverage artifact is uploaded.
- [ ] README badge works.
- [ ] Genuine red CI run exists.
- [ ] Subsequent green CI run exists.

## Frontend

- [ ] All 16 functions are accessible.
- [ ] Inputs are handled correctly.
- [ ] Backend integration works.
- [ ] Actual function results are displayed.
- [ ] Errors are displayed appropriately.
- [ ] Interface is responsive.
- [ ] No hardcoded demonstration results replace actual execution.

## Deployment

- [ ] Application is publicly accessible.
- [ ] Provider auto-deploy is disabled.
- [ ] Deployment job depends on successful tests.
- [ ] Deployment occurs only on pushes to `main`.
- [ ] GitHub Secrets are used.
- [ ] `/health` returns the deployed commit SHA.
- [ ] Frontend displays the deployed SHA.
- [ ] Smoke-test job waits for the correct SHA.
- [ ] Three live requests are verified.
- [ ] Failed CI blocks deployment.
- [ ] Successful deployment is demonstrated.

## Final submission

- [ ] README is complete.
- [ ] All relevant URLs are verified.
- [ ] Suspected original-source bugs are documented.
- [ ] Three-to-five-minute demonstration script is prepared.
- [ ] Final project structure is clean.
- [ ] Original `target.py` remains unchanged.

---

# 13. Important Execution Rules

Follow these rules without exception:

1. **Never modify `target.py`.** It is the instructor-provided source and must remain compatible with the original grading environment.

2. Do not assume that passing tests locally guarantees success on GitHub Actions. Verify all three Python versions.

3. Do not claim coverage, CI success, deployment, smoke-test success, or GitHub configuration unless the actual result has been verified.

4. Do not invent GitHub repository URLs, deployment URLs, student IDs, instructor usernames, or credentials.

5. If a required account, permission, API token, or hosting secret is unavailable, implement everything possible and clearly identify the remaining manual action.

6. Never expose credentials in terminal output, documentation, source code, or Git commits.

7. Do not weaken tests to make faulty code pass.

8. Do not change expected behavior merely to achieve better coverage.

9. Preserve the original function behavior, including its actual exception handling and return types.

10. When a suspected bug is discovered, create an appropriate test that reflects the documented behavior and record the discrepancy in the README. Do not silently modify the source.

11. Execute actual commands and inspect their output. Do not substitute explanations for implementation.

12. Fix problems before moving to the next dependent implementation phase.

13. Maintain a clear distinction between completed work, verified work, and work blocked by external permissions.

14. If an architectural or technology decision is necessary, select the simplest reliable option and document the reasoning rather than repeatedly stopping for minor decisions.

15. Avoid unnecessary questions. Ask only when genuinely required information, such as a student ID or deployment credential, prevents further progress.

---

# 14. Final Deliverables and Reporting

At the end of implementation, provide a structured completion report containing:

### A. Project overview
Explain the implemented architecture and technology stack.

### B. Implementation summary
Describe the completed testing, frontend, backend, CI/CD, and deployment components.

### C. Testing results
Report:

- Total test count.
- Passed tests.
- Failed tests.
- Line coverage.
- Branch coverage.
- Supported Python versions.
- Linting results.

Use actual execution results.

### D. GitHub information
Provide:

- Repository URL.
- Commit count.
- Feature branches.
- Pull request links.
- Branch protection status.
- CI workflow URL.

### E. Application information
Provide:

- Live application URL.
- API endpoint documentation.
- Health endpoint URL.
- Example API requests.
- Verified deployed commit SHA.

### F. Deployment verification
Explain:

- How the deployment gate works.
- How the live SHA is verified.
- Results of the three smoke tests.
- Evidence that failed CI prevents deployment.

### G. Remaining actions
List anything requiring manual intervention, account access, instructor information, or external permissions.

### H. Final grading alignment
Map each completed assignment requirement to its implementation location and available verification evidence.

### I. Demonstration
Provide a concise 3–5 minute demonstration script.

---

# FINAL INSTRUCTION

Treat `instructions.md` `Practical Assignment Functional Testing, CI CD and Live Deployment.pdf` as the authoritative assignment specification.

Your goal is to deliver a complete, production-style academic project that satisfies the instructor's actual requirements rather than merely creating a collection of files that appear to satisfy them.

Prioritize correctness, comprehensive testing, reproducibility, security, maintainability, and verifiable results.

**Start by inspecting the existing project and its files. Then implement the assignment systematically, execute the required commands, resolve errors, and validate every deliverable before reporting completion.**