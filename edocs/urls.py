from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('doclocker/', include('doclocker_app.urls') ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='homepage.html'), name='homepage'),







]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Doclocker Admin"
admin.site.site_title = "Doclcoker Admin Portal"
admin.site.index_tile = "Welcome to DOCLOCKER portal"
