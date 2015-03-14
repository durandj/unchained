import abc
import django.template

# pylint: disable=too-few-public-methods

class BaseTemplateNode(django.template.Node):
	__metaclass__ = abc.ABCMeta

	@classmethod
	@abc.abstractclassmethod
	def handle_token(cls, parser, token):
		pass

class Tag(object):
	def __init__(self, library, name):
		self.library = library
		self.name    = name

	def __call__(self, node):
		def wrapper(parser, token):
			return node.handle_token(parser, token)

		self.library.tag(self.name)(wrapper)

		return node

