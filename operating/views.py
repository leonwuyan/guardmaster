from detection.models import Excuse, Panel, UISubMenu, UIMainMenu, Tabel
from django.shortcuts import render, get_object_or_404
from detection.views import view_template
from guardmaster import common as Common

# Create your views here.


@Common.competence_required
def notify(request, panel_id, url=Common.URL):
    t = "operating/notify.html"
    d = view_template(request, panel_id, url)
    return render(request, t, d)


@Common.competence_required
def mail(request, panel_id, url=Common.URL):
    t = "operating/mail.html"
    d = view_template(request, panel_id, url)
    panel = get_object_or_404(Panel, pk=panel_id)
    d['servers'] = panel.server_set.all()
    return render(request, t, d)
