from django.conf.urls import url
from rango import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
   
    url(r'^rango/', include('rango.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
