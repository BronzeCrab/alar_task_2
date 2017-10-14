from django.views.generic import TemplateView
from django.shortcuts import render
from .tasks import test_task


class TestView(TemplateView):
    template_name = 'test.html'

    def get(self, request, *args, **kwargs):
        test_task.delay()
        return render(request, self.template_name)
