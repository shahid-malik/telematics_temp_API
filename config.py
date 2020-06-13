RECIPIENTS = ["enterprise.notification@canamwireless.com"]
# RECIPIENTS = ["shahid.ibex@yahoo.com"]


# Host configurations
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = 'johan@123'
EMAIL_HOST_USER = 'enterprise.notification@canamwireless.com'

# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_PASSWORD = '1234great5678'
# EMAIL_HOST_USER = 'mariegreat123@gmail.com'


MACHINE_IP = "24.55.9.146"

IMAGE_NAME = "employee_face.jpeg"

TEMPERATURE_LIMIT = 90.0


HEADERS = {'Content-Type': 'application/json'}
BASE_URL = "http://" + MACHINE_IP + ":8080/api/v1/face/"

TIME_PERIOD = 60
