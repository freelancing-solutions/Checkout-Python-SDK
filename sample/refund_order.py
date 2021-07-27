from sample import PayPalClient
from paypalcheckoutsdk.payments import CapturesRefundRequest
import json


class RefundOrder(PayPalClient):
    """Request body for building refund request. This can be updated with values in case of partial refund. """

    @staticmethod
    def build_request_body():
        """Method to build empty body"""
        return \
            {
                "amount": {
                    "value": "20.00",
                    "currency_code": "USD"
                }
            }

    """Below function can be used to refund an capture. Valid capture id should be passed as an argument."""

    def refund_order(self, capture_id, debug=False):
        """Method to refund order using capture_id"""
        request = CapturesRefundRequest(capture_id)
        request.prefer("return=representation")
        request.request_body(self.build_request_body())
        response = self.client.execute(request)
        if debug:
            print('Status Code: {}'.format(response.status_code))
            print('Status: {}'.format(response.result.status))
            print('Order ID:{}'.format(response.result.id))
            print('Links:')
            for link in response.result.links:
                print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
            json_data = self.object_to_json(response.result)
            print("json_data: {}".format(json.dumps(json_data, indent=4)))
        return response


"""This is the driver function which invokes the refund capture function. Capture Id value should be 
replaced with the valid capture id. """
if __name__ == "__main__":
    capture_id = '<<REPLACE-WITH-VALID-CAPTURE-ID>>'
    RefundOrder().refund_order(capture_id, debug=True)
