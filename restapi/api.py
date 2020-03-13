from rest_framework import routers
from rental import api_views

router=routers.DefaultRouter()
router.register(r'friend', api_views.FriendViewSet)
router.register(r'belonging', api_views.BelongingViewSet)
router.register(r'borrowed', api_views.BorrowedViewSet)