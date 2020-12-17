#!/usr/bin/python3

import nfc
import json
import pathlib
from typing import TypedDict

from module.scan import extract_stude_id
from module.time import now_datetime
from module.log import has_stude_id, add_log
from module.audio import res_audio
from module.post import postData

# path設定
cwd = pathlib.Path.cwd()
log_path = cwd.joinpath("log.csv")
entries_path = cwd.joinpath("entries.csv")
conf_path = cwd.joinpath("config/conf.json")
# URL情報を読み込み。
with open(conf_path, "r") as rf:
    conf: dict = json.load(rf)


def on_connect_nfc(tag) -> bool:
    Stamping_cont = TypedDict('Stamping_cont', {
        "stude_id": str, "datetime": str, "entry_exit": str
    })
    stamping_cont: Stamping_cont = {
        "stude_id": extract_stude_id(tag),
        "datetime": now_datetime(),
        "entry_exit": (
            "退室"
            if has_stude_id(entries_path, stamping_cont["stude_id"])
            else "入室"
        )
    }

    add_log(log_path, stamping_cont)
    # postData(stamping_cont, conf["GSSURL"])
    # res_audio(rs_audio_file)

    print("-----------------------------------------")
    print("stude_id:" + stamping_cont["stude_id"])
    print("datetime:" + stamping_cont["datetime"])
    print("entry_exit:" + stamping_cont["entry_exit"])
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
