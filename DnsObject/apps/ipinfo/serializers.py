# -*- coding: utf-8 -*-
from rest_framework import serializers
from ipinfo.models import IPinfo


class IPinfoSerializer(serializers.ModelSerializer):
    """
    Serializer Models.IP
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = IPinfo
        fields = (
            '__all__'
        )
        read_only_fields = ('create_user', 'update_user','reverse_ip',)