from django.contrib import admin
from .models import (
    Role,
    User,
    Event,
    Question,
    Cutaway,
    Speech,
)


class SpeechInline(admin.TabularInline):
    model = Speech
    ordering = [
        'time_start',
    ]


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'tg_id',
        'role',
    ]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    raw_id_fields = [
        'users',
    ]
    inlines = [SpeechInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'speech',
        'text',
    ]


@admin.register(Cutaway)
class CutawayAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'first_name',
        'last_name',
        'age',
        'specialization',
        'location',
    ]


@admin.register(Speech)
class SpeechAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'user',
        'event',
        'time_start',
        'time_end',
    ]
