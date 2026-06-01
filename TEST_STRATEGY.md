# Test Automation Strategy Document

## 1. First 90 Days

The first 90 days should focus on creating a trusted foundation rather than trying to automate everything quickly. The biggest risk at this stage is building a large but unstable suite that nobody trusts.

### Days 1–30: Assessment and Foundation

First, I would review the existing Playwright tests and understand what already works, what is flaky, and what can be reused. I would also meet with QAs, developers, product managers, and the Head of Product Engineering to understand release pain points and the most common regression areas.

Main focus areas:

* current manual regression scope;
* most critical weekly release checks;
* unstable product areas;
* existing Playwright code quality;
* test environment limitations;
* available test data;
* custom RPC API testability;
* frontend selector strategy;
* GitLab CI/CD constraints.

During this phase, I would define the initial framework structure, coding standards, naming conventions, tagging strategy, and contribution model. I would also create the first GitLab CI job that runs a very small and reliable smoke suite.

The first target flows would be:

* login/session handling;
* access to fleet overview;
* vehicle tracking page availability;
* trip history page availability;
* reports page availability;
* alerts page availability;
* one basic permission check.

These flows are good first candidates because they represent release-critical product areas and should give broad confidence without depending too much on complex UI behavior.

### Days 31–60: CI Adoption and First Useful Coverage

The second month should focus on making automation visible and useful for teams.

I would move the initial Playwright smoke suite into GitLab CI and publish reports from the pipeline. The suite should be small enough to run frequently and stable enough to be trusted.

At the same time, I would introduce the first backend/RPC-level checks. Since the product uses a custom RPC-based API, the framework should not rely only on browser tests. I would build reusable RPC client helpers and start covering backend flows that are faster and more stable than UI automation.

Priority areas:

* vehicle data retrieval;
* trip history data retrieval;
* reports data retrieval;
* alerts data retrieval;
* role/permission checks;
* invalid or empty RPC responses;
* response structure validation.

The goal is to move part of regression coverage below the UI layer and avoid overloading Playwright with checks that are better validated at API/backend level.

### Days 61–90: Scale to Teams and Release Process

In the third month, I would start scaling the practice across teams.

Each team should identify a small number of automation candidates from its product area. The focus should be on stable, repetitive, high-value regression checks, not edge cases or unstable UI scenarios.

By the end of 90 days, I would expect:

* structured Playwright framework in place;
* small smoke suite running in GitLab CI;
* first RPC/backend checks implemented;
* test reports published from CI;
* test tagging and suite separation introduced;
* contribution guidelines documented;
* at least 2–3 teams contributing or pairing on tests;
* flaky test handling process defined;
* automation status included in release preparation.

The main success criterion after 90 days is trust. The suite can still be small, but it should be stable, understandable, and useful for weekly releases.

---

## 2. Framework Architecture

The Playwright framework should be a shared internal tool for all teams, not a collection of unrelated test scripts.

Possible structure:

```text
tests/
  e2e/
    smoke/
    regression/
    product-areas/
      fleet/
      trips/
      reports/
      alerts/
      permissions/
  rpc/
    smoke/
    regression/
  integration/

pages/
  auth/
  fleet/
  vehicles/
  trips/
  reports/
  alerts/

clients/
  rpc/
  auth/
  test-data/

fixtures/
  users/
  sessions/
  vehicles/
  permissions/

utils/
  config/
  assertions/
  reporting/
  data-builders/
```

### Patterns

For UI tests, I would use a lightweight Page Object or Screen Object pattern. The goal is to hide UI implementation details from tests, but not create an over-engineered abstraction layer.

Good test structure:

* arrange test data and user;
* open product area;
* perform user action;
* assert business-relevant result.

I would avoid tests that only check implementation details or duplicate frontend unit tests.

For RPC/backend tests, I would create reusable client wrappers. Since the API is custom RPC rather than REST, this layer is important. Tests should not build raw RPC calls everywhere. They should use shared methods with clear names and common error handling.

### Fixtures

Fixtures should handle common setup:

* authenticated browser session;
* user roles;
* test vehicles;
* permissions;
* RPC client;
* environment configuration;
* test data references.

This keeps tests short and reduces duplication.

### Test Data Management

Test data should be stable and documented.

Initial approach:

* predefined test users;
* predefined roles and permissions;
* predefined vehicles/assets;
* stable fleets for smoke tests;
* known trip/report data where possible.

Later improvement:

* create or reset data through RPC/backend helpers;
* introduce data builders;
* isolate test data by team or test suite;
* add cleanup for tests that create or modify data.

For a fleet management platform, test data should also consider vehicle states, historical trips, alerts, and reports. Random or constantly changing data should not be used for automated regression.

### Environment Configuration

The framework should support multiple environments through configuration:

* local;
* test/staging;
* release candidate environment.

Configuration should include:

* base URL;
* RPC endpoint;
* credentials through CI secrets;
* feature flags if needed;
* browser settings;
* report settings.

No credentials or environment-specific values should be hardcoded.

### Team Contributions

Teams should contribute tests through merge requests using the same structure and standards.

Contribution rules should include:

* where to place tests;
* naming conventions;
* tagging rules;
* selector strategy;
* required assertions;
* how to run tests locally;
* how to debug failures;
* review checklist.

The framework should make the correct way easy and the wrong way obvious.

---

## 3. Test Levels and Scope

The automation strategy should avoid putting everything into E2E tests. E2E tests are valuable, but they are slower, more fragile, and more expensive to maintain.

I would communicate the test levels to teams as follows:

### E2E Tests

Use Playwright E2E tests for critical user journeys that must work from the customer perspective.

Good E2E candidates:

* user can log in and access main product areas;
* fleet overview loads;
* vehicle tracking page is available;
* trip history can be opened;
* reports can be generated or accessed;
* alerts are visible;
* user permissions are respected in the UI;
* cross-product navigation works.

Avoid deep E2E coverage for:

* every filter combination;
* every report calculation;
* complex map rendering;
* live marker movement;
* visual details;
* scenarios better validated through backend data.

### RPC / API-Level Tests

Use RPC/backend tests for business logic and data validation.

Good RPC candidates:

* vehicle data;
* trip history;
* report data;
* alert data;
* permissions;
* filtering;
* sorting;
* validation;
* empty states;
* error responses;
* response structure;
* backward compatibility of important RPC methods.

This layer should carry most regression coverage because it is faster and more stable.

### Integration and Data Flow Checks

Use integration checks for flows where data moves between systems or layers.

Examples:

* incoming vehicle data is processed correctly;
* delayed events do not break trip history;
* duplicate events are handled safely;
* report values match source events;
* alert state matches triggering data;
* backend data matches values exposed through RPC.

For future expansion, this area should include device and sensor data validation using simulators or a controlled test bench.

### Unit and Component Tests

Unit and component tests should remain mostly owned by developers. As Lead QA Automation Engineer, I would not try to own this layer, but I would encourage teams to cover business rules and frontend components closer to the code.

The message to teams would be simple:

* use unit/component tests for isolated logic;
* use RPC tests for backend behavior and data correctness;
* use Playwright E2E for customer-critical journeys;
* do not use E2E tests as the only quality gate.

---

## 4. CI/CD Integration

Automation should be integrated into GitLab CI/CD gradually and carefully.

### Merge Request Pipeline

The MR pipeline should run fast checks:

* linting/type checks for the test framework;
* small Playwright smoke suite;
* selected RPC smoke checks related to changed areas where possible.

This pipeline should be fast and stable. It should not run the full regression suite.

MR pipeline failures should block merge only when the failing tests are stable and relevant. New or unstable tests should not immediately become hard gates.

### Nightly Pipeline

Nightly runs should provide broader feedback:

* full Playwright smoke suite;
* RPC regression suite;
* selected integration checks;
* permission checks;
* report and alert checks.

Nightly results should be reviewed daily. Failures should be categorized as:

* product defect;
* test issue;
* environment issue;
* test data issue;
* flaky test.

### Release Candidate Pipeline

The weekly release pipeline should run the stable release suite:

* critical E2E scenarios;
* critical RPC regression;
* permissions;
* reports;
* alerts;
* known high-risk areas from the release.

Only stable and trusted tests should be release gates.

### Flaky Test Handling

Flaky tests should be visible and managed aggressively.

Process:

* tag flaky tests;
* remove them from release gates;
* create follow-up tickets;
* fix or delete unstable tests;
* track flaky test rate;
* do not allow retries to hide real problems.

Retries can be used carefully for infrastructure instability, but they should not become the main solution.

### Failure Handling

Every failed CI test should provide enough information to debug:

* screenshot for UI failures;
* Playwright trace;
* video where useful;
* error message;
* environment;
* test data used;
* RPC request/response details where safe.

A failed test should help the team answer: is this a product issue, test issue, data issue, or environment issue?

---

## 5. Team Enablement

### First Month

The focus would be:

* explain the automation strategy;
* collect regression pain points;
* identify automation candidates;
* show how the framework is structured;
* create simple examples;
* define contribution rules.

### Months 2–3

I would start pairing with QA specialists and interested developers.

Activities:

* Playwright basics workshop;
* framework walkthrough;
* examples of good and bad tests;
* how to write stable locators;
* how to use fixtures;
* how to run tests locally;
* how to read CI reports;
* how to investigate failures.

Each QA specialist should help identify and review scenarios from their product area. Some may start writing tests directly, while others may contribute through test design and scenario review first.

### Months 4–6

By this point, each team should have at least some ownership over automation for its area.

Expected model:

* Lead QA Automation Engineer owns framework and standards;
* team QAs own test scenarios and product-area coverage;
* developers support testability and review technical changes;
* teams maintain tests related to their features.

I would use code reviews, templates, documentation, and pairing to keep quality consistent.

The adoption goal is not to turn every manual QA into a full automation engineer immediately. The goal is to create a shared practice where teams can contribute without damaging framework stability.

---

## 6. AI Tooling

AI-assisted tooling can be useful, but only if it improves speed or quality without reducing ownership and review discipline.

I would try AI in several practical areas.

### Converting Manual Checks Into Automation Candidates

Manual regression checklists can be analyzed with AI to identify:

* repetitive checks;
* stable automation candidates;
* duplicated scenarios;
* high-risk flows;
* scenarios better suited for RPC tests instead of E2E.

Success measure: less time spent preparing automation backlog and better prioritization.

### Drafting Playwright Test Skeletons

AI can generate first drafts of Playwright tests from approved scenarios.

However, generated code should always be reviewed. It must follow framework patterns, use stable selectors, and include meaningful assertions.

Success measure: faster creation of simple tests without increasing flaky test rate.

### Test Data Variation

AI can help suggest edge cases and data combinations for reports, alerts, permissions, and vehicle states.

Success measure: better test coverage ideas, not automatic test generation without review.

### CI Failure Summaries

AI can help summarize failed pipeline logs, group similar failures, and suggest likely failure categories.

Success measure: shorter failure triage time.

### Documentation Support

AI can help maintain:

* contribution guides;
* test examples;
* onboarding notes;
* release test summaries;
* flaky test summaries.

Success measure: better documentation with less manual effort.

### Evaluation Criteria

I would evaluate AI tooling by:

* time saved;
* quality of generated output;
* reduction in repetitive work;
* review effort required;
* impact on flaky test rate;
* whether teams actually use it.

AI should be treated as an assistant, not as an owner of test quality. All AI-generated tests and documentation should go through normal review.

---

## Summary

The first 90 days should focus on building a trusted automation foundation: framework structure, CI integration, small stable E2E coverage, first RPC/backend checks, reporting, and contribution rules.

Playwright should be used for critical user-facing flows, while RPC/backend tests should carry much of the regression coverage because the product has a custom RPC-based backend and complex data-driven behavior.

Automation should be introduced gradually across teams. The long-term goal is not only to create tests, but to establish a sustainable engineering practice that supports weekly releases, reduces manual regression effort, and gives stakeholders clear confidence in product quality.
