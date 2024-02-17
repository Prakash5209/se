from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse

from main.forms import BlogForm
from .models import Blog,Comment

usr = get_user_model()


@login_required
def home(request):
    blog = Blog.objects.all()
    comment = Comment.objects.all()

    form = BlogForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('main:home')
    
    if request.method == "POST":
        comment = request.POST.get('comment')
        post_id = request.POST.get('post')
        for i in blog:
            if i.id == int(post_id):
                Comment(comment = comment,blog = i,user = request.user).save()
                print('saved')
                return redirect('main:home')
    context = {'form':form,'blog':blog,'comment':comment}
    return render(request,'home.html',context)



def deletepost(request,pk):
    modl = Comment.objects.get(id = pk,user = request.user)
    modl.delete()
    return redirect(reverse('main:home'))
    # return render(request,'home.html')


# shree12

# monitor123

