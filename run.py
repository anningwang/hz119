#!flask/bin/python
# -*- coding:utf-8 -*-
from app import app
from app.tools.getip import get_ip


if __name__ == '__main__':
    ip = get_ip()
    app.run(host=ip, port=9300, debug=True, threaded=True)
