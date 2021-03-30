from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . import views

routers = routers.DefaultRouter()
routers.register('manager', views.ManagerViewSet)
routers.register('candidate', views.CandidateViewSet)


urlpatterns = [

    path('', include(routers.urls)),
    path('demo', views.DemoView.as_view()),
    path('regc/', views.regCandidate),
    path('regm/', views.regManager),
    path('detailc/', views.candidatedetails),
    path('detailc1/', views.candidatedetail),
    path('detailm/', views.managerlist),
    path('concern/', views.sendConcern),
    path('message/', views.message),
    path('control/', views.control),
    path('new/', views.get_token),
    path('api-token-auth/', views.CustomAuthToken.as_view()),
    path('sample/', views.SampleView.as_view()),
    path('delete/', views.msgdelete),
    path('userupt/', views.userupt),
    path('events/', views.events),
    path('generate/', views.generateCertificate),
    path('test/', views.test),
    # path('userm/', views.get_manager_from_token),
    # path('userc/', views.get_candidate_from_token),
    # path('reg/', views.UserCreate.as_view(), name="create_user"),
]
