from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ContactForm

# Create your views here.


def index(request):
    contacts = Contact.objects.all()
    context = {'title': 'Контакты', 'contacts': contacts}
    return render(request, 'index.html', context)


def display_contacts(request):
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts,
        'header': 'Контакты',
    }
    return render(request, 'index.html', context)


def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    context = {
        'contact': contact,
    }
    return render(request, 'contact_detail.html', context)


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm()
        context = {
            'form': form,
            'header': 'Добавление контакта'
        }
        return render(request, 'add_contact.html', context)


def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm(instance=contact)
        context = {
            'form': form,
            'header': 'Редактирование контакта'
        }
        return render(request, 'edit_contact.html', context)


def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('index')


def search_contacts(request):
    last_name = request.GET.get('last_name')
    contacts = Contact.objects.filter(last_name__icontains=last_name)
    header = f"Search results for '{last_name}'"

    return render(request, 'index.html', {'contacts': contacts, 'header': header})


def print_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'index.html', {'contacts': contacts})
