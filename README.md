# blogua

This project was generated with [Django](https://www.djangoproject.com) version 1.11.3 and [Python](https://www.python.org) version 3.6.1.

## Additional dependencies

  * [django-taggit](https://github.com/alex/django-taggit)
   
  django-taggit a simpler approach to tagging with Django. Add "taggit" to your INSTALLED_APPS then just add a TaggableManager to your model and go.
  * [tag-it](https://github.com/aehlke/tag-it)
  
  Tag-it is a simple and configurable tag editing widget with autocomplete support.

## Development server

Install django-taggit via pip(under virtualenv).
Run `python manage.py runserver`.
Run `python manage.py migrate`.
(Optional)Run `python manage.py manage.py loaddata fixtures/initial_data.json` for loading seeds.
Navigate to `http://localhost:8000`.
The app will automatically reload if you change any of the source files.

## Further help

To get more help on the Django project go check out the [Django Help](https://docs.djangoproject.com/en/1.11/faq/help/).