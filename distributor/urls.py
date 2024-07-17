from django.urls import path
from distributor import views


urlpatterns = [
    path("items_details/",views.items_details,name="items_details"),
    path("",views.index,name="index"),
    path("registration/",views.registration,name="registration"),
    path("login1/",views.login1,name="login1"),
    path("requirements/",views.requirements,name="requirements"),
    
]

