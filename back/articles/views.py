from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from .serializers import ArticleSerializer, UserCreationSerializer
from .models import Article
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import HttpResponseForbidden
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
# from rest_framework.authentication import JSONWebTokenAuthentication

# Create your views here.

User = get_user_model()

# Create your views here.

@api_view(['POST'])
def article_create(request):
    serializer = ArticleSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=400)
    
@api_view(['DELETE'])
def article_delete(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.delete()
    return Response(status=204)
    



@api_view(['GET'])
def article_list(request, user_id, page_idx):
    user = get_object_or_404(User, pk=user_id)
    article = user.article_set.all()
    page = Paginator(article, 12)
    serializer = ArticleSerializer(page.page(page_idx).object_list, many=True)
    return Response({'total':page.num_pages , 'data':serializer.data})


@api_view(['POST'])
@permission_classes((AllowAny, ))
def user_signup(request):
    serializer = UserCreationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        # print(serializer.data)
        return Response({'message' : '회원가입이 성공적으로 완료되었습니다.'})



@api_view(['DELETE', 'PUT'])
def user_signout_and_update(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'DELETE':
        user.delete()
        return Response(status=204)
    elif request.method == 'PUT':
        origin_password = request.data.get('origin_password')
        if user.check_password(origin_password):
            user.set_password(request.data.get('password'))
            user.save()
            return Response({'message' : '비밀번호가 성공적으로 변경되었습니다.'})
        else:
            return Response({'message' : '현재 비밀번호가 맞지 않습니다.'})
        return Response(status=400)
