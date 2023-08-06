# User Interface Elements

## Breadcrumbs

Breadcrumbs are rendered using a templatetag `breadcrumb`. Define a "breadcrumbs" block in your base template:

```django
{% block breadcrumbs %}
  {% breadcrumb "Home" "home" %}
{% endblock %}
```
Then override it in your page template:

```django
{% block breadcrumbs %}
  {{ block.super }}
  {% breadcrumb page_title "person:detail" %}
{% endblock %}
```

Don't forget `block.super` - to keep the trail before the current crumb.

## Modal dialogs

To create modal dialogs easily, [Benoit Blanchon](https://blog.benoitblanchon.fr) showed a easy and versatile way of doing them with Django/HTMX.
There is a global `#modal` element that can be used as  `hx-target` to load views in a modal. Just add a link like this:

```django
<button hx-get="{% url 'tenant:add' %}" hx-target="#modal">
```

and it will open in a modal dialog. You are responsible for the content, it will render everything the view returns within this HTML, so make sure you use `modal-header`, `modal-content`, and `modal-footer` appropriately:

```django
<div id="modal" class="modal">
    <div id="dialog" class="modal-dialog" hx-target="this">
        <!-- your content here -->
    </div>
</div>
```

### Modal form views

Mostly, modals are used when opening a form for creating/editing new content, a common pattern is opening the modal using HTMX. There are a few helpers to ease that work, [ModalFormViewMixin][medux.common.api.interfaces.ModalFormViewMixin].

```django
<button class="btn" hx-get="{% url 'person:add' %}">Add person</button>

<div class="people-list"
     hx-trigger="load, medux:person:added"
     hx-get="person:list"
     hx-disinherit="*">
<!-- dynamically loaded content -->
</div>

```
where `person:add` is the name of a CreateView in your urls.py. The `hx-disinherit` attribute is used, so child elements like buttons keep their natural trigger, see below. 

To create the view, inherit from ModalFormViewMixin, and define a few class attributes:

```python
from medux.common.api.interfaces import ModalFormViewMixin
from django.views.generic import CreateView
from ... import Person

class PersonCreateView(ModalFormViewMixin, CreateView):
    model = Person
    # form_class = PersonCreateForm
    modal_title = "Add new person"
    success_event = "medux:person:added"
    
```

This creates a working modal dialog that contains your view template.
It provides `Cancel` and `Submit` buttons at the footer, and renders your form as **crispy** form - you could customize that form further, but don't forget a few things:

* always remove the crispy form tags: `self.helper.form_tags = False`
* `modal_title` is self-explanatory
* `success_event` describes an event that is emitted on the client after the form has been submitted successfully. You can react to that specifically: In the code above, `hx-trigger` is set to not only `load`, but also to this special event. So each time the form returns successfully, the list is reloaded. 