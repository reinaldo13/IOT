from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from alat_rfid.serializers import UserSerializer, GroupSerialize

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


# from django.shortcuts import render
# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# def detail(request, question_id):
#     return HttpResponse("kamu lihat pertanyaan ke %s." % question_id)

# def auth_group (request, id):
#     return HttpResponse ("nomer id = %s" %id)

# def results(request, question_id):
#     response = "Anda sedang melihat hasil dari pertanyaan %s."
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("Anda memilih dipertanyaan %s." % question_id)



# Create your views here.
