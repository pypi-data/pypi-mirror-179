# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['benchling_sdk',
 'benchling_sdk.apps',
 'benchling_sdk.apps.config',
 'benchling_sdk.apps.helpers',
 'benchling_sdk.auth',
 'benchling_sdk.docs',
 'benchling_sdk.helpers',
 'benchling_sdk.models',
 'benchling_sdk.services',
 'benchling_sdk.services.v2',
 'benchling_sdk.services.v2.alpha',
 'benchling_sdk.services.v2.beta',
 'benchling_sdk.services.v2.stable']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'attrs>=20.1.0,<23',
 'backoff>=1.10.0,<2.0.0',
 'benchling-api-client==2.0.76',
 'dataclasses-json>=0.5.2,<0.6.0',
 'httpx>=0.23.0',
 'python-dateutil>=2.8.0,<3.0.0',
 'typing-extensions>=3.7.4,<5.0']

extras_require = \
{':python_version >= "3.11" and python_version < "4.0"': ['psutil>=5.9.4,<6.0.0']}

setup_kwargs = {
    'name': 'benchling-sdk',
    'version': '1.6.0a9',
    'description': 'SDK for interacting with the Benchling Platform.',
    'long_description': "# Benchling SDK\n\nA Benchling platform Python SDK.\n\n## General Usage\n\nFor more detailed usage of the SDK, refer to the [public release notes](https://pypi.org/project/benchling-sdk/), which are stored as part of the project \nin `publish/README.public.md` or our [getting started guide](https://docs.benchling.com/docs/getting-started-with-the-sdk).\n\n## Important! AWS Authentication for Tests\n\nThe integration and smoke tests rely on AWS SSM Parameter Store to retrieve secrets for accessing\nBenchling's APIs. You will need to be authenticated to AWS to execute these successfully.\n\nExamples:\n\n```bash\naws-okta exec prod-eng -- poetry run task integration\naws-okta exec prod-eng -- python3 tests/packaged/run_smoke_test.py\n```\n\n## Developer Notes\n\nThe `benching_sdk.benchling.Benchling` object serves as the point of entry for the SDK. API calls are organized into\nservices that generally correspond to [Capillary documentation](https://docs.benchling.com/reference).\n\nEach method calling the API is wrapped with an `@api_method` decorator. This decorator applies several global\nbehaviors which may not be readily obvious including:\n* Conditionally adding some logging on each method call\n* Applying retries via the backoff library when `RetryStrategy` is configured\n\nLogging in the SDK follows the [Python best practice](https://docs.python-guide.org/writing/logging/#logging-in-a-library)\nof only adding the `logging.NullHandler()`. An example of enabling basic logging:\n\n```python\nimport logging\nlogging.basicConfig(level=logging.INFO)\n```\n\nFor more details on configuring or disabling `RetryStrategy`, refer to *Advanced Use Cases* in `publish/README.public.md`.\n\nHTTP errors like `404` not found are all caught via `raise_for_status()` and transformed into\na standardized `BenchlingError` which wraps the underlying error for a better general error handling experience.\nA caught BenchlingError can be inspected to learn the status triggering it, and the full contents of the error \nresponse returned from the Benchling server.\n\n### Exporting Models\n\nAlthough generated models are packaged in `benchling_api_client.models` \nand its files, we externalize the models via `benchling_sdk.models` in\norder to abstract `benchling_api_client` from users such that they may\nsimply import `benchling_sdk.models.ExampleModelClass`.\n\nThis is accomplished in `benchling_sdk/models/__init__.py`. This file\nis automatically generated from a Jinja template in `templates/` by \nrunning `poetry run task models`. Changes should be committed to source\ncontrol. All tasks should be run from the root directory of the project.\n\nMissing models from `benchling_api_client` are verified by unit\ntest in `benchling-sdk/tests/unit/test_models.py`.\n\n## Configuring pre-push Git Hooks\n\n```bash\npoetry run pre-commit install --hook-type pre-push\n```\n\n## Publishing Releases\n\nThe SDK publishes two main releases: manual stable releases and automated preview releases.\n\n#### Stable Releases:\n\nTo create a stable release of the SDK, create a tag in Git from the `main` branch. CI will then\ninitiate a build, generate the client, and publish the resulting packages.\n\nThe published version will reflect the tag, so a tag of `1.0.4` will publish version `1.0.4`. Tags that do not meet\nPoetry's [version format](https://semver.org/) will create a failed build when publishing is attempted.\n\nThis README will not be published alongside the public package. To modify the public README, modify \n`publish/README.public.md`. The changes will be copied over when preparing for publishing.\n\n*NOTE*: There are some scripts executed that make changes to the working directory and its files with the intention\nof them being discarded (e.g., during CI). If running the scripts locally, exercise caution and save your changes\nfirst.\n\n#### Preview Releases:\n\nPreview releases are automated and run from the `preview_sdk_release.yml` GitHub Actions workflow in this project.\nThe workflow is run on a schedule every night at midnight and publishes a new prerelease preview version of the SDK if it finds that there are\nnew commits on `main` that the current published preview version does not have.\n\nPreview releases use the same CI publishing pipeline as manual releases by creating a new prerelease tag on `main`.\nPreview releases only create tags in GitHub, they do not create GitHub releases. \n\nPreview releases will always stay one minor version ahead of the current stable version of the SDK. So if the current stable \nversion is `1.0.4`, then the next preview versions published will be `1.1.0a0` then `1.1.0a1` and so on until a `1.1.0` \nstable version is published. Once `1.1.0` is published the cycle begins again with a preview version of `1.2.0a0`.\n\n## Integration Tests\n\nIntegration tests must be run manually, either via IDE test runners or by command line:\n\n```bash\npoetry run task integration\n```\n\nIntegration tests will not run under CI yet and are currently tightly coupled to cesdktest.bnch.org. They\nare most effective for quickly running manual regression testing.\n",
    'author': 'Benchling Support',
    'author_email': 'support@benchling.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
