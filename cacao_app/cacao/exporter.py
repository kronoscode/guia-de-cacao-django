from fabric.api import local, task, lcd
from django.conf import settings


def virtualenv(command):
    '''wraps a command to be executed inside of a virtualenvv'''
    params = {
              'command': command,
              'venv': settings.VENV_PATH
             }
    local('source %(venv)s/bin/activate && %(command)s' % params, shell='/bin/bash')


@task
def render_guide(element_number):
    with lcd(settings.PROJECT_DIR):
        command = "python manage.py render_guia --configuration=Export --element=%(element)s --archive --filename=guia-%(element)s.zip" % {'element': element_number}
        virtualenv(command)