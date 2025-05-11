# Django Template Tags

## 1. Tag Basics

### Syntax
```django
{% tag_name argument %}
```

### Key Characteristics
- Perform logic rather than display values
- Can create blocks ({% tag %}...{% endtag %})
- Over 25 built-in tags available
- Extensible through custom tags

## 2. Essential Control Tags

### Conditional Logic
```django
{% if user.is_authenticated %}
  Welcome back!
{% elif user.is_anonymous %}
  Please log in
{% else %}
  Error state
{% endif %}
```

### Looping
```django
{% for item in items %}
  <p>{{ forloop.counter }}. {{ item.name }}</p>
{% empty %}
  <p>No items available</p>
{% endfor %}
```

### Special Loop Variables
- `forloop.counter` (1-based index)
- `forloop.counter0` (0-based index)
- `forloop.revcounter` (reverse count)
- `forloop.first`/`forloop.last` (boolean)

## 3. Template Structure Tags

### Inheritance
```django
{% extends "base.html" %}

{% block content %}
  Main page content
{% endblock %}
```

### Includes
```django
{% include "header.html" %}
{% include "footer.html" with year=2023 only %}
```

### Block Composition
```django
{% block title %}
  {{ block.super }} - Subpage
{% endblock %}
```

## 4. URL Handling Tags

### Basic URL
```django
<a href="{% url 'view_name' %}">Link</a>
```

### With Arguments
```django
{% url 'product_detail' product.id %}
```

### Namespaced URLs
```django
{% url 'shop:product_view' category='electronics' %}
```

## 5. Special Purpose Tags

### CSRF Protection
```django
<form>
  {% csrf_token %}
</form>
```

### Comments
```django
{# Single-line comment #}

{% comment "Optional note" %}
  Multi-line
  comment block
{% endcomment %}
```

### Debugging
```django
{% debug %}  {# Shows complete context #}
```

## 6. Custom Template Tags

### 1. Create `templatetags/custom_tags.py`
```python
from django import template

register = template.Library()

@register.simple_tag
def current_time(format_string):
    from datetime import datetime
    return datetime.now().strftime(format_string)

@register.inclusion_tag('results.html')
def show_results(poll):
    return {'choices': poll.choice_set.all()}
```

### 2. Usage in Templates
```django
{% load custom_tags %}

{% current_time "%Y-%m-%d" %}
{% show_results poll %}
```

## 7. Advanced Tag Techniques

### Assignment Tags (Django < 2.0)
```python
@register.assignment_tag
def get_site_settings():
    return SiteSettings.objects.first()
```

### Block Composition
```django
{% block javascript %}
  {{ block.super }}
  <script>/* Additional JS */</script>
{% endblock %}
```

### Dynamic Includes
```django
{% include template_name %}
```

## 8. Security Considerations

### Safe HTML
```django
{% autoescape on %}
  {{ untrusted_content }}
{% endautoescape %}
```

### URL Validation
```django
{# Always use url tag instead of hardcoded paths #}
{% url 'safe_view' %}
```

## 9. Performance Tips

1. Use `{% with %}` for expensive lookups:
```django
{% with total=items|length %}
  {{ total }} items
{% endwith %}
```

2. Limit database access in tags
3. Cache template fragments:
```django
{% load cache %}
{% cache 300 sidebar %}
  ... expensive rendering ...
{% endcache %}
```

## 10. Debugging Template Tags

### Common Issues
1. **Missing Load Tag**: Forgot `{% load custom_tags %}`
2. **Syntax Errors**: Improper tag nesting
3. **Context Issues**: Missing required variables
4. **Circular Extends**: Infinite template inheritance

### Debugging Techniques
1. Check `django.template` logger
2. Use `{% debug %}` to inspect context
3. Verify template loaders in settings
