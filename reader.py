#!/usr/bin/python3

import nfc
import time
import json
import pathlib
import typing

from module.scan import extract_stude_id
from module.time import now_datetime
from module.log import has_stude_id, add_log
from module.audio import res_audio
from module.post import postData

#URL等の情報を読み込み。
cwd = pathlib.Path.cwd()
log_path = cwd.joinpath("log.csv")
entries_path = cwd.joinpath("entries.csv")
conf_path = cwd.joinpath("config/conf.json")
with open(conf_path,"r") as rf:
    conf: dict = json.load(rf)


def on_connect_nfc(tag) -> bool:
    dict_eem: dict = {}

    dict_eem["stude_id"] = extract_stude_id(tag)
    dict_eem["datetime"] = now_datetime()
    dict_eem["entry_exit"] = (
        "退室" if has_stude_id(entries_path, dict_eem["stude_id"]) else "入室"
    )

    add_log(log_path, dict_eem)
    #postData(dict_eem, conf["GSSURL"])
    #res_audio(rs_audio_file)

    print("-----------------------------------------")
    for key in dict_eem:
        print(key + ":" + dict_eem[key])
    for key in conf:
        print(key + ":" + conf[key])
    return True


def main() -> None:
    while True:
        with nfc.ContactlessFrontend('usb') as clf:
            rdwr_options: dict = {
                'targets': ['212F', '424F'],
                'on-connect': on_connect_nfc,
            }
            clf.connect(rdwr=rdwr_options)


if __name__ == "__main__":
    main()