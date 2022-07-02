from django.urls import path
from account.views import *

urlpatterns = [
    path('account/login/', LoginForm.as_view(), name='login'),
    path('account/logout/', Logout.as_view(), name='logout'),
    path('account/register/', RegisterForm.as_view(), name='register'),

]