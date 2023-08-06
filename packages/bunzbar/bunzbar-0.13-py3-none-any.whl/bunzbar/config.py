import time, os, json, argparse #standard imports
import bunzbar.infos, bunzbar.config #module imports
import tsv_calendar 
from sh import xprop, acpi

CFGDIR = os.path.join(os.path.expanduser('~'), '.config/bunzbar/')
CONFIGFILE = os.path.join(CFGDIR, 'config.json')

available = ["infos.battery",
        "infos.clck",
        "tsv.current.all",
        "tsv.current.name",
        "tsv.current.description",
        "tsv.current.start_time",
        "tsv.current.end_time",
        "tsv.current.end_timer",
        "tsv.next.all",
        "tsv.next.name",
        "tsv.next.description",
        "tsv.next.start_time",     
        "tsv.next.end_time",
        "tsv.next.end_timer"]

class config:
    def __init__(self):
        pass
 
    def validate(self):
        config = json.load(open(CONFIGFILE, "r"))
        config["available"] = available
        open(CONFIGFILE, 'w').write(json.dumps(config, indent=4))

    def genstr(self):
        mstr = ""
        data = json.load(open(CONFIGFILE))
        for d in (data["active"]):
            mstr += d.upper() + " "
            mstr += eval(f'{d}()')
            mstr += " | "
        return mstr
