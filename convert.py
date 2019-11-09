import re
import xml.etree.ElementTree as ET
import argparse
import json
from pprint import pprint

parser = argparse.ArgumentParser(description='A command line tool to convert your Dear Esther localisation files to Dear Esther: Landmark Edition version.')
parser.add_argument("-s", '--source', required=True, help="your Dear Esther localisation file")
parser.add_argument("-e", "--encoding", required=False, default="utf16", help="encoding of the source file, default is utf16")
parser.add_argument("-x", "--xmlsource", required=False, default="text_English.xml", help="a source XML file from the LE version. The default one is found inside the install folder")
parser.add_argument("-o", "--output", required=True, help="name of the output localisation file.")
args = parser.parse_args()

with open(args.source, encoding=args.encoding) as f:
    source = f.read()

with open("keys.json") as f:
    changed_keys = json.loads(f.read())

regex = re.compile("devo.(.*)	\"<len:(?:.*)>(.*)\"")
regex_output = re.findall(regex, source)

strings = {}
for item in regex_output:
    if item[0] in changed_keys:
        strings[changed_keys[item[0].replace("\t", "")]] = item[1]
    else:
        strings[item[0].replace("\t", "")] = item[1]

tree = ET.parse(args.xmlsource)
root = tree.getroot()
for item in root.findall("text"):
    if item.get("key") in strings.keys():
        item.set("string", strings[item.get("key")])

tree.write(args.output, encoding="utf-8", xml_declaration=True)