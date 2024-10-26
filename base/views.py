from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from django.http import JsonResponse


from .models import Post
from .serializers import PostSerializer
from .models import AgoraCredentials
# Create your views here.

def register(request):
    return render(request, 'login.html')

def public_feed(request):
    posts = Post.objects.all().order_by('-created')

    context = {'posts':posts}
    return render(request, 'feed.html', context)

@api_view(['POST'])
def add_post(request):
    data = request.data 
    post = Post.objects.create(
        sender=data['sender'],
        body=data['body']
    )
    serializer  = PostSerializer(post, many=False)
    return Response(serializer.data)


def getAppID(request):
    credentials = AgoraCredentials.objects.first()  # Get the first record
    if not credentials:
        return JsonResponse({'error': 'Credentials not found'}, status=404)
    
    appId = credentials.app_id
    return JsonResponse({'appId':appId}, safe=False)