from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin, \
    LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.datetime_safe import datetime
from django.views.generic import ListView, CreateView

from forumapp.forms import ThreadCreateModelForm, ThreadResponseModelForm
from .models import Thread, Forum, ForumSection, ThreadResponse


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(
                username=username,
                password=raw_password
            )
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(
        request,
        'forumapp/signup.html',
        {'form': form}
    )


def index(request):
    return render(
        request,
        'forumapp/index.html'
    )


def forums(request):
    sections = ForumSection.objects.all()
    return render(
        request,
        'forumapp/forums.html',
        context={
            'sections': sections,
        }
    )


def forum(request, pk):
    thread_list = Thread.objects.filter(forum=pk)
    return render(
        request,
        'forumapp/thread_list.html',
        context={
            'thread_list': thread_list
        }
    )


def thread_view(request, fpk, tpk):
    thread = Thread.objects.get(id=tpk)
    response_list = ThreadResponse.objects.filter(
        thread=tpk,
        thread__forum=fpk
    )
    return render(
        request,
        'forumapp/thread.html',
        context={
            'thread': thread,
            'response_list': response_list
        }
    )


def respond(request, fpk, tpk):
    if request.method == "POST":
        form = ThreadResponseModelForm(
            request.POST,
        )
        if form.is_valid():
            obj_response = form.save()

            obj_response.responder = request.user
            obj_response.created_date = datetime.today()
            obj_response.thread = Thread.objects.get(id=tpk)

            obj_response.save()

            return HttpResponseRedirect(
                reverse(
                    'thread-view',
                    kwargs={
                        'fpk': fpk,
                        'tpk': tpk
                    }
                )
            )
    else:
        form = ThreadResponseModelForm()
    return render(
        request,
        'forumapp/threadresponse_form.html',
        context={
            'form': form
        }
    )


@permission_required('can_create_thread')
def new_thread(request, pk):
    if request.method == "POST":
        form_thread = ThreadCreateModelForm(
            request.POST,
            prefix='form_thread'
        )
        if form_thread.is_valid():
            thread_obj = form_thread.save()
            form_response = ThreadResponseModelForm(
                request.POST,
                prefix='form_response',
            )

            if form_response.is_valid():
                obj_response = form_response.save()

                obj_response.thread = thread_obj
                obj_response.responder = request.user
                obj_response.created_date = datetime.today()

                obj_response.save()

                return HttpResponseRedirect(
                    reverse(
                        'forum',
                        kwargs={
                            'pk': pk
                        }
                    )
                )
            else:  # response not valid
                thread_obj.delete()  # TODO does it work?
    else:
        form_thread = ThreadCreateModelForm(prefix='form_thread')
        form_response = ThreadResponseModelForm(prefix='form_response')
        form_thread.initial['forum'] = pk
        return render(
            request,
            'forumapp/thread_form.html',
            context={
                'form_thread': form_thread,
                'form_response': form_response
            }
        )
