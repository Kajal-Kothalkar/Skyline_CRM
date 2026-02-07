from django.contrib import admin

from .models import Customer, Interaction


class InteractionInline(admin.TabularInline):
    model = Interaction
    extra = 0


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("full_name", "company", "email", "phone", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("full_name", "email", "company")
    inlines = [InteractionInline]


@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ("interaction_type", "customer", "created_at", "next_follow_up")
    list_filter = ("interaction_type", "created_at")
    search_fields = ("customer__full_name", "notes")
