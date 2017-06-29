class Network:
    def __init__(self):
        self.members = {}
        self.sources = {}

    def get_member_by_title(self, title):
        return self.members.get(title)

    def get_source_by_title(self, title):
        return self.sources.get(title)

    def append_source(self, other):
        self.sources[other.__str__()] = other
        self.members[other.__str__()] = other

    def append_member(self, other):
        self.members[other.__str__()] = other

    def __str__(self):
        reprs = ""
        for member in self.members.values():
            relation = member.__str__() + " || "
            # for child in member.get_outgoing_neighbours()[:-1]:
            #     relation += child.__str__() + " <-> "
            # if member.get_outgoing_neighbours():
            #     relation += member.get_outgoing_neighbours()[-1].__str__() + "\n"
            reprs += relation
        return reprs

    def get_members(self):
        return self.members

class Node:
    def __init__(self, title):
        self._title = title
        self.outgoing_neighbours = []

    def append(self, neighbour):
        self.outgoing_neighbours.append(neighbour)

    def append_all(self, all_neighbours):
        for el in all_neighbours:
            self.outgoing_neighbours.append(el)

    def get_n_order_neighbours(self, order):
        current_parent = self
        all_set = current_parent.outgoing_neighbours
        frontier = current_parent.outgoing_neighbours
        for _ in xrange(order - 1):
            level_frontier_size = len(frontier)
            count = 0
            while count != level_frontier_size:
                if frontier.pop(0).__str__() != self._title:
                    to_visit = network.get_member_by_title(frontier.pop(0).__str__())

                    count += 1
                    neighbours = to_visit.get_outgoing_neighbours()
                    for neigh in neighbours:
                        if neigh not in all_set:
                            all_set.append(neigh)
                            frontier.append(neigh)

        return list(set(all_set))

    def get_outgoing_neighbours(self):
        return self.outgoing_neighbours

    def __str__(self):
        return self._title


f = open("network.txt", "r")
content = f.readlines()
i = 0
sources = 0
network = Network()
source = None

while sources != 1100:
    _ = content[i]
    if "++" in content[i]:
        source = Node(content[i].replace("++","").replace("\n",""))
        network.append_source(source)
        sources +=1

    else:
        neigh = network.get_member_by_title(content[i].replace("\n",""))
        if not neigh:
            neigh = Node(content[i].replace("\n",""))
            network.append_member(neigh)
        source.append(neigh)
    i+=1

print len(network.get_source_by_title("Radiohead").get_n_order_neighbours(3))

# import draw_newtork

# drawing = draw_newtork.DrawBoard(network)
#
# drawing.create_graph()
# drawing.draw_graph()

# for el in a.get_n_order_neighbours(3):
#     print el
