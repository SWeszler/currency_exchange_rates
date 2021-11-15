from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.routers import SimpleRouter
from rates.views import RateViewSet, CurrencyViewSet
from scraper.views import ScraperView


router = SimpleRouter()
router.register(r'rates', RateViewSet)
router.register(r'currencies', CurrencyViewSet)

explicit_api_urlpatterns = [
    re_path(
        r'^rates/(?P<currency>[^/.]+)/(?P<date>[^/.]+)/$',
        RateViewSet.as_view({'get': 'retrieve'}),
        name='rate-detail-by-date'
    )
]

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('api/v1/', include(router.urls + explicit_api_urlpatterns), name='api'),
    path('scraper/run/', ScraperView.as_view(), name='scraper-run'),
]
