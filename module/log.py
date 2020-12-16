import pathlib
import csv

csv_encode = "utf-8"

def has_stude_id(file_path, stude_id: str) -> bool:
    entries: list = load_entries_tolist(file_path)
    is_exit: bool = True if stude_id in entries else False
    update_entries(file_path, stude_id, entries, is_exit)
    return is_exit


def load_entries_tolist(file_path) -> list:
    entries: list = []
    with open(file_path,"r", encoding=csv_encode) as rf:
        reader = csv.reader(rf)
        for row in reader:
            entries.extend(row)
    return entries


def update_entries(file_path, stude_id: str, entries: list, is_exit: bool) -> None:
    entries.remove(stude_id) if is_exit else entries.append(stude_id)
    with open(file_path,"w", encoding=csv_encode) as wf:
        writer = csv.writer(wf, lineterminator="\n")
        writer.writerow(entries)


def add_log(file_path, dict_eem: dict):
    with open(file_path,"a", encoding=csv_encode) as af:
        af.write(",".join(str(x) for x in dict_eem.values()) + "\n")