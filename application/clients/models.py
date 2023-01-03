from django.contrib.auth.models import User
from django.db import models as m


class Client(m.Model):
    # Client is a worker of some company
    user = m.OneToOneField(User, on_delete=m.PROTECT)
    company_name = m.CharField(max_length=100)
    full_address = m.CharField(max_length=100)

    def __str__(self):
        return f'Client {self.company_name}'
