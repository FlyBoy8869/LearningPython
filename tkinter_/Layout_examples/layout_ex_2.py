import ttkbootstrap as ttk
from ttkbootstrap.constants import *


def on_treeview_select(event):
    selection = event.widget.selection()
    print(f"selection: {event.widget.item(selection)['text']}")


root = ttk.Window(themename="darkly")
root.geometry("800x600")
root.configure(padx=5, pady=5)

content_frame = ttk.Frame(root)
content_frame.grid(row=0, column=0, sticky="nsew")

assembly_frame = ttk.LabelFrame(
    content_frame,
    bootstyle=INFO,
    relief="solid",
    padding=(5, 5, 5, 5),
    text=" Assemblies: ",
)
assembly_frame.grid(row=0, column=0, sticky="nsew")

assembly_treeview = ttk.Treeview(
    assembly_frame,
    bootstyle=SECONDARY,
    selectmode=BROWSE,
    show="tree",
    padding=(0, 5, 0, 0),
)
assembly_treeview.grid(column=0, row=0, sticky="nsew")
assembly_treeview.bind("<<TreeviewSelect>>", on_treeview_select)

assemblies = [f"Assembly {i}" for i in range(1, 101)]
for assembly in assemblies:
    assembly_treeview.insert("", "end", text=assembly)

# Documents
document_frame = ttk.LabelFrame(
    content_frame,
    bootstyle=INFO,
    relief="solid",
    padding=(5, 5, 5, 5),
    text=" Documents: ",
)
document_frame.grid(column=1, row=0, sticky="nsew", padx=5)

document_treeview = ttk.Treeview(
    document_frame,
    bootstyle=SECONDARY,
    selectmode=EXTENDED,
    show="tree",
    padding=(0, 5, 0, 0),
)
document_treeview.grid(column=0, row=0, sticky="nsew")
document_treeview.insert("", "end", text="Korean Lance Drive, P0800150034")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content_frame.columnconfigure(1, weight=1)
content_frame.rowconfigure(0, weight=1)
assembly_frame.rowconfigure(0, weight=1)
document_frame.rowconfigure(0, weight=1)
document_frame.columnconfigure(0, weight=1)

root.place_window_center()
root.mainloop()
