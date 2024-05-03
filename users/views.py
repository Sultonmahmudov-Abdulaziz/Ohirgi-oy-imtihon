from django.shortcuts import render
from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, PostSerializer, CommentSerializer, LikesSerializer
from django.contrib.auth  import authenticate
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment,Likes
from django.shortcuts import get_object_or_404


class RegisterApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=[permissions.AllowAny]
    def post(self, request,):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token

        return Response({
            'access_token': str(access_token),
            'refresh_token': str(refresh),
            'user': UserSerializer(user).data
        })


class LoginApiView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password']) 

        if user is None:
            data = {
                "status": False,
                "message": "Invalid username or password"
            }
            return Response(data)
        
        refresh=RefreshToken.for_user(user)

        data = {
            'refresh':str (refresh),
            'access':str (refresh.access_token),
            
        }
        
    

class AllUserView(APIView):
    permission_classes =[IsAuthenticated]
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    



class PostApiView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        user = request.user 

        post = Post.objects.filter(id=id, user=user).first()
        if not post:
            return Response({"error": "Post ghcf"})


        request.data['user'] = user.id  
        serializer = PostSerializer(instance=post, data=request.data)
        serializer.is_valid(raise_exception=True) 
        serializer.save()
        return Response(serializer.data)



    


class CreatePostApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user 

        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)

        return Response(serializer.data)



class AllPostsApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user


        posts = Post.objects.filter(user=user)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    

class PostDeleteApiView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        user = request.user 

        post = Post.objects.filter(id=id, user=user).first()
        if not post:
            return Response({"error": "Post not found"})
        
        post.delete()
        return Response({"message": "Post deleted successfully"})



class AddCommentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        user = request.user

        post = get_object_or_404(Post, id=id)

        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user, post=post)


        return Response(serializer.data)
    


class GetAllCommentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data) 
    


class AddLikesAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        user = request.user 

        post = Post.objects.filter(id=id).first()
        if not post:
            return Response({"error": "Post not found"})
        post.likes.add(user)
        post.save()

        return Response({"message": "Like added successfully"})
    


class UsersWhoLikedPostView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'})

        users = post.likes.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)