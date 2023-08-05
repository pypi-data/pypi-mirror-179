# IRIS-validator 

iris-validator is a small python module for validation
stationxml files against the IRIS StationXML Validation Rules found at:

https://github.com/iris-edu/stationxml-validator/wiki/StationXML-Validation-Rule-List

It has a limited API and a command-line script


## Installation

### Requirements

    obspy >= 1.2

These requirements should be automatically installed for you (see below).

### Install

Easy install from pypi:

    >pip install iris-validator

Alternatively, you can
Clone the repository and install:

    >git clone https@gitlab.isti.com:mhagerty/iris-validator.git 
    >cd iris-validator
    >pip install .


### Usage:

Once you have installed it, you should be able to run it as a python module from any directory.

iris-validator can either test your own xml against the iris validation
rules (--infile /path/to/your.xml) or it can run through a suite of
tests that test known xml snippets against each rule (--run-tests).
The tests are mainly there to confirm that the iris rules are being
applied correctly (e.g., to test the code itself).

    >iris-validator

    usage: iris-validator [-h] (--infile INFILE | --run-tests)

    required arguments: // One of these is required
      --infile INFILE       // path-to StationXML file, e.g., --infile=/path/to/foo.xml
      --run-tests           // Run IRIS Validator Test Files

    > iris-validator --run-tests
    Check file:F1_101.xml against Rule:101
    SUCCESS: xmlfile=[F1_101.xml] FAILED as expected
    Check file:F1_110.xml against Rule:110
    SUCCESS: xmlfile=[F1_110.xml] FAILED as expected
    Check file:F2_110.xml against Rule:110 
    SUCCESS: xmlfile=[F2_110.xml] FAILED as expected
    ...
    Check file:P1_112.xml against Rule:112
    SUCCESS: xmlfile=[P1_112.xml] PASSED as expected
    ...
    Check file:F1_422.xml against Rule:422 
    SUCCESS: xmlfile=[F1_422.xml] FAILED as expected
    Check file:F1_423.xml against Rule:423
    SUCCESS: xmlfile=[F1_423.xml] FAILED as expected

#### Additional cmd line options:

    usage: iris-validator [-h] (--infile INFILE | --run-tests)
           [-s STATION] [-c CHANNEL] [-n NETWORK] [-l LOCATION] [-def] [-i IGNORE [IGNORE ...]]

    options:
      -h, --help            show this help message and exit
      -s STATION, --station STATION, --sta STATION
                            Specify a station code, wildcards are allowed
      -c CHANNEL, --channel CHANNEL, --cha CHANNEL
                            Specify a channel code, wildcards are allowed
      -n NETWORK, --network NETWORK, --net NETWORK
                            Specify a network code, wildcards are allowed
      -l LOCATION, --location LOCATION, --loc LOCATION
                            Specify a location code, wildcards are allowed
      -def, --seismic-only, --seismic_only
                            Only scan default_seismic_channels in: {[BEHSG][HNL][123ENZ]}
      -i IGNORE [IGNORE ...], --ignore IGNORE [IGNORE ...]
                            Specify list of rule codes to ignore

For example, to ignore specific rule checks you can do:

      >iris-validator --infile /path/to/file.xml -i 321,420 421 422 ...

-n, -s, -c, -l flags can be used to select *only* these channels for
scanning

### API
To use the module from within your own python script, follow the example
below:

    from iris_validator import stationxml_validator

    validator = stationxml_validator('path/to/some/stationxml.xml')

    validator.validate_inventory()

    print("[ERRORS]:\n")
    for msgs in validator.errors:
        for i, msg in enumerate(msgs):
            if i == 0:
                print(msg)
            else:
                print("%7s %s" % (' ', msg))

    print("\n[WARNINGS]:\n")
    for msgs in validator.warnings:
        for i, msg in enumerate(msgs):
            if i == 0:
                print(msg)
            else:
                print("%7s %s" % (' ', msg))

Note some other things you can do include:

    validator.validate_rule('420')          // You can test your stationxml file against one rule at a time
