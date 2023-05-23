from django.urls import path
from .views import StreamPlatformAV,StreamPlatformDetailsAV, WatchListAV, WatchDetailsAV
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView,TokenVerifyView

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('list/<int:pk>/', WatchDetailsAV.as_view() , name='watch-details'),
    path('stream/', StreamPlatformAV.as_view() , name='Stream-Platform'),
    path('stream/<int:pk>/', StreamPlatformDetailsAV.as_view() , name='StreamPlatform-Details'),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),



    
    
    
    
    
]