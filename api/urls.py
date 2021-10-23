from django.urls import path
from .views import (
	follow,
	like,
	like_info,
	retweet,
	follow_info,
)


app_name = "api"
urlpatterns = [
	path('like/<str:app_name>/<str:url_name>/<int:pk>/', like, name="like" ),
	path('retweet/<str:app_name>/<str:url_name>/<int:pk>/', retweet, name="retweet"),
	path('<int:pk>/', like_info, name="like-info"),
	path('<str:username>/', follow_info, name="follow-info"),
	path('following/<str:app_name>/<str:url_name>/<str:username>/', follow, name="follow"),
]