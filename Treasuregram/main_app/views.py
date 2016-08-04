from django.shortcuts import render
# NO LONGER NEEDED from django.http import HttpResponse


#Create views here
def index(request):
    name = 'Gold Nugget'
    value = 1000.00
    context = {'treasure_name' : name, 'treasure_val': value}

    return render(request, 'index.html', context)

