from rest_framework import serializers

from events.models import Event


class EventSerializer(serializers.ModelSerializer[Event]):
    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "description",
            "location",
            "latitude",
            "longitude",
            "date",
            "start_time",
            "end_time",
            "image",
        ]
