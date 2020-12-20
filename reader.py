#!/usr/bin/python3

import json
import pathlib
from typing import TypedDict

import nfc

from module.scan import extract_stude_id
from module.time import now_datetime
from module.log import has_stude_id, add_log
from module.audio import res_audio
from module.post import postData

# path設定
cwd = pathlib.Path.cwd()
conf_path = cwd.joinpath("config/conf.json")
log_path = cwd.joinpath("log.csv")
entries_path = cwd.joinpath("entries.csv")
audio_path = cwd.joinpath("audio")
# URL情報を読み込み。
with open(conf_path, "r") as rf:
    conf: dict = json.load(rf)


class Stamping_cont(TypedDict):
    stude_id: str
    datetime: str
    entry_exit: str


def on_connect_nfc(tag) -> bool:
    print("-----------------------------------------")
    stude_id = extract_stude_id(tag)
    stamping_cont: Stamping_cont = {
        "stude_id": stude_id,
        "datetime": now_datetime(),
        "entry_exit": (
            "退室" if has_stude_id(entries_path, stude_id)
            else "入室"
        )
    }

    add_log(log_path, stamping_cont)
    # postData(conf["GSSURL"], stamping_cont)
    if(stamping_cont["entry_exit"] == "退室"):
        res_audio(audio_path.joinpath("exit.wav"))
    else:
        res_audio(audio_path.joinpath("entry.wav"))

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
