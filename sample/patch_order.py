from paypalcheckoutsdk.orders import OrdersPatchRequest, OrdersGetRequest
from sample import PayPalClient
from sample.AuthorizeIntentExamples import CreateOrder
import json

class PatchOrder(PayPalClient):
    @staticmethod
    def build_request_body():
        """Method to created body for patch order -> list of patches"""
        return \
            [
                {
                    "op": "replace",
                    "path": "/intent",
                    "value": "CAPTURE"
                },
                {
                    "op": "replace",
                    "path": "/purchase_units/@reference_id=='PUHF'/amount",
                    "value": {
                        "currency_code": "USD",
                        "value": "200.00",
                        "breakdown": {
                            "item_total": {
                                "currency_code": "USD",
                                "value": "180.00"
                            },
                            "tax_total": {
                                "currency_code": "USD",
                                "value": "20.00"
                            }
                        }
                    }
                }
            ]

    def patch_order(self, order_id):
        """Method to patch order"""
        request = OrdersPatchRequest(order_id)
        request.request_body(self.build_request_body())
        self.client.execute(request)
        response = self.client.execute(OrdersGetRequest(order.id))
        print('Order ID: ', response.result.id)
        print('Intent: ', response.result.intent)
        print('Links:')
        for link in response.result.links:
            print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
        print ('Gross Amount: {} {}'.format(response.result.purchase_units[0].amount.currency_code,
                                           response.result.purchase_units[0].amount.value))
        json_data = self.object_to_json(response.result)
        print("json_data: ", json.dumps(json_data,indent=4))


if __name__ == "__main__":
    print('Before PATCH:')
    createResponse = CreateOrder().create_order(True)
    order = createResponse.result
    print('\nAfter PATCH (Changed Intent and Amount):', PatchOrder().patch_order(order.id))
