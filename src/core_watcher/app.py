import tkinter as tk

from .monitor import get_status
from .ui import VerticalGauge, create_ui

REFRESH_MS = 1000


def update_ui(root: tk.Tk, gauges: dict[str, VerticalGauge]) -> None:
    stats = get_status()
    for name, value in stats.items():
        if name in gauges:
            gauges[name].update_value(value)
    root.after(REFRESH_MS, update_ui, root, gauges)


def run_app() -> None:
    root, gauges = create_ui()
    update_ui(root, gauges)
    root.mainloop()
