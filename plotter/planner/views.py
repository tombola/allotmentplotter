from tarfile import PAX_NUMBER_FIELDS
from django.shortcuts import render

from django.views.generic import TemplateView


class PlannerView(TemplateView):
    template_name = "planner.html"

    def get(self, request, *args, **kwargs):
        # import pudb; pudb.set_trace();
        context = super().get_context_data(**kwargs)
        # context["test": "hello"]
        return self.render_to_response(context)