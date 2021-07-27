from sample import PayPalClient
import json
from paypalcheckoutsdk.orders import OrdersCreateRequest
from paypalhttp.http_error import HttpError


class CreateError(PayPalClient):

    def create_error_1(self):
        """
        Body has no required parameters (intent, purchase_units)
        """
        body = {}
        request = OrdersCreateRequest()
        request.request_body(body)
        print ("Request Body:", body, "\n")
        print ("Response:")
        try:
            response = self.client.execute(request)
        except HttpError as h:
            print("Status Code:", h.status_code)
            print(self.pretty_print(h.message))

    def create_error_2(self):
        """
        Body has invalid parameter value for intent
        """
        body = \
            {
                "intent": "INVALID",
                "purchase_units": [
                    {
                        "amount":
                        {
                            "currency_code": "USD",
                            "value": "100.00"
                        }
                    }
                ]
            }
        request = OrdersCreateRequest()
        request.request_body(body)
        print( "Request Body:\n", json.dumps(body, indent=4), "\n")
        print ("Response:")
        response = ""
        try:
            response = self.client.execute(request)
        except HttpError as h:
            print ("Status Code: ", h.status_code)
            print (h.message)


print("Calling create_error_1 (Body has no required parameters (intent, purchase_units))")
CreateError().create_error_1()

print("\nExecuting create_error_2 (Body has invalid parameter value for intent)")
CreateError().create_error_2()
