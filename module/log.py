def check_entry(sid, file_name):
    encode = "utf-8"
    entries = get_entries(file_name, encode)
    if(sid in entries):
        entries.remove(sid)
        write_entry(entries, file_name, encode)
        return "退室"
    else:
        entries.add(sid) 
        write_entry(entries, file_name, encode)
        return "入室"


def get_entries(file_name, encode):
    with open(file_name,"r", encoding=encode) as rf:
        entries = rf.readline()
        entries = [x.strip() for x in entries.split(",")]
        entries = set(filter(lambda x:x !='', entries))
        print(entries)
    return entries


def write_entry(entries, file_name, encode):
    with open(file_name,"w", encoding=encode) as wf:
        wf.write(",".join(entries))


def write_log(dict_eem, file_name, encode):
    log = dict_eem["sid"] + dict_eem["time"] + dict_eem["EoE"]
    with open(file_name,"w", encoding=encode) as wf:
        wf.write(",".join(log))