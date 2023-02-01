# Generated by Django 3.2.12 on 2023-02-01 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users', models.ManyToManyField(blank=True, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users', models.ManyToManyField(blank=True, related_name='bids', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Auction_listings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=255)),
                ('bid_amount', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/')),
                ('active', models.BooleanField(default=True)),
                ('bids', models.ManyToManyField(blank=True, related_name='auction_listings', to='auctions.Bid')),
                ('category', models.ManyToManyField(blank=True, related_name='category', to='auctions.Categories')),
                ('comments', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='auction_list', to='auctions.comments')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auctions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
