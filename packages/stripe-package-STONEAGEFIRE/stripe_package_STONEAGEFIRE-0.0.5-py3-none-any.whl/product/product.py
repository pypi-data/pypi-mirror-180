import stripe

from src.common.constants.constant import BAD_REQUEST_MESSAGE, DATA, MESSAGE
from src.common.constants.product import CURRENCY, INTERVAL, INTERVAL_COUNT, RECURRING, UNIT_AMOUNT
from src.common.service import convert_to_cents
from src.exceptions.exception_constants import GET_PRICE_DATA, STRIPE_BAD_REQUEST, \
    STRIPE_CREATE_PRODUCT_METHOD, STRIPE_DELETE_PRODUCT_METHOD, STRIPE_GENERIC, STRIPE_INVALID_REQUEST, \
    STRIPE_INVALID_REQUEST_MESSAGE, STRIPE_MODIFY_PRODUCT_METHOD, STRIPE_RETRIEVE_PRODUCT_METHOD
from src.exceptions.exception_handling import CoreBadRequest, CoreGenericException, CoreStripeException


def get_price_data(
    currency: str,
    unit_amount: float,
    recurring_interval: str,
    recurring_interval_count: str):
    try:
        if currency:
            if not unit_amount:
                raise CoreBadRequest(exception_detail=BAD_REQUEST_MESSAGE,
                                     exception_code=STRIPE_BAD_REQUEST,
                                     method_name=GET_PRICE_DATA)

            return {
                CURRENCY: currency,
                UNIT_AMOUNT: convert_to_cents(unit_amount),
                RECURRING: {
                    INTERVAL: recurring_interval,
                    INTERVAL_COUNT: recurring_interval_count
                }
            }
        else:
            return None

    except CoreBadRequest as exception:
        raise CoreBadRequest(exception_detail=exception.exception_detail,
                                exception_code=exception.exception_code,
                                method_name=exception.method_name)

    except Exception as exception:
        raise CoreGenericException(exception_traceback=exception,
                                    exception_code=STRIPE_GENERIC,
                                    method_name=GET_PRICE_DATA)


class StripeProduct:

    @staticmethod
    def create_stripe_product(
            stripe_secret_key: str,
            name: str,
            description: str = None,
            price_currency: str = None,
            price_unit_amount: float = None,
            price_recurring_interval: str = None,
            price_recurring_interval_count: int = None,
            metadata: dict = None) -> dict:
        """
        Creating a new stripe product.

        :type stripe_secret_key: string
        :param stripe_secret_key: Stripe authenticates your API requests using your
                                  account's API keys. Stripe raises an invalid request
                                  error if you don't include a key, and an authentication
                                  error if the key is incorrect or outdated.

        :type name: string
        :param name: The product's name, meant to be displayable to the customer.

        :type description: string
        :param description: The product's description, meant to be displayable to the customer. 
                            Use this field to optionally store a long form explanation of the 
                            product being sold for your own rendering purposes.

        :type price_currency: string
        :param price_currency: Three-letter ISO currency code, in lowercase. 
                               Must be a supported currency.

        :type price_unit_amount: float
        :param price_unit_amount: A positive value or 0 for a free price (rupees, usd, 
                                  etc) representing how much to charge. More than 2 
                                  decimal is rounded to 2 decimal places.

        :type price_recurring_interval: string
        :type price_recurring_interval: Specifies billing frequency. 
                                        Either day, week, month or year.

        :type price_recurring_interval_count: integer
        :param price_recurring_interval_count: The number of intervals between subscription 
                                               billings. For example, interval=month and 
                                               interval_count=3 bills every 3 months. Maximum 
                                               of one-year interval allowed (1 year, 12 months, 
                                               or 52 weeks).

        :type metadata: dictionary
        :param metadata: Set of key-value pairs that you can attach to an object. This can 
                         be useful for storing additional information about the object in a 
                         structured format. Individual keys can be unset by posting an empty 
                         value to them. All keys can be unset by posting an empty value to 
                         metadata.

        :type: dictionary
        :return: returns a product object if the call succeeded.
        """
        try:
            if not isinstance(stripe_secret_key, str) \
                    or not isinstance(name, str) \
                    or not isinstance(description, (str, type(None))) \
                    or not isinstance(price_currency, (str, type(None))) \
                    or not isinstance(price_unit_amount, (int, float, type(None))) \
                    or not isinstance(price_recurring_interval, (str, type(None))) \
                    or not isinstance(price_recurring_interval_count, (int, str, type(None))) \
                    or not isinstance(metadata, (dict, type(None))):
                raise CoreBadRequest(exception_detail=BAD_REQUEST_MESSAGE,
                                     exception_code=STRIPE_BAD_REQUEST,
                                     method_name=STRIPE_CREATE_PRODUCT_METHOD)

            product = stripe.Product.create(
                api_key=stripe_secret_key,
                name=name,
                description=description,
                metadata=metadata,
                default_price_data=get_price_data(
                    price_currency,
                    price_unit_amount,
                    price_recurring_interval,
                    price_recurring_interval_count
                )
            )

            return {
                MESSAGE: "Stripe product created successfully.",
                DATA: product
            }

        except stripe.error.InvalidRequestError as exception:
            raise CoreBadRequest(exception_detail=STRIPE_INVALID_REQUEST_MESSAGE,
                                 exception_traceback=exception, 
                                 exception_code=STRIPE_INVALID_REQUEST,
                                 method_name=STRIPE_CREATE_PRODUCT_METHOD)

        except stripe.error.StripeError as exception:
            raise CoreStripeException(exception_traceback=exception,
                                      exception_code = STRIPE_GENERIC,
                                      method_name=STRIPE_CREATE_PRODUCT_METHOD)

        except CoreBadRequest as exception:
            raise CoreBadRequest(exception_detail=exception.exception_detail,
                                 exception_code=exception.exception_code,
                                 method_name=exception.method_name)

        except Exception as exception:
            raise CoreGenericException(exception_traceback=exception, 
                                       exception_code=STRIPE_GENERIC,
                                       method_name=STRIPE_CREATE_PRODUCT_METHOD)

    @staticmethod
    def modify_stripe_product(
            stripe_secret_key: str,
            product_id: str,
            name: str = None,
            description: str = None,
            default_price_id: str = None,
            active: bool = True,
            metadata: dict = None) -> dict:
        """
        Modify stripe product details.

        :type stripe_secret_key: string
        :param stripe_secret_key: Stripe authenticates your API requests using your
                                  account's API keys. Stripe raises an invalid request
                                  error if you don't include a key, and an authentication
                                  error if the key is incorrect or outdated.

        :type product_id: string
        :param product_id: stripe product id which needs to be updated.

        :type name: string
        :param name: The product's name, meant to be displayable to the customer.

        :type description: string
        :param description: The product's description, meant to be displayable to the customer. 
                            Use this field to optionally store a long form explanation of the 
                            product being sold for your own rendering purposes.

        :type metadata: dictionary
        :param metadata: Set of key-value pairs that you can attach to an object. This can 
                         be useful for storing additional information about the object in a 
                         structured format. Individual keys can be unset by posting an empty 
                         value to them. All keys can be unset by posting an empty value to 
                         metadata.

        :type default_price_id: string
        :param default_price_id: The ID of the <a href="https://stripe.com/docs/api/prices">
                                 Price</a> object that is the default price for this product. 
                                 Only those IDs who are attached to product will be able to 
                                 set as default.

        :type active: boolean
        :param active: Whether the product is available for purchase.

        :type: dictionary
        :returns: Returns the product object if the update succeeded.
        """
        try:
            if not isinstance(stripe_secret_key, str) \
                    or not isinstance(product_id, str) \
                    or not isinstance(description, (str, type(None))) \
                    or not isinstance(metadata, (dict, type(None))) \
                    or not isinstance(default_price_id, (str, type(None))) \
                    or not isinstance(name, (str, type(None))) \
                    or not isinstance(active, bool):
                raise CoreBadRequest(exception_detail=BAD_REQUEST_MESSAGE,
                                     exception_code=STRIPE_BAD_REQUEST,
                                     method_name=STRIPE_MODIFY_PRODUCT_METHOD)

            product = stripe.Product.modify(
                sid=product_id,
                api_key=stripe_secret_key,
                name=name,
                description=description,
                metadata=metadata,
                default_price=default_price_id,
                active=active
            )

            return {
                MESSAGE: "Stripe product modified successfully.",
                DATA: product
            }

        except stripe.error.InvalidRequestError as exception:
            raise CoreBadRequest(exception_detail=STRIPE_INVALID_REQUEST_MESSAGE,
                                 exception_traceback=exception, 
                                 exception_code=STRIPE_INVALID_REQUEST,
                                 method_name=STRIPE_MODIFY_PRODUCT_METHOD)

        except stripe.error.StripeError as exception:
            raise CoreStripeException(exception_traceback=exception,
                                      exception_code = STRIPE_GENERIC,
                                      method_name=STRIPE_MODIFY_PRODUCT_METHOD)

        except CoreBadRequest as exception:
            raise CoreBadRequest(exception_detail=exception.exception_detail,
                                 exception_code=exception.exception_code,
                                 method_name=exception.method_name)

        except Exception as exception:
            raise CoreGenericException(exception_traceback=exception, 
                                       exception_code=STRIPE_GENERIC,
                                       method_name=STRIPE_MODIFY_PRODUCT_METHOD)

    @staticmethod
    def retrieve_stripe_product(
        stripe_secret_key: str, 
        product_id: str) -> dict:
        """
        Retrieve stripe product details using product id.

        :type stripe_secret_key: string
        :param stripe_secret_key: Stripe authenticates your API requests using your
                                  account's API keys. Stripe raises an invalid request
                                  error if you don't include a key, and an authentication
                                  error if the key is incorrect or outdated.

        :type product_id: string
        :param product_id: Unique product ID from either a product creation request or 
                           the product list, and Stripe will return the corresponding 
                           product information.

        :type: dictionary
        :return: Returns a product object if a valid identifier was provided.
        """
        try:
            if not isinstance(stripe_secret_key, str) or not isinstance(product_id, str):
                raise CoreBadRequest(exception_detail=BAD_REQUEST_MESSAGE,
                                     exception_code=STRIPE_BAD_REQUEST,
                                     method_name=STRIPE_RETRIEVE_PRODUCT_METHOD)

            product = stripe.Product.retrieve(id=product_id, api_key=stripe_secret_key)

            return {
                MESSAGE: "Stripe product retrieved successfully.",
                DATA: product
            }

        except stripe.error.InvalidRequestError as exception:
            raise CoreBadRequest(exception_detail=STRIPE_INVALID_REQUEST_MESSAGE,
                                 exception_traceback=exception, 
                                 exception_code=STRIPE_INVALID_REQUEST,
                                 method_name=STRIPE_RETRIEVE_PRODUCT_METHOD)

        except stripe.error.StripeError as exception:
            raise CoreStripeException(exception_traceback=exception,
                                       exception_code = STRIPE_GENERIC,
                                       method_name=STRIPE_RETRIEVE_PRODUCT_METHOD)

        except CoreBadRequest as exception:
            raise CoreBadRequest(exception_detail=exception.exception_detail,
                                 exception_code=exception.exception_code,
                                 method_name=exception.method_name)

        except Exception as exception:
            raise CoreGenericException(exception_traceback=exception, 
                                       exception_code=STRIPE_GENERIC,
                                       method_name=STRIPE_RETRIEVE_PRODUCT_METHOD)

    @staticmethod
    def delete_stripe_product(stripe_secret_key: str, product_id: str) -> dict:
        """
        Delete a stripe product using product id.

        :type stripe_secret_key: string
        :param stripe_secret_key: Stripe authenticates your API requests using your
                                  account's API keys. Stripe raises an invalid request
                                  error if you don't include a key, and an authentication
                                  error if the key is incorrect or outdated.

        :type product_id: string
        :param product_id: Unique product ID which needs to be deleted.

        :type: dictionary
        :return: Returns a deleted object on success. Otherwise, this call raises an error.
        """
        try:
            if not isinstance(product_id, str) or not isinstance(stripe_secret_key, str):
                raise CoreBadRequest(exception_detail=BAD_REQUEST_MESSAGE,
                                     exception_code=STRIPE_BAD_REQUEST,
                                     method_name=STRIPE_DELETE_PRODUCT_METHOD)

            product = stripe.Product.delete(sid=product_id, api_key=stripe_secret_key)

            return {
                MESSAGE: "Stripe product deleted successfully.",
                DATA: product
            }

        except stripe.error.InvalidRequestError as exception:
            raise CoreBadRequest(exception_detail=STRIPE_INVALID_REQUEST_MESSAGE,
                                 exception_traceback=exception, 
                                 exception_code=STRIPE_INVALID_REQUEST,
                                 method_name=STRIPE_DELETE_PRODUCT_METHOD)

        except stripe.error.StripeError as exception:
            raise CoreStripeException(exception_traceback=exception,
                                       exception_code = STRIPE_GENERIC,
                                       method_name=STRIPE_DELETE_PRODUCT_METHOD)

        except CoreBadRequest as exception:
            raise CoreBadRequest(exception_detail=exception.exception_detail,
                                 exception_code=exception.exception_code,
                                 method_name=exception.method_name)

        except Exception as exception:
            raise CoreGenericException(exception_traceback=exception, 
                                       exception_code=STRIPE_GENERIC,
                                       method_name=STRIPE_DELETE_PRODUCT_METHOD)
