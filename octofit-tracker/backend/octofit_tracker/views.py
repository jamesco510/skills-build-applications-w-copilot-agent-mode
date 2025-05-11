from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

@api_view(['GET'])
def api_root(request, format=None):
    base_url = 'https://stunning-doodle-x5rwx7746r9x2p79x-8000.app.github.dev'
    return Response({
        'users': base_url + settings.API_ENDPOINT_SUFFIX + 'users/',
        'teams': base_url + settings.API_ENDPOINT_SUFFIX + 'teams/',
        'activities': base_url + settings.API_ENDPOINT_SUFFIX + 'activities/',
        'leaderboard': base_url + settings.API_ENDPOINT_SUFFIX + 'leaderboard/',
        'workouts': base_url + settings.API_ENDPOINT_SUFFIX + 'workouts/',
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer