from __future__ import absolute_import

import django.template
import django.templatetags.static
from django.utils.six.moves.urllib import parse

from .base import BaseTemplateNode, Tag

# pylint: disable=invalid-name
register = django.template.Library()
# pylint: enable=invalid-name

class StaticContentMixin(object):
	def __init__(self, path):
		self.path = path

	def url(self, context):
		path = self.path.resolve(context)

		return self.handle_simple(path)

	@staticmethod
	def handle_simple(path):
		return parse.urljoin(
			django.templatetags.static.PrefixNode.handle_simple('STATIC_URL'),
			path
		)

@Tag(register, 'stylesheet')
class StylesheetNode(BaseTemplateNode, StaticContentMixin):
	def render(self, context):
		url = self.url(context)

		return '<link rel="stylesheet" href="{}" />'.format(url)

	@classmethod
	def handle_token(cls, parser, token):
		args = token.split_contents()

		if len(args) < 2:
			raise django.template.TemplateSyntaxError(
				"'{}' takes at least one parameter for the stylesheet path".format(args[0])
			)

		path = parser.compile_filter(args[1])

		return cls(path)

@Tag(register, 'script')
class ScriptNode(BaseTemplateNode, StaticContentMixin):
	def render(self, context):
		url = self.url(context)

		return '<script src="{}"></script>'.format(url)

	@classmethod
	def handle_token(cls, parser, token):
		args = token.split_contents()

		if len(args) < 2:
			raise django.template.TemplateSyntaxError(
				"'{}' takes at least one argument for the script path".format(args[0])
			)

		path = parser.compile_filter(args[1])

		return cls(path)

