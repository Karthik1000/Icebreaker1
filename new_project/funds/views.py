from django.shortcuts import render
from .models import *
from .forms import Contribute_form

# Create your views here.
def funds_table(request):
    context = Funding.objects.all()
    return render(request, 'funds/funds_table.html', {'context': context})


def funds_view(request):
    if request.method == 'POST':
        form = Contribute_form(request.POST or None)
        if form.is_valid():
            campaign = form.save(commit=False)
            
            form.save()
            context = Funding.objects.all()
            return render(request, 'funds/funds_table.html', {'context': context})
    else:
        form = Contribute_form()
    return render(request, 'funds/contribute_form.html', {'form': form})
