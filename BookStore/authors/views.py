from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Author
from .forms import AuthorForm


class AuthorListView(ListView):
    model = Author
    template_name = "authors/index.html"
    context_object_name = "authors"


class AuthorDetailView(DetailView):
    model = Author
    template_name = "authors/view.html"
    context_object_name = "author"
    pk_url_kwarg = "id"


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = "authors/create.html"

    def get_success_url(self):
        return reverse_lazy("authors.show", kwargs={"id": self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = False
        context["author"] = None
        return context


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = "authors/create.html"
    pk_url_kwarg = "id"

    def get_success_url(self):
        return reverse_lazy("authors.show", kwargs={"id": self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


class AuthorDeleteView(DeleteView):
    model = Author
    pk_url_kwarg = "id"
    success_url = reverse_lazy("authors.index")

    def get(self, request, *args, **kwargs):
        author = self.get_object()
        return redirect("authors.show", id=author.id)