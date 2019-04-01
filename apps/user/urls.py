from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_active/<token>', views.user_active, name='user_active'),
]
