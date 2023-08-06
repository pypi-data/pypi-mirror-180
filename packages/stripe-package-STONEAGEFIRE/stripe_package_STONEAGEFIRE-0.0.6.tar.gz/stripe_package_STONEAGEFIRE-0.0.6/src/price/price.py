import stripe
from src.common.constants.constant import *
from src.common.constants.product import *
from src.common.service import convert_to_cents
from src.exceptions.exception_constants import *

from src.exceptions.exception_handling import *




class StripePrice:

    @staticmethod
    def create_stripe_price(
            stripe_secret_key: str,
            product_id: str,
            currency: str,
            unit_amount: float,
            active: bool = True,
            recurring_interval: str = None,
            recurring_interval_count: int = None,
            metadata: dict = None,
            nickname: str = None) -> dict:
        """
        Create new stripe price for stripe product.

        :type stripe_secret_key: string
        :param stripe_secret_key: Stripe authenticates your API requests using your
                                  account's API keys. Stripe raises an invalid request
                                  error if you don't include a key, and an authentication
                                  error if the key is incorrect or outdated.

        :type product_id: string
        :param product_id: The ID of the product that this price will belong to.

        :type currency: string
        :param currency: Three-letter ISO currency code, in lowercase.
                         Must be a supported currency.

        :type unit_amount: float
        :param unit_amount: :type price_unit_amount: float
        :param price_unit_amount: A positive value or 0 for a free price (rupees, usd, 
                                  etc) representing how much to charge. More than 2 
                                  decimal is rounded to 2 decimal places.

        :type active: boolean
        :param active: Whether the price can be used for new purchases. Defaults to true.

        :type recurring_interval: string
        :param recurring_interval: Specifies billing frequency. 
                                   Either day, week, month or year.

        :type recurring_interval_count: integer
        :param recurring_interval_count: The number of intervals between subscription billings.
                                         For example, interval=month and interval_count=3 bills
                                         every 3 months. Maximum of one-year interval allowed
                                         (1 year, 12 months, or 52 weeks).

        :type metadata: dictionary
        :param metadata: Set of key-value pairs that you can attach to an object. This can 
                         be useful for storing additional information about the object in a 
                         structured format. Individual keys can be unset by posting an empty 
                         value to them. All keys can be unset by posting an empty value to 
                         metadata.

        :type nickname: string
        :param nickname: A brief description of the price, hidden from customers.

        :type: dictionary
        :return: The newly created Price object is returned upon success.
        """
        try:
            if not isinstance(stripe_secret_key, str) \
                    or not isinstance(currency, str) \
                    or not isinstance(product_id, str) \
                    or not isinstance(unit_amount, (int, float)) \
                    or not isinstance(recurring_interval, (str, type(None))) \
                    or not isinstance(recurring_interval_count, (int, str, type(None))):
                raise CoreBadRequest(exception_detail=BAD_REQUEST_MESSAGE,
                                     exception_code=STRIPE_BAD_REQUEST,
                                     method_name=STRIPE_CREATE_PRICE_METHOD)

            recurring = None
            if recurring_interval:
                recurring = {
                    INTERVAL: recurring_interval,
                    INTERVAL_COUNT: recurring_interval_count
                }

            price = stripe.Price.create(
                api_key=stripe_secret_key,
                currency=currency,
                product=product_id,
                unit_amount=convert_to_cents(unit_amount),
                active=active,
                recurring=recurring,
                nickname=nickname,
                metadata=metadata
            )

            return {
                MESSAGE: "Stripe price created successfully.",
                DATA: price
            }

        except stripe.error.InvalidRequestError as exception:
            raise CoreBadRequest(exception_detail=STRIPE_INVALID_REQUEST_MESSAGE,
                                 exception_code=STRIPE_INVALID_REQUEST,
                                 exception_traceback=exception,
                                 method_name=STRIPE_CREATE_PRICE_METHOD)

        except stripe.error.StripeError as exception:
            raise CoreStripeException(exception_traceback=exception,
                                      exception_code=STRIPE_GENERIC,
                                      method_name=STRIPE_CREATE_PRICE_METHOD)

        except CoreBadRequest as exception:
            raise CoreBadRequest(exception_detail=exception.exception_detail,
                                 exception_code=exception.exception_code,
                                 method_name=exception.method_name)

        except Exception as exception:
            raise CoreGenericException(exception_traceback=exception,
                                       exception_code=STRIPE_GENERIC,
                                       method_name=STRIPE_CREATE_PRICE_METHOD)

    @staticmethod
    def modify_stripe_price(
            stripe_secret_key: str,
            price_id: str,
            active: bool = True,
            metadata: dict = None,
            nickname: str = None) -> dict:
        """
        Update a stripe price.

        :type stripe_secret_key: string
        :param stripe_secret_key: Stripe authenticates your API requests using your
                                  account's API keys. Stripe raises an invalid request
                                  error if you don't include a key, and an authentication
                                  error if the key is incorrect or outdated.

        :type price_id: string
        :param price_id: An ID of price that needs to be updated.

        :type active: boolean
        :param active: Whether the price can be used for new purchases. Defaults to true.

        :type metadata: dictionary
        :param metadata: Set of key-value pairs that you can attach to an object. This can 
                         be useful for storing additional information about the object in a 
                         structured format. Individual keys can be unset by posting an empty 
                         value to them. All keys can be unset by posting an empty value to 
                         metadata.

        :type nickname: string
        :param nickname: A brief description of the price, hidden from customers.

        :type: dictionary
        :return: The updated price object is returned upon success.
        """
        try:
            if not isinstance(stripe_secret_key, str) \
                    or not isinstance(price_id, str) \
                    or not isinstance(active, bool) \
                    or not isinstance(metadata, (dict, type(None))) \
                    or not isinstance(nickname, (str, type(None))):
                raise CoreBadRequest(exception_detail=BAD_REQUEST_MESSAGE,
                                     exception_code=STRIPE_BAD_REQUEST,
                                     method_name=STRIPE_MODIFY_PRICE_METHOD)

            price = stripe.Price.modify(
                sid=price_id,
                api_key=stripe_secret_key,
                active=active,
                metadata=metadata,
                nickname=nickname
            )

            return {
                MESSAGE: "Stripe price modified successfully.",
                DATA: price
            }

        except stripe.error.InvalidRequestError as exception:
            raise CoreBadRequest(exception_detail=STRIPE_INVALID_REQUEST_MESSAGE,
                                 exception_code=STRIPE_INVALID_REQUEST,
                                 exception_traceback=exception,
                                 method_name=STRIPE_MODIFY_PRICE_METHOD)

        except stripe.error.StripeError as exception:
            raise CoreStripeException(exception_traceback=exception,
                                      exception_code=STRIPE_GENERIC,
                                      method_name=STRIPE_MODIFY_PRICE_METHOD)

        except CoreBadRequest as exception:
            raise CoreBadRequest(exception_detail=exception.exception_detail,
                                 exception_code=exception.exception_code,
                                 method_name=exception.method_name)

        except Exception as exception:
            raise CoreGenericException(exception_traceback=exception,
                                       exception_code=STRIPE_GENERIC,
                                       method_name=STRIPE_MODIFY_PRICE_METHOD)

    @staticmethod
    def retrieve_stripe_price(
            stripe_secret_key: str,
            price_id: str) -> dict:
        """
        retrieve price information from price id.

        :type stripe_secret_key: string
        :param stripe_secret_key: Stripe authenticates your API requests using your
                                  account's API keys. Stripe raises an invalid request
                                  error if you don't include a key, and an authentication
                                  error if the key is incorrect or outdated.

        :type price_id: string
        :param price_id: An ID of price that needs to be fetched.

        :type: dictionary
        :return: Returns a price if a valid price or plan ID was provided.
        """
        try:
            if not isinstance(price_id, str) or not isinstance(stripe_secret_key, str):
                raise CoreBadRequest(exception_detail=BAD_REQUEST_MESSAGE,
                                     exception_code=STRIPE_BAD_REQUEST,
                                     method_name=STRIPE_RETRIEVE_PRICE_METHOD)

            price = stripe.Price.retrieve(id=price_id, api_key=stripe_secret_key)

            return {
                MESSAGE: "Stripe price retrieved successfully.",
                DATA: price
            }

        except stripe.error.InvalidRequestError as exception:
            raise CoreBadRequest(exception_detail=STRIPE_INVALID_REQUEST_MESSAGE,
                                 exception_code=STRIPE_INVALID_REQUEST,
                                 exception_traceback=exception,
                                 method_name=STRIPE_RETRIEVE_PRICE_METHOD)

        except stripe.error.StripeError as exception:
            raise CoreStripeException(exception_traceback=exception,
                                      exception_code=STRIPE_GENERIC,
                                      method_name=STRIPE_RETRIEVE_PRICE_METHOD)

        except CoreBadRequest as exception:
            raise CoreBadRequest(exception_detail=exception.exception_detail,
                                 exception_code=exception.exception_code,
                                 method_name=exception.method_name)

        except Exception as exception:
            raise CoreGenericException(exception_traceback=exception,
                                       exception_code=STRIPE_GENERIC,
                                       method_name=STRIPE_RETRIEVE_PRICE_METHOD)
