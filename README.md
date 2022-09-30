# ServiceDown-api
Open Services Status Data
\
[![](https://badgen.net/badge/Service/Down/red)]()
[![](https://img.shields.io/badge/python-3.9-blue?logo=python&logoColor=yellow)]()
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)

![Banner](/static/banner_github-white.png#gh-light-mode-only)
![Banner](/static/banner_github-darkgrey.png#gh-dark-mode-only)


The API of Service Down

With this project I want to make services status information **open data**.
With a bunch of metrics like the number of reports, average report, in which region ...

More than 230 services is available in 2 country (FR & US).

## Get stated :rocket:
### installation
To install ServiceDown-api, you need to install some things :
- Python 3.9
- pip
- Django 4.0.4
- Install ``requirements.txt`` with ``pip install -r requirements.txt``
- Create file ``.env`` in ``ServiceDown_api/service_down`` with properties : ``DEBUG, SECRET_KEY, DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD``
### Use
Applied migrations : ``python manage.py migrate``
\
Make fixtures (seed database) with custom command : ``python manage.py loadfixtures``
\
Run server : ``python manage.py runserver``

## Roadmap
- **v1.1**: Service categories
- **v1.5** "Log4me" Log actions and send it to the Discord Bot
- **v2**: Auth and user account

## Version
[![](https://badgen.net/github/tag/BenjaminFourmaux/ServiceDown-api?cache=600)](https://github.com/BenjaminFourmaux/ServiceDown-api/tags) [![](https://badgen.net/github/release/BenjaminFourmaux/ServiceDown-api?cache=600)](https://github.com/BenjaminFourmaux/ServiceDown-api/releases)
- [coming soon][v1] First API version with basic actions

## Contributors
[![](https://badgen.net/github/contributors/BenjaminFourmaux/ServiceDown-api)](https://github.com/BenjaminFourmaux/ServiceDown-api/graphs/contributors)
- :crown: [Benjamin Fourmaux](https://github.com/BenjaminFourmaux)

## Supporting
If you like this project and if you want, make a donation

[![](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://streamlabs.com/techben-googlefanfr)

## Social Networks
[![](https://img.shields.io/youtube/channel/subscribers/UC6iaEEz7A21SfmGcbImpYDw?color=red&style=social)](https://www.youtube.com/channel/UC6iaEEz7A21SfmGcbImpYDw)
[![](https://img.shields.io/twitter/follow/BFourmaux?style=social)](https://twitter.com/BFourmaux)

[![](http://ForTheBadge.com/images/badges/built-with-love.svg)]()
