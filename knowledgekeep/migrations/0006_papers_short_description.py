# Generated by Django 4.2.5 on 2023-11-06 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledgekeep', '0005_rename_subsciption_type_userprofile_subscription_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='papers',
            name='short_description',
            field=models.TextField(null=True),
        ),
    ]
