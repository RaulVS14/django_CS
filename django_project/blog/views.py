from django.shortcuts import render


# dummy data
posts = [
    {
        'author': 'R',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'S',
        'title': 'Blog Post 2',
        'content': 'Then add title',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'T',
        'title': 'Blog Post 3',
        'content': 'Lastly sign it',
        'date_posted': 'August 27, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
