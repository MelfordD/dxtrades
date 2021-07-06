from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import *

# Create your views here.


@login_required   
def wallet(request):
	#return HttpResponse("about")
    #valuenext=request.POST.get('next')
    #user = Balance.objects.all()
    balance = Balance.objects.all()
    return render(request, 'wallet.html', {'balance':balance})
    
    
    
'''class WalletView(generic.WalletView):
    model = Balance
    template_name = 'polls/detail.html'
    def get_queryset(self): 
        """ Excludes any questions that aren't published yet. """ 
        return Balance.objects.all()'''