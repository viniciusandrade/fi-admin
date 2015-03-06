from django.contrib.contenttypes.generic import generic_inlineformset_factory
from django.forms import widgets
from django import forms
from django.conf import settings

from main.models import Descriptor, Keyword, ResourceThematic
from utils.forms import DescriptorRequired, ResourceThematicRequired

from models import *

import simplejson

class BiblioRefForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.user_data = kwargs.pop('user_data', None)

        super(BiblioRefForm, self).__init__(*args, **kwargs)

        if self.user_data['service_role'].get('BiblioRef') == 'doc':
            self.fields['status'].widget = widgets.HiddenInput()


    def save(self, *args, **kwargs):
        obj = super(BiblioRefForm, self).save(commit=False)

        # for fields with readonly attribute restore the original value for POST data insertions hack
        for name, field in self.fields.items():
            if hasattr(field.widget.attrs, 'readonly'):
                setattr(obj, name, field.widget.original_value)

        # save modifications
        obj.save()

        return obj

    class Meta:
        model = Reference
        exclude = ('cooperative_center_code',)

        source_language = forms.MultipleChoiceField()


# definition of inline formsets
DescriptorFormSet = generic_inlineformset_factory(Descriptor, formset=DescriptorRequired, 
                                                  can_delete=True, extra=1)

KeywordFormSet = generic_inlineformset_factory(Keyword, can_delete=True, extra=1)

ResourceThematicFormSet = generic_inlineformset_factory(ResourceThematic, 
                                                        formset=ResourceThematicRequired, can_delete=True, extra=1)

