# Django Unchained

A set of tools for working with Django and getting moving faster. Note that this is a work in progress.

## Table of Contents

* [Installation](#Installation)
* [Usage](#Usage)
  * [Templates](#Templates)

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

#### Gravatar

#### HTML

### Views

#### ViewDecoratorMixin

#### LoginView

#### LogoutView

###### Notes

About the name, I had to.

