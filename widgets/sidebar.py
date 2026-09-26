import customtkinter as ctk


class Sidebar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=220, corner_radius=0)

        self.grid_rowconfigure(5, weight=1)

        # Logo
        logo = ctk.CTkLabel(
            self,
            text="🌺 Period Tracker",
            font=("Arial", 20, "bold")
        )
        logo.grid(row=0, column=0, padx=20, pady=(25, 30))

        # Boutons
        self.home_button = ctk.CTkButton(
            self,
            text="🏠 Accueil"
        )
        self.home_button.grid(
            row=1,
            column=0,
            padx=20,
            pady=10,
            sticky="ew"
        )

        self.calendar_button = ctk.CTkButton(
            self,
            text="📅 Calendrier"
        )
        self.calendar_button.grid(
            row=2,
            column=0,
            padx=20,
            pady=10,
            sticky="ew"
        )

        self.stats_button = ctk.CTkButton(
            self,
            text="📊 Statistiques"
        )
        self.stats_button.grid(
            row=3,
            column=0,
            padx=20,
            pady=10,
            sticky="ew"
        )

        self.settings_button = ctk.CTkButton(
            self,
            text="⚙️ Paramètres"
        )
        self.settings_button.grid(
            row=4,
            column=0,
            padx=20,
            pady=10,
            sticky="ew"
        )