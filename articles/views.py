from django.shortcuts import render
from datetime import datetime
from .models import all_info
from django.contrib import messages

# Create your views here.
def article_info(request):
    return render(request,'home.html')
def forms(request):

    if request.method == "POST":
        email = request.POST.get('email')
        author = request.POST.get('author')
        title = request.POST.get('title')
        content = request.POST.get('content')
        form = all_info(email=email,author=author,title=title,content=content,date=datetime.today())
        form.save()
        messages.success(request, 'Your Article has been sent.')
    return render(request,'form.html')
def home(request):
    return render(request,'home.html')

def article(request):
    writers = all_info.objects.all()
    para = {'writer':writers}
    return render(request,'article.html',para)

def main(request):
    writers = all_info.objects.get(title='CoronaVirus Shutdowns')
    para = {'selected':writers}
    return render(request,'main.html',para)