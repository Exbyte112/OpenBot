# The data here is used by main.py for some functions
# =================================================
import random

#time roles
vGMT = 0
vECT = 1
vEET = 2
vART = 2
vEAT = 3
vMET = 3.5
vNET = 4
vPLT = 5
vIST = 5.5
vBST = 6
vVST = 7
vCT = 8
vJST = 9
vACT = 9.5
vAET = 10
vSST = 11
vNST = 12
vMIT = -11
vHST = -10
vAST = -9
vPST = -8
vPNT = -7
vMST = -7
vCST = -6
vEST = -5
vIET = -5
vPRT = -4
vCNT = -3.5
vAGT = -3
vBET = -3
vECT2 = -2
vCAT = -1

#zone names
GMT = "Greenwich Mean Time"
UTC = "Coordinated Universal Time"
ECT = "European Central Time"
EET = "Eastern European Time"
ART = "Arabian Time"
EAT = "East Africa Time"
MET = "Middle East Time"
NET = "Near East Time"
PLT = "Pakistan Lahore Time"
IST = "India Standard Time"
BST = "Bangladesh Standard Time"
VST = "Venezuela Standard Time"
CT = "China Standard Time"
JST = "Japan Standard Time"
ACT = "Australia Central Time"
AET = "Australia Eastern Time"
SST = "Solomon Standard Time"
NST = "New Zealand Standard Time"
MIT = "Midway Islands Time"
HST = "Hawaii Standard Time"
AST = "Alaska Standard Time"
PST = "Pacific Standard Time"
PNT = "Phoenix Standard Time"
MST = "Mountain Standard Time"
CST = "Central Standard Time"
EST = "Eastern Standard Time"
IET = "Indiana Eastern Standard Time"
PRT = "Puerto Rico and US Virgin Islands Time"
CNT = "Canada Newfoundland Time"
AGT = "Argentina Standard Time"
BET = "Brazil Eastern Time"
ECT2 = "European Central Time"
CAT = "Central Africa Time"

#time zone list
mzone = ["GMT", "UTC", "ECT", "EET, ART", "EAT", "MET", "NET", "PLT", "IST", "BST", "VST", "CT", "JST", "ACT", "AET", "SST", "NST", "MIT", "HST", "AST", "PST", "PNT", "MST", "CST", "EST", "IET", "PRT", "CNT", "AGT", "BET", "ECT2", "CAT"]
mcode = [0, 1, 2, 2, 3, 3.5, 4, 5, 5.5, 6, 7, 8, 9, 9.5, 10, 11, 12, -11, -10, -9, -8, -7, -7, -6,-5, -5, -4, -3,-3, -3.5, -2, -1]

def hlist():
    # importing datetime module
    from datetime import datetime
    import pytz

    # assigned regular string date
    tyme = datetime.now().strftime("%Y:%m:%d:%H:%M:%S")
    Year = datetime.now().strftime("%Y")
    Year = int(Year)
    Month = datetime.now().strftime("%m")
    Month = int(Month)
    Day = datetime.now().strftime("%d")
    Day = int(Day)
    h = datetime.now().strftime("%H")
    h = int(h)
    m = datetime.now().strftime("%M")
    m = int(m)
    s = datetime.now().strftime("%S")
    s = int(s)

    hlist = ""
    p = 0
    for i in range(mcode.__len__()):
        p += 1
        if h+i >= 24:
            h = h-24
            if mcode[i]-int(mcode[i]) == 0:
                hlist += f"{str(p)} : {str(mzone[i])} / GMT {str(mcode[i])} ({h+i}: {m})\n"""
            elif mcode[i]-int(mcode[i]) == 0.5 or mcode[i]-int(mcode[i]) == -0.5:
                if m+30 >= 60:
                    hlist += f"{str(p)} : {str(mzone[i])} / GMT {str(mcode[i])} ({h+i+1}: {m+30})\n"""
                else:
                    hlist += f"{str(p)} : {str(mzone[i])} / GMT {str(mcode[i])} ({h+i}: {int(m+30)}) \n"""
        else:
            if mcode[i]-int(mcode[i]) == 0:
                hlist += f"{str(p)} : {str(mzone[i])} / GMT {str(mcode[i])} ({h+i}: {m})\n"""
            elif mcode[i]-int(mcode[i]) == 0.5 or mcode[i]-int(mcode[i]) == -0.5:
                if m+30 >= 60:
                    hlist += f"{str(p)} : {str(mzone[i])} / GMT {str(mcode[i])} ({h+i+1}: {m-30})\n"""
                else:
                    hlist += f"{str(p)} : {str(mzone[i])} / GMT {str(mcode[i])} ({h+i}: {m+30})\n"""
    return hlist
#print(hlist())

# ==============================================================
 # These are the footer tips which openbot shows in some commands with embeds, you can leave them, add or replace them with yours.

def tips():
    # Tips list
    tips = ["Use command [tzone zones] to see a list of the time in all zones.", 
            "use command [UDT] to get definitions with a 25 second timeout!",
            "use comand [!event] + [hour](24 hr) + [minute] + [query] to create events\nSTILL IN BETA",
            "Generate QR codes using [!QR] + [text]",
            "Use [!help] to see the commands",
            "use `src + [query]` to ask a question and get the answer `(Powered by WolframAlpha)`",
            "use [translate] + code + [query] to translate a word or sentence or\n[translate] + [code] + [language name] to view it's language code",
            "use [!ball] to ask the magic 8 ball a question",
            "use command [!t] + word to translate any word to english"]
    import random
    return random.choice(tips)
#print(tips())

# 8ball answers
ball_answers = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

# 