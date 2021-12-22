#!/usr/bin/env python3
import toml
PUNCTUATION_NAMES={
        ".":"PERIOD",
        "?":"QUESTION",
        "!":"EXCLAMATION",
        ",":"COMMA"
        }
with open("./enc_template.toml","r+") as template_file:
    template_data=toml.load(template_file)
    template_data["GLYPHNAMES"] = [] #clear all existing data
    for c in template_data["CHARORDER"]:
        if c == ' ':
            continue
        if c.islower():
            template_data["GLYPHNAMES"].append(f"MYUUSUNIMUYO SUENIPIRO I {c.upper()}")
        elif c.isupper():
            template_data["GLYPHNAMES"].append(f"MYUUSUNIMUYO SUENIPIRO II {c.upper()}")
        else:
            template_data["GLYPHNAMES"].append(f"MYUUSUNIMUYO KOHYENSU {PUNCTUATION_NAMES[c]}")
    template_file.truncate(0)
    template_file.seek(0)
    toml.dump(template_data,template_file)
