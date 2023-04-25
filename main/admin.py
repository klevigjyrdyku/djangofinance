from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import  CustomUser, Transaction

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'photo_display')
    search_fields = ('username', 'email')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password', 'photo')}),  # shtohet 'photo' në fieldsets
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    def photo_display(self, obj):  # shtohet kjo funksion per 'photo_display'
        if obj.photo:
            return '<img src="%s" width="50px" />' % obj.photo.url
        else:
            return '(No image)'

    photo_display.allow_tags = True

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Transaction)