from django.contrib import admin
from .models import (
    Role,
    User,
    Event,
    Question,
    Cutaway,
    Speech,
    )


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    raw_id_fields = [
        'users',
    ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Cutaway)
class CutawayAdmin(admin.ModelAdmin):
    pass


@admin.register(Speech)
class SpeechAdmin(admin.ModelAdmin):
    pass
