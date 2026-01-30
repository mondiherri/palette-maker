import ipywidgets as widgets
import ipyvuetify as v


SWATCHES_HTML = """
<div class="grid">
  <div class="palette-swatch" style="background: #f6c453; color: #111;">
    <div class="palette-swatch-title">Sunrise</div>
    <div class="palette-swatch-meta">
      <div>HEX: #f6c453</div>
      <div>OKLCH: 84% 0.14 96</div>
    </div>
  </div>
  <div class="palette-swatch" style="background: #2f9ee0; color: #fff;">
    <div class="palette-swatch-title">Skylight</div>
    <div class="palette-swatch-meta">
      <div>HEX: #2f9ee0</div>
      <div>OKLCH: 65% 0.18 242</div>
    </div>
  </div>
  <div class="palette-swatch" style="background: #1f7a5e; color: #fff;">
    <div class="palette-swatch-title">Forest</div>
    <div class="palette-swatch-meta">
      <div>HEX: #1f7a5e</div>
      <div>OKLCH: 54% 0.12 162</div>
    </div>
  </div>
  <div class="palette-swatch" style="background: #d66fb8; color: #111;">
    <div class="palette-swatch-title">Blush</div>
    <div class="palette-swatch-meta">
      <div>HEX: #d66fb8</div>
      <div>OKLCH: 72% 0.17 340</div>
    </div>
  </div>
</div>
"""


class PaletteGridWidget(widgets.VBox):
    def __init__(self):
        self.grid = v.Html(tag="div", children=[SWATCHES_HTML])

        card = v.Card(
            children=[
                v.Container(children=[self.grid], fluid=True),
            ],
            class_="palette-card palette-grid-card",
        )

        super().__init__([card])
        self.add_class("palette-grid")
