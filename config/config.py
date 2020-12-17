import json

with open("conf.json", "r") as rf:
    conf: dict = json.load(rf)

for key in conf:
    print("現在の設定：" + conf[key])
    conf[key] = input(key + ":")

with open("conf.json", "w") as wf:
    json.dump(conf, wf, indent=2)
