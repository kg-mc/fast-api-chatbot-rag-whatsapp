from twilio.rest import Client
from config import ACCOUNT_SID_TWILIO, AUTH_TOKEN_TWILIO


client = Client(ACCOUNT_SID_TWILIO, AUTH_TOKEN_TWILIO)

