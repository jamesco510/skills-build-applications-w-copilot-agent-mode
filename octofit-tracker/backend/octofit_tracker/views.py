from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from urllib.parse import urljoin
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

@api_view(['GET'])
def api_root(request, format=None):
    base_url = request.build_absolute_uri('/')
    api_suffix = settings.API_ENDPOINT_SUFFIX or '/api/'  # Fallback to default if not set
    return Response({
        'users': urljoin(base_url, api_suffix + 'users/'),
        'teams': urljoin(base_url, api_suffix + 'teams/'),
        'activities': urljoin(base_url, api_suffix + 'activities/'),
        'leaderboard': urljoin(base_url, api_suffix + 'leaderboard/'),
        'workouts': urljoin(base_url, api_suffix + 'workouts/'),
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