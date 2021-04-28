from travello.models import Destination
from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    
    
    # dest1 = Destination()
    # dest1.name = 'Mumbai'
    # dest1.img = 'destination_1.jpg'
    # dest1.price = 999
    # dest1.desc = 'A city that never sleeps'
    # dest1.offer = True
    # dest2 = Destination()
    # dest2.name ='Delhi'
    # dest2.img = 'destination_2.jpg'
    # dest2.price = 999
    # dest2.desc = 'A pride capital of country'
    # dest3 = Destination()
    # dest3.name = 'Nagpur'
    # dest3.img = 'destination_3.jpg'
    # dest3.price = 999
    # dest3.desc = 'City of Oranges'

    # dests = [dest1,dest2,dest3]

    dests = Destination.objects.all()
    return render(request, "index.html",{'dests':dests})