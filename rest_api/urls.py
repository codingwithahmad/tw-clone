from django.urls import path
from .views import (
	LikeView,
	RetweetView,
	LikeDetails,
	RetweetDetails,
	MakeLike,
	MakeRetweet,
	Twits,
)

app_name = "rest_api"

urlpatterns = [
	path('twits', Twits.as_view(), name='twits'),


	path('likes', LikeView.as_view(), name='likes'),
	path('likes/<int:pk>', LikeDetails.as_view(), name='likes-details'),
	path('likes/create/', MakeLike.as_view(), name='make-like'),

	path('retweets', RetweetView.as_view(), name='retweets'),
	path('retweets/<int:pk>', RetweetDetails.as_view(), name='retweets-details'),
	path('retweets/create/', MakeRetweet.as_view(), name='make-retweets'),
]