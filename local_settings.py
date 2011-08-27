OAUTH_CLIENT_ID = '56e1d1e74d134fc6c563'
OAUTH_SECRET = 'd27cd033dfe8e825fa445c8b6e01bfe3f2bbb1f8'
OAUTH_BASE_URL = 'https://github.com/login/oauth/'

OAUTH_AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
OAUTH_ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'

GITHUB_API_URL = 'https://api.github.com'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite'
    }
}

AUTHENTICATION_BACKENDS = (
    'github_plus.auth.GitHubOAuth',
)
