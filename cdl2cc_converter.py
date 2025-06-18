# -*- coding: utf-8 -*-
import os
import xml.etree.ElementTree as ET

def convert_cdl_to_cc_files(folder_path):
    if not os.path.isdir(folder_path):
        print("Folder not found: {}".format(folder_path))
        return

    output_folder = os.path.join(folder_path, "converted_cc")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


    cdl_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".cdl")]

    if not cdl_files:
        print("No .cdl files found in the folder.")
        return

    for cdl_file in cdl_files:
        cdl_path = os.path.join(folder_path, cdl_file)
        try:
            tree = ET.parse(cdl_path)
            root = tree.getroot()
            cc_nodes = root.findall(".//ColorCorrection")

            if not cc_nodes:
                print("Skipped (no <ColorCorrection>): {}".format(cdl_file))
                continue

            base_name = os.path.splitext(cdl_file)[0]

            for i, cc_node in enumerate(cc_nodes):
                cc_id = cc_node.get("id", "default")
                cc_root = ET.Element("ColorCorrection", attrib={"id": cc_id})

                sop = cc_node.find("SOPNode")
                sat = cc_node.find("SatNode")
                if sop is not None:
                    cc_root.append(sop)
                if sat is not None:
                    cc_root.append(sat)

                cc_tree = ET.ElementTree(cc_root)

                if len(cc_nodes) == 1:
                    output_name = "{}.cc".format(base_name)
                else:
                    output_name = "{}_{}.cc".format(base_name, cc_id)

                output_path = os.path.join(output_folder, output_name)

                with open(output_path, "wb") as f:
                    f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
                    cc_tree.write(f, encoding="utf-8")

                print("Converted: {} -> {}".format(cdl_file, output_name))

        except Exception as e:
            print("Error with {}: {}".format(cdl_file, e))

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python convert_all_cdls.py /path/to/folder")
    else:
        folder = sys.argv[1]
        convert_cdl_to_cc_files(folder)