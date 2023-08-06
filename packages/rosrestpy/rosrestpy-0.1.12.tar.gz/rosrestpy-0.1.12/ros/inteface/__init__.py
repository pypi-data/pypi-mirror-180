from typing import List, Optional

from ros._base import BaseModule

from .bridge import BridgeModule, Bridge, BridgeMsti, BridgePort, BridgeVlan
from .ethernet import EthernetModule
from .interface import Interface
from .list import InterfaceList, InterfaceListMember, InterfaceListModule


class InterfaceModule(BaseModule):
    _brigde: Optional[BridgeModule] = None
    _ethernet: Optional[EthernetModule] = None
    _list: Optional[InterfaceListModule] = None

    @property
    def bridge(self) -> BridgeModule:
        if not self._brigde:
            self._brigde = BridgeModule(self, "/bridge")
        return self._brigde

    @property
    def list(self) -> InterfaceListModule:
        if not self._list:
            self._list = InterfaceListModule(self, "/list")
        return self._list

    @property
    def ethernet(self) -> EthernetModule:
        if not self._ethernet:
            self._ethernet = EthernetModule(self, "/ethernet")
        return self._ethernet

    def print(self) -> List[Interface]:
        return self.ros.get_as(self.url, List[Interface])


__all__ = [
    "BridgeModule",
    "Bridge",
    "BridgeMsti",
    "BridgePort",
    "BridgeVlan",
    "EthernetModule",
    "InterfaceModule",
    "Interface",
    "InterfaceList",
    "InterfaceListMember",
    "InterfaceListModule",
]
