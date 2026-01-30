import ipywidgets as widgets
import ipyvuetify as v


class OverviewPanelWidget(widgets.VBox):
    def __init__(self):
        self.overview = v.Html(
            tag="div",
            class_="palette-note",
            children=["Overview panel canvas will render here."],
        )

        card = v.Card(
            children=[
                v.Container(children=[self.overview], fluid=True),
            ],
            class_="palette-card",
        )

        super().__init__([card])
        self.add_class("palette-overview-panel")
