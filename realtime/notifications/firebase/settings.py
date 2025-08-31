import os

from firebase_admin import credentials, initialize_app

credential_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
credential = credentials.Certificate(os.path.join(credential_dir, "credentials.json"))

if credential:
    initialize_app(
        credential=credential,
        options={"databaseURL": "add_url"},
    )
