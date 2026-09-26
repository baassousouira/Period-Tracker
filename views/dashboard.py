import customtkinter as ctk

from widgets.sidebar import Sidebar


class Dashboard(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = Sidebar(self)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        # Contenu principal
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=20,
            pady=20
        )

        title = ctk.CTkLabel(
            self.main_frame,
            text="🌺 Mon Cycle",
            font=("Arial", 30, "bold")
        )
        title.pack(pady=20)

        cycle_label = ctk.CTkLabel(
            self.main_frame,
            text="Cycle actuel : inconnu",
            font=("Arial", 16)
        )
        cycle_label.pack(pady=10)

        next_period_label = ctk.CTkLabel(
            self.main_frame,
            text="Prochaines règles : inconnues",
            font=("Arial", 16)
        )
        next_period_label.pack(pady=10)

        add_button = ctk.CTkButton(
            self.main_frame,
            text="Ajouter une période"
        )
        add_button.pack(pady=20)