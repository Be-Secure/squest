# Generated by Django 3.2.12 on 2022-06-14 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_quota_quotabinding'),
        ('service_catalog', '0008_alter_supportmessage_support'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='approvalstepstate',
            unique_together={('request', 'approval_step', 'team')},
        ),
    ]
