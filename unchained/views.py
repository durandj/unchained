import django.shortcuts
from django.conf import settings
import django.contrib.auth
import django.contrib.auth.forms
import django.core.exceptions
import django.core.urlresolvers
import django.utils.http
import django.views.generic

# pylint: disable=too-many-ancestors

class ViewDecoratorMixin(object):
	decorators = []

	@classmethod
	def as_view(cls, **initkwargs):
		view = super(ViewDecoratorMixin, cls).as_view(**initkwargs)

		for decorator in cls.get_decorators():
			view = decorator(view)

		return view

	@classmethod
	def get_decorators(cls):
		if not cls.decorators:
			raise django.core.exceptions.ImproperlyConfigured(
				"ViewDecoratorMixin requires you to either set the 'decorators'"
				" class attribute or override the 'get_decorators' method."
			)

		return cls.decorators

class LoginView(django.views.generic.FormView):
	form_class          = django.contrib.auth.forms.AuthenticationForm
	redirect_field_name = 'next'

	def get_context_data(self, **kwargs):
		context = super(LoginView, self).get_context_data(**kwargs)

		context[self.redirect_field_name] = self.request.GET[self.redirect_field_name]

		return context

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			return django.shortcuts.redirect(self.get_success_url())

		return super(LoginView, self).get(request, *args, **kwargs)

	def get_success_url(self):
		request_params = self.request.POST

		default = settings.LOGIN_REDIRECT_URL

		if self.redirect_field_name in request_params:
			url = request_params[self.redirect_field_name]

			if not django.utils.http.is_safe_url(url, host = self.request.get_host()):
				url = default
		else:
			url = default

		return django.shortcuts.resolve_url(url)

	def form_valid(self, form):
		django.contrib.auth.login(self.request, form.get_user())

		return super(LoginView, self).form_valid(form)

class LogoutView(django.views.generic.TemplateView):
	default_redirect    = None
	redirect_field_name = 'prev'

	def get_context_data(self, **kwargs):
		context = super(LogoutView, self).get_context_data(**kwargs)

		context[self.redirect_field_name] = self.request.GET.get(
			self.redirect_field_name,
			django.core.urlresolvers.reverse(
				self.get_default_redirect()
			)
		)

		return context

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return django.shortcuts.redirect(self.get_success_url())

		return super(LogoutView, self).get(request, *args, **kwargs)

	def post(self, request):
		django.contrib.auth.logout(request)

		return django.shortcuts.redirect(self.get_success_url())

	def get_default_redirect(self):
		if not self.default_redirect:
			raise django.core.exceptions.ImproperlyConfigured(
				"LogoutView requires either the 'default_redirect' attribute "
				"be set or the 'get_default_redirect' method be overriden"
			)

		return self.default_redirect

	def get_success_url(self):
		request_params = self.request.POST

		default = self.get_default_redirect()

		if self.redirect_field_name in request_params:
			url = request_params[self.redirect_field_name]

			if not django.utils.http.is_safe_url(url, host = self.request.get_host()):
				url = default
		else:
			url = default

		return django.shortcuts.resolve_url(url)

