from django.urls import path
from firstapp.views import *

urlpatterns = [
    path('', hellodjango),
    path('date/', date),
    path('date/<value>', date),
    path('<str:name>/', usname),
]
