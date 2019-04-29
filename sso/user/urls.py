from django.conf.urls import url

from .views import UserIntrospectViewSet, UserRetrieveViewSet

urlpatterns = [
    url(
        r'^me/$',
        UserRetrieveViewSet.as_view({
            'get': 'retrieve',
            'patch': 'partial_update',
        }),
        name='me'
    ),
    url(
        r'^introspect/$',
        UserIntrospectViewSet.as_view({
            'get': 'retrieve'
        }),
        name='user-introspect'
    ),
]
