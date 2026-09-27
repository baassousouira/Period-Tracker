import customtkinter as ctk


class AddPeriodWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Ajouter une période")
        self.geometry("400x350")

        self.grab_set()

        title = ctk.CTkLabel(
            self,
            text="🌸 Nouvelle période",
            font=("Arial", 22, "bold")
        )
        title.pack(pady=(20, 30))

        # Date de début
        start_label = ctk.CTkLabel(
            self,
            text="Date de début"
        )
        start_label.pack(anchor="w", padx=30)

        self.start_entry = ctk.CTkEntry(
            self,
            placeholder_text="JJ/MM/AAAA",
            width=300
        )
        self.start_entry.pack(pady=(5, 20))

        # Date de fin
        end_label = ctk.CTkLabel(
            self,
            text="Date de fin"
        )
        end_label.pack(anchor="w", padx=30)

        self.end_entry = ctk.CTkEntry(
            self,
            placeholder_text="JJ/MM/AAAA",
            width=300
        )
        self.end_entry.pack(pady=(5, 30))

        save_button = ctk.CTkButton(
            self,
            text="Enregistrer",
            command=self.save_period
        )
        save_button.pack()

    def save_period(self):
        start_date = self.start_entry.get()
        end_date = self.end_entry.get()

        print("Début :", start_date)
        print("Fin :", end_date)

        self.destroy()