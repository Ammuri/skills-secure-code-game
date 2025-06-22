'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAXIMUM_ITEM_AMOUNT = 10_000
MAX_ITEM_QUANTITY = 100
MIN_ITEM_QUANTITY = 0
MAXIMUM_PAYABLE_AMOUNT = 1_000_000

def validorder(order: Order):
    payments = Decimal('0')
    expenses = Decimal('0')

    for item in order.items:
        if item.type == 'payment':
            if -MAXIMUM_ITEM_AMOUNT <= item.amount <= MAXIMUM_ITEM_AMOUNT:
                payments += Decimal(str(item.amount))
        elif item.type == 'product':
            if isinstance(item.quantity, int) and MIN_ITEM_QUANTITY < item.quantity <= MAX_ITEM_QUANTITY and \
            0 < item.amount <= MAXIMUM_PAYABLE_AMOUNT:
                expenses += Decimal(str(item.amount)) * item.quantity
        else:
            return "Invalid item type: %s" % item.type

    #Checking the total amount payable against the maximum payable amount
    if abs(payments) > MAXIMUM_PAYABLE_AMOUNT or abs(expenses) > MAXIMUM_PAYABLE_AMOUNT:
        return "Total amount payable for an order exceeded"

    if payments != expenses:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, payments - expenses)
    else:
        return "Order ID: %s - Full payment received!" % order.id