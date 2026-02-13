from django import forms
from .models import Location, Supplier, Person, Asset, Task

class BaseBSForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name, f in self.fields.items():
            widget = f.widget
            input_type = getattr(widget, "input_type", "")
            if input_type == "checkbox":
                continue
            if widget.__class__.__name__ == "Select":
                widget.attrs.update({"class":"form-select"})
            else:
                widget.attrs.update({"class":"form-control"})

class LocationForm(BaseBSForm):
    class Meta: model = Location; fields = "__all__"

class SupplierForm(BaseBSForm):
    class Meta: model = Supplier; fields = "__all__"

class PersonForm(BaseBSForm):
    class Meta: model = Person; fields = "__all__"

class AssetForm(BaseBSForm):
    class Meta: model = Asset; fields = "__all__"

class TaskForm(BaseBSForm):
    class Meta: model = Task; fields = "__all__"
