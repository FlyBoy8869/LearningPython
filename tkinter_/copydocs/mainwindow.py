import gettext
import tkinter as tk
import tkinter.filedialog as f_dialog
import webbrowser
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from tkinter_.copydocs import fileio
from tkinter_.copydocs.customwidgets.listitem import TKListItem
from tkinter_.copydocs.gui import menu
from tkinter_.copydocs.gui.panels import AssemblyPanel, DocumentPanel

WINDOW_SIDE_PAD = 0
WINDOW_TOP_PAD = 0
WINDOW_BOTTOM_PAD = 0


class MainWindow(AssemblyPanel, DocumentPanel):
    def __init__(self, parent):
        self.root = parent
        self.assemblies: dict = fileio.load_assembly_files()

        # setup main menubar
        self.root.configure(menu=menu.make_menu(self.root))

        self.setup_assembly_panel(self.root)
        self.assembly_listbox.list_variable_set(self.get_assembly_names())
        self.assembly_listbox.bind("<<ListboxSelect>>", self.on_assembly_item_clicked)
        self.assembly_listbox.selection_set(0)
        self.assembly_count_var.set(f"Assemblies: {len(self.assemblies)}")
        self.title_set(f"CopyDocs - {self.assembly_listbox.get(0)}")

        self.setup_document_panel(self.root)
        self._populate_document_listbox(self.assemblies[self.assembly_listbox.get(0)])
        self.document_listbox.bind(
            "<<ListboxSelect>>", self.on_document_list_box_item_clicked
        )
        self.document_listbox.bind(
            "<Double-1>", self.on_document_list_box_item_double_clicked
        )

        # ===== Status Label ================================================================================
        self.status_var = tk.StringVar(value="")
        self.status_label = ttk.Label(
            self.root, bootstyle=INFO, textvariable=self.status_var
        )
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
            self.root, text="Copy", command=self.on_copy_button_clicked
        )
        self.copy_button.configure(state=tk.DISABLED)
        self.copy_button.grid(row=1, column=3, padx=WINDOW_SIDE_PAD + 5, sticky="en")

        # ===== End Copy Button Section =====================================================================

        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

    def on_assembly_item_clicked(self, _):
        if index := self.assembly_listbox.curselection():
            assembly = self.assembly_listbox.get(index)
            docs = self.assemblies[assembly]
            self._populate_document_listbox(docs)
            self.copy_button.configure(state=tk.DISABLED)

            self.title_set(f"CopyDocs - {assembly}")
            self.update_status_bar("")

    def on_copy_button_clicked(self):
        if selection := self.document_listbox.curselection():
            dest = f_dialog.askdirectory(mustexist=True)
            if not dest:
                return

            print(f"dest selected: {dest}")

            num_files = len(selection)
            print(
                f"copying {num_files} {gettext.ngettext("file", "files", num_files)}..."
            )
            for index in selection:
                paths = fileio.get_document_paths(
                    self.document_listbox.get(index).split(":")[0]
                )
                print(f"{paths}")
                fileio.copy_files(paths, dest)

            self.document_listbox.selection_clear(0, tk.END)
            self.update_status_bar("")
            self.copy_button.configure(state=tk.DISABLED)

    def on_document_list_box_item_clicked(self, _):
        if selection := self.document_listbox.curselection():
            self.update_status_bar(f"{len(selection)} documents selected.")
            self.copy_button.configure(state=tk.NORMAL)

    def on_document_list_box_item_double_clicked(self, event):
        document = event.widget.get(event.widget.curselection()).split(":")[0]
        print(f"trying to open '{document}'")
        paths = fileio.get_document_paths(document)
        print(paths)
        for path in paths:
            webbrowser.open_new_tab(path.resolve().as_uri())

    def get_assembly_names(self) -> list[TKListItem]:
        av = [k for k in self.assemblies.keys()]
        return sorted(av)

    def title_set(self, text):
        self.root.title(text)

    def update_status_bar(self, text: str):
        self.status_var.set(text)

    def _populate_document_listbox(self, documents):
        self.document_listbox.list_variable_set(documents)
        self.document_count_var.set(f"Documents: {self.document_listbox.size()}")
