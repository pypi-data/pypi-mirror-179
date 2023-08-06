# Introduction

Python client for the ALSI/AGSI APIs

Documentation of the API can be found on [GIE's website](https://www.gie.eu/transparency-platform/GIE_API_documentation_v007.pdf)

Documentation of the client API can be found on: <https://roiti-ltd.github.io/gie-py/>

### Installation

```sh
python -m pip install roiti-gie
```

### Usage

The package is split in two clients:

1. GieRawClient: Returns data in raw Python Dict.
2. GiePandasClient: Returns parsed data in the form of a pandas DataFrame.

```python
import asyncio
import os

from roiti.gie import GiePandasClient


async def main():
    """
    The following methods return pandas DataFrame, however you can use the
    raw client "raw_client = GieRawClient(api_key=Your API key)" and you will get the results as
    Python dictionaries.

    NOTE that every method available for AGSI is also available for ALSI
    """

    API_KEY = os.getenv("API_KEY")
    pandas_client = GiePandasClient(api_key=API_KEY)

    # You can specify the country, start date, end date, size (the number of results) in order to get country storage
    await pandas_client.query_country_agsi_storage("AT", start="2020-01-01", end="2022-07-10", size=60)

    # You can run the query without any parameters (in order to get all countries result)
    await pandas_client.query_country_alsi_storage()

    # You can use this query in order to get all AGSI/ALSI EICs (Energy Identification Code)
    await pandas_client.query_alsi_eic_listing()

    # Query which lists all the ALSI/AGSI news (without params)
    await pandas_client.query_alsi_news_listing()

    # Query which lists the news for a specific country (using the url code)
    await pandas_client.query_alsi_news_listing(43419)

    # Query which lists the data for a current facility storage (provide the storage name and params)
    await pandas_client.query_agsi_facility_storage("ugs_haidach_astora", start="2022-10-10")

    # You can list the data for a current storage only using its name
    await pandas_client.query_alsi_facility_storage("dunkerque")

    # Query which lists the data for a current company (also date and size are by choice)
    await pandas_client.query_agsi_company("astora", size=60)
    await pandas_client.query_alsi_company("dunkerque_lng", size=200)

    # Query which lists the unavailability for a current country (country name, date, size are optional)
    await pandas_client.query_agsi_unavailability("GB", size=60)
    await pandas_client.query_agsi_unavailability()
    await pandas_client.query_alsi_unavailability("FR")

    await pandas_client.close_session()


# set_event_loop_policy method is used in order to avoid EventLoopError for Windows
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
```

### Running unit tests

Tell pytest where to look for unit tests and create env for ALSI API key

- On Unix

  ```sh
  export PYTHONPATH=./src/roiti
  export API_KEY='<API_KEY>'
  ```

- On Windows

  ```powershell
  $env:PYTHONPATH='./src/roiti'
  $env:API_KEY='<API_KEY>'
  ```

Run unit tests in coverage mode

```sh
python -m pytest ./tests --import-mode=append --cov
```

### Contributing

Set up your working environment:

1. Create virtual environment

   ```sh
   python -m venv venv
   ```

2. Activate the virtual environment

   - On UNIX system

     ```sh
     source venv/bin/activate
     ```

   - On Windows system

     ```powershell
     ./venv/Scripts/activate
     ```

Install required packages:

```sh
python -m pip install -r requirements.txt -r requirements-dev.txt
```

Bumping the package version after making changes:

```sh
bumpversion major|minor|patch|build
```

### Aknowledgements

- Many thanks to the [entsoe-py](https://github.com/EnergieID/entsoe-py) library for serving as inspiration for this library.

- [Frank Boerman](https://github.com/fboerman) and his [GIE repository](https://github.com/fboerman/gie-py), from which we copied the lookup function ideas.
