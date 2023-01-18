from django.shortcuts import render

posts=[
    {
    'author':'Proffessor',
    'title':'Django tutorial',
    'content':'Tutorials',
    'date_posted':'December 22,2021'
    },
    {
    'author':'Teacher',
    'title':'Python tutorial',
    'content':'Tutorial 2',
    'date_posted':'August 2,2021'
    }
]

def home(request):
    context={
        'posts':posts
    }
    return render (request, 'blog/home.html',context)

def about(request):
    return render (request, 'blog/about.html',{'title': 'about'})

