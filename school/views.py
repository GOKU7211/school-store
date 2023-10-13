from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .form import Location
from school.models import formdb, Course


# Create your views here.
def home(request):
    return render(request,'index.html')
def Reg(request):
    if request.method == 'POST':
        name=request.POST['first_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return ('register')
            else:
                user=User.objects.create_user(first_name=name,username=username,email=email,password=password)
                user.save()
                print("user created")
        else:
            messages.info(request,"password doesn't match")
            return('register')
        return redirect('login')
    return render(request,"Register.html")
def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/forms')
        else:
            messages.info(request,"something went wrong please tyr again")
            return redirect('login')

    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def index(request):
    if request.method == "POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        dob=request.POST.get('dob')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        address=request.POST.get('address')
        department=request.POST.get('department')
        course=request.POST.get('course')
        formsdb=formdb(name=name,dob=dob,phone=phone,age=age,email=email,address=address,department=department,course=course)

        form = Location(request.POST)
        if form.is_valid():
            print(form.cleaned_data["department"])
            print(form.cleaned_data["course"])
        else:
            print(form.errors)
        formsdb.save()

        messages.success(request,'successful')


    else:
        form = Location()

    return render(request, 'forms.html', {"form": form})
def load(request):
    department_id = request.GET.get("department")
    courses = Course.objects.filter(department_id=department_id)
    return render(request, "test.html", {"courses": courses})