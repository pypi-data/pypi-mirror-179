class SpaceLine(object):

    TIMELINE_RECONNECTION_WAIT_DURATION_SECONDS = 5
    MAX_TIMELINE_RECONNECTION_ATTEMPTS = 10
    POINT_PREFIX = "space"

    def prefix(self):
        raise NotImplementedError

    def client(self):
        raise NotImplementedError
    
    def info(self):
        raise NotImplementedError