import unittest
import json
from paypalcheckoutsdk.payments import AuthorizationsGetRequest
from tests.test_harness import TestHarness

class AuthorizationsGetTest(TestHarness):

    def testAuthorizationsGetTest(self):
        self.skipTest( "Tests that use this class must be ignored when run in an automated environment because executing an order will require approval via the executed payment's approve url")
        request = AuthorizationsGetRequest('ORDER-ID')
        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

if __name__ == "__main__":
    unittest.main()
