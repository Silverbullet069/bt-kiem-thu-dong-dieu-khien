# bt-kiem-thu-dong-dieu-khien

> Source code for Control Flow Testing assignments

## Table of contents:
1.  [How to use](#how-to-use)
2.  [Requirements](#requirements)
3.  [Installation](#installation)
4.  [Running Tests](#running-tests)
5.  [Generate Reports](#generate-reports)

## How to use
### Using pre-generated test results
You will use existed test results that I have pre-generated for you. You only need to:

1. Open HTML reports in ```html-report``` folder using Live Server or something else.
2. Open JSON reports in ```json-report``` folder using any text editors.

If that's the case for you, you can stop reading from here, skip to how to [clone this repository](#clone-this-repository).

### Or, generate your own test results
You will generate your own test results, which required you to continue reading.

## Requirements
[**Python**](https://docs.python.org/3.10/) (==v3.10.12)

[**unittest**](https://docs.python.org/3/library/unittest.html)

[**Coverage.py**](https://coverage.readthedocs.io/en/7.3.2/) (==v7.3.2)

## Installation

### Clone this repository
```sh
git clone --depth 1 https://github.com/Silverbullet069/bt-kiem-thu-dong-dieu-khien.git
cd bt-kiem-thu-dong-dieu-khien
```

### Create a virtual environment 
> Note: this is optional, you could install directly into your global environment but that's not recommended.
```sh
pip install virtualenv venv
pip list
python3 -m venv testing-cfg
source testing-cfg/bin/activate
```
If you ran the code successfully, **(testing-cfg)** will appear in your command prompt.

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

## Running Tests

### Run unittest module, without using Coverage.py
1. Run all tests at once
```sh
python3 -m unittest -v test.py
```

2. Run individual test, one-by-one
```sh
python3 -m unittest -v test.TestControlFlow.test_1
```
```test```: our custom module name
```TestControlFlow```: the class that inherits ```unittest.TestCase``` class
```test_1```: the method that corresponds to a unit test.

### Using Coverage.py to run individual test

```sh
coverage run -m --branch --context=notatriangle --data-file=test1.coverage unittest test.TestControlFlow.test_1
```
```coverage run```: generate a coverage file that measure code execution

```--branch```: include branch coverage

```--context```: add context label to record for this coverage run

```--data-file```: write coverage report to the specified file. Without specifed, *.coverage* is the default

```test.TestControlFlow.test_1```: only run test_1 method, defined in TestControlFlow class

This only ran test case 1, to check whether the input give a triangle or not.

This outputs a file called ```test1.coverage```

### Combine results of multiple test results
After running the remaining 3 unit tests, now we have ```test1.coverage```, ```test2.coverage```, ```test3.coverage```, ```test4.coverage``` in our possessions

```sh
coverage combine --keep --data-file=test-combine.coverage *.coverage
```
```coverage combine```: combine data from multiple coverage files into a single file representing the union of the data.

```--keep```: DO NOT delete the individual coverage file after combined

```--data-file```: write coverage report to the specified file, .coverage is the default

```*.coverage```: substitude for all coverage file in the current directory.

This outputs a file called ```test-combine.coverage```

## Generate reports

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
