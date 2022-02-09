import time 
import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "sumedhafromiim@gmail.com"  # Enter your address
password = input("Enter password - ")
message = """\
Subject: Hi there

This message is sent from Python."""

with smtplib.SMTP_SSL(smtp_server, port) as server:  #to avoid try catch dinally for cloding of files 
    server.login(sender_email, password)
    with open('emails.csv', 'r') as file:
        count = 0
        
        while True:
            count += 1
        
            # Get next line from file
            line = file.readline()
        
            # if line is empty
            # end of file is reached
            if not line:
                break
            print("Line{}: {}".format(count, line.strip()))
            server.sendmail(sender_email,line.strip(), message)  
            time.sleep(5)


