from __future__ import unicode_literals
from . import ForecastApp
import json
from google.appengine.api import urlfetch


class ForecastAppAppengine(ForecastApp):
    """
    Requests doesn't work on Appengine so use urllib2
    """

    def __init__(self, account_id, auth_token, protocol='https', host='api.forecastapp.com'):
        self.protocol = protocol
        self.host = host
        self.account_id = account_id
        self.auth_token = auth_token

    def _call(self, endpoint):
        url = '{protocol}://{host}{endpoint}'.format(
            protocol=self.protocol,
            host=self.host,
            endpoint=endpoint
        )
        response = urlfetch.fetch(
            url,
            headers={
                'Forecast-Account-ID': str(self.account_id),
                'Authorization': 'Bearer {}'.format(self.auth_token),
            }
        )
        return json.loads(response.content)
