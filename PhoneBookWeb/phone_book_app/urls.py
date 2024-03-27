from django.urls import path
from .import views


urlpatterns = [

    # Маршруты
    path('', views.index, name='index'),  # общий маршрут

    # Контакты
    path('display_contacts/', views.display_contacts, name='display_contacts'),
    path('contact/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('edit_contact/<int:pk>/', views.edit_contact, name='edit_contact'),
    path('delete_contact/<int:pk>/', views.delete_contact, name='delete_contact'),
    path('search_contacts/', views.search_contacts, name='search_contacts'),
    path('print_contacts/', views.print_contacts, name='print_contacts'),
]
