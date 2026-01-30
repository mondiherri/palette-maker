import ipywidgets as widgets
import ipyvuetify as v


OVERVIEW_HTML = """
<div class="overview-panel">
  <div class="overview-header">
    <div class="overview-chip" style="background: #f6c453;">1</div>
    <div class="overview-chip" style="background: #2f9ee0; color: #fff;">2</div>
    <div class="overview-chip" style="background: #1f7a5e; color: #fff;">3</div>
    <div class="overview-chip" style="background: #d66fb8;">4</div>
  </div>
  <div class="overview-wrap">
    <canvas width="320" height="120"></canvas>
  </div>
</div>
"""


class OverviewPanelWidget(widgets.VBox):
    def __init__(self):
        self.overview = v.Html(tag="div", children=[OVERVIEW_HTML])

        card = v.Card(
            children=[
                v.Container(children=[self.overview], fluid=True),
            ],
            class_="palette-card",
        )

        super().__init__([card])
        self.add_class("palette-overview-panel")
