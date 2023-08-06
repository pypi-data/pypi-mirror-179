# payla_utils python package

## Features

### Structlog config

#### 1) Example, structlog configuration, django
in django settings.py

    from payla_utils.logging import LoggingConfigurator

    LoggingConfigurator(
        'testapp',
        log_level='INFO',
        own_apps=settings.OWN_APPS,
        setup_logging_dict=True,
    ).configure_structlog(formatter='plain_console')


#### 2) If you want to use structlog in django celery

in celery.py

    from django.conf import settings
    from payla_utils.logging import LoggingConfigurator

    @signals.setup_logging.connect
    def receiver_setup_logging(
        loglevel, logfile, format, colorize, **kwargs
    ):  # pragma: no cover

        LoggingConfigurator(
            'testapp',
            log_level='INFO',
            own_apps=settings.OWN_APPS,
            setup_logging_dict=True,
        ).configure_structlog(formatter='plain_console')

### 3) If you want to use a structlog, not Django based project

    from payla_utils.logging import LoggingConfigurator

    LoggingConfigurator(
        'testapp',
        log_level='INFO',
        own_apps=[],
        setup_logging_dict=True,
    ).configure_structlog(formatter='plain_console')


#### 4) How to use generic structured logger:

    logger = structlog.get_logger(__name__)
    logger.warning("Here is your message", key_1="value_1", key_2="value_2", key_n="value_n")

### Why structured logger

- By default, the logging frameworks outputs the traces in plain text and tools like EFK stack or Grafana Loki can’t fully process these traces.
- Therefore, if we “structure” or send the traces in JSON format directly, all the tools can benefit of.
- As a developer, it would be nice to be able to filter all logs by a certain customer or transaction.
- The goal of structured logging is to solve these sorts of problems and allow additional analytics.


- When you log something, remember that the actual consumer is the machine Grafana Loki (EFK stack), not only humans.
- Our generic logger comes with some default context structure, but as you can see, you can introduce new keys.
- We use structlog as wraper on standard logging library, you can check for more details [structlog](https://www.structlog.org/en/stable/).


## Access decorator

To prohibit access to only internal IPs for a specific view it's possible to use the `only_internal_access` decorator.

SERVER_IP is required to be set on payla_utils settings.

[See configuration section](#Configuration-and-settings)

Example usage

```python
@only_internal_access
def test_view(request):
    return HttpResponse('OK')
```
Or inline

```python
path('test/', only_internal_access(test_view), name="test-view"),
```

## Management command to init environment

This management command will init environment based on the current env (local.dev, dev, stage, playground and prod)

- load fixtures on the first run (when the DB is empty)
- setup custom theme for admin_interface
- create user when not in prod if `LOCAL_DJANGO_ADMIN_PASSWORD` is set

APP_NAME and ENVIRONMENT settings are required. [See configuration section](#Configuration-and-settings)

## Configuration and settings

Settings for Payla Utils are all namespaced in the PAYLA_UTILS setting.
For example your project's `settings.py` file might look like this:

```python
PAYLA_UTILS = {
    'APP_NAME': 'My App',
    # Used for json logging
    'MICROSERVICE_NAME: 'myapp',
    # dev, stage, prod ...
    'ENVIRONMENT': ENVIRONMENT,
    'INITIAL_FIXTURES': [
        os.path.join(BASE_DIR, 'testapp', 'fixtures', 'users.json'),
    ],
    'SERVER_IP': '192.168.1.4',
    'REQUEST_ID_HEADER': 'X-Request-ID',
    'TRACING_ENABLED': True,
    'RUN_EXTRA_COMMANDS': ['loadinitialusers', 'setup_something'],
    'LOCAL_DJANGO_ADMIN_PASSWORD': os.environ.get('LOCAL_DJANGO_ADMIN_PASSWORD', 'admin'),
    # Only in case you need to change the defaults
    'ENV_THEMES': {
        'local.dev': {
            'title_color': '#000000',
            'css_header_background_color': '#ffffff',
            'env_color': '#00cb38',
            'css_header_text_color': '#000000',
            'css_header_link_color': '#000000',
            'css_header_link_hover_color': '#1e00ac',
            'css_module_background_color': '#ababab',
            'css_module_background_selected_color': '#e3e3e3',
            'css_module_text_color': '#000000',
            'css_module_link_color': '#000000',
            'css_module_link_hover_color': '#3255fe',
            'css_generic_link_color': '#000000',
            'css_save_button_background_color': '#6d6d6d',
            'css_save_button_background_hover_color': '#4a4a4a',
        },
        'dev': {
            'title_color': '#ffffff',
            'env_color': '#00cb68',
            'css_header_background_color': '#007b3b',
            'css_header_text_color': '#f5dd5d',
            'css_header_link_color': '#ffffff',
            'css_header_link_hover_color': '#1e00ac',
            'css_module_background_color': '#006731',
            'css_module_background_selected_color': '#ffffff',
            'css_module_text_color': '#ffffff',
            'css_module_link_color': '#ffffff',
            'css_module_link_hover_color': '#5f0000',
            'css_generic_link_color': '#000000',
            'css_save_button_background_color': '#006731',
            'css_save_button_background_hover_color': '#01a74f',
        },
        'stage': {
            'title_color': '#ffffff',
            'env_color': '#ffcb38',
            'css_header_background_color': '#ff9722',
            'css_header_text_color': '#ffffff',
            'css_header_link_color': '#ffffff',
            'css_header_link_hover_color': '#41aad1',
            'css_module_background_color': '#ca6a00',
            'css_module_background_selected_color': '#ffffff',
            'css_module_text_color': '#ffffff',
            'css_module_link_color': '#ffffff',
            'css_module_link_hover_color': '#41aad1',
            'css_generic_link_color': '#000000',
            'css_save_button_background_color': '#ca6a00',
            'css_save_button_background_hover_color': '#ff9722',
        },
        'playground': {
            'title_color': '#ffffff',
            'env_color': '#00cb38',
            'css_header_background_color': '#09137a',
            'css_header_text_color': '#ffffff',
            'css_header_link_color': '#ffffff',
            'css_header_link_hover_color': '#1e00ac',
            'css_module_background_color': '#0020bf',
            'css_module_background_selected_color': '#e3e3e3',
            'css_module_text_color': '#ffffff',
            'css_module_link_color': '#ffffff',
            'css_module_link_hover_color': '#69c2cc',
            'css_generic_link_color': '#000000',
            'css_save_button_background_color': '#0038ff',
            'css_save_button_background_hover_color': '#02208b',
        },
        'prod': {
            'title_color': '#ffffff',
            'env_color': '#00cb38',
            'css_header_background_color': '#720606',
            'css_header_text_color': '#ffffff',
            'css_header_link_color': '#ffffff',
            'css_header_link_hover_color': '#1e00ac',
            'css_module_background_color': '#e73f41',
            'css_module_background_selected_color': '#e3e3e3',
            'css_module_text_color': '#ffffff',
            'css_module_link_color': '#ffffff',
            'css_module_link_hover_color': '#5f0000',
            'css_generic_link_color': '#000000',
            'css_save_button_background_color': '#720606',
            'css_save_button_background_hover_color': '#4a4a4a',
            # APP_NAME will be replaced by the correct app name set in payla utils settings
            'title': 'APP_NAME',
        },
    }
}
```
