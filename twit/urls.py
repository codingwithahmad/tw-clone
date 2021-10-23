from django.urls import path
from .views import TimeLine, TwitDetail

app_name="twits"

urlpatterns = [

	path('', TimeLine.as_view(), name="TimeLine"),
	path('twit/<int:pk>/', TwitDetail.as_view(), name="TwitDetail")
	
]