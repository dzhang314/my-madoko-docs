import os
import shutil

os.chdir("pages")
# if os.path.isdir("out"): shutil.rmtree("out")
if os.path.isdir("html"): shutil.rmtree("html")
os.mkdir("html")

for fname in os.listdir():
    if fname.endswith(".mdk"):
        os.system("madoko " + fname)
        shutil.copy("out/" + fname[:-4] + ".html", "html/" + fname[:-4] + ".html")

# if os.path.isdir("out"): shutil.rmtree("out")
