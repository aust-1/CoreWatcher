import tkinter as tk

from .utils import value_to_color

STAT_NAMES = ["cpu", "gpu", "vram"]
GAUGE_WIDTH = 24
GAUGE_HEIGHT = 100


class VerticalGauge(tk.Canvas):
    def __init__(
        self,
        parent: tk.Widget,
        name: str,
        width: int = GAUGE_WIDTH,
        height: int = GAUGE_HEIGHT,
    ) -> None:
        super().__init__(parent, width=width, height=height, highlightthickness=0)
        self.name = name
        self.bar = self.create_rectangle(0, height, width, height, fill="green")

    def update_value(self, value: float) -> None:
        height = int(self.winfo_height() * (1 - min(value / 100, 1)))
        color = value_to_color(value)
        self.coords(self.bar, 0, height, GAUGE_WIDTH, GAUGE_HEIGHT)
        self.itemconfig(self.bar, fill=color)


def create_ui() -> tuple[tk.Tk, dict[str, VerticalGauge]]:
    root = tk.Tk()
    root.title("Core Watcher")
    root.resizable(width=False, height=False)

    # Position the window at bottom right of screen
    root.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 150
    window_height = 150
    x = screen_width - window_width - 10
    y = screen_height - window_height - 60
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    root.overrideredirect(True)
    root.wm_attributes("-topmost", True)

    # Create main frame
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Create close button frame at the top
    close_frame = tk.Frame(main_frame)
    close_frame.pack(fill=tk.X, padx=2, pady=2)

    # Add close button (red X)
    close_button = tk.Button(
        close_frame,
        text="✕",
        fg="white",
        bg="red",
        font=("Arial", 8, "bold"),
        width=2,
        height=1,
        relief="flat",
        command=root.quit
    )
    close_button.pack(side=tk.RIGHT)

    frame = tk.Frame(main_frame)
    frame.pack(padx=1, pady=1)

    gauges: dict[str, VerticalGauge] = {}
    for i, name in enumerate(STAT_NAMES):
        gauge = VerticalGauge(frame, name)
        gauge.grid(row=1, column=i, padx=5)
        gauges[name] = gauge

    for i, name in enumerate(STAT_NAMES):
        tk.Label(frame, text=name.upper(), font=("Arial", 8)).grid(row=2, column=i)

    return root, gauges
