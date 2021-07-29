import unittest
from paypalcheckoutsdk.orders import OrdersAuthorizeRequest
from tests.test_harness import TestHarness

class OrdersAuthorizeTest(TestHarness):
    def build_request_body(self):
        return {}

    def testOrdersAuthorizeTest(self):
        self.skipTest("Tests that use this class must be ignored when run in an automated environment because executing an order will require approval via the executed payment's approve url")
        request = OrdersAuthorizeRequest("ORDER-ID")
        request.request_body(self.build_request_body())

        response = self.client.execute(request)
        self.assertEqual(201, response.status_code)
        self.assertIsNotNone(response.result)

if __name__ == "__main__":
    unittest.main()
