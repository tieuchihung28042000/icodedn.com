from textwrap import dedent

from django import forms
from django.conf import settings
from django.template import Context, Template
from lxml import html

# Đã loại bỏ compressor, không cần CompressorWidgetMixin nữa
