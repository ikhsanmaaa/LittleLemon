from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import BookingForm
from django.http import JsonResponse

# Create your views here.

@csrf_exempt
def form_view(request):
    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message':'success'})
        else:
            return JsonResponse({'message' : 'error', 'errors':form.errors},status = 400)
    else:
        form = BookingForm()
    return render (request,'snippets/booking.html',{'form':form})