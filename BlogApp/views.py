from django.shortcuts import render , HttpResponse , redirect

from .models import BlogModel

from .forms import BlogForm

# Create your views here.


def home_view(request):
    # return HttpResponse("home page")

    blogs = BlogModel.objects.all()

    context = {'blogs':blogs}

    return render(request , 'home.html' , context)

def dashboard_view(request):

    blogs = BlogModel.objects.all()

    context = {'blogs':blogs}

    return render(request , 'dashboard.html' , context)

def addblog_view(request):

    forms = BlogForm()
    if request.method == 'POST':
        forms = BlogForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('dashboard')
    context = {'forms':forms}
    return render(request , 'addblog.html' , context)


def deleteblog_view(request , id):
    print(id)

    blog = BlogModel.objects.get(id = id)
    blog.delete()

    return redirect('dashboard')


def updateblog_view(request , id):
    blog = BlogModel.objects.get(id = id)

    context = {'blog':blog}

    return render(request , 'updateblog.html' , context)


    