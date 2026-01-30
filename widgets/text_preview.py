import ipywidgets as widgets
import ipyvuetify as v


SAMPLE_TEXT_HTML = """
<div class="palette-sample-text">
  <p>
    The <span data-color-index="0" style="background: #f6c453;">sunrise</span>
    warms the
    <span data-color-index="1" style="background: #2f9ee0; color: #fff;">sky</span>
    while the
    <span data-color-index="2" style="background: #1f7a5e; color: #fff;">forest</span>
    stays calm.
  </p>
  <p>
    Balance bold accents like
    <span data-color-index="3" style="background: #d66fb8;">blush</span>
    with neutrals for harmonious palettes.
  </p>
</div>
"""


class TextPreviewWidget(widgets.VBox):
    def __init__(self):
        self.preview = v.Html(tag="div", children=[SAMPLE_TEXT_HTML])

        card = v.Card(
            children=[
                v.Container(children=[self.preview], fluid=True),
            ],
            class_="palette-card palette-highlight-card",
        )

        super().__init__([card])
        self.add_class("palette-text-preview")
