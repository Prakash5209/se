from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout

from .forms import AuthenticateForm,SignupForm,ProfileDetailiForm
from .models import ProfileDetail

def userLogin(request):
    form = AuthenticateForm(request.POST or None)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = authenticate(request,username=username,password=password)
        if user_obj:
            login(request,user_obj)
            return redirect('main:home')
    context = {'form':form}
    return render(request,'login.html',context)

def userSignup(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        ProfileDetail.objects.create(user = user)
        return redirect('account:userLogin')
    context = {'form':form}
    return render(request,'signup.html',context)


def userLogout(request):
    logout(request)
    return redirect('main:home')

def userProfile(request,pk):
    modl = get_object_or_404(ProfileDetail,id = pk,user = request.user)
    # modl = ProfileDetail.objects.get(id = pk,user = request.user)
    form = ProfileDetailiForm(request.POST or None, request.FILES or None, instance=modl)
    if form.is_valid():
        form.save()
        print('saved')
    context = {'form':form,'modl':modl}
    return render(request,'profile.html',context)


