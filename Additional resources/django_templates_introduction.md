# Django Templates: Introduction

## 1. Core Configuration

### Directory Structure
```
myproject/
├── manage.py
├── myapp/
│   ├── templates/          # App-specific templates
│   │   └── myapp/          # Namespaced template folder
│   │       └── index.html  
└── templates/              # Project-wide templates
    └── base/               
        └── base.html
```

### settings.py Setup
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Project-level templates
        'APP_DIRS': True,  # Enable app template discovery
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

## 2. Basic Structure
Django templates are HTML files with special syntax for dynamic content:
```html
<!-- Simple template example -->
<!DOCTYPE html>
<html>
<head>
    <title>My Page</title>
</head>
<body>
    <h1>Welcome to our site!</h1>
    <p>Current date: {% now "jS F Y" %}</p>
</body>
</html>
```

## 3. Template Organization
Best practices for file structure:
```
project/
  templates/
    base/          # Main templates
    components/    # Reusable UI pieces
    pages/         # Individual pages
```

## 4. Three Essential Components

#### A. Displaying Content
```html
<p>Hello, {{ user.first_name }}!</p>
```

#### B. Conditional Logic
```html
{% if user.is_authenticated %}
  <p>Welcome back!</p>
{% else %}
  <p>Please log in.</p>
{% endif %}
```

#### C. Looping Through Data
```html
<ul>
{% for product in products %}
  <li>{{ product.name }} - ${{ product.price }}</li>
{% endfor %}
</ul>
```

## 5. Template Reuse

#### Include (for partials)
```html
{% include "components/header.html" %}

<main>Page content here</main>

{% include "components/footer.html" %}
```

## 6. View Integration

### Basic View
```python
from django.shortcuts import render

def home_view(request):
    return render(request, 'myapp/home.html', {
        'title': 'Home Page',
        'user': request.user
    })
```

## 7. Best Practices

1. **Organization**:
   - Use `app/templates/app/` structure
   - Namespace template files
   - Group partials in `components/` directory

2. **Performance**:
   - Use `{% with %}` for expensive lookups
   - Limit database queries in templates
   - Consider template fragment caching

3. **Security**:
   - Always escape variables (`{{ var }}`)
   - Only use `|safe` when content is trusted
   - Sanitize user-generated content

4. **Debugging**:
   - Use `{% debug %}` tag during development
   - Check template loading order
   - Verify context variables

## 8. Practical Examples

### Pagination
```django
<div class="pagination">
    {% if page_obj.has_previous %}
        <a href="?page={{ page_obj.previous_page_number }}">Previous</a>
    {% endif %}
    <span>Page {{ page_obj.number }}</span>
    {% if page_obj.has_next %}
        <a href="?page={{ page_obj.next_page_number }}">Next</a>
    {% endif %}
</div>
```

### Form Rendering
```django
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```
