import os

BACKEND_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = False

SECRET_KEY = "secret-key-213213"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BACKEND_DIR, "templates")],
        "APP_DIRS": True,
    }
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "test",
        "HOST": "192.168.1.101",
        "PORT": 5432,
        "USER": "main",
        "PASSWORD": "test",
    }
}

REACT_SSR = {
    "RENDER": {
        "TEMPLATE_NAME": "index.html",
        "URL": "http://192.168.1.102:3000/render",
        "TIMEOUT": 5.0,
        "HEADERS": {
            "Content-Type": "application/json",
        }
    },
    "STATE": {
        "URL": "http://192.168.1.102:3000/state",
        "TIMEOUT": 5.0,
        "HEADERS": {
            "Content-Type": "application/json",
        },
        "AUTH": {
            "NAME": "auth",
            "USER_SERIALIZER": None,
            "USER_KEY": "user",
            "TOKENS_KEY": "tokens",
        }
    },
    "SECRET_KEY": {
        "VALUE": "THIS_IS_A_SECRET_KEY",
        "HEADER_NAME": "secret-key",
    }
}

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "react_ssr",
    "webpack_loader_remote",
    "src.tests",
]
