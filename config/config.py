import json
import pathlib


cwd = pathlib.Path.cwd()
conf_json_path = cwd.joinpath("conf.json")

with open(conf_json_path, "r") as rf:
    conf: dict = json.load(rf)

for key in conf:
    print("現在の設定：" + conf[key])
    conf[key] = input(key + ":")

with open(conf_json_path, "w") as wf:
    json.dump(conf, wf, indent=2)
