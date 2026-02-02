import ipywidgets as widgets
import ipyvuetify as v


class BasicGenerationWidget(widgets.VBox):
    def __init__(self):
        self.input_colors = v.Textarea(
            label="Show colors in palette (one per line)",
            placeholder="#0ea5e9\n#22c55e\noklch(72% 0.12 340)\n...",
            rows=4,
        )
        self.apply_input = v.Btn(children=["Apply input to palette"], class_="palette-pill-button")
        self.generate_from_initial = v.Btn(
            children=["Generate from initial (even hues)"],
            color="primary",
            class_="palette-pill-button",
        )
        self.generate_random = v.Btn(children=["Generate randomly (even hues)"], class_="palette-pill-button")
        self.add_next = v.Btn(children=["Add next (respect L C H ranges, min Δ)"], class_="palette-pill-button")

        card = v.Card(
            children=[
                v.Container(
                    children=[
                        self.input_colors,
                        v.Html(tag="div", class_="palette-btnbar", children=[self.apply_input]),
                        v.Html(
                            tag="div",
                            class_="palette-btnbar",
                            children=[self.generate_from_initial, self.generate_random, self.add_next],
                        ),
                    ],
                    fluid=True,
                )
            ],
            class_="palette-card",
        )

        super().__init__([card])
        self.add_class("palette-basic-generation")
