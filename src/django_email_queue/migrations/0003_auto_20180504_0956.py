# Generated by Django 2.0.3 on 2018-05-04 09:56

from django.db import migrations, models
import django_email_queue.models


class Migration(migrations.Migration):

    dependencies = [
        ('django_email_queue', '0002_auto_20180412_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='queuedemailmessage',
            name='ts',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='queuedemailmessage',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Created'), (1, 'Posted'), (2, 'Sending'), (3, 'Discarded')], default=django_email_queue.models.QueuedEmailMessageStatus(0)),
        ),
    ]
