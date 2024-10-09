from rest_framework import permissions, viewsets

from events.models import Event
from events.permissions import IsCreatorOrAdmin
from events.serializers import EventSerializer


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            return [permissions.IsAuthenticated(), IsCreatorOrAdmin()]
        return [permissions.IsAuthenticated()]
