# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['django_filter_drf_camel_case', 'django_filter_drf_camel_case.spectacular']

package_data = \
{'': ['*']}

install_requires = \
['django-filter>=2.0,<23.0',
 'djangorestframework-camel-case>=1.0,<2.0',
 'djangorestframework>=3.0,<4.0',
 'drf-spectacular[drf-spectactular]>=0.24.0,<0.25.0']

setup_kwargs = {
    'name': 'django-filter-drf-camel-case',
    'version': '0.1.0',
    'description': 'A collection of utility classes that make using camel cased query parameters easier with Django REST Framework and django-filter',
    'long_description': '# Django-Filter DRF Camel Case Helpers\n\n![Tests](https://github.com/camuthig/django-filter-drf-camel-case/actions/workflows/ci.yml/badge.svg)\n[![codecov](https://codecov.io/gh/camuthig/django-filter-drf-camel-case/branch/main/graph/badge.svg?token=GAGIIZXC95)](https://codecov.io/gh/camuthig/django-filter-drf-camel-case)\n[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)\n[![Source Code](https://img.shields.io/badge/Source-code-blue)](https://github.com/camuthig/django-filter-drf-camel-case)\n\nA collection of utility classes that make using camel cased query parameters easier with [Django REST\nFramework](https://www.django-rest-framework.org/) and [django-filter](https://django-filter.readthedocs.io/en/latest/index.html).\nFilter set query parameters can be written using conventional snake cased naming in Python code, but will be treated as\ncamel case in the API. Additionally, schemas generated using [DRF Spectacular](https://drf-spectacular.readthedocs.io/en/latest/index.html)\nwill use the correct camel case notation.\n\n# Usage\n\nTo get the full benefit of this package, just swap out the normal `DjangoFilterBackend` and `OrderingFilter` classes\nprovided by the `django_filter` package with those implemented in `django_filter_drf_camel_case`.\n\n```python\nfrom django.db import models\nfrom django_filters.rest_framework import filters\nfrom django_filters.rest_framework import filterset\nfrom rest_framework.viewsets import ModelViewSet\n\nfrom django_filter_drf_camel_case import OrderingFilter\nfrom django_filter_drf_camel_case import DjangoFilterBackend\n\nclass Post(models.Model):\n    title = models.CharField(max_length=255)\n    created_at = models.DateTimeField(auto_add_now=True)\n    follow_up = models.ForeignKey("Post", null=True, on_delete=models.SET_NULL)\n\n\nclass PostFilters(filterset.FilterSet):\n    created_at = filters.IsoDateTimeFromToRangeFilter()\n    sort = OrderingFilter(fields=("created_at", "title", "follow_up__title"))\n\n    class Meta:\n        model = Post\n        fields = {\n            "title": {"exact", "contains"},\n            "follow_up__title": {"exact"},\n        }\n\nclass PostViewSet(ModelViewSet):\n    queryset = Post.objects.all()\n    filter_backends = [DjangoFilterBackend]\n    filterset_class = PostFilters\n```\n\nThe supported query parameters will be:\n* `title`\n* `createdAt`\n* `createdAt__lt`\n* `author__fullName`\n\nThe sort keys are:\n* `createdAt`/`-createdAt`\n* `title`/`-title`\n* `followUp__title`/`-followUp__title`\n\n# Underscore vs Dunderscore\n\nTo avoid ambiguous query parameters based on lookup expressions, these utilities will respect the  default use of the\ndunderscore (`__`) pattern by django-filter to separate fields from lookup expressions and relationships.\n\nIf you want to avoid this dunderscore behavior, then the recommendation is to use explicit keys, using underscores\ninstead of dunderscores where you want. A possible alternative filterset would be\n\n```python\nfrom django.db import models\nfrom django_filters.rest_framework import filters\nfrom django_filters.rest_framework import filterset\nfrom django_filter_drf_camel_case import OrderingFilter\n\nclass Post(models.Model):\n    title = models.CharField(max_length=255)\n    created_at = models.DateTimeField(auto_add_now=True)\n    follow_up = models.ForeignKey("Post", null=True, on_delete=models.SET_NULL)\n\nclass PostFilters(filterset.FilterSet):\n    created_at = filters.IsoDateTimeFromToRangeFilter()\n    follow_up_title = filters.CharFilter(field_name="follow_up__title")\n    sort = OrderingFilter(fields={\n        "created_at": "createdAt",\n        "title": "title",\n        "follow_up__title": "followUpTitle",\n    })\n\n    class Meta:\n        model = Post\n        fields = ("title",)\n```\n\nResulting in the query parameters:\n* `title`\n* `createdAt`\n* `createdAtLt`\n* `followUpTitle`\n\nThe sort keys are:\n* `createdAt`/`-createdAt`\n* `title`/`-title`\n* `followUpTitle`/`-followUpTitle`\n',
    'author': 'Chris Muthig',
    'author_email': 'camuthig@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
