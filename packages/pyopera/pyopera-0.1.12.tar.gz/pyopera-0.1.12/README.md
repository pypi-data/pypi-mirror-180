# pyOPERA
[![asv](http://img.shields.io/badge/benchmarked%20by-asv-blue.svg?style=flat)]  
Full python implementation of the NIH OPERA suite of models  
docker run -it -v %cd%:/app --rm pyopera_pyopera /bin/bash  
docker compose -f docker-compose.yml build  
docker run --rm pyopera_pyopera ~/.local/share/pypoetry/venv/bin/poetry run coverage run -m pytest tests  
docker build -t cabreratoxy/pyopera:0.0.1 .  

```
poetry run python -m pip install -r requirements.txt  
poetry run black . --exclude={docs/,libOPERA_Py/,.asv/}  
poetry run isort . --skip={docs/,libOPERA_Py/,.asv/}  
poetry run pylint $(find pyopera -name "*.py" | xargs)  
poetry run pytest tests    
poetry run coverage run --source pyopera -m pytest  
poetry run coverage report --skip-empty --fail-under=85  
poetry build  
poetry config repositories.testpypi https://test.pypi.org/legacy/  

docker run --rm pyopera_pyopera /bin/bash -c 'poetry run coverage run -m pytest tests'   
if [ git diff --exit-code Dockerfile ]; then dockerfiles/build_docker.sh; fi
```



TODO: Test TestPypi package locally  
TODO: Benchmarking with airspeed velocity (struggling to make it work without a setup.py)  
TODO: Don't repeat the library name in the Dockerfile  
~~TODO: Find out how to trigger the docker image build step when the file changes~~
TODO: Start adding the wrapper code and files - in progress  
TODO: Add actual documentation in this readme  
TODO: Automate versioning  
~~TODO: Struggling to run commands inside Docker from the host, will run commands from inside container for now~~  
~~TODO: Add the original library folder into the folder structure  (manual for now, eventually upload it as a build artifact or similar)~~  
~~TODO: poetry is not including the additional files with the library~~  
~~TODO: Fully install poetry in the container (maybe use the long name as a variable for now)~~  
~~TODO: Create CI/CD for package in TestPypi and the prod Pypi (CircleCI maybe?)~~  
~~TODO: Documentation using Sphinx (make sure original repo/builders are credited)~~  
~~TODO: Auto semantic versioning with poetry too~~    
~~TODO: Create a python package around the Matlab package (the base files) using Poetry~~  
~~TODO: Formatting/Linting/Coverage~~  
~~TODO: Choose between Pytest an Unittest~~  
~~TODO: Automate black, isort, pylint, coverage, pytest on build or push. - just have to finish coverage~~  
~~TODO: Auto docstring generating? -- used autodocstring extension for vscode~~  
~~TODO: How to autobuild the base image the CI/CD will work with - could not be done~~  

Full Documentation can be found [here](https://cabreratoxy.github.io/pyOPERA/)
