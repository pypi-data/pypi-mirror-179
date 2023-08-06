from .constants import (PAST, FUTURE)

class Being(object):

    def __init__(self, **kwargs) -> None:
        self._reset_portals()
        if "timeline" in kwargs:
            assert "type" in kwargs["timeline"]
            assert "parameters" in kwargs["timeline"]
            if kwargs["timeline"]["type"] == "substrate":
                try:
                    from .timelines import SubstrateConnector
                    self.timeline_portal = SubstrateConnector(**kwargs["timeline"]["parameters"])
                    self.timeline = self.timeline_portal.client()
                    print("""         CONNECTED TO TIMELINE!        """)
                except ImportError:
                    print("""         ERROR IMPORTING TIMELINE!     """)
            
        if "spaceline" in kwargs:
            assert "type" in kwargs["spaceline"]
            assert "parameters" in kwargs["spaceline"]
            if kwargs["spaceline"]["type"] == "ipfs":
                try:
                    from .spacelines import IPFSConnector
                    self.spaceline_portal = IPFSConnector(**kwargs["spaceline"]["parameters"])
                    self.spaceline = self.spaceline_portal.client()
                    print("""        CONNECTED TO SPACELINE!        """)
                except ImportError:
                    print("""        ERROR IMPORTING SPACELINE!     """)
                
    def _reset_portals(self):
        self.timeline_portal = None
        self.timeline = None

        self.spaceline_portal = None
        self.spaceline = None

        self.cached_time_points = {}
        self.cached_space_points = {}

    def info(self):
        return {
            "timeline" : self.timeline_portal.info() if self.timeline_portal else None,
            "spaceline" : self.spaceline_portal.info() if self.spaceline_portal else None
        }

    def _reset_cached_time_points(self):
        # temporal points that are not recorded
        self.cached_time_points = {}
    
    def _reset_cached_space_points(self):
        # temporal space points that are not recorded
        self.cached_space_points = {}

    def create_points(self, direction, reference_time={}, reference_space={}, persist_time=False, persist_space=False):
        assert direction in (PAST, FUTURE)
        persist_time = persist_time or False
        persist_space = persist_space or False
        reference_time = reference_time or {}
        reference_space = reference_space or {}
        if direction == FUTURE:
            for point, previous_point, has_happening in self.timeline_portal.get_point_pairs(direction, reference_time):
                time_point_id = None
                space_point_id = None
                # print(f"\n")
                # print(f"point :\n{point}")
                # print(f"previous_point :\n{previous_point}")
                # print(f"has_happening :\n{has_happening}")
                try:
                    time_point_id = self.spaceline_portal.create_time_point_id(point, previous_point, persist_time=persist_time)
                except AssertionError:
                    continue
                
                if has_happening:
                    space_point_id = self.spaceline_portal.create_space_point_id(time_point_id, point, persist_space=persist_space)
                
                yield time_point_id, space_point_id

    def get_persisted_points(self):
        for point in self.spaceline_portal.get_persisted_points():
            yield point

    def yield_persisted_point(self, point_id):
        self.spaceline_portal.yield_persisted_point(point_id)
