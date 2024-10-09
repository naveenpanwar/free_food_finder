from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from events.views import EventsViewSet
from free_food_finder.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("events", EventsViewSet)


app_name = "api"
urlpatterns = router.urls
