import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._artists_list = []
        self._lista_artisti_n_album = []
        self._lista_pesi = []
        self._id_map = {}

        self.load_pesi()
        self.load_all_artists()

    def load_all_artists(self):
        self._artists_list = DAO.get_all_artists()
        print(f"Artisti: {self._artists_list}")

    def load_artists_with_min_albums(self, min_albums):
        self._lista_artisti_n_album  = DAO.get_artisti_n_album(min_albums)

    def load_pesi(self):
        self._lista_pesi = DAO.get_peso()



    def build_graph(self):
        self._graph.clear()
        for a in self._lista_artisti_n_album:
            self._id_map[a.id] = a
            self._graph.add_node(a)
        for c in self._lista_pesi:
            if c.a1_id in self._id_map and c.a2_id in self._id_map:
                a1 = self._id_map[c.a1_id]
                a2 = self._id_map[c.a2_id]
                self._graph.add_edge(a1, a2, weight=c.peso)
        print(self._lista_pesi)

    def find_vicini(self, artista_scelto):
        artista = self._id_map[artista_scelto]
        vicini = []
        lista = []
        for n in self._graph.neighbors(artista):
            vicini.append(n.id)
        for u, v, w in self._graph.edges(artista, data=True):
            for n in vicini:
                if v.id==n:
                    lista.append((v.id, v.name, w))
        vicini_ord = sorted(lista, key=lambda x: x[0])
        return vicini_ord






