from capture_order import CaptureOrder
from create_order import CreateOrder
from sample.get_order import GetOrder
from sample.refund_order import RefundOrder

response = CreateOrder().create_order()
order_id = ''
print 'Creating Order...'
if response.status_code == 201:
    order_id = response.result.id
    for link in response.result.links:
        print('\t{} link: {}\tCall Type: {}'.format(str(link.rel).capitalize(), link.href, link.method))
    print 'Created Successfully\n'
    print 'Copy approve link and paste it in browser. Login with buyer account and follow the instructions.\nOnce approved hit enter...'
else:
    print 'Link is unreachable'
    exit(1)
raw_input()
print 'Capturing Order...'
capture_id =""
response = CaptureOrder().capture_order(order_id)
if response.status_code == 201:
    print 'Captured Successfully\n'
    print 'Status Code: ', response.status_code
    print 'Status: ', response.result.status
    print 'Order ID: ', response.result.id
    print 'Capture Ids: '
    for purchase_unit in response.result.purchase_units:
        for capture in purchase_unit.payments.captures:
            print '\t', capture.id
            capture_id =capture.id
    print 'Links: '
    for link in response.result.links:
        print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))

print 'Get Order'
response = GetOrder().get_order(order_id)

print 'Refunding Order...'
response = RefundOrder().refund_order(capture_id)
if response.status_code == 201:
    print 'Refunded Successfully\n'
    print 'Status Code: ', response.status_code
    print 'Status: ', response.result.status
    print 'Refund ID: ', response.result.id
    print 'Links: '
    for link in response.result.links:
        print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))





