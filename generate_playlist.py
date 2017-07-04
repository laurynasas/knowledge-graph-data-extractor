import numpy as np

from network import load_network
from song import load_songs

NUMBER_SOURCES = 20000


def get_n_list_intersection(dics):
    lists = []
    inter = []
    for el in dics:
        lists.append(el.keys())
    keyword_inter = list(set(lists[0]).intersection(*lists))

    for key in keyword_inter:
        inter.append(dics[0][key])

    return inter


def chunkify_playlist(playlist, chunk_size):
    return np.array_split(playlist, len(playlist) / chunk_size)


def main():
    network = load_network("resources/network.txt", NUMBER_SOURCES)
    load_songs("resources/songs_already_visited.txt", NUMBER_SOURCES, network)

    print network.get_source_by_title("Green Day").print_top_songs(3)
    a = network.get_source_by_title("Jon Hopkins").get_n_order_neighbours(2, network)
    b = network.get_source_by_title("Radiohead").get_n_order_neighbours(2, network)
    print len(a)
    print len(b)

    inter = get_n_list_intersection([a, b])

    playlist = ["Jon Hopkins", "Radiohead", "Tame Impala", "Bonobo", "Coldplay", "Bon Iver", "Nirvana", "David Bowie",
                "The xx"]

    chunks = chunkify_playlist(playlist, 3)
    for chunk in chunks:
        neighbours = []
        for artist in chunk:
            print artist
            neighbours.append(network.get_source_by_title(artist).get_n_order_neighbours(2, network))
        print get_n_list_intersection(neighbours)

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


if __name__ == "__main__":
    main()
