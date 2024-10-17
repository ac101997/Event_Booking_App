# Generated by Django 5.1.1 on 2024-10-14 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventBookingApp', '0005_alter_tickets_ticket_type'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='tickets',
            constraint=models.UniqueConstraint(fields=('event', 'ticket_type'), name='unique-ticket'),
        ),
    ]