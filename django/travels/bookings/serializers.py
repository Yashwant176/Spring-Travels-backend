from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Bus , Seat, Booking


class UserRegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['username','email','password']

    def create(self,validate_date):
        user=User.objects.create_user(
            username=validate_date['username'],
            email=validate_date['email'],
            password=validate_date['password']
        )

        return user

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seat
        fields=['id','seat_number','is_booked']
        
class BusSerializer(serializers.ModelSerializer):
    seats=SeatSerializer(many=True, read_only=True)
    class Meta:
        model=Bus
        fields='__all__'


class BookingSerializer(serializers.ModelSerializer):
    bus=serializers.StringRelatedField()
    seat=SeatSerializer()
    user=serializers.StringRelatedField()

    class Meta:
        model=Booking
        fields='__all__'
        read_only_fields=['user','booking_time','bus','seat']