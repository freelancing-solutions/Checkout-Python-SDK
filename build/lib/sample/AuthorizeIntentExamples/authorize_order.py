from sample import PayPalClient
from paypalcheckoutsdk.orders import OrdersAuthorizeRequest
import json

class AuthorizeOrder(PayPalClient):
    
    """Sample request body to Authorize Order. This can be updated with the required fields as per need."""
    @staticmethod
    def build_request_body():
        return {}

    """This function can be used to authorize an approved order. Valid authorized order id should be passed as an argument to this function."""
    def authorize_order(self, order_id, debug=False):
        """Method to authorize order using order_id"""
        request = OrdersAuthorizeRequest(order_id)
        request.prefer("return=representation")
        request.request_body(self.build_request_body())
        response = self.client.execute(request)
        if debug:
            print 'Status Code: ', response.status_code
            print 'Status: ', response.result.status
            print 'Order ID: ', response.result.id
            print 'Authorization ID:', response.result.purchase_units[0].payments.authorizations[0].id
            print 'Links:'
            for link in response.result.links:
                print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
            print 'Authorization Links:'
            for link in response.result.purchase_units[0].payments.authorizations[0].links:
                print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
            print "Buyer:"
            print "\tEmail Address: {}\n\tPhone Number: {}".format(response.result.payer.email_address,
                                                                   response.result.payer.phone.phone_number.national_number)
            json_data = self.object_to_json(response.result)
            print "json_data: ", json.dumps(json_data,indent=4)
        return response

"""This is the driver function which invokes the authorize_order function with valid approved order id to authorize
   an sample order. order_id value should be replaced with an valid approved order id"""
if __name__ == "__main__":
    order_id = '<<REPLACE-WITH-VALID-APPROVED-ORDER-ID>>'
    AuthorizeOrder().authorize_order(order_id, debug=True)
