from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, ExhibitSerializer

from .models import Exhibit

def index(request):
    exhibit_list = Exhibit.objects.all()
    context = {'exhibit_list': exhibit_list}
    return render(request, 'api/index.html', context)

def detail(request, exhibit_id):    
    exhibit = get_object_or_404(Exhibit, pk=exhibit_id)
    return render(request, 'api/detail.html', {'exhibit': exhibit})

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ExhibitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    lookup_field = "nfc_id"
    queryset = Exhibit.objects.all()
    serializer_class = ExhibitSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]