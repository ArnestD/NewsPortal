from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.db.models.signals import post_save

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'
    send_mail(
        subject="Пользователь",
        message="Добро пожалывать на сайт",
        from_email='al.muzykant@yandex.ru',
        recipient_list=User.email_user(all())
    )

