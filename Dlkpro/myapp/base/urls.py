from django.urls import path
from.import views


urlpatterns = [
    path('', views.splash, name='splash'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('portfolio/',views.portfolio,name='portfolio'),
     path('logout/',views.logout,name='logout')
]
