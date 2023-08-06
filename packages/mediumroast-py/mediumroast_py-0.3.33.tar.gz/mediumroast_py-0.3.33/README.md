# Introduction
This is the Python Software Development Kit (SDK) for the mediumroast.io.  Internal tooling from Mediumroast, Inc. uses this SDK, so it will always be a first class citizen. Specifically, we build tools requiring ETL (Extract, Transform and Load), Machine Learning and Natural Language Processing (NLP) with this SDK. As appropriate examples illustrating various capabilities of the SDK can be found in the `mediumroast_examples/` directory of this package. 

## Current status
This SDK mirrors the capabilities of the mediumroast.io application server.  Therefore it is fully functional mapping to the capabilities aavailable from the server.  Specifically this means the SDK is capable of:
1. Creating interaction, company, study and user objects
2. Reporting on or listing interaction, company, study and user objects
3. Transforming raw inputs into respective objects.
4. Ingesting metadata from S3 buckets, provided they match a file name specification, into raw inputs that can be transformed.
Many of these functionalities have example implementations that enable the developer to understand how to use the SDK.  Also the file name specification can be found in the github [mediumroast_examples directory](https://github.com/mediumroast/mediumroast_py/tree/main/mediumroast_examples) of the repository for mediumroast_py.

## The Examples
To illustrate how to interact programmatically with the mediumroast.io application several examples have been created to make it easier for developers to interact with the system.  The scope of the examples, over time, will include all aspects of the SDK to speed up 3rd party development processes.  This means that over time examples for all apsects of the SDK will be produced and made available under the Apache Software License.  As with anything in the SDK if you run into problems please make sure that you raise an [issue](https://github.com/mediumroast/mediumroast_py/issues) in the repository.  More detail on the examples can be found within the [examples directory](https://github.com/mediumroast/mediumroast_py/tree/main/mediumroast_examples) of this repository.

# Installation
Since the package is under heavy development please check in often and upgrade frequently.

## Installation
This package is available on PyPi and can be installed via pip use: `pip install mediumroast_py`

## Upgrade
You can perform an upgrade using pip: `pip install mediumroast_py --upgrade`

## Availability of mediumroast_examples
Installation through pip from [PyPi](https://pypi.org/project/mediumroast-py/) the examples will be installed in `dist-packages/mediumroast_examples`. For example if you're using Python 3.8 with `dist-packages` kept in `/usr/local` then this would be the path for the examples: `/usr/local/lib/python3.8/dist-packages/mediumroast_examples`.

# Structure of the repository
The following structure is available for the Python SDK, as new SDK implementations are created additional top level directories will be created.
```
mediumnroast_py/
      mediumroast_examples/
      mediumroast_py/
            api/
            extractors/
            transformers/
            helpers.py
      project.toml
      README.md
      LICENSE
```