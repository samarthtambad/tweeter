from django.urls import path
from tweets.views import (
    home_view, 
    tweet_action_view,
    tweet_delete_view,
    tweet_detailed_view, 
    tweet_list_view,
    tweet_create_view,
)

urlpatterns = [
    path('', tweet_list_view),
    path('action/', tweet_action_view),
    path('create/', tweet_create_view),
    path('<int:tweet_id>/', tweet_detailed_view),
    path('<int:tweet_id>/delete/', tweet_delete_view),
]
