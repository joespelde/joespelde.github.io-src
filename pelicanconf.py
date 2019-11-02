#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime
from pathlib import Path

CURRENT_DIR_PATH = Path(__file__).resolve().parent

AUTHOR = 'Joe Spelde'
SITENAME = 'Joe Spelde'
SITEURL = 'joespelde.github.io'
THEME = '{}/voce'.format(CURRENT_DIR_PATH)
PATH = 'content'

TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 6
SUMMARY_MAX_LENGTH = 30

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Page Settings
PAGE_SAVE_AS = '{slug}.html'
TAGS_URL = 'tags.html'
ARCHIVES_URL = 'archive.html'

# Blogroll
LINKS = (('Home', '/index.html'),
         ('About', '/about.html'))

# Social widget
SOCIAL = (('Email', 'mailto:josephspelde@gmail.com'),
          ('GitHub', 'http://github.com/joespelde'),
	  	  ('Linkedin', 'https://www.linkedin.com/in/joseph-spelde-2a3a12133/'))

# Plugins
PLUGINS = ['assets']
PLUGIN_PATHS = ['{}/plugins'.format(THEME)]

# Publish
DELETE_OUTPUT_DIRECTORY = False

USER_LOGO_URL = 'https://ibb.co/gFF6tnw'

# Sitemap
SITEMAP_SAVE_AS = 'sitemap.xml'
DIRECT_TEMPLATES = ['sitemap', 'index']

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
