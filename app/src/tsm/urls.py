from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin.sites import site
from django.urls import path

from graphene_django.views import GraphQLView

from tsm.core.schema import schema


urlpatterns = [
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
    path('', site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
