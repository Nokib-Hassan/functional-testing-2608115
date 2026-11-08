# Project Demonstration Guide

## Functional Testing, CI/CD and Live Deployment

**Repository:** https://github.com/Nokib-Hassan/functional-testing-2608115

**Live Application:** https://functional-testing-2608115.onrender.com

**Duration:** 3–5 minutes

### 1. Project Introduction

Introduce the project as a functional testing application that validates 16 Python functions through automated tests and exposes their functionality through a Flask web application.

### 2. Automated Testing

Show the test suite and explain:

- Valid, invalid and boundary-value testing.
- Parameterized tests.
- Exception handling.
- Line and branch coverage.
- Pytest and Ruff.

### 3. Continuous Integration

Open GitHub Actions and demonstrate the Python 3.10, 3.11 and 3.12 test matrix.

Explain that the workflow validates code changes before deployment.

### 4. Live Application

Open the deployed Render application.

Demonstrate:
- The interactive frontend.
- Executing selected functions.
- Displaying results and errors.
- The `/health` endpoint and deployed commit SHA.

### 5. Continuous Deployment

Show the GitHub Actions deployment and smoke-test jobs.

Explain that deployment is triggered only after the test job succeeds.

### 6. Failure Demonstration

Explain the intended failure scenario: a deliberately failing test should cause CI to fail and prevent the deployment job from running.

Do not introduce a failing change into the production branch during the demonstration. Use a temporary feature branch or a controlled demonstration branch.

### 7. Conclusion

Summarize how automated testing, CI validation, deployment gating and live smoke testing work together to improve software quality and deployment reliability.