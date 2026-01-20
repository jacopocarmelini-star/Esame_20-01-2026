import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_create_graph(self, e):

        try:
            n_album = int(self._view.txtNumAlbumMin.value)
            if n_album < 1:
                self._view.show_alert("Selezionare un numero valido di album")
                return
        except ValueError:
            self._view.show_alert("Selezionare un numero valido di album")
            return



        self._model.load_artists_with_min_albums(n_album)

        self._model.build_graph()
        self._view.ddArtist.disabled = False
        self.fill_dd()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato: {self._model._graph.number_of_nodes()} (artisti),  {self._model._graph.number_of_edges()} archi "))
        self._view._page.update()

    def fill_dd(self):
        self._view.btnArtistsConnected.disabled = False

        self._view.ddArtist.options.clear()
        for n in self._model._graph.nodes:
            self._view.ddArtist.options.append(ft.dropdown.Option(key=n.id, text=n.name))
        self._view._page.update()




    def handle_connected_artists(self, e):

        artista_scelto = int(self._view.ddArtist.value)
        self._view.txt_result.controls.clear()

        vicini_ord  = self._model.find_vicini(artista_scelto)
        self._view.txt_result.controls.append(ft.Text(f"Artisti direttamente collegati all'artista{artista_scelto}"))
        for v in vicini_ord:
            self._view.txt_result.controls.append(ft.Text(f"{v[0]}, {v[1]} - Numero di generi in comune {v[2]}"))
        self._view._page.update()

    def handle_cammino(self,e):

        try:
            durata_min = float(self._view.txtMinDuration.value)
            n_arte = int(self._view.txtMaxArtists.value)
        except ValueError:
            self._view.show_alert("Selezionare un numero valido di album")
            return



