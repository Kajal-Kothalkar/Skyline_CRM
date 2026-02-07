from django import forms

from .models import Customer, Interaction


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["full_name", "email", "phone", "company", "status"]


class InteractionForm(forms.ModelForm):
    class Meta:
        model = Interaction
        fields = ["interaction_type", "notes", "next_follow_up"]
        widgets = {
            "next_follow_up": forms.DateInput(attrs={"type": "date"}),
        }
