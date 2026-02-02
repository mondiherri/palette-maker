from __future__ import annotations

import json
import ipywidgets as widgets
import ipyvuetify as v
from traitlets import Bool, Float, Unicode


class ColorSwatchWidget(widgets.DOMWidget):
    _view_name = Unicode("ColorSwatchView").tag(sync=True)
    _view_module = Unicode("palette-ui").tag(sync=True)
    _view_module_version = Unicode("0.0.1").tag(sync=True)

    l = Float(60.0).tag(sync=True)
    c = Float(0.12).tag(sync=True)
    h = Float(200.0).tag(sync=True)
    title = Unicode("Generated").tag(sync=True)
    show_controls = Bool(True).tag(sync=True)
    swatch_text = Unicode("").tag(sync=True)

    def __init__(self, *, l: float = 60.0, c: float = 0.12, h: float = 200.0, title: str = "Generated") -> None:
        super().__init__()
        self.l = l
        self.c = c
        self.h = h
        self.title = title

    def set_color(self, l: float, c: float, h: float) -> None:
        self.l = l
        self.c = c
        self.h = h

    def as_dict(self) -> dict[str, float]:
        return {"l": self.l, "c": self.c, "h": self.h}

    def to_json(self) -> str:
        return json.dumps(self.as_dict())


class ColorSwatchPanel(widgets.VBox):
    def __init__(self):
        self.widget = ColorSwatchWidget()

        card = v.Card(
            children=[
                v.Container(
                    children=[
                        v.Html(tag="div", class_="palette-note", children=["Custom color swatch widget:"]),
                        self.widget,
                    ],
                    fluid=True,
                )
            ],
            class_="palette-card",
        )
        super().__init__([card])
        self.add_class("palette-color-swatch")
