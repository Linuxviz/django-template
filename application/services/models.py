from django.core.validators import MaxValueValidator
from django.db import models as m

# Create your models here.
from clients.models import Client


class Service(m.Model):
    name = m.CharField(max_length=100)
    full_price = m.PositiveIntegerField()


class Plan(m.Model):
    PLAN_TYPES = (
        ('full', 'full'),
        ('student', 'student'),
        ('discount', 'discount')
    )
    play_type = m.CharField(max_length=20, choices=PLAN_TYPES)
    discount_percent = m.PositiveIntegerField(default=1, validators=[MaxValueValidator(100)])


class Subscription(m.Model):
    client = m.ForeignKey(Client, related_name='subscriptions', on_delete=m.PROTECT)
    service = m.ForeignKey(Service, related_name='services', on_delete=m.PROTECT)
    plan = m.ForeignKey(Plan, related_name='plans', on_delete=m.PROTECT)
