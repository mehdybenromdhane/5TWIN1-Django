from django.shortcuts import render

# Create your views here.



def hello(request):
    
    classe= "5 TWIN1"
    
    return render(request, "event/bonjour.html" , {"c1":classe})