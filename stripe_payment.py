"""
pip install stripe
"""

import stripe, os


def complete_stripe_payment(data):
    # Set your API key
    stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

    # Create a PaymentIntent with the order amount and currency
    intent = stripe.PaymentIntent.create(
        amount=round(100 * data["total"]),
        currency=data["currency"],
        automatic_payment_methods={"enabled": True, "allow_redirects": "never"},
        metadata=data,
    )
    print("Has been completed stipe payment...")

    return intent


def confirm_payment(payment_intent):
    """
    ⚠️ WARNING: DO NOT USE THIS APPROACH IN PRODUCTION ⚠️

    This method directly sends raw card details (PAN, expiry, CVC)
    from your backend server to Stripe.

    ❌ Why this is dangerous:
    - Collecting or transmitting raw card data on your backend
      makes you fully responsible for PCI-DSS compliance (Level 1),
      which is extremely difficult and expensive to achieve.
    - Stripe strongly discourages this approach for live environments.

    ✅ Correct way:
    - In production, always collect card details using Stripe Elements,
      Checkout, or Payment Links on the frontend.
    - These tools tokenize the card securely and only send
      a PaymentMethod ID (e.g., `pm_12345`) to your backend.
    """
    payment_method = stripe.PaymentMethod.create(
        type="card",
        card={
            "number": "4242424242424242",
            "exp_month": 12,
            "exp_year": 2026,
            "cvc": "123",
        },
    )
    confirmed_intent = stripe.PaymentIntent.confirm(
        payment_intent.id,
        payment_method=payment_method.id,
    )

    print("Has been confirmed stipe payment...")
    return confirmed_intent


# Complete payment
payment_intent = complete_stripe_payment(
    {
        "total": 10,
        "currency": "usd",
    }
)

# Confirm payment
confirm_payment(payment_intent)
