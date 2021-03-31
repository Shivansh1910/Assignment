import cv2 as cv
from PIL import Image, ImageFont, ImageDraw
import openpyxl
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from django.shortcuts import render
from rest_framework import viewsets
from . import serializers, models
from .models import Candidate, Manager, Concern, UserCertificate, Sample
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.http import HttpResponse
from django.db.models import ObjectDoesNotExist
from django.http import FileResponse
import os


# Create your views here.


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = models.Manager.objects.all()
    serializer_class = serializers.ManagerSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = models.Candidate.objects.all()
    serializer_class = serializers.CandidateSerializer


class ConcernViewSet(viewsets.ModelViewSet):
    queryset = models.Concern.objects.all()
    serializer_class = serializers.ConcernSerializer


class UserCertificateViewSet(viewsets.ModelViewSet):
    queryset = models.UserCertificate.objects.all()
    serializer_class = serializers.UserCertificateSerializer


class DemoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'status': 'success'})

# class UserCreate(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         reg_serializer = serializers.RegistrationSerializer(data=request.data)
#         if reg_serializer.is_valid():
#             new_user = reg_serializer.save()
#             if new_user:
#                 return Response({'status': 'created'})
#         return Response(reg_serializer.errors)


@api_view(['POST'])
def regCandidate(request):

    reqdata = request.data
    new = reqdata['username']
    user, created = User.objects.get_or_create(username=new)
    # return Response({'status': 'kya pata'})
    if created:
        try:
            user.set_password(reqdata['password'])
            user.save()

            candi, created = Candidate.objects.get_or_create(auth=user)
            candi.name = reqdata['name']
            candi.email = reqdata['email']
            candi.urname = user.username
            certi, created = UserCertificate.objects.get_or_create(
                email=reqdata['email'])
            certi.save()
            candi.save()
            user_serializer = serializers.UserSerializer(user)
            candi_serializer = serializers.CandidateSerializer(candi)
            certi_serializer = serializers.UserCertificateSerializer(certi)
            token = Token.objects.create(user=user)

            return Response({
                'user': user_serializer.data,
                'candidate': candi_serializer.data,
                'certificate': certi_serializer.data,
                'token': token.key,
            })

        except:
            user.delete()
            return Response({
                "created": False,
                "message": "Something went wrong"
            })
    else:
        return Response({
            "created": False,
            "candidate": user.id
        })


@api_view(['POST'])
def regManager(request):
    reqdata = request.data
    user, created = User.objects.get_or_create(username=reqdata['username'])
    if created:
        try:
            user.set_password(reqdata['password'])
            user.save()
            man, created = Manager.objects.get_or_create(auth=user)
            man.name = reqdata['name']
            man.email = reqdata['email']
            man.urname = user.username
            man.save()
            user_serializer = serializers.UserSerializer(user)
            manager_serializer = serializers.ManagerSerializer(man)
            token = Token.objects.create(user=user)
            return Response({
                'user': user_serializer.data,
                'manager': manager_serializer.data,
                'token': token.key,
            })

        except:
            user.delete()
            return Response({
                "created": False,
                "message": "Something went wrong"
            })
    else:
        return Response({
            "created": False,
            "manager": user.id
        })


@api_view(['GET'])
def candidatedetails(request):
    user = request.user
    candidate = Candidate.objects.get(auth=user)
    candidate_serializer = serializers.CandidateSerializer(candidate)
    temp = candidate.email
    email = UserCertificate.objects.get(email=temp)
    temp2 = Candidate.objects.get(email=temp)

    email_serializer = serializers.UserCertificateSerializer(email)
    return Response(email_serializer.data)


@api_view(['GET'])
def candidatedetail(request):
    user = request.user
    candidate = Candidate.objects.get(auth=user)
    candidate_serializer = serializers.CandidateSerializer(candidate)
    return Response(candidate_serializer.data)


# @api_view(['GET'])
# def managerdetail(request):
#     user = request.user
#     manager = Manager.objects.get(auth=user)
#     manager_serializer = serializers.ManagerSerializer(manager)
#     return Response({
#         'team': manager_serializer.data
#     })


@api_view(['POST'])
def get_token(request):
    # reqdata = request.data
    # user = User.objects.get(username=reqdata['username'])
    user = request.user
    token = Token.objects.get_or_create(user=user.id)
    return Response(token.key)


# @api_view(['GET', 'POST'])
# def get_manager_from_token(request):
#     user = request.user
#     reqData = request.data

#     try:
#         team = Manager.objects.get(auth=user)
#         team_serializer = serializers.ManagerSerializer(team)
#         return Response({
#             'team': team_serializer.data
#         })
#     except:
#         return Response({
#             'message': "not registered"
#         })

#     return Response(reqData)


# @api_view(['GET', 'POST'])
# def get_candidate_from_token(request):
#     user = request.user
#     reqData = request.data

#     try:
#         team = Candidate.objects.get(auth=user)
#         team_serializer = serializers.CandidateSerializer(team)
#         return Response({
#             'team': team_serializer.data
#         })
#     except:
#         return Response({
#             'message': "not registered"
#         })

#     return Response(reqData)


@api_view(['POST'])
def sendConcern(request):
    reqdata = request.data
    concern, created = Concern.objects.get_or_create(
        discription=reqdata['discription'])
    concern.email = reqdata['email']
    concern.manager = reqdata['manager']
    concern.subject = reqdata['subject']
    concern.name = reqdata['name']
    concern.save()
    concern_serializer = serializers.ConcernSerializer(concern)
    return Response(concern_serializer.data)


@api_view(['GET'])
def message(request):
    user = request.user
    manager = Manager.objects.get(auth=user)
    reqdata = manager.name
    # reqdata = "vrever"
    concern = Concern.objects.all().filter(manager=reqdata)
    # concern = Concern.objects.all().filter(manager=reqdata, complete=False)
    concern_serializer = serializers.ConcernSerializer(concern, many=True)
    return Response(concern_serializer.data)


@api_view(['POST'])
def msgdelete(request):
    # user = request.user
    # manager = Manager.objects.get(auth=user)
    reqdata = request.data
    # temp = manager.name
    # concern = Concern.objects.get(
    #     discription=reqdata['discription'], manager=temp)
    concern = Concern.objects.get(discription=reqdata['discription'])
    action = reqdata['action']
    if action == "delete":
        concern.delete()
        return Response({'status': 'deleted'})
    else:
        return Response({'status': 'error'})


@api_view(['GET'])
def managerlist(request):
    lst = Manager.objects.all().filter(is_admin=True)
    manager_serializer = serializers.ManagerSerializer(lst, many=True)
    return Response(manager_serializer.data)


@api_view(['POST'])
def control(request):
    reqdata = request.data
    new, created = UserCertificate.objects.get_or_create(
        email=reqdata['email'])
    new.event1 = reqdata['event1']
    new.event2 = reqdata['event2']
    new.event3 = reqdata['event3']
    new.save()
    user_serializer = serializers.UserCertificateSerializer(new)

    return Response(user_serializer.data)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        try:
            candi = Manager.objects.get(auth=user)
        except ObjectDoesNotExist:
            candi = Candidate.objects.get(auth=user)

            # if Manager.objects.get(auth=user).DoesNotExist:
            #     candi = Candidate.objects.get(auth=user)
            # else:
            #     # candi = Candidate.objects.get(auth=user)
            #     candi = Manager.objects.get(auth=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'new': candi.is_admin,
        })


@api_view(['POST'])
def userupt(request):
    reqdata = request.data
    temp = reqdata['email']
    email = Candidate.objects.get(email=temp)
    email.name = reqdata['name']
    email.save()
    user_serializer = serializers.CandidateSerializer(email)
    return Response(user_serializer.data)


class SampleView(APIView):
    parser_class = (FileUploadParser,)

    # def post(self, request, *args, **kwargs):

    #     file_serializer = serializers.SampleSerializer(data=request.data)

    #     if file_serializer.is_valid():
    #         file_serializer.save()
    #         return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        # reqdata = request.data

        # old = Sample.objects.all().filter(
        #     certificate_name=reqdata['certificate_name'])
        # if old.certificate_name == reqdata['certificate_name']:
        # if True:

        #     samp = Sample.objects.get_or_create(
        #         certificate_name=reqdata['certificate_name'])
        #     samp.x = reqdata['x']

        #     samp.y = reqdata['y']

        #     samp.begin = reqdata['begin']
        #     samp.discription = reqdata['discription']
        #     samp.discription1 = reqdata['discription1']
        #     samp.discription2 = reqdata['discription2']

        #     samp.is_discription = reqdata['is_discription']

        #     samp.file = reqdata['file']
        #     # return Response({'status': 'success'})
        #     samp.save()
        #     file_serializer = serializers.SampleSerializer(samp)
        #     return Response({
        #         'user': file_serializer.data,
        #     })
        # else:
        try:
            file_serializer = Sample.objects.get(
                certificate_name=request.data['certificate_name'])
            file_serializer.x = request.data['x']
            file_serializer.y = request.data['y']
            file_serializer.begin = request.data['begin']
            file_serializer.discription = request.data['discription']
            file_serializer.discription1 = request.data['discription1']
            file_serializer.discription2 = request.data['discription2']
            file_serializer.save()
            new = serializers.SampleSerializer(file_serializer)
            return Response(new.data)

        except ObjectDoesNotExist:
            file_serializer = serializers.SampleSerializer(data=request.data)
            if file_serializer.is_valid():
                file_serializer.save()
                return Response(file_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request, *args, **kwargs):
    #     reqdata = request.data

    #     samp, created = Sample.objects.get_or_create(
    #         certificate_name=reqdata['certificate_name'])

    #     samp.x = reqdata['x']

    #     samp.y = reqdata['y']

    #     samp.discription = reqdata['discription']

    #     samp.is_discription = reqdata['is_discription']

    #     # samp.file = reqdata['file']
    #     # return Response({'status': 'success'})
    #     samp.save()
    #     file_serializer = serializers.SampleSerializer(samp)
    #     return Response({
    #         'user': file_serializer.data,
    #     })


# @api_view(['POST'])
# def uptsample(request):
#     reqdata = request.data
#     samp = Sample.objects.get_or_create(
#         certificate_name=reqdata['certificate_name'])
#     samp.x = reqdata['x']
#     samp.y = reqdata['y']
#     samp.discription = reqdata['discription']
#     samp.is_discription = reqdata['is_discription']
#     samp.file = reqdata['file']
#     samp.save()
#     file_serializer = serializers.SampleSerializer(samp)
#     return Response({
#         'user': file_serializer.data,
#     })


@api_view(['GET'])
def events(request):
    samp = Sample.objects.all()
    samp_serializer = serializers.SampleSerializer(samp, many=True)
    return Response(samp_serializer.data)


# def generatorname(event, name, x, y):
#     event = str(event)
#     template_path = 'media/sample/' + event + '.jpg'
#     output_path = 'media/temp'
#     size = 3

#     font_size = int(size)
#     font_color = (0, 0, 0)

#     coordinate_y_adjustment = float(y)
#     coordinate_x_adjustment = float(x)

#     certi_name = str(name)

#     img = cv.imread(template_path)

#     font = cv.FONT_HERSHEY_PLAIN

#     text_size = cv.getTextSize(certi_name, font, font_size, 10)[0]

#     text_x = (img.shape[1] - text_size[0]) / 2 + coordinate_x_adjustment
#     text_y = (img.shape[0] + text_size[1]) / 2 - coordinate_y_adjustment
#     text_x = int(text_x)
#     text_y = int(text_y)
#     cv.putText(img, certi_name,
#                (text_x, text_y),
#                font,
#                font_size,
#                font_color, 3)

#     # certi_path = output_path + '/Certificate_of_' + certi_name + '.jpg'

#     # cv.imwrite(certi_path, img)
#     img = Image.fromarray(img)
#     # img.show()
#     img = img.convert('RGB')
#     certi_path = output_path + '/Certificate_of_' + name + '.pdf'
#     img.save(certi_path)

#     return


def generatordis(event, name, x, y, begin, text, text1, text2):
    template_path = 'media/sample/' + event + '.jpg'
    image = Image.open(template_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(r'media/sample/OpenSans-Bold.ttf', 50)
    spacing = 5
    disp = begin + "\n" + name + "\n" + text + "\n" + text1 + "\n" + text2
    x = int(x)
    y = int(y)
    # text = str(text)
    draw.text((x, y), disp, fill="black",
              font=font, spacing=spacing, align="center")
    img = image.convert('RGB')
    output_path = 'media/temp'
    certi_path = output_path + '/Certificate_of_' + name + '.pdf'
    img.save(certi_path)
    print(type(img))
    return


@api_view(['POST'])
def generateCertificate(request):
    user = request.user
    reqdata = request.data
    try:
        candi = Manager.objects.get(auth=user)
    except ObjectDoesNotExist:
        candi = Candidate.objects.get(auth=user)
    # candi = Candidate.objects.get(email=reqdata['email'])

    sample = Sample.objects.get(certificate_name=reqdata['event'])

    name = candi.name
    x = sample.x
    y = sample.y
    begin = sample.begin
    text = sample.discription
    text1 = sample.discription1
    text2 = sample.discription2
    is_discription = sample.is_discription
    event = sample.certificate_name

    # generatordis(event, name, x, y, text)

    if is_discription:
        generatordis(event, name, x, y, begin, text,  text1, text2)

    else:
        generatordis(event, name, x, y, "", "", "", "")

    base = "http://127.0.0.1:8000"
    path = "media/temp/Certificate_of"
    ext = "pdf"
    output_path = "%s/%s_%s.%s" % (base, path, name, ext)
    # response = FileResponse(open(output_path, 'rb'))
    # return response
    if reqdata['action'] == 'generate':
        return Response({output_path})

    elif reqdata['action'] == 'delete':
        output_path = "%s_%s.%s" % (path, name, ext)
        os.remove(output_path)
        return Response({'status': 'success'})


@api_view(['POST'])
def test(request):
    name = "Shrianshi Singh"

    x = 350
    y = 600
    begin = "This is to certify that"
    text = "had participated in the Annual Business Model Competition Eureka! 2019"
    text1 = "conducted by E-Cell IIT Bombay and had been selected as Semi-Finalists in the same."
    event = "certificate"
    print(type(text))
    generatordis(event, name, x, y, begin, text,  text1, "")
    # # generatorname(name, x, y)

    path = "media/temp/Certificate_of"
    ext = "pdf"
    output_path = "%s_%s.%s" % (path, name, ext)
    response = FileResponse(
        open(output_path, 'rb'))
    return response

    # os.remove("media/temp/Certificate of Shrianshi.pdf")

    # return Response({'status': 'success'})
