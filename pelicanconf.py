AUTHOR = 'Omar El Mountassir'
SITENAME = 'LEGUIDE-UZZQZ'
SITEURL = ''

PATH = 'C:\\Users\\omar\\OneDrive\\Documents\\GitHub\\LEGUIDE-UZZQZ'
OUTPUT_PATH= 'output/'
STATIC_PATHS = ['images', 'static']
TIMEZONE = 'Africa/Casablanca'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Set the template engine to Jinja2
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Set the markup language to Markdown
MARKUP = ('md', 'markdown')

