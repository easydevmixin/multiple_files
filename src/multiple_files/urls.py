from django.conf.urls import url

from .views import add_attachment, add_attachment_done

urlpatterns = [
    url(r'^add_attachment/$', add_attachment, name="add_attachment"),
    url(r'^add_attachment_done/$', add_attachment_done, name="add_attachment_done"),
    url(r'^$', add_attachment, name="add_attachment"),
]
