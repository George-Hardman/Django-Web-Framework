from django.shortcuts import render


posts = [
    {
        'author': 'GeorgeHardman',
        'title': 'Blog post 1',
        'content': 'First Post Content',
        'date_posted': 'January 29, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog post 2',
        'content': 'Second Post Content',
        'date_posted': 'January 30, 2020'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
