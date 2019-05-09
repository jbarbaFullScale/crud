from django.urls import path

from . import views

urlpatterns = [
    path('sort_array', views.sort_array, name='sort_array'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:book_id>/delete', views.delete_book, name='delete'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('add_update_book/', views.add_update_book, name='add_update_book'),
    path('<int:book_id>/add_update_book/', views.add_update_book, name='add_update_book'),
]