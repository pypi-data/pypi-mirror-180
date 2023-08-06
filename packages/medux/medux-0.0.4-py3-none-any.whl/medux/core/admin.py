from django.apps import apps
from django.conf import settings
from django.contrib import admin


# taken from https://adriennedomingus.medium.com/soft-deletion-in-django-e4882581c340
from django.contrib.auth.models import Group

from .forms import DosageForm
from .models import (
    Name,
    Address,
    Country,
    ContactPoint,
    AdministrativeGender,
    HealthServiceProvider,
    Physician,
    Hospital,
    Person,
    Patient,
    Encounter,
    Problem,
    Narrative,
    NarrativeType,
    Department,
    Specialty,
    Language,
    Dosage,
)


class MeduxAdmin(admin.ModelAdmin):
    """A ModelAdmin for MeduxModels with Softdeletion awareness"""

    def get_queryset(self, request):
        # use the all_objects manager
        qs = self.model.all_objects

        # The below is copied from the base implementation in BaseModelAdmin to
        # prevent other changes in behavior
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

    def delete_model(self, request, obj):
        obj.hard_delete()


class AdministrativeGenderAdmin(admin.ModelAdmin):
    ordering = ("sort_weight",)


admin.site.register(AdministrativeGender, AdministrativeGenderAdmin)


class DosageAdmin(admin.ModelAdmin):
    form = DosageForm
    fields = [
        "method",
        "dose_type",
        "dose_rate_numerator_value",
        "dose_rate_numerator_unit",
    ]


admin.site.register(Dosage, DosageAdmin)

for model in [
    Country,
    ContactPoint,
    Address,
    # Period,
    HealthServiceProvider,
    Physician,
    Specialty,
    Hospital,
    Person,
    Patient,
    Encounter,
    Problem,
    Narrative,
    NarrativeType,
    Name,
    Department,
    Language,
]:
    admin.site.register(model)


if settings.DEBUG:
    # all other models
    models = apps.get_models()

    for model in models:
        try:
            if not model._meta.abstract:
                admin.site.register(model)
        except admin.sites.AlreadyRegistered:
            pass
