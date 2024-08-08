from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login , logout

def splash(request):
    return render(request, 'base/splash.html')




def login(request):
  if request.user.is_authenticated:
    return redirect("portfolio")
  else:
    if request.method=='POST':
      name=request.POST.get('username')
      pwd=request.POST.get('password')
      user=authenticate(request,username=name,password=pwd)
      if user is not None:
        login(request,user)
        messages.success(request,"Logged in Successfully")
        return redirect("portfolio")
      else:
        messages.error(request,"Invalid User Name or Password")
        return render(request,"base/login.html")
    return render(request,"base/login.html")
 
# def custom_login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('portfolio')  # Redirect to portfolio page
#         else:
#             # Return an 'invalid login' error message.
#             return render(request, 'login.html', {'error': 'Invalid login credentials'})

#     return render(request, 'login.html')



# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'base/register.html', {'form': form})
  
  
  


# def login(request):
#   if request.user.is_authenticated:
#     return redirect("/")
#   else:
#     if request.method=='POST':
#       name=request.POST.get('username')
#       pwd=request.POST.get('password')
#       user=authenticate(request,username=name,password=pwd)
#       if user is not None:
#         login(request,user)
#         messages.success(request,"Logged in Successfully")
#         return redirect("portfolio/")
#       else:
#         messages.error(request,"Invalid User Name or Password")
#         return redirect("/login")
#     return render(request,"base/login.html")




   






def logout(request):
    auth.logout(request)
    return redirect('/')

def portfolio(request):
    return render(request, 'base/portfolio.html')
