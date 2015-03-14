from __future__ import absolute_import

import django.template
import django.template.base
from django.utils.six.moves.urllib import parse
import hashlib

from .base import BaseTemplateNode, Tag

# pylint: disable=invalid-name
register = django.template.Library()
# pylint: enable=invalid-name

@Tag(register, 'gravatar')
class GravatarNode(BaseTemplateNode):
	def __init__(self, args, kwargs):
		self.user = args[0] if len(args) >= 1 else kwargs.get('user', None)
		self.size = args[1] if len(args) >= 2 else kwargs.get('size', 40)

	def render(self, context):
		if not self.user:
			request = context.request
			if not request.user.is_authenticated():
				raise django.template.VariableDoesNotExist(
					'Could not get Gravatar. No use was specified and no one is logged in'
				)

			user = request.user
		else:
			user = context[self.user] if self.user in context else self.user

		url = 'https://www.gravatar.com/avatar/{}?{}'.format(
			hashlib.md5(user.email.lower().encode('utf-8')).hexdigest(),
			parse.urlencode(
				{
					's': str(self.size),
				}
			),
		)

		return '<img src="{}" alt="{}" class="gravatar" />'.format(url, user.username)

	@classmethod
	def handle_token(cls, parser, token):
		bits = token.split_contents()

		args   = []
		kwargs = {}

		tag  = bits[0]
		bits = bits[1:]

		for bit in bits:
			match = django.template.base.kwarg_re.match(bit)
			if not match:
				raise django.template.TemplateSyntaxError('Malformed arguments to {} tag'.format(tag))

			name, value = match.groups()
			if name:
				kwargs[name] = parser.compile_filter(value)
			else:
				args.append(bit)

		return cls(args, kwargs)

