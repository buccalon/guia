# django core imports
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

# project guia imports
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('login/', views.login, name='login'),
    path('forgot-password/', views.ForgotPasswordView.as_view(), name='forgot-password'),
    path('forgot-password/success/', views.ForgotPasswordSuccessView.as_view(), name='forgot-password-success'),
    path('reset-password/<str:token>/', views.ResetPasswordFormView.as_view(), name='reset-password'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
