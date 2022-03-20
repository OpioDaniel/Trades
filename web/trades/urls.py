from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(r'bizlandpractice', include('trades.apps.bizlandpractice.urls')),
    path(r'b/', include('trades.apps.bizland.urls')),
    path('admin/', admin.site.urls),
    path(r'ueconomics/', include('trades.apps.ueconomics.urls')),
    path(r'core/', include('trades.apps.core.urls')),
    path(r'', include('trades.apps.main.urls')),
    path(r'todo/', include('trades.apps.todo.urls')),
    path(r'dbillings/', include('trades.apps.dbillings.urls')),
    path(r'gamestore/', include('trades.apps.gamestore.urls')),
    path(r'ugandatowns/', include('trades.apps.ugandatowns.urls')),
    path(r'fabhouse', include('trades.apps.fabhouse.urls')),
    path(r'goblin/', include('trades.apps.goblin.urls')),
    path(r'sampleapp/', include('trades.apps.sampleapp.urls')),
    path(r'bless/', include('trades.apps.bless.urls')),
    path(r'student/', include('trades.apps.student.urls')),
    path(r'todos/', include('trades.apps.todos.urls')),
    path(r'text/', include('trades.apps.text.urls')),
    path(r'control/', include('trades.apps.control.urls')),
    path(r'r/', include('trades.apps.registration.urls')),
    path(r'a/', include('trades.apps.apewives.urls')),
    path(r'v/', include('trades.apps.vtab.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

