#!/usr/bin/python3
import time, json, argparse, os
from sh import xprop, acpi

CONFIGFILE = os.path.join(os.path.expanduser('~'), '.config/bunzbar/config.json')

def battery():
    acpi_text = str(acpi())

    acpi_split = acpi_text.replace(',', '').replace('\n', ' ').split(' ')
    acpi_per = []
    for acpi_lul in acpi_split:
        if '%' in acpi_lul:
            acpi_per.append(int(acpi_lul.replace('%', '')))
            
    if len(acpi_per):
        return(str(sum(acpi_per)/len(acpi_per))+'%')
    else:
        return("no battery")
            
def clck():
    curr_time = time.strftime("%H:%M:%S", time.localtime())
    return(curr_time)

class bar:
    def __init__(self):
        #smash or
        pass

    def genstr(self):
        mstr = ""
        data = json.load(open(CONFIGFILE))
        for d in (data["active"]):
            mstr += d.upper() + " "
            mstr += eval(f'{d}()')
            mstr += " | "
        return mstr

    def updatebar(self, speed=1):
        while 1:
            mstr = self.genstr()
            shift = round((time.time()*(1/speed))%len(mstr))
            sstr = self.shiftstr(mstr, shift)
            self.changeprop(sstr)

    def changeprop(self, txt):
        xprop('-root', '-set', 'WM_NAME', txt)

    def shiftstr(self, s, k):
        return(  ((s+" ")[-k-1:-1])  +  ((s+" ")[0:-k-1])  )    

    #toggle info
    def toggle(self, arr):
        data = json.load(open(CONFIGFILE))
        for info in arr:
            if info in data["active"]:
                data["active"].remove(info)
            else:
                if info in data["available"]:
                    data["active"].append(info)
        open(CONFIGFILE, 'w').write(json.dumps(data, indent=4))

def install():
    print(os.path.dirname(CONFIGFILE))
    os.makedirs(os.path.dirname(CONFIGFILE), exist_ok=True)
    open(CONFIGFILE, 'w').write(open('config.json', 'r').read())

def main():                                  
    parser = argparse.ArgumentParser(
        prog = 'bunzbar',
        description = 'display information in status bar',
        epilog = 'stay hydrated kidz')
    
    parser.add_argument('-t', '--toggle', metavar='<info>', type=str, nargs='+')
    parser.add_argument('-i', '--install', action='store_true')
    parser.add_argument('-s', '--service', action='store_true')

    args = vars(parser.parse_args())
    
    barn = bar()
    if args['toggle']:
        barn.toggle(args['toggle'])
    if args['install']:
        install()
    if args['service']:
        barn.updatebar()

if __name__ == '__main__':
    main()
