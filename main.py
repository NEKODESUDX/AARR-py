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
    O00O000O00OOO0OO0 =requests .Session ()#line:57
    if proxy :#line:58
        O00O000O00OOO0OO0 .proxies ={"http":proxy ,"https":proxy }#line:59
    return O00O000O00OOO0OO0 #line:60
def get_headers (OOOOO00000000000O ):#line:62
    return {"Authorization":OOOOO00000000000O ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:67
def send_message_with_mention (O0O000OOO0OOOOO00 ,O0O0O00OO000OO0OO ,OO0OO00OOOOOO0O0O ,O0O0OO0000OO00000 ):#line:70
    OOOO00OO000O0O0O0 =get_session ()#line:71
    OOOOOO0O000OOOOOO =get_headers (O0O000OOO0OOOOO00 )#line:72
    if O0O0OO0000OO00000 :#line:74
        O000OOOOOOOOOO0O0 =random .choice (O0O0OO0000OO00000 )#line:75
        OO0OO00OOOOOO0O0O +=f" <@{O000OOOOOOOOOO0O0}>"#line:76
    OO0O000OOO0000000 =OOOO00OO000O0O0O0 .post (f"https://discord.com/api/v9/channels/{O0O0O00OO000OO0OO}/messages",headers =OOOOOO0O000OOOOOO ,json ={"content":OO0OO00OOOOOO0O0O })#line:82
    if OO0O000OOO0000000 .status_code in [200 ,201 ]:#line:83
        print (f"[+] Message sent to channel {O0O0O00OO000OO0OO}")#line:84
    elif OO0O000OOO0000000 .status_code ==429 :#line:85
        print ("[-] Rate limited. Please wait before retrying.")#line:86
        OOOO000000OO0OOOO =OO0O000OOO0000000 .json ().get ("retry_after",1 )#line:87
        time .sleep (OOOO000000OO0OOOO )#line:88
    else :#line:89
        print (f"[!] Error occurred: {OO0O000OOO0000000.status_code}")#line:90
def fetch_messages (OOOOOOO0O0000O0OO ,OOOO0O0000O00O000 ,limit =100 ):#line:93
    OO00O00OOOOOOO0O0 ={"Authorization":OOOOOOO0O0000O0OO ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:98
    OOO0OOO000OO0OO0O =requests .get (f"https://discord.com/api/v9/channels/{OOOO0O0000O00O000}/messages?limit={limit}",headers =OO00O00OOOOOOO0O0 )#line:102
    if OOO0OOO000OO0OO0O .status_code ==200 :#line:103
        return OOO0OOO000OO0OO0O .json ()#line:104
    else :#line:105
        print (f"[!] Failed to fetch messages. HTTP Status Code: {OOO0OOO000OO0OO0O.status_code}")#line:106
        return []#line:107
import concurrent .futures #line:109
def reaction_spammer ():#line:111
    try :#line:112
        with open ("token.txt")as O0OO00O000OOOOO0O :#line:113
            O0O0OOOO0O00OOO0O =[OO0OOO0O0OOO00OOO .strip ()for OO0OOO0O0OOO00OOO in O0OO00O000OOOOO0O .readlines ()if OO0OOO0O0OOO00OOO .strip ()]#line:114
    except (FileNotFoundError ,KeyError ):#line:115
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:116
        return #line:117
    O0OO00O000OO00OO0 =input ("Server ID?: ").strip ()#line:119
    OO00O0O000OOO0O0O =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:121
    if OO00O0O000OOO0O0O =='2':#line:122
        OOO00OO000OOOOO0O =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:123
        O0OOOOOO0O00OOO0O =[O0OO0OOO0OO000000 .strip ()for O0OO0OOO0OO000000 in OOO00OO000OOOOO0O if O0OO0OOO0OO000000 .strip ()]#line:124
    else :#line:125
        O0OOOOOO0O00OOO0O =[]#line:126
        for OO000OOO0OO00O0O0 in O0O0OOOO0O00OOO0O :#line:127
            try :#line:128
                O0OOOOOO0O00OOO0O .extend (fetch_channels (OO000OOO0OO00O0O0 ,O0OO00O000OO00OO0 ))#line:129
            except Exception as O0OO0O0OOOO0000OO :#line:130
                print (f"[!] Failed to fetch channels for token. Error: {O0OO0O0OOOO0000OO}")#line:131
                continue #line:132
    O000O0OOOO000OOOO =input ("Select your emoji (a, b, c, ... or custom emojis): ").strip ()#line:134
    OO0000O0OO000OOOO =input ("Delay between reactions (in seconds)?: ").strip ()#line:135
    try :#line:137
        OO0000O0OO000OOOO =float (OO0000O0OO000OOOO )#line:138
        if OO0000O0OO000OOOO <0 :#line:139
            raise ValueError #line:140
    except ValueError :#line:141
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:142
        OO0000O0OO000OOOO =1.0 #line:143
    O0OOOOOO0OOO0OOOO =[]#line:145
    for O000OOO0O000O0O0O in O000O0OOOO000OOOO .split (","):#line:146
        O000OOO0O000O0O0O =O000OOO0O000O0O0O .strip ().lower ()#line:147
        if O000OOO0O000O0O0O in alphabet_to_flag :#line:148
            O0OOOOOO0OOO0OOOO .append (alphabet_to_flag [O000OOO0O000O0O0O ])#line:149
        else :#line:150
            O0OOOOOO0OOO0OOOO .append (O000OOO0O000O0O0O )#line:151
    if not O0OOOOOO0OOO0OOOO :#line:153
        print (f"{colorama.Fore.RED}    [!] No valid emojis provided!{colorama.Fore.RESET}")#line:154
        return #line:155
    def O0O000OOOOO00O0OO (OOOOO0O000O00OOOO ):#line:157
        for O0OO0000O0OOOOO0O in O0OOOOOO0O00OOO0O :#line:158
            try :#line:159
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {O0OO0000O0OOOOO0O}...{colorama.Fore.RESET}")#line:160
                O000O0OO0O000OO0O =fetch_messages (OOOOO0O000O00OOOO ,O0OO0000O0OOOOO0O ,limit =100 )#line:161
                if not O000O0OO0O000OO0O :#line:162
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:163
                    continue #line:164
                for OOOOO0OOO000OOO00 in O000O0OO0O000OO0O :#line:166
                    for O0000O00000O0O000 in O0OOOOOO0OOO0OOOO :#line:167
                        reactionput (OOOOO0O000O00OOOO ,O0OO0000O0OOOOO0O ,OOOOO0OOO000OOO00 ['id'],O0000O00000O0O000 )#line:168
                        time .sleep (OO0000O0OO000OOOO )#line:169
            except Exception as OOOO000O00O0000OO :#line:170
                print (f"[!] Error processing channel {O0OO0000O0OOOOO0O}. Error: {OOOO000O00O0000OO}")#line:171
                continue #line:172
    with concurrent .futures .ThreadPoolExecutor ()as OOOO000O00OOO0000 :#line:174
        OOO0OOOO0O00OOOOO =[OOOO000O00OOO0000 .submit (O0O000OOOOO00O0OO ,OO00OOO000OO0O000 )for OO00OOO000OO0O000 in O0O0OOOO0O00OOO0O ]#line:175
        concurrent .futures .wait (OOO0OOOO0O00OOOOO )#line:176
import requests #line:179
import json #line:180
import time #line:181
import colorama #line:182
alphabet_to_flag ={'a':'🇦','b':'🇧','c':'🇨','d':'🇩','e':'🇪','f':'🇫','g':'🇬','h':'🇭','i':'🇮','j':'🇯','k':'🇰','l':'🇱','m':'🇲','n':'🇳','o':'🇴','p':'🇵','q':'🇶','r':'🇷','s':'🇸','t':'🇹','u':'🇺','v':'🇻','w':'🇼','x':'🇽','y':'🇾','z':'🇿'}#line:190
def fetch_channels (OOO00O0O0O0O000OO ,O0OOO00O0OO0000OO ):#line:192
    O0O00OO00OOOO000O =f"https://discord.com/api/v9/guilds/{O0OOO00O0OO0000OO}/channels"#line:193
    O0O0OO000000OO0O0 ={"Authorization":OOO00O0O0O0O000OO }#line:194
    OO0000OO0O0O0O0O0 =requests .get (O0O00OO00OOOO000O ,headers =O0O0OO000000OO0O0 )#line:195
    if OO0000OO0O0O0O0O0 .status_code ==200 :#line:196
        return [OOO00OOO0O00OO00O ['id']for OOO00OOO0O00OO00O in OO0000OO0O0O0O0O0 .json ()if OOO00OOO0O00OO00O ['type']==0 ]#line:197
    else :#line:198
        raise Exception (f"Failed to fetch channels: {OO0000OO0O0O0O0O0.status_code} - {OO0000OO0O0O0O0O0.text}")#line:199
def fetch_messages (OO0O00OOO0O0O00OO ,OOOO0O0O00OOO000O ,limit =100 ):#line:201
    OO0O000O0OOO0OOOO =f"https://discord.com/api/v9/channels/{OOOO0O0O00OOO000O}/messages?limit={limit}"#line:202
    OOOO0OOOOOOO00OO0 ={"Authorization":OO0O00OOO0O0O00OO }#line:203
    OO0OOOO0OO00O0O0O =requests .get (OO0O000O0OOO0OOOO ,headers =OOOO0OOOOOOO00OO0 )#line:204
    if OO0OOOO0OO00O0O0O .status_code ==200 :#line:205
        return OO0OOOO0OO00O0O0O .json ()#line:206
    else :#line:207
        print (f"[!] Failed to fetch messages: {OO0OOOO0OO00O0O0O.status_code} - {OO0OOOO0OO00O0O0O.text}")#line:208
        return []#line:209
def reactionput (O0O0OOOOO000OOO0O ,OO00OOOO0O000000O ,O000OOO0O0OOO0OOO ,O0OOO00O00O00O00O ):#line:211
    OO0O0O0O00O0O00OO =f"https://discord.com/api/v9/channels/{OO00OOOO0O000000O}/messages/{O000OOO0O0OOO0OOO}/reactions/{O0OOO00O00O00O00O}/@me"#line:212
    O00000O0OO0OOOO0O ={"Authorization":O0O0OOOOO000OOO0O ,"Content-Type":"application/json"}#line:213
    OO00OO0OO00OOOOO0 =requests .put (OO0O0O0O00O0O00OO ,headers =O00000O0OO0OOOO0O )#line:214
    if OO00OO0OO00OOOOO0 .status_code not in [204 ,200 ]:#line:215
        print (f"{colorama.Fore.RED}    [!] Failed to add reaction: {OO00OO0OO00OOOOO0.status_code} - {OO00OO0OO00OOOOO0.text}{colorama.Fore.RESET}")#line:216
import random #line:218
def reaction_art ():#line:220
    try :#line:221
        with open ("token.txt",encoding ="utf-8")as O000000000O00O00O :#line:222
            O000O0OOOO000OOO0 =[O00O0OO0O0OO000OO .strip ()for O00O0OO0O0OO000OO in O000000000O00O00O .readlines ()if O00O0OO0O0OO000OO .strip ()]#line:223
    except (FileNotFoundError ,KeyError ):#line:224
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:225
        return #line:226
    OOO000O00OO0000O0 =input ("Server ID?: ").strip ()#line:228
    O00O000O00O00OO00 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:230
    if O00O000O00O00OO00 =='2':#line:231
        OOOO0O00OO0O0O000 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:232
        OO0O000OO0OO0OO0O =[O0OO0O00O00OO00OO .strip ()for O0OO0O00O00OO00OO in OOOO0O00OO0O0O000 if O0OO0O00O00OO00OO .strip ()]#line:233
    else :#line:234
        OO0O000OO0OO0OO0O =[]#line:235
        for O0O00OOO0OO0OO0OO in O000O0OOOO000OOO0 :#line:236
            try :#line:237
                OO0O000OO0OO0OO0O .extend (fetch_channels (O0O00OOO0OO0OO0OO ,OOO000O00OO0000O0 ))#line:238
            except Exception as O000OO0OO0O0OO000 :#line:239
                print (f"[!] Failed to fetch channels for token. Error: {O000OO0OO0O0OO000}")#line:240
                continue #line:241
        random .shuffle (OO0O000OO0OO0OO0O )#line:242
    OOOO0O000000O0O0O =input ("Delay between reactions (in seconds)?: ").strip ()#line:244
    try :#line:246
        OOOO0O000000O0O0O =float (OOOO0O000000O0O0O )#line:247
        if OOOO0O000000O0O0O <0 :#line:248
            raise ValueError #line:249
    except ValueError :#line:250
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:251
        OOOO0O000000O0O0O =1.0 #line:252
    try :#line:254
        with open ("art.txt",encoding ="utf-8")as O0O000OO0OOO0O00O :#line:255
            OO0O0OOO0OOO00OOO =[O0O00OOOO00OOO0OO .strip ()for O0O00OOOO00OOO0OO in O0O000OO0OOO0O00O .readlines ()if O0O00OOOO00OOO0OO .strip ()]#line:256
    except (FileNotFoundError ,KeyError ):#line:257
        print (f"{colorama.Fore.RED}    [!] Error: art.txt file not found or empty!{colorama.Fore.RESET}")#line:258
        return #line:259
    except UnicodeDecodeError as O000OO0OO0O0OO000 :#line:260
        print (f"{colorama.Fore.RED}    [!] Error decoding art.txt: {str(O000OO0OO0O0OO000)}{colorama.Fore.RESET}")#line:261
        return #line:262
    if not OO0O0OOO0OOO00OOO :#line:264
        print (f"{colorama.Fore.RED}    [!] No valid art provided in art.txt!{colorama.Fore.RESET}")#line:265
        return #line:266
    OO0O0OOO0OOO00OOO .reverse ()#line:269
    for O0O00OOO0OO0OO0OO in O000O0OOOO000OOO0 :#line:271
        for OOOOOO0O000O00000 in OO0O000OO0OO0OO0O :#line:272
            try :#line:273
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {OOOOOO0O000O00000}...{colorama.Fore.RESET}")#line:274
                OO00O00O000OO0OO0 =fetch_messages (O0O00OOO0OO0OO0OO ,OOOOOO0O000O00000 ,limit =100 )#line:277
                if not OO00O00O000OO0OO0 :#line:278
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:279
                    continue #line:280
                for OO00O0OO0OOO00O00 ,OO00O0O00OO0OO00O in enumerate (OO00O00O000OO0OO0 ):#line:283
                    OO0OOO0OOO0OO0OOO =OO0O0OOO0OOO00OOO [OO00O0OO0OOO00O00 %len (OO0O0OOO0OOO00OOO )].split (',')#line:284
                    for OOOO00O0000OOOO00 in OO0OOO0OOO0OO0OOO :#line:285
                        reactionput (O0O00OOO0OO0OO0OO ,OOOOOO0O000O00000 ,OO00O0O00OO0OO00O ['id'],OOOO00O0000OOOO00 .strip ())#line:286
                        print (f"Adding reaction '{OOOO00O0000OOOO00.strip()}' to message {OO00O0O00OO0OO00O['id']} in channel {OOOOOO0O000O00000}")#line:287
                        time .sleep (OOOO0O000000O0O0O )#line:288
            except Exception as O000OO0OO0O0OO000 :#line:289
                print (f"[!] Error processing channel {OOOOOO0O000O00000}. Error: {O000OO0OO0O0OO000}")#line:290
                continue #line:291
    def O0O0O0O00000000O0 (O0OOOO0OO0O00OOO0 ):#line:296
        for O0000OO00OOOO0OOO in OO0O000OO0OO0OO0O :#line:297
            try :#line:298
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {O0000OO00OOOO0OOO}...{colorama.Fore.RESET}")#line:299
                O0O0OOO0OO0000O0O =fetch_messages (O0OOOO0OO0O00OOO0 ,O0000OO00OOOO0OOO ,limit =100 )#line:300
                if not O0O0OOO0OO0000O0O :#line:301
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:302
                    continue #line:303
                for OOOO0OO00O00OOOO0 in O0O0OOO0OO0000O0O :#line:305
                    for O00O0O00O00OOOO0O in OO0OOO0OOO0OO0OOO :#line:306
                        reactionput (O0OOOO0OO0O00OOO0 ,O0000OO00OOOO0OOO ,OOOO0OO00O00OOOO0 ['id'],O00O0O00O00OOOO0O )#line:307
                        time .sleep (OOOO0O000000O0O0O )#line:308
            except Exception as OOOOO0O00000OOO00 :#line:309
                print (f"[!] Error processing channel {O0000OO00OOOO0OOO}. Error: {OOOOO0O00000OOO00}")#line:310
                continue #line:311
    with concurrent .futures .ThreadPoolExecutor ()as O0OO0000O0O0O0O0O :#line:313
        O0O00OO0OO0000000 =[O0OO0000O0O0O0O0O .submit (O0O0O0O00000000O0 ,O000OOOOO0O000OOO )for O000OOOOO0O000OOO in O000O0OOOO000OOO0 ]#line:314
        concurrent .futures .wait (O0O00OO0OO0000000 )#line:315
def update_group_ids ():#line:318
    try :#line:319
        with open ("token.txt")as O00OOOO00O00OO000 :#line:320
            OOOOOO0O00OOO0000 =[O00O0O0OOO0OOO0O0 .strip ()for O00O0O0OOO0OOO0O0 in O00OOOO00O00OO000 .readlines ()if O00O0O0OOO0OOO0O0 .strip ()]#line:321
        O0OOO0OO00O0OO0O0 =OOOOOO0O00OOO0000 [0 ]#line:322
    except (FileNotFoundError ,KeyError ):#line:323
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:324
        return #line:325
    O0O00O0O00O0OOO0O ={"Authorization":O0OOO0OO00O0OO0O0 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:331
    O00OO0O00O00O0O00 =requests .get ('https://discord.com/api/v9/users/@me/channels',headers =O0O00O0O00O0OOO0O )#line:333
    if O00OO0O00O00O0O00 .status_code ==200 :#line:334
        O00O0OO0O000OO000 =O00OO0O00O00O0O00 .json ()#line:335
        with open ("group_id.txt","w")as OO00O00OOO000O000 :#line:336
            for OO0O00OOOO0O00O0O in O00O0OO0O000OO000 :#line:337
                if OO0O00OOOO0O00O0O ['type']==3 :#line:338
                    OO00O00OOO000O000 .write (OO0O00OOOO0O00O0O ['id']+'\n')#line:339
        print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Group IDs updated successfully.{colorama.Fore.RESET}")#line:340
    else :#line:341
        print (f"{colorama.Fore.LIGHTRED_EX}    [!] Failed to retrieve group IDs. HTTP Status Code: {O00OO0O00O00O0O00.status_code}{colorama.Fore.RESET}")#line:342
import requests #line:344
import requests #line:346
def fetch_channels (OOOOO0O00OOOO0000 ,OOO0OO0000O0000OO ):#line:348
    try :#line:349
        OO0OOO00OOO00OO00 =requests .Session ()#line:350
        O00000OOOOO0O0OOO =get_headers (OOOOO0O00OOOO0000 )#line:351
        OO00OO0OOO00O00OO =OO0OOO00OOO00OO00 .get (f"https://discord.com/api/v9/guilds/{OOO0OO0000O0000OO}/channels",headers =O00000OOOOO0O0OOO ,timeout =10 )#line:358
        if OO00OO0OOO00O00OO .status_code ==200 :#line:361
            try :#line:362
                OOO0OOO0000O0O000 =OO00OO0OOO00O00OO .json ()#line:363
                return [O0OOOOOO0OOOO0O00 ['id']for O0OOOOOO0OOOO0O00 in OOO0OOO0000O0O000 if O0OOOOOO0OOOO0O00 .get ('type')==0 ]#line:364
            except ValueError :#line:365
                print ("[!] Error: Response was not valid JSON.")#line:366
                return []#line:367
        elif OO00OO0OOO00O00OO .status_code ==401 :#line:368
            print ("[!] Error: Unauthorized - check your token.")#line:369
        elif OO00OO0OOO00O00OO .status_code ==403 :#line:370
            print ("[!] Error: Forbidden - you lack permissions.")#line:371
        elif OO00OO0OOO00O00OO .status_code ==404 :#line:372
            print ("[!] Error: Server not found - check the server ID.")#line:373
        else :#line:374
            print (f"[!] Error: Unexpected status code {OO00OO0OOO00O00OO.status_code}.")#line:375
        return []#line:378
    except requests .exceptions .Timeout :#line:380
        print ("[!] Error: Request timed out. Check your connection or try again later.")#line:381
        return []#line:382
    except requests .exceptions .RequestException as OO0O000OOO0OOOO0O :#line:383
        print (f"[!] Error: An error occurred while fetching channels: {OO0O000OOO0OOOO0O}")#line:384
        return []#line:385
def extract_uids_from_messages (O0O000O00000000O0 ):#line:391
    O0O00OOOOO000O00O =set ()#line:392
    for O0OOO0O0OO0O0OOOO in O0O000O00000000O0 :#line:393
        O0O00OOOOO000O00O .add (O0OOO0O0OO0O0OOOO ['author']['id'])#line:394
    return list (O0O00OOOOO000O00O )#line:395
def send_message_with_mention (O0000O00O0O00OO00 ,OOOOO00O0O0O00O00 ,O0O00O0OO0O00OO0O ,O0O00000OOO0OOOOO ):#line:397
    OO000O0O0O00O000O =get_session ()#line:398
    O0OO0OO000O00000O =get_headers (O0000O00O0O00OO00 )#line:399
    if O0O00000OOO0OOOOO :#line:401
        OOO0OOOOO0O000O00 =random .choice (O0O00000OOO0OOOOO )#line:402
        O0O00O0OO0O00OO0O +=f" <@{OOO0OOOOO0O000O00}>"#line:403
    O0OO0OO0O0OO00OO0 =OO000O0O0O00O000O .post (f"https://discord.com/api/v9/channels/{OOOOO00O0O0O00O00}/messages",headers =O0OO0OO000O00000O ,json ={"content":O0O00O0OO0O00OO0O })#line:409
    if O0OO0OO0O0OO00OO0 .status_code in [200 ,201 ]:#line:410
        print (f"[+] Message sent to channel {OOOOO00O0O0O00O00}")#line:411
    elif O0OO0OO0O0OO00OO0 .status_code ==429 :#line:412
        print ("[-] Rate limited. Please wait before retrying.")#line:413
        O000OO00OOOOO000O =O0OO0OO0O0OO00OO0 .json ().get ("retry_after",1 )#line:414
        time .sleep (O000OO00OOOOO000O )#line:415
    else :#line:416
        print (f"[!] Error occurred: {O0OO0OO0O0OO00OO0.status_code}")#line:417
def send_messages_with_mentions ():#line:418
    try :#line:419
        with open ("token.txt")as OO0000OOO0OO00OOO :#line:420
            OOOOOOOOOO00OO000 =[O0000OO00OOO00O00 .strip ()for O0000OO00OOO00O00 in OO0000OOO0OO00OOO .readlines ()if O0000OO00OOO00O00 .strip ()]#line:421
    except (FileNotFoundError ,KeyError ):#line:422
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:423
        return #line:424
    OOO0000O000OO000O =input ("Server ID?: ").strip ()#line:426
    O0O00OO0OOO00OOOO =input ("Delay between messages (in seconds)?: ").strip ()#line:427
    OOOOOO0O00O0OOO00 =input ("Number of messages to send?: ").strip ()#line:428
    O0OOO00O000OO0OO0 =input ("Message content?: ").strip ()#line:429
    OOO000OO0O00OOOOO =input ("Blacklist User IDs (comma-separated)?: ").strip ().split (',')#line:430
    OOO000OO0O00OOOOO =[O0OO000000OOOOO00 .strip ()for O0OO000000OOOOO00 in OOO000OO0O00OOOOO if O0OO000000OOOOO00 .strip ()]#line:431
    try :#line:433
        O0O00OO0OOO00OOOO =float (O0O00OO0OOO00OOOO )#line:434
        if O0O00OO0OOO00OOOO <0 :#line:435
            raise ValueError #line:436
    except ValueError :#line:437
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:438
        O0O00OO0OOO00OOOO =1.0 #line:439
    try :#line:441
        OOOOOO0O00O0OOO00 =int (OOOOOO0O00O0OOO00 )#line:442
        if OOOOOO0O00O0OOO00 <=0 :#line:443
            raise ValueError #line:444
    except ValueError :#line:445
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:446
        OOOOOO0O00O0OOO00 =1 #line:447
    OO0000O0O000OO000 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:449
    if OO0000O0O000OO000 =='2':#line:450
        O000O0O0O00O0O0OO =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:451
        O000O0O0O00O0O0OO =[OO0OO00000000000O .strip ()for OO0OO00000000000O in O000O0O0O00O0O0OO if OO0OO00000000000O .strip ()]#line:452
    else :#line:453
        O000O0O0O00O0O0OO =[]#line:454
    O0O000OOO0OO00OO0 =set ()#line:456
    for OOO0O00O0OO0OOO0O in OOOOOOOOOO00OO000 :#line:457
        O0O0OOO0O0OOOO00O =fetch_channels (OOO0O00O0OO0OOO0O ,OOO0000O000OO000O )#line:458
        for OOOO0O0O00OOO0O00 in O0O0OOO0O0OOOO00O :#line:459
            OO00OOOO000O0O0OO =fetch_messages (OOO0O00O0OO0OOO0O ,OOOO0O0O00OOO0O00 ,limit =100 )#line:460
            O0OOO000OOOOO0O0O =extract_uids_from_messages (OO00OOOO000O0O0OO )#line:461
            O0O000OOO0OO00OO0 .update (O0OOO000OOOOO0O0O )#line:462
    O0O000OOO0OO00OO0 =list (set (O0O000OOO0OO00OO0 )-set (OOO000OO0O00OOOOO ))#line:465
    for _OOOOOO0000OOO000O in range (OOOOOO0O00O0OOO00 ):#line:467
        for OOO0O00O0OO0OOO0O in OOOOOOOOOO00OO000 :#line:468
            if O000O0O0O00O0O0OO :#line:469
                O0O0OOO0O0OOOO00O =O000O0O0O00O0O0OO #line:470
            for OOOO0O0O00OOO0O00 in O0O0OOO0O0OOOO00O :#line:471
                send_message_with_mention (OOO0O00O0OO0OOO0O ,OOOO0O0O00OOO0O00 ,O0OOO00O000OO0OO0 ,O0O000OOO0OO00OO0 )#line:472
                time .sleep (O0O00OO0OOO00OOOO )#line:473
def join_discord_invite ():#line:478
    try :#line:479
        with open ("token.txt")as O000000O00OOOOO0O :#line:480
            OOOO0OOOOOOOO00O0 =[O00O0OOO0OO0OO0OO .strip ()for O00O0OOO0OO0OO0OO in O000000O00OOOOO0O .readlines ()if O00O0OOO0OO0OO0OO .strip ()]#line:481
    except (FileNotFoundError ,KeyError ):#line:482
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:483
        return #line:484
    O0OO0OOOO00O0O0O0 =input ("Invite Code?: discord.gg/").strip ()#line:486
    for O0O00O0OOO0OOOO0O in OOOO0OOOOOOOO00O0 :#line:489
        joiner (O0O00O0OOO0OOOO0O ,O0OO0OOOO00O0O0O0 )#line:490
import json ,time ,base64 ,random ,requests #line:492
def cookieset (O000OOOO0O00O000O ):#line:494
    O00OO00O0000OO000 =O000OOOO0O00O000O .get ("https://discord.com/app")#line:495
    return O00OO00O0000OO000 .cookies .get_dict ()#line:496
def generatexspandua (O0O00O00OOO00OO00 ):#line:498
    O000O0000OO0000O0 =["Android","Windows","Macintosh"]#line:499
    OOO000OO0OOO00O0O =random .choice (O000O0000OO0000O0 )#line:500
    if OOO000OO0OOO00O0O =="Macintosh":#line:501
        O00000OO0OO0O00O0 =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:502
        O00OO000OOOOO00O0 ="Macintosh; Intel Mac OS X "+O00000OO0OO0O00O0 #line:503
        OO0O0OO0O0OO00OOO ="x86_64"#line:504
    elif OOO000OO0OOO00O0O =="Windows":#line:505
        O00000OO0OO0O00O0 =f'{random.choice([6.0, 10.0, 11.0])}'#line:506
        O00OO000OOOOO00O0 ="Windows NT "+O00000OO0OO0O00O0 +" Win64; x64"#line:507
        OO0O0OO0O0OO00OOO ="x86_64"#line:508
    else :#line:509
        O00000OO0OO0O00O0 ="13"#line:510
        O00OO000OOOOO00O0 =f"Linux; Android 13; Pixel 6a"#line:511
        OO0O0OO0O0OO00OOO ="aarch64"#line:512
    OO0O00OOO0OOOOOO0 ={"os":OOO000OO0OOO00O0O ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":O00000OO0OO0O00O0 ,"os_arch":OO0O0OO0O0OO00OOO ,"system_locale":"ja-JP","client_build_number":O0O00O00OOO00OO00 ,"client_event_source":None ,"design_id":0 }#line:525
    OOOOO00O0OOO0OOO0 =f"Mozilla/5.0 ({O00OO000OOOOO00O0}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:526
    return base64 .b64encode (json .dumps (OO0O00OOO0OOOOOO0 ,separators =(',',':')).encode ()).decode (),OOOOO00O0OOO0OOO0 #line:527
def joiner (OOOOOOO00O0O0O000 ,OO0O0OO00OO0000OO ,O0OO0O0000O0OO0OO ,OO0OO0O00O0O00OOO ):#line:529
  OO0O0O0OO0O0O0000 =get_session (O0OO0O0000O0OO0OO )#line:530
  O0OO0O0OO0O0O0O0O =cookieset (OO0O0O0OO0O0O0000 )#line:531
  O0OO0O0OO0O0O0O0O ["locale"]="ja-JP"#line:532
  O000O0O0OO0OO0OOO =201211 #line:533
  OOOOOO00O00O00OO0 ,O00OOO00O00OOO0OO =generatexspandua (O000O0O0OO0OO0OOO )#line:534
  O00O00OOOOO0O0000 ={"Authorization":OOOOOOO00O0O0O000 ,"accept":"*/*","accept-language":"ja-JP","connection":"keep-alive","DNT":"1","origin":"https://discord.com","sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","referer":"https://discord.com/channels/@me","TE":"Trailers","user-agent":O00OOO00O00OOO0OO ,"X-Super-Properties":OOOOOO00O00O00OO0 ,}#line:549
  O000OOOO00OOO0OOO =OO0O0O0OO0O0O0000 .post ("https://discord.com/api/v9/invites/"+OO0O0OO00OO0000OO ,headers =O00O00OOOOO0O0000 ,json ={},cookies =O0OO0O0OO0O0O0O0O )#line:551
  if O000OOOO00OOO0OOO .status_code ==200 :#line:552
    print ("[+] Probably joined "+OOOOOOO00O0O0O000 )#line:553
    if "show_verification_form"in O000OOOO00OOO0OOO .json ():#line:554
      bypass (OOOOOOO00O0O0O000 ,O000OOOO00OOO0OOO .json ()["guild"]["id"],OO0O0O0OO0O0O0000 ,O00O00OOOOO0O0000 )#line:555
    return #line:556
  elif "captcha_key"in O000OOOO00OOO0OOO .text and O000OOOO00OOO0OOO .status_code ==400 :#line:557
    print ("[!] Hcaptcha interference "+OOOOOOO00O0O0O000 )#line:558
    return #line:559
  elif O000OOOO00OOO0OOO .status_code ==401 :#line:560
    print ("[!] Token is dead "+OOOOOOO00O0O0O000 )#line:561
    return #line:562
  elif O000OOOO00OOO0OOO .status_code ==403 :#line:563
    if "message"in O000OOOO00OOO0OOO .json ():#line:564
      if O000OOOO00OOO0OOO .json ()["message"]=="Unknown Message":#line:565
        print ("[!] Unknown error "+OOOOOOO00O0O0O000 )#line:566
        return #line:567
      else :#line:568
        print ("[!] Verification required "+OOOOOOO00O0O0O000 )#line:569
        return #line:570
    else :#line:571
      print ("[!] Error occurred "+OOOOOOO00O0O0O000 )#line:572
      return #line:573
  elif O000OOOO00OOO0OOO .status_code ==429 :#line:574
    print ("[!] Token rate-limited "+OOOOOOO00O0O0O000 )#line:575
    return #line:576
  elif O000OOOO00OOO0OOO .status_code ==400 :#line:577
    if "captcha_key"in O000OOOO00OOO0OOO .json ():#line:578
      print ("[!] Hcaptcha interference "+OOOOOOO00O0O0O000 )#line:579
      return #line:580
    else :#line:581
      print ("[!] Error occurred "+OOOOOOO00O0O0O000 )#line:582
      return #line:583
  elif O000OOOO00OOO0OOO .status_code ==401 :#line:584
    print ("[!] Token is dead "+OOOOOOO00O0O0O000 )#line:585
    return #line:586
  elif O000OOOO00OOO0OOO .status_code ==403 :#line:587
    if "message"in O000OOOO00OOO0OOO .json ():#line:588
      if O000OOOO00OOO0OOO .json ()["message"]=="Unknown Message":#line:589
        print ("[!] Unknown error "+OOOOOOO00O0O0O000 )#line:590
        return #line:591
      else :#line:592
        print ("[!] Verification required "+OOOOOOO00O0O0O000 )#line:593
        return #line:594
    else :#line:595
      print ("[!] Error occurred "+OOOOOOO00O0O0O000 )#line:596
  elif O000OOOO00OOO0OOO .status_code ==429 :#line:597
    print ("[!] Token rate-limited "+OOOOOOO00O0O0O000 )#line:598
    return #line:599
  else :#line:600
    print ("[!] Error occurred "+OOOOOOO00O0O0O000 )#line:601
    return #line:602
def update_group_ids ():#line:606
    O0OO0OO000OOO00OO =input ("Invite Code?: ").strip ()#line:607
    try :#line:608
        with open ("token.txt")as O0O000O0OOOO00O00 :#line:609
            O0OO0000O00OOOO0O =[O0O00OO0000O0O0OO .strip ()for O0O00OO0000O0O0OO in O0O000O0OOOO00O00 .readlines ()if O0O00OO0000O0O0OO .strip ()]#line:610
    except (FileNotFoundError ,KeyError ):#line:611
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:612
        return #line:613
    OO0O0O0OOOO00O000 =requests .Session ()#line:615
    for OOO0O000O00O0OO00 in O0OO0000O00OOOO0O :#line:616
        joiner (OOO0O000O00O0OO00 ,O0OO0OO000OOO00OO ,OO0O0O0OOOO00O000 )#line:617
        time .sleep (2 )#line:618
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:620
def bypass (OO0OOOO000O00O0OO ,O00O000O0O00OOO00 ,O00OOO0OO0OOO0O00 ,OOOOO0000OO00OOO0 ):#line:623
    try :#line:624
        O0OOO0O00000OOO00 =O00OOO0OO0OOO0O00 .get (f"https://discord.com/api/v9/guilds/{O00O000O0O00OOO00}/member-verification?with_guild=false",headers =OOOOO0000OO00OOO0 ).json ()#line:625
        OO0O0OO000OO0O0OO =O00OOO0OO0OOO0O00 .put (f"https://discord.com/api/v9/guilds/{O00O000O0O00OOO00}/requests/@me",headers =OOOOO0000OO00OOO0 ,json =O0OOO0O00000OOO00 )#line:626
        if OO0O0OO000OO0O0OO .status_code ==201 :#line:627
            print (f"[+] MemberscreeningBypassed {OO0OOOO000O00O0OO}")#line:628
            return #line:629
        else :#line:630
            print (f"[!] Bypassが出来ませんでした {OO0OOOO000O00O0OO}")#line:631
            return #line:632
    except Exception as OO00OO0OO0O0OO000 :#line:633
        print (f"[!] エラーが発生しました。{OO00OO0OO0O0OO000}")#line:634
session =requests .Session ()#line:636
def reactionput (OOO0OOOOOOOOO00O0 ,O0O00000OOOO00O00 ,O000OOO0OOO0000OO ,OO0000OOOOOOO0O00 ,proxy =None ):#line:639
    O0OO00O000O0000OO =get_session (proxy )#line:640
    OO000OO00O00OOO0O =get_headers (O0OO00O000O0000OO )#line:641
    OO000OO00O00OOO0O ["Authorization"]=OOO0OOOOOOOOO00O0 #line:642
    OO0000OOOOOOO0O00 =requests .utils .quote (OO0000OOOOOOO0O00 )#line:644
    O0O0000O0O00OOO0O =O0OO00O000O0000OO .put (f"https://discord.com/api/v9/channels/{O0O00000OOOO00O00}/messages/{O000OOO0OOO0000OO}/reactions/{OO0000OOOOOOO0O00}/%40me?location=Message&type=0",headers =OO000OO00O00OOO0O )#line:648
    if O0O0000O0O00OOO0O .status_code in [200 ,204 ]:#line:649
        print (f"[+] Reaction '{OO0000OOOOOOO0O00}' added successfully to message {O000OOO0OOO0000OO}")#line:650
    elif O0O0000O0O00OOO0O .status_code ==429 :#line:651
        print ("[-] Rate limited. Please wait before retrying.")#line:652
        O0O000O0O00O00OOO =O0O0000O0O00OOO0O .json ().get ("retry_after",1 )#line:653
        time .sleep (O0O000O0O00O00OOO )#line:654
    elif O0O0000O0O00OOO0O .status_code ==401 :#line:655
        print ("[-] Invalid or expired token.")#line:656
    else :#line:657
        print (f"[!] Error occurred: {O0O0000O0O00OOO0O.status_code}")#line:658
def generatexspandua (O0OOO00O00OO0OOOO ):#line:661
  OO0OO00OO00OO00OO =["Android","Windows","Macintosh"]#line:662
  O0OOOOO000000OOOO =random .choice (OO0OO00OO00OO00OO )#line:663
  if O0OOOOO000000OOOO =="Macintosh":#line:664
    OOOO0OOO00OO0O0O0 =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:665
    O00O0OOO00O00OOOO ="Macintosh; Intel Mac OS X "+OOOO0OOO00OO0O0O0 #line:666
    OO0O0OOO0OO0O000O ="x86_64"#line:667
  if O0OOOOO000000OOOO =="Windows":#line:668
    OOOO0OOO00OO0O0O0 =f'{random.choice([6.0,10.0,11.0])}'#line:669
    O00O0OOO00O00OOOO ="Windows NT "+OOOO0OOO00OO0O0O0 +" Win64; x64"#line:670
    OO0O0OOO0OO0O000O ="x86_64"#line:671
  if O0OOOOO000000OOOO =="Android":#line:672
    OOOO0OOO00OO0O0O0 ="13"#line:673
    O00O0OOO00O00OOOO =f"Linux; Android 13; Pixel 6a"#line:674
    OO0O0OOO0OO0O000O ="aarch64"#line:675
  O000O000000O0OOO0 ={"os":O0OOOOO000000OOOO ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":OOOO0OOO00OO0O0O0 ,"os_arch":OO0O0OOO0OO0O000O ,"system_locale":"ja-JP","client_build_number":O0OOO00O00OO0OOOO ,"client_event_source":None ,"design_id":0 }#line:676
  O0O00O00OO000OO0O =f"Mozilla/5.0 ({O00O0OOO00O00OOOO}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:677
  return base64 .b64encode (json .dumps (O000O000000O0OOO0 ,separators =(',',':')).encode ()).decode (),O0O00O00OO000OO0O #line:678
import base64 #line:680
def nickchanger ():#line:683
    try :#line:684
        with open ("token.txt")as O00O0O0OOOO0O0OOO :#line:685
            O0OO0000O00O0OOOO =[OOO0O0O00O0000OO0 .strip ()for OOO0O0O00O0000OO0 in O00O0O0OOOO0O0OOO .readlines ()if OOO0O0O00O0000OO0 .strip ()]#line:686
    except (FileNotFoundError ,KeyError ):#line:687
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:688
        return #line:689
    O000O0O0OOO000000 =input ("Server ID?: ").strip ()#line:691
    O0O0OO0O0000OOO00 =input ("Nickname?: ").strip ()#line:692
    O00O00O0OOOO000OO =input ("Delay (in seconds)?: ").strip ()#line:693
    try :#line:695
        O00O00O0OOOO000OO =float (O00O00O0OOOO000OO )#line:696
        if O00O00O0OOOO000OO <0 :#line:697
            raise ValueError #line:698
    except ValueError :#line:699
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:700
        O00O00O0OOOO000OO =1.0 #line:701
    for O0OOOO0OOO0OO0OO0 in O0OO0000O00O0OOOO :#line:703
        OO0OOOOOO0O000000 ={"Authorization":O0OOOO0OOO0OO0OO0 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:708
        O00000O0OO0000O0O ={"nick":O0O0OO0O0000OOO00 }#line:709
        O00O0OOO00OOOOOO0 =requests .patch (f"https://discord.com/api/v9/guilds/{O000O0O0OOO000000}/members/@me",headers =OO0OOOOOO0O000000 ,json =O00000O0OO0000O0O )#line:710
        if O00O0OOO00OOOOOO0 .status_code ==200 :#line:712
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Nickname changed to '{O0O0OO0O0000OOO00}' successfully for token {O0OOOO0OOO0OO0OO0}.{colorama.Fore.RESET}")#line:713
        elif O00O0OOO00OOOOOO0 .status_code ==429 :#line:714
            print (f"{colorama.Fore.RED}    [!] Rate limited. Please wait before retrying for token {O0OOOO0OOO0OO0OO0}.{colorama.Fore.RESET}")#line:715
            OO0O0O0OOO000OO0O =O00O0OOO00OOOOOO0 .json ().get ("retry_after",1 )#line:716
            time .sleep (OO0O0O0OOO000OO0O )#line:717
        else :#line:718
            print (f"{colorama.Fore.RED}    [!] Error occurred: {O00O0OOO00OOOOOO0.status_code} for token {O0OOOO0OOO0OO0OO0}.{colorama.Fore.RESET}")#line:719
        time .sleep (O00O00O0OOOO000OO )#line:721
import json ,websocket ,threading ,tls_client ,random ,time #line:725
session =tls_client .Session (client_identifier ="chrome112",random_tls_extension_order =True )#line:727
class Utils :#line:729
    @staticmethod #line:730
    def rangeCorrector (O00OOO00O0OOOO000 ):#line:731
        if [0 ,99 ]not in O00OOO00O0OOOO000 :#line:732
            O00OOO00O0OOOO000 .insert (0 ,[0 ,99 ])#line:733
        return O00OOO00O0OOOO000 #line:734
    @staticmethod #line:736
    def getRanges (O00OOOO0000O000OO ,O000OOOOO0OOOO00O ,OOOOOO0OOO00OO000 ):#line:737
        OOOO000OOOOO0OO00 =int (O00OOOO0000O000OO *O000OOOOO0OOOO00O )#line:738
        OO0O0000000000O0O =[[OOOO000OOOOO0OO00 ,OOOO000OOOOO0OO00 +99 ]]#line:739
        if OOOOOO0OOO00OO000 >OOOO000OOOOO0OO00 +99 :#line:740
            OO0O0000000000O0O .append ([OOOO000OOOOO0OO00 +100 ,OOOO000OOOOO0OO00 +199 ])#line:741
        return Utils .rangeCorrector (OO0O0000000000O0O )#line:742
    @staticmethod #line:744
    def parseGuildMemberListUpdate (OOOOO0OO00O00O000 ):#line:745
        O0O000OOO0O0000OO ={"online_count":OOOOO0OO00O00O000 ["d"]["online_count"],"member_count":OOOOO0OO00O00O000 ["d"]["member_count"],"id":OOOOO0OO00O00O000 ["d"]["id"],"guild_id":OOOOO0OO00O00O000 ["d"]["guild_id"],"hoisted_roles":OOOOO0OO00O00O000 ["d"]["groups"],"types":[],"locations":[],"updates":[],}#line:755
        for O0O0O00O00000OOOO in OOOOO0OO00O00O000 ["d"]["ops"]:#line:757
            O0O000OOO0O0000OO ["types"].append (O0O0O00O00000OOOO ["op"])#line:758
            if O0O0O00O00000OOOO ["op"]in ("SYNC","INVALIDATE"):#line:759
                O0O000OOO0O0000OO ["locations"].append (O0O0O00O00000OOOO ["range"])#line:760
                if O0O0O00O00000OOOO ["op"]=="SYNC":#line:761
                    O0O000OOO0O0000OO ["updates"].append (O0O0O00O00000OOOO ["items"])#line:762
                else :#line:763
                    O0O000OOO0O0000OO ["updates"].append ([])#line:764
            elif O0O0O00O00000OOOO ["op"]in ("INSERT","UPDATE","DELETE"):#line:765
                O0O000OOO0O0000OO ["locations"].append (O0O0O00O00000OOOO ["index"])#line:766
                if O0O0O00O00000OOOO ["op"]=="DELETE":#line:767
                    O0O000OOO0O0000OO ["updates"].append ([])#line:768
                else :#line:769
                    O0O000OOO0O0000OO ["updates"].append (O0O0O00O00000OOOO ["item"])#line:770
        return O0O000OOO0O0000OO #line:771
class DiscordSocket (websocket .WebSocketApp ):#line:773
    def __init__ (O00OOO0O000OOOOO0 ,O0OO0OO00OOOO0O00 ,OO0O000OOOOOOOOO0 ,OOO0000OOOO000O0O ):#line:774
        O00OOO0O000OOOOO0 .token =O0OO0OO00OOOO0O00 #line:775
        O00OOO0O000OOOOO0 .guild_id =OO0O000OOOOOOOOO0 #line:776
        O00OOO0O000OOOOO0 .channel_id =OOO0000OOOO000O0O #line:777
        O00OOO0O000OOOOO0 .socket_headers ={"Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","Cache-Control":"no-cache","Pragma":"no-cache","Sec-WebSocket-Extensions":"permessage-deflate; client_max_window_bits","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",}#line:785
        super ().__init__ ("wss://gateway.discord.gg/?encoding=json&v=9",header =O00OOO0O000OOOOO0 .socket_headers ,on_open =lambda O0OOOO00OO00OO0OO :O00OOO0O000OOOOO0 .sock_open (O0OOOO00OO00OO0OO ),on_message =lambda OOOOO00O000OOOOOO ,O00OOO0000O0O00OO :O00OOO0O000OOOOO0 .sock_message (OOOOO00O000OOOOOO ,O00OOO0000O0O00OO ),on_close =lambda OOOOOO0OO0OO0O00O ,OO00OOOOO0O00OO00 ,O000O0OO0OOOOO00O :O00OOO0O000OOOOO0 .sock_close (OOOOOO0OO0OO0O00O ,OO00OOOOO0O00OO00 ,O000O0OO0OOOOO00O ),)#line:794
        O00OOO0O000OOOOO0 .endScraping =False #line:796
        O00OOO0O000OOOOO0 .guilds ={}#line:797
        O00OOO0O000OOOOO0 .members ={}#line:798
        O00OOO0O000OOOOO0 .ranges =[[0 ,0 ]]#line:799
        O00OOO0O000OOOOO0 .lastRange =0 #line:800
        O00OOO0O000OOOOO0 .packets_recv =0 #line:801
    def run (O00O0OOO0O0O00000 ):#line:803
        O00O0OOO0O0O00000 .run_forever ()#line:804
        return O00O0OOO0O0O00000 .members #line:805
    def scrapeUsers (O0O0OOOO000O00O00 ):#line:807
        if not O0O0OOOO000O00O00 .endScraping :#line:808
            O0O0OOOO000O00O00 .send ('{"op":14,"d":{"guild_id":"'+O0O0OOOO000O00O00 .guild_id +'","typing":true,"activities":true,"threads":true,"channels":{"'+O0O0OOOO000O00O00 .channel_id +'":'+json .dumps (O0O0OOOO000O00O00 .ranges )+"}}}")#line:817
    def sock_open (O0OO0000O0O0OOO0O ,O0OOOOO0000OO000O ):#line:819
        O0OO0000O0O0OOO0O .send ('{"op":2,"d":{"token":"'+O0OO0000O0O0OOO0O .token +'","capabilities":125,"properties":{"os":"Windows NT","browser":"Chrome","device":"","system_locale":"it-IT","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36","browser_version":"119.0","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":103981,"client_event_source":null},"presence":{"status":"online","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}')#line:824
    def heartbeatThread (OOO0O000O00OO0000 ,OO0OOO0O000O0OO00 ):#line:826
        try :#line:827
            while True :#line:828
                OOO0O000O00OO0000 .send ('{"op":1,"d":'+str (OOO0O000O00OO0000 .packets_recv )+"}")#line:829
                time .sleep (OO0OOO0O000O0OO00 )#line:830
        except Exception as O0O0O0O0000O0O0OO :#line:831
            pass #line:832
    def sock_message (O00OO0O00O00O00OO ,O00OOOO00000O00O0 ,OO00000000O000O0O ):#line:834
        OO0OO0OOO00OO0OO0 =json .loads (OO00000000O000O0O )#line:835
        if OO0OO0OOO00OO0OO0 is None :#line:836
            return #line:837
        if OO0OO0OOO00OO0OO0 ["op"]!=11 :#line:838
            O00OO0O00O00O00OO .packets_recv +=1 #line:839
        if OO0OO0OOO00OO0OO0 ["op"]==10 :#line:840
            threading .Thread (target =O00OO0O00O00O00OO .heartbeatThread ,args =(OO0OO0OOO00OO0OO0 ["d"]["heartbeat_interval"]/1000 ,),daemon =True ,).start ()#line:845
        if OO0OO0OOO00OO0OO0 ["t"]=="READY":#line:846
            for OOO000O00OOOO0O0O in OO0OO0OOO00OO0OO0 ["d"]["guilds"]:#line:847
                O00OO0O00O00O00OO .guilds [OOO000O00OOOO0O0O ["id"]]={"member_count":OOO000O00OOOO0O0O ["member_count"]}#line:848
        if OO0OO0OOO00OO0OO0 ["t"]=="READY_SUPPLEMENTAL":#line:849
            O00OO0O00O00O00OO .ranges =Utils .getRanges (0 ,100 ,O00OO0O00O00O00OO .guilds [O00OO0O00O00O00OO .guild_id ]["member_count"])#line:852
            O00OO0O00O00O00OO .scrapeUsers ()#line:853
        elif OO0OO0OOO00OO0OO0 ["t"]=="GUILD_MEMBER_LIST_UPDATE":#line:854
            O0OOO00O0O0000O0O =Utils .parseGuildMemberListUpdate (OO0OO0OOO00OO0OO0 )#line:855
            if O0OOO00O0O0000O0O ["guild_id"]==O00OO0O00O00O00OO .guild_id and ("SYNC"in O0OOO00O0O0000O0O ["types"]or "UPDATE"in O0OOO00O0O0000O0O ["types"]):#line:859
                for O00O00OOO0OOO00O0 ,OOO00O0O0O0O0O000 in enumerate (O0OOO00O0O0000O0O ["types"]):#line:860
                    if OOO00O0O0O0O0O000 =="SYNC":#line:861
                        if len (O0OOO00O0O0000O0O ["updates"][O00O00OOO0OOO00O0 ])==0 :#line:862
                            O00OO0O00O00O00OO .endScraping =True #line:863
                            break #line:864
                        for OO00OOOO0O000OO00 in O0OOO00O0O0000O0O ["updates"][O00O00OOO0OOO00O0 ]:#line:866
                            if "member"in OO00OOOO0O000OO00 :#line:867
                                OOO00O0OOO00O0000 =OO00OOOO0O000OO00 ["member"]#line:868
                                O000OO0OOO0O0O000 ={"tag":OOO00O0OOO00O0000 ["user"]["username"]+"#"+OOO00O0OOO00O0000 ["user"]["discriminator"],"id":OOO00O0OOO00O0000 ["user"]["id"],}#line:874
                                if not OOO00O0OOO00O0000 ["user"].get ("bot"):#line:875
                                    O00OO0O00O00O00OO .members [OOO00O0OOO00O0000 ["user"]["id"]]=O000OO0OOO0O0O000 #line:876
                    elif OOO00O0O0O0O0O000 =="UPDATE":#line:878
                        for OO00OOOO0O000OO00 in O0OOO00O0O0000O0O ["updates"][O00O00OOO0OOO00O0 ]:#line:879
                            if "member"in OO00OOOO0O000OO00 :#line:880
                                OOO00O0OOO00O0000 =OO00OOOO0O000OO00 ["member"]#line:881
                                O000OO0OOO0O0O000 ={"tag":OOO00O0OOO00O0000 ["user"]["username"]+"#"+OOO00O0OOO00O0000 ["user"]["discriminator"],"id":OOO00O0OOO00O0000 ["user"]["id"],}#line:887
                                if not OOO00O0OOO00O0000 ["user"].get ("bot"):#line:888
                                    O00OO0O00O00O00OO .members [OOO00O0OOO00O0000 ["user"]["id"]]=O000OO0OOO0O0O000 #line:889
                    O00OO0O00O00O00OO .lastRange +=1 #line:891
                    O00OO0O00O00O00OO .ranges =Utils .getRanges (O00OO0O00O00O00OO .lastRange ,100 ,O00OO0O00O00O00OO .guilds [O00OO0O00O00O00OO .guild_id ]["member_count"])#line:894
                    time .sleep (0.45 )#line:895
                    O00OO0O00O00O00OO .scrapeUsers ()#line:896
            if O00OO0O00O00O00OO .endScraping :#line:898
                O00OO0O00O00O00OO .close ()#line:899
    def sock_close (O00O0O00OOO00OOO0 ,OOO0O0OO0O0OO0OOO ,O0O0OO0OO00O00OO0 ,O0OOO0000OOOOOO00 ):#line:901
        pass #line:902
def scrape (OOOOO00O0O0OO0O0O ,O0O000OOOOOO000O0 ,O0O0000O00OOOO000 ):#line:904
    OOO000OOO00000OOO =DiscordSocket (OOOOO00O0O0OO0O0O ,O0O000OOOOOO000O0 ,O0O0000O00OOOO000 )#line:905
    return OOO000OOO00000OOO .run ()#line:906
def member_scrape (O0OOO000O00OOOO00 ,OOOO000OOO00O0O00 ,OOOO0000O00O00OOO ):#line:908
    O0O0O0O0O0O00O000 =[]#line:909
    for O0O0O00OOO00OOOO0 in O0OOO000O00OOOO00 :#line:910
        O00O0OO0OO00OOOOO ={"Authorization":O0O0O00OOO00OOOO0 ,"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}#line:911
        O00OO0000O0OOOOO0 =session .get (f"https://canary.discord.com/api/v9/guilds/{OOOO000OOO00O0O00}",headers =O00O0OO0OO00OOOOO )#line:912
        if O00OO0000O0OOOOO0 .status_code ==200 :#line:913
            O0O0O0O0O0O00O000 .append (O0O0O00OOO00OOOO0 )#line:914
            break #line:915
    if not O0O0O0O0O0O00O000 :#line:916
        print ("missing access")#line:917
    O0O0O00OOO00OOOO0 =random .choice (O0O0O0O0O0O00O000 )#line:919
    OOO0OOO0O000OO0O0 =scrape (O0O0O00OOO00OOOO0 ,OOOO000OOO00O0O00 ,OOOO0000O00O00OOO )#line:920
    O0O000O000OO0OOO0 =[f"<@{O0O0OOO0O00O00OO0}>"for O0O0OOO0O00O00OO0 in [int (OO0OOOOOO0O00O00O )for OO0OOOOOO0O00O00O in OOO0OOO0O000OO0O0 .keys ()]]#line:921
    print (f"[SUCCESS] {len(O0O000O000OO0OOO0)} scraped members")#line:922
    return O0O000O000OO0OOO0 #line:923
def spammer_menu ():#line:925
    try :#line:926
        with open ("token.txt")as OOOOOOO0O00O0O0O0 :#line:927
            OOO0OO0O00OO00OOO =[O00OO0O0O0O000O00 .strip ()for O00OO0O0O0O000O00 in OOOOOOO0O00O0O0O0 .readlines ()if O00OO0O0O0O000O00 .strip ()]#line:928
    except (FileNotFoundError ,KeyError ):#line:929
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:930
        return #line:931
    O0O0OO0OOO0OOO000 =input ("Server ID?: ").strip ()#line:933
    OOO0O00OO0O00000O =input ("Message?: ").strip ()#line:934
    OOO00OOOOOOOO0O00 =input ("Random mention (True/False)?: ").strip ().lower ()=='true'#line:935
    OOO0OOOOOO00OOO00 =input ("Delay between messages (in seconds)?: ").strip ()#line:936
    O0OOO0000O000000O =input ("Number of messages to send?: ").strip ()#line:937
    O0O00O0OOOO00O0O0 =input ("Blacklist User IDs (comma-separated) (Leave blank to skip)?: ").strip ().split (',')#line:938
    O0O00O0OOOO00O0O0 =[f"<@{O000OO000O00O0O0O.strip()}>"for O000OO000O00O0O0O in O0O00O0OOOO00O0O0 if O000OO000O00O0O0O .strip ()]#line:939
    try :#line:941
        OOO0OOOOOO00OOO00 =float (OOO0OOOOOO00OOO00 )#line:942
        if OOO0OOOOOO00OOO00 <0 :#line:943
            raise ValueError #line:944
    except ValueError :#line:945
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:946
        OOO0OOOOOO00OOO00 =1.0 #line:947
    try :#line:949
        O0OOO0000O000000O =int (O0OOO0000O000000O )#line:950
        if O0OOO0000O000000O <=0 :#line:951
            raise ValueError #line:952
    except ValueError :#line:953
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:954
        O0OOO0000O000000O =1 #line:955
    OOOO000O00O000OOO =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:957
    if OOOO000O00O000OOO =='2':#line:958
        OO000O0O0O0O00000 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:959
        OO000O0O0O0O00000 =[OOO0OO000O0000OOO .strip ()for OOO0OO000O0000OOO in OO000O0O0O0O00000 if OOO0OO000O0000OOO .strip ()]#line:960
    else :#line:961
        OO000O0O0O0O00000 =fetch_channels (OOO0OO0O00OO00OOO [0 ],O0O0OO0OOO0OOO000 )#line:962
    O00OO00OOO0OO0O0O =None #line:964
    spammer (OOO0OO0O00OO00OOO ,O0O0OO0OOO0OOO000 ,OO000O0O0O0O00000 ,OOO0O00OO0O00000O ,OOO00OOOOOOOO0O00 ,O0O00O0OOOO00O0O0 ,O00OO00OOO0OO0O0O ,O0OOO0000O000000O )#line:966
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:968
import discum #line:971
import discum #line:972
import random #line:973
import time #line:974
def userget (O0OOO0O000O0OOO0O ,OOOOOOO00O0O00O00 ,O0OO0O0O0O000O00O ):#line:976
    OOO00O0OO00O0O000 =[]#line:977
    O0OOOOO00OO0O0OO0 =discum .Client (token =O0OOO0O000O0OOO0O ,log =False )#line:978
    try :#line:979
        O0OOOOO00OO0O0OO0 .gateway .close ()#line:980
    except :#line:981
        print ("Err")#line:982
    def O000O000O00000O0O (O0OOOOOOO00OOO0O0 ,O0O0OO00000OO0O0O ):#line:984
        if O0OOOOO00OO0O0OO0 .gateway .finishedMemberFetching (O0O0OO00000OO0O0O ):#line:985
            O00O00OO00O0O000O =len (O0OOOOO00OO0O0OO0 .gateway .session .guild (O0O0OO00000OO0O0O ).members )#line:986
            print (str (O00O00OO00O0O000O )+' members fetched')#line:987
            O0OOOOO00OO0O0OO0 .gateway .removeCommand ({'function':O000O000O00000O0O ,'params':{'guild_id':O0O0OO00000OO0O0O }})#line:988
            O0OOOOO00OO0O0OO0 .gateway .close ()#line:989
    def O00OOO00O00OO000O (OOOO0000O0OO0O00O ,O00O0O00OO0OOO000 ):#line:991
        O0OOOOO00OO0O0OO0 .gateway .fetchMembers (OOOO0000O0OO0O00O ,O00O0O00OO0OOO000 ,keep ='all',wait =1 )#line:992
        O0OOOOO00OO0O0OO0 .gateway .command ({'function':O000O000O00000O0O ,'params':{'guild_id':OOOO0000O0OO0O00O }})#line:993
        O0OOOOO00OO0O0OO0 .gateway .run ()#line:994
        O0OOOOO00OO0O0OO0 .gateway .resetSession ()#line:995
        return O0OOOOO00OO0O0OO0 .gateway .session .guild (OOOO0000O0OO0O00O ).members #line:996
    O00OO0OOOOO000000 =O00OOO00O00OO000O (OOOOOOO00O0O00O00 ,O0OO0O0O0O000O00O )#line:998
    for OO0O000O0O0OOO00O in O00OO0OOOOO000000 :#line:999
        if OO0O000O0O0OOO00O not in OOO00O0OO00O0O000 :#line:1000
            OOO00O0OO00O0O000 .append (f"<@{OO0O000O0O0OOO00O}>")#line:1001
    return OOO00O0OO00O0O000 #line:1002
def get_session (proxy =None ):#line:1004
    O0O00OOOOO00O00O0 =requests .Session ()#line:1005
    if proxy :#line:1006
        O0O00OOOOO00O00O0 .proxies .update ({'http':proxy ,'https':proxy })#line:1007
    return O0O00OOOOO00O00O0 #line:1008
def get_headers (O0O0OO0OO0O0O0000 ):#line:1010
    return {"Authorization":O0O0OO0OO0O0O0000 ,"Content-Type":"application/json"}#line:1014
def spammer (O00O000O000000OOO ,O0O000OO00O0000OO ,OOOOOOO0OO0OO0O00 ,OO00OOOO00000000O ,O000OO0OOO000OO00 ,O0OOO00OO0O0O000O ,O0O000OOOOO0OO0O0 ,OOOO0OOO0OOO0OO00 ):#line:1016
    OO0000000O00O0O00 =get_session (O0O000OOOOO0OO0O0 )#line:1017
    OOO00OO00OO0OOO00 =0 #line:1018
    O0O00O0O00000OOOO =userget (O00O000O000000OOO [0 ],O0O000OO00O0000OO ,OOOOOOO0OO0OO0O00 [0 ])#line:1020
    O0O00O0O00000OOOO =[O00O0O00O00OO0OO0 for O00O0O00O00OO0OO0 in O0O00O0O00000OOOO if O00O0O00O00OO0OO0 not in O0OOO00OO0O0O000O ]#line:1023
    for _OOOOO000OOO000O00 in range (OOOO0OOO0OOO0OO00 ):#line:1025
        OO0O0O0OOO0OOOOO0 =O00O000O000000OOO [OOO00OO00OO0OOO00 ]#line:1026
        O000O0OOOOO00000O =get_headers (OO0O0O0OOO0OOOOO0 )#line:1027
        for OO00OOOOO0OO00O0O in OOOOOOO0OO0OO0O00 :#line:1028
            O00OOO0OOO0OO0O00 =OO00OOOO00000000O #line:1029
            if O000OO0OOO000OO00 and O0O00O0O00000OOOO :#line:1030
                OO000O000O0000O0O =random .choice (O0O00O0O00000OOOO )#line:1031
                O00OOO0OOO0OO0O00 +=f" {OO000O000O0000O0O}"#line:1032
            O0O0OOOO000OO0OO0 =OO0000000O00O0O00 .post (f"https://discord.com/api/v9/channels/{OO00OOOOO0OO00O0O}/messages",json ={"content":O00OOO0OOO0OO0O00 },headers =O000O0OOOOO00000O )#line:1034
            if O0O0OOOO000OO0OO0 .status_code ==200 :#line:1035
                print (f"200 message sent: {OO0O0O0OOO0OOOOO0}")#line:1036
            elif O0O0OOOO000OO0OO0 .status_code ==429 :#line:1037
                print (f"429 rate limit: {OO0O0O0OOO0OOOOO0}")#line:1038
                O0O0O0000OOO0OO00 =O0O0OOOO000OO0OO0 .json ().get ("retry_after",1 )#line:1039
                time .sleep (O0O0O0000OOO0OO00 )#line:1040
            elif O0O0OOOO000OO0OO0 .status_code ==401 :#line:1041
                print (f"401 unknown token: {OO0O0O0OOO0OOOOO0}")#line:1042
            else :#line:1043
                print (f"error: {OO0O0O0OOO0OOOOO0}")#line:1044
        OOO00OO00OO0OOO00 =(OOO00OO00OO0OOO00 +1 )%len (O00O000O000000OOO )#line:1046
        time .sleep (1 )#line:1047
import requests #line:1052
import base64 #line:1053
import colorama #line:1054
import time #line:1055
def add_emojis_from_files ():#line:1057
    try :#line:1058
        with open ("emojiname.txt")as O000O000O0OOOOO00 ,open ("emojiurl.txt")as OO00OOOO00O0OOO0O :#line:1059
            OO000000O00OO0O0O =[O0O0000000OO000OO .strip ()for O0O0000000OO000OO in O000O000O0OOOOO00 .read ().split (',')if O0O0000000OO000OO .strip ()]#line:1060
            O0O00O0O0OOOOO000 =[O0000OO0OO00000O0 .strip ()for O0000OO0OO00000O0 in OO00OOOO00O0OOO0O .read ().split (',')if O0000OO0OO00000O0 .strip ()]#line:1061
    except FileNotFoundError as OOO0OO00OO0000OO0 :#line:1062
        print (f"{colorama.Fore.RED}    [!] Error: {str(OOO0OO00OO0000OO0)}{colorama.Fore.RESET}")#line:1063
        return #line:1064
    if len (OO000000O00OO0O0O )!=len (O0O00O0O0OOOOO000 ):#line:1066
        print (f"{colorama.Fore.RED}    [!] Error: The number of emoji names and URLs do not match!{colorama.Fore.RESET}")#line:1067
        return #line:1068
    try :#line:1070
        with open ("token.txt")as OO00OOOOO0O0O0O00 :#line:1071
            O00OO0O0O00OOO000 =[O0O0O0OO0O0OOO000 .strip ()for O0O0O0OO0O0OOO000 in OO00OOOOO0O0O0O00 .readlines ()if O0O0O0OO0O0OOO000 .strip ()]#line:1072
    except FileNotFoundError as OOO0OO00OO0000OO0 :#line:1073
        print (f"{colorama.Fore.RED}    [!] Error: {str(OOO0OO00OO0000OO0)}{colorama.Fore.RESET}")#line:1074
        return #line:1075
    OOOOOO0OOOO00O0OO =input ("Enter the Guild ID: ").strip ()#line:1077
    OOOOO0O0O0000OOO0 =input ("Enter the rate limit between requests (in seconds): ").strip ()#line:1078
    try :#line:1080
        OOOOO0O0O0000OOO0 =float (OOOOO0O0O0000OOO0 )#line:1081
        if OOOOO0O0O0000OOO0 <0 :#line:1082
            raise ValueError #line:1083
    except ValueError :#line:1084
        print (f"{colorama.Fore.RED}    [!] Invalid rate limit. Using default rate limit of 5 seconds.{colorama.Fore.RESET}")#line:1085
        OOOOO0O0O0000OOO0 =5.0 #line:1086
    O00O0000O0O0O0O0O =set ()#line:1088
    for O0000OO0000O0000O in O00OO0O0O00OOO000 :#line:1090
        O0OO0000OO0000O0O ={'Authorization':O0000OO0000O0000O ,'Content-Type':'application/json'}#line:1094
        O0O0OOOO00O0OOOO0 =requests .get (f"https://discord.com/api/v9/guilds/{OOOOOO0OOOO00O0OO}/emojis",headers =O0OO0000OO0000O0O )#line:1097
        if O0O0OOOO00O0OOOO0 .status_code ==200 :#line:1098
            OO0O00OO0OO000O00 =O0O0OOOO00O0OOOO0 .json ()#line:1099
            for OO000OOOOO00O0000 in OO0O00OO0OO000O00 :#line:1100
                O00O0000O0O0O0O0O .add (OO000OOOOO00O0000 ['name'])#line:1101
        else :#line:1102
            print (f"{colorama.Fore.RED}    [!] Error fetching existing emojis: {O0O0OOOO00O0OOOO0.status_code} - {O0O0OOOO00O0OOOO0.text}{colorama.Fore.RESET}")#line:1103
            continue #line:1104
    for O0OO0OO0OO00O0000 ,OO00000OOOO000000 in zip (OO000000O00OO0O0O ,O0O00O0O0OOOOO000 ):#line:1106
        if O0OO0OO0OO00O0000 in O00O0000O0O0O0O0O :#line:1107
            print (f"{colorama.Fore.YELLOW}    [*] Emoji '{O0OO0OO0OO00O0000}' already exists. Skipping...{colorama.Fore.RESET}")#line:1108
            continue #line:1109
        for O0000OO0000O0000O in O00OO0O0O00OOO000 :#line:1111
            try :#line:1112
                O0O0OOOO00O0OOOO0 =requests .get (OO00000OOOO000000 )#line:1113
                O0O0OOOO00O0OOOO0 .raise_for_status ()#line:1114
                OO0OOOOO0O0OOO0O0 =O0O0OOOO00O0OOOO0 .content #line:1115
                OO00000O00OOOOOOO =base64 .b64encode (OO0OOOOO0O0OOO0O0 ).decode ('utf-8')#line:1116
                OOO0O0OO000OO00OO ={'name':O0OO0OO0OO00O0000 ,'image':f"data:image/png;base64,{OO00000O00OOOOOOO}"}#line:1121
                O0OO0000OO0000O0O ={'Authorization':O0000OO0000O0000O ,'Content-Type':'application/json'}#line:1126
                O0OO00O0OOO000OO0 =requests .post (f"https://discord.com/api/v9/guilds/{OOOOOO0OOOO00O0OO}/emojis",headers =O0OO0000OO0000O0O ,json =OOO0O0OO000OO00OO )#line:1128
                if O0OO00O0OOO000OO0 .status_code ==201 :#line:1129
                    print (f"{colorama.Fore.GREEN}    [+] Successfully added emoji '{O0OO0OO0OO00O0000}' with token {O0000OO0000O0000O}{colorama.Fore.RESET}")#line:1130
                    O00O0000O0O0O0O0O .add (O0OO0OO0OO00O0000 )#line:1131
                    break #line:1132
                else :#line:1133
                    print (f"{colorama.Fore.RED}    [!] Failed to add emoji '{O0OO0OO0OO00O0000}' with token {O0000OO0000O0000O}: {O0OO00O0OOO000OO0.status_code} - {O0OO00O0OOO000OO0.text}{colorama.Fore.RESET}")#line:1134
                time .sleep (OOOOO0O0O0000OOO0 )#line:1136
            except Exception as OOO0OO00OO0000OO0 :#line:1137
                print (f"{colorama.Fore.RED}    [!] Error adding emoji '{O0OO0OO0OO00O0000}' with token {O0000OO0000O0000O}: {str(OOO0OO00OO0000OO0)}{colorama.Fore.RESET}")#line:1138
def main ():#line:1140
    colorama .init ()#line:1141
    while True :#line:1142
        logo ()#line:1143
        O000O00OO0OOOO0O0 =input (f"{colorama.Fore.LIGHTMAGENTA_EX}    [Final] Select an option from above: ")#line:1144
        if O000O00OO0OOOO0O0 =="0":#line:1146
            update_group_ids ()#line:1147
        elif O000O00OO0OOOO0O0 =="1":#line:1148
            join_discord_invite ()#line:1149
        elif O000O00OO0OOOO0O0 =="2":#line:1150
            reaction_spammer ()#line:1151
        elif O000O00OO0OOOO0O0 =="3":#line:1152
            send_messages_with_mentions ()#line:1153
        elif O000O00OO0OOOO0O0 =="4":#line:1154
            spammer_menu ()#line:1155
        elif O000O00OO0OOOO0O0 =="5":#line:1156
            nickchanger ()#line:1157
        elif O000O00OO0OOOO0O0 =="6":#line:1158
            add_emojis_from_files ()#line:1159
        elif O000O00OO0OOOO0O0 =="7":#line:1160
            reaction_art ()#line:1161
        elif O000O00OO0OOOO0O0 =="0":#line:1162
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [*] Exiting the application. Goodbye!{colorama.Fore.RESET}")#line:1163
            break #line:1164
        else :#line:1165
            print (f"{colorama.Fore.RED}    [!] Invalid option selected!{colorama.Fore.RESET}")#line:1166
        input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:1168
if __name__ =="__main__":#line:1170
    main ()#line:1171
