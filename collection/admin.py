from django.contrib import admin
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy
# Project Guia imports
from .models import *
from person.models import Person
# Third part imports ##
from ckeditor.widgets import CKEditorWidget
from django_admin_json_editor import JSONEditorWidget
from reversion_compare.admin import CompareVersionAdmin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from digitalassetsmanagement.models import Capture, Doc
from digitalassetsmanagement.widgets import MultipleSelectPreviewImageWidget
from management.models import Acquisition


class ContainerResource(resources.ModelResource):
    class Meta:
        model = Container
        fields = ('uuid', 'title', 'id_human', 'aggregation_type', 'description', 'description_level')
        skip_unchanged = False
        report_skipped = True
        import_id_fields = ('uuid',)
        exclude = ('id_auto_series')


@admin.register(Container)
class ContainerAdmin(CompareVersionAdmin, ImportExportModelAdmin):
    readonly_fields = ('created', 'uuid', 'slug',)
    resource_class = ContainerResource
    list_display = ('get_date_created', 'id_auto_series', 'id_human', 'uuid', 'title', 'description', 'description_level',)
    filter_horizontal = ('items', 'container_child')
    search_fields = ['id_human', 'aggregation_type__title', 'description', 'items__title', 'description_level__title', 'container_child__title']


class CollectionResource(resources.ModelResource):
    class Meta:
        model = Collection
        fields = ('uuid', 'id_human', 'title', 'abstract', 'full_text',
                'description_level', 'aggregation_type',
                'genre_tags', 'dimensions', 'date_start',
                'date_start_caption', 'date_end',
                'date_end_caption', 'capture', 'author',
                'container', 'items_total', 'items_processed',
                'items_online', 'access_condition',
                'access_local_status', 'access_online_status',
                'access_link', 'location_generic',
                'location_specific', 'inventary_status',      'inventary_last_date', 'management_unit')
        skip_unchanged = False
        report_skipped = True
        import_id_fields = ('uuid',)


class CollectionAdminForm(forms.ModelForm):
    id_old = forms.CharField(
        required=False,
        widget=JSONEditorWidget(settings.DATA_SCHEMA, collapsed=True),
        label=ugettext_lazy('Old IDs'))
    full_text = forms.CharField(
        required=False,
        widget=CKEditorWidget(),
        label=ugettext_lazy('Full Text'))
    dimensions = forms.CharField(
        required=False,
        widget=JSONEditorWidget(settings.DATA_SCHEMA, collapsed=True),
        label=ugettext_lazy('Dimensions'))
    inventary_data = forms.CharField(
        required=False,
        widget=JSONEditorWidget(settings.DATA_SCHEMA, collapsed=True),
        label=ugettext_lazy('Inventary Data'))
    other_data = forms.CharField(
        required=False,
        widget=JSONEditorWidget(settings.DATA_SCHEMA, collapsed=True),
        label=ugettext_lazy('Other Unstructured Data'))
    docs = forms.ModelMultipleChoiceField(
        queryset=Doc.objects.all(),
        label=ugettext_lazy('Documents'),
        required=False,
        widget=admin.widgets.FilteredSelectMultiple(
            verbose_name=ugettext_lazy('Documents'),
            is_stacked=False
        )
    )
    acquisitions = forms.ModelMultipleChoiceField(
        queryset=Acquisition.objects.all(),
        label=ugettext_lazy('Acquisitions'),
        required=False,
        widget=admin.widgets.FilteredSelectMultiple(
            verbose_name=ugettext_lazy('Acquisitions'),
            is_stacked=False
        )
    )
    capture = forms.ModelMultipleChoiceField(
        queryset=Capture.objects.all(),
        label=ugettext_lazy('Image'),
        required=False,
        widget=MultipleSelectPreviewImageWidget()
    )

    class Meta:
        model = Collection
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['acquisitions'].widget = RelatedFieldWidgetWrapper(
            self.fields['acquisitions'].widget,
            Collection._meta.get_field('acquisitions').remote_field,
            self.admin_site
        )
        self.fields['capture'].widget = RelatedFieldWidgetWrapper(
            self.fields['capture'].widget,
            Collection._meta.get_field('capture').remote_field,
            self.admin_site
        )
        self.fields['docs'].widget = RelatedFieldWidgetWrapper(
            self.fields['docs'].widget,
            Collection._meta.get_field('docs').remote_field,
            self.admin_site
        )

    def get_queryset(self):
        return Collection.objects.filter(author__is=True)


@admin.register(Collection)
class CollectionAdmin(CompareVersionAdmin, ImportExportModelAdmin):
    readonly_fields = ('created', 'uuid', 'slug',)
    resource_class = CollectionResource
    list_filter = ('management_unit', 'aggregation_type', 'description_level', 'access_condition', 'genre_tags')
    list_display = ('id_auto_series', 'id_human', 'management_unit', 'aggregation_type', 'title', 'description_level', 'access_condition', 'inventary_status', 'items_total', 'is_draft')
    search_fields = ['id_human', 'id_old', 'abstract', 'full_text', 'description_level__title', 'aggregation_type__title', 'genre_tags__title', 'dimensions', 'date_start', 'date_start_caption', 'date_end', 'date_end_caption', 'capture__title', 'author__title', 'container__title', 'access_condition__title', 'location_generic__title', 'management_unit__title', 'other_data', ]
    filter_horizontal = ('capture', 'genre_tags', 'author', 'container')
    fieldsets = (
                (ugettext_lazy('Indentification'),
                    {'fields':  (
                        ('is_draft'),
                        ('uuid', 'created'),
                        ('id_human', 'id_old'),
                        ('management_unit', 'aggregation_type'),
                        ('title', 'slug'),
                        ('capture')),
                    }),
                (ugettext_lazy('Basic Infos'),
                    {'fields': (
                        ('date_start', 'date_start_caption'),
                        ('date_end', 'date_end_caption'),
                        ('access_condition', 'description_level'),
                        ('author'),
                        ('genre_tags'),
                        ('abstract')),
                    }),
                (ugettext_lazy('Location and Dimensions'),
                    {'fields': (
                        ('location_generic', 'location_specific'),
                        ('dimensions')),
                    }),
                (ugettext_lazy('Inventory and Patrimony'),
                    {'fields': (
                        ('inventary_status', 'inventary_last_date'),
                        ('inventary_data')),
                    }),
                (ugettext_lazy('Access'),
                    {'fields': (
                        ('access_local_status', ),
                        ('access_online_status', 'access_link')),
                    }),
                (ugettext_lazy('Processed Status'),
                    {'fields': (
                        ('items_total', 'items_processed', 'items_online')),
                    }),
                (ugettext_lazy('Description'),
                    {'fields': ('full_text', 'container'),
                    }),
                (ugettext_lazy('Other Infos'),
                    {'fields': ('other_data', 'docs', 'acquisitions',),
                    }),
    )
    form = CollectionAdminForm

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.form.admin_site = admin_site

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs["queryset"] = Person.objects.filter(is_feature=True)
        return super().formfield_for_manytomany(db_field, request, **kwargs)
