from rest_framework import serializers
from yousta.models import User,Cloths,ClothVarients,Carts,Orders,Reviews,Offers


class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=["id","username","email","password","phone","address"]

    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class OfferSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    price=serializers.CharField(read_only=True)
    start_date=serializers.CharField(read_only=True)
    due_date=serializers.CharField(read_only=True)
    
    class Meta:
        model=Offers
        exclude=("clothvarient",)

class ClothVarientSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    offers=OfferSerializer(read_only=True,many=True)

    class Meta:
        model=ClothVarients
        exclude=('cloth',)

class ReviewSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    cloth=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Reviews
        fields="__all__"



class ClothsSerializer(serializers.ModelSerializer):
    # category=serializers.StringRelatedField(read_only=True)
    category=serializers.SlugRelatedField(slug_field="name",read_only=True)
    varients=ClothVarientSerializer(many=True,read_only=True)
    reviews=ReviewSerializer(read_only=True,many=True)
    avg_rating=serializers.CharField(read_only=True)
    class Meta:
        model=Cloths
        fields='__all__'

class CartSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    clothvarient=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
    class Meta:
        model=Carts
        fields=["id","clothvarient","user","status","date"]


class OrderSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    clothvarient=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    orderd_date=serializers.CharField(read_only=True)
    expected_date=serializers.CharField(read_only=True)
    class Meta:
        model=Orders
        fields=["id","user","clothvarient","status","orderd_date","expected_date","address"]

