import tkinter as tk
from tkinter import ttk

from listitem import TKListItem
from tkinter_lab import assemblies, menu

doc_path = "/Users/charles/working/MY_CECIL/test docs/Japanese Documents/cecil"

WINDOW_SIDE_PAD = 5
WINDOW_TOP_PAD = 5
WINDOW_BOTTOM_PAD = 5


class MainWindow:
    def __init__(self, parent):
        self.parent = parent
        self.assemblies: dict = assemblies.load_assemblies()

        # setup main menubar
        self.parent.configure(menu=menu.make_menu(self.parent))

        # ===== Assemblies Listbox Section =========================================================================

        # -----Frame
        self.list_box_frame = ttk.Frame(
            self.parent, relief="sunken", borderwidth=1, padding=(5, 5, 5, 5)
        )
        self.list_box_frame.grid(
            row=0,
            column=0,
            columnspan=1,
            padx=WINDOW_SIDE_PAD,
            pady=WINDOW_TOP_PAD,
            sticky="NWS",
        )
        self.list_box_frame.rowconfigure(0, weight=1)

        # ----- Listbox
        # noinspection PyTypeChecker
        self.assembly_list_var = tk.StringVar(value=self.get_assembly_names())
        self.assembly_listbox = tk.Listbox(
            self.list_box_frame, listvariable=self.assembly_list_var, height=25, width=0
        )
        self.assembly_listbox.grid(row=0, column=0, stick="NSW", padx=5, pady=5)
        self.assembly_listbox.selection_set(0)
        self.assembly_listbox.bind("<<ListboxSelect>>", self.on_assembly_item_clicked)

        # ----- Scrollbar
        self.listbox_scrollbar = tk.Scrollbar(
            self.list_box_frame, orient="vertical", command=self.assembly_listbox.yview
        )
        self.assembly_listbox.configure(yscrollcommand=self.listbox_scrollbar.set)
        self.listbox_scrollbar.grid(row=0, column=1, sticky="NS", pady=2)

        # ----- Assembly Count Label
        self.assembly_count_var = tk.StringVar(
            value=f"Assemblies: {self.assembly_listbox.size()}"
        )
        self.assembly_count = ttk.Label(
            self.parent, textvariable=self.assembly_count_var
        )
        self.assembly_count.grid(row=1, column=0, sticky="WS", padx=WINDOW_SIDE_PAD)
        # ===== End Assembly Listbox Section =========================================================================

        # ===== Documents Listbox Section

        # ----- Frame
        self.document_list_box_frame = ttk.Frame(
            self.parent, relief="sunken", borderwidth=1, padding=(5, 5, 5, 5)
        )
        self.document_list_box_frame.grid(
            row=0,
            column=1,
            columnspan=3,
            padx=WINDOW_SIDE_PAD,
            pady=WINDOW_TOP_PAD,
            sticky="NWS",
        )
        self.document_list_box_frame.rowconfigure(0, weight=1)

        # ----- Listbox
        self.document_list_var = tk.StringVar()
        self.document_listbox = tk.Listbox(
            self.document_list_box_frame,
            listvariable=self.document_list_var,
            height=25,
            width=0,
            selectmode="extended",
        )
        self.document_listbox.grid(
            row=0, column=0, columnspan=1, sticky="NSEW", padx=3, pady=3
        )

        # ----- Scrollbar
        self.document_listbox_scrollbar = tk.Scrollbar(
            self.document_list_box_frame,
            orient="vertical",
            command=self.document_listbox.yview,
        )
        self.document_listbox.configure(
            yscrollcommand=self.document_listbox_scrollbar.set
        )
        self.document_listbox_scrollbar.grid(row=0, column=2, sticky="NS", pady=2)

        # ----- Document Count Label
        self.document_count_var = tk.StringVar()
        self.document_count = ttk.Label(
            self.parent, textvariable=self.document_count_var
        )
        self.document_count.grid(row=1, column=1, sticky="WS", padx=WINDOW_SIDE_PAD)

        self._populate_document_listbox(self.assemblies[self.assembly_listbox.get(0)])
        # ===== End Assembly Document Listbox Section

        # ===== Status Label ================================================================================
        self.status_var = tk.StringVar(value="")
        self.status_label = ttk.Label(self.parent, textvariable=self.status_var)
        self.status_label.grid(
            row=2,
            column=0,
            sticky="WS",
            padx=WINDOW_SIDE_PAD,
            pady=WINDOW_BOTTOM_PAD,
        )
        # ===== End Status Label

        # ===== Copy Button Section =========================================================================
        self.copy_button = ttk.Button(
            self.parent, text="Copy", command=self.on_copy_button_clicked
        )
        self.copy_button.grid(row=1, column=2, sticky="EN")

        self.parent.rowconfigure(0, weight=1)

    def on_assembly_item_clicked(self, _):
        if index := self.assembly_listbox.curselection():
            assembly = self.assembly_listbox.get(index)
            docs = self.assemblies[assembly]
            self._populate_document_listbox(docs)

    def on_copy_button_clicked(self):
        print("copying files...")
        selection = self.document_listbox.curselection()
        print(f"{selection}")
        for index in selection:
            print(self.document_listbox.get(index))

    def update_status_bar(self, text: str):
        self.status_var.set(text)

    def _populate_document_listbox(self, documents):
        self.document_list_var.set(documents)
        self.document_count_var.set(f"Documents: {self.document_listbox.size()}")

    def get_assembly_names(self) -> list[TKListItem]:
        av = []
        for k, v in self.assemblies.items():
            av.append(TKListItem(k, v))

        return sorted(av)
