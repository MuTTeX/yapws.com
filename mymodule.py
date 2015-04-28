#!/usr/bin/python3.4
import sys
import os
PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, PATH)

from project import create_app
application = create_app()
application.debug = True

print("/////////////////////////////////////////////uwsgi load")

if __name__ == '__main__':

    application.run(host="0.0.0.0", debug=True)