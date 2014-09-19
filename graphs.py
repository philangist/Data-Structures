class Vertex(object):

    def __unicode__(self):
        return u'%s(data: %s)' % (self.__class__.__name__, self.data)
    __str__ = __unicode__
    __repr__ = __unicode__

    def __init__(self, data, neighbors=[]):
        self._validate_type(data, basestring)
        self._validate_type(neighbors, list)
        self.data = data
        self.neighbors = neighbors

    def add_neighbors(self, neighbors):
        self._validate_type(neighbors, list)
        neighbors_copy = self.neighbors[:]

        for neighbor in neighbors:
            if (neighbor not in self.neighbors and neighbor != self):
                neighbors_copy.append(neighbor)
        self.neighbors = neighbors_copy

    def _validate_type(self, parameter, expected_type):
        if not isinstance(parameter, expected_type):
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
