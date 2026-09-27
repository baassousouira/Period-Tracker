import customtkinter as ctk


class InfoCard(ctk.CTkFrame):
    def __init__(self, parent, title, value):
        super().__init__(
            parent,
            corner_radius=20,
            border_width=1,
            fg_color=("#f4f4f4", "#2b2b2b")
        )

        # Taille minimale de la carte
        self.configure(height=160)

        title_label = ctk.CTkLabel(
            self,
            text=title,
            font=("Arial", 18, "bold"),
            anchor="w"
        )

        title_label.pack(
            fill="x",
            padx=30,
            pady=(25, 10)
        )

        value_label = ctk.CTkLabel(
            self,
            text=value,
            font=("Arial", 32, "bold"),
            anchor="w"
        )

        value_label.pack(
            fill="x",
            padx=30,
            pady=(0, 25)
        )