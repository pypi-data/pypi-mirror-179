from .traffic_adstract import TrafficApp_Abstract
import sys
class TrafficApp(TrafficApp_Abstract):
    def __init__(self, name: str | None = None, payloadchannel=sys.stdin):
        super().__init__(name, payloadchannel)

    def _check_function_name_is_not_exists(self, fname):
        if fname not in self._nfunc:
            self._nfunc.append(fname)
            return True
        return False

    def _add_route(self, key, func):
        self._dfunc[key] = func