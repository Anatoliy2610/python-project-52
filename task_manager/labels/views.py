from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.utils import MixinDeleteLabel, MixinLoginRequired

from .forms import CreateUpdateLabelForm
from .models import Labels


class LabelsHome(
    LoginRequiredMixin, MixinLoginRequired, SuccessMessageMixin, ListView
):
    model = Labels
    template_name = "labels/labels.html"
    context_object_name = "labels"
    extra_context = {"title": _("Labels")}

    def get_queryset(self):
        return Labels.objects.all()


class LabelsCreate(
    LoginRequiredMixin, MixinLoginRequired, SuccessMessageMixin, CreateView
):
    form_class = CreateUpdateLabelForm
    model = Labels
    template_name = "actions/create_or_update.html"
    success_url = reverse_lazy("labels")
    success_message = _("The label was created successfully")
    extra_context = {
        "title": _("Create a label"),
        "button_text": _("Create"),
    }


class LabelsUpdate(
    LoginRequiredMixin, MixinLoginRequired, SuccessMessageMixin, UpdateView
):
    form_class = CreateUpdateLabelForm
    model = Labels
    template_name = "actions/create_or_update.html"
    success_url = reverse_lazy("labels")
    pk_url_kwarg = "label_id"
    extra_context = {
        "title": _("Changing the label"),
        "button_text": _("Update"),
    }
    success_message = _("The label has been successfully changed")


class LabelsDelete(
    LoginRequiredMixin,
    MixinLoginRequired,
    SuccessMessageMixin,
    MixinDeleteLabel,
    DeleteView,
):
    model = Labels
    template_name = "actions/delete.html"
    pk_url_kwarg = "label_id"
    context_object_name = "labels1"
    extra_context = {
        "title": _("Deleting a label"),
        "button_text": _("Delete"),
    }
    success_url = reverse_lazy("labels")
    success_message = _("The label was successfully deleted")
    messages_for_error = _(
        "It is not possible to remove the label because it is being used"
    )
    redirect_for_error = "labels"
