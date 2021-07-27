from sample import PayPalClient
from paypalcheckoutsdk.orders import OrdersGetRequest
from sample.CaptureIntentExamples.create_order import CreateOrder
import json


# noinspection DuplicatedCode
class GetOrder(PayPalClient):
    """This function can be used to retrieve an order by passing order id as argument"""

    def get_order(self, order_id):
        """Method to get order"""
        request = OrdersGetRequest(order_id)
        response = self.client.execute(request)
        print('Status Code: ', response.status_code)
        print('Status: ', response.result.status)
        print('Order ID: ', response.result.id)
        print('Intent: ', response.result.intent)
        print('Links:')
        for link in response.result.links:
            print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
        print('Gross Amount: {} {}'.format(response.result.purchase_units[0].amount.currency_code,
                                           response.result.purchase_units[0].amount.value))
        json_data = self.object_to_json(response.result)
        print("json_data: ", json.dumps(json_data, indent=4))


"""This is the driver function which invokes the get_order function with order id to retrieve
   an sample order. For the order id, we invoke the create order to create an new order and then we are using 
   the newly created order id for retrieving the order"""
if __name__ == '__main__':
    createResponse = CreateOrder().create_order()
    order = createResponse.result
    GetOrder().get_order(order.id)
