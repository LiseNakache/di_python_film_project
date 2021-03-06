from django.urls import path
from . import views

app_name = 'account_app'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_auth, name='login'),
    path('logout/', views.logout_auth, name='logout'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
]
