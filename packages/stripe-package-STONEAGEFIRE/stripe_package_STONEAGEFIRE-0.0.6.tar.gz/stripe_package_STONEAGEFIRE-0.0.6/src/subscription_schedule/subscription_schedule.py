import stripe
from src.common.constants.constant import *
from src.exceptions.exception_constants import *
from src.exceptions.exception_handling import *


class StripeSubscriptionSchedule:

    @staticmethod
    def create_stripe_subscription_schedule(
            stripe_secret_key: str, subscription_id: str
    ) -> dict:
        """
        A stripe create subscription schedule method.

        :type stripe_secret_key: string
        :param stripe_secret_key: Stripe authenticates your API requests using your
                                  account’s API keys. Stripe raises an invalid request
                                  error if you don’t include a key, and an authentication
                                  error if the key is incorrect or outdated.

        :type subscription_id: string
        :param subscription_id: Stripe subscription id.

        :type: dictionary
        :returns: Returns a subscription schedule object if the call succeeded.
        """
        try:
            if not isinstance(stripe_secret_key, str) \
                    or not isinstance(subscription_id, str):
                raise CoreBadRequest(exception_detail=BAD_REQUEST_MESSAGE,
                                     exception_code=STRIPE_BAD_REQUEST,
                                     method_name=STRIPE_CREATE_SUBSCRIPTION_SCHEDULE_METHOD)

            subscription_schedule = stripe.SubscriptionSchedule.create(
                from_subscription=subscription_id,
                api_key=stripe_secret_key
            )

            return {
                DATA: subscription_schedule,
                MESSAGE: "Subscription schedule created successfully."
            }

        except stripe.error.InvalidRequestError as exception:
            raise CoreBadRequest(exception_detail=STRIPE_INVALID_REQUEST_MESSAGE,
                                 exception_code=STRIPE_INVALID_REQUEST,
                                 exception_traceback=exception,
                                 method_name=STRIPE_CREATE_SUBSCRIPTION_SCHEDULE_METHOD)

        except stripe.error.StripeError as exception:
            raise CoreStripeException(exception_code=STRIPE_GENERIC,
                                      exception_traceback=exception,
                                      method_name=STRIPE_CREATE_SUBSCRIPTION_SCHEDULE_METHOD)

        except CoreBadRequest as exception:
            raise CoreBadRequest(exception_detail=exception.exception_detail,
                                 exception_code=exception.exception_code,
                                 method_name=exception.method_name)

        except Exception as exception:
            raise CoreGenericException(exception_code=STRIPE_GENERIC,
                                       exception_traceback=exception,
                                       method_name=STRIPE_CREATE_SUBSCRIPTION_SCHEDULE_METHOD)

    @staticmethod
    def update_stripe_subscription_schedule(
            stripe_secret_key: str, schedule_id: str,
            current_phase_start_dt: str, current_phase_end_dt: str,
            current_price_id: str, new_price_id: str = None,
            coupon: str = None, default_payment_method: str = None,
            metadata: dict = None, description: str = None
    ) -> dict:
        """
        A stripe update subscription schedule method.

        :type stripe_secret_key: string
        :param stripe_secret_key: Stripe authenticates your API requests using your
                                  account’s API keys. Stripe raises an invalid request
                                  error if you don’t include a key, and an authentication
                                  error if the key is incorrect or outdated.

        :type schedule_id: string
        :param schedule_id: Stripe subscription schedule id.

        :type current_phase_start_dt: string
        :param current_phase_start_dt: The date at which this phase of the subscription
                                       schedule starts or now. Must be set on the first phase.

        :type current_phase_end_dt: string
        :param current_phase_end_dt: The date at which this phase of the subscription
                                     schedule ends. If set, iterations must not be set.

        :type current_price_id: string
        :param current_price_id: Current ID of the price object.

        :type new_price_id: string
        :param new_price_id: New ID of the price object.

        :type coupon: string
        :param coupon: The identifier of the coupon to apply to this phase of the subscription
                       schedule.

        :type default_payment_method: string
        :param default_payment_method: ID of the default payment method for the subscription
                                       schedule. It must belong to the customer associated with
                                       the subscription schedule. If not set, invoices will use
                                       the default payment method in the customer’s invoice
                                       settings.

        :type metadata: dictionary
        :param metadata: Set of key-value pairs that you can attach to a phase. Metadata on a
                         schedule’s phase will update the underlying subscription’s metadata
                         when the phase is entered, adding new keys and replacing existing keys
                         in the subscription’s metadata. Individual keys in the subscription’s
                         metadata can be unset by posting an empty value to them in the phase’s
                         metadata. To unset all keys in the subscription’s metadata, update the
                         subscription directly or unset every key individually from the phase’s
                         metadata.

        :type description: string
        :param description: Subscription description, meant to be displayable to the customer.
                            Use this field to optionally store an explanation of the subscription.

        :type: dictionary
        :returns: Returns an updated subscription schedule object if the call succeeded.
        """
        try:
            if not isinstance(stripe_secret_key, str) \
                    or not isinstance(schedule_id, str) \
                    or not isinstance(current_phase_start_dt, int) \
                    or not isinstance(current_phase_end_dt, int) \
                    or not isinstance(current_price_id, str) \
                    or not isinstance(new_price_id, (str, type(None))) \
                    or not isinstance(coupon, (str, type(None))) \
                    or not isinstance(default_payment_method, (str, type(None))) \
                    or not isinstance(metadata, (dict, type(None))) \
                    or not isinstance(description, (str, type(None))):
                raise CoreBadRequest(exception_detail=BAD_REQUEST_MESSAGE,
                                     exception_code=STRIPE_BAD_REQUEST,
                                     method_name=STRIPE_MODIFY_SUBSCRIPTION_SCHEDULE_METHOD)

            if new_price_id is None:
                new_price_id = current_price_id

            subscription_schedule = stripe.SubscriptionSchedule.modify(
                schedule_id,
                api_key=stripe_secret_key,
                end_behavior="release",
                phases=[
                    {
                        "start_date": current_phase_start_dt,
                        "end_date": current_phase_end_dt,
                        "items": [
                            {
                                "price": current_price_id,
                            },
                        ],
                    },
                    {
                        "items": [
                            {
                                "price": new_price_id,
                            },
                        ],
                        "metadata": metadata,
                        "coupon": coupon,
                        "default_payment_method": default_payment_method,
                        "description": description,
                    },
                ],
            )

            return {
                DATA: subscription_schedule,
                MESSAGE: "Subscription Schedule modified successfully."
            }

        except stripe.error.InvalidRequestError as exception:
            raise CoreBadRequest(exception_detail=STRIPE_INVALID_REQUEST,
                                 exception_code=STRIPE_INVALID_REQUEST,
                                 exception_traceback=exception,
                                 method_name=STRIPE_MODIFY_SUBSCRIPTION_SCHEDULE_METHOD)

        except stripe.error.StripeError as exception:
            raise CoreStripeException(exception_code=STRIPE_GENERIC,
                                      exception_traceback=exception,
                                      method_name=STRIPE_MODIFY_SUBSCRIPTION_SCHEDULE_METHOD)

        except CoreBadRequest as exception:
            raise CoreBadRequest(exception_detail=exception.exception_detail,
                                 exception_code=exception.exception_code,
                                 method_name=exception.method_name)

        except Exception as exception:
            raise CoreGenericException(exception_code=STRIPE_GENERIC,
                                       exception_traceback=exception,
                                       method_name=STRIPE_MODIFY_SUBSCRIPTION_SCHEDULE_METHOD)

    @staticmethod
    def release_stripe_subscription_schedule(
            stripe_secret_key: str, schedule_id: str
    ) -> dict:
        """
        A stripe release subscription schedule method.

        :type stripe_secret_key: string
        :param stripe_secret_key: Stripe authenticates your API requests using your
                                  account’s API keys. Stripe raises an invalid request
                                  error if you don’t include a key, and an authentication
                                  error if the key is incorrect or outdated.

        :type schedule_id: string
        :param schedule_id: Stripe schedule id.

        :type: dictionary
        :returns: The released subscription_schedule object. Its status will be released,
                  released_at will be the current time, and released_subscription will be
                  the ID of the subscription schedule managed prior to being released.
        """
        try:
            if not isinstance(stripe_secret_key, str) \
                    or not isinstance(schedule_id, str):
                raise CoreBadRequest(exception_detail=BAD_REQUEST_MESSAGE,
                                     exception_code=STRIPE_BAD_REQUEST,
                                     method_name=STRIPE_RELEASE_SUBSCRIPTION_SCHEDULE_METHOD)

            subscription_schedule = stripe.SubscriptionSchedule.release(
                    schedule_id, api_key=stripe_secret_key
                )

            return {
                DATA: subscription_schedule,
                MESSAGE: "Subscription schedule released successfully."
            }

        except stripe.error.InvalidRequestError as exception:
            raise CoreBadRequest(exception_detail=STRIPE_INVALID_REQUEST_MESSAGE,
                                 exception_code=STRIPE_INVALID_REQUEST,
                                 exception_traceback=exception,
                                 method_name=STRIPE_RELEASE_SUBSCRIPTION_SCHEDULE_METHOD)

        except stripe.error.StripeError as exception:
            raise CoreStripeException(exception_code=STRIPE_GENERIC,
                                      exception_traceback=exception,
                                      method_name=STRIPE_RELEASE_SUBSCRIPTION_SCHEDULE_METHOD)

        except CoreBadRequest as exception:
            raise CoreBadRequest(exception_detail=exception.exception_detail,
                                 exception_code=exception.exception_code,
                                 method_name=exception.method_name)

        except Exception as exception:
            raise CoreGenericException(exception_code=STRIPE_GENERIC,
                                       exception_traceback=exception,
                                       method_name=STRIPE_RELEASE_SUBSCRIPTION_SCHEDULE_METHOD)
