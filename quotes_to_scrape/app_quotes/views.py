from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required

from .forms import AuthorForm, TagForm, QuoteForm
from .models import Author, Tag, Quote


# Create your views here.
def main(request):
    quotes = Quote.objects.all()
    paginator = Paginator(quotes, 10)
    page = request.GET.get('page')
    try:
        quotes = paginator.page(page)
    except PageNotAnInteger:
        quotes = paginator.page(1)
    except EmptyPage:
        quotes = paginator.page(
            paginator.num_pages)
    return render(request, 'app_quotes/index.html', context={'title': 'Quotes to Scrape', 'quotes': quotes})


@login_required
def tag(request):
    form = TagForm(instance=Tag())
    if request.method == 'POST':
        form = TagForm(request.POST, instance=Tag())
        if form.is_valid():
            form.save()
            return redirect(to='app_quotes:root')
    return render(request, 'app_quotes/tag.html', context={'title': 'Quotes to Scrape', 'form': form})


@login_required
def add_quote(request):
    form = QuoteForm(instance=Quote())
    if request.method == 'POST':
        form = QuoteForm(request.POST, instance=Quote())
        if form.is_valid():
            form.save()
            return redirect(to='app_quotes:root')
    return render(request, 'app_quotes/add_quote.html',
                  context={'title': 'Quotes to Scrape', 'form': form})


@login_required
def add_author(request):
    form = AuthorForm(instance=Author())
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=Author())
        if form.is_valid():
            form.save()
            return redirect(to='app_quotes:root')
    return render(request, 'app_quotes/add_author.html', context={'title': 'Quotes to Scrape', 'form': form})


def author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'app_quotes/author.html', {'author': author})
