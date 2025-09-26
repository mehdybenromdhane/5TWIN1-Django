from django.shortcuts import render

# Create your views here.
from .models import Event
from django.views.generic import ListView, DeleteView,DetailView,CreateView,UpdateView

def hello(request):
    
    classe= "5 TWIN1"
    
    return render(request, "event/bonjour.html" , {"c1":classe})



def listEvents(request):
    
    
    events = Event.objects.filter(state=True)
    
    
    return render(request,'event/list.html' , {"list":events})



class EventList(ListView):
    
    model =Event
    
    template_name='event/list.html'
    
    context_object_name="list"
    
    

def details(request, ide):
    
    event =Event.objects.get(id=ide)
    
    
    return render(request, 'event/details.html' , {'event':event})



class DetailsEvent(DetailView):
    
    model=Event
    template_name="event/details.html"
    context_object_name="event"