import customtkinter as ctk

from views.dashboard import Dashboard

class PeriodTrackerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Fenêtre
        self.title("🌺 Period Tracker")
        self.geometry("1200x800")
        self.resizable(True, True)
        self.minsize(800,600)

        # Dashboard
        self.dashboard = Dashboard(self)
        self.dashboard.pack(fill="both", expand=True)


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = PeriodTrackerApp()
    app.mainloop()