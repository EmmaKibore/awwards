from django.shortcuts import render
from django.shortcuts import render,redirect

from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.contrib.auth.decorators import login_required
from .forms import NewProfForm, NewProjectForm, ReviewForm

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Profile,Project,Review,User
from .serializer import ProjectSerializer,ProfileSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly

@login_required(login_url='/accounts/login')
def home(request):
    try:
        date = dt.date.today()
        projects = Project.objects.all()
        # project = Project.objects.filter(id).first()
        # overall = (project.design+project.usability+project.
    except DoesNotExist:
        raise Http404()
    return render(request,"all_posts/home.html",{"date": date, "projects": projects})


@login_required(login_url='/accounts/login')
def prof(request):
    users =User.objects.all()

    for user in users:
        user=user
        profile = Profile.objects.all()
        projects = Project.objects.all()
        print(user)
    return render(request,"all_posts/prof.html",{ "user": user,"profile": profile,"projects": projects})

@login_required(login_url='/accounts/login')
def project(request,id):
    project = Project.objects.filter(id__icontains = id)
    return render(request,"all_posts/project",{"project": project})


@login_required(login_url='/accounts/login')
def search(request):
    if 'project' in request.GET and request.GET["project"]:
        title = request.GET.get("project")
        print(title)
        # owner = request.GET.get("project")
        searched_projects = Project.search_project(title)
        message = f"{title}"
        return render(request,"all_posts/search.html", {"message": message, "projects": searched_projects})
    else:
        message = "There is no such project"
        return render(request,"all_posts/search.html", {"message": message})

@login_required(login_url='/accounts/login')
def new_prof(request):
    current_user = request.user
    user = User.objects.filter().first()
    if request.method == 'POST':
        form = NewProfForm(request.POST,request.FILES)
        print(form.errors.as_text())
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            # profile=Profile.objects.update()
            profile.save()
        return redirect('prof')
    else:
        form = NewProfForm()
    return render(request,'registration/new_prof.html',{"form": form,"id":id})


@login_required(login_url='/accounts/login')
def new_project(request):
    current_user=request.user
    profile= Profile.objects.filter(user=current_user.id).first()
    if request.method == 'POST':
        form = NewProjectForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile=profile
            project.save()
        return redirect('prof')
    else:
        form = NewProjectForm()
    return render(request,'registration/new_project.html',{"form": form,"id":id})



# Create your views here.
