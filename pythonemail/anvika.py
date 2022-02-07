import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "sumedhafromiim@gmail.com"  # Enter your address
receiver_email = "mailtoanvika@gmail.com"  # Enter receiver address
password = input("Enter password - ")
message = """\
Subject: Hi there

This message is sent from Python."""

with smtplib.SMTP_SSL(smtp_server, port) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)