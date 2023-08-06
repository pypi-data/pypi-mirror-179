import math
import time

from substrateinterface import SubstrateInterface

from ..constants import FUTURE, PAST, SUBSTRATE
from .base import TimeLine
from .exceptions import TimeLineConnectionRefusedError

ALL_BLOCKS = math.inf
METARIUM_EXTRINSIC = "Metarium"


class SubstrateConnector(TimeLine):

    def __init__(self, *args, **kwargs) -> None:
        reconnection_attempts = 1
        while True:
            try:
                self.__client = SubstrateInterface(
                    url=kwargs.get("url", "ws://127.0.0.1:9944")
                )
            except ConnectionRefusedError:
                if reconnection_attempts == self.__class__.MAX_TIMELINE_RECONNECTION_ATTEMPTS:
                    print(f"Timeline connection terminated after {reconnection_attempts} attempts.")
                    raise TimeLineConnectionRefusedError
                print(f"Timeline connection refused. Retrying in {self.__class__.TIMELINE_RECONNECTION_WAIT_DURATION_SECONDS} seconds ...")
                reconnection_attempts += 1
                time.sleep(self.__class__.TIMELINE_RECONNECTION_WAIT_DURATION_SECONDS)
                continue
            break
        
        self._reset_cached_blocks()
        self._reset_block_headers()

    def prefix(self):
        return self.__class__.POINT_PREFIX

    def client(self):
        return self.__client
    
    def info(self):
        return self.__client.__dict__

    def _reset_cached_blocks(self):
        self.__cached_blocks = {}

    def _reset_block_headers(self):
        self.__current_block = None
        self.__current_block_header = {}
        self.__current_block_number = -1

    def _set_current_block(self, block_hash=None, block_number=None, persevere=False):
        current_block = self.__client.get_block(block_hash=block_hash or None, block_number=block_number or None)
        if persevere:
            while (current_block is None):
                current_block = self.__client.get_block(block_hash=block_hash or None, block_number=block_number or None)
        if current_block and current_block["header"]["number"] != self.__current_block_number:
            self.__current_block = current_block
            self.__current_block_header = self.__current_block["header"]
            self.__current_block_number = self.__current_block_header["number"]


    def get_points(self, direction, block_hash=None, block_count=None) -> None:
        """
            if direction is PAST:
                if block_hash is None:
                    if block_count is None:
                        _get_blocks(start=now, end=block_0, block_count="all")
                    else:
                        _get_blocks(start=now, end=block_0, block_count=block_count)
                else:
                    if block_count is None:
                        _get_blocks(start=block_({block_hash}), end=block_0, block_count="all")
                    else:
                        _get_blocks(start=block_({block_hash}), end=block_0, block_count=block_count)
            else:#if direction is FUTURE
                if block_hash is None:
                    if block_count is None:
                        _stream_blocks(start=now, block_count="all")
                    else:
                        _stream_blocks(start=now, block_count=block_count)
                else:
                    if block_count is None:
                        _stream_blocks(start=block_({block_hash}), block_count="all")
                    else:
                        _stream_blocks(start=block_({block_hash}), block_count=block_count)
        """
        # sanitize inputs
        assert direction in (FUTURE, PAST)
        # setup
        self._reset_cached_blocks()
        self._reset_block_headers()
        self._set_current_block(block_hash=block_hash)
        if block_count is None:
            if direction == PAST:
                block_count = self.__current_block_number
            else:
                block_count = ALL_BLOCKS
        self._reset_cached_blocks()
        # _get_blocks()
        while len(self.__cached_blocks) < block_count:
            if self.__current_block_number in self.__cached_blocks:
                continue
            self.__cached_blocks[self.__current_block_number] = self.__current_block
            has_metarium_call = False
            for extrinsic in self.__current_block["extrinsics"]:
                if extrinsic['call']['call_module']['name'] == METARIUM_EXTRINSIC:
                    has_metarium_call = True
        
            yield self.__current_block, has_metarium_call
            
            if direction == PAST:
                self._set_current_block(block_number=self.__current_block_number-1, persevere=True)
            else:
                self._set_current_block(block_number=self.__current_block_number+1, persevere=True)
    
    def get_point_pairs(self, direction, reference_time={}) -> None:
        """
            reference_time = {
                "type": substrate,
                "pair_point_1": time_point_id (Eg, CID)
                "point_count": int refering block_count
            }
        """
        # sanitize inputs
        reference_time = reference_time or {}
        if len(reference_time):
            assert reference_time["type"] == SUBSTRATE
            assert reference_time["time_point"] is not None
        block_hash = reference_time.get("time_point", None)
        block_count = reference_time.get("point_count", None)
        # _get_pairs()
        block_1 = {}
        block_2 = {}

        for block, has_metarium_call in self.get_points(direction, block_hash, block_count):
            if len(self.__cached_blocks) > 1:
                if direction == FUTURE:
                    block_1 = self.__current_block
                    block_2 = self.__cached_blocks[self.__current_block_number-1]
                else:
                    block_1 = self.__current_block
                    block_2 = self.__cached_blocks[self.__current_block_number+1]
            yield block_1, block_2, has_metarium_call
        
