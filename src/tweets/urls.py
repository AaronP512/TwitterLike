from django.conf.urls import url

from .views import TweetListView, TweetDetailView

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', TweetListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),
]
