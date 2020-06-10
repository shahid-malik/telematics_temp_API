import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config import *
from templates import EMAIL_TEXT, BASIC_EMAIL_TEMPLATE


def send_email(name, temperature, image):
    """
    Send an email to administration with employee name, temperature, picture and timestamp.
    :param temperature: Decimal Value in degree celcius
    :return:
    """
    message = MIMEMultipart("alternative")
    message['From'] = EMAIL_HOST_USER
    message['To'] = RECIPIENTS[0]
    message['Subject'] = 'Temperature Alert - {}'.format(datetime.datetime.now())
    plain_text = MIMEText(EMAIL_TEXT.format(name, temperature), "plain")
    html_text = MIMEText(BASIC_EMAIL_TEMPLATE, "html")
    message.attach(plain_text)
    print(plain_text)
    message.attach(html_text)

    session = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo()
    session.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    msg_text = message.as_string()
    for recipient in RECIPIENTS:
        session.sendmail(EMAIL_HOST_USER, recipient, msg_text)
    session.quit()
