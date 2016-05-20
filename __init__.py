import requests


class ForecastApp(object):
    def __init__(self, account_id, auth_token, protocol="https",
                 host="api.forecastapp.com"):
        self.account_id = account_id
        self.auth_token = auth_token
        self.protocol = protocol
        self.host = host

    def projects(self):
        return self._call('/projects')['projects']

    def people(self):
        return self._call('/people')['people']

    def clients(self):
        return self._call('/clients')['clients']

    def assignments(self):
        return self._call('/assignments')['assignments']

    def milestones(self):
        return self._call('/milestones')['milestones']

    def _call(self, url):
        headers = {'Authorization': 'Bearer %s' % self.auth_token,
                   'Forecast-Account-ID': '%s' % self.account_id}

        req = requests.get('%s://%s%s' % (self.protocol,
                                          self.host,
                                          url),
                           headers=headers)
        return req.json()
