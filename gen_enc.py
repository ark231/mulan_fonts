#!/usr/bin/env python3
import toml
with open("./enc_template.toml","r") as template_file:
    template_data=toml.load(template_file)
CHARORDER=template_data["CHARORDER"]
GLYPHNAMES=template_data["GLYPHNAMES"]
index=0
with open("./encoding.txt","w") as outfile:
    for c in CHARORDER:
        if c == ' ':
            continue
        outfile.write(f"{index:#04x} {ord(c):#06x} # {GLYPHNAMES[index]}\n")
        index+=1
