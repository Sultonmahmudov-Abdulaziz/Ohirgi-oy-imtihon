from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Post, Comment, Likes
 

# class UsersLoginSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=50, min_length=4)
#     password = serializers.CharField(min_length=4)

#     def validate(self, data):
#         username = data.get('username')
#         password = data.get('password')

#         if username and password:
#             user = authenticate(username=username, password=password)
#             if not user:
#                 raise serializers.ValidationError("Username or password is incorrect")
#         else:
#             raise serializers.ValidationError("Username and password are required")

#         data['user'] = user
#         return data
    

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id','username', 'email', 'password']

    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields = ['id','user','publikatsiya']

    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'post_id', 'coment', 'created_at', 'updated_at'] 
        read_only_fields = ['user', 'post_id', 'created_at', 'updated_at']


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = ['id', 'user', 'post_id', 'created_at', 'updated_at']
        read_only_fields = ['user', 'post_id', 'created_at', 'updated_at']
