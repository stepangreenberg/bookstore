from .models import Book
from django.views import generic

class BookListView(generic.ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "book_list"



class BookDetailView(generic.DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"
