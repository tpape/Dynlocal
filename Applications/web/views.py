from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from Applications.web.forms import UserForm, UserProfileForm, LoginForm, ContributerProfileForm
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
def register(request):
    context=RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        login_form = LoginForm()
        registered = False

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save() #save the user's form data to the database
            user.set_password(user.password) # hash password
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            user_to_login = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user_to_login:
                if user_to_login.is_active:
                    login(request,user_to_login)
                    render_to_response('/widgets/contrib/dashboard.html',{'registered':registered}, context)
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        login_form = LoginForm()
    return render_to_response('contrib.html',{'user_form':user_form, 'profile_form':profile_form, 'login_form':login_form,'registered':registered}, context)

def user_login(request):
    context=RequestContext(request)

    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return render_to_response('contrib.html',{'loged_in':loged_in}, context)
            else:
                return HttpResponse('Votre compte est désactivé.') #
        else:
            return HttpResponse('Vos identifiants sont invalides.')
    else:
        return render_to_response('contrib.html', context)
