
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_post", views.new_post, name="new_post"),
    path("profile/<user_id>", views.profile, name="profile"),
    path("add_follower/<user_id>", views.add_follower, name="add_follower"),
    path("remove_follower/<user_id>", views.remove_follower, name="remove_follower"),
    path("following", views.following, name="following"),
    path("edit_post/<post_id>", views.edit_post, name="edit_post"),    
    path("like_post/<post_id>", views.like_post, name="like_post"),
]
