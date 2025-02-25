from django.contrib import admin
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _
# Project Guia imports
from .models import *
## Third part imports ##
from ckeditor.widgets import CKEditorWidget
from django_admin_json_editor import JSONEditorWidget
from reversion_compare.admin import CompareVersionAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from digitalassetsmanagement.models import Capture, Doc
from digitalassetsmanagement.widgets import MultipleSelectPreviewImageWidget


class PublicationTypeResource(resources.ModelResource):

    class Meta:
        model = PublicationType


@admin.register(PublicationType)
class PublicationTypeAdmin(CompareVersionAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'uuid', 'slug',)
    resource_class = PublicationTypeResource
    list_display = ('id_auto_series', 'title', 'description')
    search_fields = ['__all__']


class PublicationAdminForm(forms.ModelForm):
    full_text = forms.CharField(
        required=False,
        widget=CKEditorWidget(),
        label=_('Full Description'))
    dimension = forms.CharField(
        required=False,
        widget=JSONEditorWidget(settings.DATA_SCHEMA, collapsed=False),
        label=_('Dimensions'))
    other_data = forms.CharField(
        required=False,
        widget=JSONEditorWidget(settings.DATA_SCHEMA, collapsed=False),
        label=_('Other Unstructured Data'))
    capture = forms.ModelMultipleChoiceField(
        queryset=Capture.objects.all(),
        label=_('Image'),
        required=False,
        widget=MultipleSelectPreviewImageWidget()
    )
    docs = forms.ModelMultipleChoiceField(
        queryset=Doc.objects.all(),
        label=_('Documents'),
        required=False,
        widget=admin.widgets.FilteredSelectMultiple(
            verbose_name=_('Documents'),
            is_stacked=False
        )
    )

    class Meta:
        model = Publication
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['capture'].widget = RelatedFieldWidgetWrapper(
            self.fields['capture'].widget,
            Publication._meta.get_field('capture').remote_field,
            self.admin_site
        )
        self.fields['docs'].widget = RelatedFieldWidgetWrapper(
            self.fields['docs'].widget,
            Publication._meta.get_field('docs').remote_field,
            self.admin_site
        )


class PublicationResource(resources.ModelResource):

    class Meta:
        model = Publication
        fields = ('uuid', 'title', 'id_human', 'type', 'abstract', 'full_text', 'date_released', )
        skip_unchanged = False
        report_skipped = True
        import_id_fields = ('uuid',)
        exclude = ('id_auto_series')


@admin.register(Publication)
class PublicationAdmin(CompareVersionAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'uuid', 'slug', )
    resource_class = PublicationResource
    list_display = ('id_auto_series', 'uuid', 'title', 'date_released', 'is_draft')
    search_fields = ['title']
    filter_horizontal = ('author', 'publisher', 'capture')
    form = PublicationAdminForm

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.form.admin_site = admin_site
