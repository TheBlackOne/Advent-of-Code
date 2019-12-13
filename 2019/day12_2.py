from itertools import combinations
import numpy as np

def add_vectors(v1, v2):
    return list(map(lambda x, y: x + y, v1, v2))

def get_vector_sum(vec):
    return sum([abs(ele) for ele in vec])

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
    vel1 = add_vectors(body1.vel, f1)
    vel2 = add_vectors(body2.vel, f2)
    body1.vel = vel1
    body2.vel = vel2

class Body:
    def __init__(self, _pos):
        self.pos = _pos
        self.vel = (0,0,0)

    def update_pos(self):
        self.pos = add_vectors(self.pos, self.vel)
    
    def get_kin_energy(self):
        return get_vector_sum(self.vel)

    def get_pot_energy(self):
        return get_vector_sum(self.pos)

    def __eq__(self, other):
        return self.pos[0] == other.pos[0]

#io = Body([-1, 0, 2])
#europa = Body([2, -10, -7])
#ganymede = Body([4, -8, 8])
#callisto = Body([3, 5, -1])

io = Body([-10, -10, -13])
europa = Body([5, 5, -9])
ganymede = Body([3, 8, -16])
callisto = Body([1, 3, -3])

#io = Body([-8, -10, 0])
#europa = Body([5, 5, 10])
#ganymede = Body([2, -7, 3])
#callisto = Body([9, -8, -3])

moons = []
moons.append(io)
moons.append(europa)
moons.append(ganymede)
moons.append(callisto)

i = 1

freq_x, freq_y, freq_z = None, None, None
statesx = [(io.pos[0], io.vel[0]), (europa.pos[0], europa.vel[0]), (ganymede.pos[0], ganymede.vel[0]), (callisto.pos[0], callisto.vel[0])]
statesy = [(io.pos[1], io.vel[1]), (europa.pos[1], europa.vel[1]), (ganymede.pos[1], ganymede.vel[1]), (callisto.pos[1], callisto.vel[1])]
statesz = [(io.pos[2], io.vel[2]), (europa.pos[2], europa.vel[2]), (ganymede.pos[2], ganymede.vel[2]), (callisto.pos[2], callisto.vel[2])]



while True:
    for moon_pair in list(combinations(moons,2)):
        moon1, moon2 = moon_pair
        apply_gravity(moon1, moon2)
    for moon in moons:
        moon.update_pos()

    current_state_x = []
    current_state_y = []
    current_state_z = []
    for moon in moons:
        current_state_x.append((moon.pos[0], moon.vel[0]))
        current_state_y.append((moon.pos[1], moon.vel[1]))
        current_state_z.append((moon.pos[2], moon.vel[2]))

    if freq_x is None and current_state_x == statesx:
        freq_x = i
        print(freq_x)
    if freq_y is None and current_state_y == statesy:
        freq_y = i
        print(freq_y)
    if freq_z is None and current_state_z == statesz:
        freq_z = i
        print(freq_z)

    if freq_x is not None and freq_y is not None and freq_z is not None:
        break
    
    i += 1

result = np.lcm.reduce([np.uint64(freq_x), np.uint64(freq_y), np.uint64(freq_z)])
print(result)