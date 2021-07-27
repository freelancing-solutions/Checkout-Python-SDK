from sample import PayPalClient
from paypalcheckoutsdk.orders import OrdersCaptureRequest
import json


class CaptureOrder(PayPalClient):
        
    """this is the sample function performing payment capture on the order.
    Approved Order id should be passed as an argument to this function"""

    def capture_order(self, order_id, debug=False):
        """Method to capture order using order_id"""
        request = OrdersCaptureRequest(order_id)
        response = self.client.execute(request)
        if debug:
            print('Status Code: ', response.status_code)
            print('Status: ', response.result.status)
            print('Order ID: ', response.result.id)
            print('Links: ')
            for link in response.result.links:
                print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
            print('Capture Ids: ')
            for purchase_unit in response.result.purchase_units:
                for capture in purchase_unit.payments.captures:
                    print('\t', capture.id)
            print("Buyer:")
            print("\tEmail Address: {}\n\tName: {}\n\tPhone Number: {}".format(response.result.payer.email_address,
                                                                           response.result.payer.name.given_name + " " + response.result.payer.name.surname,
                                                                           response.result.payer.phone.phone_number.national_number))
            json_data = self.object_to_json(response.result)
            print("json_data: ", json.dumps(json_data,indent=4))
        return response


"""This is the driver function which invokes the capture order function. 
Order Id value should be replaced with the approved order id. """
if __name__ == "__main__":
    order_id = '8G344453R30787301'
    CaptureOrder().capture_order(order_id, debug=True)
