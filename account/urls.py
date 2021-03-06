from django.contrib.auth import views
from django.urls import path
from .views import Profile, Registration, activate, EditProfile

app_name = "account"

urlpatterns = [
    path('login/', views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    # path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    path("register/", Registration.as_view(), name="register"),
    path("activate/<uidb64>/<token>/", activate, name="activate"),
]



urlpatterns += [
    # path('twit', Twit.as_view(), name='tw'),
    path('<slug:username>/', Profile.as_view(), name="profile"),
    path('update/<int:pk>', EditProfile.as_view(), name="edit_profile"),
]