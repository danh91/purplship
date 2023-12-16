# Generated by Django 3.2.10 on 2022-01-13 11:58

from django.db import migrations, models
import functools
import karrio.server.core.utils


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0024_alter_parcel_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='pickup',
            name='metadata',
            field=models.JSONField(blank=True, default=functools.partial(karrio.server.core.utils.identity, *(), **{'value': {}}), null=True),
        ),
        migrations.AddField(
            model_name='tracking',
            name='metadata',
            field=models.JSONField(blank=True, default=functools.partial(karrio.server.core.utils.identity, *(), **{'value': {}}), null=True),
        ),
    ]