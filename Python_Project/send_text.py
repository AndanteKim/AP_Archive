from twilio import rest
""" This is mini project for sms text message. Sometimes, I use this to send a sms message to my friend."""
# My Account Sid and Auth Token from twilio.com/user/account

account_sid = "ACc35bbdca89f92dce210697f238189e78"
auth_token = "6c1b6a0323fd2f734e3bc63fc642027f"
client = rest.Client(account_sid, auth_token)
number = input("Input phone number you want to send : ")
body_text = input("Write a message : ")
message = client.messages.create(
        body=body_text,
        to="+1"+number,    # receiver number
        from_="+12058904323")  # sender number(my number)
print("Sending successful!")
