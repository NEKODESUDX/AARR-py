import os #line:1
import sys #line:2
import colorama #line:3
import ctypes #line:4
import requests #line:5
import json #line:6
import time #line:7
import random #line:8
xtrack ="eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEyLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk5OTksImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"#line:9
alphabet_to_flag ={'a':'🇦','b':'🇧','c':'🇨','d':'🇩','e':'🇪','f':'🇫','g':'🇬','h':'🇭','i':'🇮','j':'🇯','k':'🇰','l':'🇱','m':'🇲','n':'🇳','o':'🇴','p':'🇵','q':'🇶','r':'🇷','s':'🇸','t':'🇹','u':'🇺','v':'🇻','w':'🇼','x':'🇽','y':'🇾','z':'🇿'}#line:17
def logo ():#line:19
    if os .name =="nt":#line:20
        ctypes .windll .kernel32 .SetConsoleTitleW (f'[Mass Group Manager] | Ready for use <3')#line:21
    print (f"""{colorama.Fore.RESET}{colorama.Fore.LIGHTMAGENTA_EX}
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        _        _     ____   ____    _                  _
       / \      / \   |  _ \ |  _ \  | |_   ___    ___  | |
      / _ \    / _ \  | |_) || |_) | | __| / _ \  / _ \ | |
     / ___ \  / ___ \ |  _ < |  _ <  | |_ | (_) || (_) || |
    /_/   \_\/_/   \_\|_| \_\|_| \_\  \__| \___/  \___/ |_|
                                                     
    support
    https://nekodesudx.github.io/aarr/

    created by AARR
          
    If you like this tool, please donate to the developers 
    BTC: 37fB226Pyoc4so7H6KVMjxWzRKeporBDfW  
    LTC: MSU7xJHQJzocME3xLQmtAKfow36nwhuZ9Y
    
    {colorama.Fore.LIGHTCYAN_EX}
    >select number
※このツールは開発中の為joinはまだ実装してません
    [1] server join
    [2] mass Reaction spammer
    [3] active users only mentions
    [4] all user mentions
    [5] nickname changer
    [6] emoji add
    [7] reaction art

    [0] exit
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    {colorama.Fore.RESET}
    """)#line:53
def get_session (proxy =None ):#line:56
    OO00O0OOO0O00000O =requests .Session ()#line:57
    if proxy :#line:58
        OO00O0OOO0O00000O .proxies ={"http":proxy ,"https":proxy }#line:59
    return OO00O0OOO0O00000O #line:60
def get_headers (OOO0O0OO00OOO0O0O ):#line:62
    return {"Authorization":OOO0O0OO00OOO0O0O ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:67
def send_message_with_mention (O0OOOOOOOOO0O00OO ,O000OOO000O0O00O0 ,OO0000O0O00O00OOO ,O0000O00000000000 ):#line:70
    O00OO00O0O0O0O000 =get_session ()#line:71
    O0O00000OOOOO000O =get_headers (O0OOOOOOOOO0O00OO )#line:72
    if O0000O00000000000 :#line:74
        O0OO0OOO0O0OO0OO0 =random .choice (O0000O00000000000 )#line:75
        OO0000O0O00O00OOO +=f" <@{O0OO0OOO0O0OO0OO0}>"#line:76
    OO0OOO00000OOOOOO =O00OO00O0O0O0O000 .post (f"https://discord.com/api/v9/channels/{O000OOO000O0O00O0}/messages",headers =O0O00000OOOOO000O ,json ={"content":OO0000O0O00O00OOO })#line:82
    if OO0OOO00000OOOOOO .status_code in [200 ,201 ]:#line:83
        print (f"[+] Message sent to channel {O000OOO000O0O00O0}")#line:84
    elif OO0OOO00000OOOOOO .status_code ==429 :#line:85
        print ("[-] Rate limited. Please wait before retrying.")#line:86
        OOOO0O0O0OOOOO000 =OO0OOO00000OOOOOO .json ().get ("retry_after",1 )#line:87
        time .sleep (OOOO0O0O0OOOOO000 )#line:88
    else :#line:89
        print (f"[!] Error occurred: {OO0OOO00000OOOOOO.status_code}")#line:90
def fetch_messages (OOOO0OOO00O0O000O ,OO0OO000O0OOOOOO0 ,limit =100 ):#line:93
    OO0OOOO0OOOO0O000 ={"Authorization":OOOO0OOO00O0O000O ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:98
    O00O00000O0O0OO00 =requests .get (f"https://discord.com/api/v9/channels/{OO0OO000O0OOOOOO0}/messages?limit={limit}",headers =OO0OOOO0OOOO0O000 )#line:102
    if O00O00000O0O0OO00 .status_code ==200 :#line:103
        return O00O00000O0O0OO00 .json ()#line:104
    else :#line:105
        print (f"[!] Failed to fetch messages. HTTP Status Code: {O00O00000O0O0OO00.status_code}")#line:106
        return []#line:107
import concurrent .futures #line:109
def reaction_spammer ():#line:111
    try :#line:112
        with open ("token.txt")as O00OOO0O000O0O0OO :#line:113
            O0O0O0000OO0000O0 =[O0O0O00OO0O0O0OOO .strip ()for O0O0O00OO0O0O0OOO in O00OOO0O000O0O0OO .readlines ()if O0O0O00OO0O0O0OOO .strip ()]#line:114
    except (FileNotFoundError ,KeyError ):#line:115
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:116
        return #line:117
    O0O0000O000OOOO0O =input ("Server ID?: ").strip ()#line:119
    O0OOO00O0O00O000O =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:121
    if O0OOO00O0O00O000O =='2':#line:122
        OO0OO0O0OOOO00OO0 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:123
        O0OO0O00O00O0O0O0 =[O00OOO0O0OO00O000 .strip ()for O00OOO0O0OO00O000 in OO0OO0O0OOOO00OO0 if O00OOO0O0OO00O000 .strip ()]#line:124
    else :#line:125
        O0OO0O00O00O0O0O0 =[]#line:126
        for O00OO00000OO0OO00 in O0O0O0000OO0000O0 :#line:127
            try :#line:128
                O0OO0O00O00O0O0O0 .extend (fetch_channels (O00OO00000OO0OO00 ,O0O0000O000OOOO0O ))#line:129
            except Exception as O0OOO0O0OOO000OOO :#line:130
                print (f"[!] Failed to fetch channels for token. Error: {O0OOO0O0OOO000OOO}")#line:131
                continue #line:132
    OOOO0O000O00O000O =input ("Select your emoji (a, b, c, ... or custom emojis): ").strip ()#line:134
    OOO00000000O000O0 =input ("Delay between reactions (in seconds)?: ").strip ()#line:135
    try :#line:137
        OOO00000000O000O0 =float (OOO00000000O000O0 )#line:138
        if OOO00000000O000O0 <0 :#line:139
            raise ValueError #line:140
    except ValueError :#line:141
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:142
        OOO00000000O000O0 =1.0 #line:143
    OO0OO0OO00O00O00O =[]#line:145
    for OOOOOOO0OOO000O0O in OOOO0O000O00O000O .split (","):#line:146
        OOOOOOO0OOO000O0O =OOOOOOO0OOO000O0O .strip ().lower ()#line:147
        if OOOOOOO0OOO000O0O in alphabet_to_flag :#line:148
            OO0OO0OO00O00O00O .append (alphabet_to_flag [OOOOOOO0OOO000O0O ])#line:149
        else :#line:150
            OO0OO0OO00O00O00O .append (OOOOOOO0OOO000O0O )#line:151
    if not OO0OO0OO00O00O00O :#line:153
        print (f"{colorama.Fore.RED}    [!] No valid emojis provided!{colorama.Fore.RESET}")#line:154
        return #line:155
    def O0O0OOO00O000OOO0 (OO0OO00OO00OO0OOO ):#line:157
        for O0OOO000OOOOOOO00 in O0OO0O00O00O0O0O0 :#line:158
            try :#line:159
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {O0OOO000OOOOOOO00}...{colorama.Fore.RESET}")#line:160
                OO00OO0OOOO0OO0OO =fetch_messages (OO0OO00OO00OO0OOO ,O0OOO000OOOOOOO00 ,limit =100 )#line:161
                if not OO00OO0OOOO0OO0OO :#line:162
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:163
                    continue #line:164
                for O00OOOOO00OOO000O in OO00OO0OOOO0OO0OO :#line:166
                    for OOOOOO0000O000O00 in OO0OO0OO00O00O00O :#line:167
                        reactionput (OO0OO00OO00OO0OOO ,O0OOO000OOOOOOO00 ,O00OOOOO00OOO000O ['id'],OOOOOO0000O000O00 )#line:168
                        time .sleep (OOO00000000O000O0 )#line:169
            except Exception as O00O0OO00000OO0OO :#line:170
                print (f"[!] Error processing channel {O0OOO000OOOOOOO00}. Error: {O00O0OO00000OO0OO}")#line:171
                continue #line:172
    with concurrent .futures .ThreadPoolExecutor ()as O0O00O0O0O00OO0O0 :#line:174
        O0000OO0O000OO0O0 =[O0O00O0O0O00OO0O0 .submit (O0O0OOO00O000OOO0 ,OO00OOOOOO00O0O00 )for OO00OOOOOO00O0O00 in O0O0O0000OO0000O0 ]#line:175
        concurrent .futures .wait (O0000OO0O000OO0O0 )#line:176
import requests #line:179
import json #line:180
import time #line:181
import colorama #line:182
alphabet_to_flag ={'a':'🇦','b':'🇧','c':'🇨','d':'🇩','e':'🇪','f':'🇫','g':'🇬','h':'🇭','i':'🇮','j':'🇯','k':'🇰','l':'🇱','m':'🇲','n':'🇳','o':'🇴','p':'🇵','q':'🇶','r':'🇷','s':'🇸','t':'🇹','u':'🇺','v':'🇻','w':'🇼','x':'🇽','y':'🇾','z':'🇿'}#line:190
def fetch_channels (OOOO0O0O000000OO0 ,OO0O000O000OOOOOO ):#line:192
    O00OO0OOOO00O0OOO =f"https://discord.com/api/v9/guilds/{OO0O000O000OOOOOO}/channels"#line:193
    OOO000O0O000O0OOO ={"Authorization":OOOO0O0O000000OO0 }#line:194
    OOOOO00O0OOOO000O =requests .get (O00OO0OOOO00O0OOO ,headers =OOO000O0O000O0OOO )#line:195
    if OOOOO00O0OOOO000O .status_code ==200 :#line:196
        return [O0O00O000O0OO00O0 ['id']for O0O00O000O0OO00O0 in OOOOO00O0OOOO000O .json ()if O0O00O000O0OO00O0 ['type']==0 ]#line:197
    else :#line:198
        raise Exception (f"Failed to fetch channels: {OOOOO00O0OOOO000O.status_code} - {OOOOO00O0OOOO000O.text}")#line:199
def fetch_messages (OO00OOO0O00OO0O0O ,OOO0OOO00O0O00OOO ,limit =100 ):#line:201
    OO0O00OO0O00O0OOO =f"https://discord.com/api/v9/channels/{OOO0OOO00O0O00OOO}/messages?limit={limit}"#line:202
    OOO0000O0000OOOO0 ={"Authorization":OO00OOO0O00OO0O0O }#line:203
    OOO0OOO000OOO00OO =requests .get (OO0O00OO0O00O0OOO ,headers =OOO0000O0000OOOO0 )#line:204
    if OOO0OOO000OOO00OO .status_code ==200 :#line:205
        return OOO0OOO000OOO00OO .json ()#line:206
    else :#line:207
        print (f"[!] Failed to fetch messages: {OOO0OOO000OOO00OO.status_code} - {OOO0OOO000OOO00OO.text}")#line:208
        return []#line:209
def reactionput (OOO0O0O0O0O000OOO ,OOO00O000000O00O0 ,O0O0OO00OO0O00OOO ,O00OOO00OO0OOO000 ):#line:211
    O0O0OOOO00O0OOOOO =f"https://discord.com/api/v9/channels/{OOO00O000000O00O0}/messages/{O0O0OO00OO0O00OOO}/reactions/{O00OOO00OO0OOO000}/@me"#line:212
    O0O0O0OO0000OOO0O ={"Authorization":OOO0O0O0O0O000OOO ,"Content-Type":"application/json"}#line:213
    OOO00O000O000O00O =requests .put (O0O0OOOO00O0OOOOO ,headers =O0O0O0OO0000OOO0O )#line:214
    if OOO00O000O000O00O .status_code not in [204 ,200 ]:#line:215
        print (f"{colorama.Fore.RED}    [!] Failed to add reaction: {OOO00O000O000O00O.status_code} - {OOO00O000O000O00O.text}{colorama.Fore.RESET}")#line:216
import random #line:218
def reaction_art ():#line:220
    try :#line:221
        with open ("token.txt",encoding ="utf-8")as OOOOOOO00OOO0OO00 :#line:222
            OO00OO0OOO00OOO00 =[OO00000O000O0O00O .strip ()for OO00000O000O0O00O in OOOOOOO00OOO0OO00 .readlines ()if OO00000O000O0O00O .strip ()]#line:223
    except (FileNotFoundError ,KeyError ):#line:224
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:225
        return #line:226
    OO0O0OOO00000O00O =input ("Server ID?: ").strip ()#line:228
    OO0OO00O00OO000O0 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:230
    if OO0OO00O00OO000O0 =='2':#line:231
        O0OOO00OOOOO00OOO =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:232
        O000OOOO00OO000OO =[O0OO0O000OO00OOOO .strip ()for O0OO0O000OO00OOOO in O0OOO00OOOOO00OOO if O0OO0O000OO00OOOO .strip ()]#line:233
    else :#line:234
        O000OOOO00OO000OO =[]#line:235
        for OO0OOOOO0OOOO0O00 in OO00OO0OOO00OOO00 :#line:236
            try :#line:237
                O000OOOO00OO000OO .extend (fetch_channels (OO0OOOOO0OOOO0O00 ,OO0O0OOO00000O00O ))#line:238
            except Exception as OO0O00O00OO000OO0 :#line:239
                print (f"[!] Failed to fetch channels for token. Error: {OO0O00O00OO000OO0}")#line:240
                continue #line:241
        random .shuffle (O000OOOO00OO000OO )#line:242
    OOO0OO00O0OOOOO0O =input ("Delay between reactions (in seconds)?: ").strip ()#line:244
    try :#line:246
        OOO0OO00O0OOOOO0O =float (OOO0OO00O0OOOOO0O )#line:247
        if OOO0OO00O0OOOOO0O <0 :#line:248
            raise ValueError #line:249
    except ValueError :#line:250
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:251
        OOO0OO00O0OOOOO0O =1.0 #line:252
    try :#line:254
        with open ("art.txt",encoding ="utf-8")as OOO0OO0O0000O0OO0 :#line:255
            OO0OO0O0O0O00O0OO =[O00O00OOO0OOO0OO0 .strip ()for O00O00OOO0OOO0OO0 in OOO0OO0O0000O0OO0 .readlines ()if O00O00OOO0OOO0OO0 .strip ()]#line:256
    except (FileNotFoundError ,KeyError ):#line:257
        print (f"{colorama.Fore.RED}    [!] Error: art.txt file not found or empty!{colorama.Fore.RESET}")#line:258
        return #line:259
    except UnicodeDecodeError as OO0O00O00OO000OO0 :#line:260
        print (f"{colorama.Fore.RED}    [!] Error decoding art.txt: {str(OO0O00O00OO000OO0)}{colorama.Fore.RESET}")#line:261
        return #line:262
    if not OO0OO0O0O0O00O0OO :#line:264
        print (f"{colorama.Fore.RED}    [!] No valid art provided in art.txt!{colorama.Fore.RESET}")#line:265
        return #line:266
    OO0OO0O0O0O00O0OO .reverse ()#line:269
    for OO0OOOOO0OOOO0O00 in OO00OO0OOO00OOO00 :#line:271
        for O0OO00OOO0O0O0OO0 in O000OOOO00OO000OO :#line:272
            try :#line:273
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {O0OO00OOO0O0O0OO0}...{colorama.Fore.RESET}")#line:274
                OOO000OO00000OOOO =fetch_messages (OO0OOOOO0OOOO0O00 ,O0OO00OOO0O0O0OO0 ,limit =100 )#line:277
                if not OOO000OO00000OOOO :#line:278
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:279
                    continue #line:280
                for O00O0O0OOO0OOO0OO ,OO0000O000OOOOO00 in enumerate (OOO000OO00000OOOO ):#line:283
                    O0O0O0O00000O0OO0 =OO0OO0O0O0O00O0OO [O00O0O0OOO0OOO0OO %len (OO0OO0O0O0O00O0OO )].split (',')#line:284
                    for O00OO00O0O0O0OO0O in O0O0O0O00000O0OO0 :#line:285
                        reactionput (OO0OOOOO0OOOO0O00 ,O0OO00OOO0O0O0OO0 ,OO0000O000OOOOO00 ['id'],O00OO00O0O0O0OO0O .strip ())#line:286
                        print (f"Adding reaction '{O00OO00O0O0O0OO0O.strip()}' to message {OO0000O000OOOOO00['id']} in channel {O0OO00OOO0O0O0OO0}")#line:287
                        time .sleep (OOO0OO00O0OOOOO0O )#line:288
            except Exception as OO0O00O00OO000OO0 :#line:289
                print (f"[!] Error processing channel {O0OO00OOO0O0O0OO0}. Error: {OO0O00O00OO000OO0}")#line:290
                continue #line:291
    def OO0OO00OO00O0000O (OO0000O000O0O0000 ):#line:296
        for O0000OOOO00O0O0OO in O000OOOO00OO000OO :#line:297
            try :#line:298
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {O0000OOOO00O0O0OO}...{colorama.Fore.RESET}")#line:299
                O0OOOOO00OOO0000O =fetch_messages (OO0000O000O0O0000 ,O0000OOOO00O0O0OO ,limit =100 )#line:300
                if not O0OOOOO00OOO0000O :#line:301
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:302
                    continue #line:303
                for OOO000O0OOOOO0000 in O0OOOOO00OOO0000O :#line:305
                    for O00O0000OOO00O0O0 in O0O0O0O00000O0OO0 :#line:306
                        reactionput (OO0000O000O0O0000 ,O0000OOOO00O0O0OO ,OOO000O0OOOOO0000 ['id'],O00O0000OOO00O0O0 )#line:307
                        time .sleep (OOO0OO00O0OOOOO0O )#line:308
            except Exception as OO0OOOO000OOOOOOO :#line:309
                print (f"[!] Error processing channel {O0000OOOO00O0O0OO}. Error: {OO0OOOO000OOOOOOO}")#line:310
                continue #line:311
    with concurrent .futures .ThreadPoolExecutor ()as OOOOO0OOO0O0O0OO0 :#line:313
        OO0O0O000O00000OO =[OOOOO0OOO0O0O0OO0 .submit (OO0OO00OO00O0000O ,O00OOOOOOOO0O0000 )for O00OOOOOOOO0O0000 in OO00OO0OOO00OOO00 ]#line:314
        concurrent .futures .wait (OO0O0O000O00000OO )#line:315
def update_group_ids ():#line:318
    try :#line:319
        with open ("token.txt")as O0OOO00O0O0OO0OO0 :#line:320
            O0O0O00OO0O0OO00O =[O0O00O0O0O00O00O0 .strip ()for O0O00O0O0O00O00O0 in O0OOO00O0O0OO0OO0 .readlines ()if O0O00O0O0O00O00O0 .strip ()]#line:321
        OOOO0OOOO000O00OO =O0O0O00OO0O0OO00O [0 ]#line:322
    except (FileNotFoundError ,KeyError ):#line:323
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:324
        return #line:325
    OOO00O0O0O000OOOO ={"Authorization":OOOO0OOOO000O00OO ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:331
    OOO0O00O00OO000O0 =requests .get ('https://discord.com/api/v9/users/@me/channels',headers =OOO00O0O0O000OOOO )#line:333
    if OOO0O00O00OO000O0 .status_code ==200 :#line:334
        O0O0OO00OOOO0OOO0 =OOO0O00O00OO000O0 .json ()#line:335
        with open ("group_id.txt","w")as OOOO0OOOOO000O00O :#line:336
            for OOO000OOO00OO00O0 in O0O0OO00OOOO0OOO0 :#line:337
                if OOO000OOO00OO00O0 ['type']==3 :#line:338
                    OOOO0OOOOO000O00O .write (OOO000OOO00OO00O0 ['id']+'\n')#line:339
        print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Group IDs updated successfully.{colorama.Fore.RESET}")#line:340
    else :#line:341
        print (f"{colorama.Fore.LIGHTRED_EX}    [!] Failed to retrieve group IDs. HTTP Status Code: {OOO0O00O00OO000O0.status_code}{colorama.Fore.RESET}")#line:342
import requests #line:344
import requests #line:346
def fetch_channels (OO000O00O0OO0OOOO ,OO00O00OOO0OO00OO ):#line:348
    try :#line:349
        OO000O00O0OOO000O =requests .Session ()#line:350
        OOO00OO0OO00OO0OO =get_headers (OO000O00O0OO0OOOO )#line:351
        O0000OO0O0O0O0OOO =OO000O00O0OOO000O .get (f"https://discord.com/api/v9/guilds/{OO00O00OOO0OO00OO}/channels",headers =OOO00OO0OO00OO0OO ,timeout =10 )#line:358
        if O0000OO0O0O0O0OOO .status_code ==200 :#line:361
            try :#line:362
                OOO000OOOOO0000OO =O0000OO0O0O0O0OOO .json ()#line:363
                return [OO0O00OO0OO0O0OOO ['id']for OO0O00OO0OO0O0OOO in OOO000OOOOO0000OO if OO0O00OO0OO0O0OOO .get ('type')==0 ]#line:364
            except ValueError :#line:365
                print ("[!] Error: Response was not valid JSON.")#line:366
                return []#line:367
        elif O0000OO0O0O0O0OOO .status_code ==401 :#line:368
            print ("[!] Error: Unauthorized - check your token.")#line:369
        elif O0000OO0O0O0O0OOO .status_code ==403 :#line:370
            print ("[!] Error: Forbidden - you lack permissions.")#line:371
        elif O0000OO0O0O0O0OOO .status_code ==404 :#line:372
            print ("[!] Error: Server not found - check the server ID.")#line:373
        else :#line:374
            print (f"[!] Error: Unexpected status code {O0000OO0O0O0O0OOO.status_code}.")#line:375
        return []#line:378
    except requests .exceptions .Timeout :#line:380
        print ("[!] Error: Request timed out. Check your connection or try again later.")#line:381
        return []#line:382
    except requests .exceptions .RequestException as OOOOO0O0O0O00O000 :#line:383
        print (f"[!] Error: An error occurred while fetching channels: {OOOOO0O0O0O00O000}")#line:384
        return []#line:385
def extract_uids_from_messages (OO0000O0O00OO0OOO ):#line:391
    OOOO00OOO0000O0O0 =set ()#line:392
    for OO0OO00000O00O0O0 in OO0000O0O00OO0OOO :#line:393
        OOOO00OOO0000O0O0 .add (OO0OO00000O00O0O0 ['author']['id'])#line:394
    return list (OOOO00OOO0000O0O0 )#line:395
def send_message_with_mention (O0O0O000O0O00O00O ,O0O00000OO0OO0OOO ,O0O00OOOO0OO0OOO0 ,OOOOOO0OOO00O0OO0 ):#line:397
    O0O00OO00OOOO00OO =get_session ()#line:398
    OOOO000OO0000O00O =get_headers (O0O0O000O0O00O00O )#line:399
    if OOOOOO0OOO00O0OO0 :#line:401
        OO0OO00O0000OO0OO =random .choice (OOOOOO0OOO00O0OO0 )#line:402
        O0O00OOOO0OO0OOO0 +=f" <@{OO0OO00O0000OO0OO}>"#line:403
    O0OOO000OO000O0O0 =O0O00OO00OOOO00OO .post (f"https://discord.com/api/v9/channels/{O0O00000OO0OO0OOO}/messages",headers =OOOO000OO0000O00O ,json ={"content":O0O00OOOO0OO0OOO0 })#line:409
    if O0OOO000OO000O0O0 .status_code in [200 ,201 ]:#line:410
        print (f"[+] Message sent to channel {O0O00000OO0OO0OOO}")#line:411
    elif O0OOO000OO000O0O0 .status_code ==429 :#line:412
        print ("[-] Rate limited. Please wait before retrying.")#line:413
        OO0000000000OOO00 =O0OOO000OO000O0O0 .json ().get ("retry_after",1 )#line:414
        time .sleep (OO0000000000OOO00 )#line:415
    else :#line:416
        print (f"[!] Error occurred: {O0OOO000OO000O0O0.status_code}")#line:417
def send_messages_with_mentions ():#line:418
    try :#line:419
        with open ("token.txt")as OOOO00O0O0O0OO00O :#line:420
            OOOOO0O00000O0OO0 =[OOO0OOO0000O0OOO0 .strip ()for OOO0OOO0000O0OOO0 in OOOO00O0O0O0OO00O .readlines ()if OOO0OOO0000O0OOO0 .strip ()]#line:421
    except (FileNotFoundError ,KeyError ):#line:422
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:423
        return #line:424
    OOO0O00OOOO0OO00O =input ("Server ID?: ").strip ()#line:426
    O00OOO000OO000000 =input ("Delay between messages (in seconds)?: ").strip ()#line:427
    OO000O0000OOOOOO0 =input ("Number of messages to send?: ").strip ()#line:428
    O0O000O0O00O00OO0 =input ("Message content?: ").strip ()#line:429
    O000000OO0O00O000 =input ("Blacklist User IDs (comma-separated)?: ").strip ().split (',')#line:430
    O000000OO0O00O000 =[OOO0O00O0OO0000O0 .strip ()for OOO0O00O0OO0000O0 in O000000OO0O00O000 if OOO0O00O0OO0000O0 .strip ()]#line:431
    try :#line:433
        O00OOO000OO000000 =float (O00OOO000OO000000 )#line:434
        if O00OOO000OO000000 <0 :#line:435
            raise ValueError #line:436
    except ValueError :#line:437
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:438
        O00OOO000OO000000 =1.0 #line:439
    try :#line:441
        OO000O0000OOOOOO0 =int (OO000O0000OOOOOO0 )#line:442
        if OO000O0000OOOOOO0 <=0 :#line:443
            raise ValueError #line:444
    except ValueError :#line:445
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:446
        OO000O0000OOOOOO0 =1 #line:447
    OO00000000OOOOOOO =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:449
    if OO00000000OOOOOOO =='2':#line:450
        OOO0O0O00O00O0O00 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:451
        OOO0O0O00O00O0O00 =[OO000OOOO0000OO0O .strip ()for OO000OOOO0000OO0O in OOO0O0O00O00O0O00 if OO000OOOO0000OO0O .strip ()]#line:452
    else :#line:453
        OOO0O0O00O00O0O00 =[]#line:454
    O0OO0O0O00OO00O0O =set ()#line:456
    for O00O0O0O0O00OO0O0 in OOOOO0O00000O0OO0 :#line:457
        O0OO00O00OOOOOOOO =fetch_channels (O00O0O0O0O00OO0O0 ,OOO0O00OOOO0OO00O )#line:458
        for OOO0OOO00O0OOO000 in O0OO00O00OOOOOOOO :#line:459
            O00000O000000OOOO =fetch_messages (O00O0O0O0O00OO0O0 ,OOO0OOO00O0OOO000 ,limit =100 )#line:460
            O00000OOOOOOOO0O0 =extract_uids_from_messages (O00000O000000OOOO )#line:461
            O0OO0O0O00OO00O0O .update (O00000OOOOOOOO0O0 )#line:462
    O0OO0O0O00OO00O0O =list (set (O0OO0O0O00OO00O0O )-set (O000000OO0O00O000 ))#line:465
    for _O0O00O0000OOO0OOO in range (OO000O0000OOOOOO0 ):#line:467
        for O00O0O0O0O00OO0O0 in OOOOO0O00000O0OO0 :#line:468
            if OOO0O0O00O00O0O00 :#line:469
                O0OO00O00OOOOOOOO =OOO0O0O00O00O0O00 #line:470
            for OOO0OOO00O0OOO000 in O0OO00O00OOOOOOOO :#line:471
                send_message_with_mention (O00O0O0O0O00OO0O0 ,OOO0OOO00O0OOO000 ,O0O000O0O00O00OO0 ,O0OO0O0O00OO00O0O )#line:472
                time .sleep (O00OOO000OO000000 )#line:473
def join_discord_invite ():#line:478
    try :#line:479
        with open ("token.txt")as O0O00OOO0000O0O00 :#line:480
            OO0O000O0O000OOOO =[OO00O00O000OOOOOO .strip ()for OO00O00O000OOOOOO in O0O00OOO0000O0O00 .readlines ()if OO00O00O000OOOOOO .strip ()]#line:481
    except (FileNotFoundError ,KeyError ):#line:482
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:483
        return #line:484
    OO0OOOO000OO000O0 =input ("Invite Code?: discord.gg/").strip ()#line:486
    for OOOOOOO000OO0OOOO in OO0O000O0O000OOOO :#line:489
        joiner (OOOOOOO000OO0OOOO ,OO0OOOO000OO000O0 )#line:490
import json ,time ,base64 ,random ,requests #line:492
def cookieset (O00O0OOOOO0OOO0O0 ):#line:494
    O0O00O0OOOO0OO000 =O00O0OOOOO0OOO0O0 .get ("https://discord.com/app")#line:495
    return O0O00O0OOOO0OO000 .cookies .get_dict ()#line:496
def generatexspandua (O0OO0O0OOO000000O ):#line:498
    OOO0OO00OOO00O0OO =["Android","Windows","Macintosh"]#line:499
    O000O00O0O0OOOOO0 =random .choice (OOO0OO00OOO00O0OO )#line:500
    if O000O00O0O0OOOOO0 =="Macintosh":#line:501
        O00OO0OO0OO00000O =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:502
        O0O0O000000OO00OO ="Macintosh; Intel Mac OS X "+O00OO0OO0OO00000O #line:503
        O0OO000O0O000O0OO ="x86_64"#line:504
    elif O000O00O0O0OOOOO0 =="Windows":#line:505
        O00OO0OO0OO00000O =f'{random.choice([6.0, 10.0, 11.0])}'#line:506
        O0O0O000000OO00OO ="Windows NT "+O00OO0OO0OO00000O +" Win64; x64"#line:507
        O0OO000O0O000O0OO ="x86_64"#line:508
    else :#line:509
        O00OO0OO0OO00000O ="13"#line:510
        O0O0O000000OO00OO =f"Linux; Android 13; Pixel 6a"#line:511
        O0OO000O0O000O0OO ="aarch64"#line:512
    OO000O00000O0O0OO ={"os":O000O00O0O0OOOOO0 ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":O00OO0OO0OO00000O ,"os_arch":O0OO000O0O000O0OO ,"system_locale":"ja-JP","client_build_number":O0OO0O0OOO000000O ,"client_event_source":None ,"design_id":0 }#line:525
    O000OOOOO0000O00O =f"Mozilla/5.0 ({O0O0O000000OO00OO}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:526
    return base64 .b64encode (json .dumps (OO000O00000O0O0OO ,separators =(',',':')).encode ()).decode (),O000OOOOO0000O00O #line:527
def joiner (OO0OO00OO0OO0O0OO ,OOO0O0O000000OOO0 ,OO00000O0OOOOOO0O ):#line:529
    O0O00OOOOO0OOO000 =cookieset (OO00000O0OOOOOO0O )#line:530
    O0O00OOOOO0OOO000 ["locale"]="ja-JP"#line:531
    OO0OOO000O0O000OO =201211 #line:532
    OOOO0O000000O0O00 ,OO0OO0OOOOOO0OO00 =generatexspandua (OO0OOO000O0O000OO )#line:533
    OOOO0000OOOOOO0OO ={"Authorization":OO0OO00OO0OO0O0OO ,"accept":"*/*","accept-language":"ja-JP","connection":"keep-alive","DNT":"1","origin":"https://discord.com","sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","referer":"https://discord.com/channels/@me","TE":"Trailers","user-agent":OO0OO0OOOOOO0OO00 ,"X-Super-Properties":OOOO0O000000O0O00 ,}#line:548
    O0O0O0OOOO000O0OO =OO00000O0OOOOOO0O .post ("https://discord.com/api/v9/invites/"+OOO0O0O000000OOO0 ,headers =OOOO0000OOOOOO0OO ,json ={},cookies =O0O00OOOOO0OOO000 )#line:549
    if O0O0O0OOOO000O0OO .status_code ==200 :#line:550
        print ("[+] join this server "+OO0OO00OO0OO0O0OO )#line:551
        if "show_verification_form"in O0O0O0OOOO000O0OO .json ():#line:552
            bypass (OO0OO00OO0OO0O0OO ,O0O0O0OOOO000O0OO .json ()["guild"]["id"],OO00000O0OOOOOO0O ,OOOO0000OOOOOO0OO )#line:553
        return #line:554
    elif "captcha_key"in O0O0O0OOOO000O0OO .text and O0O0O0OOOO000O0OO .status_code ==400 :#line:555
        print ("[!] Hcaptcha protect"+OO0OO00OO0OO0O0OO )#line:556
        return #line:557
    elif O0O0O0OOOO000O0OO .status_code ==401 :#line:558
        print ("[×] token is dead"+OO0OO00OO0OO0O0OO )#line:559
        return #line:560
    elif O0O0O0OOOO000O0OO .status_code ==403 :#line:561
        print ("[!] 403 banned "+OO0OO00OO0OO0O0OO )#line:562
        return #line:563
    elif O0O0O0OOOO000O0OO .status_code ==429 :#line:564
        OO0OOOOO000OO0OOO =O0O0O0OOOO000O0OO .json ().get ("retry_after",1 )#line:565
        print (f"[!] 429 rate limit. Retrying after {OO0OOOOO000OO0OOO} seconds.")#line:566
        time .sleep (OO0OOOOO000OO0OOO )#line:567
        return #line:568
    else :#line:569
        print ("[!] error "+OO0OO00OO0OO0O0OO )#line:570
        return #line:571
def update_group_ids ():#line:573
    OOOOOO00OOOO0OOOO =input ("Invite Code?: ").strip ()#line:574
    try :#line:575
        with open ("token.txt")as OO0OO0O0O000OOOOO :#line:576
            OOO0O0OOOOOOO0O0O =[O0000O00000000O0O .strip ()for O0000O00000000O0O in OO0OO0O0O000OOOOO .readlines ()if O0000O00000000O0O .strip ()]#line:577
    except (FileNotFoundError ,KeyError ):#line:578
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:579
        return #line:580
    O0OOO000O0O00OO0O =requests .Session ()#line:582
    for OOO000O00OO0000OO in OOO0O0OOOOOOO0O0O :#line:583
        joiner (OOO000O00OO0000OO ,OOOOOO00OOOO0OOOO ,O0OOO000O0O00OO0O )#line:584
        time .sleep (2 )#line:585
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:587
def bypass (O00O0OO0O0OO0OOOO ,OOOO0O0OOO0OOO0O0 ,OO0OOOOO00OO0O0OO ,O00OO0000OOO0OO00 ):#line:590
    try :#line:591
        OOO0000O0OO0OO0OO =OO0OOOOO00OO0O0OO .get (f"https://discord.com/api/v9/guilds/{OOOO0O0OOO0OOO0O0}/member-verification?with_guild=false",headers =O00OO0000OOO0OO00 ).json ()#line:592
        OO0000O0OO0O0000O =OO0OOOOO00OO0O0OO .put (f"https://discord.com/api/v9/guilds/{OOOO0O0OOO0OOO0O0}/requests/@me",headers =O00OO0000OOO0OO00 ,json =OOO0000O0OO0OO0OO )#line:593
        if OO0000O0OO0O0000O .status_code ==201 :#line:594
            print (f"[+] MemberscreeningBypassed {O00O0OO0O0OO0OOOO}")#line:595
            return #line:596
        else :#line:597
            print (f"[!] Bypassが出来ませんでした {O00O0OO0O0OO0OOOO}")#line:598
            return #line:599
    except Exception as O0000OO00000O00OO :#line:600
        print (f"[!] エラーが発生しました。{O0000OO00000O00OO}")#line:601
session =requests .Session ()#line:603
def reactionput (OOO00OO0O0O0OO00O ,OO00O0OO000O00O00 ,OO0O0O00O0O00O0O0 ,OOO00OOOOOOO0O0O0 ,proxy =None ):#line:606
    O000O00O00OO0O0OO =get_session (proxy )#line:607
    O00OOOO00OO0OOOO0 =get_headers (O000O00O00OO0O0OO )#line:608
    O00OOOO00OO0OOOO0 ["Authorization"]=OOO00OO0O0O0OO00O #line:609
    OOO00OOOOOOO0O0O0 =requests .utils .quote (OOO00OOOOOOO0O0O0 )#line:611
    OO0OO0O0O0OO00000 =O000O00O00OO0O0OO .put (f"https://discord.com/api/v9/channels/{OO00O0OO000O00O00}/messages/{OO0O0O00O0O00O0O0}/reactions/{OOO00OOOOOOO0O0O0}/%40me?location=Message&type=0",headers =O00OOOO00OO0OOOO0 )#line:615
    if OO0OO0O0O0OO00000 .status_code in [200 ,204 ]:#line:616
        print (f"[+] Reaction '{OOO00OOOOOOO0O0O0}' added successfully to message {OO0O0O00O0O00O0O0}")#line:617
    elif OO0OO0O0O0OO00000 .status_code ==429 :#line:618
        print ("[-] Rate limited. Please wait before retrying.")#line:619
        O00OOOOO0O00OO0OO =OO0OO0O0O0OO00000 .json ().get ("retry_after",1 )#line:620
        time .sleep (O00OOOOO0O00OO0OO )#line:621
    elif OO0OO0O0O0OO00000 .status_code ==401 :#line:622
        print ("[-] Invalid or expired token.")#line:623
    else :#line:624
        print (f"[!] Error occurred: {OO0OO0O0O0OO00000.status_code}")#line:625
def generatexspandua (OO0O0OO000OOO0O00 ):#line:628
  O00OOO0OOOO0OOO0O =["Android","Windows","Macintosh"]#line:629
  OO0O00OOOOOO00O00 =random .choice (O00OOO0OOOO0OOO0O )#line:630
  if OO0O00OOOOOO00O00 =="Macintosh":#line:631
    O0O0OOOO0O0000O0O =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:632
    OO00O0OO000O0000O ="Macintosh; Intel Mac OS X "+O0O0OOOO0O0000O0O #line:633
    O0000OO0O0O000000 ="x86_64"#line:634
  if OO0O00OOOOOO00O00 =="Windows":#line:635
    O0O0OOOO0O0000O0O =f'{random.choice([6.0,10.0,11.0])}'#line:636
    OO00O0OO000O0000O ="Windows NT "+O0O0OOOO0O0000O0O +" Win64; x64"#line:637
    O0000OO0O0O000000 ="x86_64"#line:638
  if OO0O00OOOOOO00O00 =="Android":#line:639
    O0O0OOOO0O0000O0O ="13"#line:640
    OO00O0OO000O0000O =f"Linux; Android 13; Pixel 6a"#line:641
    O0000OO0O0O000000 ="aarch64"#line:642
  O0OOO0O00O00O0000 ={"os":OO0O00OOOOOO00O00 ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":O0O0OOOO0O0000O0O ,"os_arch":O0000OO0O0O000000 ,"system_locale":"ja-JP","client_build_number":OO0O0OO000OOO0O00 ,"client_event_source":None ,"design_id":0 }#line:643
  OO0O0OO0OOO0O0OOO =f"Mozilla/5.0 ({OO00O0OO000O0000O}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:644
  return base64 .b64encode (json .dumps (O0OOO0O00O00O0000 ,separators =(',',':')).encode ()).decode (),OO0O0OO0OOO0O0OOO #line:645
import base64 #line:647
def nickchanger ():#line:650
    try :#line:651
        with open ("token.txt")as OOOOOOOO0OOOOO0OO :#line:652
            OOOOOO0000OO0OO0O =[O0OOO0OOO000000OO .strip ()for O0OOO0OOO000000OO in OOOOOOOO0OOOOO0OO .readlines ()if O0OOO0OOO000000OO .strip ()]#line:653
    except (FileNotFoundError ,KeyError ):#line:654
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:655
        return #line:656
    O0OO000000OOOO00O =input ("Server ID?: ").strip ()#line:658
    OOO000OOO0OOOO000 =input ("Nickname?: ").strip ()#line:659
    O00OO0O0OOOOOOOO0 =input ("Delay (in seconds)?: ").strip ()#line:660
    try :#line:662
        O00OO0O0OOOOOOOO0 =float (O00OO0O0OOOOOOOO0 )#line:663
        if O00OO0O0OOOOOOOO0 <0 :#line:664
            raise ValueError #line:665
    except ValueError :#line:666
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:667
        O00OO0O0OOOOOOOO0 =1.0 #line:668
    for OOO0000OO0O000O00 in OOOOOO0000OO0OO0O :#line:670
        OOOO00OOOO0O0O00O ={"Authorization":OOO0000OO0O000O00 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:675
        OOO0OO0OO0OO00OOO ={"nick":OOO000OOO0OOOO000 }#line:676
        OOO0OOOOO0OO000OO =requests .patch (f"https://discord.com/api/v9/guilds/{O0OO000000OOOO00O}/members/@me",headers =OOOO00OOOO0O0O00O ,json =OOO0OO0OO0OO00OOO )#line:677
        if OOO0OOOOO0OO000OO .status_code ==200 :#line:679
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Nickname changed to '{OOO000OOO0OOOO000}' successfully for token {OOO0000OO0O000O00}.{colorama.Fore.RESET}")#line:680
        elif OOO0OOOOO0OO000OO .status_code ==429 :#line:681
            print (f"{colorama.Fore.RED}    [!] Rate limited. Please wait before retrying for token {OOO0000OO0O000O00}.{colorama.Fore.RESET}")#line:682
            O0OO0O00000O0O0OO =OOO0OOOOO0OO000OO .json ().get ("retry_after",1 )#line:683
            time .sleep (O0OO0O00000O0O0OO )#line:684
        else :#line:685
            print (f"{colorama.Fore.RED}    [!] Error occurred: {OOO0OOOOO0OO000OO.status_code} for token {OOO0000OO0O000O00}.{colorama.Fore.RESET}")#line:686
        time .sleep (O00OO0O0OOOOOOOO0 )#line:688
import json ,websocket ,threading ,tls_client ,random ,time #line:692
session =tls_client .Session (client_identifier ="chrome112",random_tls_extension_order =True )#line:694
class Utils :#line:696
    @staticmethod #line:697
    def rangeCorrector (O0OOOO0O000O00O00 ):#line:698
        if [0 ,99 ]not in O0OOOO0O000O00O00 :#line:699
            O0OOOO0O000O00O00 .insert (0 ,[0 ,99 ])#line:700
        return O0OOOO0O000O00O00 #line:701
    @staticmethod #line:703
    def getRanges (O0000O0O00OOOOOOO ,OO0O000000O00OO00 ,O000O00OOO00O0OOO ):#line:704
        O00000OOOOOO00OOO =int (O0000O0O00OOOOOOO *OO0O000000O00OO00 )#line:705
        OO0O000000O0O0OO0 =[[O00000OOOOOO00OOO ,O00000OOOOOO00OOO +99 ]]#line:706
        if O000O00OOO00O0OOO >O00000OOOOOO00OOO +99 :#line:707
            OO0O000000O0O0OO0 .append ([O00000OOOOOO00OOO +100 ,O00000OOOOOO00OOO +199 ])#line:708
        return Utils .rangeCorrector (OO0O000000O0O0OO0 )#line:709
    @staticmethod #line:711
    def parseGuildMemberListUpdate (OOOO00000O0O00O00 ):#line:712
        O00OO0OO000OOO0O0 ={"online_count":OOOO00000O0O00O00 ["d"]["online_count"],"member_count":OOOO00000O0O00O00 ["d"]["member_count"],"id":OOOO00000O0O00O00 ["d"]["id"],"guild_id":OOOO00000O0O00O00 ["d"]["guild_id"],"hoisted_roles":OOOO00000O0O00O00 ["d"]["groups"],"types":[],"locations":[],"updates":[],}#line:722
        for O00OO0OO0O0O0O0OO in OOOO00000O0O00O00 ["d"]["ops"]:#line:724
            O00OO0OO000OOO0O0 ["types"].append (O00OO0OO0O0O0O0OO ["op"])#line:725
            if O00OO0OO0O0O0O0OO ["op"]in ("SYNC","INVALIDATE"):#line:726
                O00OO0OO000OOO0O0 ["locations"].append (O00OO0OO0O0O0O0OO ["range"])#line:727
                if O00OO0OO0O0O0O0OO ["op"]=="SYNC":#line:728
                    O00OO0OO000OOO0O0 ["updates"].append (O00OO0OO0O0O0O0OO ["items"])#line:729
                else :#line:730
                    O00OO0OO000OOO0O0 ["updates"].append ([])#line:731
            elif O00OO0OO0O0O0O0OO ["op"]in ("INSERT","UPDATE","DELETE"):#line:732
                O00OO0OO000OOO0O0 ["locations"].append (O00OO0OO0O0O0O0OO ["index"])#line:733
                if O00OO0OO0O0O0O0OO ["op"]=="DELETE":#line:734
                    O00OO0OO000OOO0O0 ["updates"].append ([])#line:735
                else :#line:736
                    O00OO0OO000OOO0O0 ["updates"].append (O00OO0OO0O0O0O0OO ["item"])#line:737
        return O00OO0OO000OOO0O0 #line:738
class DiscordSocket (websocket .WebSocketApp ):#line:740
    def __init__ (OOO000O0OO00O0000 ,OOO000OO00OO00000 ,O0OO0OOOOO00OO0O0 ,OOO0OO0OO0OO0OOO0 ):#line:741
        OOO000O0OO00O0000 .token =OOO000OO00OO00000 #line:742
        OOO000O0OO00O0000 .guild_id =O0OO0OOOOO00OO0O0 #line:743
        OOO000O0OO00O0000 .channel_id =OOO0OO0OO0OO0OOO0 #line:744
        OOO000O0OO00O0000 .socket_headers ={"Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","Cache-Control":"no-cache","Pragma":"no-cache","Sec-WebSocket-Extensions":"permessage-deflate; client_max_window_bits","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",}#line:752
        super ().__init__ ("wss://gateway.discord.gg/?encoding=json&v=9",header =OOO000O0OO00O0000 .socket_headers ,on_open =lambda OOO00O0O00O00OOO0 :OOO000O0OO00O0000 .sock_open (OOO00O0O00O00OOO0 ),on_message =lambda O0OOO0O0O000OOOOO ,O0OO00O0O0O00OOO0 :OOO000O0OO00O0000 .sock_message (O0OOO0O0O000OOOOO ,O0OO00O0O0O00OOO0 ),on_close =lambda OOO00O0000OOOOOOO ,OO0O0OOOOO0O00000 ,OO00OO0OO00OO000O :OOO000O0OO00O0000 .sock_close (OOO00O0000OOOOOOO ,OO0O0OOOOO0O00000 ,OO00OO0OO00OO000O ),)#line:761
        OOO000O0OO00O0000 .endScraping =False #line:763
        OOO000O0OO00O0000 .guilds ={}#line:764
        OOO000O0OO00O0000 .members ={}#line:765
        OOO000O0OO00O0000 .ranges =[[0 ,0 ]]#line:766
        OOO000O0OO00O0000 .lastRange =0 #line:767
        OOO000O0OO00O0000 .packets_recv =0 #line:768
    def run (OO0O00OO000OO00OO ):#line:770
        OO0O00OO000OO00OO .run_forever ()#line:771
        return OO0O00OO000OO00OO .members #line:772
    def scrapeUsers (OO000000OO0OOO0OO ):#line:774
        if not OO000000OO0OOO0OO .endScraping :#line:775
            OO000000OO0OOO0OO .send ('{"op":14,"d":{"guild_id":"'+OO000000OO0OOO0OO .guild_id +'","typing":true,"activities":true,"threads":true,"channels":{"'+OO000000OO0OOO0OO .channel_id +'":'+json .dumps (OO000000OO0OOO0OO .ranges )+"}}}")#line:784
    def sock_open (O00OOOO00OOO000O0 ,OO0O00O000OO0OO00 ):#line:786
        O00OOOO00OOO000O0 .send ('{"op":2,"d":{"token":"'+O00OOOO00OOO000O0 .token +'","capabilities":125,"properties":{"os":"Windows NT","browser":"Chrome","device":"","system_locale":"it-IT","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36","browser_version":"119.0","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":103981,"client_event_source":null},"presence":{"status":"online","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}')#line:791
    def heartbeatThread (O000O0OO00O0O000O ,O0O00000OOO0O00OO ):#line:793
        try :#line:794
            while True :#line:795
                O000O0OO00O0O000O .send ('{"op":1,"d":'+str (O000O0OO00O0O000O .packets_recv )+"}")#line:796
                time .sleep (O0O00000OOO0O00OO )#line:797
        except Exception as OOO0O000O0000O0OO :#line:798
            pass #line:799
    def sock_message (OO0O0O00OO000O0O0 ,OO0O00OOO000O0000 ,OOO0OO0O0O00O00O0 ):#line:801
        OOOO0OO00O0O00O00 =json .loads (OOO0OO0O0O00O00O0 )#line:802
        if OOOO0OO00O0O00O00 is None :#line:803
            return #line:804
        if OOOO0OO00O0O00O00 ["op"]!=11 :#line:805
            OO0O0O00OO000O0O0 .packets_recv +=1 #line:806
        if OOOO0OO00O0O00O00 ["op"]==10 :#line:807
            threading .Thread (target =OO0O0O00OO000O0O0 .heartbeatThread ,args =(OOOO0OO00O0O00O00 ["d"]["heartbeat_interval"]/1000 ,),daemon =True ,).start ()#line:812
        if OOOO0OO00O0O00O00 ["t"]=="READY":#line:813
            for OOO0OO00OO0OO00O0 in OOOO0OO00O0O00O00 ["d"]["guilds"]:#line:814
                OO0O0O00OO000O0O0 .guilds [OOO0OO00OO0OO00O0 ["id"]]={"member_count":OOO0OO00OO0OO00O0 ["member_count"]}#line:815
        if OOOO0OO00O0O00O00 ["t"]=="READY_SUPPLEMENTAL":#line:816
            OO0O0O00OO000O0O0 .ranges =Utils .getRanges (0 ,100 ,OO0O0O00OO000O0O0 .guilds [OO0O0O00OO000O0O0 .guild_id ]["member_count"])#line:819
            OO0O0O00OO000O0O0 .scrapeUsers ()#line:820
        elif OOOO0OO00O0O00O00 ["t"]=="GUILD_MEMBER_LIST_UPDATE":#line:821
            OOOOO00O0O00OO00O =Utils .parseGuildMemberListUpdate (OOOO0OO00O0O00O00 )#line:822
            if OOOOO00O0O00OO00O ["guild_id"]==OO0O0O00OO000O0O0 .guild_id and ("SYNC"in OOOOO00O0O00OO00O ["types"]or "UPDATE"in OOOOO00O0O00OO00O ["types"]):#line:826
                for O00000O0000OOOOO0 ,O00000O00OO00O00O in enumerate (OOOOO00O0O00OO00O ["types"]):#line:827
                    if O00000O00OO00O00O =="SYNC":#line:828
                        if len (OOOOO00O0O00OO00O ["updates"][O00000O0000OOOOO0 ])==0 :#line:829
                            OO0O0O00OO000O0O0 .endScraping =True #line:830
                            break #line:831
                        for O0OOOOO000O0O0000 in OOOOO00O0O00OO00O ["updates"][O00000O0000OOOOO0 ]:#line:833
                            if "member"in O0OOOOO000O0O0000 :#line:834
                                OO0OOOOOO0OO000O0 =O0OOOOO000O0O0000 ["member"]#line:835
                                O000O0O0O0O000O0O ={"tag":OO0OOOOOO0OO000O0 ["user"]["username"]+"#"+OO0OOOOOO0OO000O0 ["user"]["discriminator"],"id":OO0OOOOOO0OO000O0 ["user"]["id"],}#line:841
                                if not OO0OOOOOO0OO000O0 ["user"].get ("bot"):#line:842
                                    OO0O0O00OO000O0O0 .members [OO0OOOOOO0OO000O0 ["user"]["id"]]=O000O0O0O0O000O0O #line:843
                    elif O00000O00OO00O00O =="UPDATE":#line:845
                        for O0OOOOO000O0O0000 in OOOOO00O0O00OO00O ["updates"][O00000O0000OOOOO0 ]:#line:846
                            if "member"in O0OOOOO000O0O0000 :#line:847
                                OO0OOOOOO0OO000O0 =O0OOOOO000O0O0000 ["member"]#line:848
                                O000O0O0O0O000O0O ={"tag":OO0OOOOOO0OO000O0 ["user"]["username"]+"#"+OO0OOOOOO0OO000O0 ["user"]["discriminator"],"id":OO0OOOOOO0OO000O0 ["user"]["id"],}#line:854
                                if not OO0OOOOOO0OO000O0 ["user"].get ("bot"):#line:855
                                    OO0O0O00OO000O0O0 .members [OO0OOOOOO0OO000O0 ["user"]["id"]]=O000O0O0O0O000O0O #line:856
                    OO0O0O00OO000O0O0 .lastRange +=1 #line:858
                    OO0O0O00OO000O0O0 .ranges =Utils .getRanges (OO0O0O00OO000O0O0 .lastRange ,100 ,OO0O0O00OO000O0O0 .guilds [OO0O0O00OO000O0O0 .guild_id ]["member_count"])#line:861
                    time .sleep (0.45 )#line:862
                    OO0O0O00OO000O0O0 .scrapeUsers ()#line:863
            if OO0O0O00OO000O0O0 .endScraping :#line:865
                OO0O0O00OO000O0O0 .close ()#line:866
    def sock_close (OO0O000OOOOO0O00O ,O0O00O0OO000O00O0 ,OOOO00OO0OO0O0000 ,O00OO000O00OO000O ):#line:868
        pass #line:869
def scrape (OOOO0O00OOO0OOO0O ,O0O0OOOOO0O000000 ,OOOO0O00O000OOO00 ):#line:871
    O00O0OOO0O0000O0O =DiscordSocket (OOOO0O00OOO0OOO0O ,O0O0OOOOO0O000000 ,OOOO0O00O000OOO00 )#line:872
    return O00O0OOO0O0000O0O .run ()#line:873
def member_scrape (OO0O00OO0O00O0O0O ,O0OO00OO0OOO0000O ,OO000O0000OOOOOOO ):#line:875
    OO000OOOO0OOOOOO0 =[]#line:876
    for O0O000OO0OO0OO00O in OO0O00OO0O00O0O0O :#line:877
        OOO0O00OO000OO000 ={"Authorization":O0O000OO0OO0OO00O ,"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}#line:878
        OOO0OOOOO00OOO0O0 =session .get (f"https://canary.discord.com/api/v9/guilds/{O0OO00OO0OOO0000O}",headers =OOO0O00OO000OO000 )#line:879
        if OOO0OOOOO00OOO0O0 .status_code ==200 :#line:880
            OO000OOOO0OOOOOO0 .append (O0O000OO0OO0OO00O )#line:881
            break #line:882
    if not OO000OOOO0OOOOOO0 :#line:883
        print ("missing access")#line:884
    O0O000OO0OO0OO00O =random .choice (OO000OOOO0OOOOOO0 )#line:886
    OOO00OO0OOOOOOO00 =scrape (O0O000OO0OO0OO00O ,O0OO00OO0OOO0000O ,OO000O0000OOOOOOO )#line:887
    OOOOOO0OOOOO00OOO =[f"<@{OO0O0O00OOO00OO0O}>"for OO0O0O00OOO00OO0O in [int (OO0O000OOO00O0OOO )for OO0O000OOO00O0OOO in OOO00OO0OOOOOOO00 .keys ()]]#line:888
    print (f"[SUCCESS] {len(OOOOOO0OOOOO00OOO)} scraped members")#line:889
    return OOOOOO0OOOOO00OOO #line:890
def spammer_menu ():#line:892
    try :#line:893
        with open ("token.txt")as O0000OOO0OO0O0O00 :#line:894
            OOO0OOO0O0OOO0O00 =[OOO000O0000O00OOO .strip ()for OOO000O0000O00OOO in O0000OOO0OO0O0O00 .readlines ()if OOO000O0000O00OOO .strip ()]#line:895
    except (FileNotFoundError ,KeyError ):#line:896
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:897
        return #line:898
    OOOO0OOO00OOO000O =input ("Server ID?: ").strip ()#line:900
    OOOO0000OO000OOO0 =input ("Message?: ").strip ()#line:901
    OO000O0OOO0OOOO0O =input ("Random mention (True/False)?: ").strip ().lower ()=='true'#line:902
    OOO0OOOOO00O00O0O =input ("Delay between messages (in seconds)?: ").strip ()#line:903
    O000O0O000OO0OOO0 =input ("Number of messages to send?: ").strip ()#line:904
    O0O0O0O0O0OO0OO00 =input ("Blacklist User IDs (comma-separated) (Leave blank to skip)?: ").strip ().split (',')#line:905
    O0O0O0O0O0OO0OO00 =[f"<@{O00OO00000OO0O00O.strip()}>"for O00OO00000OO0O00O in O0O0O0O0O0OO0OO00 if O00OO00000OO0O00O .strip ()]#line:906
    try :#line:908
        OOO0OOOOO00O00O0O =float (OOO0OOOOO00O00O0O )#line:909
        if OOO0OOOOO00O00O0O <0 :#line:910
            raise ValueError #line:911
    except ValueError :#line:912
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:913
        OOO0OOOOO00O00O0O =1.0 #line:914
    try :#line:916
        O000O0O000OO0OOO0 =int (O000O0O000OO0OOO0 )#line:917
        if O000O0O000OO0OOO0 <=0 :#line:918
            raise ValueError #line:919
    except ValueError :#line:920
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:921
        O000O0O000OO0OOO0 =1 #line:922
    OO00O000O0OOO0O0O =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:924
    if OO00O000O0OOO0O0O =='2':#line:925
        O0O00O00O0OOO00OO =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:926
        O0O00O00O0OOO00OO =[OOOOO000O00OOO0O0 .strip ()for OOOOO000O00OOO0O0 in O0O00O00O0OOO00OO if OOOOO000O00OOO0O0 .strip ()]#line:927
    else :#line:928
        O0O00O00O0OOO00OO =fetch_channels (OOO0OOO0O0OOO0O00 [0 ],OOOO0OOO00OOO000O )#line:929
    OOOOO0OO0OOOO00O0 =None #line:931
    spammer (OOO0OOO0O0OOO0O00 ,OOOO0OOO00OOO000O ,O0O00O00O0OOO00OO ,OOOO0000OO000OOO0 ,OO000O0OOO0OOOO0O ,O0O0O0O0O0OO0OO00 ,OOOOO0OO0OOOO00O0 ,O000O0O000OO0OOO0 )#line:933
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:935
def spammer (O0000000O000OOOO0 ,OO00O0O0O0O0OOO0O ,OOO00O0O0000OO0OO ,O0O00OOOOOO0OOOOO ,OO0O00OO0OO000O00 ,OOOOO00O0OO0OO00O ,OO00OO0O00OOO0OO0 ,OOO00OOO0O00O0O0O ):#line:937
    OOO0O00O00OO0OOOO =get_session (OO00OO0O00OOO0OO0 )#line:938
    OO00O0O00OO000O0O =0 #line:939
    OOOOO0000O0O0000O =member_scrape (O0000000O000OOOO0 ,OO00O0O0O0O0OOO0O ,OOO00O0O0000OO0OO [0 ])#line:941
    OOOOO0000O0O0000O =[OOOO0O0O0O0OOOO00 for OOOO0O0O0O0OOOO00 in OOOOO0000O0O0000O if OOOO0O0O0O0OOOO00 not in OOOOO00O0OO0OO00O ]#line:942
    for _O0O000O000OOOO0O0 in range (OOO00OOO0O00O0O0O ):#line:944
        OO00000OOOOO00O00 =O0000000O000OOOO0 [OO00O0O00OO000O0O ]#line:945
        OOO000OOO0000OOO0 =get_headers (OO00000OOOOO00O00 )#line:946
        for O0OOO0000O000000O in OOO00O0O0000OO0OO :#line:947
            O0OOOO0O0O0000OO0 =O0O00OOOOOO0OOOOO #line:948
            if OO0O00OO0OO000O00 and OOOOO0000O0O0000O :#line:949
                O0O0OOO00OOOOO00O =random .choice (OOOOO0000O0O0000O )#line:950
                O0OOOO0O0O0000OO0 +=f" {O0O0OOO00OOOOO00O}"#line:951
            OOO00000OO00OOOO0 =OOO0O00O00OO0OOOO .post (f"https://discord.com/api/v9/channels/{O0OOO0000O000000O}/messages",json ={"content":O0OOOO0O0O0000OO0 },headers =OOO000OOO0000OOO0 )#line:953
            if OOO00000OO00OOOO0 .status_code ==200 :#line:954
                print (f"200 message sent: {OO00000OOOOO00O00}")#line:955
            elif OOO00000OO00OOOO0 .status_code ==429 :#line:956
                print (f"429 rate limit: {OO00000OOOOO00O00}")#line:957
                OO0O0O00OOOOOO0OO =OOO00000OO00OOOO0 .json ().get ("retry_after",1 )#line:958
                time .sleep (OO0O0O00OOOOOO0OO )#line:959
            elif OOO00000OO00OOOO0 .status_code ==401 :#line:960
                print (f"401 unknown token: {OO00000OOOOO00O00}")#line:961
            else :#line:962
                print (f"error: {OO00000OOOOO00O00}")#line:963
        OO00O0O00OO000O0O =(OO00O0O00OO000O0O +1 )%len (O0000000O000OOOO0 )#line:965
        time .sleep (1 )#line:966
import requests #line:970
import base64 #line:971
import colorama #line:972
import time #line:973
def add_emojis_from_files ():#line:975
    try :#line:976
        with open ("emojiname.txt")as OOOOOO000OOOO00OO ,open ("emojiurl.txt")as O000OO000000000OO :#line:977
            O0OOO0O00OOOO0OOO =[OOO00O0O0000O00O0 .strip ()for OOO00O0O0000O00O0 in OOOOOO000OOOO00OO .read ().split (',')if OOO00O0O0000O00O0 .strip ()]#line:978
            O00000O0OOO0O0OOO =[O00OOOO00OOO000OO .strip ()for O00OOOO00OOO000OO in O000OO000000000OO .read ().split (',')if O00OOOO00OOO000OO .strip ()]#line:979
    except FileNotFoundError as OO000O0OO0OOO0000 :#line:980
        print (f"{colorama.Fore.RED}    [!] Error: {str(OO000O0OO0OOO0000)}{colorama.Fore.RESET}")#line:981
        return #line:982
    if len (O0OOO0O00OOOO0OOO )!=len (O00000O0OOO0O0OOO ):#line:984
        print (f"{colorama.Fore.RED}    [!] Error: The number of emoji names and URLs do not match!{colorama.Fore.RESET}")#line:985
        return #line:986
    try :#line:988
        with open ("token.txt")as O0OOO00OOO00O0OOO :#line:989
            OO00O000O00000OOO =[OOOO00OO0000OO0OO .strip ()for OOOO00OO0000OO0OO in O0OOO00OOO00O0OOO .readlines ()if OOOO00OO0000OO0OO .strip ()]#line:990
    except FileNotFoundError as OO000O0OO0OOO0000 :#line:991
        print (f"{colorama.Fore.RED}    [!] Error: {str(OO000O0OO0OOO0000)}{colorama.Fore.RESET}")#line:992
        return #line:993
    O00O0O0OOO000000O =input ("Enter the Guild ID: ").strip ()#line:995
    OO00O00O0O0000O00 =input ("Enter the rate limit between requests (in seconds): ").strip ()#line:996
    try :#line:998
        OO00O00O0O0000O00 =float (OO00O00O0O0000O00 )#line:999
        if OO00O00O0O0000O00 <0 :#line:1000
            raise ValueError #line:1001
    except ValueError :#line:1002
        print (f"{colorama.Fore.RED}    [!] Invalid rate limit. Using default rate limit of 5 seconds.{colorama.Fore.RESET}")#line:1003
        OO00O00O0O0000O00 =5.0 #line:1004
    OOOO0O0000OO00O0O =set ()#line:1006
    for O00OOOO0OOOOO0O0O in OO00O000O00000OOO :#line:1008
        O0O00000OO0O00OOO ={'Authorization':O00OOOO0OOOOO0O0O ,'Content-Type':'application/json'}#line:1012
        OO00O0000O0O00O00 =requests .get (f"https://discord.com/api/v9/guilds/{O00O0O0OOO000000O}/emojis",headers =O0O00000OO0O00OOO )#line:1015
        if OO00O0000O0O00O00 .status_code ==200 :#line:1016
            O0O00O00000OO0OO0 =OO00O0000O0O00O00 .json ()#line:1017
            for OOOOO000O0O0OOO0O in O0O00O00000OO0OO0 :#line:1018
                OOOO0O0000OO00O0O .add (OOOOO000O0O0OOO0O ['name'])#line:1019
        else :#line:1020
            print (f"{colorama.Fore.RED}    [!] Error fetching existing emojis: {OO00O0000O0O00O00.status_code} - {OO00O0000O0O00O00.text}{colorama.Fore.RESET}")#line:1021
            continue #line:1022
    for O0OOOO0OO00O0O0OO ,O0O0OO0O0O0OO0OO0 in zip (O0OOO0O00OOOO0OOO ,O00000O0OOO0O0OOO ):#line:1024
        if O0OOOO0OO00O0O0OO in OOOO0O0000OO00O0O :#line:1025
            print (f"{colorama.Fore.YELLOW}    [*] Emoji '{O0OOOO0OO00O0O0OO}' already exists. Skipping...{colorama.Fore.RESET}")#line:1026
            continue #line:1027
        for O00OOOO0OOOOO0O0O in OO00O000O00000OOO :#line:1029
            try :#line:1030
                OO00O0000O0O00O00 =requests .get (O0O0OO0O0O0OO0OO0 )#line:1031
                OO00O0000O0O00O00 .raise_for_status ()#line:1032
                O00O0000O00O0OOO0 =OO00O0000O0O00O00 .content #line:1033
                O00O0OO00000OO00O =base64 .b64encode (O00O0000O00O0OOO0 ).decode ('utf-8')#line:1034
                OOO0O0000O0OOOOOO ={'name':O0OOOO0OO00O0O0OO ,'image':f"data:image/png;base64,{O00O0OO00000OO00O}"}#line:1039
                O0O00000OO0O00OOO ={'Authorization':O00OOOO0OOOOO0O0O ,'Content-Type':'application/json'}#line:1044
                OO00OO000000O0O00 =requests .post (f"https://discord.com/api/v9/guilds/{O00O0O0OOO000000O}/emojis",headers =O0O00000OO0O00OOO ,json =OOO0O0000O0OOOOOO )#line:1046
                if OO00OO000000O0O00 .status_code ==201 :#line:1047
                    print (f"{colorama.Fore.GREEN}    [+] Successfully added emoji '{O0OOOO0OO00O0O0OO}' with token {O00OOOO0OOOOO0O0O}{colorama.Fore.RESET}")#line:1048
                    OOOO0O0000OO00O0O .add (O0OOOO0OO00O0O0OO )#line:1049
                    break #line:1050
                else :#line:1051
                    print (f"{colorama.Fore.RED}    [!] Failed to add emoji '{O0OOOO0OO00O0O0OO}' with token {O00OOOO0OOOOO0O0O}: {OO00OO000000O0O00.status_code} - {OO00OO000000O0O00.text}{colorama.Fore.RESET}")#line:1052
                time .sleep (OO00O00O0O0000O00 )#line:1054
            except Exception as OO000O0OO0OOO0000 :#line:1055
                print (f"{colorama.Fore.RED}    [!] Error adding emoji '{O0OOOO0OO00O0O0OO}' with token {O00OOOO0OOOOO0O0O}: {str(OO000O0OO0OOO0000)}{colorama.Fore.RESET}")#line:1056
def main ():#line:1058
    colorama .init ()#line:1059
    while True :#line:1060
        logo ()#line:1061
        OOOO0OOOOO0000O0O =input (f"{colorama.Fore.LIGHTMAGENTA_EX}    [Final] Select an option from above: ")#line:1062
        if OOOO0OOOOO0000O0O =="0":#line:1064
            update_group_ids ()#line:1065
        elif OOOO0OOOOO0000O0O =="1":#line:1066
            join_discord_invite ()#line:1067
        elif OOOO0OOOOO0000O0O =="2":#line:1068
            reaction_spammer ()#line:1069
        elif OOOO0OOOOO0000O0O =="3":#line:1070
            send_messages_with_mentions ()#line:1071
        elif OOOO0OOOOO0000O0O =="4":#line:1072
            spammer_menu ()#line:1073
        elif OOOO0OOOOO0000O0O =="5":#line:1074
            nickchanger ()#line:1075
        elif OOOO0OOOOO0000O0O =="6":#line:1076
            add_emojis_from_files ()#line:1077
        elif OOOO0OOOOO0000O0O =="7":#line:1078
            reaction_art ()#line:1079
        elif OOOO0OOOOO0000O0O =="0":#line:1080
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [*] Exiting the application. Goodbye!{colorama.Fore.RESET}")#line:1081
            break #line:1082
        else :#line:1083
            print (f"{colorama.Fore.RED}    [!] Invalid option selected!{colorama.Fore.RESET}")#line:1084
        input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:1086
if __name__ =="__main__":#line:1088
    main ()#line:1089
