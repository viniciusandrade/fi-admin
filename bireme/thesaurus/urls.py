#! coding: utf-8
from django.conf.urls import patterns, include, url

from views import *

urlpatterns = [

    # Descriptors -------------------------------------------------------------------------------------------
    url(r'^descriptors/?$', DescListView.as_view(), name='list_descriptor'),

    # Form 1 para criacao de novo registro
    url(r'^descriptors/new/?$', DescCreateView.as_view(), name='create_descriptor'),

    # Form 2 para criacao de novo registro
    url(r'^descriptors/register/term/?$', DescCreateView2.as_view(), name='create_concept_termdesc'),

    # Delecao caso seja cancelado a inclusao de novo registro, a partir do Form2
    url(r'^descriptors/delete/(?P<pk>\d+)/?$', DescDeleteView.as_view(), name='delete_descriptor'),

    # PageViewDesc - lista registro - Abas Details e Concepts
    url(r'^descriptors/view/(?P<pk>[\w-]+)$', PageViewDesc.as_view(), name='detail_descriptor'),

    # Edit Register 
    url(r'^descriptors/register/edit/(?P<pk>\d+)/?$', DescRegisterUpdateView.as_view(), name='edit_register_desc'),

    # Cria conceito + Termo
    url(r'^descriptors/concept/new/?$', ConceptListDescCreateView.as_view(), name='create_concept_desc'),
    url(r'^descriptors/concept/edit/(?P<pk>\d+)/?$', ConceptListDescUpdateView.as_view(), name='edit_concept_desc'),

    # Cria Termo
    url(r'^descriptors/term/new/?$', TermListDescCreateView.as_view(), name='create_term_desc'),
    url(r'^descriptors/term/edit/(?P<pk>\d+)/?$', TermListDescUpdateView.as_view(), name='edit_term_desc'),


    # Nao esta sendo utilizado por enquanto
    # Lista conceitos
    url(r'^descriptors/concept/?$', ConceptListDescView.as_view(), name='list_concept'),



    # Qualifiers --------------------------------------------------------------------------------------------
    url(r'^qualifiers/?$', QualifListView.as_view(), name='list_qualifier'),

    # Form 1 para criacao de novo registro
    url(r'^qualifiers/new/?$', QualifCreateView.as_view(), name='create_qualifier'),

    # Form 2 para criacao de novo registro
    url(r'^qualifiers/register/term/?$', QualifCreateView2.as_view(), name='create_concept_termqualif'),

    # Delecao caso seja cancelado a inclusao de novo registro, a partir do Form2
    url(r'^qualifiers/delete/(?P<pk>\d+)/?$', QualifDeleteView.as_view(), name='delete_qualifier'),

    # PageViewQualif - lista registro - Abas Details e Concepts
    url(r'^qualifiers/view/(?P<pk>[\w-]+)$', PageViewQualif.as_view(), name='detail_qualifier'),

    # Edit Register 
    url(r'^qualifiers/register/edit/(?P<pk>\d+)/?$', QualifRegisterUpdateView.as_view(), name='edit_register_qualif'),

    # Cria conceito + Termo
    url(r'^qualifiers/concept/new/?$', ConceptListQualifCreateView.as_view(), name='create_concept_qualif'),
    url(r'^qualifiers/concept/edit/(?P<pk>\d+)/?$', ConceptListQualifUpdateView.as_view(), name='edit_concept_qualif'),

    # Cria Termo
    url(r'^qualifiers/term/new/?$', TermListQualifCreateView.as_view(), name='create_term_qualif'),
    url(r'^qualifiers/term/edit/(?P<pk>\d+)/?$', TermListQualifUpdateView.as_view(), name='edit_term_qualif'),

]
