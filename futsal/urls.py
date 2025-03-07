from django.urls import path
from . import views
from .views import home,login_view,signup_view,logout_view

urlpatterns = [
    # path('',views.all_user),
    path('',home, name='home'),
    path('login/',login_view,name='login'),
    path('signup/',signup_view,name='signup'),
    path('logout/',logout_view,name='logout')
]
