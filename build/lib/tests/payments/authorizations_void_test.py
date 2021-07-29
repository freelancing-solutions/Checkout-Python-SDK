import unittest
import json
from paypalcheckoutsdk.payments import AuthorizationsVoidRequest
from tests.test_harness import TestHarness

class AuthorizationsVoidTest(TestHarness):

    def testAuthorizationsVoidTest(self):
        self.skipTest("Tests that use this class must be ignored when run in an automated environment because executing an order will require approval via the executed payment's approve url")
        request = AuthorizationsVoidRequest('ORDER-ID')

        response = self.client.execute(request)
        self.assertEqual(204, response.status_code)

if __name__ == "__main__":
    unittest.main()
