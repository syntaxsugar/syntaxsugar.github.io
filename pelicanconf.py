#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

THEME = os.path.join(BASE_DIR, 'syntaxsugar.github.io', 'sstheme')

PLUGIN_PATHS = ['/home/fojtu/Projects/pelican-plugins']
#PLUGINS = ['summary',]

AUTHOR = u'Jaromir Fojtu'
SITENAME = u'syntaxsugar.github.io'
SITEURL = 'https://syntaxsugar.github.io'
MINI_BIO = u"A Daily PHP programmer, a nightly Python/Django developer"
BIO = u'<strong>Jaromir Fojtu</strong>. He is doing web development since 2000 and he is in love with Python & Django.'

TIMEZONE = 'Europe/Prague'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ('Github', 'https://github.com/syntaxsugar', '&#xe037;'),
    ('Google Plus', 'https://plus.google.com/118025323950244875124/about', '&#xe039;'),
    ('Twitter', 'https://twitter.com/jaromirfojtu', '&#xe086;'),
    ('Facebook', 'https://facebook.com/paiti', '&#xe027;'),
)

PATH = '/home/fojtu/PycharmProjects/syntaxsugar.github.io/content'

DEFAULT_PAGINATION = 0

TAG_CLOUD_MAX_ITEMS = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PYGMENTS_STYLE = 'friendly'

DEFAULT_DATE = 'fs'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'

LOCALE = ('en_US.utf8', 'cs_CZ.utf8')

DATE_FORMATS = {
    'en': ('en_US.utf8', '%d %b %Y'),
    'cs': ('cs_CZ.utf8', '%d.%m.%Y'),
}

STATIC_PATHS = [
    'images',
    'extra',
    'theme/img/avatar.jpg',
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/google91e15f50f8a42f37.txt': {'path': 'google91e15f50f8a42f37.html'}
}

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
SITEMAP_SAVE_AS = 'sitemap.xml'
