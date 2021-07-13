from django.contrib import admin
from .models import Comment, User, Match, Prediction, MatchDescription, Post


def make_user_is_premium(modelAdmin, request, queryset):
    queryset.update(is_premium=True)


def make_user_is_default(modelAdmin, request, queryset):
    queryset.update(
        is_premium=False,
    )


# Register your models here.
class MatchAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']

    list_filter = [
        'title',
        'category',
    ]


class PredictionAdmin(admin.ModelAdmin):
    list_display = ['title', 'prediction_category']


class DescriptionAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone', 'country', 'payment_code', 'is_premium']

    list_filter = [
        'is_premium',
    ]

    actions = [
        make_user_is_premium,
        make_user_is_default
    ]

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']

admin.site.register(User, UserAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Prediction, PredictionAdmin)
admin.site.register(MatchDescription, DescriptionAdmin)
admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)
