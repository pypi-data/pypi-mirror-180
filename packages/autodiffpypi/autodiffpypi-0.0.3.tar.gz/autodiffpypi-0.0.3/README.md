[![.github/workflows/coverage.yml](https://code.harvard.edu/CS107/team12/actions/workflows/coverage.yml/badge.svg)](https://code.harvard.edu/CS107/team12/actions/workflows/coverage.yml)
[![.github/workflows/tests.yml](https://code.harvard.edu/CS107/team12/actions/workflows/tests.yml/badge.svg)](https://code.harvard.edu/CS107/team12/actions/workflows/tests.yml)
# team12
Team 12's private repository for CS107's final project. 

## Documentation
Our library's [documentation](https://code.harvard.edu/CS107/team12/blob/main/docs/documentation.ipynb)

## Installation
Install the latest AD library for application usage from PyPi.org with the command `pip install autodiffpypi`.

## Development Setup
For developers interested in contributing to or making changes to the source code, follow the below instructions. Copy the SSH url for the Github repo, then follow the below steps in your terminal.

1. `git clone <repo>`
2. `cd <repo>`
3. `pip install virtualenv`
4. `python -m venv autodiff_venv`
5. `source autodiff_venv/bin/activate`
6. `pip install -r requirements.txt`

## Running the tests
Run the command `pytest` to run all test suites. Provide an optional file parameter, e.g. pytest tests/test_dual_number.py to run the specified test.
To view a coverage report, run the following command `python3 -m pytest --cov=src/AutoDiffPy --cov-fail-under=90`.

## Broader Impact
Our software provides a tool for users to efficiently compute derivatives and jacobian values. As a public package lisenced under the MIT License, this tool may be used in a number of areas ranging from scientific research, personal projects, and industry applications. While our package provides similar functionality to pre-existing AutoDiff software, releasing our own version still contributes to the public domain by providing a unique implementation and framework that others may find particularly suitable to their use case. 

As the authors of this package, there are a few consequences important to note. Firstly, while our library has undergone unit and integration testing, we cannot guarantee full correctness in all cases, especially under the conditions of large-scale usage. As with most software, this package may be subject to further iteration & fixes. There may be significant consequences if this AutoDiff library is used without user-written tests; therefore we expect any users to take responsibility for ensuring that their applications meet their expectations and that integrating this AutoDiff package does not make them susceptible to incorrect or unexpected results.

## Software Inclusivity
The aim of this package is to increase access to Autodifferentiation capabilities, for students, researchers, programmers, and others who find it applicable. Additionally, our code is released on Github to improve visibility of the internal implementation of such libraries. We welcome open-source contributions or suggestions, which can be submitted by forking this repository and creating a pull-request (this pull request can contain a simple txt file for suggestions). Pull requests will be reviewed and approved by the original authors, who may reach out to you for collaboration. As an international team, we are happy to work with individuals of any background including non-native English speakers, and will provide language accomodation if needed. For those who are visually-impaired, an audio recording of this README can be accessed in the below Google Drive link.