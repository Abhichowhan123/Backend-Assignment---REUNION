from rest_framework_simplejwt.views import (TokenObtainPairView
,TokenRefreshView,
TokenVerifyView
                                            )

from django.urls import path
from .views import *

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', Login.as_view()),
    path('logout', Logout.as_view()),
    path('follow/<int:pk>', FollowView.as_view({'post': 'follow'})),
    path('unfollow/<int:pk>', FollowView.as_view({'post': 'unfollow'})),
]
