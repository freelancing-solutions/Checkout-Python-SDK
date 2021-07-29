import unittest
from paypalcheckoutsdk.orders import OrdersCreateRequest
from tests import TestHarness


class OrdersCreateTest(TestHarness):
    def testOrdersCreateTest(self):
        response = create_order(self.client)

        self.assertEqual(201, response.status_code)
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


def create_order(client):
    request = OrdersCreateRequest()
    request.prefer("return=representation")
    body = {
        "intent": "CAPTURE",
        "purchase_units": [{
            "reference_id": "test_ref_id1",
            "amount": {
                "value": "100.00",
                "currency_code": "USD"
            }
        }],
        "redirect_urls": {
            "cancel_url": "https://example.com/cancel",
            "return_url": "https://example.com/return"
        }
    }
    request.request_body(body)
    return client.execute(request)


if __name__ == "__main__":
    unittest.main()
