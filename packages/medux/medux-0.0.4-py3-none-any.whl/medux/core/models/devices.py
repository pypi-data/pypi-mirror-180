from enum import Enum

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from ..fields import CodeField
from medux.core.models import PackageDataModel
from medux.common.models import BaseModel


class DeviceType(PackageDataModel):
    pass


class Device(BaseModel):
    class Status(Enum):
        ACTIVE = "active"
        INACTIVE = "inactive"
        ENTERED_IN_ERROR = "entered_in_error"
        UNKNOWN = "unknown"

    class StatusReason(Enum):
        ONLINE = "online"
        PAUSED = "paused"
        STANDBY = "standby"
        OFFLINE = "offline"
        NOT_READY = "not_ready"
        TRANSDUC_DISCONNECTED = "transduc_discon"
        HARDWARE_DISCONNECTED = "hardware__discon"
        OFF = "off"

    status = CodeField(
        terminology_binding=Status,
        default="active",
        help_text=_("Status of the device availability"),
    )
    statusReason = CodeField(
        terminology_binding=StatusReason,
        default="online",
        help_text=_("reason for the status of the device availability"),
    )
    distinct_identifier = models.CharField(
        max_length=255, blank=True, help_text=_("The distinct identification string")
    )
    manufacturer = models.CharField(
        max_length=255, blank=True, help_text=_("Name of device manufacturer")
    )
    manufacture_date = models.DateField(
        blank=True, null=True, help_text=_("Date when the device was made")
    )
    expiration_date = models.DateField(
        blank=True,
        null=True,
        help_text=_("Date and time of expiry of this device (if applicable)"),
    )
    lot_number = models.CharField(
        max_length=255,
        blank=True,
        help_text=_("Lot number assigned by the manufacturer"),
    )
    serial_number = models.CharField(
        max_length=255,
        blank=True,
        help_text=_("Serial number assigned by the manufacturer"),
    )
    device_name = models.CharField(
        max_length=255,
        blank=True,
        help_text=_("The name of the device as given by the manufacturer"),
    )
    model_number = models.CharField(
        max_length=255,
        blank=True,
        help_text=_("The model number for the device"),
    )
    part_number = models.CharField(
        max_length=255,
        blank=True,
        help_text=_("The part number for the device"),
    )

    type = models.ForeignKey(
        DeviceType,
        blank=True,
        null=True,
        help_text=_("The kind or type of device"),
        on_delete=models.PROTECT,
    )

    # specialization
    # version
    # property

    patient = models.ForeignKey(
        "Patient",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_("Patient to whom Device is affixed"),
    )

    owner = models.ForeignKey(
        "Organization",
        null=True,
        on_delete=models.SET_NULL,
        help_text=_("Organization responsible for device"),
    )
    contact = models.ManyToManyField("ContactPoint", blank=True)
    location = models.CharField(max_length=255, blank=True)
    url = models.URLField(blank=True)
    parent = models.ForeignKey(
        "Device", blank=True, null=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.device_name} (SN: {self.serial_number or _('n/a')})"

    def clean(self):
        if not self.device_name and not self.serial_number:
            raise ValidationError(
                _("A device must have either a device name or a serial number.")
            )
