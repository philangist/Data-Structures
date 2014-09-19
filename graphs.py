class Vertex(object):
    def __init__(self, value, neighbors=[]):
        self._validate_type(value, basestring)
        self._validate_type(neighbors, list)
        self.value = value
        self.neighbors = neighbors

    def __unicode__(self):
        return u'%s(value: %s)' % (self.__class__.__name__, self.value)
    __str__ = __unicode__
    __repr__ = __unicode__

    def add_neighbors(self, neighbors):
        self._validate_type(neighbors, list)
        neighbors_copy = self.neighbors[:]

        for neighbor in neighbors:
            if (neighbor not in self.neighbors and neighbor != self):
                neighbors_copy.append(neighbor)
        self.neighbors = neighbors_copy

    def _validate_type(self, parameter, type):
        if not isinstance(parameter, type):
            raise TypeError


A = Vertex('A')
B = Vertex('B')
C = Vertex('C')
D = Vertex('D')
E = Vertex('E')
F = Vertex('F')


A.add_neighbors([B, C])
B.add_neighbors([C, D])
C.add_neighbors([D])
D.add_neighbors([C])
E.add_neighbors([F])
F.add_neighbors([C])
