from django.urls import path

from .views import *
urlpatterns = [
    
    path('', hello ),
    
    path('list/' , listEvents , name="listfunction"),
    
    path('listClass/' , EventList.as_view() , name="listClass"),
    
    path('details/<int:ide>', details , name="details"),
    
    path('detailsClass/<str:pk>',  DetailsEvent.as_view()    , name="detailsClass")
]