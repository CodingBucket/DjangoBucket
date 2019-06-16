from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html')

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('index')
#     else:
#         form = UserCreationForm()
#     context = {'form': form}
#     return render(request, 'registration/register.html', context)

def register(request):
    if request.method == 'POST':
        form = ExtendedCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(
                username=username,
                password=password
            )
            login(request, user)
            return redirect('index')
        else:
            form = ExtendedUserCreationForm()
            profile_form = UserProfileForm() 

        context = {
            'form': form,
            'profile_form': profile_form
        }
        return render(request, 'example/register.html', context)