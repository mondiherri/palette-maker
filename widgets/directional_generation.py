import ipywidgets as widgets
import ipyvuetify as v


class DirectionalGenerationWidget(widgets.VBox):
    def __init__(self):
        self.hue_window = v.TextField(label="Direction window (± degrees)", type="number", min=1, max=180, value=15)
        self.hue_slider = v.Slider(label="Directional hue (0–360° OKLCH)", min=0, max=360, step=1, value=200)
        self.dir_l = v.Slider(label="Directional Lightness (L)", min=0, max=100, step=1, value=60)
        self.dir_c = v.Slider(label="Directional Chroma (C)", min=0, max=0.4, step=0.005, value=0.12)
        self.add_next = v.Btn(children=["Add next (directional)"], class_="palette-pill-button")

        card = v.Card(
            children=[
                v.Container(
                    children=[
                        v.Html(tag="div", class_="palette-note", children=["Directional preview goes here."]),
                        self.hue_window,
                        self.hue_slider,
                        self.dir_l,
                        self.dir_c,
                        v.Html(tag="div", class_="palette-btnbar", children=[self.add_next]),
                    ],
                    fluid=True,
                )
            ],
            class_="palette-card",
        )

        super().__init__([card])
        self.add_class("palette-directional-generation")
