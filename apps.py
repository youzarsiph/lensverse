""" AppConf for pixhub """


from django.apps import AppConfig


# Create your AppConf here.
class PixHubConfig(AppConfig):
    """App configuration for pixhub"""

    name = "pixhub"
    default_auto_field = "django.db.models.BigAutoField"
