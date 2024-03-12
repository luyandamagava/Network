from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Comment, Post
from django.contrib import messages
from django.core.paginator import Paginator


def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')

    return render(request, "network/index.html", {
        "posts": posts,
        "page_obj": paginator.get_page(page_number)
        
    })


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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
    
def new_post(request):
    if request.method == "POST":
        content = request.POST["new_post_text"]
        post = Post(creator=request.user, content=content)
        post.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/new_post.html")
    
def profile(request, user_id):

                                                        # - here the signed in user is trying to view the profile of the profile user
    profile_user = User.objects.get(pk=user_id)
    posts = profile_user.creator_posts.all()            # The posts of the profile user
    following = profile_user.following.all()            # The list of users objects that the profile user is following
    followingNum = len(following)                       # The number of users that the profile user is following
    followers = profile_user.followers.all()             # The list of user objects that are following the profile user
    followersNum = len(followers)                       # The number of users that are following the profile user
    followers_list = []

    for follower in followers:
        followers_list.append(follower.id)     # The list of user ids that are following the profile user
    
    return render(request, "network/profile.html", {
        "profile_user": profile_user,
        "posts": posts,
        "following": following,
        "followingNum": followingNum,
        "followers": followers_list,
        "followersNum": followersNum,
        "logged_in_user": request.user
    })

def add_follower(request, user_id):
                                                                        # here the signed in user is trying to follow the profile user
    profile_user = User.objects.get(pk=user_id)                         # The user object you're trying to follow
    profile_user_followers = profile_user.followers.all()               # The list of users that are following the user object you're trying to follow
    logged_in_username = request.user
    logged_in_user = User.objects.get(username=logged_in_username)      # The user object of the logged in user

    if logged_in_user in profile_user_followers:                        # check if the logged in user is following the profile user
        messages.error(request, 'You are already following this user!')
        return HttpResponseRedirect(reverse("profile", args=(user_id,)))
    
    else:
        profile_user.followers.add(logged_in_user)
        logged_in_user.following.add(profile_user)
        return HttpResponseRedirect(reverse("profile", args=(user_id,)))
    
def remove_follower(request, user_id):
                                                                        # here the signed in user is trying to unfollow the profile user
    profile_user = User.objects.get(pk=user_id)                         # The user object you're trying to unfollow
    profile_user_followers = profile_user.followers.all()               # The list of users that are following the user object you're trying to unfollow
    logged_in_username = request.user
    logged_in_user = User.objects.get(username=logged_in_username)      # The user object of the logged in user

    if logged_in_user not in profile_user_followers:                    # check if the logged in user is following the profile user
        messages.error(request, 'You are not following this user!')
        return HttpResponseRedirect(reverse("profile", args=(user_id,)))
    
    else:
        profile_user.followers.remove(logged_in_user)
        logged_in_user.following.remove(profile_user)
        return HttpResponseRedirect(reverse("profile", args=(user_id,)))
    
def following(request):
    logged_in_user = request.user
    following = logged_in_user.following.all() # The list of users that the logged in user is following
    follower_posts = []

    for follow in following:
        posts = follow.creator_posts.all()
        for post in posts:
            follower_posts.append(post)        

    
    return render(request, "network/following.html", {
        "posts": follower_posts,
    })

def edit_post(request, post_id):        
    post = Post.objects.get(pk=post_id)
    if request.method == "POST":
        post.content = request.POST["edit_post_text"]
        post.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/edit_post.html", {
            "post": post
        })