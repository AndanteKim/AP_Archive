from twilio import rest
""" This is mini project for sms text message. Sometimes, I use this to send a sms message to my friend."""
# My Account Sid and Auth Token from twilio.com/user/account
# Due to personal information, I hided my unique SID number.
account_sid = "################################"
auth_token = "##################################"
client = rest.Client(account_sid, auth_token)
number = input("Input phone number you want to send : ")
body_text = input("Write a message : ")
message = client.messages.create(
        body=body_text,
        to="+1"+number,    # receiver number
        from_="+12058904323")  # sender number(my number)
print("Sending successful!")
