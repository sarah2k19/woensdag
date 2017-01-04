from todoapp.models import Post
from items.serializers import PostSerializer
from rest_framework import generics
from django.contrib.auth.models import User
#from items.serializers import UserSerializer
from rest_framework import permissions
from items.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route


class PostViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create` and `retrieve` actions.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


#class UserViewSet(viewsets.ReadOnlyModelViewSet):
#    """
#    This viewset automatically provides `list` and `detail` actions.
#    """
#    queryset = User.objects.all()
#    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'items': reverse('item-list', request=request, format=format)
    })
