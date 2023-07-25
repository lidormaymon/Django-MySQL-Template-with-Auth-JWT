from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
    path('user', views.get_user_info),
    path('register/', views.register),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', views.MyTokenObtainPairView11.as_view()),
    path('get_all_images', views.getImages),
    path('upload_image',views.APIViews.as_view()),
]

