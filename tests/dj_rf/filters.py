from __future__ import unicode_literals

from dj_rql.filter_cls import RQLFilterClass
from dj_rql.constants import FilterLookups, RQL_NULL
from tests.dj_rf.models import Book


AUTHOR_FILTERS = ['is_male', {
    'filter': 'email',
    'ordering': True,
    'search': True,
}, {
    'namespace': 'publisher',
    'filters': ['id']
}]


PAGE_FILTERS = [{
    'filter': 'number',
    'lookups': {FilterLookups.EQ, FilterLookups.NE},
}, {
    'filter': 'id',
    'source': 'uuid',
}]


class BooksFilterClass(RQLFilterClass):
    MODEL = Book
    FILTERS = ['id', {
        'filter': 'title',
        'null_values': {RQL_NULL, 'NULL_ID'},
        'search': True,
    }, 'current_price', 'written', {
        'filter': 'status',
    }, {
        'filter': 'author__email',
        'search': True,
    }, {
        'filter': 'name',
        'source': 'author__name',
    }, {
        'namespace': 'author',
        'filters': AUTHOR_FILTERS,
    }, {
        'namespace': 'page',
        'source': 'pages',
        'filters': PAGE_FILTERS,
    }, {
        'filter': 'published.at',
        'source': 'published_at',
        'ordering': True,
    }, {
        'filter': 'rating.blog',
        'source': 'blog_rating',
        'use_repr': True,
    }, {
        'filter': 'rating.blog_int',
        'source': 'blog_rating',
        'use_repr': False,
    }, {
        'filter': 'amazon_rating',
        'lookups': {FilterLookups.GE, FilterLookups.LT},
        'null_values': {'random'},
    }, {
        'filter': 'url',
        'source': 'publishing_url',
    }, {
        'filter': 'd_id',
        'sources': ['id', 'author__id'],
        'ordering': True,
    }, {
        'filter': 'custom_filter',
        'custom': True,
        'lookups': {FilterLookups.I_LIKE},

        'custom_data': [1],
    }, {
        'filter': 'int_choice_field',
        'ordering': True,
    }, {
        'filter': 'int_choice_field_repr',
        'source': 'int_choice_field',
        'use_repr': True,
        'lookups': {FilterLookups.EQ, FilterLookups.NE},
    }, {
        'filter': 'str_choice_field',
        'search': True,
    }, {
        'filter': 'str_choice_field_repr',
        'source': 'str_choice_field',
        'use_repr': True,
        'lookups': {FilterLookups.EQ, FilterLookups.NE},
    }, {
        'filter': 'has_list_lookup',
        'custom': True,
        'lookups': {FilterLookups.EQ, FilterLookups.NE, FilterLookups.IN, FilterLookups.OUT},
    }, {
        'filter': 'no_list_lookup',
        'custom': True,
        'lookups': {FilterLookups.EQ},
    }, {
        'filter': 't__in',
        'source': 'title',
    }, 'github_stars', {
        'filter': 'ordering_filter',
        'custom': True,
        'ordering': True,
    }, {
        'filter': 'fsm',
        'source': 'fsm_field',
        'ordering': True,
        'search': True,
    }]
