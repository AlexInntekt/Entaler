from .base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")

STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static_dirs"),
    )


print("BASE_DIR: ", BASE_DIR)
print("STATIC_ROOT: ", STATIC_ROOT)
print("MEDIA_ROOT: ", MEDIA_ROOT)
print("MEDIA_URL: ", MEDIA_URL)