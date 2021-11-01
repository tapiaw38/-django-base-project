""" Main URLs Module. """

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

#import ipdb
#ipdb.set_trace()

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    #path('api/', include(('app.core.urls', 'app'), namespace='app')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
