from rest_framework import serializers
from .models import Complaint, Event, CustomUser


class CustomUserSeriealizer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'email','phone_number', 'department', 'year', 'user_type', 'unique_id']
        extra_kwargs = {'password' : {'write_only' : True}}

    
    def create(self, validated_data):
        user = CustomUser(
            username = validated_data['username'],
            email = validated_data['email'],
            phone_number = validated_data['phone_number'],
            department = validated_data['department'],
            year = validated_data['year'],
            user_type = validated_data['user_type'],
            unique_id = validated_data['unique_id']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ['id','title', 'name', 'description', 'category', 'status', 'resolution']
    
    def create(self, validated_data):
        user = self.context['request'].user
        complaint = Complaint(created_by=user, title = validated_data['title'], name = validated_data['name'], description = validated_data['description'], category = validated_data['category'])
        complaint.save()
        return complaint

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'description', 'location', 'date', 'time']
    
    def create(self, validated_data):
        user = self.context['request'].user
        event = Event(created_by=user, name = validated_data['name'], description = validated_data['description'], date = validated_data['date'], time = validated_data['time'])
        event.save()
        return event
