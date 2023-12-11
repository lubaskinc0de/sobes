import os

tree: str = ""


def get_root_content(root: str):
    for root, folders, files in os.walk(root):
        yield root, folders, files


def add_to_tree(root, files):
    global tree

    root = root.replace('./', '')

    indent = root.count('\\') * 2
    root_indent = "" if not tree else indent
    root_name = root.split('\\')[-1]

    section_sep = " " * (indent + 2)
    root_section_sep = " " * root_indent if root_indent else ""
    sep = "\n" + section_sep

    tree += f"""{root_section_sep + root_name + '/'}
{section_sep + sep.join(files) if files else ""}
"""


def get_tree(root):
    for root, _, files in get_root_content(root):
        add_to_tree(root, files)

    return tree


"""
Result:

example/
  doc.txt
  file.txt
  sub1/
    mycat.txt
    cats/
      somecat.txt
      ultra/
        ultracat!!.txt
    dogs/
      mydog.txt
      yayaya/
        somefile.txt
  sub2/
    cat.txt
    cat1.txt
    cat2.txt
    folder/
      iphone.txt
      promax/
        xr.txt
    folder2/
      file2.txt
"""

result = get_tree("./example")
print(result)
