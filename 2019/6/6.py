input = []
with open('input.txt') as fp:
# with open('input_test.txt') as fp:
    for line in fp:
        input.append([line.split(')')[0], line.split(')')[1][:-1]])

class Tree():
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []
        self.nb_orbits = 0

    def set_parent(self, parent):
        self.parent = parent
        parent.children.append(self)

    def reannotate(self, nb_orbits):
        self.nb_orbits += nb_orbits
        for child in self.children:
            child.reannotate(self.nb_orbits + 1)

planet_dict = {}

for connection in input:
    if connection[0] not in planet_dict:
        planet_dict[connection[0]] = Tree(connection[0])
    if connection[1] not in planet_dict:
        planet_dict[connection[1]] = Tree(connection[1])
    planet_dict[connection[1]].set_parent(planet_dict[connection[0]])

for planet, planet_obj in planet_dict.items():
    if planet_obj.parent is None:
        planet_obj.reannotate(0)

total_orbits = 0
for planet, planet_obj in planet_dict.items():
    total_orbits += planet_obj.nb_orbits

# part 1 135690
print(total_orbits)

my_planet = planet_dict['YOU']
santa_planet = planet_dict['SAN']

rang = 0
planet_dist = {}
planet = my_planet
while planet is not None:
    planet_dist[planet.name] = rang
    rang += 1
    planet = planet.parent

rang = 0
planet = santa_planet
dist = -1
while planet is not None:
    # planet_dist[planet.name] = rang
    if planet.name in planet_dist:
        dist = planet_dist[planet.name] + rang
        break
    rang += 1
    planet = planet.parent

# part 2 298
print(dist - 2)