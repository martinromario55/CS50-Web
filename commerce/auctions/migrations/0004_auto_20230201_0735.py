# Generated by Django 3.2.12 on 2023-02-01 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20230201_0730'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auction_listings',
            options={'verbose_name_plural': 'Auction_listing'},
        ),
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name_plural': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name_plural': 'Comment'},
        ),
    ]
