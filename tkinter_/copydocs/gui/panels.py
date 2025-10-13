import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from tkinter_.copydocs.customwidgets.listbox import SpacedListbox

WINDOW_SIDE_PAD = 5
WINDOW_TOP_PAD = 5
WINDOW_BOTTOM_PAD = 5


class AssemblyPanel:
    # noinspection PyAttributeOutsideInit
    def setup_assembly_panel(self, widget_parent):
        # ===== Assemblies Listbox Section =========================================================================

        # -----Frame
        self.list_box_frame = ttk.LabelFrame(
            widget_parent,
            text=" Assemblies: ",
            bootstyle=INFO,
            relief="solid",
            borderwidth=1,
            padding=(3, 3, 3, 3),
        )
        self.list_box_frame.grid(
            row=0,
            column=0,
            columnspan=1,
            padx=WINDOW_SIDE_PAD,
            pady=WINDOW_TOP_PAD,
            sticky="nws",
        )
        self.list_box_frame.rowconfigure(0, weight=1)

        # ----- Listbox
        self.assembly_listbox = SpacedListbox(
            self.list_box_frame,
            height=25,
            width=0,
        )
        self.assembly_listbox.grid(row=0, column=0, stick="nsw", padx=5, pady=5)
        self.assembly_listbox.selection_set(0)

        # ----- Scrollbar
        self.listbox_scrollbar = ttk.Scrollbar(
            self.list_box_frame,
            bootstyle=(PRIMARY, ROUND),
            orient="vertical",
            command=self.assembly_listbox.yview,
        )
        self.assembly_listbox.configure(yscrollcommand=self.listbox_scrollbar.set)
        self.listbox_scrollbar.grid(row=0, column=1, sticky="ns", pady=2)

        # ----- Assembly Count Label
        self.assembly_count_var = tk.StringVar()
        self.assembly_count = ttk.Label(
            self.list_box_frame, bootstyle=INFO, textvariable=self.assembly_count_var
        )
        self.assembly_count.grid(row=1, column=0, sticky="ws", padx=WINDOW_SIDE_PAD)
        # ===== End Assembly Listbox Section =========================================================================


class DocumentPanel:
    # noinspection PyAttributeOutsideInit
    def setup_document_panel(self, widget_parent):
        # ===== Documents Listbox Section

        # ----- Frame
        self.document_list_box_frame = ttk.LabelFrame(
            widget_parent,
            text=" Documents: ",
            bootstyle=INFO,
            relief="solid",
            borderwidth=1,
            padding=(5, 5, 5, 5),
        )
        self.document_list_box_frame.grid(
            row=0,
            column=1,
            columnspan=3,
            pady=WINDOW_TOP_PAD,
            sticky="nsew",
        )
        self.document_list_box_frame.rowconfigure(0, weight=1)
        self.document_list_box_frame.columnconfigure(0, weight=1)

        # ----- Listbox
        self.document_listbox = SpacedListbox(
            self.document_list_box_frame,
            height=25,
            width=0,
            selectmode="extended",
        )
        self.document_listbox.grid(
            row=0,
            column=0,
            columnspan=1,
            padx=5,
            pady=5,
            sticky="NSEW",
        )

        # ----- Scrollbar
        self.document_listbox_scrollbar = ttk.Scrollbar(
            self.document_list_box_frame,
            bootstyle=(PRIMARY, ROUND),
            orient="vertical",
            command=self.document_listbox.yview,
        )
        self.document_listbox.configure(
            yscrollcommand=self.document_listbox_scrollbar.set
        )
        self.document_listbox_scrollbar.grid(row=0, column=2, sticky="ns", pady=2)

        # ----- Document Count Label
        self.document_count_var = tk.StringVar()
        self.document_count = ttk.Label(
            self.document_list_box_frame,
            bootstyle=INFO,
            textvariable=self.document_count_var,
        )
        self.document_count.grid(row=1, column=0, sticky="ws", padx=WINDOW_SIDE_PAD)

        # ===== End Assembly Document Listbox Section
