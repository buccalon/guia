from django.contrib.postgres.fields import JSONField
from django.contrib.gis.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from guia.models import Base, DraftModel

# Third part imports
import reversion


@reversion.register()
class Exhibition(Base, DraftModel):
    """To store Exhibition data"""
    id_human = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        unique=True,
        help_text=_('Institucional Identifier'),
        verbose_name=_('Institucional ID'))
    abstract = models.TextField(
        null=True,
        blank=True,
        help_text=_('Ex.: This exhibition is composed by...'),
        verbose_name=_('Abstract'))
    full_text = models.TextField(
        null=True,
        blank=True,
        help_text=_('Ex.: This exhibition is about...'),
        verbose_name=_('Full Text'))
    capture = models.ManyToManyField(
        'digitalassetsmanagement.capture',
        blank=True,
        help_text=_('Choose some introduction and representative images'),
        verbose_name=_('Image'))
    date_start = models.DateField(
        null=True,
        blank=True,
        help_text=_('Choose a start date'),
        verbose_name=_('Initial Date'))
    date_end = models.DateField(
        null=True,
        blank=True,
        help_text=_('Choose an final date'),
        verbose_name=_('Final date'))
    locations = models.ManyToManyField(
        'location.Location',
        help_text=_('What is the exhibition edition location?'),
        verbose_name=_('Location'))
    link = models.URLField(
        null=True,
        blank=True,
        help_text=_('Do you have some online link to this edition?'),
        verbose_name=_('Link'))
    team = JSONField(
        null=True,
        blank=True,
        help_text=_('Infos about the exhibition team'),
        verbose_name=_('Team'))
    catalog = models.ManyToManyField(
        'publication.Publication',
        related_name='exhibitionCatalog',
        blank=True,
        help_text=_("Is there an catalog about the exhibition?"),
        verbose_name=_('Catalog(s)'))
    publication = models.ManyToManyField(
        'publication.Publication',
        related_name='exhibitionPublication',
        blank=True,
        help_text=_("Is there any other publications about the exhibition?"),
        verbose_name=_('Publication(s)'))
    docs = models.ManyToManyField(
        'digitalassetsmanagement.Doc',
        blank=True,
        verbose_name=_('Documents'))
    audience = models.IntegerField(
        verbose_name=_('Audience'),
        blank=True,
        null=True,
        help_text=_("Number of participants"))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.slug is not None:
            return reverse('exhibition_detail_slug', kwargs={'slug': self.slug})
        else:
            return reverse('exhibition_detail', kwargs={'pk': self.id_auto_series})

    def save(self, *args, **kwargs):
        if self.id_auto_series is None:
            super().save()

        raw_slug = [
            self.title,
            str(self.id_auto_series),
        ]
        self.slug = slugify(' '.join(raw_slug))
        return super().save()

    class Meta:
        verbose_name = _('Exhibition')
        verbose_name_plural = _('Exhibitions')


@reversion.register()
class ExhibitionEdition(Base):
    """Used to label editions of Exhibitions"""
    id_human = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        unique=True,
        help_text=_('Institucional Identifier'),
        verbose_name=_('Institucional ID'))
    exhibition = models.ForeignKey(
        Exhibition,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('The main Exhibition source from this edition'),
        verbose_name=_('Original Exhibition'))
    full_text = models.TextField(
        null=True,
        blank=True,
        help_text=_('Ex.: This exhibition is about...'),
        verbose_name=_('Full Text'))
    location = models.ForeignKey(
        'location.Location',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('What is the location where occurs this exhibition edition?'),
        verbose_name=_('Location'))
    date_start = models.DateField(
        null=True,
        blank=True,
        help_text=_('Choose a start date'),
        verbose_name=_('Initial Date'))
    date_end = models.DateField(
        null=True,
        blank=True,
        help_text=_('Choose an final date'),
        verbose_name=_('Final date'))
    team = JSONField(
        null=True,
        blank=True,
        help_text=_('Infos about the edition team'),
        verbose_name=_('Team'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Exhibition Edition')
        verbose_name_plural = _('Exhibition Editions')
