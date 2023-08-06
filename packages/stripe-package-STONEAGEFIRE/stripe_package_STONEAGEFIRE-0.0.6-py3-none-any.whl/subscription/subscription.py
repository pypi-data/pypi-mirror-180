from datetime import datetime
import pytz
import stripe
from src.common.constants.constant import *
from src.exceptions.exception_constants import *

from src.exceptions.exception_handling import *



class StripeSubscription:

    @staticmethod
    def create_stripe_subscription(
            stripe_secret_key: str, customer_id: str,
            price_id: str, currency: str,
            coupon: str = None, promo_code: str = None,
            cancel_at_period_end: bool = False, default_payment_method: str = None,
            metadata: dict = None, description: str = None
    ) -> dict:
        """
        A stripe create subscription method.

        :type stripe_secret_key: string
        :param stripe_secret_key: Stripe authenticates your API requests using your
                                  account’s API keys. Stripe raises an invalid request
                                  error if you don’t include a key, and an authentication
                                  error if the key is incorrect or outdated.

        :type customer_id: string
        :param customer_id: Stripe id of the customer to subscribe.

        :type price_id: string
        :param price_id: Stripe id of the price object.

        :type currency: string
        :param currency: Three-letter ISO currency code, in lowercase.
                         Must be a <a href="https://stripe.com/docs/currencies">
                         supported currency</a>.

        :type coupon: string
        :param coupon: The ID of the coupon to apply to this subscription.
                       A coupon applied to a subscription will only affect
                       invoices created for that particular subscription.

        :type promo_code: string
        :param promo_code: The API ID of a promotion code to apply to this subscription.
                           A promotion code applied to a subscription will only affect
                           invoices created for that particular subscription.

        :type cancel_at_period_end: boolean
        :param cancel_at_period_end: Boolean indicating whether this subscription should
                                     cancel at the end of the current period.

        :type default_payment_method: string
        :param default_payment_method: ID of the default payment method for the subscription.
                                       It must belong to the customer associated with the
                                       subscription.

        :type metadata: dictionary
        :param metadata: Set of key-value pairs that you can attach to an object. This can be useful
                         for storing additional information about the object in a structured format.
                         Individual keys can be unset by posting an empty value to them. All keys
                         can be unset by posting an empty value to metadata.

        :type description: string
        :param description: The subscription’s description, meant to be displayable to the customer.
                            Use this field to optionally store an explanation of the subscription
                            for rendering in Stripe surfaces.

        :type: dictionary
        :returns: The newly created Subscription object, if the call succeeded.
                  If the attempted charge fails, the subscription is created in an incomplete
                  status.
        """
        try:
            if not isinstance(stripe_secret_key, str) \
                    or not isinstance(customer_id, str) \
                    or not isinstance(price_id, str) \
                    or not isinstance(currency, str) \
                    or not isinstance(coupon, (str, type(None))) \
                    or not isinstance(promo_code, (str, type(None))) \
                    or not isinstance(cancel_at_period_end, bool) \
                    or not isinstance(default_payment_method, (str, type(None))) \
                    or not isinstance(metadata, (dict, type(None))) \
                    or not isinstance(description, (str, type(None))):
                raise CoreBadRequest(exception_detail=BAD_REQUEST_MESSAGE,
                                     exception_code=STRIPE_BAD_REQUEST,
                                     method_name=STRIPE_CREATE_SUBSCRIPTION_METHOD)

            subscription = stripe.Subscription.create(
                customer=customer_id,
                items=[
                    {
                        "price": price_id
                    }
                ],
                metadata=metadata,
                coupon=coupon,
                cancel_at_period_end=cancel_at_period_end,
                default_payment_method=default_payment_method,
                description=description,
                payment_behavior="default_incomplete",
                currency=currency,
                promotion_code=promo_code,
                collection_method="charge_automatically",
                proration_behavior=None,
                expand=["latest_invoice.payment_intent"],
                api_key=stripe_secret_key
            )

            return {
                DATA: subscription,
                MESSAGE: "Subscription created successfully."
            }

        except stripe.error.InvalidRequestError as exception:
            raise CoreBadRequest(exception_detail=STRIPE_INVALID_REQUEST_MESSAGE,
                                 exception_code=STRIPE_INVALID_REQUEST,
                                 exception_traceback=exception,
                                 method_name=STRIPE_CREATE_SUBSCRIPTION_METHOD)

        except stripe.error.StripeError as exception:
            raise CoreStripeException(exception_code=STRIPE_GENERIC,
                                      exception_traceback=exception,
                                      method_name=STRIPE_CREATE_SUBSCRIPTION_METHOD)

        except CoreBadRequest as exception:
            raise CoreBadRequest(exception_detail=exception.exception_detail,
                                 exception_code=exception.exception_code,
                                 method_name=exception.method_name)

        except Exception as exception:
            raise CoreGenericException(exception_code=STRIPE_GENERIC,
                                       exception_traceback=exception,
                                       method_name=STRIPE_CREATE_SUBSCRIPTION_METHOD)

    def update_stripe_subscription(
            self, stripe_secret_key: str,
            subscription_id: str, price_id: str = None,
            coupon: str = None, promo_code: str = None,
            default_payment_method: str = None, metadata: dict = None,
            description: str = None
    ) -> dict:
        """
        A stripe update subscription method. It will update the subscription at the
        current period end.

        :type stripe_secret_key: string
        :param stripe_secret_key: Stripe authenticates your API requests using your
                                  account’s API keys. Stripe raises an invalid request
                                  error if you don’t include a key, and an authentication
                                  error if the key is incorrect or outdated.

        :type subscription_id: string
        :param subscription_id: Stripe subscription id.

        :type price_id: string
        :param price_id: Stripe price id.

        :type coupon: string
        :param coupon: The ID of the coupon to apply to this subscription.
                       A coupon applied to a subscription will only affect
                       invoices created for that particular subscription.

        :type promo_code: string
        :param promo_code: The API ID of a promotion code to apply to this subscription.
                           A promotion code applied to a subscription will only affect
                            invoices created for that particular subscription.

        :type default_payment_method: string
        :param default_payment_method: ID of the default payment method for the subscription.
                                       It must belong to the customer associated with the
                                       subscription.

        :type metadata: dictionary
        :param metadata: Set of key-value pairs that you can attach to an object. This can be useful
                         for storing additional information about the object in a structured format.
                         Individual keys can be unset by posting an empty value to them. All keys
                         can be unset by posting an empty value to metadata.

        :type description: string
        :param description: The subscription’s description, meant to be displayable to the customer.
                            Use this field to optionally store an explanation of the subscription
                            for rendering in Stripe surfaces.

        :type: dictionary
        :returns: The newly updated Subscription object, if the call succeeded.
        """
        try:
            if not isinstance(stripe_secret_key, str) \
                    or not isinstance(subscription_id, str) \
                    or not isinstance(price_id, (str, type(None))) \
                    or not isinstance(coupon, (str, type(None))) \
                    or not isinstance(promo_code, (str, type(None))) \
                    or not isinstance(default_payment_method, (str, type(None))) \
                    or not isinstance(metadata, (dict, type(None))) \
                    or not isinstance(description, (str, type(None))):
                raise CoreBadRequest(exception_detail=BAD_REQUEST_MESSAGE,
                                     exception_code=STRIPE_BAD_REQUEST,
                                     method_name=STRIPE_MODIFY_SUBSCRIPTION_METHOD)

            # stripe retrieve stripe subscription
            subscription_obj = self.retrieve_stripe_subscription(
                stripe_secret_key=stripe_secret_key, subscription_id=subscription_id
            )

            # get coupon from promo-code
            if coupon is None and promo_code is not None:
                # TODO: Call from promo_code pkg
                promo_code_obj = stripe.PromotionCode.retrieve(
                    promo_code, api_key=stripe_secret_key
                )
                coupon = promo_code_obj.get("coupon").get("id")

            # get scheduler_id from subscription object or create scheduler for subscription
            if subscription_obj.get("schedule") is None:
                schedule_obj = StripeSubscriptionSchedule().create_stripe_subscription_schedule(
                    stripe_secret_key=stripe_secret_key, subscription_id=subscription_id
                )
                scheduler_id = schedule_obj.get("data").get("id")
            else:
                scheduler_id = subscription_obj.get("schedule")

            if price_id is not None or \
                    (price_id is None and coupon is not None):

                # Update subscription via subscription schedule
                StripeSubscriptionSchedule().update_stripe_subscription_schedule(
                    stripe_secret_key=stripe_secret_key,
                    schedule_id=scheduler_id,
                    current_phase_start_dt=subscription_obj.get("current_period_start"),
                    current_phase_end_dt=subscription_obj.get("current_period_end"),
                    current_price_id=subscription_obj.get("plan").get("id"),
                    new_price_id=price_id,
                    coupon=coupon,
                    default_payment_method=default_payment_method,
                    metadata=metadata,
                    description=description
                )

                # get updated subscription object
                subscription_obj = self.retrieve_stripe_subscription(
                    stripe_secret_key=stripe_secret_key,
                    subscription_id=subscription_id
                )

            else:
                # Update subscription when not having price related changes
                subscription_obj = stripe.Subscription.modify(
                    subscription_id,
                    metadata=metadata,
                    default_payment_method=default_payment_method,
                    description=description,
                    expand=["latest_invoice.payment_intent"],
                    api_key=stripe_secret_key
                )

            return {
                DATA: subscription_obj,
                MESSAGE: "Subscription changes for upgrade/downgrade are applied at the end "
                         "of your current billing cycle."
            }

        except stripe.error.InvalidRequestError as exception:
            log_error(exception, STRIPE_INVALID_REQUEST, STRIPE_MODIFY_SUBSCRIPTION_METHOD)
            raise CoreBadRequest(exception_detail=STRIPE_INVALID_REQUEST,
                                 exception_code=STRIPE_INVALID_REQUEST,
                                 exception_traceback=exception,
                                 method_name=STRIPE_MODIFY_SUBSCRIPTION_METHOD)

        except stripe.error.StripeError as exception:
            log_error(exception, STRIPE_GENERIC, STRIPE_MODIFY_SUBSCRIPTION_METHOD)
            raise CoreStripeException(exception_code=STRIPE_GENERIC,
                                      exception_traceback=exception,
                                      method_name=STRIPE_MODIFY_SUBSCRIPTION_METHOD)

        except CoreBadRequest as exception:
            log_error(exception.exception_traceback if exception.exception_traceback else exception,
                      exception.exception_code, method_name=exception.method_name)
            raise CoreBadRequest(exception_detail=exception.exception_detail,
                                 exception_code=exception.exception_code,
                                 method_name=exception.method_name)

        except Exception as exception:
            log_error(exception, STRIPE_GENERIC, STRIPE_MODIFY_SUBSCRIPTION_METHOD)
            raise CoreGenericException(exception_code=STRIPE_GENERIC,
                                       exception_traceback=exception,
                                       method_name=STRIPE_MODIFY_SUBSCRIPTION_METHOD)

    def cancel_stripe_subscription(
            self, stripe_secret_key: str, subscription_id: str
    ) -> dict:
        """
            A stripe cancel subscription method. It will cancel the subscription at the
            current period end.

            :type stripe_secret_key: string
            :param stripe_secret_key: Stripe authenticates your API requests using your
                                      account’s API keys. Stripe raises an invalid request
                                      error if you don’t include a key, and an authentication
                                      error if the key is incorrect or outdated.

            :type subscription_id: string
            :param subscription_id: Stripe subscription id.

            :type: dictionary
            :returns: The canceled Subscription object. Its subscription status will set to be
                      canceled.
        """
        try:
            if not isinstance(subscription_id, str) \
                    or not isinstance(stripe_secret_key, str):
                raise CoreBadRequest(exception_detail=BAD_REQUEST_MESSAGE,
                                     exception_code=STRIPE_BAD_REQUEST,
                                     method_name=STRIPE_CANCEL_SUBSCRIPTION_METHOD)

            # stripe retrieve stripe subscription
            subscription_obj = self.retrieve_stripe_subscription(
                stripe_secret_key=stripe_secret_key, subscription_id=subscription_id
            )

            # convert unix time to utc timestamp
            current_period_end = pytz.utc.localize(
                datetime.fromtimestamp(subscription_obj.get("current_period_end")))

            now = pytz.utc.localize(datetime.now())

            if subscription_obj.get("schedule") is not None:

                # release stripe subscription schedule for cancel at period end
                StripeSubscriptionSchedule().release_stripe_subscription_schedule(
                    stripe_secret_key=stripe_secret_key,
                    schedule_id=subscription_obj.get("schedule")
                )

            if now < current_period_end:
                subscription = stripe.Subscription.modify(
                    subscription_id,
                    cancel_at_period_end=True,
                    api_key=stripe_secret_key
                )
                return {
                    DATA: subscription,
                    MESSAGE: "Subscription would be cancelled on end day of your billing period."
                }

            else:
                subscription = stripe.Subscription.delete(
                    subscription_id, api_key=stripe_secret_key
                )
                return {
                    DATA: subscription,
                    MESSAGE: "Subscription cancelled."
                }

        except stripe.error.InvalidRequestError as exception:
            log_error(exception, STRIPE_INVALID_REQUEST, STRIPE_CANCEL_SUBSCRIPTION_METHOD)
            raise CoreBadRequest(exception_detail=STRIPE_INVALID_REQUEST,
                                 exception_code=STRIPE_INVALID_REQUEST,
                                 exception_traceback=exception,
                                 method_name=STRIPE_CANCEL_SUBSCRIPTION_METHOD)

        except stripe.error.StripeError as exception:
            log_error(exception, STRIPE_GENERIC, STRIPE_CANCEL_SUBSCRIPTION_METHOD)
            raise CoreStripeException(exception_code=STRIPE_GENERIC,
                                      exception_traceback=exception,
                                      method_name=STRIPE_CANCEL_SUBSCRIPTION_METHOD)

        except CoreBadRequest as exception:
            log_error(exception.exception_traceback if exception.exception_traceback else exception,
                      exception.exception_code, method_name=exception.method_name)
            raise CoreBadRequest(exception_detail=exception.exception_detail,
                                 exception_code=exception.exception_code,
                                 method_name=exception.method_name)

        except Exception as exception:
            log_error(exception, STRIPE_GENERIC, STRIPE_CANCEL_SUBSCRIPTION_METHOD)
            raise CoreGenericException(exception_code=STRIPE_GENERIC,
                                       exception_traceback=exception,
                                       method_name=STRIPE_CANCEL_SUBSCRIPTION_METHOD)

    @staticmethod
    def retrieve_stripe_subscription(
            stripe_secret_key: str, subscription_id: str
    ) -> dict:
        """
            A stripe retrieve subscription method.

            :type stripe_secret_key: string
            :param stripe_secret_key: Stripe authenticates your API requests using your
                                      account’s API keys. Stripe raises an invalid request
                                      error if you don’t include a key, and an authentication
                                      error if the key is incorrect or outdated.

            :type subscription_id: string
            :param subscription_id: Stripe subscription id

            :type: dictionary
            :returns: Returns the subscription object.
        """

        try:
            if not isinstance(subscription_id, str) \
                    or not isinstance(stripe_secret_key, str):
                raise CoreBadRequest(exception_detail=BAD_REQUEST_MESSAGE,
                                     exception_code=STRIPE_BAD_REQUEST,
                                     method_name=STRIPE_RETRIEVE_SUBSCRIPTION_METHOD)

            subscription = stripe.Subscription.retrieve(
                subscription_id, api_key=stripe_secret_key
            )

            return {
                DATA: subscription,
                MESSAGE: "Subscription retrieved successfully."
            }

        except stripe.error.InvalidRequestError as exception:
            log_error(exception, STRIPE_INVALID_REQUEST, STRIPE_RETRIEVE_SUBSCRIPTION_METHOD)
            raise CoreBadRequest(exception_detail=STRIPE_INVALID_REQUEST,
                                 exception_code=STRIPE_INVALID_REQUEST,
                                 exception_traceback=exception,
                                 method_name=STRIPE_RETRIEVE_SUBSCRIPTION_METHOD)

        except stripe.error.StripeError as exception:
            log_error(exception, STRIPE_GENERIC, STRIPE_RETRIEVE_SUBSCRIPTION_METHOD)
            raise CoreStripeException(exception_code=STRIPE_GENERIC,
                                      exception_traceback=exception,
                                      method_name=STRIPE_RETRIEVE_SUBSCRIPTION_METHOD)

        except CoreBadRequest as exception:
            log_error(exception.exception_traceback if exception.exception_traceback else exception,
                      exception.exception_code, method_name=exception.method_name)
            raise CoreBadRequest(exception_detail=exception.exception_detail,
                                 exception_code=exception.exception_code,
                                 method_name=exception.method_name)

        except Exception as exception:
            log_error(exception, STRIPE_GENERIC, STRIPE_RETRIEVE_SUBSCRIPTION_METHOD)
            raise CoreGenericException(exception_code=STRIPE_GENERIC,
                                       exception_traceback=exception,
                                       method_name=STRIPE_RETRIEVE_SUBSCRIPTION_METHOD)
