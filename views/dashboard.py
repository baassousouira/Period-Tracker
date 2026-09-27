import customtkinter as ctk

from widgets.sidebar import Sidebar
from widgets.cards import InfoCard
from views.add_period import AddPeriodWindow


class Dashboard(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Configuration de la grille principale
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = Sidebar(self)
        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        # Contenu principal
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=20,
            pady=20
        )

        # Titre
        title = ctk.CTkLabel(
            self.main_frame,
            text="🌺 Mon Cycle",
            font=("Arial", 30, "bold")
        )
        title.pack(pady=20)

        # Conteneur des cartes
        cards_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent"
        )
        cards_frame.pack(
            fill="x",
            padx=20,
            pady=20
        )

        cards_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # Carte 1
        cycle_card = InfoCard(
            cards_frame,
            "Cycle actuel",
            "Jour 12"
        )

        cycle_card.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        # Carte 2
        next_period_card = InfoCard(
            cards_frame,
            "Prochaines règles",
            "11 Oct."
        )

        next_period_card.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        # Carte 3
        average_card = InfoCard(
            cards_frame,
            "Durée moyenne",
            "29 jours"
        )

        average_card.grid(
            row=0,
            column=2,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        # Bouton d'ajout
        add_button = ctk.CTkButton(
            self.main_frame,
            text="+ Ajouter une période",
            width=220,
            height=40,
            command=self.open_add_period_window
        )

        add_button.pack(pady=30)

    def open_add_period_window(self):
        AddPeriodWindow(self)