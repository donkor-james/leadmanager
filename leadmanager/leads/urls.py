from leads.api import LeadViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')

urlpatterns = router.urls
