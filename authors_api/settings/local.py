from .base import * #noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="X-RaTTGao4FEZoBTkD2whDHKRgwAMooVv0fpDUJP5o905-D66JE",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]


EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
DEFAULT_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "support@apiimperfect.site"
DOMAIN = env("DOMAIN")
SITE_NAME = "Authors Haven"
