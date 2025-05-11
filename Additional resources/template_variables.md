# Django Template Variables

## 1. Variable Basics

### Syntax
```django
{{ variable_name }}
```

### How Variables Work
- Resolved against the template context
- Output is automatically HTML-escaped
- Returns empty string if variable doesn't exist (unless strict mode)

## 2. Variable Types

### Common Variable Types
1. **Strings**: `{{ "Hello" }}` or `{{ string_var }}`
2. **Numbers**: `{{ 42 }}` or `{{ number_var }}`
3. **Booleans**: `{{ True }}` or `{{ boolean_var }}`
4. **Lists/Arrays**: `{{ list_var.0 }}` (access first element)
5. **Dictionaries**: `{{ dict_var.key }}`
6. **Objects**: `{{ object.attribute }}` or `{{ object.method }}`

### Example Context
```python
context = {
    'title': 'My Page',
    'visits': 42,
    'user': request.user,  # User object
    'items': ['Apple', 'Banana', 'Cherry'],
    'settings': {'color': 'blue', 'size': 'large'}
}
```

## 3. Variable Access Methods

### Dot Notation
```django
{{ object.attribute }}
{{ dictionary.key }}
{{ list.index }}
```

### Examples
```django
{{ user.first_name }}  # Object attribute
{{ settings.color }}   # Dictionary key
{{ items.1 }}         # List item (Banana)
```

### Special Cases
```django
{{ user.is_authenticated }}  # Boolean property
{{ user.get_full_name }}     # Method call (no parentheses)
```

## 4. Variable Resolution

### Lookup Order
1. Dictionary lookup (`var[key]`)
2. Attribute lookup (`obj.attr`)
3. List index lookup (`list[index]`)

### Complex Example
```django
{{ request.session.cart_items.0.product.name }}
```
This checks:
1. `request` (object)
2. `session` (attribute)
3. `cart_items` (dictionary key or attribute)
4. `0` (list index)
5. `product` (attribute)
6. `name` (attribute)

## 5. Built-in Variables

### Automatic Variables
- `{{ request }}`: Current HttpRequest object
- `{{ user }}`: Current logged in user (or AnonymousUser)
- `{{ perms }}`: Permission object

### Loop Variables (in {% for %})
- `{{ forloop.counter }}`: Current iteration (1-indexed)
- `{{ forloop.counter0 }}`: Current iteration (0-indexed)
- `{{ forloop.first }}`: True if first iteration
- `{{ forloop.last }}`: True if last iteration

## 6. Variable Filters

### Common Filters
```django
{{ name|lower }}          # Convert to lowercase
{{ value|default:"N/A" }} # Default value
{{ text|truncatechars:25 }} # Trim text
{{ list|join:", " }}      # Join list
{{ date|date:"Y-m-d" }}   # Format date
```

### Chaining Filters
```django
{{ title|lower|truncatechars:10 }}
```

## 7. Special Variable Cases

### Handling Missing Variables
By default, Django:
- Returns empty string for missing variables
- Can enable strict mode (raises exception) in settings:
```python
TEMPLATES = [{
    'OPTIONS': {
        'string_if_invalid': 'INVALID_EXPRESSION',  # or raise exception
    },
}]
```

### HTML Escaping
Automatic escaping:
```django
{{ unsafe_html }}  # Gets escaped
{{ safe_html|safe }}  # Marked as safe
```

## 8. Best Practices

1. **Keep Logic Minimal**: Move complex logic to views/models
2. **Use Meaningful Names**: `{{ product.price }}` not `{{ p.p }}`
3. **Handle Missing Data**: Use default filter or template conditions
4. **Performance**: Avoid expensive method calls in templates
5. **Security**: Never mark untrusted content as safe

## 9. Debugging Variables

### Techniques
1. Use `{% debug %}` tag to see all available variables
2. Check view context in debug mode
3. Temporary display: `{{ variable|pprint }}`
4. Check for typos in variable names

### Example Debug Output
```django
{% debug %}
```
Shows complete context including:
- All passed variables
- Built-in variables
- Available filters/tags
