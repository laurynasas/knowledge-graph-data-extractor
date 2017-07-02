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
            reprs += relation
        return reprs

    def get_members(self):
        return self.members

class Song:
    def __init__(self, title):
        self._title = title

class Node:
    def __init__(self, title):
        self._title = title
        self.outgoing_neighbours = []
        self.incoming_neighbours = []
        self.songs =[]

    def append_outcoming(self, neighbour):
        self.outgoing_neighbours.append(neighbour)

    def append_incoming(self, neighbour):
        self.incoming_neighbours.append(neighbour)

    def append_song(self, song):
        self.songs.append(song)

    def append_all(self, all_neighbours):
        for el in all_neighbours:
            self.outgoing_neighbours.append(el)

    def get_n_order_neighbours(self, order, network, all_set=None, frontier=None):
        if not all_set:
            all_set = {}
        if not frontier:
            frontier = self.get_outgoing_neighbours()
        if order == 0:
            return all_set
        else:
            future_frontier = []
            for el in frontier:
                future_frontier.extend(network.get_member_by_title(el.get_title()).get_outgoing_neighbours())
                if not all_set.get(el.get_title()):
                    all_set[el.get_title()] = el
            return self.get_n_order_neighbours(order-1, network, all_set, future_frontier)

    def get_outgoing_neighbours(self):
        return self.outgoing_neighbours

    def get_incoming_neighbours(self):
        return self.incoming_neighbours

    def __str__(self):
        return self._title

    def get_title(self):
        return self._title

    def print_top_songs(self, n):
        print_string = ""
        for song in self.songs[:n]:
            print_string += song._title + " | "
        return print_string


f = open("network.txt", "r")
songs = open("songs_alread_visited.txt","r")
songs_content = songs.readlines()
content = f.readlines()
i = 0
sources = 0
network = Network()
source = None
number_sources = 20000

while sources != number_sources:
    _ = content[i]
    if "++" in content[i]:
        source = Node(content[i].replace("++", "").replace("\n", ""))
        network.append_source(source)
        sources += 1

    else:
        neigh = network.get_member_by_title(content[i].replace("\n", ""))
        if not neigh:
            neigh = Node(content[i].replace("\n", ""))
            network.append_member(neigh)
        neigh.append_incoming(source)
        source.append_outcoming(neigh)
    i += 1

sources = 0
i=0
while sources != number_sources:
    title = songs_content[i].replace("\n", "")
    if "++" in title:
        title = title.replace("++","")
        source = network.get_member_by_title(title)
    else:
        song = Song(title)
        source.append_song(song)
    sources+=1
    i+=1


print network.get_source_by_title("Green Day").print_top_songs(3)
a = network.get_source_by_title("Jon Hopkins").get_n_order_neighbours(2, network)
b = network.get_source_by_title("Radiohead").get_n_order_neighbours(2, network)
print len(a)
print len(b)

inter = []

for a_band in a:
    if a_band in b:
        inter.append(a[a_band])

print len(inter)
print [el.get_title() for el in inter]

links = [len(el.get_incoming_neighbours()) for el in inter]
print links

links, bands = zip(*sorted(zip(links, inter), reverse=True))

print links
print [el.get_title() + " = " + el.print_top_songs(2) for el in bands[:5]]
# import draw_newtork

# drawing = draw_newtork.DrawBoard(network)
#
# drawing.create_graph()
# drawing.draw_graph()

# for el in a.get_n_order_neighbours(3):
#     print el
