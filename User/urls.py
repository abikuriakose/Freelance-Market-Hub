from django.urls import path
from User import views
app_name="User"

urlpatterns=[
    path("Home/",views.Home,name="Home"),
    path('Myprofile/',views.Myprofile,name="Myprofile"),
    path('Editprofile/',views.Editprofile,name="Editprofile"),
    path('Changepassword/',views.Changepassword,name="Changepassword"),
    path('Complaint/',views.Complaint,name="Complaint")
]