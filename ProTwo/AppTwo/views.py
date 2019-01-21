from django.shortcuts import render
from AppTwo.forms import NewUserForm
# from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'AppTwo/index.html')


def user(request):

    form = NewUserForm()

    
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)

        else:
            print('ERROR FORM IS INVALID')

    return render(request,'AppTwo/user.html',{'form':form})
