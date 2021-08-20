from django.shortcuts import render, redirect
from .models import Url

# Create your views here.
def index(request):
    todos = Url.objects.all()
    if request.method =='POST':
        title = request.POST['title']
        new_mess = Url(title = title)
        new_mess.save()
        return redirect('/')
    return render(request, 'index.html', {'todos':todos})

def delete(request, pk):
    now = Url.objects.get(id = pk)
    now.delete()
    return redirect('/')
    