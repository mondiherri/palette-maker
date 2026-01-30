from pathlib import Path


ASSETS_ROOT = Path(__file__).resolve().parent.parent / "assets"


def load_assets() -> None:
    from IPython.display import HTML, display

    css_path = ASSETS_ROOT / "css" / "palette-ui.css"
    js_path = ASSETS_ROOT / "js" / "palette-ui.js"

    css_tag = f"<style>{css_path.read_text(encoding='utf-8')}</style>" if css_path.exists() else ""
    js_tag = f"<script>{js_path.read_text(encoding='utf-8')}</script>" if js_path.exists() else ""

    if css_tag or js_tag:
        display(HTML(css_tag + js_tag))
