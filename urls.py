from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hkssite.views.home', name='home'),
    # url(r'^hkssite/', include('hkssite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
      'document_root': settings.MEDIA_ROOT,
    }),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^', include('zinnia.urls.capabilities')),
    url(r'^search/', include('zinnia.urls.search')),
    url(r'^sitemap/', include('zinnia.urls.sitemap')),
    url(r'^trackback/', include('zinnia.urls.trackback')),
    url(r'^weblog/tags/', include('zinnia.urls.tags')),
    url(r'^weblog/feeds/', include('zinnia.urls.feeds')),
    url(r'^weblog/authors/', include('zinnia.urls.authors')),
    url(r'^weblog/categories/', include('zinnia.urls.categories')),
    url(r'^weblog/discussions/', include('zinnia.urls.discussions')),
    #url(r'^weblog/', include('zinnia.urls.quick_entry')),
    url(r'^weblog/', include('zinnia.urls.entries')),
    url(r'^comments/', include('django.contrib.comments.urls')),
)
