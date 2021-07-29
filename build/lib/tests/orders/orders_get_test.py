import unittest
from paypalcheckoutsdk.orders import OrdersGetRequest
from tests.test_harness import TestHarness
from tests.orders.orders_create_test import create_order

class OrderGetTest(TestHarness):

    def testOrderGetRequestTest(self):
        response = create_order(self.client)

        request = OrdersGetRequest(response.result.id)
        response = self.client.execute(request)

        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

        self.assertIsNotNone(response.result.id)
        self.assertIsNotNone(response.result.purchase_units)
        self.assertEqual(1, len(response.result.purchase_units))

        first_purchase_unit = response.result.purchase_units[0]
        self.assertEqual("test_ref_id1", first_purchase_unit.reference_id)
        self.assertEqual("USD", first_purchase_unit.amount.currency_code)
        self.assertEqual("100.00", first_purchase_unit.amount.value)

        self.assertIsNotNone(response.result.create_time)

        self.assertIsNotNone(response.result.links)

        found_approve = False
        for link in response.result.links:
            if "approve" == link.rel:
                found_approve = True
                self.assertIsNotNone(link.href)
                self.assertEqual("GET", link.method)
        self.assertTrue(found_approve)

        self.assertEqual("CREATED", response.result.status)

if __name__ == "__main__":
    unittest.main()
