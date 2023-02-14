from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    pass
    

class Category(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.name}"



class Auction_listings(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    bid_amount = models.IntegerField()
    image = models.ImageField(upload_to='images/', default='images/default.jpg')
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    bids = models.ManyToManyField(User, through='Bid', blank=True, related_name="auction_listings", null=True)
    comments = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)


    class Meta:
        verbose_name_plural = 'Auction_listings'

    def __str__(self):
        return f"{self.title}"


class Bid(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    auction_listing = models.ForeignKey(Auction_listings, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.bid
