from django.urls import path
from .views import TimeLine, TwitDetail, like, like_info, retweet

app_name="twits"

urlpatterns = [

	path('', TimeLine.as_view(), name="TimeLine"),
	path('api/like/<str:app_name>/<str:url_name>/<int:pk>/', like, name="like" ),
	path('api/retweet/<str:app_name>/<str:url_name>/<int:pk>/', retweet, name="retweet" ),
	path('api/<int:pk>/', like_info, name="like-info"),
	path('twit/<int:pk>/', TwitDetail.as_view(), name="TwitDetail")
	
]