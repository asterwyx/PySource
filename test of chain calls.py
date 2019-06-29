class Chain(object):
    
    def __init__(self, path = ''):
        self._path = path
    
    def __getattribute__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
    
    __repr__ = __str__

print(Chain().status.user.timeline.list)