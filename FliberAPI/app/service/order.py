import logging
from datetime import datetime, timedelta
from random import randint
from uuid import UUID

import requests
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import CashFreeKeys
from app.db.repositories.order import OrderRepository
from app.models.schema.order import (
    OutOrderSchema,
    InOrderSchema,
    RequestOrderSchema,
    OrderSchema,
    RequestOrderPayment,
    OrderSchemaBase,
)

logger = logging.getLogger(__name__)


class OrderService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._order_repository = OrderRepository(self._db_session)

    async def create(self, payload: InOrderSchema):
        order = await self._order_repository.create(payload)
        return order

    async def get_by_id(self, uuid: UUID) -> OutOrderSchema:
        order = await self._order_repository.get_by_id(uuid)
        return order

    async def get_all(self):
        order = await self._order_repository.get_all()
        return order

    async def delete(self, uuid: UUID):
        await self._order_repository.delete(uuid)

    async def update(self, payload: OrderSchema):
        await self._order_repository.update(payload)

    async def create_order(self, payload: RequestOrderSchema):

        order_id = "order_"
        for i in range(9):
            order_id += str(randint(0, 9) * 1)

        # JST = timezone(timedelta(hours=+5, minutes=+30))
        date_time = payload.ExpiryDate + timedelta(days=1)
        date_time = str(date_time).replace(" ", "T").split(".")
        date_time = date_time[0] + "Z"

        order_payload = {
            "order_id": order_id,
            "order_amount": payload.OrderAmount,
            "order_currency": payload.OrderCurrency,
            "customer_details": {
                "customer_name": payload.CustomerName,
                "customer_id": payload.CustomerId,
                "customer_email": payload.CustomerEmail,
                "customer_phone": payload.PhoneNo,
            },
            "order_expiry_time": date_time,
            "order_note": payload.OrderNote,
        }

        # print(f"'{datetime.utcnow()}'")
        # return None

        url = "https://sandbox.cashfree.com/pg/orders"

        headers = {
            "Accept": "application/json",
            "x-api-version": "2021-05-21",
            "Content-Type": "application/json",
            "x-client-id": CashFreeKeys.KEY_ID,
            "x-client-secret": CashFreeKeys.KEY_SECRET,
        }

        response = requests.request("POST", url, json=order_payload, headers=headers)

        if response.status_code == 200:
            response = response.json()
            print(response)
            orders = OrderSchemaBase(
                UserId=payload.UserId,
                OrderId=response["order_id"],
                CFOrderId=response["cf_order_id"],
                Entity=response["entity"],
                CFPaymentId=0,
                PaymentMethod="",
                OrderAmount=response["order_amount"],
                OrderStatus=response["order_status"],
                OrderToken=response["order_token"],
                OrderNote=response["order_note"],
                OrderExpiryTime=response["order_expiry_time"],
                CustomerName=response["customer_details"]["customer_name"],
                CustomerEmail=response["customer_details"]["customer_email"],
                CustomerId=response["customer_details"]["customer_id"],
                CustomerPhone=response["customer_details"]["customer_phone"],
                SettlementsUrl=response["settlements"]["url"],
                PaymentsUrl=response["payments"]["url"],
                RefundsUrl=response["refunds"]["url"],
                PaymentLink=response["payment_link"],
                OrderTags=response["order_tags"] if response["order_tags"] else "",
                CreatedOn=datetime.now(),
                UpdatedOn=datetime.now(),
            )
            result = await self._order_repository.generate(orders)
            return result
        else:
            return response

    async def order_pay(self, payload: RequestOrderPayment):
        url = "https://sandbox.cashfree.com/pg/orders/pay"

        order_payload = {
            "order_token": payload.OrderToken,
            "payment_method": {
                "card": {
                    "channel": "link",
                    "card_number": payload.CardNumber,
                    "card_holder_name": payload.CardHolderName,
                    "card_expiry_mm": payload.cardExpiryMonth,
                    "card_expiry_yy": payload.CardExpiryYear,
                    "card_cvv": payload.CardCVV,
                }
            },
        }

        headers = {
            "Accept": "application/json",
            "x-api-version": "2021-05-21",
            "Content-Type": "application/json",
            "x-client-id": CashFreeKeys.KEY_ID,
            "x-client-secret": CashFreeKeys.KEY_SECRET,
        }

        response = requests.request("POST", url, json=order_payload, headers=headers)
        if response.status_code == 200:
            response = response.json()

            await self._order_repository.update_by_token(
                payload.OrderToken,
                response["cf_payment_id"],
                response["payment_method"],
            )
            return response
        return response.json()

    async def get_order_data_from_cashfree(self, order_id: str):
        url = f"https://sandbox.cashfree.com/pg/orders/{order_id}"

        headers = {
            "Accept": "application/json",
            "x-api-version": "2021-05-21",
            "Content-Type": "application/json",
            "x-client-id": CashFreeKeys.KEY_ID,
            "x-client-secret": CashFreeKeys.KEY_SECRET,
        }

        response = requests.request("GET", url, headers=headers)
        return response.json()

    async def delete_order_by_user_id(self, user_id: UUID):
        await self._order_repository.delete_by_user_id(user_id)
