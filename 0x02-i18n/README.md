# i18n

## Definition

Internationalization (i18n) is a process of designing and preparing software so that it can be easily translated and localized for different languages and regions. The term "i18n" is a shorthand for "internationalization" where "18" refers to the number of letters between "i" and "n."
Localization (l10n) is the process of adapting the internationalized software for a specific region or language by adding locale-specific components and translating text.

---

- Key Components

1. Content Translation:
   This involves translating all visible content, such as text, images, and multimedia elements, into different languages.

2. Date and Time Formats
   Adapt date and time formats based on the user's locale.

3. Number Formats
   Display numbers and currency in formats appropriate for the user's region.

4. User Interface (UI)
   Design UI elements in a way that accommodates different text lengths and structures in various languages.

5. Pluralization
   Different languages have different rules for pluralization. Ensure that your application can handle these variations.

6. Character Encodings
   Support Unicode and ensure that your application can handle characters from different languages

## Tools and Libraries

- **GNU gettext**
- **Flask-Babel**
- **React-Intl**
- **Vue I18n**

### Resources

- [Flask-Babel](https://python-babel.github.io/flask-babel/)
- [Flask i18n tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
- [pytz](https://sourceforge.net/directory/software-development/linux/)

### Learning Objectives

```
    Learn how to parametrize Flask templates to display different languages
    Learn how to infer the correct locale based on URL parameters, user settings or request headers
    Learn how to localize timestamps
```

### Requirements

```
    All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
    All your files should end with a new line
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the pycodestyle style (version 2.5)
    The first line of all your files should be exactly #!/usr/bin/env python3
    All your *.py files should be executable
    All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    All your functions and methods should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
    All your functions and coroutines must be type-annotated.
```

### Project Tasks

0. Basic Flask app
   First you will setup a basic Flask app in `0-app.py`. Create a single `/` route and an `index.html` template that simply outputs “Welcome to Holberton” as page title (<title>) and “Hello world” as header (<h1>).

1. Basic Babel setup
   Then instantiate the `Babel` object in your app. Store it in a module-level variable named `babel`.
   In order to configure available languages in our app, you will create a `Config` class that has a `LANGUAGES` class attribute equal to `["en", "fr"]`
   Use `Config` to set Babel’s default locale `("en")` and timezone`("UTC")`
   Use that class as config for your Flask app

2. Get locale from request
   Create `a get_locale` function with the `babel.localeselector` decorator. Use `request.accept_languages` to determine the best match with our supported languages.

3. Parametrize templates
   Use the `_` or `gettext` function to parametrize your templates. Use the message IDs `home_title` and `home_header`.Create a `babel.cfg` file containing

```
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
```

Then initialize your translations with

```
$ pybabel extract -F babel.cfg -o messages.pot .
```

and your two dictionaries with

```
$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr
```

Then edit files `translations/[en|fr]/LC_MESSAGES/messages.po` to provide the correct value for each message ID for each language. Use the following translations:

| msgid       | English                | French                     |
| ----------- | ---------------------- | -------------------------- |
| home_title  | "Welcome to Holberton" | "Bienvenue chez Holberton" |
| home_header | "Hello world!"         | "Bonjour monde!"           |

4. Force locale with URL parameter
