from django.core.mail import send_mail as sd
import time
from example_celery.celery import app


@app.task
def send_mail(email,first_name,last_name):
    time.sleep(30)
    sd(
        "Bienvenido",
        "Este es un mensaje para {0} {1}".format(first_name,last_name),
        "correo@gmail.com",
        [email]
    )