from django.urls import path
from .views import TimeLine

app_name="twits"

urlpatterns = [

	path('', TimeLine.as_view(), name="TimeLine"),
	
]