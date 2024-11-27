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
    O0OOOO0O0OOOOOO0O =requests .Session ()#line:57
    if proxy :#line:58
        O0OOOO0O0OOOOOO0O .proxies ={"http":proxy ,"https":proxy }#line:59
    return O0OOOO0O0OOOOOO0O #line:60
def get_headers (O0000O0OOO00000O0 ):#line:62
    return {"Authorization":O0000O0OOO00000O0 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:67
def send_message_with_mention (O00O0000OO0OO00OO ,OOOO0OOO0OOOO000O ,O0OOOOOOO000OOOO0 ,O000000OO0O000000 ):#line:70
    OOO0O0O00O0O00OO0 =get_session ()#line:71
    O0000000OO00OOO0O =get_headers (O00O0000OO0OO00OO )#line:72
    if O000000OO0O000000 :#line:74
        OOOOOOOO00O0O0OOO =random .choice (O000000OO0O000000 )#line:75
        O0OOOOOOO000OOOO0 +=f" <@{OOOOOOOO00O0O0OOO}>"#line:76
    OOOOOO00OOO0000O0 =OOO0O0O00O0O00OO0 .post (f"https://discord.com/api/v9/channels/{OOOO0OOO0OOOO000O}/messages",headers =O0000000OO00OOO0O ,json ={"content":O0OOOOOOO000OOOO0 })#line:82
    if OOOOOO00OOO0000O0 .status_code in [200 ,201 ]:#line:83
        print (f"[+] Message sent to channel {OOOO0OOO0OOOO000O}")#line:84
    elif OOOOOO00OOO0000O0 .status_code ==429 :#line:85
        print ("[-] Rate limited. Please wait before retrying.")#line:86
        OOOOO0O0O0O0O0O00 =OOOOOO00OOO0000O0 .json ().get ("retry_after",1 )#line:87
        time .sleep (OOOOO0O0O0O0O0O00 )#line:88
    else :#line:89
        print (f"[!] Error occurred: {OOOOOO00OOO0000O0.status_code}")#line:90
def fetch_messages (OO00OOOOO00OOO0O0 ,O00O0O00O000OOOOO ,limit =100 ):#line:93
    OOO0OO0000O0OOOO0 ={"Authorization":OO00OOOOO00OOO0O0 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:98
    O00000OOO0O0000O0 =requests .get (f"https://discord.com/api/v9/channels/{O00O0O00O000OOOOO}/messages?limit={limit}",headers =OOO0OO0000O0OOOO0 )#line:102
    if O00000OOO0O0000O0 .status_code ==200 :#line:103
        return O00000OOO0O0000O0 .json ()#line:104
    else :#line:105
        print (f"[!] Failed to fetch messages. HTTP Status Code: {O00000OOO0O0000O0.status_code}")#line:106
        return []#line:107
import concurrent .futures #line:109
def reaction_spammer ():#line:111
    try :#line:112
        with open ("token.txt")as O0OOOOO0000OO0OO0 :#line:113
            OOOO00OO0OO0O0O0O =[O00OOOOO00O0OOOO0 .strip ()for O00OOOOO00O0OOOO0 in O0OOOOO0000OO0OO0 .readlines ()if O00OOOOO00O0OOOO0 .strip ()]#line:114
    except (FileNotFoundError ,KeyError ):#line:115
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:116
        return #line:117
    OO00O0OOOOOOO0O00 =input ("Server ID?: ").strip ()#line:119
    O00000OOOO00O000O =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:121
    if O00000OOOO00O000O =='2':#line:122
        O0O00OO000000O000 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:123
        O0O0OO0OOOO0O0000 =[OOOOOOO0000O0000O .strip ()for OOOOOOO0000O0000O in O0O00OO000000O000 if OOOOOOO0000O0000O .strip ()]#line:124
    else :#line:125
        O0O0OO0OOOO0O0000 =[]#line:126
        for OOO0O0OOO00OO0000 in OOOO00OO0OO0O0O0O :#line:127
            try :#line:128
                O0O0OO0OOOO0O0000 .extend (fetch_channels (OOO0O0OOO00OO0000 ,OO00O0OOOOOOO0O00 ))#line:129
            except Exception as O000O000O00OO00O0 :#line:130
                print (f"[!] Failed to fetch channels for token. Error: {O000O000O00OO00O0}")#line:131
                continue #line:132
    O0000O0OO000OOOOO =input ("Select your emoji (a, b, c, ... or custom emojis): ").strip ()#line:134
    OOO00000O0O0OOOOO =input ("Delay between reactions (in seconds)?: ").strip ()#line:135
    try :#line:137
        OOO00000O0O0OOOOO =float (OOO00000O0O0OOOOO )#line:138
        if OOO00000O0O0OOOOO <0 :#line:139
            raise ValueError #line:140
    except ValueError :#line:141
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:142
        OOO00000O0O0OOOOO =1.0 #line:143
    O0000OO0O00O00OO0 =[]#line:145
    for O00000OO000O0OOO0 in O0000O0OO000OOOOO .split (","):#line:146
        O00000OO000O0OOO0 =O00000OO000O0OOO0 .strip ().lower ()#line:147
        if O00000OO000O0OOO0 in alphabet_to_flag :#line:148
            O0000OO0O00O00OO0 .append (alphabet_to_flag [O00000OO000O0OOO0 ])#line:149
        else :#line:150
            O0000OO0O00O00OO0 .append (O00000OO000O0OOO0 )#line:151
    if not O0000OO0O00O00OO0 :#line:153
        print (f"{colorama.Fore.RED}    [!] No valid emojis provided!{colorama.Fore.RESET}")#line:154
        return #line:155
    def O0000O00OO0OOOO0O (OO0OO0OO0000OO00O ):#line:157
        for OO0000OO0O0O0O0OO in O0O0OO0OOOO0O0000 :#line:158
            try :#line:159
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {OO0000OO0O0O0O0OO}...{colorama.Fore.RESET}")#line:160
                O0O00O00OO00O0OO0 =fetch_messages (OO0OO0OO0000OO00O ,OO0000OO0O0O0O0OO ,limit =100 )#line:161
                if not O0O00O00OO00O0OO0 :#line:162
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:163
                    continue #line:164
                for OOO0OOO00O0OOOO0O in O0O00O00OO00O0OO0 :#line:166
                    for O0OO0O00OO0O0O0OO in O0000OO0O00O00OO0 :#line:167
                        reactionput (OO0OO0OO0000OO00O ,OO0000OO0O0O0O0OO ,OOO0OOO00O0OOOO0O ['id'],O0OO0O00OO0O0O0OO )#line:168
                        time .sleep (OOO00000O0O0OOOOO )#line:169
            except Exception as OO000O0OO0OOOOOO0 :#line:170
                print (f"[!] Error processing channel {OO0000OO0O0O0O0OO}. Error: {OO000O0OO0OOOOOO0}")#line:171
                continue #line:172
    with concurrent .futures .ThreadPoolExecutor ()as OO0OOO000O00O0O00 :#line:174
        O0O0O000O0OO0O0O0 =[OO0OOO000O00O0O00 .submit (O0000O00OO0OOOO0O ,O0000OOOOO00OOO00 )for O0000OOOOO00OOO00 in OOOO00OO0OO0O0O0O ]#line:175
        concurrent .futures .wait (O0O0O000O0OO0O0O0 )#line:176
import requests #line:179
import json #line:180
import time #line:181
import colorama #line:182
alphabet_to_flag ={'a':'🇦','b':'🇧','c':'🇨','d':'🇩','e':'🇪','f':'🇫','g':'🇬','h':'🇭','i':'🇮','j':'🇯','k':'🇰','l':'🇱','m':'🇲','n':'🇳','o':'🇴','p':'🇵','q':'🇶','r':'🇷','s':'🇸','t':'🇹','u':'🇺','v':'🇻','w':'🇼','x':'🇽','y':'🇾','z':'🇿'}#line:190
def fetch_channels (O0O0000OO0O00OOO0 ,O0O000OO0O0OOO000 ):#line:192
    OO0O00000OOO0000O =f"https://discord.com/api/v9/guilds/{O0O000OO0O0OOO000}/channels"#line:193
    O0OO0OO0O00000O0O ={"Authorization":O0O0000OO0O00OOO0 }#line:194
    O0O0OOO00OO00O00O =requests .get (OO0O00000OOO0000O ,headers =O0OO0OO0O00000O0O )#line:195
    if O0O0OOO00OO00O00O .status_code ==200 :#line:196
        return [O0O0O000OO0OOO0O0 ['id']for O0O0O000OO0OOO0O0 in O0O0OOO00OO00O00O .json ()if O0O0O000OO0OOO0O0 ['type']==0 ]#line:197
    else :#line:198
        raise Exception (f"Failed to fetch channels: {O0O0OOO00OO00O00O.status_code} - {O0O0OOO00OO00O00O.text}")#line:199
def fetch_messages (O00OO0OO0OOOOOO0O ,O000000OOO0O0O0OO ,limit =100 ):#line:201
    O00000OO0O0O0O000 =f"https://discord.com/api/v9/channels/{O000000OOO0O0O0OO}/messages?limit={limit}"#line:202
    OOOO0OOOOO0O000O0 ={"Authorization":O00OO0OO0OOOOOO0O }#line:203
    O00O0OO00O0OO000O =requests .get (O00000OO0O0O0O000 ,headers =OOOO0OOOOO0O000O0 )#line:204
    if O00O0OO00O0OO000O .status_code ==200 :#line:205
        return O00O0OO00O0OO000O .json ()#line:206
    else :#line:207
        print (f"[!] Failed to fetch messages: {O00O0OO00O0OO000O.status_code} - {O00O0OO00O0OO000O.text}")#line:208
        return []#line:209
def reactionput (O0OOO00000O0O0OOO ,O000O0O000OO00000 ,O00000000O0O00OOO ,OOOO00O0O000OOOOO ):#line:211
    O000O00000O0OO0O0 =f"https://discord.com/api/v9/channels/{O000O0O000OO00000}/messages/{O00000000O0O00OOO}/reactions/{OOOO00O0O000OOOOO}/@me"#line:212
    O0OOOOOOOOOOO00OO ={"Authorization":O0OOO00000O0O0OOO ,"Content-Type":"application/json"}#line:213
    OOO000OOO0OO0000O =requests .put (O000O00000O0OO0O0 ,headers =O0OOOOOOOOOOO00OO )#line:214
    if OOO000OOO0OO0000O .status_code not in [204 ,200 ]:#line:215
        print (f"{colorama.Fore.RED}    [!] Failed to add reaction: {OOO000OOO0OO0000O.status_code} - {OOO000OOO0OO0000O.text}{colorama.Fore.RESET}")#line:216
import random #line:218
def reaction_art ():#line:220
    try :#line:221
        with open ("token.txt",encoding ="utf-8")as O0000OO0OO0OO0OOO :#line:222
            O00O00OOO0OOOO000 =[O000000O0OOOO0OO0 .strip ()for O000000O0OOOO0OO0 in O0000OO0OO0OO0OOO .readlines ()if O000000O0OOOO0OO0 .strip ()]#line:223
    except (FileNotFoundError ,KeyError ):#line:224
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:225
        return #line:226
    O0OOO00000O0000OO =input ("Server ID?: ").strip ()#line:228
    OOOOOOO0000O0O0OO =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:230
    if OOOOOOO0000O0O0OO =='2':#line:231
        O000O00O00OOOOOOO =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:232
        O0OOO0OO0O0O00000 =[O0OO0000OO0OOOO00 .strip ()for O0OO0000OO0OOOO00 in O000O00O00OOOOOOO if O0OO0000OO0OOOO00 .strip ()]#line:233
    else :#line:234
        O0OOO0OO0O0O00000 =[]#line:235
        for OO0OO0000OOO00000 in O00O00OOO0OOOO000 :#line:236
            try :#line:237
                O0OOO0OO0O0O00000 .extend (fetch_channels (OO0OO0000OOO00000 ,O0OOO00000O0000OO ))#line:238
            except Exception as O0OOO0O0OOO000OO0 :#line:239
                print (f"[!] Failed to fetch channels for token. Error: {O0OOO0O0OOO000OO0}")#line:240
                continue #line:241
        random .shuffle (O0OOO0OO0O0O00000 )#line:242
    OOO000O0OOOO0000O =input ("Delay between reactions (in seconds)?: ").strip ()#line:244
    try :#line:246
        OOO000O0OOOO0000O =float (OOO000O0OOOO0000O )#line:247
        if OOO000O0OOOO0000O <0 :#line:248
            raise ValueError #line:249
    except ValueError :#line:250
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:251
        OOO000O0OOOO0000O =1.0 #line:252
    try :#line:254
        with open ("art.txt",encoding ="utf-8")as O0O0O0000OO0OO000 :#line:255
            O00O000OOOOOO0OO0 =[OOO0OO0O0OO0O00O0 .strip ()for OOO0OO0O0OO0O00O0 in O0O0O0000OO0OO000 .readlines ()if OOO0OO0O0OO0O00O0 .strip ()]#line:256
    except (FileNotFoundError ,KeyError ):#line:257
        print (f"{colorama.Fore.RED}    [!] Error: art.txt file not found or empty!{colorama.Fore.RESET}")#line:258
        return #line:259
    except UnicodeDecodeError as O0OOO0O0OOO000OO0 :#line:260
        print (f"{colorama.Fore.RED}    [!] Error decoding art.txt: {str(O0OOO0O0OOO000OO0)}{colorama.Fore.RESET}")#line:261
        return #line:262
    if not O00O000OOOOOO0OO0 :#line:264
        print (f"{colorama.Fore.RED}    [!] No valid art provided in art.txt!{colorama.Fore.RESET}")#line:265
        return #line:266
    O00O000OOOOOO0OO0 .reverse ()#line:269
    for OO0OO0000OOO00000 in O00O00OOO0OOOO000 :#line:271
        for O0OO0OOOO0OO0O00O in O0OOO0OO0O0O00000 :#line:272
            try :#line:273
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {O0OO0OOOO0OO0O00O}...{colorama.Fore.RESET}")#line:274
                O00000OO00000OOOO =fetch_messages (OO0OO0000OOO00000 ,O0OO0OOOO0OO0O00O ,limit =100 )#line:277
                if not O00000OO00000OOOO :#line:278
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:279
                    continue #line:280
                for O0OOOO0O0O00OO00O ,O000000OOO0OO0OO0 in enumerate (O00000OO00000OOOO ):#line:283
                    OOO0OO0O00O00OO0O =O00O000OOOOOO0OO0 [O0OOOO0O0O00OO00O %len (O00O000OOOOOO0OO0 )].split (',')#line:284
                    for OO0OO0OO00O00O0O0 in OOO0OO0O00O00OO0O :#line:285
                        reactionput (OO0OO0000OOO00000 ,O0OO0OOOO0OO0O00O ,O000000OOO0OO0OO0 ['id'],OO0OO0OO00O00O0O0 .strip ())#line:286
                        print (f"Adding reaction '{OO0OO0OO00O00O0O0.strip()}' to message {O000000OOO0OO0OO0['id']} in channel {O0OO0OOOO0OO0O00O}")#line:287
                        time .sleep (OOO000O0OOOO0000O )#line:288
            except Exception as O0OOO0O0OOO000OO0 :#line:289
                print (f"[!] Error processing channel {O0OO0OOOO0OO0O00O}. Error: {O0OOO0O0OOO000OO0}")#line:290
                continue #line:291
    def OO0O0O0000O0O0O0O (O000O000OOO0000O0 ):#line:296
        for O00OOOOOOO0OO0O00 in O0OOO0OO0O0O00000 :#line:297
            try :#line:298
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {O00OOOOOOO0OO0O00}...{colorama.Fore.RESET}")#line:299
                OOOOO0O00O0O0OOO0 =fetch_messages (O000O000OOO0000O0 ,O00OOOOOOO0OO0O00 ,limit =100 )#line:300
                if not OOOOO0O00O0O0OOO0 :#line:301
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:302
                    continue #line:303
                for O00OO0OO0O0000O0O in OOOOO0O00O0O0OOO0 :#line:305
                    for O0O0OOO0O0OOO0O0O in OOO0OO0O00O00OO0O :#line:306
                        reactionput (O000O000OOO0000O0 ,O00OOOOOOO0OO0O00 ,O00OO0OO0O0000O0O ['id'],O0O0OOO0O0OOO0O0O )#line:307
                        time .sleep (OOO000O0OOOO0000O )#line:308
            except Exception as OO0O000OO00OOO000 :#line:309
                print (f"[!] Error processing channel {O00OOOOOOO0OO0O00}. Error: {OO0O000OO00OOO000}")#line:310
                continue #line:311
    with concurrent .futures .ThreadPoolExecutor ()as OO000O0O0O00O00OO :#line:313
        O000O0OO0000O0O00 =[OO000O0O0O00O00OO .submit (OO0O0O0000O0O0O0O ,OOO0O0OO0OO0O000O )for OOO0O0OO0OO0O000O in O00O00OOO0OOOO000 ]#line:314
        concurrent .futures .wait (O000O0OO0000O0O00 )#line:315
def update_group_ids ():#line:318
    try :#line:319
        with open ("token.txt")as OOO00000OOOO0000O :#line:320
            O000OOO00OO0O00OO =[O0O0000OOO00O00OO .strip ()for O0O0000OOO00O00OO in OOO00000OOOO0000O .readlines ()if O0O0000OOO00O00OO .strip ()]#line:321
        OO00000000O0O0OO0 =O000OOO00OO0O00OO [0 ]#line:322
    except (FileNotFoundError ,KeyError ):#line:323
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:324
        return #line:325
    OOO0OO00OOOO0OO00 ={"Authorization":OO00000000O0O0OO0 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:331
    O00000O00OO0OO0O0 =requests .get ('https://discord.com/api/v9/users/@me/channels',headers =OOO0OO00OOOO0OO00 )#line:333
    if O00000O00OO0OO0O0 .status_code ==200 :#line:334
        O0OO0O000O0O0O0O0 =O00000O00OO0OO0O0 .json ()#line:335
        with open ("group_id.txt","w")as OO0OOO00O0O0OOOO0 :#line:336
            for OOOOO0O00OOOO0OOO in O0OO0O000O0O0O0O0 :#line:337
                if OOOOO0O00OOOO0OOO ['type']==3 :#line:338
                    OO0OOO00O0O0OOOO0 .write (OOOOO0O00OOOO0OOO ['id']+'\n')#line:339
        print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Group IDs updated successfully.{colorama.Fore.RESET}")#line:340
    else :#line:341
        print (f"{colorama.Fore.LIGHTRED_EX}    [!] Failed to retrieve group IDs. HTTP Status Code: {O00000O00OO0OO0O0.status_code}{colorama.Fore.RESET}")#line:342
import requests #line:344
import requests #line:346
def fetch_channels (O000OO00O000000O0 ,O00OO00000000O000 ):#line:348
    try :#line:349
        OO0OO0O00OO00OOOO =requests .Session ()#line:350
        O0OOO00OO0O000O0O =get_headers (O000OO00O000000O0 )#line:351
        O0O000OOOO0000OOO =OO0OO0O00OO00OOOO .get (f"https://discord.com/api/v9/guilds/{O00OO00000000O000}/channels",headers =O0OOO00OO0O000O0O ,timeout =10 )#line:358
        if O0O000OOOO0000OOO .status_code ==200 :#line:361
            try :#line:362
                OOOO0OOOO00O00O00 =O0O000OOOO0000OOO .json ()#line:363
                return [O00O0OOOOO00OOO0O ['id']for O00O0OOOOO00OOO0O in OOOO0OOOO00O00O00 if O00O0OOOOO00OOO0O .get ('type')==0 ]#line:364
            except ValueError :#line:365
                print ("[!] Error: Response was not valid JSON.")#line:366
                return []#line:367
        elif O0O000OOOO0000OOO .status_code ==401 :#line:368
            print ("[!] Error: Unauthorized - check your token.")#line:369
        elif O0O000OOOO0000OOO .status_code ==403 :#line:370
            print ("[!] Error: Forbidden - you lack permissions.")#line:371
        elif O0O000OOOO0000OOO .status_code ==404 :#line:372
            print ("[!] Error: Server not found - check the server ID.")#line:373
        else :#line:374
            print (f"[!] Error: Unexpected status code {O0O000OOOO0000OOO.status_code}.")#line:375
        return []#line:378
    except requests .exceptions .Timeout :#line:380
        print ("[!] Error: Request timed out. Check your connection or try again later.")#line:381
        return []#line:382
    except requests .exceptions .RequestException as O0OO0O0O00O00OO00 :#line:383
        print (f"[!] Error: An error occurred while fetching channels: {O0OO0O0O00O00OO00}")#line:384
        return []#line:385
def extract_uids_from_messages (OOOOOOOOO000O0OO0 ):#line:391
    OO0O0O00OOO0O00OO =set ()#line:392
    for O00OOOO0000O0OO0O in OOOOOOOOO000O0OO0 :#line:393
        OO0O0O00OOO0O00OO .add (O00OOOO0000O0OO0O ['author']['id'])#line:394
    return list (OO0O0O00OOO0O00OO )#line:395
def send_message_with_mention (O0O0O0OO00OO000OO ,O0O0OOOOOO0000OOO ,O0OOOO0O00000OO00 ,O000O000OOO0000OO ):#line:397
    OO0OOOOOO000000O0 =get_session ()#line:398
    OO000O0000O000000 =get_headers (O0O0O0OO00OO000OO )#line:399
    if O000O000OOO0000OO :#line:401
        O0O00O000OOOO0000 =random .choice (O000O000OOO0000OO )#line:402
        O0OOOO0O00000OO00 +=f" <@{O0O00O000OOOO0000}>"#line:403
    O0O00O0O00000OO00 =OO0OOOOOO000000O0 .post (f"https://discord.com/api/v9/channels/{O0O0OOOOOO0000OOO}/messages",headers =OO000O0000O000000 ,json ={"content":O0OOOO0O00000OO00 })#line:409
    if O0O00O0O00000OO00 .status_code in [200 ,201 ]:#line:410
        print (f"[+] Message sent to channel {O0O0OOOOOO0000OOO}")#line:411
    elif O0O00O0O00000OO00 .status_code ==429 :#line:412
        print ("[-] Rate limited. Please wait before retrying.")#line:413
        OOO0OO00O00000000 =O0O00O0O00000OO00 .json ().get ("retry_after",1 )#line:414
        time .sleep (OOO0OO00O00000000 )#line:415
    else :#line:416
        print (f"[!] Error occurred: {O0O00O0O00000OO00.status_code}")#line:417
def send_messages_with_mentions ():#line:418
    try :#line:419
        with open ("token.txt")as OO0O0OO000000O000 :#line:420
            OO00O0O0OOO000OO0 =[OO00OOO0000000O00 .strip ()for OO00OOO0000000O00 in OO0O0OO000000O000 .readlines ()if OO00OOO0000000O00 .strip ()]#line:421
    except (FileNotFoundError ,KeyError ):#line:422
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:423
        return #line:424
    O0OO00O0O0OO0O00O =input ("Server ID?: ").strip ()#line:426
    OO00O0O00O00OO000 =input ("Delay between messages (in seconds)?: ").strip ()#line:427
    OO0O000OO0OOOOO00 =input ("Number of messages to send?: ").strip ()#line:428
    O0O0OO0O00O00OOOO =input ("Message content?: ").strip ()#line:429
    OO0OO0O0O00OOO0OO =input ("Blacklist User IDs (comma-separated)?: ").strip ().split (',')#line:430
    OO0OO0O0O00OOO0OO =[OO0OOO00O000O0O00 .strip ()for OO0OOO00O000O0O00 in OO0OO0O0O00OOO0OO if OO0OOO00O000O0O00 .strip ()]#line:431
    try :#line:433
        OO00O0O00O00OO000 =float (OO00O0O00O00OO000 )#line:434
        if OO00O0O00O00OO000 <0 :#line:435
            raise ValueError #line:436
    except ValueError :#line:437
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:438
        OO00O0O00O00OO000 =1.0 #line:439
    try :#line:441
        OO0O000OO0OOOOO00 =int (OO0O000OO0OOOOO00 )#line:442
        if OO0O000OO0OOOOO00 <=0 :#line:443
            raise ValueError #line:444
    except ValueError :#line:445
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:446
        OO0O000OO0OOOOO00 =1 #line:447
    OOO0000O0O00O0OO0 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:449
    if OOO0000O0O00O0OO0 =='2':#line:450
        O00OO0O000000OOO0 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:451
        O00OO0O000000OOO0 =[OOOOO000OO0OOO0OO .strip ()for OOOOO000OO0OOO0OO in O00OO0O000000OOO0 if OOOOO000OO0OOO0OO .strip ()]#line:452
    else :#line:453
        O00OO0O000000OOO0 =[]#line:454
    OOOOO000000000OO0 =set ()#line:456
    for O00000000O00O0OO0 in OO00O0O0OOO000OO0 :#line:457
        O000O0O00OO0OOO0O =fetch_channels (O00000000O00O0OO0 ,O0OO00O0O0OO0O00O )#line:458
        for O00OO00O00O0O0OO0 in O000O0O00OO0OOO0O :#line:459
            OOOOO00000OOO0000 =fetch_messages (O00000000O00O0OO0 ,O00OO00O00O0O0OO0 ,limit =100 )#line:460
            O000OOO00O0O0O0OO =extract_uids_from_messages (OOOOO00000OOO0000 )#line:461
            OOOOO000000000OO0 .update (O000OOO00O0O0O0OO )#line:462
    OOOOO000000000OO0 =list (set (OOOOO000000000OO0 )-set (OO0OO0O0O00OOO0OO ))#line:465
    for _OO0O0OO00OO0OO0OO in range (OO0O000OO0OOOOO00 ):#line:467
        for O00000000O00O0OO0 in OO00O0O0OOO000OO0 :#line:468
            if O00OO0O000000OOO0 :#line:469
                O000O0O00OO0OOO0O =O00OO0O000000OOO0 #line:470
            for O00OO00O00O0O0OO0 in O000O0O00OO0OOO0O :#line:471
                send_message_with_mention (O00000000O00O0OO0 ,O00OO00O00O0O0OO0 ,O0O0OO0O00O00OOOO ,OOOOO000000000OO0 )#line:472
                time .sleep (OO00O0O00O00OO000 )#line:473
def join_discord_invite ():#line:478
    try :#line:479
        with open ("token.txt")as OOO0O0O00O00000O0 :#line:480
            OOOOOO0O00000O0O0 =[O00OOOOO0OO0O00O0 .strip ()for O00OOOOO0OO0O00O0 in OOO0O0O00O00000O0 .readlines ()if O00OOOOO0OO0O00O0 .strip ()]#line:481
    except (FileNotFoundError ,KeyError ):#line:482
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:483
        return #line:484
    OOOO000OO00O000O0 =input ("Invite Code?: discord.gg/").strip ()#line:486
    for O00OO0OOO000O0000 in OOOOOO0O00000O0O0 :#line:489
        joiner (O00OO0OOO000O0000 ,OOOO000OO00O000O0 )#line:490
import json ,time ,base64 ,random ,requests #line:492
def cookieset (O0O0OOOO0OO0OOO0O ):#line:494
    O00000OO0O00OO000 =O0O0OOOO0OO0OOO0O .get ("https://discord.com/app")#line:495
    return O00000OO0O00OO000 .cookies .get_dict ()#line:496
def generatexspandua (OOO00OO0OO0OO00O0 ):#line:498
    O0OO0O0000OO0OOOO =["Android","Windows","Macintosh"]#line:499
    O0OO0OO0OOOOOOO0O =random .choice (O0OO0O0000OO0OOOO )#line:500
    if O0OO0OO0OOOOOOO0O =="Macintosh":#line:501
        O0O00OO0000OO00O0 =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:502
        OOOOOO0OOOOOOO0O0 ="Macintosh; Intel Mac OS X "+O0O00OO0000OO00O0 #line:503
        O0OOO0OO0O00O0OOO ="x86_64"#line:504
    elif O0OO0OO0OOOOOOO0O =="Windows":#line:505
        O0O00OO0000OO00O0 =f'{random.choice([6.0, 10.0, 11.0])}'#line:506
        OOOOOO0OOOOOOO0O0 ="Windows NT "+O0O00OO0000OO00O0 +" Win64; x64"#line:507
        O0OOO0OO0O00O0OOO ="x86_64"#line:508
    else :#line:509
        O0O00OO0000OO00O0 ="13"#line:510
        OOOOOO0OOOOOOO0O0 =f"Linux; Android 13; Pixel 6a"#line:511
        O0OOO0OO0O00O0OOO ="aarch64"#line:512
    O0O0OOO0O0000OO0O ={"os":O0OO0OO0OOOOOOO0O ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":O0O00OO0000OO00O0 ,"os_arch":O0OOO0OO0O00O0OOO ,"system_locale":"ja-JP","client_build_number":OOO00OO0OO0OO00O0 ,"client_event_source":None ,"design_id":0 }#line:525
    OO0OO000OO0000O0O =f"Mozilla/5.0 ({OOOOOO0OOOOOOO0O0}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:526
    return base64 .b64encode (json .dumps (O0O0OOO0O0000OO0O ,separators =(',',':')).encode ()).decode (),OO0OO000OO0000O0O #line:527
def joiner (OOO000OO000OOOO0O ,O0O000O00O0O0O00O ,OOOO000O0O0OO0O0O ,O0O0O0O0OO0O000O0 ):#line:529
  OOO0OO0O00000OO00 =get_session (OOOO000O0O0OO0O0O )#line:530
  OO0OOO000000O00O0 =cookieset (OOO0OO0O00000OO00 )#line:531
  OO0OOO000000O00O0 ["locale"]="ja-JP"#line:532
  OOOOOO00O0OOO0OOO =201211 #line:533
  O0O0O0OO00OOO0O00 ,O00OO0OO00OO00OOO =generatexspandua (OOOOOO00O0OOO0OOO )#line:534
  O0OOOOO0OOO000O00 ={"Authorization":OOO000OO000OOOO0O ,"accept":"*/*","accept-language":"ja-JP","connection":"keep-alive","DNT":"1","origin":"https://discord.com","sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","referer":"https://discord.com/channels/@me","TE":"Trailers","user-agent":O00OO0OO00OO00OOO ,"X-Super-Properties":O0O0O0OO00OOO0O00 ,}#line:549
  O0OOOOOOOO0O0O0O0 =OOO0OO0O00000OO00 .post ("https://discord.com/api/v9/invites/"+O0O000O00O0O0O00O ,headers =O0OOOOO0OOO000O00 ,json ={},cookies =OO0OOO000000O00O0 )#line:551
  if O0OOOOOOOO0O0O0O0 .status_code ==200 :#line:552
    print ("[+] Probably joined "+OOO000OO000OOOO0O )#line:553
    if "show_verification_form"in O0OOOOOOOO0O0O0O0 .json ():#line:554
      bypass (OOO000OO000OOOO0O ,O0OOOOOOOO0O0O0O0 .json ()["guild"]["id"],OOO0OO0O00000OO00 ,O0OOOOO0OOO000O00 )#line:555
    return #line:556
  elif "captcha_key"in O0OOOOOOOO0O0O0O0 .text and O0OOOOOOOO0O0O0O0 .status_code ==400 :#line:557
    print ("[!] Hcaptcha interference "+OOO000OO000OOOO0O )#line:558
    return #line:559
  elif O0OOOOOOOO0O0O0O0 .status_code ==401 :#line:560
    print ("[!] Token is dead "+OOO000OO000OOOO0O )#line:561
    return #line:562
  elif O0OOOOOOOO0O0O0O0 .status_code ==403 :#line:563
    if "message"in O0OOOOOOOO0O0O0O0 .json ():#line:564
      if O0OOOOOOOO0O0O0O0 .json ()["message"]=="Unknown Message":#line:565
        print ("[!] Unknown error "+OOO000OO000OOOO0O )#line:566
        return #line:567
      else :#line:568
        print ("[!] Verification required "+OOO000OO000OOOO0O )#line:569
        return #line:570
    else :#line:571
      print ("[!] Error occurred "+OOO000OO000OOOO0O )#line:572
      return #line:573
  elif O0OOOOOOOO0O0O0O0 .status_code ==429 :#line:574
    print ("[!] Token rate-limited "+OOO000OO000OOOO0O )#line:575
    return #line:576
  elif O0OOOOOOOO0O0O0O0 .status_code ==400 :#line:577
    if "captcha_key"in O0OOOOOOOO0O0O0O0 .json ():#line:578
      print ("[!] Hcaptcha interference "+OOO000OO000OOOO0O )#line:579
      return #line:580
    else :#line:581
      print ("[!] Error occurred "+OOO000OO000OOOO0O )#line:582
      return #line:583
  elif O0OOOOOOOO0O0O0O0 .status_code ==401 :#line:584
    print ("[!] Token is dead "+OOO000OO000OOOO0O )#line:585
    return #line:586
  elif O0OOOOOOOO0O0O0O0 .status_code ==403 :#line:587
    if "message"in O0OOOOOOOO0O0O0O0 .json ():#line:588
      if O0OOOOOOOO0O0O0O0 .json ()["message"]=="Unknown Message":#line:589
        print ("[!] Unknown error "+OOO000OO000OOOO0O )#line:590
        return #line:591
      else :#line:592
        print ("[!] Verification required "+OOO000OO000OOOO0O )#line:593
        return #line:594
    else :#line:595
      print ("[!] Error occurred "+OOO000OO000OOOO0O )#line:596
  elif O0OOOOOOOO0O0O0O0 .status_code ==429 :#line:597
    print ("[!] Token rate-limited "+OOO000OO000OOOO0O )#line:598
    return #line:599
  else :#line:600
    print ("[!] Error occurred "+OOO000OO000OOOO0O )#line:601
    return #line:602
def update_group_ids ():#line:605
    OO00OO000OOOO0O00 =input ("Invite Code?: ").strip ()#line:606
    try :#line:607
        with open ("token.txt")as O000OO0O00OO0OOO0 :#line:608
            O00O00O0OO0OOO000 =[O00OOO0O0OO0000O0 .strip ()for O00OOO0O0OO0000O0 in O000OO0O00OO0OOO0 .readlines ()if O00OOO0O0OO0000O0 .strip ()]#line:609
    except (FileNotFoundError ,KeyError ):#line:610
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:611
        return #line:612
    O0000O00O0O000OO0 =requests .Session ()#line:614
    for O00O00000O0OO00OO in O00O00O0OO0OOO000 :#line:615
        joiner (O00O00000O0OO00OO ,OO00OO000OOOO0O00 ,O0000O00O0O000OO0 )#line:616
        time .sleep (2 )#line:617
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:619
def bypass (O0OOO00O000000000 ,O0000O0OOOO0O0OOO ,O0O0000OO0OOO0OO0 ,OOO0OO0OOO0OOO00O ):#line:622
    try :#line:623
        O00OOOOOOOO000OO0 =O0O0000OO0OOO0OO0 .get (f"https://discord.com/api/v9/guilds/{O0000O0OOOO0O0OOO}/member-verification?with_guild=false",headers =OOO0OO0OOO0OOO00O ).json ()#line:624
        O000O00O0OO00O0O0 =O0O0000OO0OOO0OO0 .put (f"https://discord.com/api/v9/guilds/{O0000O0OOOO0O0OOO}/requests/@me",headers =OOO0OO0OOO0OOO00O ,json =O00OOOOOOOO000OO0 )#line:625
        if O000O00O0OO00O0O0 .status_code ==201 :#line:626
            print (f"[+] MemberscreeningBypassed {O0OOO00O000000000}")#line:627
            return #line:628
        else :#line:629
            print (f"[!] Bypassが出来ませんでした {O0OOO00O000000000}")#line:630
            return #line:631
    except Exception as O0OO000OO0OO00OO0 :#line:632
        print (f"[!] エラーが発生しました。{O0OO000OO0OO00OO0}")#line:633
session =requests .Session ()#line:635
def reactionput (OO0OO0O00O0OOO00O ,OOO00000000OO000O ,OOO00OO000OO000O0 ,OO0OOOO00OOO0O0OO ,proxy =None ):#line:638
    OO00OOOO0OO00OOO0 =get_session (proxy )#line:639
    O0OOO0OOO00OO00OO =get_headers (OO00OOOO0OO00OOO0 )#line:640
    O0OOO0OOO00OO00OO ["Authorization"]=OO0OO0O00O0OOO00O #line:641
    OO0OOOO00OOO0O0OO =requests .utils .quote (OO0OOOO00OOO0O0OO )#line:643
    O0O000O000OOOOOO0 =OO00OOOO0OO00OOO0 .put (f"https://discord.com/api/v9/channels/{OOO00000000OO000O}/messages/{OOO00OO000OO000O0}/reactions/{OO0OOOO00OOO0O0OO}/%40me?location=Message&type=0",headers =O0OOO0OOO00OO00OO )#line:647
    if O0O000O000OOOOOO0 .status_code in [200 ,204 ]:#line:648
        print (f"[+] Reaction '{OO0OOOO00OOO0O0OO}' added successfully to message {OOO00OO000OO000O0}")#line:649
    elif O0O000O000OOOOOO0 .status_code ==429 :#line:650
        print ("[-] Rate limited. Please wait before retrying.")#line:651
        OOO0OO0O00O0OOOOO =O0O000O000OOOOOO0 .json ().get ("retry_after",1 )#line:652
        time .sleep (OOO0OO0O00O0OOOOO )#line:653
    elif O0O000O000OOOOOO0 .status_code ==401 :#line:654
        print ("[-] Invalid or expired token.")#line:655
    else :#line:656
        print (f"[!] Error occurred: {O0O000O000OOOOOO0.status_code}")#line:657
def generatexspandua (O0O00O0O00O00OOOO ):#line:660
  O0O00OOOOO0O0OO00 =["Android","Windows","Macintosh"]#line:661
  OO0O0O00O00OOO00O =random .choice (O0O00OOOOO0O0OO00 )#line:662
  if OO0O0O00O00OOO00O =="Macintosh":#line:663
    O00OOO000OO0O000O =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:664
    OOOO0OOOO0OO0000O ="Macintosh; Intel Mac OS X "+O00OOO000OO0O000O #line:665
    O0OO0O00OOOOOOOO0 ="x86_64"#line:666
  if OO0O0O00O00OOO00O =="Windows":#line:667
    O00OOO000OO0O000O =f'{random.choice([6.0,10.0,11.0])}'#line:668
    OOOO0OOOO0OO0000O ="Windows NT "+O00OOO000OO0O000O +" Win64; x64"#line:669
    O0OO0O00OOOOOOOO0 ="x86_64"#line:670
  if OO0O0O00O00OOO00O =="Android":#line:671
    O00OOO000OO0O000O ="13"#line:672
    OOOO0OOOO0OO0000O =f"Linux; Android 13; Pixel 6a"#line:673
    O0OO0O00OOOOOOOO0 ="aarch64"#line:674
  OO0OO00O0OO00OOOO ={"os":OO0O0O00O00OOO00O ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":O00OOO000OO0O000O ,"os_arch":O0OO0O00OOOOOOOO0 ,"system_locale":"ja-JP","client_build_number":O0O00O0O00O00OOOO ,"client_event_source":None ,"design_id":0 }#line:675
  OO0OO00OOO00OO000 =f"Mozilla/5.0 ({OOOO0OOOO0OO0000O}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:676
  return base64 .b64encode (json .dumps (OO0OO00O0OO00OOOO ,separators =(',',':')).encode ()).decode (),OO0OO00OOO00OO000 #line:677
import base64 #line:679
def nickchanger ():#line:682
    try :#line:683
        with open ("token.txt")as OO0OO00OOO0OOOO00 :#line:684
            OO0000OOO0OOO0OO0 =[OOOOOOO0OOO00O0O0 .strip ()for OOOOOOO0OOO00O0O0 in OO0OO00OOO0OOOO00 .readlines ()if OOOOOOO0OOO00O0O0 .strip ()]#line:685
    except (FileNotFoundError ,KeyError ):#line:686
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:687
        return #line:688
    O000O0O000O000OO0 =input ("Server ID?: ").strip ()#line:690
    O0O00OOO00O0OOOO0 =input ("Nickname?: ").strip ()#line:691
    OOO00OO00OOOO0O0O =input ("Delay (in seconds)?: ").strip ()#line:692
    try :#line:694
        OOO00OO00OOOO0O0O =float (OOO00OO00OOOO0O0O )#line:695
        if OOO00OO00OOOO0O0O <0 :#line:696
            raise ValueError #line:697
    except ValueError :#line:698
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:699
        OOO00OO00OOOO0O0O =1.0 #line:700
    for OO00OOOOO00O0OOOO in OO0000OOO0OOO0OO0 :#line:702
        O0O00O00OO0O0O0O0 ={"Authorization":OO00OOOOO00O0OOOO ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:707
        O00O0O0O0OOO0OOOO ={"nick":O0O00OOO00O0OOOO0 }#line:708
        O00O00O0OO0O00O0O =requests .patch (f"https://discord.com/api/v9/guilds/{O000O0O000O000OO0}/members/@me",headers =O0O00O00OO0O0O0O0 ,json =O00O0O0O0OOO0OOOO )#line:709
        if O00O00O0OO0O00O0O .status_code ==200 :#line:711
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Nickname changed to '{O0O00OOO00O0OOOO0}' successfully for token {OO00OOOOO00O0OOOO}.{colorama.Fore.RESET}")#line:712
        elif O00O00O0OO0O00O0O .status_code ==429 :#line:713
            print (f"{colorama.Fore.RED}    [!] Rate limited. Please wait before retrying for token {OO00OOOOO00O0OOOO}.{colorama.Fore.RESET}")#line:714
            O0O00O0000OO0000O =O00O00O0OO0O00O0O .json ().get ("retry_after",1 )#line:715
            time .sleep (O0O00O0000OO0000O )#line:716
        else :#line:717
            print (f"{colorama.Fore.RED}    [!] Error occurred: {O00O00O0OO0O00O0O.status_code} for token {OO00OOOOO00O0OOOO}.{colorama.Fore.RESET}")#line:718
        time .sleep (OOO00OO00OOOO0O0O )#line:720
import json ,websocket ,threading ,tls_client ,random ,time #line:724
session =tls_client .Session (client_identifier ="chrome112",random_tls_extension_order =True )#line:726
class Utils :#line:728
    @staticmethod #line:729
    def rangeCorrector (OO0O00O00O0OOO000 ):#line:730
        if [0 ,99 ]not in OO0O00O00O0OOO000 :#line:731
            OO0O00O00O0OOO000 .insert (0 ,[0 ,99 ])#line:732
        return OO0O00O00O0OOO000 #line:733
    @staticmethod #line:735
    def getRanges (O0O000OOO00O000OO ,OOO0O0OOOO0000OO0 ,O0O0000OO0O0OOO00 ):#line:736
        O0OOO0OOO0O000000 =int (O0O000OOO00O000OO *OOO0O0OOOO0000OO0 )#line:737
        OOOO00OOO0OO0000O =[[O0OOO0OOO0O000000 ,O0OOO0OOO0O000000 +99 ]]#line:738
        if O0O0000OO0O0OOO00 >O0OOO0OOO0O000000 +99 :#line:739
            OOOO00OOO0OO0000O .append ([O0OOO0OOO0O000000 +100 ,O0OOO0OOO0O000000 +199 ])#line:740
        return Utils .rangeCorrector (OOOO00OOO0OO0000O )#line:741
    @staticmethod #line:743
    def parseGuildMemberListUpdate (O0O0O00O0OOO00O0O ):#line:744
        O000OO00O0O0OO0OO ={"online_count":O0O0O00O0OOO00O0O ["d"]["online_count"],"member_count":O0O0O00O0OOO00O0O ["d"]["member_count"],"id":O0O0O00O0OOO00O0O ["d"]["id"],"guild_id":O0O0O00O0OOO00O0O ["d"]["guild_id"],"hoisted_roles":O0O0O00O0OOO00O0O ["d"]["groups"],"types":[],"locations":[],"updates":[],}#line:754
        for OOO00OOO0O0OO0000 in O0O0O00O0OOO00O0O ["d"]["ops"]:#line:756
            O000OO00O0O0OO0OO ["types"].append (OOO00OOO0O0OO0000 ["op"])#line:757
            if OOO00OOO0O0OO0000 ["op"]in ("SYNC","INVALIDATE"):#line:758
                O000OO00O0O0OO0OO ["locations"].append (OOO00OOO0O0OO0000 ["range"])#line:759
                if OOO00OOO0O0OO0000 ["op"]=="SYNC":#line:760
                    O000OO00O0O0OO0OO ["updates"].append (OOO00OOO0O0OO0000 ["items"])#line:761
                else :#line:762
                    O000OO00O0O0OO0OO ["updates"].append ([])#line:763
            elif OOO00OOO0O0OO0000 ["op"]in ("INSERT","UPDATE","DELETE"):#line:764
                O000OO00O0O0OO0OO ["locations"].append (OOO00OOO0O0OO0000 ["index"])#line:765
                if OOO00OOO0O0OO0000 ["op"]=="DELETE":#line:766
                    O000OO00O0O0OO0OO ["updates"].append ([])#line:767
                else :#line:768
                    O000OO00O0O0OO0OO ["updates"].append (OOO00OOO0O0OO0000 ["item"])#line:769
        return O000OO00O0O0OO0OO #line:770
class DiscordSocket (websocket .WebSocketApp ):#line:772
    def __init__ (OO00O0O00000OOOOO ,OO00O00000000O00O ,O0OOO0OO00OOO000O ,OOO00O00O000OO000 ):#line:773
        OO00O0O00000OOOOO .token =OO00O00000000O00O #line:774
        OO00O0O00000OOOOO .guild_id =O0OOO0OO00OOO000O #line:775
        OO00O0O00000OOOOO .channel_id =OOO00O00O000OO000 #line:776
        OO00O0O00000OOOOO .socket_headers ={"Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","Cache-Control":"no-cache","Pragma":"no-cache","Sec-WebSocket-Extensions":"permessage-deflate; client_max_window_bits","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",}#line:784
        super ().__init__ ("wss://gateway.discord.gg/?encoding=json&v=9",header =OO00O0O00000OOOOO .socket_headers ,on_open =lambda O0OO00OOO000OO000 :OO00O0O00000OOOOO .sock_open (O0OO00OOO000OO000 ),on_message =lambda O0OO0O0O0OO0000OO ,OO0OO0O0000OOOOOO :OO00O0O00000OOOOO .sock_message (O0OO0O0O0OO0000OO ,OO0OO0O0000OOOOOO ),on_close =lambda OO0O0OOOO0OO0O00O ,OO000OOOO00OOOOOO ,OOO0OO00OO00OOOO0 :OO00O0O00000OOOOO .sock_close (OO0O0OOOO0OO0O00O ,OO000OOOO00OOOOOO ,OOO0OO00OO00OOOO0 ),)#line:793
        OO00O0O00000OOOOO .endScraping =False #line:795
        OO00O0O00000OOOOO .guilds ={}#line:796
        OO00O0O00000OOOOO .members ={}#line:797
        OO00O0O00000OOOOO .ranges =[[0 ,0 ]]#line:798
        OO00O0O00000OOOOO .lastRange =0 #line:799
        OO00O0O00000OOOOO .packets_recv =0 #line:800
    def run (OOO00O0O0000OO0O0 ):#line:802
        OOO00O0O0000OO0O0 .run_forever ()#line:803
        return OOO00O0O0000OO0O0 .members #line:804
    def scrapeUsers (OOOO00OO0OOOO00OO ):#line:806
        if not OOOO00OO0OOOO00OO .endScraping :#line:807
            OOOO00OO0OOOO00OO .send ('{"op":14,"d":{"guild_id":"'+OOOO00OO0OOOO00OO .guild_id +'","typing":true,"activities":true,"threads":true,"channels":{"'+OOOO00OO0OOOO00OO .channel_id +'":'+json .dumps (OOOO00OO0OOOO00OO .ranges )+"}}}")#line:816
    def sock_open (OO0OOO00OOOO0OO0O ,O00OOO0O0OO0O0OOO ):#line:818
        OO0OOO00OOOO0OO0O .send ('{"op":2,"d":{"token":"'+OO0OOO00OOOO0OO0O .token +'","capabilities":125,"properties":{"os":"Windows NT","browser":"Chrome","device":"","system_locale":"it-IT","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36","browser_version":"119.0","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":103981,"client_event_source":null},"presence":{"status":"online","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}')#line:823
    def heartbeatThread (OO000O0O0O00OO0O0 ,O0O00OOOO0OOOO00O ):#line:825
        try :#line:826
            while True :#line:827
                OO000O0O0O00OO0O0 .send ('{"op":1,"d":'+str (OO000O0O0O00OO0O0 .packets_recv )+"}")#line:828
                time .sleep (O0O00OOOO0OOOO00O )#line:829
        except Exception as O0OO0OO00OO00O000 :#line:830
            pass #line:831
    def sock_message (OOO0OO00O0OOO0O0O ,OO00O0OO0O00OOO0O ,OO000O0O0OO0OO0OO ):#line:833
        OOO0OO00OO0O0OOOO =json .loads (OO000O0O0OO0OO0OO )#line:834
        if OOO0OO00OO0O0OOOO is None :#line:835
            return #line:836
        if OOO0OO00OO0O0OOOO ["op"]!=11 :#line:837
            OOO0OO00O0OOO0O0O .packets_recv +=1 #line:838
        if OOO0OO00OO0O0OOOO ["op"]==10 :#line:839
            threading .Thread (target =OOO0OO00O0OOO0O0O .heartbeatThread ,args =(OOO0OO00OO0O0OOOO ["d"]["heartbeat_interval"]/1000 ,),daemon =True ,).start ()#line:844
        if OOO0OO00OO0O0OOOO ["t"]=="READY":#line:845
            for OO0O00O0O00OO0O00 in OOO0OO00OO0O0OOOO ["d"]["guilds"]:#line:846
                OOO0OO00O0OOO0O0O .guilds [OO0O00O0O00OO0O00 ["id"]]={"member_count":OO0O00O0O00OO0O00 ["member_count"]}#line:847
        if OOO0OO00OO0O0OOOO ["t"]=="READY_SUPPLEMENTAL":#line:848
            OOO0OO00O0OOO0O0O .ranges =Utils .getRanges (0 ,100 ,OOO0OO00O0OOO0O0O .guilds [OOO0OO00O0OOO0O0O .guild_id ]["member_count"])#line:851
            OOO0OO00O0OOO0O0O .scrapeUsers ()#line:852
        elif OOO0OO00OO0O0OOOO ["t"]=="GUILD_MEMBER_LIST_UPDATE":#line:853
            OO00OO0O0O0O0OO0O =Utils .parseGuildMemberListUpdate (OOO0OO00OO0O0OOOO )#line:854
            if OO00OO0O0O0O0OO0O ["guild_id"]==OOO0OO00O0OOO0O0O .guild_id and ("SYNC"in OO00OO0O0O0O0OO0O ["types"]or "UPDATE"in OO00OO0O0O0O0OO0O ["types"]):#line:858
                for O0OOOO0O0OOO0O00O ,OO0O0000O00OOO00O in enumerate (OO00OO0O0O0O0OO0O ["types"]):#line:859
                    if OO0O0000O00OOO00O =="SYNC":#line:860
                        if len (OO00OO0O0O0O0OO0O ["updates"][O0OOOO0O0OOO0O00O ])==0 :#line:861
                            OOO0OO00O0OOO0O0O .endScraping =True #line:862
                            break #line:863
                        for OOOOO0OOOOO0O0OO0 in OO00OO0O0O0O0OO0O ["updates"][O0OOOO0O0OOO0O00O ]:#line:865
                            if "member"in OOOOO0OOOOO0O0OO0 :#line:866
                                OOOO00OO0000OO000 =OOOOO0OOOOO0O0OO0 ["member"]#line:867
                                OOOOOO0OO00OOO00O ={"tag":OOOO00OO0000OO000 ["user"]["username"]+"#"+OOOO00OO0000OO000 ["user"]["discriminator"],"id":OOOO00OO0000OO000 ["user"]["id"],}#line:873
                                if not OOOO00OO0000OO000 ["user"].get ("bot"):#line:874
                                    OOO0OO00O0OOO0O0O .members [OOOO00OO0000OO000 ["user"]["id"]]=OOOOOO0OO00OOO00O #line:875
                    elif OO0O0000O00OOO00O =="UPDATE":#line:877
                        for OOOOO0OOOOO0O0OO0 in OO00OO0O0O0O0OO0O ["updates"][O0OOOO0O0OOO0O00O ]:#line:878
                            if "member"in OOOOO0OOOOO0O0OO0 :#line:879
                                OOOO00OO0000OO000 =OOOOO0OOOOO0O0OO0 ["member"]#line:880
                                OOOOOO0OO00OOO00O ={"tag":OOOO00OO0000OO000 ["user"]["username"]+"#"+OOOO00OO0000OO000 ["user"]["discriminator"],"id":OOOO00OO0000OO000 ["user"]["id"],}#line:886
                                if not OOOO00OO0000OO000 ["user"].get ("bot"):#line:887
                                    OOO0OO00O0OOO0O0O .members [OOOO00OO0000OO000 ["user"]["id"]]=OOOOOO0OO00OOO00O #line:888
                    OOO0OO00O0OOO0O0O .lastRange +=1 #line:890
                    OOO0OO00O0OOO0O0O .ranges =Utils .getRanges (OOO0OO00O0OOO0O0O .lastRange ,100 ,OOO0OO00O0OOO0O0O .guilds [OOO0OO00O0OOO0O0O .guild_id ]["member_count"])#line:893
                    time .sleep (0.45 )#line:894
                    OOO0OO00O0OOO0O0O .scrapeUsers ()#line:895
            if OOO0OO00O0OOO0O0O .endScraping :#line:897
                OOO0OO00O0OOO0O0O .close ()#line:898
    def sock_close (O0O0O000OO0OOO0OO ,O00OO0O00OOO0O00O ,OO0O00O00O0O0OO0O ,OOOO0OO000O00O00O ):#line:900
        pass #line:901
def scrape (O0000O00O00000000 ,OO0000000O0OO000O ,OOO0OO0000O00OO00 ):#line:903
    O00O00O0OOOO00OOO =DiscordSocket (O0000O00O00000000 ,OO0000000O0OO000O ,OOO0OO0000O00OO00 )#line:904
    return O00O00O0OOOO00OOO .run ()#line:905
def member_scrape (O000OOO0O0O00OO0O ,OO0OOOO000OOOOOOO ,OOO000O0O0O0OO00O ):#line:907
    O0OO0O00O0OOO0000 =[]#line:908
    for OOOOO000OO0O0OOOO in O000OOO0O0O00OO0O :#line:909
        O0O00OOO0O0OO0OOO ={"Authorization":OOOOO000OO0O0OOOO ,"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}#line:910
        O000O0O0O00O00OO0 =session .get (f"https://canary.discord.com/api/v9/guilds/{OO0OOOO000OOOOOOO}",headers =O0O00OOO0O0OO0OOO )#line:911
        if O000O0O0O00O00OO0 .status_code ==200 :#line:912
            O0OO0O00O0OOO0000 .append (OOOOO000OO0O0OOOO )#line:913
            break #line:914
    if not O0OO0O00O0OOO0000 :#line:915
        print ("missing access")#line:916
    OOOOO000OO0O0OOOO =random .choice (O0OO0O00O0OOO0000 )#line:918
    OOOOOO0O000O0000O =scrape (OOOOO000OO0O0OOOO ,OO0OOOO000OOOOOOO ,OOO000O0O0O0OO00O )#line:919
    OO0OO00O000OOO0O0 =[f"<@{OO00O0O000O0OO000}>"for OO00O0O000O0OO000 in [int (O00000OOOO0O00OOO )for O00000OOOO0O00OOO in OOOOOO0O000O0000O .keys ()]]#line:920
    print (f"[SUCCESS] {len(OO0OO00O000OOO0O0)} scraped members")#line:921
    return OO0OO00O000OOO0O0 #line:922
def spammer_menu ():#line:924
    try :#line:925
        with open ("token.txt")as OOO0O00OOO0OOO000 :#line:926
            OOOO000000000O0OO =[O0O0OO00OO0O0OO0O .strip ()for O0O0OO00OO0O0OO0O in OOO0O00OOO0OOO000 .readlines ()if O0O0OO00OO0O0OO0O .strip ()]#line:927
    except (FileNotFoundError ,KeyError ):#line:928
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:929
        return #line:930
    OO00OOOOO0O00OOOO =input ("Server ID?: ").strip ()#line:932
    OO00O00000OO00O0O =input ("Message?: ").strip ()#line:933
    O0OOO00OOOO00O000 =input ("Random mention (True/False)?: ").strip ().lower ()=='true'#line:934
    O0O0O0OOOOO0O00OO =input ("Delay between messages (in seconds)?: ").strip ()#line:935
    O0OO000O0O0O0O0OO =input ("Number of messages to send?: ").strip ()#line:936
    O00OOOOOO000OOOO0 =input ("Blacklist User IDs (comma-separated) (Leave blank to skip)?: ").strip ().split (',')#line:937
    O00OOOOOO000OOOO0 =[f"<@{O0O0OO00000OOOO00.strip()}>"for O0O0OO00000OOOO00 in O00OOOOOO000OOOO0 if O0O0OO00000OOOO00 .strip ()]#line:938
    try :#line:940
        O0O0O0OOOOO0O00OO =float (O0O0O0OOOOO0O00OO )#line:941
        if O0O0O0OOOOO0O00OO <0 :#line:942
            raise ValueError #line:943
    except ValueError :#line:944
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:945
        O0O0O0OOOOO0O00OO =1.0 #line:946
    try :#line:948
        O0OO000O0O0O0O0OO =int (O0OO000O0O0O0O0OO )#line:949
        if O0OO000O0O0O0O0OO <=0 :#line:950
            raise ValueError #line:951
    except ValueError :#line:952
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:953
        O0OO000O0O0O0O0OO =1 #line:954
    OO0O0OO0O0OOO0O00 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:956
    if OO0O0OO0O0OOO0O00 =='2':#line:957
        O0000OO0O000OO000 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:958
        O0000OO0O000OO000 =[OO0O0O0O0OO0O0O00 .strip ()for OO0O0O0O0OO0O0O00 in O0000OO0O000OO000 if OO0O0O0O0OO0O0O00 .strip ()]#line:959
    else :#line:960
        O0000OO0O000OO000 =fetch_channels (OOOO000000000O0OO [0 ],OO00OOOOO0O00OOOO )#line:961
    OO00O000OO0O0O00O =None #line:963
    spammer (OOOO000000000O0OO ,OO00OOOOO0O00OOOO ,O0000OO0O000OO000 ,OO00O00000OO00O0O ,O0OOO00OOOO00O000 ,O00OOOOOO000OOOO0 ,OO00O000OO0O0O00O ,O0OO000O0O0O0O0OO )#line:965
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:967
import discum #line:969
import random #line:970
import time #line:971
def userget (O0OOO00OO0O0O0000 ,O0O00O00O00000OO0 ,OOOOOO00OO0O0OO0O ):#line:973
    OOOOO0OO0OO0000O0 =[]#line:974
    OOO0O0OOO000O0OO0 =discum .Client (token =O0OOO00OO0O0O0000 ,log =False )#line:975
    def OO00O00OOO0OOOO0O (OO000O0OOOOO00O00 ):#line:977
        if OOO0O0OOO000O0OO0 .gateway .finishedMemberFetching (O0O00O00O00000OO0 ):#line:978
            OO00O000000OOO0OO =len (OOO0O0OOO000O0OO0 .gateway .session .guild (O0O00O00O00000OO0 ).members )#line:979
            print (str (OO00O000000OOO0OO )+' members fetched')#line:980
            OOO0O0OOO000O0OO0 .gateway .removeCommand ({'function':OO00O00OOO0OOOO0O ,'params':{}})#line:981
            OOO0O0OOO000O0OO0 .gateway .close ()#line:982
    def O00O0O000OOO0O000 (O0O00OO00O00O000O ,OO0O0O0000OO0O0OO ):#line:984
        OOO0O0OOO000O0OO0 .gateway .fetchMembers (O0O00OO00O00O000O ,OO0O0O0000OO0O0OO ,keep ='all',wait =1 )#line:985
        OOO0O0OOO000O0OO0 .gateway .command ({'function':OO00O00OOO0OOOO0O ,'params':{}})#line:986
        OOO0O0OOO000O0OO0 .gateway .run ()#line:987
        OOO0O0OOO000O0OO0 .gateway .resetSession ()#line:988
        return OOO0O0OOO000O0OO0 .gateway .session .guild (O0O00OO00O00O000O ).members #line:989
    OOO000O0O0OOO000O =O00O0O000OOO0O000 (O0O00O00O00000OO0 ,OOOOOO00OO0O0OO0O )#line:991
    for O0OO0O00O0O0O0O0O in OOO000O0O0OOO000O :#line:992
        if O0OO0O00O0O0O0O0O not in OOOOO0OO0OO0000O0 :#line:993
            OOOOO0OO0OO0000O0 .append (f"<@{O0OO0O00O0O0O0O0O}>")#line:994
    return OOOOO0OO0OO0000O0 #line:995
def spammer (O000OO0O00O00O0OO ,OOOOO0OO0O0OOO0O0 ,OOO0OOOOO0OOO0000 ,O000O00OO0OOO00OO ,OOOOOO0O0OO00O0O0 ,OOO0OOOO0O0000O0O ,OO0000O0OO00OO0OO ,O00OOO00O0OOOO0O0 ):#line:1000
    OOOOO00O0O000O0OO =get_session (OO0000O0OO00OO0OO )#line:1001
    OOO0O00OOOOOOO000 =0 #line:1002
    OO00OOO0OOOOOO0O0 =userget (O000OO0O00O00O0OO [0 ],OOOOO0OO0O0OOO0O0 ,OOO0OOOOO0OOO0000 [0 ])#line:1004
    OO00OOO0OOOOOO0O0 =[O0OOOO0OO00OO00OO for O0OOOO0OO00OO00OO in OO00OOO0OOOOOO0O0 if O0OOOO0OO00OO00OO not in OOO0OOOO0O0000O0O ]#line:1007
    for _O0000O000OO0OO0O0 in range (O00OOO00O0OOOO0O0 ):#line:1009
        O00OO000OOO00OO0O =O000OO0O00O00O0OO [OOO0O00OOOOOOO000 ]#line:1010
        O00OOOOO0O00OOOOO =get_headers (O00OO000OOO00OO0O )#line:1011
        for O000O0OOOO0000OO0 in OOO0OOOOO0OOO0000 :#line:1012
            OOOOOO0000OOO0O0O =O000O00OO0OOO00OO #line:1013
            if OOOOOO0O0OO00O0O0 and OO00OOO0OOOOOO0O0 :#line:1014
                O0O0OOOOOO0O00O0O =random .choice (OO00OOO0OOOOOO0O0 )#line:1015
                OOOOOO0000OOO0O0O +=f" {O0O0OOOOOO0O00O0O}"#line:1016
            O000000OO0O0OOOO0 =OOOOO00O0O000O0OO .post (f"https://discord.com/api/v9/channels/{O000O0OOOO0000OO0}/messages",json ={"content":OOOOOO0000OOO0O0O },headers =O00OOOOO0O00OOOOO )#line:1018
            if O000000OO0O0OOOO0 .status_code ==200 :#line:1019
                print (f"200 message sent: {O00OO000OOO00OO0O}")#line:1020
            elif O000000OO0O0OOOO0 .status_code ==429 :#line:1021
                print (f"429 rate limit: {O00OO000OOO00OO0O}")#line:1022
                O0O0O00OO00OOOOO0 =O000000OO0O0OOOO0 .json ().get ("retry_after",1 )#line:1023
                time .sleep (O0O0O00OO00OOOOO0 )#line:1024
            elif O000000OO0O0OOOO0 .status_code ==401 :#line:1025
                print (f"401 unknown token: {O00OO000OOO00OO0O}")#line:1026
            else :#line:1027
                print (f"error: {O00OO000OOO00OO0O}")#line:1028
        OOO0O00OOOOOOO000 =(OOO0O00OOOOOOO000 +1 )%len (O000OO0O00O00O0OO )#line:1030
        time .sleep (1 )#line:1031
import requests #line:1035
import base64 #line:1036
import colorama #line:1037
import time #line:1038
def add_emojis_from_files ():#line:1040
    try :#line:1041
        with open ("emojiname.txt")as OO0O0OO00OO0000O0 ,open ("emojiurl.txt")as OO0OO000OOO0O0O00 :#line:1042
            O0000O0OOOOO000O0 =[O0O0OO00OOO0O00OO .strip ()for O0O0OO00OOO0O00OO in OO0O0OO00OO0000O0 .read ().split (',')if O0O0OO00OOO0O00OO .strip ()]#line:1043
            O0O00O0OO0OO0O000 =[OOOO0O0O00OOO0O0O .strip ()for OOOO0O0O00OOO0O0O in OO0OO000OOO0O0O00 .read ().split (',')if OOOO0O0O00OOO0O0O .strip ()]#line:1044
    except FileNotFoundError as OOOOO0O0OO0OOO00O :#line:1045
        print (f"{colorama.Fore.RED}    [!] Error: {str(OOOOO0O0OO0OOO00O)}{colorama.Fore.RESET}")#line:1046
        return #line:1047
    if len (O0000O0OOOOO000O0 )!=len (O0O00O0OO0OO0O000 ):#line:1049
        print (f"{colorama.Fore.RED}    [!] Error: The number of emoji names and URLs do not match!{colorama.Fore.RESET}")#line:1050
        return #line:1051
    try :#line:1053
        with open ("token.txt")as OO0O00OO0O0O00000 :#line:1054
            O00OO0000O0O0O00O =[O0O00O0O00OO0O0O0 .strip ()for O0O00O0O00OO0O0O0 in OO0O00OO0O0O00000 .readlines ()if O0O00O0O00OO0O0O0 .strip ()]#line:1055
    except FileNotFoundError as OOOOO0O0OO0OOO00O :#line:1056
        print (f"{colorama.Fore.RED}    [!] Error: {str(OOOOO0O0OO0OOO00O)}{colorama.Fore.RESET}")#line:1057
        return #line:1058
    O0O00O00O000OOOO0 =input ("Enter the Guild ID: ").strip ()#line:1060
    OOO00O00OO000O0OO =input ("Enter the rate limit between requests (in seconds): ").strip ()#line:1061
    try :#line:1063
        OOO00O00OO000O0OO =float (OOO00O00OO000O0OO )#line:1064
        if OOO00O00OO000O0OO <0 :#line:1065
            raise ValueError #line:1066
    except ValueError :#line:1067
        print (f"{colorama.Fore.RED}    [!] Invalid rate limit. Using default rate limit of 5 seconds.{colorama.Fore.RESET}")#line:1068
        OOO00O00OO000O0OO =5.0 #line:1069
    O0O00OOO0O00OO0O0 =set ()#line:1071
    for OO0OOOO0OO00OOO00 in O00OO0000O0O0O00O :#line:1073
        OOOO000O0O00O000O ={'Authorization':OO0OOOO0OO00OOO00 ,'Content-Type':'application/json'}#line:1077
        OOO0O0OO00O0O0OO0 =requests .get (f"https://discord.com/api/v9/guilds/{O0O00O00O000OOOO0}/emojis",headers =OOOO000O0O00O000O )#line:1080
        if OOO0O0OO00O0O0OO0 .status_code ==200 :#line:1081
            OOO0000OO0O00O0OO =OOO0O0OO00O0O0OO0 .json ()#line:1082
            for O0O0000OO0OOO0O0O in OOO0000OO0O00O0OO :#line:1083
                O0O00OOO0O00OO0O0 .add (O0O0000OO0OOO0O0O ['name'])#line:1084
        else :#line:1085
            print (f"{colorama.Fore.RED}    [!] Error fetching existing emojis: {OOO0O0OO00O0O0OO0.status_code} - {OOO0O0OO00O0O0OO0.text}{colorama.Fore.RESET}")#line:1086
            continue #line:1087
    for O0O00OOO00OOO000O ,O000OO00O00O0OOOO in zip (O0000O0OOOOO000O0 ,O0O00O0OO0OO0O000 ):#line:1089
        if O0O00OOO00OOO000O in O0O00OOO0O00OO0O0 :#line:1090
            print (f"{colorama.Fore.YELLOW}    [*] Emoji '{O0O00OOO00OOO000O}' already exists. Skipping...{colorama.Fore.RESET}")#line:1091
            continue #line:1092
        for OO0OOOO0OO00OOO00 in O00OO0000O0O0O00O :#line:1094
            try :#line:1095
                OOO0O0OO00O0O0OO0 =requests .get (O000OO00O00O0OOOO )#line:1096
                OOO0O0OO00O0O0OO0 .raise_for_status ()#line:1097
                O0OOO00OOOOO0O0O0 =OOO0O0OO00O0O0OO0 .content #line:1098
                OOO0O000OO0O00O0O =base64 .b64encode (O0OOO00OOOOO0O0O0 ).decode ('utf-8')#line:1099
                O0OO0000O0O0O000O ={'name':O0O00OOO00OOO000O ,'image':f"data:image/png;base64,{OOO0O000OO0O00O0O}"}#line:1104
                OOOO000O0O00O000O ={'Authorization':OO0OOOO0OO00OOO00 ,'Content-Type':'application/json'}#line:1109
                O000OO0O0OOO0OO0O =requests .post (f"https://discord.com/api/v9/guilds/{O0O00O00O000OOOO0}/emojis",headers =OOOO000O0O00O000O ,json =O0OO0000O0O0O000O )#line:1111
                if O000OO0O0OOO0OO0O .status_code ==201 :#line:1112
                    print (f"{colorama.Fore.GREEN}    [+] Successfully added emoji '{O0O00OOO00OOO000O}' with token {OO0OOOO0OO00OOO00}{colorama.Fore.RESET}")#line:1113
                    O0O00OOO0O00OO0O0 .add (O0O00OOO00OOO000O )#line:1114
                    break #line:1115
                else :#line:1116
                    print (f"{colorama.Fore.RED}    [!] Failed to add emoji '{O0O00OOO00OOO000O}' with token {OO0OOOO0OO00OOO00}: {O000OO0O0OOO0OO0O.status_code} - {O000OO0O0OOO0OO0O.text}{colorama.Fore.RESET}")#line:1117
                time .sleep (OOO00O00OO000O0OO )#line:1119
            except Exception as OOOOO0O0OO0OOO00O :#line:1120
                print (f"{colorama.Fore.RED}    [!] Error adding emoji '{O0O00OOO00OOO000O}' with token {OO0OOOO0OO00OOO00}: {str(OOOOO0O0OO0OOO00O)}{colorama.Fore.RESET}")#line:1121
def main ():#line:1123
    colorama .init ()#line:1124
    while True :#line:1125
        logo ()#line:1126
        O0OOO0O0OO0O00OO0 =input (f"{colorama.Fore.LIGHTMAGENTA_EX}    [Final] Select an option from above: ")#line:1127
        if O0OOO0O0OO0O00OO0 =="0":#line:1129
            update_group_ids ()#line:1130
        elif O0OOO0O0OO0O00OO0 =="1":#line:1131
            join_discord_invite ()#line:1132
        elif O0OOO0O0OO0O00OO0 =="2":#line:1133
            reaction_spammer ()#line:1134
        elif O0OOO0O0OO0O00OO0 =="3":#line:1135
            send_messages_with_mentions ()#line:1136
        elif O0OOO0O0OO0O00OO0 =="4":#line:1137
            spammer_menu ()#line:1138
        elif O0OOO0O0OO0O00OO0 =="5":#line:1139
            nickchanger ()#line:1140
        elif O0OOO0O0OO0O00OO0 =="6":#line:1141
            add_emojis_from_files ()#line:1142
        elif O0OOO0O0OO0O00OO0 =="7":#line:1143
            reaction_art ()#line:1144
        elif O0OOO0O0OO0O00OO0 =="0":#line:1145
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [*] Exiting the application. Goodbye!{colorama.Fore.RESET}")#line:1146
            break #line:1147
        else :#line:1148
            print (f"{colorama.Fore.RED}    [!] Invalid option selected!{colorama.Fore.RESET}")#line:1149
        input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:1151
if __name__ =="__main__":#line:1153
    main ()#line:1154
