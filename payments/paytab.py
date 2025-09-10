import requests

url = "https://www.paytabs.com/apiv2/create_pay_page"
payload = {
    "merchant_email": "your_merchant_email",
    "secret_key": "your_secret_key",
    "site_url": "https://yourwebsite.com",
    "return_url": "https://yourwebsite.com/payment/return",
    "title": "Test Payment",
    "cc_first_name": "John",
    "cc_last_name": "Doe",
    "cc_phone_number": "965",
    "phone_number": "12345678",
    "email": "customer@example.com",
    "products_per_title": "Product1",
    "unit_price": 10,
    "quantity": 1,
    "amount": 10,
    "currency": "SAR"
}
response = requests.post(url, data=payload)
print(response.json())
