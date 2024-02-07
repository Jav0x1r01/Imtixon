import csv

from django.contrib import admin

from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import redirect, render
import io

from django.urls import path

from apps.models import UserModel

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'old_price', 'sale','image']
    change_list_template = "admin/change_list.html"

    def custom_title(self, obj):
        return ' '.join(obj.title.split()[:4])

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            decoded_file = csv_file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            reader = csv.reader(io_string)
            next(reader)

            result = []
            for row in reader:
                result.append(UserModel(
                    title=(row[0]),
                    price=row[1],
                    old_price=row[2],
                    sale=row[3],
                    image=row[4],


                ))

            UserModel.objects.bulk_create(result)

            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(request, "csv_form.html", payload)

    custom_title.short_description = 'Sarlavha'
