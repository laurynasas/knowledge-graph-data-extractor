from graphviz import Graph



class DrawBoard:
    def __init__(self, network):
        self._network = network

    def create_graph(self):
        self.dot = Graph(comment='Musicians',node_attr={'width':'0.5'}, engine="fdp")

        for member in self._network.get_members().values():
            self.dot.node(member.__str__().decode('utf8'))
            for neigh in member.get_outgoing_neighbours():
                self.dot.node(neigh.__str__().decode('utf8'))
                self.dot.edge(member.__str__().decode('utf8'), neigh.__str__().decode('utf8'),  constraint='true')

    def draw_graph(self):
        self.dot.format = 'pdf'
        self.dot.view('test-output/musicians_dot.gv')


