from django_unicorn.components import UnicornView


class MedicationRequestLine(UnicornView):
    # template_name = "core/medicationrequest_line.html"

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        # self.name = kwargs.get("name")

    def search(self, **kwargs):
        med_text = kwargs["medication_name"]
        self.med_text = med_text
