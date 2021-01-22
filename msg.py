import smtplib 
import time
import os

EMAIL = os.getenv("GMAIL")
PASS = os.getenv("GPASS")

class MSG:
    
    def text(self, number, carrier, message):
        client = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        client.ehlo()
        client.login(EMAIL, PASS) 
        email = str(number) + self.cellCarrier(carrier)
        client.sendmail(EMAIL, email, message)
        client.quit()
        
    def cellCarrier(self, carrier):
        if carrier == 'GOOGLE':
            return "@msg.fi.google.com"



if __name__ == "__main__":
    send = MSG()
    send.text(800000000, 'GOOGLE', 'TESTING')
