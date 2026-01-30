import ipywidgets as widgets
import ipyvuetify as v


class TextPreviewWidget(widgets.VBox):
    def __init__(self):
        self.preview = v.Html(
            tag="div",
            class_="palette-sample-text",
            children=["Sample preview text goes here."],
        )

        card = v.Card(
            children=[
                v.Container(children=[self.preview], fluid=True),
            ],
            class_="palette-card",
        )

        super().__init__([card])
        self.add_class("palette-text-preview")
