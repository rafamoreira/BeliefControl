from django.shortcuts import render, get_object_or_404
from .models import Article


# Create your views here.
def home_view(request):
    qs = Article.objects.all()
    template_name = 'home.html'
    context = {'object_list': qs}
    return render(request, template_name, context)


def read_article(request, slug):
    obj = get_object_or_404(Article, slug=slug)
    template_name = 'read_article.html'
    context = {'object': obj}
    return render(request, template_name, context)


