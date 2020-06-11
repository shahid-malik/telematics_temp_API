import datetime
import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64
from config import *
from templates import EMAIL_TEXT, BASIC_EMAIL_TEMPLATE


def send_email(name, temperature, base_64_string, timestamp):
    """
    Send an email to administration with employee name, temperature, picture and timestamp.
    :param name:
    :param timestamp:
    :param base_64_string:
    :param temperature: Decimal Value in degree celcius
    :return:
    """
    message = MIMEMultipart("alternative")
    message['From'] = EMAIL_HOST_USER
    message['To'] = RECIPIENTS[0]
    message['Subject'] = 'Temperature Alert - {}'.format(datetime.datetime.now())
    plain_text = MIMEText(EMAIL_TEXT.format(name, temperature), "plain")
    values_update0 = BASIC_EMAIL_TEMPLATE.replace('namevalue', name)
    values_update0 = values_update0.replace('temperaturevalue', str(temperature))
    values_update0 = values_update0.replace('timestamp', str(timestamp))
    html_text = MIMEText(values_update0, "html")

    message.attach(plain_text)
    message.attach(html_text)

    face_image = get_image(base_64_string)
    face_image.add_header('Content-ID', '<image1>')
    message.attach(face_image)

    session = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo()
    session.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    msg_text = message.as_string()
    for recipient in RECIPIENTS:
        session.sendmail(EMAIL_HOST_USER, recipient, msg_text)
    session.quit()


def base64_to_image(img_data):
    """
    Convert base64 to an image file to attach in the email
    :param img_data:
    :return:
    """
    imgdata = base64.b64decode(img_data)
    with open(IMAGE_NAME, 'wb') as f:
        f.write(imgdata)


def get_image(base_64_string):
    """
    Get Image
    :param base_64_string:
    :return:
    """
    base_64_string = base_64_string.split(';base64,')[1]
    base64_to_image(base_64_string)
    fp = open(IMAGE_NAME, 'rb')
    msgImage = MIMEImage(fp.read(), _subtype="jpeg")
    fp.close()
    return msgImage
