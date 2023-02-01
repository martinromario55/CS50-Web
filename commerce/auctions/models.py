from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime




class User(AbstractUser):
    pass


class Bid(models.Model):
    users = models.ManyToManyField(User, blank=True, related_name="bids")
    bid = models.IntegerField(null=True)


    def __str__(self):
        return self.bid
    


class Comments(models.Model):
    users = models.ManyToManyField(User, blank=True, related_name="comments")
    comment = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.comment


class Categories(models.Model):
    title = models.CharField(max_length=64)


    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.title}"



class Auction_listings(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    bid_amount = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    created_date = models.DateTimeField
    active = models.BooleanField(default=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auctions")
    bids = models.ManyToManyField(Bid, blank=True, related_name="auction_listings", null=True)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name="auction_list", blank=True, null=True)
    category = models.ManyToManyField(Categories, blank=True, related_name="category", null=True)


    class Meta:
        verbose_name_plural = 'Auction_listings'

    def __str__(self):
        return f"{self.title}"