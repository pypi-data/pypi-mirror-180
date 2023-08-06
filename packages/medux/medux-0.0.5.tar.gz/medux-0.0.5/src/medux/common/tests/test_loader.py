# empty test so that pytest doesn't fail
# remove this test when you created your own
import pytest
from django.contrib.auth import get_user_model

from medux.preferences.definitions import Scope, KeyType
from medux.preferences.loaders import PreferencesLoader
from medux.preferences.registry import PreferencesRegistry


@pytest.mark.django_db
def test_load_key():
    PreferencesRegistry.register(
        "test_namespace", "test_key", [Scope.USER], key_type=KeyType.INTEGER
    )
    User = get_user_model()
    admin = User.objects.create(username="admin")
    admin.save()
    loader = PreferencesLoader(scope=Scope.USER, foreign_object=admin)
    loader.update_preferences({"test_namespace": {"test_key": 42}})


@pytest.mark.django_db
def test_load_key_without_registering():
    loader = PreferencesLoader(scope=Scope.VENDOR)
    with pytest.raises(KeyError):
        loader.update_preferences({"notexisting_namespace": {"new_key": 42}})
