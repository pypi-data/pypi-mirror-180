# Common patterns


MedUX is a huge piece of software, so it helps to follow some programming patterns, here they are.


### Code style

Not grey, never use pink. Just use [Black](https://black.readthedocs.io/en/stable/) for code formatting, **before every commit**. 

Use an auto-save trigger that calls `black` in your IDE.

### Django CRUD naming verbs

I chose to stick mostly to Django itself, to be consistent. 
It's not the best IMHO, but anyhow, Django sets the standards.

| View class name | Permission | view name | URL    | Js adjective |
|-----------------|:-----------|-----------|--------|--------------|
| ListView        | view       | list      |        |              |
| DetailView      | view       | detail    |        |              |
| CreateView      | add        | add       | add    | added        |
| UpdateView      | change     | update    | change | changed      |
| DeleteView      | delete     | delete    | delete | deleted      |

So, a simple example urlpatterns could be:

```python 
urlpatterns = [
    path("/", PersonListView.as_view(), name="list"),
    path("add/", PersonCreateView.as_view(), name="add"),
    path("<pk>/", PersonListView.as_view(), name="detail"),
    path("<pk>/change/", PersonUpdateView.as_view(), name="update"),
    path("<pk>/delete/", PersonDeleteView.as_view(), name="delete"),
]
```

Similarly, when using custom Javascript events, use this pattern:

    medux:<model>:<adjective>

Standard case: `adjective` should be built from the verb the view was built of, like *added*, *deleted*, *changed*. 

```python
class PersonUpdateView(...):
    ...
    def form_valid(self, form):
        return HttpResponseEmpty(
            headers={
                "HX-Trigger": "medux:person:added",
            }
        )
```
```django
<div hx-get="{% url 'person:list' %}" hx-trigger="load once, medux:person:added"
```