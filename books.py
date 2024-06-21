import jinja2

env = jinja2.Environment()
template_titles = env.from_string("""
My favorite books are:
{% for book in my_books -%}
- {{ book.title }}
{% endfor %}
""")

my_books = [
    {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960
    }
]

print(template_titles.render(my_books=my_books))
