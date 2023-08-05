from argparse import ArgumentParser
usage = 'python -m pyFMQTT --name [name] --host [host] --port [port] --protocol [protocol]'

description = '''
pyFMQTT is a part for supported FullstackMQTT enviroment.
'''

from random import choices
from string import ascii_letters, digits

a = ArgumentParser(
usage=usage,
description=description
)

a.add_argument(
    '--name', 
    default='FSTKMQTTPROJECT_%s'%(''.join(choices(ascii_letters+digits, k = 12))),
    help='Name project'
)
a.add_argument(
    '--host', 
    default='localhost',
    type=str,
    help='IP Address or Hosting'
)
a.add_argument(
    '--port', 
    default=4435,
    type=int,
    help='Port (1 <= port <= 65535)'
)
a.add_argument(
    '--protocol',
    default='HTTPS',
    help='Protocol HTTP or HTTPS or TCP'
)

values = a.parse_args()

nameproject = values.name
host = values.host
port = values.port
protocol = values.protocol

# Code tool file
toolcode = """# DON'T FIX IT.
from argparse import ArgumentParser
usage = 'python tools nameapp'
description = '''
It help for your creative a dir and file.
'''
a = ArgumentParser(
    usage=usage,
    description=description
)
a.add_argument(
    '--createapp',
    required=False,
    help='Create new app when it not exists and raiseError with other case',
)
a.add_argument(
    '--createconnect',
    required=False,
    choices=['mysql', 'mssql', 'sqlite', 'warehouse', ''],
    default=''
)
a.add_argument(
    '--host',
    required=False,
    help='host index that used by your database server. It active when you use createconnect option',
    default=''
)
a.add_argument(
    '--port',
    required=False,
    help='port index that used by your database server',
    default=''
)
a.add_argument(
    '--user',
    required=False,
    help='user help you login to database(either SQLite and Warehouse)',
    default=''
)
a.add_argument(
    '--password',
    required=False ,
    help='password for login or perform decode file database.',
    default=''
)
a.add_argument(
    '--dbname',
    required=False,
    help='Database name.',
    default=''
)
a.add_argument(
    '--dbfile',
    required=False,
    help='Database directory, It only active when you use SQLite and Warehouse for your project' ,
    default=''
)
value = a.parse_args()
createapp = value.createapp
createconnect = value.createconnect
host = value.host
port = value.port
user= value.user
password = value.password
dbname = value.dbname
dbfile = value.dbfile
VALUEAUTO = 1
import getpass
if user and not password: password = getpass.getpass('$password>>')
import os
view = b'{\\r\\n"view": {\\r\\n"__type__" : "dir",\\r\\n"%s" : {\\r\\n"__type__" : "dir",\\r\\n"__init__.py": {\\r\\n"__type__" : "__file__",\\r\\n"__content__" : "import os;tmp = os.listdir();joinpath = lambda *x: os.path.join(*x)\\\\ndef _allfiles(dir):\\\\n\\\\tres = {}\\\\n\\\\tld = os.listdir(dir)\\\\n\\\\tfor i in ld:\\\\n\\\\t\\\\tif i == \\\\"__init__.py\\\\": continue\\\\n\\\\t\\\\ttmp = joinpath(dir, i)\\\\n\\\\t\\\\tif os.path.isfile(tmp): res[\\\\"/\\\\".join(tmp.split(\\\\"\\\\\\\\\\\\\\\\\\\\")[-2:]).split(\\\\".\\\\")[0]]=tmp\\\\n\\\\t\\\\telse: res.update(_allfiles(tmp))\\\\n\\\\treturn res\\\\nallfile = _allfiles(os.path.abspath(os.curdir))\\\\ndel tmp, joinpath"\\r\\n},\\r\\n"theme" : {\\r\\n"__type__" : "dir",\\r\\n"index.html": {\\r\\n"__type__" : "__file__",\\r\\n"__content__" : "<!DOCTYPE html>\\\\n<html lang=\\\\"en\\\\">\\\\n<head>\\\\n\\\\t<meta charset=\\\\"UTF-8\\\\">\\\\n\\\\t<meta http-equiv=\\\\"X-UA-Compatible\\\\" content=\\\\"IE=edge\\\\">\\\\n\\\\t<meta name=\\\\"viewport\\\\" content=\\\\"width=device-width, initial-scale=1.0\\\\">\\\\n\\\\t<title>Document</title>\\\\n</head>\\\\n<body>\\\\n\\\\t\\\\n</body>\\\\n</html>"\\r\\n}\\r\\n},\\r\\n"style" : {\\r\\n"__type__" : "dir",\\r\\n"style.css": {\\r\\n"__type__" : "__file__",\\r\\n"__content__" : ""\\r\\n}\\r\\n},\\r\\n"code" : {\\r\\n"__type__" : "dir",\\r\\n"code.js": {\\r\\n"__type__" : "__file__",\\r\\n"__content__" : ""\\r\\n}\\r\\n}\\r\\n}\\r\\n}\\r\\n}\\r\\n\\r\\n\\r\\n'
viewmodel=b'{\\r\\n"viewmodel": {\\r\\n"__type__" : "dir",\\r\\n"%s" : {\\r\\n"__type__" : "dir",\\r\\n"__init__.py": {\\r\\n"__type__" : "__file__",\\r\\n"__content__" : ""\\r\\n},\\r\\n"page.py": {\\r\\n"__type__" : "__file__",\\r\\n"__content__" : "import sys\\\\nsys.path.append(\\\\"../../\\\\")\\\\nfrom view.hello import allfile\\\\nfrom fstkmqtt import GetRender\\\\ndef page_%s_process(request, *args, **kwargs):\\\\n\\\\t# Your code:\\\\n\\\\tpass"\\r\\n}\\r\\n}\\r\\n}\\r\\n}\\r\\n\\r\\n\\r\\n'
modulepyfile = {
    "mysql": "from fstkmqtt import MySQL\\r\\nmysql{id} = MySQL.MySQL()\\nmysql{id}.config(\\n\\thost = {host},\\n\\tuser = {user},\\n\\tpassword= \\"{password}\\",\\n\\tdatabase = {dbname}\\n)",
    'mssql': "from fstkmqtt import MSSQL\\r\\nmssql{id} = MSSQL.SQLServer()\\ns.config(\\n\\tuser={user},\\n\\tpassword=\\"{password}\\",\\n\\tdatabased={dbname},\\n\\thost = {host},\\n\\tport = {port}\\n)",
    "sqlite": "from fstkmqtt import SQLite\\n\\nsqlite{id} = SQLite.SQLite()\\na.config(\\n\\tdatabase='{dbpath}'\\n)",
    'warehouse' : '''from fstkmqtt import Warehouse
warehouse{id} = Warehouse()
from datetime import datetime
utcnow = datetime.utcnow()
warehouse{id}.config((utcnow.year, utcnow.month, utcnow.day), nameproject="{dbname}")    
'''
}
from json import loads
import re
def istype(object, cast): return type(object) is cast
def anytype(object, *castes): return any([istype(object, cast) for cast in castes])
VIEWMODEL = loads(viewmodel)
VIEW = loads(view)
joinpath = lambda *x: os.path.join(*x)
def directoryget(data, *replace, parent = []):
    currentpath = os.path.abspath(os.curdir)
    _type_ = data['__type__']
    __path__ = joinpath(currentpath, *parent)
    try: __path__ = __path__%replace
    except: pass
    tmp = parent.copy()
    if _type_ == "dir":
        os.makedirs(__path__, exist_ok=True)
        for i in data:
            if i == '__type__': continue
            tmp.append(i)
            directoryget(data[i], *replace, parent = tmp)
            tmp.pop()
    elif _type_ == "__file__":
        try:
            open(__path__, 'r')
            raise NotImplementedError
        except: 
            rawdata = data['__content__']
            try: rawdata = data['__content__'].decode()
            except: rawdata = data['__content__']
            try: rawdata = rawdata%replace
            except: pass
            with open(__path__, 'x') as f:
                f.write(rawdata)
# Create app
if createapp:
    directoryget(VIEW['view'], createapp, parent=['view'])
    directoryget(VIEWMODEL['viewmodel'], createapp, parent=['viewmodel'])    
    data = 'from viewmodel.{nameapp}.page import allfile as allfileHello, page_{nameapp}_process\\r'
    with open('app.py', 'r') as f:
        nowdata = f.read()
    location = nowdata.find('#AUTO_ADD_LIB%')
    if location >=0: 
        nowdata = nowdata[:location] + data.format(nameapp=createapp)+ nowdata[location:]
        with open('app.py', 'w') as f:
            f.seek(0)
            f.truncate()
            f.write(nowdata)
    
    data = '''@app.route('/{nameapp}', method="GET")
def fslash{nameappcap}(request, *args, **kwargs):
    return page_{nameapp}_process(request, *args, **kwargs)\\r'''
    with open('app.py', 'r') as f:
        nowdata = f.read()
    location = nowdata.find('#AUTO_ADD%')
    if location >=0: 
        nowdata = nowdata[:location] + data.format(nameapp=createapp, nameappcap=createapp.capitalize())+ nowdata[location:]
        with open('app.py', 'w') as f:
            f.seek(0)
            f.truncate()
            f.write(nowdata)
            
elif createconnect:
    f = open('tool.py', 'r')
    data = f.read()
    f.close()
    tmp = re.search('VALUEAUTO\\s*=\\s*[0-9]*\\n', data).span()
    left, right = tmp
    nowvalue = int(data[left:right].split(' = ')[1])
    tmp = modulepyfile[createconnect]
    if createconnect == "mysql" or createconnect == "mssql": 
        while not all([host, port, user, password, dbname]):
            if not host: host = input('$host>>')
            if not port: port = int(input('$port>>'))
            if not user: user = input('$user>>')
            if not password: password = getpass.getpass('$password>>')
            if not dbname: dbname = input('$dbname>>')
        tmp = tmp.format(id = nowvalue, host = host, user = user, password = password, dbname = dbname)
    elif createconnect == 'warehouse' : 
        while not dbname: dbname = input('$dbname>>')
        tmp = tmp.format(id = nowvalue, dbname = dbname)
    elif createconnect == 'sqlite':
        while not dbfile: dbfile = input('$dbfile>>')
        tmp = tmp.format(id = nowvalue, dbpath = dbfile)
    else: raise NotImplementedError
    namefile = f'connect{createconnect.capitalize()}Id{nowvalue}'
    cur = os.path.abspath(os.curdir)
    os.makedirs(joinpath(cur, "model"), exist_ok=True)
    with open(joinpath(cur, 'model', f"{namefile}.py"), 'x') as f:
        f.write(tmp)
    nowvalue += 1

    data = data[:left] + f'VALUEAUTO = {nowvalue}\\n' + data[right:]
    with open('tool.py', 'w') as f:
        f.seek(0)
        f.truncate()
        f.write(data)
"""

# pyFMQTT = open('pyFMQTT.json', 'rb').read()
# print(pyFMQTT)
pyFMQTT = b'{\r\n"view": {\r\n"__type__" : "dir",\r\n"__init__.py": {\r\n"__type__": "__file__",\r\n"__content__" : ""\r\n},\r\n"tutorial.txt": {\r\n"__type__" : "__file__",\r\n"__content__": "using command \\n\\t>> python tool.py --createapp [Name app]\\nto create"\r\n}\r\n},\r\n"viewmodel": {\r\n"__type__" : "dir",\r\n"__init__.py": {\r\n"__type__": "__file__",\r\n"__content__" : ""\r\n},\r\n"tutorial.txt": {\r\n"__type__" : "__file__",\r\n"__content__": "using command \\n\\t>> python tool.py --createapp [Name app]\\nto create"\r\n}\r\n},\r\n"model": {\r\n"__type__" : "dir",\r\n"__init__.py": {\r\n"__type__": "__file__",\r\n"__content__" : ""\r\n},\r\n"tutorial.txt": {\r\n"__type__" : "__file__",\r\n"__content__": "using command \\n\\t>> python tool.py --createconnect [type]\\nto create.\\nOptions of type variables:\\n\\tmysql\\n\\tmssql\\n\\tsqlite\\n\\twarehouse"\r\n}\r\n},\r\n"app.py":{\r\n"__type__" : "__file__",\r\n"__content__": ""\r\n},\r\n"tool.py":{\r\n"__type__" : "__file__",\r\n"__content__": ""\r\n}\r\n}'
from json import loads
import os

joinpath= lambda *x : os.path.join(*x)

constructPyFMQTT = loads(pyFMQTT)

def directoryget(data, *replace, parent = []):
    currentpath = os.path.abspath(os.curdir)
    _type_ = data['__type__']
    __path__ = joinpath(currentpath, *parent)
    try: __path__ = __path__%replace
    except: pass
    tmp = parent.copy()
    if _type_ == "dir":
        os.makedirs(__path__, exist_ok=True)
        for i in data:
            if i == '__type__': continue
            tmp.append(i)
            directoryget(data[i], *replace, parent = tmp)
            tmp.pop()
    elif _type_ == "__file__":
        try:
            open(__path__, 'r')
            raise NotImplementedError
        except: 
            rawdata = data['__content__']
            try: rawdata = data['__content__'].decode()
            except: rawdata = data['__content__']
            try: rawdata = rawdata%replace
            except: pass
            with open(__path__, 'x') as f:
                f.write(rawdata)

for i in constructPyFMQTT:
    directoryget(constructPyFMQTT[i], parent=[nameproject, i])

appcode = '''# Import libaries
import sys
sys.path.append('./viewmodel')
from fstkmqtt.TrafficApp import TrafficApp
#AUTO_ADD_LIB%\n
#YOUR CA_FILE:
CA_FILE = None

#YOUR KEY_FILE:
KEY_FILE = None

#YOUR HOST: None -> localhost(127.0.0.1)
HOST = None

# YOUR PORT: None -> 3445
PORT = None

app = TrafficApp()
app.config(
    host = HOST,
    port = PORT,
    ca_file = CA_FILE,
    key_file = KEY_FILE,
    protocol = '{protocol}',
    TCPProcess = lambda x: x
)

# Example
# @app.route('/')
# def forwardslash(request, *args, **kwargs):
#     return b"""HTTP/1.1 200 OK
#             \\rDate: Mon, 27 Jul 2009 12:28:53 GMT
#             \\rServer: FullstackMQTT/0.0.1a (Win32)
#             \\rLast-Modified: Wed, 22 Jul 2009 19:15:56 GMT
#             \\rContent-Type: text/html\\n\\n
#             \\r<html>
#             \\r<body>
#             \\r<h1>Hello, World!</h1>
#             \\r</body>
#             \\r</html>"""

#AUTO_ADD%\n
app.run()
'''

with open(joinpath(nameproject, 'tool.py'), 'w') as f:
    f.write(toolcode)

if protocol.lower() in ['http', 'https']:
    with open(joinpath(nameproject, 'app.py'), 'w') as f:
        f.write(appcode.format(protocol="HTTP").replace(""",
    TCPProcess = lambda x: x""", ''))
elif protocol.lower() in ['tcp']:
    with open(joinpath(nameproject, 'app.py'), 'w') as f:
        f.write(appcode.format(protocol="TCP"))