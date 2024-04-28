from django.views.generic import ListView

from .models import Stat


class StatListView(ListView):
    model = Stat
    template_name = "stat_list.html"
