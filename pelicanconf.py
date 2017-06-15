#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mark Gondree'
SITENAME = u'Mark Gondree'
HIDE_SITENAME = True

SITEURL = 'http://localhost:8000'
SITELOGO = 'images/icon.png'
SITELOGO_SIZE = '30'
FAVICON = 'images/favicon.ico'

TIMEZONE = 'US/Pacific'
DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = 5
USE_PAGER = False

# About Me
ABOUT_ME = [
'<br>'.join([
    "<strong>Mark Gondree</strong>", 
    "Assistant Professor", 
    "<a href='http://www.cs.sonoma.edu/'>CS</a>, <a href='http://www.sonoma.edu/'>Sonoma State</a>",
    "",
    "<tt>gondree at gmail dot com</tt>"
    ]), 

' | '.join([
    "| @<a href='http://twitter.com/mgondree'>Twitter</a>",
    "@<a href='http://www.linkedin.com/in/markgondree'>LinkedIn</a>",
    "<br>",
    "@<a href='http://scholar.google.com/citations?user=Dyee0SUAAAAJ'>GoogleScholar</a>",
    "@<a href='http://www.researchgate.net/profile/Mark_Gondree/'>ResearchGate</a>",
    "<br>",
    "@<a href='https://github.com/gondree'>GitHub</a>",
    "@<a href='https://www.ohloh.net/accounts/gondree'>Ohloh</a>",
    "@<a href='http://www.flickr.com/photos/mgondree'>Flickr</a>",
    "<br>",
    "@<a href='http://boardgamegeek.com/user/mgondree'>BGG</a>",
    "@<a href='http://www.tabletopsecurity.com/'>TableTopSecurity</a> |",
    ]),

'<br>'.join([
    "PGP KeyID <a href='https://pgp.mit.edu/pks/lookup?op=get&search=0x56968F5D51091591'>0x56968f5d51091591</a>",
    "<tt>217E 9CD9 A4A3 B9DA 871D",
    "A204 660A 01EB 0A5B 89A1</tt>"
    ])
]



# Home / index.html
NEWS_ITEMS = 5

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ['render_math','pelicanfly']
#GOOGLE_ANALYTICS = "UA-37266550-1"


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PATH = 'content'
BOOTSTRAP_THEME = ""

STATIC_PATHS = ['images', 'pdfs',
    'extras/css/mg.css', 'extras/CNAME',
    'extras/google14081f6503dca9ab'  # req'd for Google+ website verification
]

EXTRA_PATH_METADATA = {
    'extras/css/mg.css': {'path': 'static/mg.css'},
    'extras/CNAME' : {'path': 'CNAME'},
    'extras/google14081f6503dca9ab' : {'path' : 'google14081f6503dca9ab.html'},
}

# Category options
USE_FOLDER_AS_CATEGORY = True
CATEGORY_SAVE_AS = '{slug}.html'
DEFAULT_CATEGORY = 'Blog'

# Article saving options
ARTICLE_URL = 'article/{slug}.html'
ARTICLE_SAVE_AS = 'article/{slug}.html'
INDEX_SAVE_AS = 'all.html'
DISPLAY_ARTICLE_INFO_ON_INDEX = True
SUMMARY_MAX_LENGTH = 100

# Article meta info shown
SHOW_ARTICLE_AUTHOR = True
ARTICLE_AUTHORS_PAGE = 'about.html'
SHOW_DATE_MODIFIED = False
SHOW_SERIES = False
SHOW_ARTICLE_CATEGORY = False
PDF_PROCESSOR = False

# Menu items
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_ARCHIVE_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_SOCIAL_ON_MENU = False
MENUITEMS = (('Bio', '/about'),
             ('Teaching', '/teaching'),
             ('Research', '/research'),
             ('Advising', '/advising'),
             ('Calendar', '/calendar'),
             ('C.V.', '/pdfs/gondree_cv.pdf'),
            )

# Sidebar options
AVATAR = "/images/nps.jpg"
HIDE_SIDEBAR = True
LINKS = ()

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/TableTopSec'),
          ('youtube', 'https://www.youtube.com/user/TableTopSecurity'),
          ('flickr', 'https://www.flickr.com/tabletopsecurity'),
          ('boardgamegeek', 'https://boardgamegeek.com/boardgamepublisher/23997/tabletop-security'),
          ('google-plus', 'https://plus.google.com/114066012466458862886'),
          ('github', 'http://github.com/tabletopsecurity')
         )


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme related settings
THEME = 'themes/pelican-bootstrap3'
THEME_STATIC_PATHS=['static']
CSS_FILE='mg.css'
CUSTOM_CSS = 'static/mg.css'

# Caching
LOAD_CONTENT_CACHE = False
