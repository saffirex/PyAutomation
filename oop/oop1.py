class point:
    """Creates a new point with x and y coordinates """

    def __init__(self, a=0, b=0):
        """ initializes the coordinates at x and y """
        self.x=a
        self.y=b
    
    def distance_from_origin(self):
        """#distance from origin printing"""
        return (self.x**2 + self.y**2)**0.5


p= point()
print ("x={0}), y={1}".format(p.x,p.y))
print(p.x, p.y)

p.x=5
p.y=8
q = point(0,87)
print ("for q: x={0}, y={1}".format(q.x,q.y))
print( q.distance_from_origin () )
