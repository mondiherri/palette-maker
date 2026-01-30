import ipywidgets as widgets
import ipyvuetify as v


class PaletteConstraintsWidget(widgets.VBox):
    def __init__(self):
        self.target_size = v.TextField(
            label="Target palette size",
            type="number",
            min=1,
            max=200,
            step=1,
            value=25,
        )
        self.initial_color = v.TextField(
            label="Starting color (CSS or Hex)",
            placeholder="oklch(60% 0.12 30)",
            value="oklch(99.3% 0.2 104.3)",
        )
        self.min_distance = v.TextField(
            label="Min Δ (OKLCH)",
            type="number",
            step=0.001,
            min=0,
            max=1,
            value=0.14,
        )
        self.l_min = v.TextField(label="L min", type="number", step=1, value=30)
        self.l_max = v.TextField(label="L max", type="number", step=1, value=99)
        self.c_min = v.TextField(label="C min", type="number", step=0.005, value=0.06)
        self.c_max = v.TextField(label="C max", type="number", step=0.005, value=0.4)
        self.exclude_colors = v.Textarea(
            label="Exclude colors (one per line)",
            placeholder="#000000\noklch(90% 0.02 0)\n...",
            rows=3,
        )
        self.hue_ex_start = v.TextField(label="Exclude hue start (deg)")
        self.hue_ex_end = v.TextField(label="Exclude hue end (deg)")
        self.srgb_gamut = v.Checkbox(label="Show in sRGB Gamut", v_model=True)

        left_row = v.Row(
            children=[
                v.Col(children=[self.target_size], cols=6),
                v.Col(children=[self.initial_color], cols=6),
            ],
            class_="palette-row",
        )
        min_row = v.Row(children=[v.Col(children=[self.min_distance], cols=6)], class_="palette-row")
        range_row = v.Row(
            children=[
                v.Col(children=[self.l_min, self.l_max, v.Html(tag="div", class_="palette-note", children=["Enter % (0–100). Internally 0–1."])], cols=6),
                v.Col(children=[self.c_min, self.c_max, v.Html(tag="div", class_="palette-note", children=["Typical ~0–0.4 for OKLCH."])], cols=6),
            ],
            class_="palette-row",
        )
        exclude_row = v.Row(
            children=[
                v.Col(children=[self.exclude_colors], cols=6),
                v.Col(
                    children=[
                        self.hue_ex_start,
                        self.hue_ex_end,
                        v.Html(
                            tag="div",
                            class_="palette-note",
                            children=[
                                "Wrap-around supported (e.g., 300 → 40 excludes reds).",
                                "Excluded colors are skipped when generating.",
                            ],
                        ),
                    ],
                    cols=6,
                ),
            ],
            class_="palette-row",
        )
        s_rgb_row = v.Row(
            children=[
                v.Col(
                    children=[
                        self.srgb_gamut,
                        v.Html(
                            tag="div",
                            class_="palette-note",
                            children=[
                                "Only RGB can be defined in some software.",
                                "Uncheck to see OKLCH colors.",
                            ],
                        ),
                    ],
                    cols=6,
                ),
            ],
            class_="palette-row",
        )

        card = v.Card(
            children=[
                v.Container(
                    children=[
                        v.Html(tag="div", class_="palette-controls", children=[left_row, min_row, range_row, exclude_row, s_rgb_row]),
                    ],
                    fluid=True,
                )
            ],
            class_="palette-card",
        )

        super().__init__([card])
        self.add_class("palette-controls-widget")
