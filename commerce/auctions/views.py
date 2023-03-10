from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import User
from .forms import *
from django.contrib.auth.decorators import login_required
import uuid


def index(request):
    # Show all listings
    listings = Auction_listings.objects.all()
    # for list in listings:
        # print(list.id)
    # Show user listings
    if request.user.is_authenticated:
        # Get current user
        current_user = User.objects.get(username=request.user.username)
        # Get all listings
        current_user_list = Auction_listings.objects.filter(user_id=current_user)
        # for list in current_user_list:
        #     print(list.title, list.description)
        return render(request, "auctions/index.html", {"current_user_list":current_user_list, "listings":listings})
    return render(request, "auctions/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def create_listing(request):
    # POST
    if request.method == "POST":
        # Save user data in a form
        form = CreateListingForm(request.POST, request.FILES)
        
        # Check if form is valid
        if form.is_valid():
            # Isolate the data
            data = form.save(commit=False)
            # Add username
            username = request.user.username
            user = User.objects.get(username=username)
            data.user = user

            data.save()
            return HttpResponseRedirect(reverse("index"))

        else:
            form = CreateListingForm(request.POST)
            return render(request, "auctions/create_listing.html", {"message": "Failed to create Listing", "form":form})


    form = CreateListingForm()
    return render(request, 'auctions/create_listing.html', {"form":form})



def list_view(request, title):
    list = get_object_or_404(Auction_listings,title=title)
    return render(request, 'auctions/list_view.html', {"list":list})