from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.register(models.Candidate)
admin.site.register(models.Manager)
# admin.site.register(models.Concern)
# admin.site.register(models.UserCertificate)
admin.site.register(models.Sample)


class UserCertificateAdmin(ImportExportModelAdmin):
    list_display = ('email', )


admin.site.register(models.UserCertificate, UserCertificateAdmin)


@admin.register(models.Concern)
class ConcernAdmin(admin.ModelAdmin):
    list_display = ['name', 'manager', 'subject', 'discription']
