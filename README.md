# bt-kiem-thu-dong-dieu-khien
Source code for Control Flow Testing assignments

## Technologies used
Python v3.10.12

Unittest module

Official documentation: https://docs.python.org/3/library/unittest.html

Coverage.py module, v7.3.2

Official documentation: https://coverage.readthedocs.io/en/7.3.2/

## There are 2 ways to use this repository
### One. Using pre-generated test results
You use existing test results that I have pre-generated for you. You only need to use Live Server or something else to open HTML reports in ```html-report``` folder, use any text editor to view JSON reports in ```json-report``` folder. If that's the case for you, you can stop reading from here, read how to clone this repository, clone it and use it.

### Two. Generated your own test results
You generated your own test results, which required you to continue reading.

## Setup environment

### Clone this repository
```sh
git clone --depth 1 https://github.com/Silverbullet069/bt-kiem-thu-dong-dieu-khien.git
cd bt-kiem-thu-dong-dieu-khien
```

### Create a virtual environment (this is Optional)
```sh
pip install virtualenv venv
pip list
python3 -m venv testing-cfg
source testing-cfg/bin/activate
```
Make sure **(testing-cfg)** appear in your command prompt.

### Install Coverage.py
```sh
pip install coverage
pip list
coverage --version
```

**Note:** after running ```coverage --version```, you have to make sure that *Coverage.py, version 7.3.2 with C extension* appear. If not, and you are running Linux, these modules may be missing so you need to install them
```sh
sudo apt install python3-dev gcc
```

## Testing workflow

### Recall from last assignment: Run unittest module, without Coverage.py
```sh
python3 -m unittest test.py
```

### Using Coverage.py to run individual test
```sh
coverage run -m --branch --context=notatriangle --data-file=test1.coverage unittest test.TestControlFlow.test_1
```
```coverage run```: generate a coverage file that measure code execution

```--branch```: include branch coverage

```--context```: add context label to record for this coverage run

```--data-file```: write coverage report to the specified file, *.coverage* is the default

```test.TestControlFlow.test_1```: only run 1 out of 4 tests

This only ran test case 1, to check whether the input give a triangle or not and produce ```test1.coverage```

### Combine results of multiple test results
```sh
coverage combine --keep --data-file=test-combine.coverage *.coverage
```
```coverage combine```: combine data from multiple coverage files into a single file representing the union of the data.

```--keep```: DO NOT delete the individual coverage file after combined

```--data-file```: write coverage report to the specified file, .coverage is the default

```*.coverage```: substitude for all coverage file in the current directory.

## Create reports
### Text-based, command-line
```sh
coverage report -m --date-file=test1.coverage
```
```coverage report```: report coverage statistics on modules.

```-m```: show the missing lines that aren't being covered.

```--data-file```: write coverage report to the specified file, .coverage is the default

### Web view
```sh
coverage html -d htmlcov-test1 --data-file test1.coverage --title=test1
```
```coverage html```: generated HTML report

```-d```: write HTML report into the specified folder

```--data-file```: write coverage report to the specified file, .coverage is the default

```--title=test1```: specify the title to write into HTML file

### JSON view
```sh
coverage json --data-file=test1.coverage -o test1.json --pretty-print
```
```coverage json```: generated JSON report

```--data-file```: write coverage report to the specified file, .coverage is the default

```-o```: write the JSON report to this file




