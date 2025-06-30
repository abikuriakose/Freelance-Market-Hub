from django.urls import path,include
from Basic import views

urlpatterns = [
    path('Sum/',views.Sum,name="Sum"),
    path('Calculator/',views.Calculator,name="Calculator"),
    path('LandS/',views.LandS,name="LandS"),
    path('Rank/',views.Rank,name="Rank"),
]