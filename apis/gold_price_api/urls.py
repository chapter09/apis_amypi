from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'db_books_api.views.home', name='home'),
    # url(r'^db_books_api/', include('db_books_api.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^query/$', 'gold_price_api.views.query', name='query'),
    #url(r'^id', 'db_books_api.views.id', name='id'),
)
