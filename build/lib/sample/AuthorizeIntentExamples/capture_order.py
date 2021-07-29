from paypalcheckoutsdk.payments import AuthorizationsCaptureRequest
from sample.paypal_client import PayPalClient
import json


class CaptureOrder(PayPalClient):
    
    """Sample request body to Capture Authorization. This can be updated with the required fields as per need."""
    @staticmethod
    def build_request_body():
        return {}

    """This function can be used to capture an approved authorization. Valid authorization id should be passed as an argument to this function."""
    def capture_order(self, authorization_id, debug=False):
        """Method to capture order using authorization_id"""
        request = AuthorizationsCaptureRequest(authorization_id)
        request.request_body(self.build_request_body())
        response = self.client.execute(request)
        if debug:
            print 'Status Code: ', response.status_code
            print 'Status: ', response.result.status
            print 'Capture ID: ', response.result.id
            print 'Links: '
            for link in response.result.links:
                print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
            json_data = self.object_to_json(response.result)
            print "json_data: ", json.dumps(json_data,indent=4)
        return response

"""This is the driver function which invokes the capture order function with valid authorization id to capture.
 auth_id value should be replaced with an valid authorization id"""
if __name__ == "__main__":
    auth_id = '<<REPLACE-WITH-VALID-AUTHORIZATION-ID>>'
    CaptureOrder().capture_order(auth_id, debug=True)
