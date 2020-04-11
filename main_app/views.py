from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

import uuid
import boto3
from .models import Jersey, Player, Sponsor, Photo, Photo_sponsor, Photo_player

from .forms import ChampionshipForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'jerseycollector-gt-2'
new_S3_url = 'https://jerseycollector-gt.s3.amazonaws.com/'

# Create your views here.
def signup(request):
  error_message = ''

  if request.method == 'POST':
    #handle the signup of a new user
    form = UserCreationForm(request.POST)
    
    if form.is_valid():
      user = form.save()
      
      login(request, user)
      
      return redirect('index')
    else:
      error_message = 'Invalid Sign Up - Try Again'

  form = UserCreationForm()
  context = {'form': form, 'error': error_message}
  return render(request, 'registration/signup.html', context)



def home(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

@login_required
def jerseys_detail(request, jersey_id):
  jersey = Jersey.objects.get(id=jersey_id)
  player_jersey_doesnt_have = Player.objects.exclude(id__in = jersey.players.all().values_list('id'))
  sponsor_jersey_doesnt_have = Sponsor.objects.exclude(id__in = jersey.sponsors.all().values_list('id'))
  championship_form = ChampionshipForm()

  return render(request, 'jerseys/detail.html', {
    'jersey': jersey,
    'players': player_jersey_doesnt_have,
    'sponsors': sponsor_jersey_doesnt_have,
    'championship_form': championship_form
  })

@login_required
def add_championship(request, jersey_id):
  form = ChampionshipForm(request.POST)

  if form.is_valid():
    new_championship = form.save(commit=False)
    new_championship.jersey_id = jersey_id
    new_championship.save()
  return redirect('detail', jersey_id=jersey_id) 

@login_required
def assoc_player(request, jersey_id, player_id):
  Jersey.objects.get(id=jersey_id).players.add(player_id)
  return redirect('detail', jersey_id=jersey_id)

@login_required
def disassoc_player(request, jersey_id, player_id):
  Jersey.objects.get(id=jersey_id).players.remove(player_id)
  return redirect('detail', jersey_id=jersey_id)

@login_required
def assoc_sponsor(request, jersey_id, sponsor_id):
  Jersey.objects.get(id=jersey_id).sponsors.add(sponsor_id)
  return redirect('detail', jersey_id=jersey_id)

@login_required
def disassoc_sponsor(request, jersey_id, sponsor_id):
  Jersey.objects.get(id=jersey_id).sponsors.remove(sponsor_id)
  return redirect('detail', jersey_id=jersey_id)

@login_required
def jerseys_index(request):
  context = {'jerseys': Jersey.objects.filter(user=request.user)}
  return render(request, 'jerseys/index.html', context)

@login_required
def add_photo(request, jersey_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:

    # s3 = boto3.session.Session(profile_name='project1').client('s3')
    s3 = boto3.client('s3')

    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]

    try:
      s3.upload_fileobj(photo_file, BUCKET, key)

      url = f"{S3_BASE_URL}{BUCKET}/{key}"

      photo = Photo(url=url, jersey_id=jersey_id)
      photo.save()
    except Exception as e:
      print(e)
      print('An error occurred uploading file to S3')
  return redirect('detail', jersey_id=jersey_id)

@login_required
def add_player_photo(request, player_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:

    # s3 = boto3.session.Session(profile_name='project1').client('s3')
    s3 = boto3.client('s3')

    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]

    try:
      s3.upload_fileobj(photo_file, BUCKET, key)

      url = f"{S3_BASE_URL}{BUCKET}/{key}"

      photo = Photo_player(url=url, player_id=player_id)
      photo.save()
    except Exception as e:
      print(e)
      print('An error occurred uploading file to S3')
  return redirect('players_index')

@login_required
def add_sponsor_photo(request, sponsor_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:

    # s3 = boto3.session.Session(profile_name='project1').client('s3')
    s3 = boto3.client('s3')

    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]

    try:
      s3.upload_fileobj(photo_file, BUCKET, key)

      url = f"{S3_BASE_URL}{BUCKET}/{key}"

      photo = Photo_sponsor(url=url, sponsor_id=sponsor_id)
      photo.save()
    except Exception as e:
      print(e)
      print('An error occurred uploading file to S3')
  return redirect('sponsors_detail', sponsor_id=sponsor_id)

class JerseyCreate(LoginRequiredMixin, CreateView):
  model = Jersey
  fields = ['team_name', 'jersey_type', 'country', 'year_added', 'jersey_colors', 'jersey_description']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class JerseyUpdate(LoginRequiredMixin, UpdateView):
  model = Jersey
  fields = '__all__'

class JerseyDelete(LoginRequiredMixin, DeleteView):
  model = Jersey
  success_url = '/jerseys/'

class PlayerList(LoginRequiredMixin, ListView):
    model = Player

class PlayerDetail(LoginRequiredMixin, DetailView):
    model = Player

class PlayerCreate(LoginRequiredMixin, CreateView):
    model = Player
    fields = '__all__'
    success_url = '/players/'

class PlayerUpdate(LoginRequiredMixin, UpdateView):
    model = Player
    fields = '__all__'
    success_url = '/players/'

class PlayerDelete(LoginRequiredMixin, DeleteView):
    model = Player
    success_url = '/players/'

class SponsorList(LoginRequiredMixin, ListView):
    model = Sponsor

class SponsorDetail(LoginRequiredMixin, DetailView):
    model = Sponsor

class SponsorCreate(LoginRequiredMixin, CreateView):
    model = Sponsor
    fields = '__all__'
    success_url = '/sponsors/'

class SponsorUpdate(LoginRequiredMixin, UpdateView):
    model = Sponsor
    fields = '__all__'
    success_url = '/sponsors/'

class SponsorDelete(LoginRequiredMixin, DeleteView):
    model = Sponsor
    success_url = '/sponsors/'