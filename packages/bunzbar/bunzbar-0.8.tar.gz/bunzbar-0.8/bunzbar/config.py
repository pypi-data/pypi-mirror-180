class config:
    def __init__(self):
        pass
 
    def genstr(self):
        mstr = ""
        data = json.load(open(CONFIGFILE))
        for d in (data["active"]):
            mstr += d.upper() + " "
            mstr += eval(f'{d}()')
            mstr += " | "
        return mstr
