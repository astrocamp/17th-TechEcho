# -*- coding: utf-8 -*-
# sample_create_order_ALL.py

import os
from datetime import datetime

from .payment_sdk import ECPayPaymentSdk


def ecpay_api(order_params):
    order_params = order_params
    # 建立實體
    ecpay_payment_sdk = ECPayPaymentSdk(
        MerchantID=os.getenv("ECPAY_MerchantID"),
        HashKey=os.getenv("ECPAY_HashKey"),
        HashIV=os.getenv("ECPAY_HashIV"),
    )

    try:
        # 產生綠界訂單所需參數
        final_order_params = ecpay_payment_sdk.create_order(order_params)

        # 產生 html 的 form 格式
        action_url = (
            "https://payment-stage.ecpay.com.tw/Cashier/AioCheckOut/V5"  # 測試環境
        )
        # action_url = "https://payment.ecpay.com.tw/Cashier/AioCheckOut/V5"  # 正式環境
        html = ecpay_payment_sdk.gen_html_post_form(action_url, final_order_params)
        return html
    except Exception as error:
        print("An exception happened: " + str(error))
