import nfc
from typing import Union

def extract_stude_id(tag) -> Union[str,bool]:
    service_code: int = 0x09c8
    if isinstance(tag, nfc.tag.tt3.Type3Tag):
        try:
            sc = nfc.tag.tt3.ServiceCode(service_code >> 6 ,0x0B)
            bc = nfc.tag.tt3.BlockCode(0,service=0)
            data = tag.read_without_encryption([sc],[bc])
            return data[2:10].decode('utf-8')
        except Exception as e:
            print ("error: %s" % e)
            return False
    else:
        print ("error: tag isn't Type3Tag")
    return False