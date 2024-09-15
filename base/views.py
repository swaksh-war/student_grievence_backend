from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Event, Complaint, CustomUser
from .serializers import EventSerializer, ComplaintSerializer, CustomUserSeriealizer
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    if request.method == 'POST':
        serializer = CustomUserSeriealizer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                return Response({
                    'user': serializer.data,
                    'token': token.key
                }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try:
                user = CustomUser.objects.get(email=username)
            
            except ObjectDoesNotExist:
                pass
        
        if not user:
            user = authenticate(username = username, password = password)
        
        if user:
            token, _ = Token.objects.get_or_create(user = user)
            return Response({'token' : token.key, 'user_type': user.user_type}, status=200)
        return Response({'error': 'Invalid Credential'}, 401)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_complaint(request):
    if request.method == 'POST':
        print(request.data, request.headers)
        serializer = ComplaintSerializer(data=request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_complaints(request):
    category = request.query_params.get('category', None)
    if category:
        complaints = Complaint.objects.filter(created_by = request.user, category = category)
    else:
        complaints = Complaint.objects.filter(created_by = request.user)
    serializer = ComplaintSerializer(complaints, many=True)
    print(serializer.data)
    return Response(serializer.data, status=200)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_complaints_admin(request):
    complaints = Complaint.objects.all()
    serializer = ComplaintSerializer(complaints, many=True)
    return Response(serializer.data, status=200)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_event(request):
    if request.method == 'POST':
        # print(request.headers)
        print(request.data)
        serializer = EventSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        print(serializer.errors)
        return Response(serializer.errors, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_complaints_category_admin(request):
    category = request.query_params.get('category', None)
    if category:
        complaints = Complaint.objects.filter(category = category)
    else:
        complaints = Complaint.objects.all()
    serializer = ComplaintSerializer(complaints, many=True)
    print(serializer.data)
    return Response(serializer.data, status=200)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_event(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data, status=200)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request):
    if request.method == 'PUT':
        user = CustomUser.objects.get(id = request.user.id)
        serializer = CustomUserSeriealizer(user, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    user = request.user
    serializer = CustomUserSeriealizer(user)   
    return Response(serializer.data, status = 200)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def resolve_complaint(request, complaint_id):
    if request.method == 'PUT':
        complaint = Complaint.objects.get(id = complaint_id)
        complaint.resolution = request.data['resolution']
        complaint.status = 'Resolved'
        complaint.save()
        return Response({'status': 'Complaint Resolved'}, status=200)

