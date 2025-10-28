from django.urls import path
from .views import MyTokenObtainPairView, MyTokenRefreshView, LogoutView, ProtectedView

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view()),
    path('token/refresh/', MyTokenRefreshView.as_view()),
    path('token/logout/', LogoutView.as_view()),
    path('protected/', ProtectedView.as_view()),
]
