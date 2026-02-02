(() => {
  const clamp = (value, min, max) => Math.min(max, Math.max(min, value));

  function formatOklch(l, c, h) {
    return `oklch(${l.toFixed(1)}% ${c.toFixed(3)} ${Math.round(h)}deg)`;
  }

  function textColorForL(l) {
    return l > 62 ? "#111" : "#fff";
  }

  function defineModule(widgets) {
    class ColorSwatchView extends widgets.DOMWidgetView {
      render() {
        this.el.classList.add("palette-swatch-widget");
        this.el.innerHTML = "";

        this.headerEl = document.createElement("div");
        this.headerEl.className = "palette-swatch-header";

        this.titleEl = document.createElement("div");
        this.titleEl.className = "palette-swatch-title";
        this.headerEl.appendChild(this.titleEl);

        this.valueEl = document.createElement("div");
        this.valueEl.className = "palette-swatch-value";
        this.headerEl.appendChild(this.valueEl);

        this.swatchEl = document.createElement("div");
        this.swatchEl.className = "palette-swatch-preview";

        this.controlsEl = document.createElement("div");
        this.controlsEl.className = "palette-swatch-controls";

        this.el.appendChild(this.headerEl);
        this.el.appendChild(this.swatchEl);
        this.el.appendChild(this.controlsEl);

        this.renderControls();
        this.updateFromModel();

        this.model.on("change:l change:c change:h change:title change:show_controls change:swatch_text", () => {
          this.updateFromModel();
        });
      }

      renderControls() {
        const configs = [
          { key: "l", label: "L", min: 0, max: 100, step: 0.1 },
          { key: "c", label: "C", min: 0, max: 0.4, step: 0.001 },
          { key: "h", label: "H", min: 0, max: 360, step: 1 },
        ];
        this.controlsEl.innerHTML = "";
        this.sliders = {};

        configs.forEach((config) => {
          const row = document.createElement("label");
          row.className = "palette-swatch-control";

          const label = document.createElement("span");
          label.className = "palette-swatch-control-label";
          label.textContent = config.label;

          const input = document.createElement("input");
          input.type = "range";
          input.min = String(config.min);
          input.max = String(config.max);
          input.step = String(config.step);

          const value = document.createElement("span");
          value.className = "palette-swatch-control-value";

          input.addEventListener("input", (event) => {
            const numeric = parseFloat(event.target.value);
            const next = clamp(numeric, config.min, config.max);
            this.model.set(config.key, next);
            this.model.save_changes();
          });

          row.appendChild(label);
          row.appendChild(input);
          row.appendChild(value);

          this.controlsEl.appendChild(row);
          this.sliders[config.key] = { input, value, config };
        });
      }

      updateFromModel() {
        const l = clamp(Number(this.model.get("l") || 0), 0, 100);
        const c = clamp(Number(this.model.get("c") || 0), 0, 0.4);
        const h = clamp(Number(this.model.get("h") || 0), 0, 360);
        const title = this.model.get("title") || "Generated";
        const swatchText = this.model.get("swatch_text") || "";
        const showControls = this.model.get("show_controls");

        this.titleEl.textContent = title;
        this.valueEl.textContent = formatOklch(l, c, h);

        this.swatchEl.style.background = `oklch(${l}% ${c} ${h})`;
        this.swatchEl.style.color = textColorForL(l);
        this.swatchEl.textContent = swatchText;

        this.controlsEl.style.display = showControls ? "grid" : "none";

        if (this.sliders) {
          Object.entries(this.sliders).forEach(([key, { input, value }]) => {
            const current = key === "l" ? l : key === "c" ? c : h;
            input.value = String(current);
            value.textContent = key === "l"
              ? `${current.toFixed(1)}%`
              : key === "c"
                ? current.toFixed(3)
                : `${Math.round(current)}°`;
          });
        }
      }
    }

    return { ColorSwatchView };
  }

  if (typeof define === "function" && define.amd) {
    define("palette-ui", ["@jupyter-widgets/base"], defineModule);
  } else if (window.jupyterWidgetsBase) {
    window.PaletteUI = window.PaletteUI || {};
    window.PaletteUI.widgets = defineModule(window.jupyterWidgetsBase);
  }
})();
