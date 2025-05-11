# Django Template Inheritance

## 1. Core Inheritance Concepts

### Base Template Structure (`base.html`)
```django
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Default Title{% endblock %}</title>
    {% block head_styles %}{% endblock %}
    {% block head_scripts %}{% endblock %}
</head>
<body>
    {% block header %}
        <header>Default Header</header>
    {% endblock %}
    
    {% block content_wrapper %}
        <main class="container">
            {% block content %}{% endblock %}
        </main>
    {% endblock %}
    
    {% block footer %}
        <footer>Default Footer</footer>
    {% endblock %}
    
    {% block body_scripts %}{% endblock %}
</body>
</html>
```

### Key Principles
1. **DRY (Don't Repeat Yourself)**: Define common elements once
2. **Block Nesting**: Blocks can contain other blocks
3. **Template Hierarchy**: Multiple levels of inheritance
4. **Block Overriding**: Child templates replace parent blocks

## 2. Implementation Patterns

### Three-Level Inheritance
1. **Level 1**: `base.html` (site-wide structure)
2. **Level 2**: `section_base.html` (section-specific layout)
3. **Level 3**: `page.html` (individual page content)

### Example Structure
```
templates/
  base/
    base.html          # Master template
    admin_base.html    # Admin section base
    auth_base.html     # Auth section base
  sections/
    blog_base.html     # Blog section template
    shop_base.html     # E-commerce section
  pages/
    blog/
      post_detail.html
      post_list.html
    shop/
      product_detail.html
```

## 3. Advanced Inheritance Techniques

### Block Composition
```django
{% block javascript %}
  {{ block.super }}  {# Preserves parent content #}
  <script src="{% static 'js/custom.js' %}"></script>
{% endblock %}
```

### Conditional Inheritance
```django
{% extends use_alternate_layout|yesno:"layouts/alt_base.html,base.html" %}
```

### Dynamic Block Names
```django
{% block "dynamic_{% if mobile %}mobile{% else %}desktop{% endif %}" %}
  Content
{% endblock %}
```

## 4. Best Practices

### Organization
1. **Namespace Templates**: `app/templates/app/` structure
2. **Logical Grouping**: Group related templates together
3. **Clear Naming**: `_` prefix for partials (e.g., `_navbar.html`)

### Performance
1. **Limit Nesting**: 3-4 levels maximum
2. **Use `{% include %}`** for reusable components
3. **Cache Blocks** when appropriate

### Maintenance
1. **Document Blocks**: Comment block purposes
2. **Consistent Structure**: Standardize block names
3. **Version Control**: Track template changes

## 5. Common Patterns

### Dashboard Layout
```django
{% extends "base.html" %}

{% block content_wrapper %}
  <div class="dashboard">
    <aside class="sidebar">{% block sidebar %}{% endblock %}</aside>
    <main class="main-content">{% block main_content %}{% endblock %}</main>
  </div>
{% endblock %}
```

### Error Page Customization
```django
{% extends "base.html" %}

{% block content %}
  <div class="error-container">
    {% block error_content %}
      <h1>{% block error_title %}Error{% endblock %}</h1>
      {% block error_details %}{% endblock %}
    {% endblock %}
  </div>
{% endblock %}
```

## 6. Troubleshooting

### Common Issues
1. **Missing Blocks**: Forgetting required blocks
2. **Circular Extends**: A extends B extends A
3. **Block Overrides**: Accidentally overriding critical blocks
4. **Context Problems**: Missing parent template variables

### Debugging Techniques
1. **Template Debugging**:
   ```django
   {% debug %}  {# Shows available context #}
   ```
2. **Inheritance Visualization**:
   ```bash
   python manage.py find_template <template_name>
   ```
3. **Block Inspection**:
   ```django
   {% block %}...{% endblock %} comments
   ```
