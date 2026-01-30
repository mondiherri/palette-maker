import ipywidgets as widgets
import ipyvuetify as v


class PreviewSettingsWidget(widgets.VBox):
    def __init__(self):
        self.preview_font = v.Select(
            label="Preview font",
            items=["System", "Serif", "Mono"],
            v_model="System",
        )
        self.preview_font_size = v.TextField(label="Font size", type="number", min=10, max=28, value=13)
        self.preview_line_height = v.TextField(label="Line height", type="number", min=1.0, max=2.0, value=1.55)
        self.preview_background = v.TextField(label="Background (hex)", value="#fdfdf9")
        self.randomize_text = v.Btn(children=["Randomize text"], class_="palette-pill-button")

        card = v.Card(
            children=[
                v.Container(
                    children=[
                        self.preview_font,
                        self.preview_font_size,
                        self.preview_line_height,
                        self.preview_background,
                        v.Html(tag="div", class_="palette-btnbar", children=[self.randomize_text]),
                    ],
                    fluid=True,
                )
            ],
            class_="palette-card",
        )

        super().__init__([card])
        self.add_class("palette-preview-settings")
