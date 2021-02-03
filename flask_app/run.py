#!/usr/bin/env python3
"""Created on Sat Dec  5 16:50:58 2020"""


from annotation import app

if __name__ == '__main__':
    app.run(host='192.168.1.9', threaded=True,debug=True)
