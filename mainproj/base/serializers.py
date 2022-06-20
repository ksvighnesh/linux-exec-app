from rest_framework import serializers
from . models import command

class commandSerializer(serializers.ModelSerializer):
    class Meta:
        model=command
        fields=['id','cmd','repetition','sleep_dur']