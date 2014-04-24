#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jaromir Fojtu'
SITENAME = u'SyntaxSugar'
SITEURL = 'http://localhost:8000'

TIMEZONE = 'Europe/Prague'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = None

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/syntaxsugar'),
          ('facebook', 'https://www.facebook.com/paiti'),
          ('github', 'https://github.com/syntaxsugar'),)

DEFAULT_PAGINATION = 5

TAG_CLOUD_MAX_ITEMS = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'pelican-bootstrap3'

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

PYGMENTS_STYLE = 'friendly'

DEFAULT_DATE = 'fs'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'

LOCALE = ('en_US.utf8', 'cs_CZ.utf8')

DATE_FORMATS = {
    'en': ('en_US.utf8', '%a, %d %b %Y'),
    'cs': ('cs_CZ.utf8', '%d.%m.%Y'),
}


STATIC_PATHS = [
    'images',
    'extra/robots.txt',
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/google91e15f50f8a42f37.html': {'path': 'google91e15f50f8a42f37.html'}
}

DISPLAY_ARTICLE_INFO_ON_INDEX = True