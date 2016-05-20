# PyForecastApp
Python API for accessing ForecastApp (http://www.forecastapp.com).

## Usage
```
from pyforecastapp import ForecastApp

api = ForecastApp('<account-id>','<email>', '<password>')
for p in api.clients():
    print p
```

