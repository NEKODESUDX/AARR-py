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
    OO00O0O00O000OOO0 =requests .Session ()#line:57
    if proxy :#line:58
        OO00O0O00O000OOO0 .proxies ={"http":proxy ,"https":proxy }#line:59
    return OO00O0O00O000OOO0 #line:60
def get_headers (OOOO0O0O00O0OO0OO ):#line:62
    return {"Authorization":OOOO0O0O00O0OO0OO ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:67
def send_message_with_mention (O0O0OO0O0OO00O0O0 ,O0OO00O00OOO00O00 ,OOO0OO0O0OO0000O0 ,OO0O0O0O000O0OO0O ):#line:70
    O0000OO0OO0000O00 =get_session ()#line:71
    OOO0O0O000O000O00 =get_headers (O0O0OO0O0OO00O0O0 )#line:72
    if OO0O0O0O000O0OO0O :#line:74
        O0O0OOO0O000O00OO =random .choice (OO0O0O0O000O0OO0O )#line:75
        OOO0OO0O0OO0000O0 +=f" <@{O0O0OOO0O000O00OO}>"#line:76
    O00OOO0O00O0000OO =O0000OO0OO0000O00 .post (f"https://discord.com/api/v9/channels/{O0OO00O00OOO00O00}/messages",headers =OOO0O0O000O000O00 ,json ={"content":OOO0OO0O0OO0000O0 })#line:82
    if O00OOO0O00O0000OO .status_code in [200 ,201 ]:#line:83
        print (f"[+] Message sent to channel {O0OO00O00OOO00O00}")#line:84
    elif O00OOO0O00O0000OO .status_code ==429 :#line:85
        print ("[-] Rate limited. Please wait before retrying.")#line:86
        OOOO0000O0O0O0O0O =O00OOO0O00O0000OO .json ().get ("retry_after",1 )#line:87
        time .sleep (OOOO0000O0O0O0O0O )#line:88
    else :#line:89
        print (f"[!] Error occurred: {O00OOO0O00O0000OO.status_code}")#line:90
def fetch_messages (OOOOO00OO0O0OO0O0 ,O00O000OOO0O00O00 ,limit =100 ):#line:93
    O0OOOOO0000O00O0O ={"Authorization":OOOOO00OO0O0OO0O0 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:98
    OOO000OO00OO0O00O =requests .get (f"https://discord.com/api/v9/channels/{O00O000OOO0O00O00}/messages?limit={limit}",headers =O0OOOOO0000O00O0O )#line:102
    if OOO000OO00OO0O00O .status_code ==200 :#line:103
        return OOO000OO00OO0O00O .json ()#line:104
    else :#line:105
        print (f"[!] Failed to fetch messages. HTTP Status Code: {OOO000OO00OO0O00O.status_code}")#line:106
        return []#line:107
import concurrent .futures #line:109
def reaction_spammer ():#line:111
    try :#line:112
        with open ("token.txt")as OO0O000O0OOO0OOOO :#line:113
            O00OO0O0O0O0O0O0O =[O0000O00OO0000OO0 .strip ()for O0000O00OO0000OO0 in OO0O000O0OOO0OOOO .readlines ()if O0000O00OO0000OO0 .strip ()]#line:114
    except (FileNotFoundError ,KeyError ):#line:115
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:116
        return #line:117
    OOOOOO0OOOO00OOOO =input ("Server ID?: ").strip ()#line:119
    O0OOO0OO000OO0OO0 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:121
    if O0OOO0OO000OO0OO0 =='2':#line:122
        OO00O00OOOOOOO000 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:123
        O00OOOOO000OOOOOO =[O0OOOO00000O0OOO0 .strip ()for O0OOOO00000O0OOO0 in OO00O00OOOOOOO000 if O0OOOO00000O0OOO0 .strip ()]#line:124
    else :#line:125
        O00OOOOO000OOOOOO =[]#line:126
        for O000OOO0000OO0O0O in O00OO0O0O0O0O0O0O :#line:127
            try :#line:128
                O00OOOOO000OOOOOO .extend (fetch_channels (O000OOO0000OO0O0O ,OOOOOO0OOOO00OOOO ))#line:129
            except Exception as O0OO0O0OOO0OOOOO0 :#line:130
                print (f"[!] Failed to fetch channels for token. Error: {O0OO0O0OOO0OOOOO0}")#line:131
                continue #line:132
    OOOO00OOOOO0000O0 =input ("Select your emoji (a, b, c, ... or custom emojis): ").strip ()#line:134
    OOOO0O00OO000000O =input ("Delay between reactions (in seconds)?: ").strip ()#line:135
    try :#line:137
        OOOO0O00OO000000O =float (OOOO0O00OO000000O )#line:138
        if OOOO0O00OO000000O <0 :#line:139
            raise ValueError #line:140
    except ValueError :#line:141
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:142
        OOOO0O00OO000000O =1.0 #line:143
    OO0O0OO0000OO00O0 =[]#line:145
    for OOOO0O0OOO0O000O0 in OOOO00OOOOO0000O0 .split (","):#line:146
        OOOO0O0OOO0O000O0 =OOOO0O0OOO0O000O0 .strip ().lower ()#line:147
        if OOOO0O0OOO0O000O0 in alphabet_to_flag :#line:148
            OO0O0OO0000OO00O0 .append (alphabet_to_flag [OOOO0O0OOO0O000O0 ])#line:149
        else :#line:150
            OO0O0OO0000OO00O0 .append (OOOO0O0OOO0O000O0 )#line:151
    if not OO0O0OO0000OO00O0 :#line:153
        print (f"{colorama.Fore.RED}    [!] No valid emojis provided!{colorama.Fore.RESET}")#line:154
        return #line:155
    def O000O000000OOO0O0 (OO0OOOOOO00000OO0 ):#line:157
        for O000OO0OO0OO0000O in O00OOOOO000OOOOOO :#line:158
            try :#line:159
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {O000OO0OO0OO0000O}...{colorama.Fore.RESET}")#line:160
                OO0O0OOOO000OO0OO =fetch_messages (OO0OOOOOO00000OO0 ,O000OO0OO0OO0000O ,limit =100 )#line:161
                if not OO0O0OOOO000OO0OO :#line:162
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:163
                    continue #line:164
                for O000000OOO0O000O0 in OO0O0OOOO000OO0OO :#line:166
                    for OOO0O0O0O0O0OO0O0 in OO0O0OO0000OO00O0 :#line:167
                        reactionput (OO0OOOOOO00000OO0 ,O000OO0OO0OO0000O ,O000000OOO0O000O0 ['id'],OOO0O0O0O0O0OO0O0 )#line:168
                        time .sleep (OOOO0O00OO000000O )#line:169
            except Exception as OO000O0OOO00O000O :#line:170
                print (f"[!] Error processing channel {O000OO0OO0OO0000O}. Error: {OO000O0OOO00O000O}")#line:171
                continue #line:172
    with concurrent .futures .ThreadPoolExecutor ()as OOOO00OOO0000OOO0 :#line:174
        OO0OO0O00OOO00000 =[OOOO00OOO0000OOO0 .submit (O000O000000OOO0O0 ,O00OOO0OOO00O0000 )for O00OOO0OOO00O0000 in O00OO0O0O0O0O0O0O ]#line:175
        concurrent .futures .wait (OO0OO0O00OOO00000 )#line:176
import requests #line:179
import json #line:180
import time #line:181
import colorama #line:182
alphabet_to_flag ={'a':'🇦','b':'🇧','c':'🇨','d':'🇩','e':'🇪','f':'🇫','g':'🇬','h':'🇭','i':'🇮','j':'🇯','k':'🇰','l':'🇱','m':'🇲','n':'🇳','o':'🇴','p':'🇵','q':'🇶','r':'🇷','s':'🇸','t':'🇹','u':'🇺','v':'🇻','w':'🇼','x':'🇽','y':'🇾','z':'🇿'}#line:190
def fetch_channels (O0O00O00O0O0OOO00 ,OOO00OOOO00000O00 ):#line:192
    OO00000O0O0OO00OO =f"https://discord.com/api/v9/guilds/{OOO00OOOO00000O00}/channels"#line:193
    OOOOO0O000O0O00O0 ={"Authorization":O0O00O00O0O0OOO00 }#line:194
    O0O00000O0OO0O0OO =requests .get (OO00000O0O0OO00OO ,headers =OOOOO0O000O0O00O0 )#line:195
    if O0O00000O0OO0O0OO .status_code ==200 :#line:196
        return [OOO0OOOOO0O0OO00O ['id']for OOO0OOOOO0O0OO00O in O0O00000O0OO0O0OO .json ()if OOO0OOOOO0O0OO00O ['type']==0 ]#line:197
    else :#line:198
        raise Exception (f"Failed to fetch channels: {O0O00000O0OO0O0OO.status_code} - {O0O00000O0OO0O0OO.text}")#line:199
def fetch_messages (OOO00O0OOO0O0OO00 ,OO0O00OOO0O0O0000 ,limit =100 ):#line:201
    O00OOO00OOOO0OO0O =f"https://discord.com/api/v9/channels/{OO0O00OOO0O0O0000}/messages?limit={limit}"#line:202
    OOO00OO000O0O000O ={"Authorization":OOO00O0OOO0O0OO00 }#line:203
    OOO0000OO00OOOOOO =requests .get (O00OOO00OOOO0OO0O ,headers =OOO00OO000O0O000O )#line:204
    if OOO0000OO00OOOOOO .status_code ==200 :#line:205
        return OOO0000OO00OOOOOO .json ()#line:206
    else :#line:207
        print (f"[!] Failed to fetch messages: {OOO0000OO00OOOOOO.status_code} - {OOO0000OO00OOOOOO.text}")#line:208
        return []#line:209
def reactionput (O0O0OO000OOO0OOOO ,O00OOOO0000O00OOO ,O000OO0OO0000O0O0 ,OOO00OO0OO0OO0OOO ):#line:211
    O0O00O000O00000O0 =f"https://discord.com/api/v9/channels/{O00OOOO0000O00OOO}/messages/{O000OO0OO0000O0O0}/reactions/{OOO00OO0OO0OO0OOO}/@me"#line:212
    OOO0OOO0O00O00OO0 ={"Authorization":O0O0OO000OOO0OOOO ,"Content-Type":"application/json"}#line:213
    O0000O00O000O00O0 =requests .put (O0O00O000O00000O0 ,headers =OOO0OOO0O00O00OO0 )#line:214
    if O0000O00O000O00O0 .status_code not in [204 ,200 ]:#line:215
        print (f"{colorama.Fore.RED}    [!] Failed to add reaction: {O0000O00O000O00O0.status_code} - {O0000O00O000O00O0.text}{colorama.Fore.RESET}")#line:216
import random #line:218
def reaction_art ():#line:220
    try :#line:221
        with open ("token.txt",encoding ="utf-8")as O0000000OO0OO0000 :#line:222
            OOO0O0OO000O0OOO0 =[O0O000OO00OO0OOOO .strip ()for O0O000OO00OO0OOOO in O0000000OO0OO0000 .readlines ()if O0O000OO00OO0OOOO .strip ()]#line:223
    except (FileNotFoundError ,KeyError ):#line:224
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:225
        return #line:226
    OOO00O0OO00O0000O =input ("Server ID?: ").strip ()#line:228
    OOOO000OOOO0O00OO =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:230
    if OOOO000OOOO0O00OO =='2':#line:231
        OO00OOOOO0O0OOO00 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:232
        OO0OOOOO0OOOO000O =[O0O0OO0O00OO0O0OO .strip ()for O0O0OO0O00OO0O0OO in OO00OOOOO0O0OOO00 if O0O0OO0O00OO0O0OO .strip ()]#line:233
    else :#line:234
        OO0OOOOO0OOOO000O =[]#line:235
        for OO000OO00OO00OOO0 in OOO0O0OO000O0OOO0 :#line:236
            try :#line:237
                OO0OOOOO0OOOO000O .extend (fetch_channels (OO000OO00OO00OOO0 ,OOO00O0OO00O0000O ))#line:238
            except Exception as O0O0O00OOO000O00O :#line:239
                print (f"[!] Failed to fetch channels for token. Error: {O0O0O00OOO000O00O}")#line:240
                continue #line:241
        random .shuffle (OO0OOOOO0OOOO000O )#line:242
    OO0OO0OO0OO0000O0 =input ("Delay between reactions (in seconds)?: ").strip ()#line:244
    try :#line:246
        OO0OO0OO0OO0000O0 =float (OO0OO0OO0OO0000O0 )#line:247
        if OO0OO0OO0OO0000O0 <0 :#line:248
            raise ValueError #line:249
    except ValueError :#line:250
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:251
        OO0OO0OO0OO0000O0 =1.0 #line:252
    try :#line:254
        with open ("art.txt",encoding ="utf-8")as OOO0O0O0O0OOO0OO0 :#line:255
            O0OOOOO0OOOO0O0O0 =[O0O0O00O00O0O0O00 .strip ()for O0O0O00O00O0O0O00 in OOO0O0O0O0OOO0OO0 .readlines ()if O0O0O00O00O0O0O00 .strip ()]#line:256
    except (FileNotFoundError ,KeyError ):#line:257
        print (f"{colorama.Fore.RED}    [!] Error: art.txt file not found or empty!{colorama.Fore.RESET}")#line:258
        return #line:259
    except UnicodeDecodeError as O0O0O00OOO000O00O :#line:260
        print (f"{colorama.Fore.RED}    [!] Error decoding art.txt: {str(O0O0O00OOO000O00O)}{colorama.Fore.RESET}")#line:261
        return #line:262
    if not O0OOOOO0OOOO0O0O0 :#line:264
        print (f"{colorama.Fore.RED}    [!] No valid art provided in art.txt!{colorama.Fore.RESET}")#line:265
        return #line:266
    O0OOOOO0OOOO0O0O0 .reverse ()#line:269
    for OO000OO00OO00OOO0 in OOO0O0OO000O0OOO0 :#line:271
        for OOOOO0O0000OOO000 in OO0OOOOO0OOOO000O :#line:272
            try :#line:273
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {OOOOO0O0000OOO000}...{colorama.Fore.RESET}")#line:274
                OO0OO000OO00OOOO0 =fetch_messages (OO000OO00OO00OOO0 ,OOOOO0O0000OOO000 ,limit =100 )#line:277
                if not OO0OO000OO00OOOO0 :#line:278
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:279
                    continue #line:280
                for O0O00O0000OOO00OO ,O00OOOO0O0O0O00OO in enumerate (OO0OO000OO00OOOO0 ):#line:283
                    O0O0000OOO00OO0OO =O0OOOOO0OOOO0O0O0 [O0O00O0000OOO00OO %len (O0OOOOO0OOOO0O0O0 )].split (',')#line:284
                    for O00OOO0OO00O0O0OO in O0O0000OOO00OO0OO :#line:285
                        reactionput (OO000OO00OO00OOO0 ,OOOOO0O0000OOO000 ,O00OOOO0O0O0O00OO ['id'],O00OOO0OO00O0O0OO .strip ())#line:286
                        print (f"Adding reaction '{O00OOO0OO00O0O0OO.strip()}' to message {O00OOOO0O0O0O00OO['id']} in channel {OOOOO0O0000OOO000}")#line:287
                        time .sleep (OO0OO0OO0OO0000O0 )#line:288
            except Exception as O0O0O00OOO000O00O :#line:289
                print (f"[!] Error processing channel {OOOOO0O0000OOO000}. Error: {O0O0O00OOO000O00O}")#line:290
                continue #line:291
    def O0OOOOOO00O0O0OO0 (O0OOO00OOO0000O0O ):#line:296
        for O0OOO00OOOO0O0OO0 in OO0OOOOO0OOOO000O :#line:297
            try :#line:298
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {O0OOO00OOOO0O0OO0}...{colorama.Fore.RESET}")#line:299
                O0O0O0OO0O00O0O0O =fetch_messages (O0OOO00OOO0000O0O ,O0OOO00OOOO0O0OO0 ,limit =100 )#line:300
                if not O0O0O0OO0O00O0O0O :#line:301
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:302
                    continue #line:303
                for OOO0000000O0O000O in O0O0O0OO0O00O0O0O :#line:305
                    for OOO000OO0OO0000O0 in O0O0000OOO00OO0OO :#line:306
                        reactionput (O0OOO00OOO0000O0O ,O0OOO00OOOO0O0OO0 ,OOO0000000O0O000O ['id'],OOO000OO0OO0000O0 )#line:307
                        time .sleep (OO0OO0OO0OO0000O0 )#line:308
            except Exception as O000OOO00000OO0OO :#line:309
                print (f"[!] Error processing channel {O0OOO00OOOO0O0OO0}. Error: {O000OOO00000OO0OO}")#line:310
                continue #line:311
    with concurrent .futures .ThreadPoolExecutor ()as OO0OOO0O000O00000 :#line:313
        OOOOOOOOOO0OOO0O0 =[OO0OOO0O000O00000 .submit (O0OOOOOO00O0O0OO0 ,OO0O0000OOOOO0000 )for OO0O0000OOOOO0000 in OOO0O0OO000O0OOO0 ]#line:314
        concurrent .futures .wait (OOOOOOOOOO0OOO0O0 )#line:315
def update_group_ids ():#line:318
    try :#line:319
        with open ("token.txt")as O0O0OOOO0OO0OO0OO :#line:320
            OO00OOOOO00O0OOO0 =[OOOO0OOOOOOO0O0O0 .strip ()for OOOO0OOOOOOO0O0O0 in O0O0OOOO0OO0OO0OO .readlines ()if OOOO0OOOOOOO0O0O0 .strip ()]#line:321
        OO0OO0O000OOOOO00 =OO00OOOOO00O0OOO0 [0 ]#line:322
    except (FileNotFoundError ,KeyError ):#line:323
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:324
        return #line:325
    O00O0OO00OO000000 ={"Authorization":OO0OO0O000OOOOO00 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:331
    O0O00O000O0OO0O00 =requests .get ('https://discord.com/api/v9/users/@me/channels',headers =O00O0OO00OO000000 )#line:333
    if O0O00O000O0OO0O00 .status_code ==200 :#line:334
        O000O00000O000OOO =O0O00O000O0OO0O00 .json ()#line:335
        with open ("group_id.txt","w")as O0O00O0O00000OOOO :#line:336
            for OOO0OOOOO0OOOOO00 in O000O00000O000OOO :#line:337
                if OOO0OOOOO0OOOOO00 ['type']==3 :#line:338
                    O0O00O0O00000OOOO .write (OOO0OOOOO0OOOOO00 ['id']+'\n')#line:339
        print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Group IDs updated successfully.{colorama.Fore.RESET}")#line:340
    else :#line:341
        print (f"{colorama.Fore.LIGHTRED_EX}    [!] Failed to retrieve group IDs. HTTP Status Code: {O0O00O000O0OO0O00.status_code}{colorama.Fore.RESET}")#line:342
import requests #line:344
import requests #line:346
def fetch_channels (O0OOOOOO00000O0OO ,OO00O0OO0O0O0O00O ):#line:348
    try :#line:349
        OOOO00OO0000O00OO =requests .Session ()#line:350
        O0O0OOO0O0O0OOOOO =get_headers (O0OOOOOO00000O0OO )#line:351
        OOO0O0OO00OOOOO0O =OOOO00OO0000O00OO .get (f"https://discord.com/api/v9/guilds/{OO00O0OO0O0O0O00O}/channels",headers =O0O0OOO0O0O0OOOOO ,timeout =10 )#line:358
        if OOO0O0OO00OOOOO0O .status_code ==200 :#line:361
            try :#line:362
                O00O0OOOOOO00OO00 =OOO0O0OO00OOOOO0O .json ()#line:363
                return [OO00OOOOOO000O000 ['id']for OO00OOOOOO000O000 in O00O0OOOOOO00OO00 if OO00OOOOOO000O000 .get ('type')==0 ]#line:364
            except ValueError :#line:365
                print ("[!] Error: Response was not valid JSON.")#line:366
                return []#line:367
        elif OOO0O0OO00OOOOO0O .status_code ==401 :#line:368
            print ("[!] Error: Unauthorized - check your token.")#line:369
        elif OOO0O0OO00OOOOO0O .status_code ==403 :#line:370
            print ("[!] Error: Forbidden - you lack permissions.")#line:371
        elif OOO0O0OO00OOOOO0O .status_code ==404 :#line:372
            print ("[!] Error: Server not found - check the server ID.")#line:373
        else :#line:374
            print (f"[!] Error: Unexpected status code {OOO0O0OO00OOOOO0O.status_code}.")#line:375
        return []#line:378
    except requests .exceptions .Timeout :#line:380
        print ("[!] Error: Request timed out. Check your connection or try again later.")#line:381
        return []#line:382
    except requests .exceptions .RequestException as O0O00O0OO0OOO0O00 :#line:383
        print (f"[!] Error: An error occurred while fetching channels: {O0O00O0OO0OOO0O00}")#line:384
        return []#line:385
def extract_uids_from_messages (OOO0OO0O0OOOOOOOO ):#line:391
    OO0OO00O000OOO00O =set ()#line:392
    for O0O0OO000OOOOOO0O in OOO0OO0O0OOOOOOOO :#line:393
        OO0OO00O000OOO00O .add (O0O0OO000OOOOOO0O ['author']['id'])#line:394
    return list (OO0OO00O000OOO00O )#line:395
def send_message_with_mention (OO0000O0OO00O0OOO ,OOO0O0000OO00OOOO ,OOO00OO0O000O0000 ,O000O0O00O0000OOO ):#line:397
    OO000000O000O000O =get_session ()#line:398
    O00OOO0O00000O00O =get_headers (OO0000O0OO00O0OOO )#line:399
    if O000O0O00O0000OOO :#line:401
        OOO000OOOOO0OO000 =random .choice (O000O0O00O0000OOO )#line:402
        OOO00OO0O000O0000 +=f" <@{OOO000OOOOO0OO000}>"#line:403
    OO00OOO0O00O000OO =OO000000O000O000O .post (f"https://discord.com/api/v9/channels/{OOO0O0000OO00OOOO}/messages",headers =O00OOO0O00000O00O ,json ={"content":OOO00OO0O000O0000 })#line:409
    if OO00OOO0O00O000OO .status_code in [200 ,201 ]:#line:410
        print (f"[+] Message sent to channel {OOO0O0000OO00OOOO}")#line:411
    elif OO00OOO0O00O000OO .status_code ==429 :#line:412
        print ("[-] Rate limited. Please wait before retrying.")#line:413
        O00O0O00OO00OOO00 =OO00OOO0O00O000OO .json ().get ("retry_after",1 )#line:414
        time .sleep (O00O0O00OO00OOO00 )#line:415
    else :#line:416
        print (f"[!] Error occurred: {OO00OOO0O00O000OO.status_code}")#line:417
def send_messages_with_mentions ():#line:418
    try :#line:419
        with open ("token.txt")as O0O00OOO00O0OO000 :#line:420
            O0OOOOOOOOOOOOO0O =[O0OO00OOOOO0O0000 .strip ()for O0OO00OOOOO0O0000 in O0O00OOO00O0OO000 .readlines ()if O0OO00OOOOO0O0000 .strip ()]#line:421
    except (FileNotFoundError ,KeyError ):#line:422
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:423
        return #line:424
    OOOOOO0O000OO00O0 =input ("Server ID?: ").strip ()#line:426
    OOOOOOOO0OO0O0O00 =input ("Delay between messages (in seconds)?: ").strip ()#line:427
    O0O0000O0OOO0O00O =input ("Number of messages to send?: ").strip ()#line:428
    OO0O00OOO0OOOOOO0 =input ("Message content?: ").strip ()#line:429
    O000OOO0O0OO0OO00 =input ("Blacklist User IDs (comma-separated)?: ").strip ().split (',')#line:430
    O000OOO0O0OO0OO00 =[O0O00000O00OOOO00 .strip ()for O0O00000O00OOOO00 in O000OOO0O0OO0OO00 if O0O00000O00OOOO00 .strip ()]#line:431
    try :#line:433
        OOOOOOOO0OO0O0O00 =float (OOOOOOOO0OO0O0O00 )#line:434
        if OOOOOOOO0OO0O0O00 <0 :#line:435
            raise ValueError #line:436
    except ValueError :#line:437
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:438
        OOOOOOOO0OO0O0O00 =1.0 #line:439
    try :#line:441
        O0O0000O0OOO0O00O =int (O0O0000O0OOO0O00O )#line:442
        if O0O0000O0OOO0O00O <=0 :#line:443
            raise ValueError #line:444
    except ValueError :#line:445
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:446
        O0O0000O0OOO0O00O =1 #line:447
    O00O00O00000O00O0 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:449
    if O00O00O00000O00O0 =='2':#line:450
        O0OO0O000O0OOO000 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:451
        O0OO0O000O0OOO000 =[O000O000OOOOOOO00 .strip ()for O000O000OOOOOOO00 in O0OO0O000O0OOO000 if O000O000OOOOOOO00 .strip ()]#line:452
    else :#line:453
        O0OO0O000O0OOO000 =[]#line:454
    O00O0O000OOO00OOO =set ()#line:456
    for O00000OO0OOOO0O0O in O0OOOOOOOOOOOOO0O :#line:457
        OO0OO0O00OOOO00OO =fetch_channels (O00000OO0OOOO0O0O ,OOOOOO0O000OO00O0 )#line:458
        for OO0000O00OO0000O0 in OO0OO0O00OOOO00OO :#line:459
            O0O0OOOOOOO0O0OO0 =fetch_messages (O00000OO0OOOO0O0O ,OO0000O00OO0000O0 ,limit =100 )#line:460
            O0OOO0000000OO0O0 =extract_uids_from_messages (O0O0OOOOOOO0O0OO0 )#line:461
            O00O0O000OOO00OOO .update (O0OOO0000000OO0O0 )#line:462
    O00O0O000OOO00OOO =list (set (O00O0O000OOO00OOO )-set (O000OOO0O0OO0OO00 ))#line:465
    for _OO000OO000OOO00OO in range (O0O0000O0OOO0O00O ):#line:467
        for O00000OO0OOOO0O0O in O0OOOOOOOOOOOOO0O :#line:468
            if O0OO0O000O0OOO000 :#line:469
                OO0OO0O00OOOO00OO =O0OO0O000O0OOO000 #line:470
            for OO0000O00OO0000O0 in OO0OO0O00OOOO00OO :#line:471
                send_message_with_mention (O00000OO0OOOO0O0O ,OO0000O00OO0000O0 ,OO0O00OOO0OOOOOO0 ,O00O0O000OOO00OOO )#line:472
                time .sleep (OOOOOOOO0OO0O0O00 )#line:473
def join_discord_invite ():#line:478
    try :#line:479
        with open ("token.txt")as O00O0OOOO00OO0O00 :#line:480
            OOO0OO0O0O00O0OO0 =[OOO00OOO0000OO0O0 .strip ()for OOO00OOO0000OO0O0 in O00O0OOOO00OO0O00 .readlines ()if OOO00OOO0000OO0O0 .strip ()]#line:481
    except (FileNotFoundError ,KeyError ):#line:482
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:483
        return #line:484
    OOOOO0OOO0OOO0OO0 =input ("Invite Code?: discord.gg/").strip ()#line:486
    for OO0OOO0O0OOOOO0O0 in OOO0OO0O0O00O0OO0 :#line:489
        joiner (OO0OOO0O0OOOOO0O0 ,OOOOO0OOO0OOO0OO0 )#line:490
import json ,time ,base64 ,random ,requests #line:492
def cookieset (OO0O00000OOO0OOO0 ):#line:494
    O00O000O00000O00O =OO0O00000OOO0OOO0 .get ("https://discord.com/app")#line:495
    return O00O000O00000O00O .cookies .get_dict ()#line:496
def generatexspandua (OOOO000O0O0O0OO00 ):#line:498
    O00O0OO0O00O00OOO =["Android","Windows","Macintosh"]#line:499
    O0OO00000OO00OOOO =random .choice (O00O0OO0O00O00OOO )#line:500
    if O0OO00000OO00OOOO =="Macintosh":#line:501
        OO0OOOOOOOOO0OOOO =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:502
        O00O0O00OOOOO00O0 ="Macintosh; Intel Mac OS X "+OO0OOOOOOOOO0OOOO #line:503
        O000O0OO00O0000O0 ="x86_64"#line:504
    elif O0OO00000OO00OOOO =="Windows":#line:505
        OO0OOOOOOOOO0OOOO =f'{random.choice([6.0, 10.0, 11.0])}'#line:506
        O00O0O00OOOOO00O0 ="Windows NT "+OO0OOOOOOOOO0OOOO +" Win64; x64"#line:507
        O000O0OO00O0000O0 ="x86_64"#line:508
    else :#line:509
        OO0OOOOOOOOO0OOOO ="13"#line:510
        O00O0O00OOOOO00O0 =f"Linux; Android 13; Pixel 6a"#line:511
        O000O0OO00O0000O0 ="aarch64"#line:512
    O0O00O000000O0OO0 ={"os":O0OO00000OO00OOOO ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":OO0OOOOOOOOO0OOOO ,"os_arch":O000O0OO00O0000O0 ,"system_locale":"ja-JP","client_build_number":OOOO000O0O0O0OO00 ,"client_event_source":None ,"design_id":0 }#line:525
    OO0OO0OO0O00OO0OO =f"Mozilla/5.0 ({O00O0O00OOOOO00O0}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:526
    return base64 .b64encode (json .dumps (O0O00O000000O0OO0 ,separators =(',',':')).encode ()).decode (),OO0OO0OO0O00OO0OO #line:527
def joiner (O0OO0OOOOO0O0O00O ,OO0OO0O0OO0OO0OOO ,O0O000O00OO0O0OOO ,OO0OOO0O0OO0000O0 ):#line:529
  O0O000O0OOO0OOO0O =get_session (O0O000O00OO0O0OOO )#line:530
  O00OOOOOO0OO00OOO =cookieset (O0O000O0OOO0OOO0O )#line:531
  O00OOOOOO0OO00OOO ["locale"]="ja-JP"#line:532
  O00OOO0OO0000O000 =201211 #line:533
  OO0OOO000O00O00OO ,OOO0O0OOOOO00000O =generatexspandua (O00OOO0OO0000O000 )#line:534
  OOOO00OOOOOO0000O ={"Authorization":O0OO0OOOOO0O0O00O ,"accept":"*/*","accept-language":"ja-JP","connection":"keep-alive","DNT":"1","origin":"https://discord.com","sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","referer":"https://discord.com/channels/@me","TE":"Trailers","user-agent":OOO0O0OOOOO00000O ,"X-Super-Properties":OO0OOO000O00O00OO ,}#line:549
  OO0O00OOO0OOO00OO =O0O000O0OOO0OOO0O .post ("https://discord.com/api/v9/invites/"+OO0OO0O0OO0OO0OOO ,headers =OOOO00OOOOOO0000O ,json ={},cookies =O00OOOOOO0OO00OOO )#line:551
  if OO0O00OOO0OOO00OO .status_code ==200 :#line:552
    print ("[+] Probably joined "+O0OO0OOOOO0O0O00O )#line:553
    if "show_verification_form"in OO0O00OOO0OOO00OO .json ():#line:554
      bypass (O0OO0OOOOO0O0O00O ,OO0O00OOO0OOO00OO .json ()["guild"]["id"],O0O000O0OOO0OOO0O ,OOOO00OOOOOO0000O )#line:555
    return #line:556
  elif "captcha_key"in OO0O00OOO0OOO00OO .text and OO0O00OOO0OOO00OO .status_code ==400 :#line:557
    print ("[!] Hcaptcha interference "+O0OO0OOOOO0O0O00O )#line:558
    return #line:559
  elif OO0O00OOO0OOO00OO .status_code ==401 :#line:560
    print ("[!] Token is dead "+O0OO0OOOOO0O0O00O )#line:561
    return #line:562
  elif OO0O00OOO0OOO00OO .status_code ==403 :#line:563
    if "message"in OO0O00OOO0OOO00OO .json ():#line:564
      if OO0O00OOO0OOO00OO .json ()["message"]=="Unknown Message":#line:565
        print ("[!] Unknown error "+O0OO0OOOOO0O0O00O )#line:566
        return #line:567
      else :#line:568
        print ("[!] Verification required "+O0OO0OOOOO0O0O00O )#line:569
        return #line:570
    else :#line:571
      print ("[!] Error occurred "+O0OO0OOOOO0O0O00O )#line:572
      return #line:573
  elif OO0O00OOO0OOO00OO .status_code ==429 :#line:574
    print ("[!] Token rate-limited "+O0OO0OOOOO0O0O00O )#line:575
    return #line:576
  elif OO0O00OOO0OOO00OO .status_code ==400 :#line:577
    if "captcha_key"in OO0O00OOO0OOO00OO .json ():#line:578
      print ("[!] Hcaptcha interference "+O0OO0OOOOO0O0O00O )#line:579
      return #line:580
    else :#line:581
      print ("[!] Error occurred "+O0OO0OOOOO0O0O00O )#line:582
      return #line:583
  elif OO0O00OOO0OOO00OO .status_code ==401 :#line:584
    print ("[!] Token is dead "+O0OO0OOOOO0O0O00O )#line:585
    return #line:586
  elif OO0O00OOO0OOO00OO .status_code ==403 :#line:587
    if "message"in OO0O00OOO0OOO00OO .json ():#line:588
      if OO0O00OOO0OOO00OO .json ()["message"]=="Unknown Message":#line:589
        print ("[!] Unknown error "+O0OO0OOOOO0O0O00O )#line:590
        return #line:591
      else :#line:592
        print ("[!] Verification required "+O0OO0OOOOO0O0O00O )#line:593
        return #line:594
    else :#line:595
      print ("[!] Error occurred "+O0OO0OOOOO0O0O00O )#line:596
  elif OO0O00OOO0OOO00OO .status_code ==429 :#line:597
    print ("[!] Token rate-limited "+O0OO0OOOOO0O0O00O )#line:598
    return #line:599
  else :#line:600
    print ("[!] Error occurred "+O0OO0OOOOO0O0O00O )#line:601
    return #line:602
def update_group_ids ():#line:605
    O00O00OOOO0OO00O0 =input ("Invite Code?: ").strip ()#line:606
    try :#line:607
        with open ("token.txt")as OO0O0OO0O0000OO00 :#line:608
            O00000000OO00OOO0 =[OO0O0OO00O0OOO0O0 .strip ()for OO0O0OO00O0OOO0O0 in OO0O0OO0O0000OO00 .readlines ()if OO0O0OO00O0OOO0O0 .strip ()]#line:609
    except (FileNotFoundError ,KeyError ):#line:610
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:611
        return #line:612
    OO00O00OOOO0OOO00 =requests .Session ()#line:614
    for O0OOOOO00OOOO00OO in O00000000OO00OOO0 :#line:615
        joiner (O0OOOOO00OOOO00OO ,O00O00OOOO0OO00O0 ,OO00O00OOOO0OOO00 )#line:616
        time .sleep (2 )#line:617
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:619
def bypass (OO0OO000O0OOO0O0O ,O0OO0OO0OOOOO0OO0 ,O0000O0O000O0OOOO ,OOOOO000OOO00O00O ):#line:622
    try :#line:623
        OOOOO0O0OO0O0O000 =O0000O0O000O0OOOO .get (f"https://discord.com/api/v9/guilds/{O0OO0OO0OOOOO0OO0}/member-verification?with_guild=false",headers =OOOOO000OOO00O00O ).json ()#line:624
        OOO0000OOO0OOOO00 =O0000O0O000O0OOOO .put (f"https://discord.com/api/v9/guilds/{O0OO0OO0OOOOO0OO0}/requests/@me",headers =OOOOO000OOO00O00O ,json =OOOOO0O0OO0O0O000 )#line:625
        if OOO0000OOO0OOOO00 .status_code ==201 :#line:626
            print (f"[+] MemberscreeningBypassed {OO0OO000O0OOO0O0O}")#line:627
            return #line:628
        else :#line:629
            print (f"[!] Bypassが出来ませんでした {OO0OO000O0OOO0O0O}")#line:630
            return #line:631
    except Exception as OOOO0O00O0O00O00O :#line:632
        print (f"[!] エラーが発生しました。{OOOO0O00O0O00O00O}")#line:633
session =requests .Session ()#line:635
def reactionput (OO0OO00O0OOOOOOOO ,OOOOO00O000O0O0OO ,O0OO0OO000000O0OO ,O000O0O0OOOO000OO ,proxy =None ):#line:638
    O0OOOO000O000O0O0 =get_session (proxy )#line:639
    OOOO000O0000OO0OO =get_headers (O0OOOO000O000O0O0 )#line:640
    OOOO000O0000OO0OO ["Authorization"]=OO0OO00O0OOOOOOOO #line:641
    O000O0O0OOOO000OO =requests .utils .quote (O000O0O0OOOO000OO )#line:643
    O00OOO00O0OO0OO00 =O0OOOO000O000O0O0 .put (f"https://discord.com/api/v9/channels/{OOOOO00O000O0O0OO}/messages/{O0OO0OO000000O0OO}/reactions/{O000O0O0OOOO000OO}/%40me?location=Message&type=0",headers =OOOO000O0000OO0OO )#line:647
    if O00OOO00O0OO0OO00 .status_code in [200 ,204 ]:#line:648
        print (f"[+] Reaction '{O000O0O0OOOO000OO}' added successfully to message {O0OO0OO000000O0OO}")#line:649
    elif O00OOO00O0OO0OO00 .status_code ==429 :#line:650
        print ("[-] Rate limited. Please wait before retrying.")#line:651
        O0O0OOO0O00000000 =O00OOO00O0OO0OO00 .json ().get ("retry_after",1 )#line:652
        time .sleep (O0O0OOO0O00000000 )#line:653
    elif O00OOO00O0OO0OO00 .status_code ==401 :#line:654
        print ("[-] Invalid or expired token.")#line:655
    else :#line:656
        print (f"[!] Error occurred: {O00OOO00O0OO0OO00.status_code}")#line:657
def generatexspandua (O0000000O0000O000 ):#line:660
  OO0000OO0OO0O0O00 =["Android","Windows","Macintosh"]#line:661
  OO0OOOO0000OOO00O =random .choice (OO0000OO0OO0O0O00 )#line:662
  if OO0OOOO0000OOO00O =="Macintosh":#line:663
    OOOOO00O000OOO0O0 =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:664
    O0O0OO0000O000OO0 ="Macintosh; Intel Mac OS X "+OOOOO00O000OOO0O0 #line:665
    OOO00OO0O00O0O0O0 ="x86_64"#line:666
  if OO0OOOO0000OOO00O =="Windows":#line:667
    OOOOO00O000OOO0O0 =f'{random.choice([6.0,10.0,11.0])}'#line:668
    O0O0OO0000O000OO0 ="Windows NT "+OOOOO00O000OOO0O0 +" Win64; x64"#line:669
    OOO00OO0O00O0O0O0 ="x86_64"#line:670
  if OO0OOOO0000OOO00O =="Android":#line:671
    OOOOO00O000OOO0O0 ="13"#line:672
    O0O0OO0000O000OO0 =f"Linux; Android 13; Pixel 6a"#line:673
    OOO00OO0O00O0O0O0 ="aarch64"#line:674
  OO000OO000OOOO00O ={"os":OO0OOOO0000OOO00O ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":OOOOO00O000OOO0O0 ,"os_arch":OOO00OO0O00O0O0O0 ,"system_locale":"ja-JP","client_build_number":O0000000O0000O000 ,"client_event_source":None ,"design_id":0 }#line:675
  OOO0OOOO0O0OO00O0 =f"Mozilla/5.0 ({O0O0OO0000O000OO0}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:676
  return base64 .b64encode (json .dumps (OO000OO000OOOO00O ,separators =(',',':')).encode ()).decode (),OOO0OOOO0O0OO00O0 #line:677
import base64 #line:679
def nickchanger ():#line:682
    try :#line:683
        with open ("token.txt")as OOOO0O00O000O00O0 :#line:684
            O00OO000O0OO00000 =[O00OO000O00000O0O .strip ()for O00OO000O00000O0O in OOOO0O00O000O00O0 .readlines ()if O00OO000O00000O0O .strip ()]#line:685
    except (FileNotFoundError ,KeyError ):#line:686
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:687
        return #line:688
    OOO000000O00O00O0 =input ("Server ID?: ").strip ()#line:690
    O0000OOO0OO0O0OOO =input ("Nickname?: ").strip ()#line:691
    O0OO00000O0OO000O =input ("Delay (in seconds)?: ").strip ()#line:692
    try :#line:694
        O0OO00000O0OO000O =float (O0OO00000O0OO000O )#line:695
        if O0OO00000O0OO000O <0 :#line:696
            raise ValueError #line:697
    except ValueError :#line:698
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:699
        O0OO00000O0OO000O =1.0 #line:700
    for O00OO0O0O0OO0O0OO in O00OO000O0OO00000 :#line:702
        OOO00O0O000OO0O00 ={"Authorization":O00OO0O0O0OO0O0OO ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:707
        OO0000O0OOOOOO0O0 ={"nick":O0000OOO0OO0O0OOO }#line:708
        O00000OOO0O0O0O00 =requests .patch (f"https://discord.com/api/v9/guilds/{OOO000000O00O00O0}/members/@me",headers =OOO00O0O000OO0O00 ,json =OO0000O0OOOOOO0O0 )#line:709
        if O00000OOO0O0O0O00 .status_code ==200 :#line:711
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Nickname changed to '{O0000OOO0OO0O0OOO}' successfully for token {O00OO0O0O0OO0O0OO}.{colorama.Fore.RESET}")#line:712
        elif O00000OOO0O0O0O00 .status_code ==429 :#line:713
            print (f"{colorama.Fore.RED}    [!] Rate limited. Please wait before retrying for token {O00OO0O0O0OO0O0OO}.{colorama.Fore.RESET}")#line:714
            O000O00OO0OOOOOO0 =O00000OOO0O0O0O00 .json ().get ("retry_after",1 )#line:715
            time .sleep (O000O00OO0OOOOOO0 )#line:716
        else :#line:717
            print (f"{colorama.Fore.RED}    [!] Error occurred: {O00000OOO0O0O0O00.status_code} for token {O00OO0O0O0OO0O0OO}.{colorama.Fore.RESET}")#line:718
        time .sleep (O0OO00000O0OO000O )#line:720
import json ,websocket ,threading ,tls_client ,random ,time #line:724
session =tls_client .Session (client_identifier ="chrome112",random_tls_extension_order =True )#line:726
class Utils :#line:728
    @staticmethod #line:729
    def rangeCorrector (O0O0OOO00O000000O ):#line:730
        if [0 ,99 ]not in O0O0OOO00O000000O :#line:731
            O0O0OOO00O000000O .insert (0 ,[0 ,99 ])#line:732
        return O0O0OOO00O000000O #line:733
    @staticmethod #line:735
    def getRanges (O00OO000OO00OOOO0 ,O000OOO00OO00O0OO ,O000OO0OOOO0O00OO ):#line:736
        O000O000O0O000OO0 =int (O00OO000OO00OOOO0 *O000OOO00OO00O0OO )#line:737
        O000OOOO000O00OOO =[[O000O000O0O000OO0 ,O000O000O0O000OO0 +99 ]]#line:738
        if O000OO0OOOO0O00OO >O000O000O0O000OO0 +99 :#line:739
            O000OOOO000O00OOO .append ([O000O000O0O000OO0 +100 ,O000O000O0O000OO0 +199 ])#line:740
        return Utils .rangeCorrector (O000OOOO000O00OOO )#line:741
    @staticmethod #line:743
    def parseGuildMemberListUpdate (OOOOOO00O0OO00O00 ):#line:744
        O00OO00OO0O0OOO0O ={"online_count":OOOOOO00O0OO00O00 ["d"]["online_count"],"member_count":OOOOOO00O0OO00O00 ["d"]["member_count"],"id":OOOOOO00O0OO00O00 ["d"]["id"],"guild_id":OOOOOO00O0OO00O00 ["d"]["guild_id"],"hoisted_roles":OOOOOO00O0OO00O00 ["d"]["groups"],"types":[],"locations":[],"updates":[],}#line:754
        for OO000O00O00OO00O0 in OOOOOO00O0OO00O00 ["d"]["ops"]:#line:756
            O00OO00OO0O0OOO0O ["types"].append (OO000O00O00OO00O0 ["op"])#line:757
            if OO000O00O00OO00O0 ["op"]in ("SYNC","INVALIDATE"):#line:758
                O00OO00OO0O0OOO0O ["locations"].append (OO000O00O00OO00O0 ["range"])#line:759
                if OO000O00O00OO00O0 ["op"]=="SYNC":#line:760
                    O00OO00OO0O0OOO0O ["updates"].append (OO000O00O00OO00O0 ["items"])#line:761
                else :#line:762
                    O00OO00OO0O0OOO0O ["updates"].append ([])#line:763
            elif OO000O00O00OO00O0 ["op"]in ("INSERT","UPDATE","DELETE"):#line:764
                O00OO00OO0O0OOO0O ["locations"].append (OO000O00O00OO00O0 ["index"])#line:765
                if OO000O00O00OO00O0 ["op"]=="DELETE":#line:766
                    O00OO00OO0O0OOO0O ["updates"].append ([])#line:767
                else :#line:768
                    O00OO00OO0O0OOO0O ["updates"].append (OO000O00O00OO00O0 ["item"])#line:769
        return O00OO00OO0O0OOO0O #line:770
class DiscordSocket (websocket .WebSocketApp ):#line:772
    def __init__ (OO000OOO0OOO00000 ,OO0OO0OOOOOOOOO0O ,O0O0OOOOOOOO0OOO0 ,O0OO000OOOO00O0O0 ):#line:773
        OO000OOO0OOO00000 .token =OO0OO0OOOOOOOOO0O #line:774
        OO000OOO0OOO00000 .guild_id =O0O0OOOOOOOO0OOO0 #line:775
        OO000OOO0OOO00000 .channel_id =O0OO000OOOO00O0O0 #line:776
        OO000OOO0OOO00000 .socket_headers ={"Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","Cache-Control":"no-cache","Pragma":"no-cache","Sec-WebSocket-Extensions":"permessage-deflate; client_max_window_bits","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",}#line:784
        super ().__init__ ("wss://gateway.discord.gg/?encoding=json&v=9",header =OO000OOO0OOO00000 .socket_headers ,on_open =lambda OOOO0OO0O00OOO00O :OO000OOO0OOO00000 .sock_open (OOOO0OO0O00OOO00O ),on_message =lambda O000000000O00OOO0 ,OO0000O00O0O0OO0O :OO000OOO0OOO00000 .sock_message (O000000000O00OOO0 ,OO0000O00O0O0OO0O ),on_close =lambda O0OOO0OOO0OO00000 ,O000O0OO00000OO00 ,O0OO0O0OO0O0OOO00 :OO000OOO0OOO00000 .sock_close (O0OOO0OOO0OO00000 ,O000O0OO00000OO00 ,O0OO0O0OO0O0OOO00 ),)#line:793
        OO000OOO0OOO00000 .endScraping =False #line:795
        OO000OOO0OOO00000 .guilds ={}#line:796
        OO000OOO0OOO00000 .members ={}#line:797
        OO000OOO0OOO00000 .ranges =[[0 ,0 ]]#line:798
        OO000OOO0OOO00000 .lastRange =0 #line:799
        OO000OOO0OOO00000 .packets_recv =0 #line:800
    def run (OOO000O000000O0OO ):#line:802
        OOO000O000000O0OO .run_forever ()#line:803
        return OOO000O000000O0OO .members #line:804
    def scrapeUsers (OO0O0O00OOO0OO0O0 ):#line:806
        if not OO0O0O00OOO0OO0O0 .endScraping :#line:807
            OO0O0O00OOO0OO0O0 .send ('{"op":14,"d":{"guild_id":"'+OO0O0O00OOO0OO0O0 .guild_id +'","typing":true,"activities":true,"threads":true,"channels":{"'+OO0O0O00OOO0OO0O0 .channel_id +'":'+json .dumps (OO0O0O00OOO0OO0O0 .ranges )+"}}}")#line:816
    def sock_open (OO00000O0OO0OO0O0 ,OOOO00O0000O0O000 ):#line:818
        OO00000O0OO0OO0O0 .send ('{"op":2,"d":{"token":"'+OO00000O0OO0OO0O0 .token +'","capabilities":125,"properties":{"os":"Windows NT","browser":"Chrome","device":"","system_locale":"it-IT","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36","browser_version":"119.0","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":103981,"client_event_source":null},"presence":{"status":"online","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}')#line:823
    def heartbeatThread (OOO0O0OO000O00OO0 ,O0000OOO0OOOO0OO0 ):#line:825
        try :#line:826
            while True :#line:827
                OOO0O0OO000O00OO0 .send ('{"op":1,"d":'+str (OOO0O0OO000O00OO0 .packets_recv )+"}")#line:828
                time .sleep (O0000OOO0OOOO0OO0 )#line:829
        except Exception as O00O000OO0OO0O0O0 :#line:830
            pass #line:831
    def sock_message (O0O0O0O0O000O000O ,O00OOOOO0000OO0O0 ,OO0OOOO0O00OO0O00 ):#line:833
        OOO0O0O000000O00O =json .loads (OO0OOOO0O00OO0O00 )#line:834
        if OOO0O0O000000O00O is None :#line:835
            return #line:836
        if OOO0O0O000000O00O ["op"]!=11 :#line:837
            O0O0O0O0O000O000O .packets_recv +=1 #line:838
        if OOO0O0O000000O00O ["op"]==10 :#line:839
            threading .Thread (target =O0O0O0O0O000O000O .heartbeatThread ,args =(OOO0O0O000000O00O ["d"]["heartbeat_interval"]/1000 ,),daemon =True ,).start ()#line:844
        if OOO0O0O000000O00O ["t"]=="READY":#line:845
            for O0O0O0O0000O000O0 in OOO0O0O000000O00O ["d"]["guilds"]:#line:846
                O0O0O0O0O000O000O .guilds [O0O0O0O0000O000O0 ["id"]]={"member_count":O0O0O0O0000O000O0 ["member_count"]}#line:847
        if OOO0O0O000000O00O ["t"]=="READY_SUPPLEMENTAL":#line:848
            O0O0O0O0O000O000O .ranges =Utils .getRanges (0 ,100 ,O0O0O0O0O000O000O .guilds [O0O0O0O0O000O000O .guild_id ]["member_count"])#line:851
            O0O0O0O0O000O000O .scrapeUsers ()#line:852
        elif OOO0O0O000000O00O ["t"]=="GUILD_MEMBER_LIST_UPDATE":#line:853
            OOO0000O00O0OOOOO =Utils .parseGuildMemberListUpdate (OOO0O0O000000O00O )#line:854
            if OOO0000O00O0OOOOO ["guild_id"]==O0O0O0O0O000O000O .guild_id and ("SYNC"in OOO0000O00O0OOOOO ["types"]or "UPDATE"in OOO0000O00O0OOOOO ["types"]):#line:858
                for OO00O00O000OO0OOO ,OOOOO000000O000O0 in enumerate (OOO0000O00O0OOOOO ["types"]):#line:859
                    if OOOOO000000O000O0 =="SYNC":#line:860
                        if len (OOO0000O00O0OOOOO ["updates"][OO00O00O000OO0OOO ])==0 :#line:861
                            O0O0O0O0O000O000O .endScraping =True #line:862
                            break #line:863
                        for O000O000000000OO0 in OOO0000O00O0OOOOO ["updates"][OO00O00O000OO0OOO ]:#line:865
                            if "member"in O000O000000000OO0 :#line:866
                                OOO0OOO00O00O00O0 =O000O000000000OO0 ["member"]#line:867
                                O0O00O0OO000O00O0 ={"tag":OOO0OOO00O00O00O0 ["user"]["username"]+"#"+OOO0OOO00O00O00O0 ["user"]["discriminator"],"id":OOO0OOO00O00O00O0 ["user"]["id"],}#line:873
                                if not OOO0OOO00O00O00O0 ["user"].get ("bot"):#line:874
                                    O0O0O0O0O000O000O .members [OOO0OOO00O00O00O0 ["user"]["id"]]=O0O00O0OO000O00O0 #line:875
                    elif OOOOO000000O000O0 =="UPDATE":#line:877
                        for O000O000000000OO0 in OOO0000O00O0OOOOO ["updates"][OO00O00O000OO0OOO ]:#line:878
                            if "member"in O000O000000000OO0 :#line:879
                                OOO0OOO00O00O00O0 =O000O000000000OO0 ["member"]#line:880
                                O0O00O0OO000O00O0 ={"tag":OOO0OOO00O00O00O0 ["user"]["username"]+"#"+OOO0OOO00O00O00O0 ["user"]["discriminator"],"id":OOO0OOO00O00O00O0 ["user"]["id"],}#line:886
                                if not OOO0OOO00O00O00O0 ["user"].get ("bot"):#line:887
                                    O0O0O0O0O000O000O .members [OOO0OOO00O00O00O0 ["user"]["id"]]=O0O00O0OO000O00O0 #line:888
                    O0O0O0O0O000O000O .lastRange +=1 #line:890
                    O0O0O0O0O000O000O .ranges =Utils .getRanges (O0O0O0O0O000O000O .lastRange ,100 ,O0O0O0O0O000O000O .guilds [O0O0O0O0O000O000O .guild_id ]["member_count"])#line:893
                    time .sleep (0.45 )#line:894
                    O0O0O0O0O000O000O .scrapeUsers ()#line:895
            if O0O0O0O0O000O000O .endScraping :#line:897
                O0O0O0O0O000O000O .close ()#line:898
    def sock_close (OO00O00O000O0OOOO ,OO0O000OOO00000O0 ,OO00O00O00OO00OOO ,O0000OO0OO0OO0OOO ):#line:900
        pass #line:901
def scrape (O0OOO0000O00O000O ,O00O0O00O0O0OO000 ,OOOO000O0O0O00000 ):#line:903
    OOO0O0O0OO0O0OO00 =DiscordSocket (O0OOO0000O00O000O ,O00O0O00O0O0OO000 ,OOOO000O0O0O00000 )#line:904
    return OOO0O0O0OO0O0OO00 .run ()#line:905
def member_scrape (O0OO000O0OOOOO0OO ,O0OO00O0OO0OOO0O0 ,O0O0OOOO00O0O0OOO ):#line:907
    O0O0O000O0000OO0O =[]#line:908
    for OO00O00OOOO000OO0 in O0OO000O0OOOOO0OO :#line:909
        OOO0O0OO00OO0OOOO ={"Authorization":OO00O00OOOO000OO0 ,"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}#line:910
        OOOO0OO00O000OO00 =session .get (f"https://canary.discord.com/api/v9/guilds/{O0OO00O0OO0OOO0O0}",headers =OOO0O0OO00OO0OOOO )#line:911
        if OOOO0OO00O000OO00 .status_code ==200 :#line:912
            O0O0O000O0000OO0O .append (OO00O00OOOO000OO0 )#line:913
            break #line:914
    if not O0O0O000O0000OO0O :#line:915
        print ("missing access")#line:916
    OO00O00OOOO000OO0 =random .choice (O0O0O000O0000OO0O )#line:918
    OOOOOOOO0OO0OO00O =scrape (OO00O00OOOO000OO0 ,O0OO00O0OO0OOO0O0 ,O0O0OOOO00O0O0OOO )#line:919
    O000OO0000O000OOO =[f"<@{O000O000O0O0O0OOO}>"for O000O000O0O0O0OOO in [int (OO0000OOOOOOO0000 )for OO0000OOOOOOO0000 in OOOOOOOO0OO0OO00O .keys ()]]#line:920
    print (f"[SUCCESS] {len(O000OO0000O000OOO)} scraped members")#line:921
    return O000OO0000O000OOO #line:922
def spammer_menu ():#line:924
    try :#line:925
        with open ("token.txt")as OOO0OOO0O0O0OO0OO :#line:926
            O0OOO0000O0OO000O =[OOOO0OO00O00OO0O0 .strip ()for OOOO0OO00O00OO0O0 in OOO0OOO0O0O0OO0OO .readlines ()if OOOO0OO00O00OO0O0 .strip ()]#line:927
    except (FileNotFoundError ,KeyError ):#line:928
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:929
        return #line:930
    O0OOO0000O000O000 =input ("Server ID?: ").strip ()#line:932
    O00000O0OOOOOOOOO =input ("Message?: ").strip ()#line:933
    OO00OO0O00000O000 =input ("Random mention (True/False)?: ").strip ().lower ()=='true'#line:934
    OO00OO0O00O0000OO =input ("Delay between messages (in seconds)?: ").strip ()#line:935
    O00O00000OO0000O0 =input ("Number of messages to send?: ").strip ()#line:936
    OO0O00OOO0000OO0O =input ("Blacklist User IDs (comma-separated) (Leave blank to skip)?: ").strip ().split (',')#line:937
    OO0O00OOO0000OO0O =[f"<@{O0O0O0O00O00OO00O.strip()}>"for O0O0O0O00O00OO00O in OO0O00OOO0000OO0O if O0O0O0O00O00OO00O .strip ()]#line:938
    try :#line:940
        OO00OO0O00O0000OO =float (OO00OO0O00O0000OO )#line:941
        if OO00OO0O00O0000OO <0 :#line:942
            raise ValueError #line:943
    except ValueError :#line:944
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:945
        OO00OO0O00O0000OO =1.0 #line:946
    try :#line:948
        O00O00000OO0000O0 =int (O00O00000OO0000O0 )#line:949
        if O00O00000OO0000O0 <=0 :#line:950
            raise ValueError #line:951
    except ValueError :#line:952
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:953
        O00O00000OO0000O0 =1 #line:954
    O0OO0O0O0OO0O00O0 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:956
    if O0OO0O0O0OO0O00O0 =='2':#line:957
        O00O00OO0O0000O00 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:958
        O00O00OO0O0000O00 =[OO0OO0OO0000OOO00 .strip ()for OO0OO0OO0000OOO00 in O00O00OO0O0000O00 if OO0OO0OO0000OOO00 .strip ()]#line:959
    else :#line:960
        O00O00OO0O0000O00 =fetch_channels (O0OOO0000O0OO000O [0 ],O0OOO0000O000O000 )#line:961
    OOOO000OO0OO000O0 =None #line:963
    spammer (O0OOO0000O0OO000O ,O0OOO0000O000O000 ,O00O00OO0O0000O00 ,O00000O0OOOOOOOOO ,OO00OO0O00000O000 ,OO0O00OOO0000OO0O ,OOOO000OO0OO000O0 ,O00O00000OO0000O0 )#line:965
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:967
import discum #line:969
import random #line:970
import time #line:971
def userget (O0OOOO0O00000O000 ,O0OO00O0OOO0OOO0O ,O00O0OO00OOOOO00O ):#line:973
    OOO0OOO0O00000000 =[]#line:974
    OOO0O0OOO0000O0O0 =discum .Client (token =O0OOOO0O00000O000 ,log =False )#line:975
    try :#line:976
        OOO0O0OOO0000O0O0 .gateway .close ()#line:977
    except :#line:978
        print ("Err")#line:979
    def O0O0OO00OO000O000 (O000OOO000O0O0OO0 ,O0O00O00000OO00OO ):#line:981
        if OOO0O0OOO0000O0O0 .gateway .finishedMemberFetching (O0O00O00000OO00OO ):#line:982
            OOOO000OO0O0OOOOO =len (OOO0O0OOO0000O0O0 .gateway .session .guild (O0O00O00000OO00OO ).members )#line:983
            print (str (OOOO000OO0O0OOOOO )+' members fetched')#line:984
            OOO0O0OOO0000O0O0 .gateway .removeCommand ({'function':O0O0OO00OO000O000 ,'params':{'guild_id':O0O00O00000OO00OO }})#line:985
            OOO0O0OOO0000O0O0 .gateway .close ()#line:986
    def OOO0OOO0OO00OOOOO (O00OOOO000OOO00O0 ,O00OOOO0OOOOO00OO ):#line:988
        OOO0O0OOO0000O0O0 .gateway .fetchMembers (O00OOOO000OOO00O0 ,O00OOOO0OOOOO00OO ,keep ='all',wait =1 )#line:989
        OOO0O0OOO0000O0O0 .gateway .command ({'function':O0O0OO00OO000O000 ,'params':{'guild_id':O00OOOO000OOO00O0 }})#line:990
        OOO0O0OOO0000O0O0 .gateway .run ()#line:991
        OOO0O0OOO0000O0O0 .gateway .resetSession ()#line:992
        return OOO0O0OOO0000O0O0 .gateway .session .guild (O00OOOO000OOO00O0 ).members #line:993
    O0O00O000000OO00O =OOO0OOO0OO00OOOOO (O0OO00O0OOO0OOO0O ,O00O0OO00OOOOO00O )#line:995
    for O00O00O00OOO00OO0 in O0O00O000000OO00O :#line:996
        if O00O00O00OOO00OO0 not in OOO0OOO0O00000000 :#line:997
            OOO0OOO0O00000000 .append (f"<@{O00O00O00OOO00OO0}>")#line:998
    return OOO0OOO0O00000000 #line:999
def spammer (O0O000OO0OOO0OO00 ,O0O0000O00OO00000 ,O000000OO00O0O00O ,O00OO0000O0O0O0O0 ,O00OO000OO0000OOO ,O00OO0O00O0OOO00O ,OOOO0O00OO00OO0OO ,OOOO0OO00O0OO000O ):#line:1003
    O000O0O0OOOOO0OO0 =get_session (OOOO0O00OO00OO0OO )#line:1004
    O0OOO00O00O00O0OO =0 #line:1005
    O0OO0O0000O0OOO00 =userget (O0O000OO0OOO0OO00 [0 ],O0O0000O00OO00000 ,O000000OO00O0O00O [0 ])#line:1007
    O0OO0O0000O0OOO00 =[OO00OOO00OO0OO000 for OO00OOO00OO0OO000 in O0OO0O0000O0OOO00 if OO00OOO00OO0OO000 not in O00OO0O00O0OOO00O ]#line:1010
    for _O000O00O00O0OO0OO in range (OOOO0OO00O0OO000O ):#line:1012
        O0O000O0O00000O00 =O0O000OO0OOO0OO00 [O0OOO00O00O00O0OO ]#line:1013
        OO0O0OO0OO0O00000 =get_headers (O0O000O0O00000O00 )#line:1014
        for OO00OOOOOOOOO00OO in O000000OO00O0O00O :#line:1015
            OOO0000OOOO0OO0OO =O00OO0000O0O0O0O0 #line:1016
            if O00OO000OO0000OOO and O0OO0O0000O0OOO00 :#line:1017
                O00OOO000O000O0O0 =random .choice (O0OO0O0000O0OOO00 )#line:1018
                OOO0000OOOO0OO0OO +=f" {O00OOO000O000O0O0}"#line:1019
            O0O0O000OOOOO00OO =O000O0O0OOOOO0OO0 .post (f"https://discord.com/api/v9/channels/{OO00OOOOOOOOO00OO}/messages",json ={"content":OOO0000OOOO0OO0OO },headers =OO0O0OO0OO0O00000 )#line:1021
            if O0O0O000OOOOO00OO .status_code ==200 :#line:1022
                print (f"200 message sent: {O0O000O0O00000O00}")#line:1023
            elif O0O0O000OOOOO00OO .status_code ==429 :#line:1024
                print (f"429 rate limit: {O0O000O0O00000O00}")#line:1025
                O0OO00O0000OO00OO =O0O0O000OOOOO00OO .json ().get ("retry_after",1 )#line:1026
                time .sleep (O0OO00O0000OO00OO )#line:1027
            elif O0O0O000OOOOO00OO .status_code ==401 :#line:1028
                print (f"401 unknown token: {O0O000O0O00000O00}")#line:1029
            else :#line:1030
                print (f"error: {O0O000O0O00000O00}")#line:1031
        O0OOO00O00O00O0OO =(O0OOO00O00O00O0OO +1 )%len (O0O000OO0OOO0OO00 )#line:1033
        time .sleep (1 )#line:1034
import requests #line:1038
import base64 #line:1039
import colorama #line:1040
import time #line:1041
def add_emojis_from_files ():#line:1043
    try :#line:1044
        with open ("emojiname.txt")as OO0OO00O0O00OOO00 ,open ("emojiurl.txt")as O0O0OOOOO0000O0O0 :#line:1045
            O00OOOO0OOO000OO0 =[O00O00O0000000O0O .strip ()for O00O00O0000000O0O in OO0OO00O0O00OOO00 .read ().split (',')if O00O00O0000000O0O .strip ()]#line:1046
            O00000OOO0OO0OOO0 =[O0O00O00OO0OOO00O .strip ()for O0O00O00OO0OOO00O in O0O0OOOOO0000O0O0 .read ().split (',')if O0O00O00OO0OOO00O .strip ()]#line:1047
    except FileNotFoundError as OO0OOO0O00O00OOO0 :#line:1048
        print (f"{colorama.Fore.RED}    [!] Error: {str(OO0OOO0O00O00OOO0)}{colorama.Fore.RESET}")#line:1049
        return #line:1050
    if len (O00OOOO0OOO000OO0 )!=len (O00000OOO0OO0OOO0 ):#line:1052
        print (f"{colorama.Fore.RED}    [!] Error: The number of emoji names and URLs do not match!{colorama.Fore.RESET}")#line:1053
        return #line:1054
    try :#line:1056
        with open ("token.txt")as O0O0000O0O00OO0O0 :#line:1057
            OOOOO0OO0OO0O0O00 =[OO0OO0OOOO000OO0O .strip ()for OO0OO0OOOO000OO0O in O0O0000O0O00OO0O0 .readlines ()if OO0OO0OOOO000OO0O .strip ()]#line:1058
    except FileNotFoundError as OO0OOO0O00O00OOO0 :#line:1059
        print (f"{colorama.Fore.RED}    [!] Error: {str(OO0OOO0O00O00OOO0)}{colorama.Fore.RESET}")#line:1060
        return #line:1061
    O0O0OO00OO0O00O0O =input ("Enter the Guild ID: ").strip ()#line:1063
    OO0O0O00O0O000OOO =input ("Enter the rate limit between requests (in seconds): ").strip ()#line:1064
    try :#line:1066
        OO0O0O00O0O000OOO =float (OO0O0O00O0O000OOO )#line:1067
        if OO0O0O00O0O000OOO <0 :#line:1068
            raise ValueError #line:1069
    except ValueError :#line:1070
        print (f"{colorama.Fore.RED}    [!] Invalid rate limit. Using default rate limit of 5 seconds.{colorama.Fore.RESET}")#line:1071
        OO0O0O00O0O000OOO =5.0 #line:1072
    O0O0OO000000000OO =set ()#line:1074
    for OOO0O00OO0O00000O in OOOOO0OO0OO0O0O00 :#line:1076
        OOO00OO0000OOOOOO ={'Authorization':OOO0O00OO0O00000O ,'Content-Type':'application/json'}#line:1080
        OOO0OOO0000OOOOO0 =requests .get (f"https://discord.com/api/v9/guilds/{O0O0OO00OO0O00O0O}/emojis",headers =OOO00OO0000OOOOOO )#line:1083
        if OOO0OOO0000OOOOO0 .status_code ==200 :#line:1084
            OOOO000OO00OOO00O =OOO0OOO0000OOOOO0 .json ()#line:1085
            for OOOO0OO00OOOOOOO0 in OOOO000OO00OOO00O :#line:1086
                O0O0OO000000000OO .add (OOOO0OO00OOOOOOO0 ['name'])#line:1087
        else :#line:1088
            print (f"{colorama.Fore.RED}    [!] Error fetching existing emojis: {OOO0OOO0000OOOOO0.status_code} - {OOO0OOO0000OOOOO0.text}{colorama.Fore.RESET}")#line:1089
            continue #line:1090
    for OO0OO0O00OOO0O0O0 ,OO000000O0O000O0O in zip (O00OOOO0OOO000OO0 ,O00000OOO0OO0OOO0 ):#line:1092
        if OO0OO0O00OOO0O0O0 in O0O0OO000000000OO :#line:1093
            print (f"{colorama.Fore.YELLOW}    [*] Emoji '{OO0OO0O00OOO0O0O0}' already exists. Skipping...{colorama.Fore.RESET}")#line:1094
            continue #line:1095
        for OOO0O00OO0O00000O in OOOOO0OO0OO0O0O00 :#line:1097
            try :#line:1098
                OOO0OOO0000OOOOO0 =requests .get (OO000000O0O000O0O )#line:1099
                OOO0OOO0000OOOOO0 .raise_for_status ()#line:1100
                OO000OO0O00OOOO0O =OOO0OOO0000OOOOO0 .content #line:1101
                O00O00000OO00OO0O =base64 .b64encode (OO000OO0O00OOOO0O ).decode ('utf-8')#line:1102
                O00OO000O000O0OOO ={'name':OO0OO0O00OOO0O0O0 ,'image':f"data:image/png;base64,{O00O00000OO00OO0O}"}#line:1107
                OOO00OO0000OOOOOO ={'Authorization':OOO0O00OO0O00000O ,'Content-Type':'application/json'}#line:1112
                OOOO0OOOO00OO0O0O =requests .post (f"https://discord.com/api/v9/guilds/{O0O0OO00OO0O00O0O}/emojis",headers =OOO00OO0000OOOOOO ,json =O00OO000O000O0OOO )#line:1114
                if OOOO0OOOO00OO0O0O .status_code ==201 :#line:1115
                    print (f"{colorama.Fore.GREEN}    [+] Successfully added emoji '{OO0OO0O00OOO0O0O0}' with token {OOO0O00OO0O00000O}{colorama.Fore.RESET}")#line:1116
                    O0O0OO000000000OO .add (OO0OO0O00OOO0O0O0 )#line:1117
                    break #line:1118
                else :#line:1119
                    print (f"{colorama.Fore.RED}    [!] Failed to add emoji '{OO0OO0O00OOO0O0O0}' with token {OOO0O00OO0O00000O}: {OOOO0OOOO00OO0O0O.status_code} - {OOOO0OOOO00OO0O0O.text}{colorama.Fore.RESET}")#line:1120
                time .sleep (OO0O0O00O0O000OOO )#line:1122
            except Exception as OO0OOO0O00O00OOO0 :#line:1123
                print (f"{colorama.Fore.RED}    [!] Error adding emoji '{OO0OO0O00OOO0O0O0}' with token {OOO0O00OO0O00000O}: {str(OO0OOO0O00O00OOO0)}{colorama.Fore.RESET}")#line:1124
def main ():#line:1126
    colorama .init ()#line:1127
    while True :#line:1128
        logo ()#line:1129
        O000OO0OOOO0O00O0 =input (f"{colorama.Fore.LIGHTMAGENTA_EX}    [Final] Select an option from above: ")#line:1130
        if O000OO0OOOO0O00O0 =="0":#line:1132
            update_group_ids ()#line:1133
        elif O000OO0OOOO0O00O0 =="1":#line:1134
            join_discord_invite ()#line:1135
        elif O000OO0OOOO0O00O0 =="2":#line:1136
            reaction_spammer ()#line:1137
        elif O000OO0OOOO0O00O0 =="3":#line:1138
            send_messages_with_mentions ()#line:1139
        elif O000OO0OOOO0O00O0 =="4":#line:1140
            spammer_menu ()#line:1141
        elif O000OO0OOOO0O00O0 =="5":#line:1142
            nickchanger ()#line:1143
        elif O000OO0OOOO0O00O0 =="6":#line:1144
            add_emojis_from_files ()#line:1145
        elif O000OO0OOOO0O00O0 =="7":#line:1146
            reaction_art ()#line:1147
        elif O000OO0OOOO0O00O0 =="0":#line:1148
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [*] Exiting the application. Goodbye!{colorama.Fore.RESET}")#line:1149
            break #line:1150
        else :#line:1151
            print (f"{colorama.Fore.RED}    [!] Invalid option selected!{colorama.Fore.RESET}")#line:1152
        input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:1154
if __name__ =="__main__":#line:1156
    main ()#line:1157
