from twilio.rest import Client
from baseapp.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

def check_phone(phone):
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    phone_number = client.lookups.v2.phone_numbers(phone).fetch()

    if phone_number.valid == True:
        return True
    
    return False
