from .models import Event
from rest_framework import serializers 
from accounts.serializers import GetUserSerializer


class EventSer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    # comments_count = serializers.SerializerMethodField()
    # likes_count = serializers.SerializerMethodField()
    # delikes_count = serializers.SerializerMethodField()
    # likes = serializers.SerializerMethodField()
    class Meta():
        model = Event 
        fields = ['title', 'content', 'owner', 'p_date','u_date']

    def get_owner(self ,obj):
        return GetUserSerializer(obj.owner).data

    # def get_comments_count(self ,obj):
    #     return obj.comments.count()

    # def get_likes_count(self ,obj):
    #     return obj.likes.filter(like = True).count()

    # def get_delikes_count(self ,obj):
    #     return obj.likes.filter(like = False).count()

    
