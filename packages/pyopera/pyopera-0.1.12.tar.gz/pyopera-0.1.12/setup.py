# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyopera', 'pyopera.opera', 'pyopera.opera.helpers']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyopera',
    'version': '0.1.12',
    'description': 'The NIH OPERA suite of models with Python specific functionality',
    'long_description': '# pyOPERA\n[![asv](http://img.shields.io/badge/benchmarked%20by-asv-blue.svg?style=flat)]  \nFull python implementation of the NIH OPERA suite of models  \ndocker run -it -v %cd%:/app --rm pyopera_pyopera /bin/bash  \ndocker compose -f docker-compose.yml build  \ndocker run --rm pyopera_pyopera ~/.local/share/pypoetry/venv/bin/poetry run coverage run -m pytest tests  \ndocker build -t cabreratoxy/pyopera:0.0.1 .  \n\n```\npoetry run python -m pip install -r requirements.txt  \npoetry run black . --exclude={docs/,libOPERA_Py/,.asv/}  \npoetry run isort . --skip={docs/,libOPERA_Py/,.asv/}  \npoetry run pylint $(find pyopera -name "*.py" | xargs)  \npoetry run pytest tests    \npoetry run coverage run --source pyopera -m pytest  \npoetry run coverage report --skip-empty --fail-under=85  \npoetry build  \npoetry config repositories.testpypi https://test.pypi.org/legacy/  \n\ndocker run --rm pyopera_pyopera /bin/bash -c \'poetry run coverage run -m pytest tests\'   \nif [ git diff --exit-code Dockerfile ]; then dockerfiles/build_docker.sh; fi\n```\n\n\n\nTODO: Test TestPypi package locally  \nTODO: Benchmarking with airspeed velocity (struggling to make it work without a setup.py)  \nTODO: Don\'t repeat the library name in the Dockerfile  \n~~TODO: Find out how to trigger the docker image build step when the file changes~~\nTODO: Start adding the wrapper code and files - in progress  \nTODO: Add actual documentation in this readme  \nTODO: Automate versioning  \n~~TODO: Struggling to run commands inside Docker from the host, will run commands from inside container for now~~  \n~~TODO: Add the original library folder into the folder structure  (manual for now, eventually upload it as a build artifact or similar)~~  \n~~TODO: poetry is not including the additional files with the library~~  \n~~TODO: Fully install poetry in the container (maybe use the long name as a variable for now)~~  \n~~TODO: Create CI/CD for package in TestPypi and the prod Pypi (CircleCI maybe?)~~  \n~~TODO: Documentation using Sphinx (make sure original repo/builders are credited)~~  \n~~TODO: Auto semantic versioning with poetry too~~    \n~~TODO: Create a python package around the Matlab package (the base files) using Poetry~~  \n~~TODO: Formatting/Linting/Coverage~~  \n~~TODO: Choose between Pytest an Unittest~~  \n~~TODO: Automate black, isort, pylint, coverage, pytest on build or push. - just have to finish coverage~~  \n~~TODO: Auto docstring generating? -- used autodocstring extension for vscode~~  \n~~TODO: How to autobuild the base image the CI/CD will work with - could not be done~~  \n\nFull Documentation can be found [here](https://cabreratoxy.github.io/pyOPERA/)\n',
    'author': 'Manuel Cabrera',
    'author_email': 'cabrera.manuel555@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
