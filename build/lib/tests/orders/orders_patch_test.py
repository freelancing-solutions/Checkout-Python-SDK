import unittest
from paypalcheckoutsdk.orders import OrdersPatchRequest, OrdersGetRequest
from tests.test_harness import TestHarness
from tests.orders.orders_create_test import create_order


class OrdersPatchTest(TestHarness):
    def build_request_body(self):
        return [
            {
                "op": "add",
                "path": "/purchase_units/@reference_id=='test_ref_id1'/description",
                "value": "added_description"
            },
            {
                "op": "replace",
                "path": "/purchase_units/@reference_id=='test_ref_id1'/amount",
                "value": {
                    "currency_code": "USD",
                    "value": "200.00"
                }

            }
        ]

    def testOrdersPatchTest(self):
        response = create_order(self.client)
        order_id = response.result.id
        request = OrdersPatchRequest(order_id)
        request.request_body(self.build_request_body())

        response = self.client.execute(request)
        self.assertEqual(204, response.status_code)

        response = self.client.execute(OrdersGetRequest(order_id))
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

        self.assertIsNotNone(response.result.id)
        self.assertIsNotNone(response.result.purchase_units)
        self.assertEqual(1, len(response.result.purchase_units))

        first_purchase_unit = response.result.purchase_units[0]
        self.assertEqual("test_ref_id1", first_purchase_unit.reference_id)
        self.assertEqual("USD", first_purchase_unit.amount.currency_code)
        self.assertEqual("200.00", first_purchase_unit.amount.value)
        self.assertEqual("added_description", first_purchase_unit.description)

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
