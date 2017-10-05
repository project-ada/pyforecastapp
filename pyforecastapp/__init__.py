import re
import requests


class ForecastApp(object):
    """
    Supports both standard and Personal Access Token methods of authication

    (1) Standard - requires email and password.  This method will attempt to login using the credentials in order
    to fetch the auth token

    e.g. ForecastApp('my account id', email='my email', password='my password')

    (2) Personal Access Token - see http://help.getharvest.com/api-v2/authentication-api/authentication/authentication/#personal-access-tokens

    e.g. ForecastApp('my account id', auth_token='my personal access token')

    After authentication, usage is the same
    """

    def __init__(self, account_id, email=None, password=None, auth_token=None, protocol="https",
            host="api.forecastapp.com"):
        self.protocol = protocol
        self.host = host
        self.account_id = account_id
        self.auth_token = auth_token

        if self.auth_token is not None:
            # if the user has setup a Personal Access Token, then that's all we need to access the API
            return

        # try to look up the user's token.  To do this we must have their email and password
        if not any(email, password):
            raise ForecastAppException('Both password and email are required to fetch an auth token')

        self.auth_token = self.get_token(email, password, account_id)

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

    def _call(self, endpoint):
        url = '{protocol}://{host}{endpoint}'.format(
            protocol=self.protocol,
            host=self.host,
            endpoint=endpoint
        )
        response = requests.get(
            url,
            headers={
                'Forecast-Account-ID': unicode(self.account_id),
                'Authorization': 'Bearer {}'.format(self.auth_token),
            }
        )
        return response.json()

    def _get_token(self, email, password, account_id):
        with requests.Session() as s:
            try:
                form_request = s.get('https://id.getharvest.com/forecast/sign_in')
                csrf_token = re.search('name="authenticity_token" value="(.*)"', form_request.text).group(1)
            except:
                raise ForecastAppException("Error authenticating, could not find csrf token")

            data = {
                'authenticity_token': csrf_token,
                'email': email,
                'password': password,
                'product': 'forecast'
            }

            try:
                login_request = s.post('https://id.getharvest.com/sessions', data=data, allow_redirects=True)
                token_request = s.get('https://id.getharvest.com/accounts/%s' % account_id)
                return token_request.url.split('/')[-1]
            except:
                raise ForecastAppException("Error authenticating, could not find authentication token")
