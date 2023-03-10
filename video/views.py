import json
import warnings
import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.views.generic.list import ListView
from .models import Video
from .forms import VideoForm
from .util import get_details

from django.contrib.auth.models import User

@method_decorator(login_required, name='dispatch')
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

@method_decorator(login_required, name='dispatch')
class VideoList(ListView):
    """
    Video Report filtered by project
    """
    model = Video
    template_name = 'videos/video_list.html'

    def get(self, request, *args, **kwargs):
        get_user = User.objects.all().filter(username=request.user.username)
        get_videos = Video.objects.all()

        return render(request, self.template_name, {'getVideos': get_videos})


@method_decorator(login_required, name='dispatch')
class VideoView(View):
    """
    Video Detail View
    """
    model = Video
    template_name = 'videos/view_video.html'

    def get(self, request, *args, **kwargs):
        id = self.kwargs['pk']
        get_video = Video.objects.get(pk=id)
        details = get_details(get_video.stream_id)
        return render(request, self.template_name, {'getVideo': get_video, 'getDetails': details})


@method_decorator(login_required, name='dispatch')
class VideoPlayer(View):
    """
    Video Detail View
    """
    model = Video
    template_name = 'player_example.html'

    def get(self, request, *args, **kwargs):
        get_videos = Video.objects.all()
        return render(request, self.template_name, {'getVideos': get_videos})

@method_decorator(login_required, name='dispatch')
class VideoCreate(CreateView):
    """
    Using Video Form for new Video per user
    """
    model = Video
    template_name = 'videos/video_form.html'

    def dispatch(self, request, *args, **kwargs):
        return super(VideoCreate, self).dispatch(request, *args, **kwargs)

    # add the request to the kwargs
    def get_form_kwargs(self):
        kwargs = super(VideoCreate, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_initial(self):

        initial = {
            'user': self.request.user,
        }

        return initial

    def form_invalid(self, form):

        messages.error(self.request, 'Invalid Form', fail_silently=False)

        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Success, Video Created!')
        latest = Video.objects.latest('id')
        redirect_url = '/video/video_update/' + str(latest.id)
        return HttpResponseRedirect(redirect_url)

    form_class = VideoForm

@method_decorator(login_required, name='dispatch')
class VideoUpdate(UpdateView):
    """
    Video Form Update an existing video
    """
    model = Video
    template_name = 'videos/video_form.html'

    def dispatch(self, request, *args, **kwargs):
        return super(VideoUpdate, self).dispatch(request, *args, **kwargs)

    # add the request to the kwargs
    def get_form_kwargs(self):
        kwargs = super(VideoUpdate, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_initial(self):

        initial = {
            'user': self.request.user,
        }

        return initial

    def form_invalid(self, form):

        messages.error(self.request, 'Invalid Form', fail_silently=False)

        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Success, Video Updated!')
        latest = Video.objects.latest('id')
        redirect_url = '/video/video_update/' + str(latest.id)
        return HttpResponseRedirect(redirect_url)

    form_class = VideoForm

@method_decorator(login_required, name='dispatch')
class VideoDelete(DeleteView):
    """
    Video Form Delete an existing Video
    """
    model = Video
    template_name = 'videos/video_confirm_delete.html'
    success_url = "/video/video_list"

    def dispatch(self, request, *args, **kwargs):
        return super(VideoDelete, self).dispatch(request, *args, **kwargs)

    def form_invalid(self, form):

        messages.error(self.request, 'Invalid Form', fail_silently=False)

        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):

        form.save()

        messages.success(self.request, 'Success, Video Deleted!')
        return self.render_to_response(self.get_context_data(form=form))

    form_class = VideoForm


def logout_view(request):
    """
    Logout a user in activity and track
    """
    # Redirect to track, so the user will
    # be logged out there as well
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect("/")

    return HttpResponseRedirect("/")


def check_view(request):
    return HttpResponse("Hostname "+request.get_host())
