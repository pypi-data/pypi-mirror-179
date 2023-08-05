from .algorithms.rsa import decrypto, encrypto, createPEM, test
from .algorithms.aes import AESCipher
from .algorithms.hmac import hmacsha256, hmac, merginhmacsha256
from .algorithms.sha import (
    sha1,
    sha224,
    sha256,
    sha384,
    sha3_224,
    sha3_256,
    sha3_512,
    sha512
)

decrypto = decrypto
encrypto = encrypto
createPEM = createPEM

AESCipher = AESCipher
hmac = hmac
hmacsha256 = hmacsha256
sha1 = sha1
sha224 = sha224
sha256 = sha256
sha384 = sha384
sha3_224 = sha3_224
sha3_256 = sha3_256
sha3_512 = sha3_512
sha512 = sha512
merginhmacsha256 = merginhmacsha256

from .database.mssql.mssqlconnect import MSSQLConnection
from .database.mssql.mssqlquery import query as mssqlQuery
from .database.mysql.mysqlconnect import (
    MySequel,
    configconnectionMySql,
    configssl,
    createFailoverserver
)
from .database.mysql.mysqlquery import query as mysqlquery
from .database.mssql.mssqlconnect import SQLServer

from .database.sqlite.sqliteconnect import sqliteconnect as _SQLite
from .database.sqlite.sqlitequery import query as SQLiteQuery

from .database.warehouse.warehouseconnect import warehouseconnect as Warehouse

class MSSQL:
    SQLServer = SQLServer
    SQLServerConnection = MSSQLConnection
    SQLServerQuery = mssqlQuery

class MySQL:
    MySQL = MySequel
    MySQLQuery = mysqlquery
    ConfigConnection = configconnectionMySql
    ConfigSSL = configssl
    CreateFailoverServer = createFailoverserver

class SQLite:
    SQLite = _SQLite
    Query = SQLiteQuery

Warehouse = Warehouse

from .exceptions import (
    MissingDataException,
    ConnectException,
    NotEnoughPrivilege,
    NullConnectionError
)

MissingDataException = MissingDataException
ConnectException = ConnectException
NotEnoughPrivilege = NotEnoughPrivilege
NullConnectionError = NullConnectionError
DontHaveAnyConnectionException = ConnectException.DontHaveAnyConnectionException

from .network.TCPServer import tcpserver
from .network.HTTPServer import httpserver
from .network.func import request, response

tcpserver = tcpserver
httpserver = httpserver
request = request
response = response

from .render import GetRender as _Getrender
GetRender =_Getrender