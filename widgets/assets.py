from pathlib import Path

from IPython.display import HTML, display


ASSETS_ROOT = Path(__file__).resolve().parent.parent / "assets"


def load_assets() -> None:
    css_path = ASSETS_ROOT / "css" / "palette-ui.css"
    js_root = ASSETS_ROOT / "js"

    css_tag = f"<style>{css_path.read_text(encoding='utf-8')}</style>" if css_path.exists() else ""
    js_tags = []
    if js_root.exists():
        for js_path in sorted(js_root.glob("*.js")):
            js_tags.append(f"<script>{js_path.read_text(encoding='utf-8')}</script>")

    html = css_tag + "".join(js_tags)
    if html:
        display(HTML(html))
