from .models import Event
from rest_framework import serializers 
from accounts.serializers import GetUserSerializer
from .models import Like
from accounts.serializers import GetUserSerializer
from venue.serializers import EventSessionSerializer, VenueSerializer
from venue.models import Venue, EventSession

class LikeSer(serializers.ModelSerializer):
    class Meta():
        model = Like 
        fields = '__all__'
        read_only_fields = ['owner',]
    
    def validate(self ,data):
        owner_id = self.context['request'].user.id
        event = data['event']

        like = Like.objects.filter(owner = owner_id ,event = event.id)
        if like.exists():
            raise serializers.ValidationError("this like with this user and event already exists")
        return data


# like Update serializer 
class LikeUpdateSer(serializers.ModelSerializer):
    class Meta():
        model = Like 
        fields = '__all__'
        read_only_fields = ['owner','event']

    
class EventSer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    # session_detail=serializers.SerializerMethodField()
    # comments_count = serializers.SerializerMethodField()
    venues = VenueSerializer(many=True, read_only=True)
    sessions = EventSessionSerializer(many=True, read_only=True)

    likes_count = serializers.SerializerMethodField()
    # delikes_count = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    class Meta():
        model = Event 
        fields = ['id','cover_img','title', 'content', 'owner', 'p_date','u_date','event_date',
                  'venues','sessions',
                  'likes_count', 'likes']

    def get_owner(self ,obj):
        return GetUserSerializer(obj.owner).data

    def get_session_detail(self, obj):
        return EventSessionSerializer(obj.session, many= True).data
    # def get_comments_count(self ,obj):
    #     return obj.comments.count()

    def get_likes_count(self ,obj):
        return obj.likes.filter(like = True).count()

    # def get_delikes_count(self ,obj):
    #     return obj.likes.filter(like = False).count()
    
    def get_likes(self,obj):
        return LikeSer(obj.likes ,many = True).data
    
    # def create_venue(self, data):
    #     venue = Venue.objects.create(
    #         name= data['venue_name'],
    #         address= data['venue_address'],
    #         city= data['venue_city'],
    #         capacity=data['venue_capacity']
    #     )
    #     venue.save()
    #     return venue

