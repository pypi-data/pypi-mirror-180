import logging

from django.http.response import HttpResponseNotAllowed

logger = logging.getLogger(__file__)


class HtmxResponseMixin:
    """View Mixin to add HTMX functionality.

    If enforce_htmx is True, all requests that do not come from a HTMX
    component are blocked.

    When a HTMX request is detected, the view adds ``_htmx`` to the
    template name. So you can e.g. use different templates for normal
    requests and htmx requests (e.g.  ``model_list.html`` vs
     ``model_list_htmx.html``).
    You can always override that behaviour by explicitly specifying
    a fixed ``template_name`` attribute.
    """

    enforce_htmx = False

    def get_template_names(self):
        # if self.request.htmx:
        #     if self.template_name_suffix:
        #         self.template_name_suffix += "_htmx"
        #     else:
        #         self.template_name_suffix = "_htmx"
        return super().get_template_names()

    def dispatch(self, request, *args, **kwargs):
        if self.enforce_htmx and not self.request.htmx:
            return HttpResponseNotAllowed(
                f"Permission denied: View {self.__class__.__name__} can only be called "
                f"by HTMX."
            )
        response = super().dispatch(request, *args, **kwargs)
        # logger.debug(f"View {self.__class__.__name__} called from HTMX.")
        # FIXME: this should be placed in MedUX' middleware
        # if messages.get_messages(request):
        #     response.headers["HX-Trigger"] = "showMessages"
        return response

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     if self.request.htmx:
    #         context["base_template"] = self.base_template_htmx
    #         print(
    #             f"{self.__class__.__name__}: using {self.base_template_htmx} as base_template."
    #         )
    #     else:
    #         context["base_template"] = self.base_template
    #         print(
    #             f"{self.__class__.__name__}: using {self.base_template} as base_template."
    #         )
    #     return context
