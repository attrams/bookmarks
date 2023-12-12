# Bookmarks

This is a simple django project that allows users to create account and also share images.

## What was learnt

- Authentication.
- Password change and reset.
- Social Authentication(Google and Apple).

## Libraries used

- [pillow](https://pypi.org/project/Pillow/) - for image processing.
- [social-auth-app-django](https://github.com/python-social-auth/social-app-django) - for social authentication.
- [django-extensions](https://github.com/django-extensions/django-extensions) - this extension also includes the installation of:
  - [werkzeug](https://pypi.org/project/Werkzeug/) - which is required by RunServerPlus extension of Django extensions.
  - [pyOpenSSL](https://pypi.org/project/pyOpenSSL/) - which is required to use SSL/TLS functionality of RunServerPlus.

## PS

- Locate `/etc/hosts`(linux) or `C:\Windows\System32\Drivers\etc\hosts`(windows). Edit This file to include:

```
127.0.0.1 mysite.com
```

This is to allow your pc to redirect to localhost when you enter `mysite.com` in your browser.
