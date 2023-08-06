from enum import Enum

from django.apps import apps
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from ..fields import CodeField
from medux.core.models import PackageDataModel


class Settings(PackageDataModel):
    """A simple scoped key-value store for application settings.

    This is not to be mixed up with Django settings.py. It should not be a replacement for that, there are plenty oft
    projects that deal with that sort of settings. It's meant as an application configuration method that could be
    overridden by a vendor, settings that could be set per workspace, preferences per user, etc.

    Each setting has a scope which is important to be mentioned. There are different settings scopes:

    global
      Settings that are defaults to MedUX. Each app can add settings to that scope.

    vendor
      These are settings that are provided by the vendor. Only vendor settings should be packaged in :ref:`Datapack`s.

    system
      These settings are specific to one "appliance" or "installation" of MedUX.

    machine
      applicable for one computer, or workplace.

    user
      Settings that only affect one user.

    These settings are searched for and applied in that order. So, if you retrieve a setting for
    Settings can be packaged as :ref:`Datapack`, and hence updated by the vendor (Here, only "vendor" scoped settings
    should be provided via datapacks!)

    The ``key`` must be a dotted path, starting with the name of an app, followed by a dot, like `medux.foo_setting`.
    """

    class Scope(Enum):
        GLOBAL = "global"
        VENDOR = "vendor"
        SYSTEM = "system"
        MACHINE = "machine"
        USER = "user"

    scope = CodeField(terminology_binding=Scope)
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        help_text=_(
            "The user this setting is scoped to. Just applicable if scope == 'user'."
        ),
    )

    class Meta:
        unique_together = ("scope", "key")

    def __str__(self):
        return f"{self.key} ({self.scope})"

    def clean(self):
        if self.scope == Settings.Scope.USER and self.user is None:
            raise ValidationError(
                {"title": _("'User' must be given when scope == 'USER'.")}
            )
        if not self.key.startswith(
            tuple([key + "." for key in apps.app_configs.keys()])
        ):
            raise ValidationError(
                _("'Key' must start with an app name (followed by a dot)")
            )
        for part in self.key.split("."):
            if not part.isidentifier():
                raise ValidationError(
                    _(
                        "Key must be dotted valid python identifiers, like 'medux.foo_setting.baz'."
                    )
                )

    def save(self, *args, **kwargs):
        self.full_clean()
        self.scope = self.scope.value
        super().save(*args, **kwargs)

    @staticmethod
    def get(key: str, default="", scope=None) -> str:
        """Retrieves the current valid value for ``key``, matching the scope.

        :param key: the dotted settings parameter to retrieve a value for. Must start with
                    a name of an app, followed by a dot, like 'medux.foo_setting'.
        :param scope: if given, only the setting with the given scope is returned.
                      If not, the highest ranked scope is used.
        :param default: if setting is not found, this default will be returned.
        """

        settings = Settings.objects.filter(key=key).order_by("scope")
        if scope:
            settings = settings.filter(scope=scope)
            # FIXME: make sure here that order_by orders correctly - NOT alphabetically!

        settings = settings.last()
        if settings is None:
            return str(default)
        return settings.value
