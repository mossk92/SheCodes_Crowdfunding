from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
     path('users/', views.CustomUserList.as_view()),
     path('users/<int:pk>/', views.CustomUserDetail.as_view()),
     path('api-token-auth/', obtain_auth_token)
]
urlpatterns = format_suffix_patterns(urlpatterns)