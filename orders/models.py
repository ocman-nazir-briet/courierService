from django.db import models
import uuid
from django.utils import timezone
from .utils import *

# Create your models here.
class Item(models.Model):
    City=(
    ('Lhr','Lahore'),
    ('Isl','Islamabad'),
    ('Rwp','Rawalpindi'),
    ('Mln','Multan'),
    ('Bwp','Bahawalpur'),
    ('Okr','Okara'),
    ('Ksr','Kasur'),
    ('Gjr','Gujranwala'),
    ('DGK','DG Khan'),
    ('Fsd','Faisalabad'),
    )

    delivery=(
        ('Processing','Processing'),
        ('On the Way','On the Way'),
        ('Delivered','Delivered'),
        ('Cancelled','Cancelled')
    )
    order_id = models.CharField(max_length=156, blank=True)
    sender_name = models.CharField(help_text='Sender', max_length=128)
    from_city=models.CharField(help_text='Sender', max_length=32, choices=City)
    sender_address = models.CharField(help_text='Sender', max_length=1024)
    sender_phone = models.CharField(help_text='Sender', max_length=1024)

    receiver_name = models.CharField(help_text='Receiver', max_length=128)
    to_city=models.CharField(help_text='Receiver', max_length=32, choices=City)
    receiver_address = models.CharField(help_text='Receiver', max_length=1024)
    receiver_phone = models.CharField(help_text='Receiver', max_length=1024)

    insurance = models.BooleanField(default=False)

    created=models.DateTimeField(blank=True)
    updated=models.DateTimeField(auto_now=True)

    current_status= models.CharField(help_text='Current Location', max_length=32, choices=City)

    delivery_status = models.CharField(help_text='Delivery Status', default="Processing", max_length=32, choices=delivery)


    def save(self, *args, **kwargs):
        if self.order_id == "":                                       
            self.order_id = generate_code()
        if self.created is None:
            self.created = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.order_id}-{self.receiver_name}"

class RateCheck(models.Model):
    from_city = models.CharField(max_length=50)
    to_city = models.CharField(max_length=50)
    weight = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return self.from_city

class news(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1024)
    image = models.ImageField(upload_to="news")

    def __str__(self):
        return self.title
