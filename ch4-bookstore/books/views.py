from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from books.models import Book


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'book_list'


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'
    login_url = 'account_login'
    permission_required = 'books.special_status'


class SearchResultsView(ListView):
    model = Book
    template_name = 'book/search_results.html'
    context_object_name = 'book_list'

    # search
    def get_queryset(self):  # new
        return Book.objects.filter(
            Q(title__icontains='мос') | Q(title__icontains='пет')
            Q(title__icontains='мос') | Q(title__icontains='пет')
        )




