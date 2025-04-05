import os
import re
from django import template
from django.templatetags.static import static
from django.conf import settings

register = template.Library()

@register.simple_tag
def latest_svelte_asset(ext):
    asset_dir = os.path.join(settings.BASE_DIR, 'static', 'frontend', 'assets')
    files = os.listdir(asset_dir)
    # Updated regex to match files starting with "main"
    pattern = re.compile(rf'^main[-.].+\.{ext}$')
    for file in files:
        if pattern.match(file):
            return static(f'frontend/assets/{file}')
    return ''
