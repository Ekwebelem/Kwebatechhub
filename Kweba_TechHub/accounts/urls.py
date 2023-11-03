from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('softwaredev/', views.softwaredev, name='softwaredev'),
    path('businessdev/', views.businessdev, name='businessdev'),
    path('ui_ux/', views.ui_ux, name='ui_ux'),
    path('crypto/', views.crypto, name='crypto'),
    path('career/', views.career, name='career'),
    path('privacy/', views.privacy, name='privacy'),
    path('contact/', views.contact, name='contact'),
    path('ourservices/', views.ourservices, name='ourservices'),
    path('project/', views.project, name='project'),
    path('marketer/', views.marketer, name='marketer'),
#    path('upload_pdf/', views.upload_pdf, name='upload_pdf'),
    path('submit_application/', views.submit_application, name='submit_application'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout')
]



# urls.py
