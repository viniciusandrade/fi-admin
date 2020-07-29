# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='updated', null=True)),
                ('status', models.SmallIntegerField(default=0, null=True, verbose_name='Status', choices=[(0, 'Pending'), (1, 'Admitted'), (2, 'Refused'), (3, 'Deleted')])),
                ('reference_title', models.TextField(verbose_name='Title', blank=True)),
                ('cooperative_center_code', models.CharField(max_length=55, verbose_name='Cooperative center', blank=True)),
                ('call_number', utils.fields.JSONField(null=True, verbose_name='Call number', blank=True)),
                ('database', models.TextField(verbose_name='Database', blank=True)),
                ('literature_type', models.CharField(max_length=10, verbose_name='Literature type', blank=True)),
                ('treatment_level', models.CharField(max_length=10, verbose_name='Treatment level', blank=True)),
                ('electronic_address', utils.fields.JSONField(null=True, verbose_name='Electronic address', blank=True)),
                ('record_type', utils.fields.AuxiliaryChoiceField(max_length=10, verbose_name='Record type', blank=True)),
                ('descriptive_information', utils.fields.JSONField(null=True, verbose_name='Descriptive information', blank=True)),
                ('text_language', utils.fields.MultipleAuxiliaryChoiceField(verbose_name='Text language', blank=True)),
                ('internal_note', models.TextField(verbose_name='Internal note', blank=True)),
                ('publication_date', models.CharField(max_length=250, verbose_name='Publication date', blank=True)),
                ('publication_date_normalized', models.CharField(max_length=25, verbose_name='Publication normalized date', blank=True)),
                ('total_number_of_references', models.CharField(max_length=100, verbose_name='Total number of references', blank=True)),
                ('time_limits_from', models.CharField(max_length=50, verbose_name='Time limits (from)', blank=True)),
                ('time_limits_to', models.CharField(max_length=50, verbose_name='Time limits (to)', blank=True)),
                ('person_as_subject', models.TextField(verbose_name='Person as subject', blank=True)),
                ('non_decs_region', models.TextField(verbose_name='Non-DeCS Region', blank=True)),
                ('abstract', utils.fields.JSONField(null=True, verbose_name='Abstract', blank=True)),
                ('transfer_date_to_database', models.CharField(max_length=20, verbose_name='Transfer date do database', blank=True)),
                ('author_keyword', utils.fields.JSONField(null=True, verbose_name='Author keyword', blank=True)),
                ('item_form', utils.fields.AuxiliaryChoiceField(max_length=10, verbose_name='Item form', blank=True)),
                ('type_of_computer_file', utils.fields.AuxiliaryChoiceField(max_length=10, verbose_name='Type of computer file', blank=True)),
                ('type_of_cartographic_material', utils.fields.AuxiliaryChoiceField(max_length=10, verbose_name='Type of cartographic material', blank=True)),
                ('type_of_journal', utils.fields.AuxiliaryChoiceField(max_length=10, verbose_name='Type of journal', blank=True)),
                ('type_of_visual_material', utils.fields.AuxiliaryChoiceField(max_length=10, verbose_name='Type of visual material', blank=True)),
                ('specific_designation_of_the_material', utils.fields.AuxiliaryChoiceField(max_length=10, verbose_name='Specific designation of the material', blank=True)),
                ('general_note', models.TextField(verbose_name='General note', blank=True)),
                ('formatted_contents_note', models.TextField(verbose_name='Formatted contents note', blank=True)),
                ('additional_physical_form_available_note', models.TextField(verbose_name='Additional physical form available note', blank=True)),
                ('reproduction_note', models.TextField(verbose_name='Reproduction note', blank=True)),
                ('original_version_note', models.TextField(verbose_name='Original version note', blank=True)),
                ('institution_as_subject', models.TextField(verbose_name='Institution as subject', blank=True)),
                ('local_descriptors', models.TextField(verbose_name='Local descriptors', blank=True)),
                ('software_version', models.CharField(max_length=50, verbose_name='Software version', blank=True)),
                ('LILACS_original_id', models.CharField(max_length=8, verbose_name='LILACS id', blank=True)),
            ],
            options={
                'verbose_name': 'Bibliographic Reference',
                'verbose_name_plural': 'Bibliographic References',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReferenceAnalytic',
            fields=[
                ('reference_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='biblioref.Reference', on_delete=models.PROTECT)),
                ('individual_author', utils.fields.JSONField(null=True, verbose_name='Individual author', blank=True)),
                ('corporate_author', utils.fields.JSONField(null=True, verbose_name='Corporate author', blank=True)),
                ('title', utils.fields.JSONField(null=True, verbose_name='Title', blank=True)),
                ('english_translated_title', models.CharField(max_length=400, verbose_name='English translated title', blank=True)),
                ('pages', models.CharField(max_length=80, verbose_name='Pages', blank=True)),
                ('clinical_trial_registry_name', models.TextField(verbose_name='Clinical trial registry name', blank=True)),
            ],
            options={
                'verbose_name': 'Bibliographic Reference Analytic',
                'verbose_name_plural': 'Bibliographic References Analytic',
            },
            bases=('biblioref.reference',),
        ),
        migrations.CreateModel(
            name='ReferenceComplement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('conference_sponsoring_institution', models.TextField(verbose_name='Conference Sponsoring Institution', blank=True)),
                ('conference_name', models.TextField(verbose_name='Conference name', blank=True)),
                ('conference_date', models.CharField(max_length=100, verbose_name='Conference date', blank=True)),
                ('conference_normalized_date', models.CharField(max_length=100, verbose_name='Conference normalized date', blank=True)),
                ('conference_city', models.CharField(max_length=100, verbose_name='Conference city', blank=True)),
                ('project_sponsoring_institution', models.TextField(verbose_name='Project - Sponsoring Institution', blank=True)),
                ('project_name', models.CharField(max_length=500, verbose_name='Project name', blank=True)),
            ],
            options={
                'verbose_name': 'Bibliographic Reference Analytic',
                'verbose_name_plural': 'Bibliographic References Analytic',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReferenceSource',
            fields=[
                ('reference_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='biblioref.Reference', on_delete=models.PROTECT)),
                ('inventory_number', models.TextField(verbose_name='Inventory number', blank=True)),
                ('individual_author_monographic', utils.fields.JSONField(null=True, verbose_name='Individual author', blank=True)),
                ('corporate_author_monographic', utils.fields.JSONField(null=True, verbose_name='Corporate author', blank=True)),
                ('title_monographic', models.CharField(max_length=250, verbose_name='Title', blank=True)),
                ('english_title_monographic', models.CharField(max_length=250, verbose_name='English translated title', blank=True)),
                ('pages_monographic', models.CharField(max_length=80, verbose_name='Pages', blank=True)),
                ('volume_monographic', models.CharField(max_length=100, verbose_name='Volume', blank=True)),
                ('individual_author_collection', utils.fields.JSONField(null=True, verbose_name='Individual author', blank=True)),
                ('corporate_author_collection', utils.fields.JSONField(null=True, verbose_name='Corporate author', blank=True)),
                ('title_collection', models.CharField(max_length=250, verbose_name='Title', blank=True)),
                ('english_title_collection', models.CharField(max_length=250, verbose_name='English translated title', blank=True)),
                ('total_number_of_volumes', models.CharField(max_length=10, verbose_name='Total number of volumes', blank=True)),
                ('title_serial', models.CharField(max_length=250, verbose_name='Journal title', blank=True)),
                ('volume_serial', models.CharField(max_length=100, verbose_name='Volume', blank=True)),
                ('issue_number', models.CharField(max_length=80, verbose_name='Issue number', blank=True)),
                ('issn', models.CharField(max_length=40, verbose_name='ISSN', blank=True)),
                ('thesis_dissertation_leader', utils.fields.JSONField(null=True, verbose_name='Thesis, Dissertation - Leader', blank=True)),
                ('thesis_dissertation_institution', models.CharField(max_length=300, verbose_name='Thesis, Dissertation - Institution', blank=True)),
                ('thesis_dissertation_academic_title', models.CharField(max_length=250, verbose_name='Thesis, Dissertation - Academic title', blank=True)),
                ('publisher', models.TextField(verbose_name='Publisher', blank=True)),
                ('edition', models.CharField(max_length=150, verbose_name='Edition', blank=True)),
                ('publication_city', models.CharField(max_length=100, verbose_name='City of publication', blank=True)),
                ('symbol', models.TextField(verbose_name='Symbol', blank=True)),
                ('isbn', models.CharField(max_length=60, verbose_name='ISBN', blank=True)),
                ('doi_number', models.CharField(max_length=150, verbose_name='DOI number', blank=True)),
            ],
            options={
                'verbose_name': 'Bibliographic Reference Source',
                'verbose_name_plural': 'Bibliographic References Source',
            },
            bases=('biblioref.reference',),
        ),
        migrations.AddField(
            model_name='referencecomplement',
            name='source',
            field=models.ForeignKey(verbose_name='Source', to='biblioref.Reference', on_delete=models.PROTECT),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='referenceanalytic',
            name='source',
            field=models.ForeignKey(verbose_name='Source', to='biblioref.ReferenceSource', on_delete=models.PROTECT),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reference',
            name='created_by',
            field=models.ForeignKey(related_name='+', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True, on_delete=models.PROTECT),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reference',
            name='updated_by',
            field=models.ForeignKey(related_name='+', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True, on_delete=models.PROTECT),
            preserve_default=True,
        ),
    ]
