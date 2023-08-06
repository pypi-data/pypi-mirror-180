from django_unicorn.components import UnicornView


class MedicationrequestEntryView(UnicornView):
    med_text = ""
    is_editing: bool = False

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.med_text = kwargs.get("med_text")

    def search(self):
        self.med_text = self.med_text.upper()
        self.is_editing = False

    def clear(self):
        self.med_text = ""
