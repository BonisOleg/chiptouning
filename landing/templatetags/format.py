import re

from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()

_PHONE_RE = re.compile(r'(\+?\d[\d\s\-()]{7,17}\d)')
_DIGITS_RE = re.compile(r'[^\d+]')


def _normalise_phone(raw: str) -> str:
    """Return a tel: href-safe phone string (digits only, leading + preserved)."""
    stripped = _DIGITS_RE.sub('', raw)
    if raw.lstrip().startswith('+') and not stripped.startswith('+'):
        stripped = '+' + stripped
    return stripped


@register.filter(name='tellinks', is_safe=True)
def tellinks(value: str) -> str:
    """Wrap phone-like sequences in <a href="tel:..."> tags.

    The rest of the text is HTML-escaped before substitution so XSS is impossible.
    """
    escaped = escape(value)

    def _replace(m: re.Match) -> str:
        raw = m.group(1)
        href = _normalise_phone(raw)
        return f'<a href="tel:{href}" class="tel-link">{raw}</a>'

    return mark_safe(_PHONE_RE.sub(_replace, escaped))
