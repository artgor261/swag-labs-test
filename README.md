# swag-labs-test

## Install

1. Download this repo on your system
2. Create virtual environment in project folder: `python -m venv <venv_name>`
3. Activate created venv in `cmd`: `<venv_name>/Scripts/activate.bat`
4. Install all dependecies: `pip install -r requirements.txt`
5. Install `allure`. Instructions are here: https://allurereport.org/docs/install-for-windows/

## Usage

1. Switch to tests folder in project dir: `cd Path/To/Project/Dir/tests`
2. Print the following command: `python -m pytest -s --alluredir allure-results`
3. Input browser's name and version
4. Serve allure report: `allure serve allure-results`
