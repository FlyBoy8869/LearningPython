import re
from pathlib import Path

import double_linked_list as dll

documents_folder = Path(
    "/Users/charles/working/MY_CECIL/test docs/Korean Docs/Released Documents"
)
regex = "^[A-Za-z]?\d{10}"

if __name__ == "__main__":
    dlinklist = dll.DoublyLinkedList()

    for d in documents_folder.glob("*.pdf"):
        filename = "unknown"
        if match := re.match(regex, d.name):
            filename = match.group(0)
        dlinklist.append((filename, d))
        # dlinklist.append((cast(Path, d).name, d))

    dlinklist.print_forward()
    print(f"file count: {dlinklist.length}")
