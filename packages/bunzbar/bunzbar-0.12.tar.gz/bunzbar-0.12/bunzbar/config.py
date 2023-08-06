available = ["infos.battery",
        "infos.clck",
        "tsv.current.all",
        "tsv.current.name",
        "tsv.current.description",
        "tsv.current.start_time",
        "tsv.current.end_time",
        "tsv.next.all",
        "tsv.next.name",
        "tsv.next.description",
        "tsv.next.start_time",
        "tsv.next.end_time"]

class config:
    def __init__(self):
        pass
 
    def validate(self):
        pass
    
    def genstr(self):
        mstr = ""
        data = json.load(open(CONFIGFILE))
        for d in (data["active"]):
            mstr += d.upper() + " "
            mstr += eval(f'{d}()')
            mstr += " | "
        return mstr
