import os
import shutil
import sys


def build_and_move(src_name: str, dst_name: str):
    os.system("madoko " + src_name + ".mdk")
    os.renames(os.path.join("out", src_name + ".html"),
               os.path.join("site", dst_name + ".html"))


if not os.path.exists("DZHeader.html"):
    print("ERROR: Run this from inside the " +
          "my-madoko-docs/PersonalWebsite directory.")
    sys.exit(1)

if os.path.isdir("out"):
    shutil.rmtree("out")

if os.path.isdir("site"):
    shutil.rmtree("site")

os.mkdir("site")

build_and_move("Home", "index")
build_and_move("Projects", "projects")
build_and_move("Publications", "publications")
build_and_move("Contact", "contact")

build_and_move("AutoparallelCurves", "notes/autoparallel-curves")

if os.path.isdir("out"):
    shutil.rmtree("out")
