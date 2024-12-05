from django.http import JsonResponse
from .models import Post
from .serializers import PostSerializer

def posts_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse({'posts': serializer.data}, safe=False)