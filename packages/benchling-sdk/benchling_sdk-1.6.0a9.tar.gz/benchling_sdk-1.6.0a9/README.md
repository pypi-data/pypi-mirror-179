# Benchling SDK

A Benchling platform Python SDK.

## General Usage

For more detailed usage of the SDK, refer to the [public release notes](https://pypi.org/project/benchling-sdk/), which are stored as part of the project 
in `publish/README.public.md` or our [getting started guide](https://docs.benchling.com/docs/getting-started-with-the-sdk).

## Important! AWS Authentication for Tests

The integration and smoke tests rely on AWS SSM Parameter Store to retrieve secrets for accessing
Benchling's APIs. You will need to be authenticated to AWS to execute these successfully.

Examples:

```bash
aws-okta exec prod-eng -- poetry run task integration
aws-okta exec prod-eng -- python3 tests/packaged/run_smoke_test.py
```

## Developer Notes

The `benching_sdk.benchling.Benchling` object serves as the point of entry for the SDK. API calls are organized into
services that generally correspond to [Capillary documentation](https://docs.benchling.com/reference).

Each method calling the API is wrapped with an `@api_method` decorator. This decorator applies several global
behaviors which may not be readily obvious including:
* Conditionally adding some logging on each method call
* Applying retries via the backoff library when `RetryStrategy` is configured

Logging in the SDK follows the [Python best practice](https://docs.python-guide.org/writing/logging/#logging-in-a-library)
of only adding the `logging.NullHandler()`. An example of enabling basic logging:

```python
import logging
logging.basicConfig(level=logging.INFO)
```

For more details on configuring or disabling `RetryStrategy`, refer to *Advanced Use Cases* in `publish/README.public.md`.

HTTP errors like `404` not found are all caught via `raise_for_status()` and transformed into
a standardized `BenchlingError` which wraps the underlying error for a better general error handling experience.
A caught BenchlingError can be inspected to learn the status triggering it, and the full contents of the error 
response returned from the Benchling server.

### Exporting Models

Although generated models are packaged in `benchling_api_client.models` 
and its files, we externalize the models via `benchling_sdk.models` in
order to abstract `benchling_api_client` from users such that they may
simply import `benchling_sdk.models.ExampleModelClass`.

This is accomplished in `benchling_sdk/models/__init__.py`. This file
is automatically generated from a Jinja template in `templates/` by 
running `poetry run task models`. Changes should be committed to source
control. All tasks should be run from the root directory of the project.

Missing models from `benchling_api_client` are verified by unit
test in `benchling-sdk/tests/unit/test_models.py`.

## Configuring pre-push Git Hooks

```bash
poetry run pre-commit install --hook-type pre-push
```

## Publishing Releases

The SDK publishes two main releases: manual stable releases and automated preview releases.

#### Stable Releases:

To create a stable release of the SDK, create a tag in Git from the `main` branch. CI will then
initiate a build, generate the client, and publish the resulting packages.

The published version will reflect the tag, so a tag of `1.0.4` will publish version `1.0.4`. Tags that do not meet
Poetry's [version format](https://semver.org/) will create a failed build when publishing is attempted.

This README will not be published alongside the public package. To modify the public README, modify 
`publish/README.public.md`. The changes will be copied over when preparing for publishing.

*NOTE*: There are some scripts executed that make changes to the working directory and its files with the intention
of them being discarded (e.g., during CI). If running the scripts locally, exercise caution and save your changes
first.

#### Preview Releases:

Preview releases are automated and run from the `preview_sdk_release.yml` GitHub Actions workflow in this project.
The workflow is run on a schedule every night at midnight and publishes a new prerelease preview version of the SDK if it finds that there are
new commits on `main` that the current published preview version does not have.

Preview releases use the same CI publishing pipeline as manual releases by creating a new prerelease tag on `main`.
Preview releases only create tags in GitHub, they do not create GitHub releases. 

Preview releases will always stay one minor version ahead of the current stable version of the SDK. So if the current stable 
version is `1.0.4`, then the next preview versions published will be `1.1.0a0` then `1.1.0a1` and so on until a `1.1.0` 
stable version is published. Once `1.1.0` is published the cycle begins again with a preview version of `1.2.0a0`.

## Integration Tests

Integration tests must be run manually, either via IDE test runners or by command line:

```bash
poetry run task integration
```

Integration tests will not run under CI yet and are currently tightly coupled to cesdktest.bnch.org. They
are most effective for quickly running manual regression testing.
