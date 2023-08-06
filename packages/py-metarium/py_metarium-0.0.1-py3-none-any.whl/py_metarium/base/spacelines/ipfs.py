import time

import ipfshttpclient
from ipfshttpclient.exceptions import ConnectionError

from .base import SpaceLine
from .exceptions import SpaceLineConnectionRefusedError


class IPFSConnector(SpaceLine):

    POINT_PREFIX = "ipfs"

    def __init__(self, *args, **kwargs) -> None:
        reconnection_attempts = 1
        while True:
            try:
                self.__client = ipfshttpclient.connect(session=True)
            except ConnectionError:
                if reconnection_attempts == self.__class__.MAX_TIMELINE_RECONNECTION_ATTEMPTS:
                    print(f"Spaceline connection terminated after {reconnection_attempts} attempts.")
                    raise SpaceLineConnectionRefusedError
                print(f"Spaceline connection refused. Retrying in {self.__class__.TIMELINE_RECONNECTION_WAIT_DURATION_SECONDS} seconds ...")
                reconnection_attempts += 1
                time.sleep(self.__class__.TIMELINE_RECONNECTION_WAIT_DURATION_SECONDS)
                continue
            break            

    def prefix(self):
        return self.__class__.POINT_PREFIX

    def client(self):
        return self.__client
    
    def info(self):
        return self.__client.__dict__
    
    def create_time_point_id(self, point_1, point_2, persist_time=False):
        assert len(point_1)
        assert len(point_2)
        persist_time = persist_time or False
        point_1_id = self.__client.add_json(f"{point_1}")
        point_2_id = self.__client.add_json(f"{point_2}")
        time_point_id_str = f"{self.prefix()}:{point_1_id}\n{self.prefix()}:{point_2_id}"
        time_point_id = self.__client.add_str(time_point_id_str)
        if persist_time:
            res = self.__client.pin.add(time_point_id)
        return f"{self.prefix()}:{time_point_id}"
    
    def create_space_point_id(self, time_point_id, happening_point, persist_space=False):
        assert len(time_point_id.split(":")) == 2
        assert len(happening_point)
        persist_space = persist_space or False
        happening_point_id = self.__client.add_json(f"{happening_point}")
        space_point_id_str = f"{time_point_id}\n{self.prefix()}:{happening_point_id}"
        space_point_id = self.__client.add_str(space_point_id_str)
        if persist_space:
            res = self.__client.pin.add(space_point_id)
        return f"{self.prefix()}:{space_point_id}"
    
    def get_persisted_points(self):
        for k, valdict in self.__client.pin.ls().items():
            for val in valdict.items():
                yield val[0]
    
    def yield_persisted_point(self, point_id):
        self.__client.pin.rm(point_id)

