#! coding: utf-8
from collections import OrderedDict
from django.utils.translation import ugettext_lazy as _, get_language
from django.utils.translation import string_concat
from django.contrib.contenttypes.generic import generic_inlineformset_factory
from django.forms import widgets
from django import forms
from form_utils.forms import BetterModelForm, FieldsetCollection
from form_utils.widgets import AutoResizeTextarea
from django.conf import settings

from main.models import Descriptor, Keyword, ResourceThematic
from utils.forms import DescriptorRequired, ResourceThematicRequired

from models import *
import json


class SelectDocumentTypeForm(forms.Form):
    DOCUMENT_TYPE_CHOICES = (
        # ('MS', _('Monograph Series')),
        # ('', _('Monograph in a Collection')),
        ('M', _('Monograph')),
        ('N', _('Non conventional')),
        ('S', _('Periodical Series')),
        # ('', _('Collection')),
        # ('TS', _('Thesis, Dissertation appearing as a Monograph Series')),
        ('T', _('Thesis, Dissertation')),
    )

    document_type = forms.ChoiceField(choices=DOCUMENT_TYPE_CHOICES)


class BiblioRefForm(BetterModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.user_data = kwargs.pop('user_data', None)
        self.document_type = kwargs.pop('document_type', None)
        self.reference_source = kwargs.pop('reference_source')
        self.is_LILACS = False

        fieldsets = kwargs.pop('fieldsets', None)

        super(BiblioRefForm, self).__init__(*args, **kwargs)

        # used for fieldsets method for construct internal fieldset_collection
        self._fieldsets = fieldsets

        # hidden status field for documentalist profile
        if self.user_data['service_role'].get('BiblioRef') == 'doc':
            self.fields['status'].widget = widgets.HiddenInput()

    def fieldsets(self):
        if not self._fieldset_collection:
            self._fieldset_collection = FieldsetCollection(self, self._fieldsets)

        return self._fieldset_collection

    def clean(self):
        data = self.cleaned_data
        error_messages = []

        for field_name, field_value in self.fields.iteritems():
            field_check = data[field_name]

            if isinstance(self.fields[field_name].widget, forms.widgets.Textarea):
                if '%' in field_check:
                    self.add_error(field_name, _("The % simbol don't separete occurences"))

            if isinstance(field_check, basestring):
                if field_check.strip().endswith('.'):
                    self.add_error(field_name, _("Point at end of field is not allowed"))

        # Always return the full collection of cleaned data.
        return data

    def clean_database(self):
        data = self.cleaned_data['database']
        if "LILACS" in data:
            self.is_LILACS = True

        return data

    def clean_individual_author_monographic(self):
        field = 'individual_author_monographic'
        data = self.cleaned_data[field]

        if self.document_type[0] == 'T':
            if not data:
                self.add_error(field, _("Mandatory"))
            else:
                occ = 0
                for author in data:
                    occ = occ + 1
                    author_name = author.get('text', '')
                    message_item = _("item %s: ") % occ
                    if author_name == 'Anon':
                        message = _("Thesis's author anonymous")
                        message = string_concat(message_item, message)
                        self.add_error(field, message)
                    if not ',' in author_name:
                        message = _("Comma abscent")
                        message = string_concat(message_item, message)
                        self.add_error(field, message)
                    elif not ', ' in author_name:
                        message = _("Insert space after comma")
                        message = string_concat(message_item, message)
                        self.add_error(field, message)
        else:
            occ = 0
            for author in data:
                occ = occ + 1
                author_name = author.get('text', '')
                message_item = _("item %s: ") % occ
                if author_name != 'Anon':
                    if not ',' in author_name and self.is_LILACS:
                        message = "Comma absense or error in the word Anon"
                        message = string_concat(message_item, message)
                        self.add_error(field, message)



        return data

    def clean_electronic_address(self):
        field = 'electronic_address'
        data = self.cleaned_data[field]
        LILACS_compatible_languages = ['pt', 'es', 'en', 'fr']
        url_list = []

        if data:
            occ = 0
            for electronic_address in data:
                occ = occ + 1
                url = electronic_address.get('_u', '')
                message_item = _("item %s: ") % occ
                if self.is_LILACS:
                    if electronic_address.get('_q', '') == '':
                        message = _("File extension attribute is mandatory")
                        message = string_concat(message_item, message)
                        self.add_error(field, message)

                    if electronic_address.get('_y', '') == '':
                        message = _("File type attribute is mandatory")
                        message = string_concat(message_item, message)
                        self.add_error(field, message)

                    if electronic_address.get('_i', '') not in LILACS_compatible_languages:
                        message = _("Language incompatible with LILACS")
                        message = string_concat(message_item, message)
                        self.add_error(field, message)

                    if url not in url_list:
                        url_list.append(url)
                    else:
                        message = _("URL duplicated")
                        message = string_concat(message_item, message)
                        self.add_error(field, message)

        return data

    def clean_record_type(self):
        field = 'record_type'
        data = self.cleaned_data[field]
        message = ''

        if data and self.is_LILACS:
            if data == 'c':
                message = _("Printed music in the Record Type is incompatible with the LILACS Methodology")
            elif data == 'd':
                message = _("Manuscript music in the Record Type is incompatible with the LILACS Methodology")
            elif data == 'e':
                message = _("Printed cartographic material in the Record Type is incompatible with the LILACS Methodology")
            elif data == 'f':
                message = _("Manuscript cartographic material in the Record Type is incompatible with the LILACS Methodology")
            elif data == 'j':
                message = _("Musical sound recording in the Record Type is incompatible with the LILACS Methodology")
            elif data == 'k':
                message = _("Two-dimensional nonprojectable graphic in the Record Type is incompatible with the LILACS Methodology")
            elif data == 'm':
                message = _("Computer file in the Record Type is incompatible with the LILACS Methodology")
            elif data == 'o':
                message = _("Kit in the Record Type is incompatible with the LILACS Methodology")
            elif data == 'p':
                message = _("Mixed material in the Record Type is incompatible with the LILACS Methodology")
            elif data == 'r':
                message = _("Three-dimensional artifact or naturally occurring object in the Record Type is incompatible with the LILACS Methodology")
            elif data == 't':
                message = _("Manuscript language material in the Record Type is incompatible with the LILACS Methodology")

            if message:
                self.add_error(field, message)

        return data

    def save(self, *args, **kwargs):
        obj = super(BiblioRefForm, self).save(commit=False)

        # if is a new analytic save reference source info
        if self.reference_source:
            obj.source = self.reference_source

        obj.literature_type = self.document_type[0]
        obj.treatment_level = self.document_type[1:]

        if self.document_type[0] == 'S':
            if self.document_type == 'S':
                obj.reference_title = u"{0}; {1} ({2}), {3}".format(self.cleaned_data['title_serial'],
                                                                    self.cleaned_data['volume_serial'],
                                                                    self.cleaned_data['issue_number'],
                                                                    self.cleaned_data['publication_date_normalized'][:4])
            elif self.document_type == 'Sas':
                if self.cleaned_data['title']:
                    analytic_title = self.cleaned_data['title']
                    analytic_title = analytic_title[0]['text']
                    obj.reference_title = u"{0} | {1}".format(obj.source.reference_title, analytic_title)
        else:
            if 'a' in self.document_type:
                analytic_title = self.cleaned_data['title']
                analytic_title = analytic_title[0]['text']
                obj.reference_title = u"{0} | {1}".format(obj.source.reference_title, analytic_title)
            else:
                obj.reference_title = u"{0}".format(self.cleaned_data['title_monographic'])

        # for fields with readonly attribute restore the original value for POST data insertions hack
        for name, field in self.fields.items():
            if hasattr(field.widget.attrs, 'readonly'):
                setattr(obj, name, field.widget.original_value)

        # save modifications
        obj.save()

        return obj


class BiblioRefSourceForm(BiblioRefForm):
    class Meta:
        model = ReferenceSource
        exclude = ('cooperative_center_code',)


class BiblioRefAnalyticForm(BiblioRefForm):
    class Meta:
        model = ReferenceAnalytic
        exclude = ('source', 'cooperative_center_code',)


# definition of inline formsets
DescriptorFormSet = generic_inlineformset_factory(Descriptor, can_delete=True, extra=1)

KeywordFormSet = generic_inlineformset_factory(Keyword, can_delete=True, extra=1)

ResourceThematicFormSet = generic_inlineformset_factory(ResourceThematic, can_delete=True, extra=1)
