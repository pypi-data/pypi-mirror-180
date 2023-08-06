from decimal import Decimal
from src.common.constants.constant import HUNDRED


def convert_to_cents(amount):
    amount = Decimal(str(round(amount, 2)))
    return int(amount * HUNDRED)
