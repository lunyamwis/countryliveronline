from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def make_crud(
    *,
    model_,
    form_class_,
    prefix: str,
    template_base: str = "shared",
    paginate_by: int = 20,
    ordering=None,
    search_fields=None,
    list_columns=None,
    detail_groups=None,
    staff_only_write: bool = True,
):
    
    if ordering is None:
        ordering = ["-id"]
    if search_fields is None:
        search_fields = []
    if list_columns is None:
        list_columns = []
    if detail_groups is None:
        detail_groups = [{"title": "Details", "fields": list_columns}]

    class _BaseCtx:
        model = model_
        form_class = form_class_

        def get_context_data(self, **kwargs):
            ctx = super().get_context_data(**kwargs)
            ctx["crud_prefix"] = prefix
            ctx["model_meta"] = {
                "app_label": model_._meta.app_label,
                "model__name": model_._meta.model_name,
                "verbose__name": model_._meta.verbose_name,
                "verbose_name_plural": model_._meta.verbose_name_plural,
            }
            ctx["list_columns"] = list_columns
            ctx["detail_groups"] = detail_groups
            return ctx

    class List(_BaseCtx, ListView):
        template_name = f"{template_base}/generic_list.html"
        paginate_by = 20
        ordering = None

        def get_queryset(self):
            qs = super().get_queryset()
            q = (self.request.GET.get("q") or "").strip()
            if q and search_fields:
                query = Q()
                for f in search_fields:
                    query |= Q(**{f"{f}__icontains": q})
                qs = qs.filter(query)
            return qs

    class Detail(_BaseCtx, DetailView):
        template_name = f"{template_base}/generic_detail.html"
        context_object_name = "obj"

    class _WritePerm(LoginRequiredMixin):
        def dispatch(self, request, *args, **kwargs):
            if staff_only_write and not (request.user.is_authenticated and request.user.is_staff):
                if request.user.is_authenticated and not request.user.is_staff:
                    from django.http import HttpResponseForbidden
                    return HttpResponseForbidden("Staff only.")
            return super().dispatch(request, *args, **kwargs)

    class Create(_WritePerm, _BaseCtx, CreateView):
        template_name = f"{template_base}/form.html"

    class Update(_WritePerm, _BaseCtx, UpdateView):
        template_name = f"{template_base}/form.html"

    class Delete(_WritePerm, _BaseCtx, DeleteView):
        template_name = f"{template_base}/confirm_delete.html"
        success_url = reverse_lazy(f"{prefix}_list")

    return {"List": List, "Detail": Detail, "Create": Create, "Update": Update, "Delete": Delete}
