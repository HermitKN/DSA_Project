from django.urls import path
from .views import Sign_Up, log_out, log_in

urlpatterns = [ 

    path('',Sign_Up.as_view(), name="SignUp"),
    path('log_out',log_out, name="Logout"),
    path('log_in',log_in, name="Login"),
]