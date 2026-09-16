from django.contrib import admin
from django.urls import path
from core.views import (
    JobListAPIView,
    UserTestAPIView,
    SignupAPIView,
    LogoutAPIView,
    CandidateProfileAPIView,
    EmployerProfileAPIView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/jobs/', JobListAPIView.as_view()),
    path('api/user-test/', UserTestAPIView.as_view()),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/signup/', SignupAPIView.as_view(), name='signup'),
    path('api/logout/', LogoutAPIView.as_view(), name='logout'),

    path(
    'api/candidate/profile/',
    CandidateProfileAPIView.as_view(),
    name='candidate-profile'
),
path(
    'api/employer/profile/',
    EmployerProfileAPIView.as_view(),
    name='employer-profile'
),
]