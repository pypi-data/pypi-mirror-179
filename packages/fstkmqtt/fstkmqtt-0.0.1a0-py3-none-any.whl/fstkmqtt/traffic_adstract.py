import sys
from .network.HTTPServer import httpserver
from .network.TCPServer import tcpserver
from .network.func import request, response
from .supported.func import getinfomation, getresponse, setup_method
import socket as skt
class TrafficApp_Abstract:
    def __init__(
            self, 
            name: str|None = None,
            payloadchannel = sys.stdin):
        self._name = name
        self._connection = None
        
        self._typeprotocol = 'HTTP'

        self._prikey = None
        self._pubkey = None

        self._host = 'localhost'
        self._port = 3445
        
        self._dfunc = {}
        self._nfunc = []

        self._tcpfuncProcess = None

        self._stdin = payloadchannel

    def _check_function_name_is_not_exists(self, fname):
        raise NotImplementedError

    def config(self, **options):
        tmp_host = options.pop('host', self._host)
        self._host = tmp_host if tmp_host else self._host
        tmp_port = options.pop('port', self._port)
        self._port = tmp_port if tmp_port else self._port

        self._prikey = options.pop('key_file', None)
        self._pubkey = options.pop('ca_file', None)

        self._typeprotocol = options.pop('protocol', 'HTTP')

        self._tcpfuncProcess = options.pop('TCPProcess', lambda x: x)

    def _handling_http_request(sock, address, *args, **kargs):
        print(f'[+] Connect from {address[0]}:{address[1]}')
        _this = args[0]
        first_request = getinfomation(request(sock).decode())
        key = first_request['method'] + ";" + first_request['baseurl']
        if first_request['method'] != 'GET': payload = _this._stdin.read()
        else: payload = None
        response(sock, _this._dfunc[key](first_request, payload=payload))

    def _run_with_http(self, listen = 20):
        if self._pubkey and self._prikey:
            print(f'Run at: https://{skt.gethostbyname(self._host)}:{self._port}')
        else:
            print(f'Run at: http://{skt.gethostbyname(self._host)}:{self._port}')
        httpserver.loop_forever_http_server(
            self._host, 
            self._port, 
            listen,
            self,
            ca_file = self._pubkey,
            key_file = self._prikey,
            handling_func = TrafficApp_Abstract._handling_http_request)

    def _handling_tcp_request(sock, address, *self, **kargs):
        self = self[0]
        first_request = request(sock).decode()
        print(f'[+] Connect from {address[0]}:{address[1]}')
        response(sock, self._tcpfuncProcess(first_request))

    def _run_with_tcp(self, listen = 20):
        tcpserver.loop_forever_tcp_server(
            host = self._host,
            port= self._port,
            args=(self),
            listen= listen,
            func_handling = TrafficApp_Abstract._handling_tcp_request
        )

    def run(self, listen = 20):
        if self._typeprotocol == 'HTTP':
            self._run_with_http(listen)
        else:
            self._run_with_tcp(listen)

    def _add_route(self, key, func):
        raise NotImplementedError

    @setup_method
    def route(self, url, *args, method: str = "GET",**options):
        def inner(f):
            f_name = f.__name__
            if self._check_function_name_is_not_exists(f_name):
                key = method+';'+url
                self._add_route(key, f)
                return f
            else:
                raise AssertionError
        return inner