from datetime import datetime

class StatTracker(object):
    def __init__(self):
        self.nodes_visited = 0
        self.total_time = 0
        self._timer = None

    def tick(self):
        self.nodes_visited += 1
        if self._timer == None:
            self._timer = datetime.now()

    def done(self):
        self.total_time = (datetime.now() - self._timer).total_seconds()

    def reset(self):
        self.nodes_visited = 0
        self.total_time = 0
        self._timer = None

