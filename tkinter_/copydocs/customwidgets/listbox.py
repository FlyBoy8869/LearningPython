import tkinter as tk


class SpacedListbox(tk.Listbox):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.list_variable = tk.StringVar()
        self.configure(listvariable=self.list_variable)

    def get(self, first, last=None):
        item = super().get(first, last)
        return item.strip()

    def list_variable_set(self, items, spacing="  "):
        self.list_variable.set([spacing + item + spacing for item in items])
