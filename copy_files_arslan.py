#!/usr/bin/env python
import os
from BI.settings import BASE_DIR, INSTALLED_APPS
if __name__ == '__main__':
    destination = os.path.join(BASE_DIR, 'BI', 'static')
    for app in [_.split('.')[0] for _ in INSTALLED_APPS if not _.startswith('django')] + ['django.contrib.staticfiles']:
        source = os.path.join(BASE_DIR, app.split('.')[0], 'static')
        if os.path.isdir(source):
            os.system('cp -Rf {}/* {}/'.format(source, destination))
            print('App "{}" static folder copied to {}'.format(app, destination))
        else:
            print ('App "{}" has no static folder. '.format(app))