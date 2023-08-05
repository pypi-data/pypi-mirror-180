# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['midas_dev', 'midas_dev.deploy_data']

package_data = \
{'': ['*']}

install_requires = \
['autoflake>=1.7.8,<2.0.0',
 'black>=22.10.0,<23.0.0',
 'click>=8.1.3,<9.0.0',
 'coloredlogs>=15.0.1,<16.0.0',
 'flake8-broken-line>=0.6.0,<0.7.0',
 'flake8-debugger>=4.1.2,<5.0.0',
 'flake8-mock-x2>=0.4.1,<0.5.0',
 'flake8-print>=5.0.0,<6.0.0',
 'flake8-pytest-style>=1.6.0,<2.0.0',
 'flake8-use-fstring>=1.4,<2.0',
 'flake8>=5.0.4,<6.0.0',
 'ipdb>=0.13.9,<0.14.0',
 'isort>=5.10.1,<6.0.0',
 'mypy>=0.991,<0.992',
 'poetry>=1.2.2,<2.0.0',
 'poetryup>=0.12.5,<0.13.0',
 'pre-commit>=2.20.0,<3.0.0',
 'pytest-asyncio>=0.20.2,<0.21.0',
 'pytest-blockage>=0.2.4,<0.3.0',
 'pytest-cov>=4.0.0,<5.0.0',
 'pytest-deadfixtures>=2.2.1,<3.0.0',
 'pytest-env>=0.8.1,<0.9.0',
 'pytest-timeout>=2.1.0,<3.0.0',
 'pytest>=7.2.0,<8.0.0',
 'toml>=0.10.2,<0.11.0']

extras_require = \
{'django': ['django-coverage-plugin>=2.0.4,<3.0.0',
            'django-debug-toolbar>=3.7.0,<4.0.0',
            'django-extra-checks>=0.13.3,<0.14.0',
            'django-migration-linter>=4.1.0,<5.0.0',
            'django-querycount>=0.7.0,<0.8.0',
            'django-split-settings>=1.2.0,<2.0.0',
            'django-stubs>=1.13.0,<2.0.0',
            'django-stubs-ext>=0.7.0,<0.8.0',
            'django-test-migrations>=1.2.0,<2.0.0',
            'flake8-django>=1.1.5,<2.0.0',
            'pytest-django>=4.5.2,<5.0.0']}

entry_points = \
{'console_scripts': ['mid = midas_dev.main:Fulltest.run_cli',
                     'midautoflake = midas_dev.main:Autoflake.run_cli',
                     'midblack = midas_dev.main:Black.run_cli',
                     'middeploy = midas_dev.deploy:DeployManager.run_cli',
                     'midflake8 = midas_dev.main:Flake8.run_cli',
                     'midfmt = midas_dev.main:Format.run_cli',
                     'midisort = midas_dev.main:ISort.run_cli',
                     'midmypy = midas_dev.main:Mypy.run_cli',
                     'midpytest = midas_dev.main:Pytest.run_cli',
                     'midtest = midas_dev.main:Fulltest.run_cli']}

setup_kwargs = {
    'name': 'midas-dev',
    'version': '0.45.0',
    'description': '',
    'long_description': 'None',
    'author': 'Anton V',
    'author_email': 'anton.vasilyev@midas.investments',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
