from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .models import Person, Teacher


def index(request: HttpRequest) -> HttpResponse:  # GET/POST
    # check
    context = {'teachers': Teacher.objects.all()}  # получаем всех преподавателей
    return render(request, 'index.html', context)


def add_teacher(request):
    if request.method == 'POST':
        # получаем данные из формы, но для этого есть такая штука как джанго forms
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        city = request.POST.get('city')
        email = request.POST.get('email')
        # photo = request.POST.get('photo')     #TODO google how to get photo from django form
        salary = request.POST.get('salary')
        # educational_institution = request.POST.get('educational_institution')
        work_experiences = request.POST.get('work_experiences')
        subject = request.POST.get('subject')
        new_teacher = Teacher(name=name, surname=surname, age=age, city=city, email=email, salary=salary,
                              educational_institution="Hogwarts", work_experiences=work_experiences, subject="Magic")
        new_teacher.save()
        print("Teacher added!")
        return redirect('/')
    return render(request, 'add_teacher.html')


def delete(request, id: int):
    if Teacher.objects.filter(id=id).exists():
        Teacher.objects.get(id=id).delete()
        print("Teacher deleted!")
    return redirect('/')


def update(request, id: int):
    if request.method == 'POST':
        # получаем данные из формы, но для этого есть такая штука как джанго forms
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        city = request.POST.get('city')
        email = request.POST.get('email')
        # photo = request.POST.get('photo')     #TODO google how to get photo from django form
        salary = request.POST.get('salary')
        # educational_institution = request.POST.get('educational_institution')
        work_experiences = request.POST.get('work_experiences')
        subject = request.POST.get('subject')
        Teacher.objects.filter(id=id).update(name=name, surname=surname, age=age, city=city, email=email, salary=salary,
                                             educational_institution="Hogwarts", work_experiences=work_experiences,
                                             subject="Magic")
        # получаем объект Учителя по id и перезаписываем его данные
        print("Teacher updated!")
        return redirect('/')
    return render(request, 'add_teacher.html')


from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate  # add this
from django.contrib.auth.forms import AuthenticationForm  # add this


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.info('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa')
            messages.success(request, "Registration successful.")
            return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)       # создали встроенную форму из джанго
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) # вызываем
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()     # всегда ренденрим форму
    return render(request=request, template_name="login.html", context={"login_form": form})
