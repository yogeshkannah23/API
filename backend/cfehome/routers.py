from rest_framework.routers import DefaultRouter

from api.viewsets import ProductViewSets 

router = DefaultRouter()
router.register('product-abc',ProductViewSets,
                basename='asd')
print(router.urls)
urlpatterns = router.urls