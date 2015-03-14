from __future__ import absolute_import

import django.template

from .base import BaseTemplateNode, Tag

# pylint: disable=invalid-name
register = django.template.Library()
# pylint: enable=invalid-name

@Tag(register, 'glyphicon')
class GlyphiconNode(BaseTemplateNode):
	def __init__(self, name):
		self.name = name

	def render(self, context):
		return '<span class="glyphicon glyphicon-{}"></span>'.format(self.name)

	# pylint: disable=unused-argument
	@classmethod
	def handle_token(cls, parser, token):
		args = token.split_contents()

		if len(args) < 2:
			raise django.template.TemplateSyntaxError(
				"'{}' requires at least one parameter for the icon name".format(args[0])
			)

		name = args[1].strip('\'\"')

		return cls(name)
	# pylint: disable=unused-argument

