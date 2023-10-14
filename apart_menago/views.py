from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.utils import timezone

# Create your views here.
from django.views import generic, View
from django.urls import reverse
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404

from apart_menago.forms import NameForm


def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/thanks/")

    else:
        form = NameForm()
    return render(request, "name.html", {"form": form})


class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse("result")


class MyFormView(View):
    form_class = NameForm
    initial = {"key": "value"}
    template_name = "apart_menago/name.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect("/success/")

        return render(request, self.template_name, {"form": form})
