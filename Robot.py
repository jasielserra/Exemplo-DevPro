class Robot():
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Robot3D(Robot):
    def __init__(self, x, y, z):
        super(Robot3D, self).__init__(x,y)
        self.z = z