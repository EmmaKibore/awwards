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


# Create your views here.
