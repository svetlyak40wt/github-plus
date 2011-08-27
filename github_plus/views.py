# Create your views here.
import oauth2
import logging
import urllib
import urllib2
import urlparse

#from django.utils.shortcuts import render_to_string
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate, login as login_user, logout as logout_user


def login(request):
    url = settings.OAUTH_AUTHORIZE_URL + '?' + urllib.urlencode(dict(
        client_id=settings.OAUTH_CLIENT_ID,
    ))
    return HttpResponseRedirect(url)


def logout(request):
    logout_user(request)
    return HttpResponseRedirect('/')


def auth_callback(request):
    code = request.GET.get('code', '')
    response = urllib2.urlopen(
        settings.OAUTH_ACCESS_TOKEN_URL,
        urllib.urlencode(dict(
            client_id=settings.OAUTH_CLIENT_ID,
            client_secret=settings.OAUTH_SECRET,
            code=code,
        )),
        timeout=30,
    )
    response = dict(
        urlparse.parse_qsl(response.read())
    )
    print response

    if 'access_token' in response:
        user = authenticate(token=response['access_token'])
        print 'user=', user
        login_user(request, user)

    return HttpResponseRedirect('/')

