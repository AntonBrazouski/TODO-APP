from django.urls import path
from . import views 
from todo.views import HomeView, ItemView, ItemCreate, ItemDelete, ItemUpdate, ItemList 


urlpatterns = [
	#path('', views.index, name='index'),
	#path('home',views.HomeView.as_view(), name='home'),
	
	#path('<int:pk>/' ,views.DetailView.as_view(), name='detail'),
	#path('<int:pk>/' ,views.DetailView.as_view(), name='item-detail'),
	
	#path('thanks/', views.ItemView.as_view(), name='thanks'),
	#path('item/', ItemView.as_view(), name='item-view'),
	
	path('item/add/', ItemCreate.as_view(), name='item-add'),
	path('item/<int:pk>/', ItemUpdate.as_view(), name='item-update'),
	path('item/<int:pk>/delete/', ItemDelete.as_view(), name='item-delete'),
	
	path('', ItemList.as_view(), name='item-list'),
	
]
