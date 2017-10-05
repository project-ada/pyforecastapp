import mock
import unittest

from . import ForecastApp, ForecastAppException


class ForecastAppTestCase(unittest.TestCase):

    def test_auth_token_provided(self):
        # if auth token is provided, email and password are not required
        account_id, auth_token = None, 'foo'
        forecast = ForecastApp(account_id, auth_token=auth_token)
        self.assertEqual(
            forecast.auth_token,
            auth_token
        )

    def test_auth_token_not_provided(self):
        # if auth token is not provided, email and password are required
        account_id = None
        with self.assertRaises(ForecastAppException):
            ForecastApp(account_id)

    def test_auth_token_not_provided_with_params(self):
        account_id, email, password = 'account_id', 'email', 'password'
        with mock.patch.object(ForecastApp, '_get_token') as mock_get_token:
            ForecastApp(account_id, email, password)
            mock_get_token.assert_called_once_with(email, password, account_id)

    # auth_token must be passed below even though we don't care about it
    # to prevent raising a ForecastAppException

    def test_protocol_default(self):
        self.assertEqual(
            ForecastApp('account_id', auth_token='foo').protocol, 'https'
        )

    def test_protocol_override(self):
        self.assertEqual(
            ForecastApp('account_id', auth_token='foo', protocol='http').protocol, 'http'
        )

    def test_host_default(self):
        self.assertEqual(
            ForecastApp('account_id', auth_token='foo').host, 'api.forecastapp.com'
        )

    def test_host_override(self):
        self.assertEqual(
            ForecastApp('account_id', auth_token='foo', host='foobar').host, 'foobar'
        )

    def test_account_is_is_set(self):
        self.assertEqual(
            ForecastApp('account_id', auth_token='foo').account_id, 'account_id'
        )


if __name__ == '__main__':
    unittest.main()
