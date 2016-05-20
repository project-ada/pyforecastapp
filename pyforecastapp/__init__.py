import requests
import re


class ForecastApp(object):
    def __init__(self, account_id, email, password, protocol="https",
                 host="api.forecastapp.com"):
        self.protocol = protocol
        self.host = host
        self.account_id = account_id
        
        self.auth_token = self._authenticate(email, password, account_id)

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

    def _authenticate(self, email, password, account_id):
        with requests.Session() as s:
            try:
                form_request = s.get('https://id.getharvest.com/forecast/sign_in')
                csrf_token = re.search('name="authenticity_token" value="(.*)"', form_request.text).group(1)
            except:
                print "Error authenticating, could not find csrf token"
                raise

            data = {'authenticity_token': csrf_token,
                    'email': email,
                    'password': password,
                    'product': 'forecast'}

            try:
                login_request = s.post('https://id.getharvest.com/sessions', data=data, allow_redirects=True)
                token_request = s.get('https://id.getharvest.com/accounts/%s' % account_id)
                return token_request.url.split('/')[-1]
            except:
                print "Error authenticating, could not find authentication token"
                raise
