
from pathlib import Path

import os
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-7ppocbnx@w71dcuinn*t^_mzal(t@o01v3fee27g%rg18fc5d@')



DEBUG = False
ALLOWED_HOSTS = ['https://blogwizard.azurewebsites.net/']


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'accounts',
    'posts',
    'tinymce',
    'ckeditor',
    'ckeditor_uploader',
    'storages',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "blog_main.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ['templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "blog_main.wsgi.application"


hostname = os.environ['DBHOST']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DBNAME'],
        'HOST': hostname + ".postgres.database.azure.com",
        'USER': os.environ['DBUSER'],
        'PASSWORD': os.environ['DBPASS'] 
    }
}

CSRF_TRUSTED_ORIGINS=['https://blogwizard.azurewebsites.net/']



AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

AUTH_USER_MODEL='accounts.User'



LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True



STATIC_ROOT=BASE_DIR/'static'

STATICFILES_DIRS=['blog_main/static']

MEDIA_ROOT=BASE_DIR/'media'
CKEDITOR_UPLOAD_PATH = "uploads/"


DEFAULT_FILE_STORAGE = 'blog_main.custom_azure.AzureMediaStorage'
STATICFILES_STORAGE = 'blog_main.custom_azure.AzureStaticStorage'

STATIC_LOCATION = "static"
MEDIA_LOCATION = "media"

AZURE_ACCOUNT_NAME = "blogwizardstorage"
AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'
STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'



CKEDITOR_BASEPATH = 'https://blogwizardstorage.blob.core.windows.net/static/ckeditor/ckeditor/'
CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            {'name': 'yourcustomtools', 'items': [
                'Preview',
                'Maximize',

            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig', 
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage',
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
    }
}



DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'error',
    messages.SUCCESS:'success',
    messages.WARNING:'warning',
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='sahiltallnia222@gmail.com'
EMAIL_HOST_PASSWORD='rprkfwpivdberxox'
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL='Blog Website <sahiltallnia222@gmail.com>'













# -----------------------------------development env------------------------










# from pathlib import Path
# BASE_DIR = Path(__file__).resolve().parent.parent
# SECRET_KEY = "django-insecure-i@1w&6#hi_9u#b(&oe0-&nms5r=75qqa0*4r+4^jm1zt1-ai*3"
# DEBUG = False

# ALLOWED_HOSTS = ['*']

# INSTALLED_APPS = [
#     "django.contrib.admin",
#     "django.contrib.auth",
#     "django.contrib.contenttypes",
#     "django.contrib.sessions",
#     "django.contrib.messages",
#     "django.contrib.staticfiles",
#     'accounts',
#     'posts',
#     'tinymce',
#     'ckeditor',
#     'ckeditor_uploader',
#     'storages',
# ]

# MIDDLEWARE = [
#     "django.middleware.security.SecurityMiddleware",
#     "django.contrib.sessions.middleware.SessionMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     "django.middleware.csrf.CsrfViewMiddleware",
#     "django.contrib.auth.middleware.AuthenticationMiddleware",
#     "django.contrib.messages.middleware.MessageMiddleware",
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",
# ]

# ROOT_URLCONF = "blog_main.urls"

# TEMPLATES = [
#     {
#         "BACKEND": "django.template.backends.django.DjangoTemplates",
#         "DIRS": ['templates'],
#         "APP_DIRS": True,
#         "OPTIONS": {
#             "context_processors": [
#                 "django.template.context_processors.debug",
#                 "django.template.context_processors.request",
#                 "django.contrib.auth.context_processors.auth",
#                 "django.contrib.messages.context_processors.messages",
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = "blog_main.wsgi.application"


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": 'django_blog',
#         'USER':'postgres',
#         'PASSWORD':'a882jwuah7Sahil',
#         'HOST':'localhost',
#     }
# }

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
#     },
#     {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
#     {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
#     {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
# ]

# AUTH_USER_MODEL='accounts.User'

# LANGUAGE_CODE = "en-us"

# TIME_ZONE = "UTC"

# USE_I18N = True

# USE_TZ = True


# STATIC_URL = "/static/"

# STATIC_ROOT=BASE_DIR/'static'

# STATICFILES_DIRS=['blog_main/static']

# MEDIA_ROOT=BASE_DIR/'media'
# MEDIA_URL='/media/'
# CKEDITOR_UPLOAD_PATH = "uploads/"


# CKEDITOR_CONFIGS = {
#     'default': {
#         'skin': 'moono',
#         'toolbar_Basic': [
#             ['Source', '-', 'Bold', 'Italic']
#         ],
#         'toolbar_YourCustomToolbarConfig': [
#             {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
#             {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
#             {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
#             {'name': 'forms',
#              'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
#                        'HiddenField']},
#             '/',
#             {'name': 'basicstyles',
#              'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
#             {'name': 'paragraph',
#              'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
#                        'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
#                        'Language']},
#             {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
#             {'name': 'insert',
#              'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
#             '/',
#             {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
#             {'name': 'colors', 'items': ['TextColor', 'BGColor']},
#             {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
#             {'name': 'about', 'items': ['About']},
#             {'name': 'yourcustomtools', 'items': [
#                 'Preview',
#                 'Maximize',

#             ]},
#         ],
#         'toolbar': 'YourCustomToolbarConfig',
#         'tabSpaces': 4,
#         'extraPlugins': ','.join([
#             'uploadimage',
#             'div',
#             'autolink',
#             'autoembed',
#             'embedsemantic',
#             'autogrow',
#             'widget',
#             'lineutils',
#             'clipboard',
#             'dialog',
#             'dialogui',
#             'elementspath'
#         ]),
#     }
# }


# DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# from django.contrib.messages import constants as messages
# MESSAGE_TAGS = {
#     messages.ERROR: 'error',
#     messages.SUCCESS:'success',
#     messages.WARNING:'warning',
# }


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST='smtp.gmail.com'
# EMAIL_PORT=587
# EMAIL_HOST_USER='sahiltallnia222@gmail.com'
# EMAIL_HOST_PASSWORD='rprkfwpivdberxox'
# EMAIL_USE_TLS=True
# DEFAULT_FROM_EMAIL='Blog Website <sahiltallnia222@gmail.com>'