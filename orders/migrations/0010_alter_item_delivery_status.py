# Generated by Django 4.1.3 on 2022-11-07 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_news_ratecheck'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='delivery_status',
            field=models.CharField(choices=[('Processing', 'Processing'), ('On the Way', 'On the Way'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Processing', help_text='Delivery Status', max_length=32),
        ),
    ]
