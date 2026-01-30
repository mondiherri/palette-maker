import ipywidgets as widgets
import ipyvuetify as v


class PaletteGridWidget(widgets.VBox):
    def __init__(self):
        self.grid_placeholder = v.Html(
            tag="div",
            class_="palette-note",
            children=["Palette swatches will render here."],
        )

        card = v.Card(
            children=[
                v.Container(children=[self.grid_placeholder], fluid=True),
            ],
            class_="palette-card",
        )

        super().__init__([card])
        self.add_class("palette-grid")
