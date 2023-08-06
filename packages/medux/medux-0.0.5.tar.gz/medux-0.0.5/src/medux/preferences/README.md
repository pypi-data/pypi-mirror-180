# MedUX settings

`medux-settings` is a framework to save settings of the application in your database.

These can be scoped by e.g. a DEVICE or User, meaning that these settings are meant to be applied to only this device or user.

## Settings Registry
All settings need to be registered at application start, or st least before they can be created, read or imported from a file. You should probably do this e.g. in your AppConfig.ready(). This is a feature to prevent bugs like reading from/writing to nonexistent settings.

```python
from django.apps.config import AppConfig
from medux.preferences import Scope
from medux.preferences.registry import PreferencesRegistry


class MyPluginConfig(AppConfig):
    def ready(self):
        PreferencesRegistry.register(namespace="my_plugin", key="foregeound_color",
                                  allowed_scopes=[Scope.USER, Scope.TENANT],
                                  key_type=str)
```
It is necessary to define the `allowed_scopes`: for some settings it makes sense to e.g. allow users to define their own values, for some settings it may just be necessary to create device entries. You can set that here, at registration. `Scope.VENDOR` is implicitly always allowed. 

## Set values

Now you can set settings values using `CachedPreferences.set()`.

```python
from medux.preferences.models import ScopedPreference
from medux.preferences import Scope
import django.contrib.auth

# ...
User = django.contrib.auth.get_user_model()
admin = User.objects.get(pk=1)

CachedPreferences.set("prescriptions", "use_approval", value=True, scope=Scope.USER,
                   foreign_object=admin)
```
## Get values

And retrieve it with`CachedPreferences.get()`:

```python
from medux.preferences.models import ScopedPreference

use_approval = CachedPreferences.get("prescriptions", "use_approval")  # True
```

Settings that are not existing just raise a KeyError:

```python
CachedPreferences.get("my_namespace", "non_existing_setting", Scope.VENDOR)

#
```

## Usage in templates
You also can use them in templates. Here the currently (per request) applied settings are returned.

```django
{% if settings.prescriptions.use_approval %}
  Approval is enabled.
{% endif %}
```

You can create settings with the "VENDOR" scope, which are updateable defaults that are taken when no other settings with this key are available. When other scopes are available in the database for this key, they are taken using the following order: `VENDOR` < `CLIENT` < `GROUP` < `DEVICE` < `USER`.

The `USER` scope is the one with the highest priority.

## Providing default settings files

Each app can add a `settings.toml` file that introduces app-wide vendor settings. The file must contain a section with the app name:

```toml
[laboratory]
use_lab_results = true
```

You can load `settings.toml` files using a management command:

```bash
./manage.py loadsettings
```

Settings are automatically found in each app and loaded into the database under the VENDOR scope, so they can act as defaults.