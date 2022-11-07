from django.shortcuts import render
from .models import Item
from .forms import OrderTrackForm

def index(request):
    return render(request, 'index.html')
def tracking(request):
    obj=""
    form = OrderTrackForm(request.POST)
    if request.method == "POST":
        id = request.POST.get('order_id')
        obj=Item.objects.filter(order_id=id)
    return render(request, 'track.html', {'form':form, 'obj':obj})
    