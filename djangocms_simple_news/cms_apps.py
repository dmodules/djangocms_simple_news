from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

class SimpleNewsApphook(CMSApp):
    name = _("Simple News")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["djangocms_simple_news.urls"]

apphook_pool.register(SimpleNewsApphook)
