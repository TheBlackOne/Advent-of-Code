from itertools import combinations

def add_vectors(v1, v2):
    return list(map(lambda x, y: x + y, v1, v2))

def apply_gravity(body1, body2):
    f1 = [0, 0, 0]
    f2 = [0, 0, 0]

    for i in range(3):
        if body1.pos[i] > body2.pos[i]:
            f1[i] = -1
            f2[i] = 1
        elif body1.pos[i] < body2.pos[i]:
            f1[i] = 1
            f2[i] = -1

    body1.vel = add_vectors(body1.vel, f1)
    body2.vel = add_vectors(body2.vel, f2)

class Body:
    def __init__(self, _pos):
        self.pos = _pos
        self.vel = (0,0,0)

    def update_pos(self):
        self.pos = add_vectors(self.pos, self.vel)

io = Body([-1, 0, 2])
europa = Body([2, -10, -7])
ganymede = Body([4, -8, 8])
callisto = Body([3, 5, -1])

#io = Body([10, 10, 13])
#europa = Body([5, 5, -9])
#ganymede = Body([3, 8, 16])
#callisto = Body([1, 3, -3])

moons = []
moons.append(io)
moons.append(europa)
moons.append(ganymede)
moons.append(callisto)

for i in range(10):
    for moon_pair in list(combinations(moons,2)):
    #for moon_pair in list(zip(moons, moons[1:] + moons[:1])):
        moon1, moon2 = moon_pair
        apply_gravity(moon1, moon2)

    print("After {} steps:".format(i))
    for moon in moons:
        moon.update_pos()
        
        x, y, z = moon.pos
        vx, vy, vz = moon.vel
        print("pos=<x={}, y={}, z={}>, vel=<x={}, y={}, z={}>".format(x, y, z, vx, vy, vz))
    print("")
