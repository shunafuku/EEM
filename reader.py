#!/usr/bin/python3

import nfc
import time
import json
import pathlib

from module.scan import scan_sic
from module.time import get_time
from module.log import check_entry, write_log
from module.audio import res_audio
from module.post import postData

#URL等の情報を読み込み。
with open("conf.json","r") as rf:
    conf_dict = json.load(rf)

log_path = "log.csv"
entries_file = "entries-file.csv"


def on_connect_nfc(tag):
    print("-----------------------------------------")
    
    dict_eem = {}
    dict_eem["sid"] = scan_sic(tag)
    dict_eem["time"] = get_time()
    dict_eem["EoE"] = check_entry(dict_eem["sid"], entries_file)
    print(dict_eem)
    write_log(dict_eem, log_file, 'utf-8')
    #postData(dict_eem, conf_dict["GSSURL"])
    #res_audio(rs_audio_file)


def main():
    clf = nfc.ContactlessFrontend('usb') 
    while True:
        clf.connect(rdwr={'on-connect': on_connect_nfc})
        time.sleep(2)


if __name__ == "__main__":
    main()