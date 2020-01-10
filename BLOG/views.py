from django.shortcuts import render, get_object_or_404
from .models import BLOG


def allBlogs(request):
    blogs = BLOG.objects
    return render(request, 'allblogs.html', {"blogs": blogs})


def detail(request, id):
    blog = get_object_or_404(BLOG, pk=id)
    return render(request, 'details.html', {"blog": blog})
