# Generated by Django 3.2.12 on 2023-02-01 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20230201_0903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction_listings',
            old_name='username',
            new_name='user_id',
        ),
    ]
