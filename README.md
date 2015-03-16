# Django Unchained

A set of tools for working with Django and getting moving faster. Note that this is a work in progress.

## Table of Contents

* [Installation](#installation)
* [Usage](#usage)
  * [Templates](#templates)
    * [html5](#html5)
  * [Template Tags](#template-tags)
    * [Bootstrap](#bootstrap)
      * [glyphicon](#glyphicon)
	* [Gravatar](#gravatar)
      * [gravatar](#gravatar)
	* [HTML](#html)
      * [stylesheet](#stylesheet)
      * [script](#script)
  * [Views](#views)
    * [ViewDecoratorMixin](#viewdecoratormixin)
    * [LoginView](#loginview)
    * [LogoutView](#logoutview)
* [Notes](#notes)

## Installation

Installation is easy. You need to install with `pip` first.

	pip install unchained

Then just add unchained to your apps list.

	INSTALLED_APPS = (
		# snip...
		'unchained',
	)

## Usage

There are a lot of tools baked in.

### Templates

Some standard templates are provided so that you don't have to rewrite the same thing everytime.

#### html5

This template provides the basis for an HTML5 compliant page. Usage is simple:

	{% extends 'unchained/html5.html' %}

	{% block page %}
		<h1>Hello, World!</h1>
	{% endblock %}

### Template Tags

We also include some simple template tags.

#### Bootstrap

The Bootstrap tag library aims to make usage of the [Bootstrap](http://getbootstrap.com/) framework. It should be noted that this is targeting Bootstrap 3.3.2+. To include
the template library in your template just add the following line:

	{% load bootstrap %}

Documentation on using the tags is given below.

##### glyphicon

Glyphicon are useful icons from Bootstrap and while they aren't particularly difficult to use sometimes its annoying to have to type `<span class="glyphicon glyphicon-log-in"></span>` everywhere.
To that end we include the `glyphicon` tag. Usage is simple, find the name for the glyphicon you want to use (such as log-in) and include it in the tag like so:

	{% glyphicon 'log-in' %}

The quotes ARE required or it won't work properly.

#### Gravatar

The gravatar library includes a way to load up Gravatar images for users. For now it assumes that you're using it for a user in your system and that that user has an email
set in the database.

##### gravatar

There are a few options for the gravatar tag. First and foremost is the user object. This is optional to an extent. If you don't specify it then it uses the logged in user.
If no user is logged in an error is thrown. You can also specify what image size you want in pixels but if you don't specify this it defaults to 40 pixels. There are two
ways to specify both of these parameters.

Method 1:

	{% gravatar user 90 %}

Method 2:

	{% gravatar user=user size=90 %}

#### HTML

It's important to know how to write proper HTML but sometimes its just a waste of time to write the same thing 101 times.

To include these tags in your template just do this:

	{% load html %}

##### stylesheet

The stylesheet does what it sounds like, generate a link tag pointing to the given stylesheet. So instead of typing

	<link rel="stylesheet" href="{% static 'mystylesheet.css' %}" />

You can simply do

	{% stylesheet 'mystylesheet.css' %}

Note that this also works with a full URL like `http://example.com/mystylesheet.css`.

##### script

The script tag works just like the stylesheet tag except that, well, it generates a script tag. Usage is also the same.

	{% script 'myscript.js' %}

### Views

We also include some views and view mixins to make working with Django easier.

#### ViewDecoratorMixin

Try adding a decorator like the `login_required` mixin to a class based view. It gets hairy. This gets even hairier when you have inherited views adding their
own decorators. Why not just add them in one place. Note that this builds off of the example from the
[Django documentation](https://docs.djangoproject.com/en/1.7/topics/class-based-views/intro/#mixins-that-wrap-as-view).

	class LoginRequiredMixin(ViewDecoratorMixin):
		decorators = [login_required]

#### LoginView

A class based view version of Django's login system.

	class MyLoginView(LoginView):
		template_name = 'login.html'

#### LogoutView

A class based view version of Django's logout system.

	class MyLogoutView(LogoutView):
		template_name = 'logout.html'

## Notes

About the name, I had to.

