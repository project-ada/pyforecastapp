# PyForecastApp

Python API for accessing ForecastApp (http://www.forecastapp.com).

## Installation

```
pip install pyforecastapp
```

## Usage

Standard authentication:

```
from pyforecastapp import ForecastApp

api = ForecastApp('<account-id>','<email>', '<password>')
for p in api.clients():
    print p
```

Personal Access Token authentication (see http://help.getharvest.com/api-v2/authentication-api/authentication/authentication/#personal-access-tokens):

```
from pyforecastapp import ForecastApp

api = ForecastApp('<account-id>', auth_token='<personal access token>')
for p in api.clients():
    print p
```


## Running the tests

```
pip install -r requirements-dev.txt
python -m pyforecastapp.tests
```
