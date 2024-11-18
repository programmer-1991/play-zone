from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Contact
from .forms import ContactForm
# Create your views here.


def contact(request):
    """ Leave a message to the store """
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save()
            messages.success(request, 'Message Sent!')
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Failed to send a message!')
    else:
        form = ContactForm()
        
    template = 'contact/contact.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
