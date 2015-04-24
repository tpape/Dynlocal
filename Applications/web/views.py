from django.shortcuts import render, render_to_response
from django.template import RequestContext
from Applications.web.forms import UserForm, UserProfileForm

def index(request):
    return render(request, 'index.html')
def register(request):
    context=RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        registered = True
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save() #save te user's form data to the database
            user.set_password(user.password) # hash password
            user.save()

            profile = profile_form.save(commit=false)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render_to_response('contrib.html',{'user_form':user_form, 'registered':registered}, context)
