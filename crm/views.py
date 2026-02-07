from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView

from .forms import CustomerForm, InteractionForm
from .models import Customer, Interaction


def dashboard(request):
    status_breakdown = (
        Customer.objects.values("status").annotate(total=Count("id")).order_by("status")
    )
    recent_customers = Customer.objects.all()[:5]
    recent_interactions = Interaction.objects.select_related("customer")[:5]
    return render(
        request,
        "crm/dashboard.html",
        {
            "status_breakdown": status_breakdown,
            "recent_customers": recent_customers,
            "recent_interactions": recent_interactions,
        },
    )


class CustomerListView(ListView):
    model = Customer
    template_name = "crm/customer_list.html"
    paginate_by = 20


class CustomerDetailView(DetailView):
    model = Customer
    template_name = "crm/customer_detail.html"


def customer_create(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect("crm:customer_detail", pk=customer.pk)
    else:
        form = CustomerForm()
    return render(request, "crm/customer_form.html", {"form": form, "mode": "Create"})


def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("crm:customer_detail", pk=customer.pk)
    else:
        form = CustomerForm(instance=customer)
    return render(
        request,
        "crm/customer_form.html",
        {"form": form, "mode": "Update", "customer": customer},
    )


def interaction_create(request, customer_pk):
    customer = get_object_or_404(Customer, pk=customer_pk)
    if request.method == "POST":
        form = InteractionForm(request.POST)
        if form.is_valid():
            interaction = form.save(commit=False)
            interaction.customer = customer
            interaction.save()
            return redirect("crm:customer_detail", pk=customer.pk)
    else:
        form = InteractionForm()
    return render(
        request,
        "crm/interaction_form.html",
        {"form": form, "customer": customer},
    )


def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        customer.delete()
        return redirect(reverse("crm:customer_list"))
    return render(request, "crm/customer_confirm_delete.html", {"customer": customer})
