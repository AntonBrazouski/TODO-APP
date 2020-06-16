from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, FormView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from todo.models import Item
from todo.forms import ItemForm 
from django.urls import reverse_lazy

## unused

def index(request):
	return HttpResponse('hi todo')

class HomeView(TemplateView):
	template_name = 'todo/base.html'
	
class DetailView(DetailView):
	model = Item
	template_name = 'todo/detail.html'

class ItemView(FormView):
	template_name = 'todo/item.html'
	form_class = ItemForm
	success_url = '/thanks/'
##

class ItemCreate(CreateView):
	model = Item 
	fields = ['item_text']
	success_url = reverse_lazy('item-list')
	
class ItemUpdate(UpdateView):
	model = Item 
	fields = ['item_text','done']
	success_url = reverse_lazy('item-list')
	
class ItemDelete(DeleteView):
	model = Item 
	success_url = reverse_lazy('item-list')	

class ItemList(ListView):
	model = Item 
