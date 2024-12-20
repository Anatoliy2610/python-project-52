from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _

from task_manager.tasks.models import Tasks


class MixinDeleteStatus:
    messages_for_error = None
    redirect_for_error = None

    def post(self, request, *args, **kwargs):
        if self.get_object().status.exists():
            messages.error(self.request, (self.messages_for_error))
            return redirect(self.redirect_for_error)
        return super().post(request, *args, **kwargs)


class MixinDeleteLabel:
    messages_for_error = None
    redirect_for_error = None

    def post(self, request, *args, **kwargs):
        if self.get_object().labels.exists():
            messages.error(self.request, (self.messages_for_error))
            return redirect(self.redirect_for_error)
        return super().post(request, *args, **kwargs)


class MixinDeleteTask:
    messages_for_error = None
    redirect_for_error = None

    def get(self, request, *args, **kwargs):
        if self.get_object().author != self.request.user:
            messages.error(
                self.request, _("An issue can only be deleted by its author.")
            )
            return redirect(self.redirect_for_error)
        return super().get(request, *args, **kwargs)


class MixinDeleteUser:
    flash_get = None
    flash_post = None
    redirect_for_error = None

    def get(self, request, *args, **kwargs):
        if self.get_object().username != self.request.user.username:
            messages.error(self.request, (self.flash_get))
            return redirect(self.redirect_for_error)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if Tasks.objects.filter(author=self.get_object().id):
            messages.error(self.request, (self.flash_post))
            return redirect(self.redirect_for_error)
        return super().post(request, *args, **kwargs)


class MixinUpdateUser:
    messages_for_error = None
    redirect_for_error = None

    def get(self, request, *args, **kwargs):
        if self.get_object().username != self.request.user.username:
            messages.error(self.request, (self.messages_for_error))
            return redirect(self.redirect_for_error)
        return super().get(request, *args, **kwargs)


class MixinLoginRequired:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                self.request,
                _("You are not logged in! Please log in."),
            )
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)
