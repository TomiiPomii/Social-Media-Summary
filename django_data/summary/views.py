from django.shortcuts import render
from django.views import View
from .collectors.collect import getAllData
from .forms import UrlForm


class HomePageView(View):
    form_class = UrlForm
    template_name = "summary/home.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            urls = {"twitter": form["twitter_url"].value()}
            data = getAllData(urls)
            return render(request, "summary/result.html", {"data": data})

        return render(request, self.template_name, {"form": form})
