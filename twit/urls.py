from django.urls import path
from .views import TimeLine, TwitDetail, like

app_name="twits"

urlpatterns = [

	path('', TimeLine.as_view(), name="TimeLine"),
	path('api/<str:app_name>/<str:url_name>/<int:pk>/', like, name="like" ),
	path('twit/<int:pk>/', TwitDetail.as_view(), name="TwitDetail")
	
]