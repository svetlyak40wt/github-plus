import shelve
import urllib
import urllib2
import contextlib
import json

from django.contrib.auth.backends import ModelBackend, User
from django.conf import settings
from urlparse import urljoin


class GitHubOAuth(ModelBackend):
    def authenticate(self, token=None):
        with contextlib.closing(shelve.open('tokens.shelve')) as tokens:
            if token in tokens:
                return User.objects.get(id=tokens[token])
            else:
                response = urllib2.urlopen(
                    urljoin(
                        settings.GITHUB_API_URL,
                        '/user'
                    ) + '?' + urllib.urlencode(dict(
                        access_token=token,
                    )),
                    timeout=30,
                )
                response = json.load(response)
                user, created = User.objects.get_or_create(
                    username=response['login'],
                    first_name=response.get('name', ''),
                    email=response.get('email', ''),
                )
                tokens[token] = user.id
                return user

