from django.urls import path
from .views import LikeView, RetweetView, LikeDetails, RetweetDetails

app_name = "rest_api"

urlpatterns = [
	path("likes", LikeView.as_view(), name="likes"),
	path("likes/<int:pk>", LikeDetails.as_view(), name="likes-details"),
	path('retweets', RetweetView.as_view(), name='retweets'),
	path('retweets/<int:pk>', RetweetDetails.as_view(), name='retweets-details'),
]