# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['neptune_optuna', 'neptune_optuna.impl']

package_data = \
{'': ['*']}

install_requires = \
['neptune-client>=0.16.7', 'optuna>=2.4.0', 'plotly', 'scikit-learn']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata'],
 'dev': ['pre-commit', 'pytest>=5.0', 'pytest-cov==2.10.1']}

setup_kwargs = {
    'name': 'neptune-optuna',
    'version': '0.10.1',
    'description': 'Neptune.ai Optuna integration library',
    'long_description': '# Neptune + Optuna Integration\n\nNeptune is a tool for experiment tracking, model registry, data versioning, and monitoring model training live.\n\nThis integration lets you use it as an Optuna visualization dashboard to log and monitor hyperparameter sweep live.\n\n## What will you get with this integration?\n\n* log and monitor the Optuna hyperparameter sweep live:\n** values and params for each Trial\n** best values and params for the Study\n** hardware consumption and console logs\n** interactive plots from the optuna.visualization module\n** parameter distributions for each Trial\n** Study object itself for \'InMemoryStorage\' or the database location for the Studies with database storage\n* load the Study directly from the existing Neptune Run\nand more.\n\n![image](https://user-images.githubusercontent.com/97611089/160636423-82951249-a5d8-40d3-be34-4c2ff470b9db.png)\n*Parallel coordinate plot logged to Neptune*\n\n\n## Resources\n\n* [Documentation](https://docs.neptune.ai/integrations-and-supported-tools/hyperparameter-optimization/optuna)\n* [Code example on GitHub](https://github.com/neptune-ai/examples/blob/main/integrations-and-supported-tools/optuna/scripts)\n* [Runs logged in the Neptune app](https://app.neptune.ai/o/common/org/optuna-integration/experiments?split=bth&dash=parallel-coordinates-plot&viewId=b6190a29-91be-4e64-880a-8f6085a6bb78)\n* [Run example in Google Colab](https://colab.research.google.com/github/neptune-ai/examples/blob/master/integrations-and-supported-tools/optuna/notebooks/Neptune_Optuna_integration.ipynb)\n\n## Example\n\n```python\n# On the command line:\npip install neptune-client[optuna] optuna\n```\n```python\n# In Python:\nimport neptune.new as neptune\nimport neptune.new.integrations.optuna as optuna_utils\n\n# Start a run\nrun = neptune.init(api_token="ANONYMOUS",\n                   project="common/optuna-integration")\n\n\n# Create a NeptuneCallback instance\nneptune_callback = optuna_utils.NeptuneCallback(run)\n\n\n# Pass the callback to study.optimize()\nstudy = optuna.create_study(direction="maximize")\nstudy.optimize(objective, n_trials=100, callbacks=[neptune_callback])\n\n\n# Watch the optimization live in Neptune\n```\n\n## Support\n\nIf you got stuck or simply want to talk to us, here are your options:\n\n* Check our [FAQ page](https://docs.neptune.ai/getting-started/getting-help#frequently-asked-questions)\n* You can submit bug reports, feature requests, or contributions directly to the repository.\n* Chat! When in the Neptune application click on the blue message icon in the bottom-right corner and send a message. A real person will talk to you ASAP (typically very ASAP),\n* You can just shoot us an email at support@neptune.ai\n',
    'author': 'neptune.ai',
    'author_email': 'contact@neptune.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://neptune.ai/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
