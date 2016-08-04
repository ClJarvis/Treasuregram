from django.shortcuts import render
# NO LONGER NEEDED from django.http import HttpResponse
from models import Treasure


#Create views here
def index(request):
  #  name = 'Gold Nugget'
   # value = 1000.00
    #context = {'treasure_name' : name, 'treasure_val': value}
    treasures = Treasure.objects.all()
    return render(request, 'index.html', {'treasure': treasures})

