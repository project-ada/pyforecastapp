# PyForecastApp
Python API for accessing ForecastApp (http://www.forecastapp.com).

## Usage
```
from pyforecastapp import ForecastApp

api = ForecastApp('<client-id>','<auth-token>')
for p in api.clients():
    print p
```

