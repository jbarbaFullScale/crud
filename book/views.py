from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from .models import Book
import json


class IndexView(generic.ListView):
	template_name = 'index.html'
	context_object_name = 'latest_book_list'

	def get_queryset(self):
		return Book.objects.order_by('-name')[:5]

class DetailView(generic.DetailView):
	model = Book
	template_name = 'detail.html'

class ResultsView(generic.DetailView):
	template_name = 'results.html'

def add_update_book(request, book_id=None):
	book = get_object_or_404(Book, pk=book_id) if book_id else Book()
	book.name = request.POST['name']
	book.pages = request.POST['pages']
	book.save()
	return HttpResponseRedirect(reverse('index'))

def delete_book(request, book_id):
	if book_id:
		book = Book.objects.get(id=book_id)
		book.delete()
	return HttpResponseRedirect(reverse('index'))

@csrf_exempt
def sort_array(request):
	unsorted_array = request.POST['unsorted_array']
	# if unsorted_array:
	# unsorted_array = json.loads(unsorted_array)
	print (unsorted_array)
	print (type(unsorted_array))
	return json.dumps({
		'status_code': 200,
		'sorted_array': unsorted_array.sort() if unsorted_array else []
	})