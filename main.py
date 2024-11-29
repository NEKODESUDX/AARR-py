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
※このツールは開発中の為joinは動作しない可能性があります
    [1] server join
    [2] mass Reaction spammer
    [3] active users only mentions
    [4] all user mentions
    [5] nickname changer
    [6] emoji add
    [7] reaction art
    [8] poll spammer

    [0] exit
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    {colorama.Fore.RESET}
    """)#line:54
def get_session (proxy =None ):#line:57
    OOO0O00O00OO0OOOO =requests .Session ()#line:58
    if proxy :#line:59
        OOO0O00O00OO0OOOO .proxies ={"http":proxy ,"https":proxy }#line:60
    return OOO0O00O00OO0OOOO #line:61
def get_headers (OO0000OOOOOOOO0OO ):#line:63
    return {"Authorization":OO0000OOOOOOOO0OO ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:68
def send_message_with_mention (OO0O0OO0OO00OO00O ,O00OO0000OO00OOO0 ,OOOOO0O0OO0000000 ,O0O0OO0OO0000O000 ):#line:71
    OO000OOO0O00OOOO0 =get_session ()#line:72
    OOO0000OO00O0OO00 =get_headers (OO0O0OO0OO00OO00O )#line:73
    if O0O0OO0OO0000O000 :#line:75
        OOOOO0O00O0O0OO00 =random .choice (O0O0OO0OO0000O000 )#line:76
        OOOOO0O0OO0000000 +=f" <@{OOOOO0O00O0O0OO00}>"#line:77
    O000000000OO0OOOO =OO000OOO0O00OOOO0 .post (f"https://discord.com/api/v9/channels/{O00OO0000OO00OOO0}/messages",headers =OOO0000OO00O0OO00 ,json ={"content":OOOOO0O0OO0000000 })#line:83
    if O000000000OO0OOOO .status_code in [200 ,201 ]:#line:84
        print (f"[+] Message sent to channel {O00OO0000OO00OOO0}")#line:85
    elif O000000000OO0OOOO .status_code ==429 :#line:86
        print ("[-] Rate limited. Please wait before retrying.")#line:87
        O000OO000OOOOO00O =O000000000OO0OOOO .json ().get ("retry_after",1 )#line:88
        time .sleep (O000OO000OOOOO00O )#line:89
    else :#line:90
        print (f"[!] Error occurred: {O000000000OO0OOOO.status_code}")#line:91
def fetch_messages (O0OOO00OOOOO0000O ,O00O0OO0OOO0OOOOO ,limit =100 ):#line:94
    O00O0OOOO0000O0O0 ={"Authorization":O0OOO00OOOOO0000O ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:99
    OO000O00O0O0O0OOO =requests .get (f"https://discord.com/api/v9/channels/{O00O0OO0OOO0OOOOO}/messages?limit={limit}",headers =O00O0OOOO0000O0O0 )#line:103
    if OO000O00O0O0O0OOO .status_code ==200 :#line:104
        return OO000O00O0O0O0OOO .json ()#line:105
    else :#line:106
        print (f"[!] Failed to fetch messages. HTTP Status Code: {OO000O00O0O0O0OOO.status_code}")#line:107
        return []#line:108
import concurrent .futures #line:110
def reaction_spammer ():#line:112
    try :#line:113
        with open ("token.txt")as O0OO0OO0OOO00O0OO :#line:114
            OOOO0OOO00000OO0O =[OO00OOO0O0OOOO000 .strip ()for OO00OOO0O0OOOO000 in O0OO0OO0OOO00O0OO .readlines ()if OO00OOO0O0OOOO000 .strip ()]#line:115
    except (FileNotFoundError ,KeyError ):#line:116
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:117
        return #line:118
    OOOO0O00O0OO0O00O =input ("Server ID?: ").strip ()#line:120
    OO00O00OO00O00OOO =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:122
    if OO00O00OO00O00OOO =='2':#line:123
        OO0OOOO000O0OOOO0 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:124
        O000O000OOO000000 =[O0O0O0O0OO00O00OO .strip ()for O0O0O0O0OO00O00OO in OO0OOOO000O0OOOO0 if O0O0O0O0OO00O00OO .strip ()]#line:125
    else :#line:126
        O000O000OOO000000 =[]#line:127
        for O0O000O0O0O0O000O in OOOO0OOO00000OO0O :#line:128
            try :#line:129
                O000O000OOO000000 .extend (fetch_channels (O0O000O0O0O0O000O ,OOOO0O00O0OO0O00O ))#line:130
            except Exception as O0OO00000000OOOO0 :#line:131
                print (f"[!] Failed to fetch channels for token. Error: {O0OO00000000OOOO0}")#line:132
                continue #line:133
    OO000000000O0O00O =input ("Select your emoji (a, b, c, ... or custom emojis): ").strip ()#line:135
    O0O0O0000O00000O0 =input ("Delay between reactions (in seconds)?: ").strip ()#line:136
    try :#line:138
        O0O0O0000O00000O0 =float (O0O0O0000O00000O0 )#line:139
        if O0O0O0000O00000O0 <0 :#line:140
            raise ValueError #line:141
    except ValueError :#line:142
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:143
        O0O0O0000O00000O0 =1.0 #line:144
    OOOO000OOOOOO0OOO =[]#line:146
    for O00OO00O00O00OOO0 in OO000000000O0O00O .split (","):#line:147
        O00OO00O00O00OOO0 =O00OO00O00O00OOO0 .strip ().lower ()#line:148
        if O00OO00O00O00OOO0 in alphabet_to_flag :#line:149
            OOOO000OOOOOO0OOO .append (alphabet_to_flag [O00OO00O00O00OOO0 ])#line:150
        else :#line:151
            OOOO000OOOOOO0OOO .append (O00OO00O00O00OOO0 )#line:152
    if not OOOO000OOOOOO0OOO :#line:154
        print (f"{colorama.Fore.RED}    [!] No valid emojis provided!{colorama.Fore.RESET}")#line:155
        return #line:156
    def OO0OOO00O0OO0O000 (OO0OOOOO00O0OO0OO ):#line:158
        for OO0O000O0OOO0O000 in O000O000OOO000000 :#line:159
            try :#line:160
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {OO0O000O0OOO0O000}...{colorama.Fore.RESET}")#line:161
                OOO0O00O0OOO00O0O =fetch_messages (OO0OOOOO00O0OO0OO ,OO0O000O0OOO0O000 ,limit =100 )#line:162
                if not OOO0O00O0OOO00O0O :#line:163
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:164
                    continue #line:165
                for O0O0OO00000000OO0 in OOO0O00O0OOO00O0O :#line:167
                    for O00000OO00000000O in OOOO000OOOOOO0OOO :#line:168
                        reactionput (OO0OOOOO00O0OO0OO ,OO0O000O0OOO0O000 ,O0O0OO00000000OO0 ['id'],O00000OO00000000O )#line:169
                        time .sleep (O0O0O0000O00000O0 )#line:170
            except Exception as O000000O0OO000000 :#line:171
                print (f"[!] Error processing channel {OO0O000O0OOO0O000}. Error: {O000000O0OO000000}")#line:172
                continue #line:173
    with concurrent .futures .ThreadPoolExecutor ()as OO0O0OOOOO0O0O0OO :#line:175
        O0000000O00O00OO0 =[OO0O0OOOOO0O0O0OO .submit (OO0OOO00O0OO0O000 ,O0OOOOOO000OO0O00 )for O0OOOOOO000OO0O00 in OOOO0OOO00000OO0O ]#line:176
        concurrent .futures .wait (O0000000O00O00OO0 )#line:177
import requests #line:180
import json #line:181
import time #line:182
import colorama #line:183
alphabet_to_flag ={'a':'🇦','b':'🇧','c':'🇨','d':'🇩','e':'🇪','f':'🇫','g':'🇬','h':'🇭','i':'🇮','j':'🇯','k':'🇰','l':'🇱','m':'🇲','n':'🇳','o':'🇴','p':'🇵','q':'🇶','r':'🇷','s':'🇸','t':'🇹','u':'🇺','v':'🇻','w':'🇼','x':'🇽','y':'🇾','z':'🇿'}#line:191
def fetch_channels (O0OO0O000OOOO0O00 ,OO0OO0000OO000OOO ):#line:193
    OOO0O0O0000O000O0 =f"https://discord.com/api/v9/guilds/{OO0OO0000OO000OOO}/channels"#line:194
    O0O0OO0OO0O000OO0 ={"Authorization":O0OO0O000OOOO0O00 }#line:195
    OOOOO0OOO0O0OOOOO =requests .get (OOO0O0O0000O000O0 ,headers =O0O0OO0OO0O000OO0 )#line:196
    if OOOOO0OOO0O0OOOOO .status_code ==200 :#line:197
        return [OO00000O0OO000O00 ['id']for OO00000O0OO000O00 in OOOOO0OOO0O0OOOOO .json ()if OO00000O0OO000O00 ['type']==0 ]#line:198
    else :#line:199
        raise Exception (f"Failed to fetch channels: {OOOOO0OOO0O0OOOOO.status_code} - {OOOOO0OOO0O0OOOOO.text}")#line:200
def fetch_messages (O0O0000OO0OO00O00 ,O0OO0O0O0OOO0000O ,limit =100 ):#line:202
    OO00O0O00OOOO0OO0 =f"https://discord.com/api/v9/channels/{O0OO0O0O0OOO0000O}/messages?limit={limit}"#line:203
    O00000OO0OO00OO0O ={"Authorization":O0O0000OO0OO00O00 }#line:204
    OOOOO00OO00O0O0OO =requests .get (OO00O0O00OOOO0OO0 ,headers =O00000OO0OO00OO0O )#line:205
    if OOOOO00OO00O0O0OO .status_code ==200 :#line:206
        return OOOOO00OO00O0O0OO .json ()#line:207
    else :#line:208
        print (f"[!] Failed to fetch messages: {OOOOO00OO00O0O0OO.status_code} - {OOOOO00OO00O0O0OO.text}")#line:209
        return []#line:210
def reactionput (OOOO0OOOOOOO00O0O ,O000O0O00OO00O0OO ,O0OOO0OO0O0OOOOOO ,O0OOO0OOOOOO0O0OO ):#line:212
    O0OO0O00OO0O00O00 =f"https://discord.com/api/v9/channels/{O000O0O00OO00O0OO}/messages/{O0OOO0OO0O0OOOOOO}/reactions/{O0OOO0OOOOOO0O0OO}/@me"#line:213
    O000OO0O0O00000O0 ={"Authorization":OOOO0OOOOOOO00O0O ,"Content-Type":"application/json"}#line:214
    O0O0OOO000000OO00 =requests .put (O0OO0O00OO0O00O00 ,headers =O000OO0O0O00000O0 )#line:215
    if O0O0OOO000000OO00 .status_code not in [204 ,200 ]:#line:216
        print (f"{colorama.Fore.RED}    [!] Failed to add reaction: {O0O0OOO000000OO00.status_code} - {O0O0OOO000000OO00.text}{colorama.Fore.RESET}")#line:217
import random #line:219
def reaction_art ():#line:221
    try :#line:222
        with open ("token.txt",encoding ="utf-8")as O0OOOO0OOO00O0000 :#line:223
            OO0O00OO000OOOO00 =[OOO00OOOOOO0O0000 .strip ()for OOO00OOOOOO0O0000 in O0OOOO0OOO00O0000 .readlines ()if OOO00OOOOOO0O0000 .strip ()]#line:224
    except (FileNotFoundError ,KeyError ):#line:225
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:226
        return #line:227
    O0O0O0O0O0OO00OOO =input ("Server ID?: ").strip ()#line:229
    O0O0OOOOOOOO0O0OO =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:231
    if O0O0OOOOOOOO0O0OO =='2':#line:232
        OO0OO0OO00OO00000 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:233
        OOOO00O0OO0OO00OO =[OOOO000OO00O0O0O0 .strip ()for OOOO000OO00O0O0O0 in OO0OO0OO00OO00000 if OOOO000OO00O0O0O0 .strip ()]#line:234
    else :#line:235
        OOOO00O0OO0OO00OO =[]#line:236
        for OOOOO0000000OO0O0 in OO0O00OO000OOOO00 :#line:237
            try :#line:238
                OOOO00O0OO0OO00OO .extend (fetch_channels (OOOOO0000000OO0O0 ,O0O0O0O0O0OO00OOO ))#line:239
            except Exception as OO0O00OOO00OO0000 :#line:240
                print (f"[!] Failed to fetch channels for token. Error: {OO0O00OOO00OO0000}")#line:241
                continue #line:242
        random .shuffle (OOOO00O0OO0OO00OO )#line:243
    O00O0O0OOOOOO0000 =input ("Delay between reactions (in seconds)?: ").strip ()#line:245
    try :#line:247
        O00O0O0OOOOOO0000 =float (O00O0O0OOOOOO0000 )#line:248
        if O00O0O0OOOOOO0000 <0 :#line:249
            raise ValueError #line:250
    except ValueError :#line:251
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:252
        O00O0O0OOOOOO0000 =1.0 #line:253
    try :#line:255
        with open ("art.txt",encoding ="utf-8")as OO00O0O00OOOO0000 :#line:256
            OO000000O0O00O0OO =[O0OO0OO0O0O0O0OO0 .strip ()for O0OO0OO0O0O0O0OO0 in OO00O0O00OOOO0000 .readlines ()if O0OO0OO0O0O0O0OO0 .strip ()]#line:257
    except (FileNotFoundError ,KeyError ):#line:258
        print (f"{colorama.Fore.RED}    [!] Error: art.txt file not found or empty!{colorama.Fore.RESET}")#line:259
        return #line:260
    except UnicodeDecodeError as OO0O00OOO00OO0000 :#line:261
        print (f"{colorama.Fore.RED}    [!] Error decoding art.txt: {str(OO0O00OOO00OO0000)}{colorama.Fore.RESET}")#line:262
        return #line:263
    if not OO000000O0O00O0OO :#line:265
        print (f"{colorama.Fore.RED}    [!] No valid art provided in art.txt!{colorama.Fore.RESET}")#line:266
        return #line:267
    OO000000O0O00O0OO .reverse ()#line:270
    for OOOOO0000000OO0O0 in OO0O00OO000OOOO00 :#line:272
        for OOO0OOO00O0000O0O in OOOO00O0OO0OO00OO :#line:273
            try :#line:274
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {OOO0OOO00O0000O0O}...{colorama.Fore.RESET}")#line:275
                OO000O000OO0OOOO0 =fetch_messages (OOOOO0000000OO0O0 ,OOO0OOO00O0000O0O ,limit =100 )#line:278
                if not OO000O000OO0OOOO0 :#line:279
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:280
                    continue #line:281
                for OOO00OO000000O0OO ,OO0O000O0OO0000OO in enumerate (OO000O000OO0OOOO0 ):#line:284
                    O0O0000O00O000OO0 =OO000000O0O00O0OO [OOO00OO000000O0OO %len (OO000000O0O00O0OO )].split (',')#line:285
                    for O00OO00000OOO0O0O in O0O0000O00O000OO0 :#line:286
                        reactionput (OOOOO0000000OO0O0 ,OOO0OOO00O0000O0O ,OO0O000O0OO0000OO ['id'],O00OO00000OOO0O0O .strip ())#line:287
                        print (f"Adding reaction '{O00OO00000OOO0O0O.strip()}' to message {OO0O000O0OO0000OO['id']} in channel {OOO0OOO00O0000O0O}")#line:288
                        time .sleep (O00O0O0OOOOOO0000 )#line:289
            except Exception as OO0O00OOO00OO0000 :#line:290
                print (f"[!] Error processing channel {OOO0OOO00O0000O0O}. Error: {OO0O00OOO00OO0000}")#line:291
                continue #line:292
    def OO000OO00OOOOO00O (OO00O0OOO0OO00OO0 ):#line:297
        for OOO0OOOO00O0OOO00 in OOOO00O0OO0OO00OO :#line:298
            try :#line:299
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {OOO0OOOO00O0OOO00}...{colorama.Fore.RESET}")#line:300
                O0O0OOOOOOOO00000 =fetch_messages (OO00O0OOO0OO00OO0 ,OOO0OOOO00O0OOO00 ,limit =100 )#line:301
                if not O0O0OOOOOOOO00000 :#line:302
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:303
                    continue #line:304
                for OO000000000O0000O in O0O0OOOOOOOO00000 :#line:306
                    for O00O0O0OOOOOO00O0 in O0O0000O00O000OO0 :#line:307
                        reactionput (OO00O0OOO0OO00OO0 ,OOO0OOOO00O0OOO00 ,OO000000000O0000O ['id'],O00O0O0OOOOOO00O0 )#line:308
                        time .sleep (O00O0O0OOOOOO0000 )#line:309
            except Exception as O0O0O0O0O0O00O0O0 :#line:310
                print (f"[!] Error processing channel {OOO0OOOO00O0OOO00}. Error: {O0O0O0O0O0O00O0O0}")#line:311
                continue #line:312
    with concurrent .futures .ThreadPoolExecutor ()as OOOO00O0O00O0O000 :#line:314
        O0000O00OOO000000 =[OOOO00O0O00O0O000 .submit (OO000OO00OOOOO00O ,OO00OOOO0O00OO0O0 )for OO00OOOO0O00OO0O0 in OO0O00OO000OOOO00 ]#line:315
        concurrent .futures .wait (O0000O00OOO000000 )#line:316
def update_group_ids ():#line:319
    try :#line:320
        with open ("token.txt")as O00O00OO0OOO0O0O0 :#line:321
            OO0O0O0000O000O00 =[OO0O00O0000O00OOO .strip ()for OO0O00O0000O00OOO in O00O00OO0OOO0O0O0 .readlines ()if OO0O00O0000O00OOO .strip ()]#line:322
        OO0000O0O0O00O00O =OO0O0O0000O000O00 [0 ]#line:323
    except (FileNotFoundError ,KeyError ):#line:324
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:325
        return #line:326
    OOO00OO00000OOOOO ={"Authorization":OO0000O0O0O00O00O ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:332
    OO0O0OOO000OOO000 =requests .get ('https://discord.com/api/v9/users/@me/channels',headers =OOO00OO00000OOOOO )#line:334
    if OO0O0OOO000OOO000 .status_code ==200 :#line:335
        OO00OOOO000OO00OO =OO0O0OOO000OOO000 .json ()#line:336
        with open ("group_id.txt","w")as O000O00O0O000O0OO :#line:337
            for O00OOO0OOOOO00OO0 in OO00OOOO000OO00OO :#line:338
                if O00OOO0OOOOO00OO0 ['type']==3 :#line:339
                    O000O00O0O000O0OO .write (O00OOO0OOOOO00OO0 ['id']+'\n')#line:340
        print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Group IDs updated successfully.{colorama.Fore.RESET}")#line:341
    else :#line:342
        print (f"{colorama.Fore.LIGHTRED_EX}    [!] Failed to retrieve group IDs. HTTP Status Code: {OO0O0OOO000OOO000.status_code}{colorama.Fore.RESET}")#line:343
import requests #line:345
import requests #line:347
def fetch_channels (O0000OO00O0O0O00O ,OO000000O0O0O0O0O ):#line:349
    try :#line:350
        O00OO000000OO0000 =requests .Session ()#line:351
        OOOO0O0OO00O0O000 =get_headers (O0000OO00O0O0O00O )#line:352
        OOO00O0O000O0OOOO =O00OO000000OO0000 .get (f"https://discord.com/api/v9/guilds/{OO000000O0O0O0O0O}/channels",headers =OOOO0O0OO00O0O000 ,timeout =10 )#line:359
        if OOO00O0O000O0OOOO .status_code ==200 :#line:362
            try :#line:363
                O0O00O0OOOOOO000O =OOO00O0O000O0OOOO .json ()#line:364
                return [O00OOO0OO0000O00O ['id']for O00OOO0OO0000O00O in O0O00O0OOOOOO000O if O00OOO0OO0000O00O .get ('type')==0 ]#line:365
            except ValueError :#line:366
                print ("[!] Error: Response was not valid JSON.")#line:367
                return []#line:368
        elif OOO00O0O000O0OOOO .status_code ==401 :#line:369
            print ("[!] Error: Unauthorized - check your token.")#line:370
        elif OOO00O0O000O0OOOO .status_code ==403 :#line:371
            print ("[!] Error: Forbidden - you lack permissions.")#line:372
        elif OOO00O0O000O0OOOO .status_code ==404 :#line:373
            print ("[!] Error: Server not found - check the server ID.")#line:374
        else :#line:375
            print (f"[!] Error: Unexpected status code {OOO00O0O000O0OOOO.status_code}.")#line:376
        return []#line:379
    except requests .exceptions .Timeout :#line:381
        print ("[!] Error: Request timed out. Check your connection or try again later.")#line:382
        return []#line:383
    except requests .exceptions .RequestException as O000000OOOO0O0000 :#line:384
        print (f"[!] Error: An error occurred while fetching channels: {O000000OOOO0O0000}")#line:385
        return []#line:386
def extract_uids_from_messages (O00O0000OO00000OO ):#line:392
    O0000O0OOOO000O0O =set ()#line:393
    for OO0OO0OOO0OO00O0O in O00O0000OO00000OO :#line:394
        O0000O0OOOO000O0O .add (OO0OO0OOO0OO00O0O ['author']['id'])#line:395
    return list (O0000O0OOOO000O0O )#line:396
def send_message_with_mention (O000O00000O000O0O ,OO00O00OO0OO00000 ,OO000OOO000O0000O ,OO000O0O00O0OO00O ):#line:398
    OO0O000OO00OOO00O =get_session ()#line:399
    OOOOOO0OOOO0OO0O0 =get_headers (O000O00000O000O0O )#line:400
    if OO000O0O00O0OO00O :#line:402
        OOO00OO000000O0O0 =random .choice (OO000O0O00O0OO00O )#line:403
        OO000OOO000O0000O +=f" <@{OOO00OO000000O0O0}>"#line:404
    O00000OO0OO00O00O =OO0O000OO00OOO00O .post (f"https://discord.com/api/v9/channels/{OO00O00OO0OO00000}/messages",headers =OOOOOO0OOOO0OO0O0 ,json ={"content":OO000OOO000O0000O })#line:410
    if O00000OO0OO00O00O .status_code in [200 ,201 ]:#line:411
        print (f"[+] Message sent to channel {OO00O00OO0OO00000}")#line:412
    elif O00000OO0OO00O00O .status_code ==429 :#line:413
        print ("[-] Rate limited. Please wait before retrying.")#line:414
        OOO0OOOOOO00O0O0O =O00000OO0OO00O00O .json ().get ("retry_after",1 )#line:415
        time .sleep (OOO0OOOOOO00O0O0O )#line:416
    else :#line:417
        print (f"[!] Error occurred: {O00000OO0OO00O00O.status_code}")#line:418
def send_messages_with_mentions ():#line:419
    try :#line:420
        with open ("token.txt")as O000O0000O00O00OO :#line:421
            OO000O00OOO0OOOOO =[OOO0OO0OO0OOO000O .strip ()for OOO0OO0OO0OOO000O in O000O0000O00O00OO .readlines ()if OOO0OO0OO0OOO000O .strip ()]#line:422
    except (FileNotFoundError ,KeyError ):#line:423
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:424
        return #line:425
    O00O000O00OOOOO0O =input ("Server ID?: ").strip ()#line:427
    OO000O0O0O000O000 =input ("Delay between messages (in seconds)?: ").strip ()#line:428
    O000O0OOOO0000OO0 =input ("Number of messages to send?: ").strip ()#line:429
    OO00OOOOO0OO0000O =input ("Message content?: ").strip ()#line:430
    O00OO0O00O000O0OO =input ("Blacklist User IDs (comma-separated)?: ").strip ().split (',')#line:431
    O00OO0O00O000O0OO =[O0O00OO00OO0OO0OO .strip ()for O0O00OO00OO0OO0OO in O00OO0O00O000O0OO if O0O00OO00OO0OO0OO .strip ()]#line:432
    try :#line:434
        OO000O0O0O000O000 =float (OO000O0O0O000O000 )#line:435
        if OO000O0O0O000O000 <0 :#line:436
            raise ValueError #line:437
    except ValueError :#line:438
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:439
        OO000O0O0O000O000 =1.0 #line:440
    try :#line:442
        O000O0OOOO0000OO0 =int (O000O0OOOO0000OO0 )#line:443
        if O000O0OOOO0000OO0 <=0 :#line:444
            raise ValueError #line:445
    except ValueError :#line:446
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:447
        O000O0OOOO0000OO0 =1 #line:448
    OOO0O0O0OOO0OOOOO =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:450
    if OOO0O0O0OOO0OOOOO =='2':#line:451
        OOOOOO00O0OO000O0 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:452
        OOOOOO00O0OO000O0 =[O0OO0000OOO0O0O0O .strip ()for O0OO0000OOO0O0O0O in OOOOOO00O0OO000O0 if O0OO0000OOO0O0O0O .strip ()]#line:453
    else :#line:454
        OOOOOO00O0OO000O0 =[]#line:455
    OO0OOO00OOO0O00O0 =set ()#line:457
    for O0OOOO00O0OO0O0O0 in OO000O00OOO0OOOOO :#line:458
        O00OO00OO0OO00O00 =fetch_channels (O0OOOO00O0OO0O0O0 ,O00O000O00OOOOO0O )#line:459
        for OO00OO0OOOO0000OO in O00OO00OO0OO00O00 :#line:460
            OO000O00OO00O0O0O =fetch_messages (O0OOOO00O0OO0O0O0 ,OO00OO0OOOO0000OO ,limit =100 )#line:461
            O0O0O00O0OO00O000 =extract_uids_from_messages (OO000O00OO00O0O0O )#line:462
            OO0OOO00OOO0O00O0 .update (O0O0O00O0OO00O000 )#line:463
    OO0OOO00OOO0O00O0 =list (set (OO0OOO00OOO0O00O0 )-set (O00OO0O00O000O0OO ))#line:466
    for _OOO000O00OOOO0O00 in range (O000O0OOOO0000OO0 ):#line:468
        for O0OOOO00O0OO0O0O0 in OO000O00OOO0OOOOO :#line:469
            if OOOOOO00O0OO000O0 :#line:470
                O00OO00OO0OO00O00 =OOOOOO00O0OO000O0 #line:471
            for OO00OO0OOOO0000OO in O00OO00OO0OO00O00 :#line:472
                send_message_with_mention (O0OOOO00O0OO0O0O0 ,OO00OO0OOOO0000OO ,OO00OOOOO0OO0000O ,OO0OOO00OOO0O00O0 )#line:473
                time .sleep (OO000O0O0O000O000 )#line:474
def join_discord_invite ():#line:479
    try :#line:480
        with open ("token.txt")as O0OOO00O0OOOO0000 :#line:481
            OO0OOOOO00OOO0OO0 =[OO000OOOO0O0O0OOO .strip ()for OO000OOOO0O0O0OOO in O0OOO00O0OOOO0000 .readlines ()if OO000OOOO0O0O0OOO .strip ()]#line:482
    except (FileNotFoundError ,KeyError ):#line:483
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:484
        return #line:485
    OO0000OOO0000O00O =input ("Invite Code?: discord.gg/").strip ()#line:487
    for OO0O0O0O0OOOO0OO0 in OO0OOOOO00OOO0OO0 :#line:490
        joiner (OO0O0O0O0OOOO0OO0 ,OO0000OOO0000O00O )#line:491
import json ,time ,base64 ,random ,requests #line:493
def cookieset (OO0O0OOO000O00000 ):#line:495
    O00OOO00O0OO0OOOO =OO0O0OOO000O00000 .get ("https://discord.com/app")#line:496
    return O00OOO00O0OO0OOOO .cookies .get_dict ()#line:497
def generatexspandua (O0OO0000OOOOOO0OO ):#line:499
    O0OO0O0OO00O0O0O0 =["Android","Windows","Macintosh"]#line:500
    O000OO000O00O000O =random .choice (O0OO0O0OO00O0O0O0 )#line:501
    if O000OO000O00O000O =="Macintosh":#line:502
        OOOOOOOOOO0000O00 =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:503
        O0O0O0O0000OOO0OO ="Macintosh; Intel Mac OS X "+OOOOOOOOOO0000O00 #line:504
        O0O00O0OOO0OO0000 ="x86_64"#line:505
    elif O000OO000O00O000O =="Windows":#line:506
        OOOOOOOOOO0000O00 =f'{random.choice([6.0, 10.0, 11.0])}'#line:507
        O0O0O0O0000OOO0OO ="Windows NT "+OOOOOOOOOO0000O00 +" Win64; x64"#line:508
        O0O00O0OOO0OO0000 ="x86_64"#line:509
    else :#line:510
        OOOOOOOOOO0000O00 ="13"#line:511
        O0O0O0O0000OOO0OO =f"Linux; Android 13; Pixel 6a"#line:512
        O0O00O0OOO0OO0000 ="aarch64"#line:513
    O0O0O00O0000O00O0 ={"os":O000OO000O00O000O ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":OOOOOOOOOO0000O00 ,"os_arch":O0O00O0OOO0OO0000 ,"system_locale":"ja-JP","client_build_number":O0OO0000OOOOOO0OO ,"client_event_source":None ,"design_id":0 }#line:526
    O000O000OO00O00OO =f"Mozilla/5.0 ({O0O0O0O0000OOO0OO}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:527
    return base64 .b64encode (json .dumps (O0O0O00O0000O00O0 ,separators =(',',':')).encode ()).decode (),O000O000OO00O00OO #line:528
def joiner (O0OO000000O0OO0OO ,O000O00OOOOOOO0O0 ,OO00OO00000OO0OOO ,O00OO000OOO0OOOOO ):#line:530
  OOOO0O0000O0O00O0 =get_session (OO00OO00000OO0OOO )#line:531
  O00OO0O0O0O0O0OO0 =cookieset (OOOO0O0000O0O00O0 )#line:532
  O00OO0O0O0O0O0OO0 ["locale"]="ja-JP"#line:533
  O0000OOO0O0O0O00O =201211 #line:534
  O000OOOOO00000OOO ,OO0O000OOO0O0000O =generatexspandua (O0000OOO0O0O0O00O )#line:535
  OO0OOO00O0OO00000 ={"Authorization":O0OO000000O0OO0OO ,"accept":"*/*","accept-language":"ja-JP","connection":"keep-alive","DNT":"1","origin":"https://discord.com","sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","referer":"https://discord.com/channels/@me","TE":"Trailers","user-agent":OO0O000OOO0O0000O ,"X-Super-Properties":O000OOOOO00000OOO ,}#line:550
  OOO0O0O00O00OO0O0 =OOOO0O0000O0O00O0 .post ("https://discord.com/api/v9/invites/"+O000O00OOOOOOO0O0 ,headers =OO0OOO00O0OO00000 ,json ={},cookies =O00OO0O0O0O0O0OO0 )#line:552
  if OOO0O0O00O00OO0O0 .status_code ==200 :#line:553
    print ("[+] Probably joined "+O0OO000000O0OO0OO )#line:554
    if "show_verification_form"in OOO0O0O00O00OO0O0 .json ():#line:555
      bypass (O0OO000000O0OO0OO ,OOO0O0O00O00OO0O0 .json ()["guild"]["id"],OOOO0O0000O0O00O0 ,OO0OOO00O0OO00000 )#line:556
    return #line:557
  elif "captcha_key"in OOO0O0O00O00OO0O0 .text and OOO0O0O00O00OO0O0 .status_code ==400 :#line:558
    print ("[!] Hcaptcha interference "+O0OO000000O0OO0OO )#line:559
    return #line:560
  elif OOO0O0O00O00OO0O0 .status_code ==401 :#line:561
    print ("[!] Token is dead "+O0OO000000O0OO0OO )#line:562
    return #line:563
  elif OOO0O0O00O00OO0O0 .status_code ==403 :#line:564
    if "message"in OOO0O0O00O00OO0O0 .json ():#line:565
      if OOO0O0O00O00OO0O0 .json ()["message"]=="Unknown Message":#line:566
        print ("[!] Unknown error "+O0OO000000O0OO0OO )#line:567
        return #line:568
      else :#line:569
        print ("[!] Verification required "+O0OO000000O0OO0OO )#line:570
        return #line:571
    else :#line:572
      print ("[!] Error occurred "+O0OO000000O0OO0OO )#line:573
      return #line:574
  elif OOO0O0O00O00OO0O0 .status_code ==429 :#line:575
    print ("[!] Token rate-limited "+O0OO000000O0OO0OO )#line:576
    return #line:577
  elif OOO0O0O00O00OO0O0 .status_code ==400 :#line:578
    if "captcha_key"in OOO0O0O00O00OO0O0 .json ():#line:579
      print ("[!] Hcaptcha interference "+O0OO000000O0OO0OO )#line:580
      return #line:581
    else :#line:582
      print ("[!] Error occurred "+O0OO000000O0OO0OO )#line:583
      return #line:584
  elif OOO0O0O00O00OO0O0 .status_code ==401 :#line:585
    print ("[!] Token is dead "+O0OO000000O0OO0OO )#line:586
    return #line:587
  elif OOO0O0O00O00OO0O0 .status_code ==403 :#line:588
    if "message"in OOO0O0O00O00OO0O0 .json ():#line:589
      if OOO0O0O00O00OO0O0 .json ()["message"]=="Unknown Message":#line:590
        print ("[!] Unknown error "+O0OO000000O0OO0OO )#line:591
        return #line:592
      else :#line:593
        print ("[!] Verification required "+O0OO000000O0OO0OO )#line:594
        return #line:595
    else :#line:596
      print ("[!] Error occurred "+O0OO000000O0OO0OO )#line:597
  elif OOO0O0O00O00OO0O0 .status_code ==429 :#line:598
    print ("[!] Token rate-limited "+O0OO000000O0OO0OO )#line:599
    return #line:600
  else :#line:601
    print ("[!] Error occurred "+O0OO000000O0OO0OO )#line:602
    return #line:603
def update_group_ids ():#line:606
    OO000O0OOO00O0OOO =input ("Invite Code?: ").strip ()#line:607
    try :#line:608
        with open ("token.txt")as O0O0O00OO000OOOOO :#line:609
            OO0O00O00OOO000OO =[OOOOOO0O0O00OOO00 .strip ()for OOOOOO0O0O00OOO00 in O0O0O00OO000OOOOO .readlines ()if OOOOOO0O0O00OOO00 .strip ()]#line:610
    except (FileNotFoundError ,KeyError ):#line:611
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:612
        return #line:613
    O00O0O0O0O0O00OO0 =requests .Session ()#line:615
    for OO0OOOO000OO0O0OO in OO0O00O00OOO000OO :#line:616
        joiner (OO0OOOO000OO0O0OO ,OO000O0OOO00O0OOO ,O00O0O0O0O0O00OO0 )#line:617
        time .sleep (2 )#line:618
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:620
def bypass (O00O0O000OO00OO00 ,O00OO00O000O0O000 ,OOOOOOOOOO00O0O00 ,OO0OO0OOO0000O0O0 ):#line:623
    try :#line:624
        O0000O0O0OOOOOO00 =OOOOOOOOOO00O0O00 .get (f"https://discord.com/api/v9/guilds/{O00OO00O000O0O000}/member-verification?with_guild=false",headers =OO0OO0OOO0000O0O0 ).json ()#line:625
        OOOO0O0O0OO0OOOO0 =OOOOOOOOOO00O0O00 .put (f"https://discord.com/api/v9/guilds/{O00OO00O000O0O000}/requests/@me",headers =OO0OO0OOO0000O0O0 ,json =O0000O0O0OOOOOO00 )#line:626
        if OOOO0O0O0OO0OOOO0 .status_code ==201 :#line:627
            print (f"[+] MemberscreeningBypassed {O00O0O000OO00OO00}")#line:628
            return #line:629
        else :#line:630
            print (f"[!] Bypassが出来ませんでした {O00O0O000OO00OO00}")#line:631
            return #line:632
    except Exception as OO0O0OO0O0OO000OO :#line:633
        print (f"[!] エラーが発生しました。{OO0O0OO0O0OO000OO}")#line:634
session =requests .Session ()#line:636
def reactionput (O0OOOO0OO0O0OOO00 ,O00O0O0O0O0O00000 ,O00O0000O0OOOO0O0 ,OOOOO0OOOOOOOO00O ,proxy =None ):#line:639
    OO0000000OOO0O000 =get_session (proxy )#line:640
    O0OOO0O0OOOOOOO00 =get_headers (OO0000000OOO0O000 )#line:641
    O0OOO0O0OOOOOOO00 ["Authorization"]=O0OOOO0OO0O0OOO00 #line:642
    OOOOO0OOOOOOOO00O =requests .utils .quote (OOOOO0OOOOOOOO00O )#line:644
    O0O000O00OOOOOOOO =OO0000000OOO0O000 .put (f"https://discord.com/api/v9/channels/{O00O0O0O0O0O00000}/messages/{O00O0000O0OOOO0O0}/reactions/{OOOOO0OOOOOOOO00O}/%40me?location=Message&type=0",headers =O0OOO0O0OOOOOOO00 )#line:648
    if O0O000O00OOOOOOOO .status_code in [200 ,204 ]:#line:649
        print (f"[+] Reaction '{OOOOO0OOOOOOOO00O}' added successfully to message {O00O0000O0OOOO0O0}")#line:650
    elif O0O000O00OOOOOOOO .status_code ==429 :#line:651
        print ("[-] Rate limited. Please wait before retrying.")#line:652
        OOOOOO000O0OOOO0O =O0O000O00OOOOOOOO .json ().get ("retry_after",1 )#line:653
        time .sleep (OOOOOO000O0OOOO0O )#line:654
    elif O0O000O00OOOOOOOO .status_code ==401 :#line:655
        print ("[-] Invalid or expired token.")#line:656
    else :#line:657
        print (f"[!] Error occurred: {O0O000O00OOOOOOOO.status_code}")#line:658
def generatexspandua (O0O00OOOOOOOO00OO ):#line:661
  OOO0OO00000O0OOOO =["Android","Windows","Macintosh"]#line:662
  OO0000OOO0O0O000O =random .choice (OOO0OO00000O0OOOO )#line:663
  if OO0000OOO0O0O000O =="Macintosh":#line:664
    OO00OOO0O00OO0OOO =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:665
    O00O00OO0O00OOOOO ="Macintosh; Intel Mac OS X "+OO00OOO0O00OO0OOO #line:666
    OO0OO00OOO0O0000O ="x86_64"#line:667
  if OO0000OOO0O0O000O =="Windows":#line:668
    OO00OOO0O00OO0OOO =f'{random.choice([6.0,10.0,11.0])}'#line:669
    O00O00OO0O00OOOOO ="Windows NT "+OO00OOO0O00OO0OOO +" Win64; x64"#line:670
    OO0OO00OOO0O0000O ="x86_64"#line:671
  if OO0000OOO0O0O000O =="Android":#line:672
    OO00OOO0O00OO0OOO ="13"#line:673
    O00O00OO0O00OOOOO =f"Linux; Android 13; Pixel 6a"#line:674
    OO0OO00OOO0O0000O ="aarch64"#line:675
  OO00O000OOOOO00O0 ={"os":OO0000OOO0O0O000O ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":OO00OOO0O00OO0OOO ,"os_arch":OO0OO00OOO0O0000O ,"system_locale":"ja-JP","client_build_number":O0O00OOOOOOOO00OO ,"client_event_source":None ,"design_id":0 }#line:676
  O0OOO0OO00OOOO000 =f"Mozilla/5.0 ({O00O00OO0O00OOOOO}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:677
  return base64 .b64encode (json .dumps (OO00O000OOOOO00O0 ,separators =(',',':')).encode ()).decode (),O0OOO0OO00OOOO000 #line:678
import base64 #line:680
def nickchanger ():#line:683
    try :#line:684
        with open ("token.txt")as OO00O00O0OOO0000O :#line:685
            OOO0OO0OOOOOOO000 =[O00O00OO0OOOO0O00 .strip ()for O00O00OO0OOOO0O00 in OO00O00O0OOO0000O .readlines ()if O00O00OO0OOOO0O00 .strip ()]#line:686
    except (FileNotFoundError ,KeyError ):#line:687
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:688
        return #line:689
    O000O00O0O00O0OO0 =input ("Server ID?: ").strip ()#line:691
    O0OO0OO0OOOOO00OO =input ("Nickname?: ").strip ()#line:692
    O0O0O0OOO0OO0OO00 =input ("Delay (in seconds)?: ").strip ()#line:693
    try :#line:695
        O0O0O0OOO0OO0OO00 =float (O0O0O0OOO0OO0OO00 )#line:696
        if O0O0O0OOO0OO0OO00 <0 :#line:697
            raise ValueError #line:698
    except ValueError :#line:699
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:700
        O0O0O0OOO0OO0OO00 =1.0 #line:701
    for O0000OO0O000O000O in OOO0OO0OOOOOOO000 :#line:703
        OO00O0000O00O0OO0 ={"Authorization":O0000OO0O000O000O ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:708
        O00OO0OOO0O0000O0 ={"nick":O0OO0OO0OOOOO00OO }#line:709
        OO00O0OOO0O0O00O0 =requests .patch (f"https://discord.com/api/v9/guilds/{O000O00O0O00O0OO0}/members/@me",headers =OO00O0000O00O0OO0 ,json =O00OO0OOO0O0000O0 )#line:710
        if OO00O0OOO0O0O00O0 .status_code ==200 :#line:712
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Nickname changed to '{O0OO0OO0OOOOO00OO}' successfully for token {O0000OO0O000O000O}.{colorama.Fore.RESET}")#line:713
        elif OO00O0OOO0O0O00O0 .status_code ==429 :#line:714
            print (f"{colorama.Fore.RED}    [!] Rate limited. Please wait before retrying for token {O0000OO0O000O000O}.{colorama.Fore.RESET}")#line:715
            O0OO00O00OOOO0OOO =OO00O0OOO0O0O00O0 .json ().get ("retry_after",1 )#line:716
            time .sleep (O0OO00O00OOOO0OOO )#line:717
        else :#line:718
            print (f"{colorama.Fore.RED}    [!] Error occurred: {OO00O0OOO0O0O00O0.status_code} for token {O0000OO0O000O000O}.{colorama.Fore.RESET}")#line:719
        time .sleep (O0O0O0OOO0OO0OO00 )#line:721
import json ,websocket ,threading ,tls_client ,random ,time #line:725
session =tls_client .Session (client_identifier ="chrome112",random_tls_extension_order =True )#line:727
class Utils :#line:729
    @staticmethod #line:730
    def rangeCorrector (O00O000OOO000OOO0 ):#line:731
        if [0 ,99 ]not in O00O000OOO000OOO0 :#line:732
            O00O000OOO000OOO0 .insert (0 ,[0 ,99 ])#line:733
        return O00O000OOO000OOO0 #line:734
    @staticmethod #line:736
    def getRanges (O0OO0000O0OOOOO00 ,OOO0OOO0OO0OO0O00 ,O0000O0O0OO00OOOO ):#line:737
        O00O00000O00OO00O =int (O0OO0000O0OOOOO00 *OOO0OOO0OO0OO0O00 )#line:738
        O00OO0O0OO00O0OOO =[[O00O00000O00OO00O ,O00O00000O00OO00O +99 ]]#line:739
        if O0000O0O0OO00OOOO >O00O00000O00OO00O +99 :#line:740
            O00OO0O0OO00O0OOO .append ([O00O00000O00OO00O +100 ,O00O00000O00OO00O +199 ])#line:741
        return Utils .rangeCorrector (O00OO0O0OO00O0OOO )#line:742
    @staticmethod #line:744
    def parseGuildMemberListUpdate (OOOOOO0OO0OOOO00O ):#line:745
        OO0OOOO0OOOOO000O ={"online_count":OOOOOO0OO0OOOO00O ["d"]["online_count"],"member_count":OOOOOO0OO0OOOO00O ["d"]["member_count"],"id":OOOOOO0OO0OOOO00O ["d"]["id"],"guild_id":OOOOOO0OO0OOOO00O ["d"]["guild_id"],"hoisted_roles":OOOOOO0OO0OOOO00O ["d"]["groups"],"types":[],"locations":[],"updates":[],}#line:755
        for O0O000OO00OOO0OOO in OOOOOO0OO0OOOO00O ["d"]["ops"]:#line:757
            OO0OOOO0OOOOO000O ["types"].append (O0O000OO00OOO0OOO ["op"])#line:758
            if O0O000OO00OOO0OOO ["op"]in ("SYNC","INVALIDATE"):#line:759
                OO0OOOO0OOOOO000O ["locations"].append (O0O000OO00OOO0OOO ["range"])#line:760
                if O0O000OO00OOO0OOO ["op"]=="SYNC":#line:761
                    OO0OOOO0OOOOO000O ["updates"].append (O0O000OO00OOO0OOO ["items"])#line:762
                else :#line:763
                    OO0OOOO0OOOOO000O ["updates"].append ([])#line:764
            elif O0O000OO00OOO0OOO ["op"]in ("INSERT","UPDATE","DELETE"):#line:765
                OO0OOOO0OOOOO000O ["locations"].append (O0O000OO00OOO0OOO ["index"])#line:766
                if O0O000OO00OOO0OOO ["op"]=="DELETE":#line:767
                    OO0OOOO0OOOOO000O ["updates"].append ([])#line:768
                else :#line:769
                    OO0OOOO0OOOOO000O ["updates"].append (O0O000OO00OOO0OOO ["item"])#line:770
        return OO0OOOO0OOOOO000O #line:771
class DiscordSocket (websocket .WebSocketApp ):#line:773
    def __init__ (O00O0O0OOO0O0O0OO ,OOO0O0O0OO00000O0 ,OOO0O0O000OOOO00O ,OOO00O0OOOOO00OO0 ):#line:774
        O00O0O0OOO0O0O0OO .token =OOO0O0O0OO00000O0 #line:775
        O00O0O0OOO0O0O0OO .guild_id =OOO0O0O000OOOO00O #line:776
        O00O0O0OOO0O0O0OO .channel_id =OOO00O0OOOOO00OO0 #line:777
        O00O0O0OOO0O0O0OO .socket_headers ={"Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","Cache-Control":"no-cache","Pragma":"no-cache","Sec-WebSocket-Extensions":"permessage-deflate; client_max_window_bits","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",}#line:785
        super ().__init__ ("wss://gateway.discord.gg/?encoding=json&v=9",header =O00O0O0OOO0O0O0OO .socket_headers ,on_open =lambda O00OO0OOOOOO0OOOO :O00O0O0OOO0O0O0OO .sock_open (O00OO0OOOOOO0OOOO ),on_message =lambda O0OO0000O000O0O0O ,OO0000O0O00O0OO00 :O00O0O0OOO0O0O0OO .sock_message (O0OO0000O000O0O0O ,OO0000O0O00O0OO00 ),on_close =lambda O0O0O0O0O00OO0O00 ,OO00O00OO00OOO0O0 ,O000O0OOO000OO000 :O00O0O0OOO0O0O0OO .sock_close (O0O0O0O0O00OO0O00 ,OO00O00OO00OOO0O0 ,O000O0OOO000OO000 ),)#line:794
        O00O0O0OOO0O0O0OO .endScraping =False #line:796
        O00O0O0OOO0O0O0OO .guilds ={}#line:797
        O00O0O0OOO0O0O0OO .members ={}#line:798
        O00O0O0OOO0O0O0OO .ranges =[[0 ,0 ]]#line:799
        O00O0O0OOO0O0O0OO .lastRange =0 #line:800
        O00O0O0OOO0O0O0OO .packets_recv =0 #line:801
    def run (OO000OO00O00OO00O ):#line:803
        OO000OO00O00OO00O .run_forever ()#line:804
        return OO000OO00O00OO00O .members #line:805
    def scrapeUsers (O0OO00O0O00000O0O ):#line:807
        if not O0OO00O0O00000O0O .endScraping :#line:808
            O0OO00O0O00000O0O .send ('{"op":14,"d":{"guild_id":"'+O0OO00O0O00000O0O .guild_id +'","typing":true,"activities":true,"threads":true,"channels":{"'+O0OO00O0O00000O0O .channel_id +'":'+json .dumps (O0OO00O0O00000O0O .ranges )+"}}}")#line:817
    def sock_open (OOO0OO00O0OO00O00 ,O0OO00O0O0OO00O0O ):#line:819
        OOO0OO00O0OO00O00 .send ('{"op":2,"d":{"token":"'+OOO0OO00O0OO00O00 .token +'","capabilities":125,"properties":{"os":"Windows NT","browser":"Chrome","device":"","system_locale":"it-IT","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36","browser_version":"119.0","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":103981,"client_event_source":null},"presence":{"status":"online","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}')#line:824
    def heartbeatThread (OO0OOOOO0000OO00O ,OO00OOOO00OO0O0OO ):#line:826
        try :#line:827
            while True :#line:828
                OO0OOOOO0000OO00O .send ('{"op":1,"d":'+str (OO0OOOOO0000OO00O .packets_recv )+"}")#line:829
                time .sleep (OO00OOOO00OO0O0OO )#line:830
        except Exception as OO000000000OO0OO0 :#line:831
            pass #line:832
    def sock_message (OO00OOOOO0O000000 ,OO000000OOO0OO00O ,O0OO0O00O000O0OOO ):#line:834
        OO00OOOOOOO00OOO0 =json .loads (O0OO0O00O000O0OOO )#line:835
        if OO00OOOOOOO00OOO0 is None :#line:836
            return #line:837
        if OO00OOOOOOO00OOO0 ["op"]!=11 :#line:838
            OO00OOOOO0O000000 .packets_recv +=1 #line:839
        if OO00OOOOOOO00OOO0 ["op"]==10 :#line:840
            threading .Thread (target =OO00OOOOO0O000000 .heartbeatThread ,args =(OO00OOOOOOO00OOO0 ["d"]["heartbeat_interval"]/1000 ,),daemon =True ,).start ()#line:845
        if OO00OOOOOOO00OOO0 ["t"]=="READY":#line:846
            for O000OO0000OO00O0O in OO00OOOOOOO00OOO0 ["d"]["guilds"]:#line:847
                OO00OOOOO0O000000 .guilds [O000OO0000OO00O0O ["id"]]={"member_count":O000OO0000OO00O0O ["member_count"]}#line:848
        if OO00OOOOOOO00OOO0 ["t"]=="READY_SUPPLEMENTAL":#line:849
            OO00OOOOO0O000000 .ranges =Utils .getRanges (0 ,100 ,OO00OOOOO0O000000 .guilds [OO00OOOOO0O000000 .guild_id ]["member_count"])#line:852
            OO00OOOOO0O000000 .scrapeUsers ()#line:853
        elif OO00OOOOOOO00OOO0 ["t"]=="GUILD_MEMBER_LIST_UPDATE":#line:854
            O00O00OO0OOO000O0 =Utils .parseGuildMemberListUpdate (OO00OOOOOOO00OOO0 )#line:855
            if O00O00OO0OOO000O0 ["guild_id"]==OO00OOOOO0O000000 .guild_id and ("SYNC"in O00O00OO0OOO000O0 ["types"]or "UPDATE"in O00O00OO0OOO000O0 ["types"]):#line:859
                for O00O0OO00OO00OO00 ,OO0OO0OO0OOOO0OO0 in enumerate (O00O00OO0OOO000O0 ["types"]):#line:860
                    if OO0OO0OO0OOOO0OO0 =="SYNC":#line:861
                        if len (O00O00OO0OOO000O0 ["updates"][O00O0OO00OO00OO00 ])==0 :#line:862
                            OO00OOOOO0O000000 .endScraping =True #line:863
                            break #line:864
                        for O00OO0OOO0OOO0O0O in O00O00OO0OOO000O0 ["updates"][O00O0OO00OO00OO00 ]:#line:866
                            if "member"in O00OO0OOO0OOO0O0O :#line:867
                                O0OO0O000O0OOO000 =O00OO0OOO0OOO0O0O ["member"]#line:868
                                OO0O00OOO00O0OO00 ={"tag":O0OO0O000O0OOO000 ["user"]["username"]+"#"+O0OO0O000O0OOO000 ["user"]["discriminator"],"id":O0OO0O000O0OOO000 ["user"]["id"],}#line:874
                                if not O0OO0O000O0OOO000 ["user"].get ("bot"):#line:875
                                    OO00OOOOO0O000000 .members [O0OO0O000O0OOO000 ["user"]["id"]]=OO0O00OOO00O0OO00 #line:876
                    elif OO0OO0OO0OOOO0OO0 =="UPDATE":#line:878
                        for O00OO0OOO0OOO0O0O in O00O00OO0OOO000O0 ["updates"][O00O0OO00OO00OO00 ]:#line:879
                            if "member"in O00OO0OOO0OOO0O0O :#line:880
                                O0OO0O000O0OOO000 =O00OO0OOO0OOO0O0O ["member"]#line:881
                                OO0O00OOO00O0OO00 ={"tag":O0OO0O000O0OOO000 ["user"]["username"]+"#"+O0OO0O000O0OOO000 ["user"]["discriminator"],"id":O0OO0O000O0OOO000 ["user"]["id"],}#line:887
                                if not O0OO0O000O0OOO000 ["user"].get ("bot"):#line:888
                                    OO00OOOOO0O000000 .members [O0OO0O000O0OOO000 ["user"]["id"]]=OO0O00OOO00O0OO00 #line:889
                    OO00OOOOO0O000000 .lastRange +=1 #line:891
                    OO00OOOOO0O000000 .ranges =Utils .getRanges (OO00OOOOO0O000000 .lastRange ,100 ,OO00OOOOO0O000000 .guilds [OO00OOOOO0O000000 .guild_id ]["member_count"])#line:894
                    time .sleep (0.45 )#line:895
                    OO00OOOOO0O000000 .scrapeUsers ()#line:896
            if OO00OOOOO0O000000 .endScraping :#line:898
                OO00OOOOO0O000000 .close ()#line:899
    def sock_close (O000OO0OOOO0OO00O ,O000O0OO0O0OOO000 ,O0OO0O0OOO0OOO0O0 ,OOOO0O0OOOOOO00O0 ):#line:901
        pass #line:902
def scrape (OO0OOO000OO0OOOOO ,OOO0000O0O000OOO0 ,O0OO00OOOO00O000O ):#line:904
    OOO000OOO0OOO0000 =DiscordSocket (OO0OOO000OO0OOOOO ,OOO0000O0O000OOO0 ,O0OO00OOOO00O000O )#line:905
    return OOO000OOO0OOO0000 .run ()#line:906
def member_scrape (O0000OOO00O0O0O00 ,OOOOOOOOOOO0O0O00 ,OO0OOOOO00O0OOO0O ):#line:908
    O00OOOOOO000O0O0O =[]#line:909
    for O0OOOOOOO00O00O00 in O0000OOO00O0O0O00 :#line:910
        O0OO0OOO0O00O0O0O ={"Authorization":O0OOOOOOO00O00O00 ,"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}#line:911
        O0O00O0000OO00O0O =session .get (f"https://canary.discord.com/api/v9/guilds/{OOOOOOOOOOO0O0O00}",headers =O0OO0OOO0O00O0O0O )#line:912
        if O0O00O0000OO00O0O .status_code ==200 :#line:913
            O00OOOOOO000O0O0O .append (O0OOOOOOO00O00O00 )#line:914
            break #line:915
    if not O00OOOOOO000O0O0O :#line:916
        print ("missing access")#line:917
    O0OOOOOOO00O00O00 =random .choice (O00OOOOOO000O0O0O )#line:919
    O00O000000OO00OO0 =scrape (O0OOOOOOO00O00O00 ,OOOOOOOOOOO0O0O00 ,OO0OOOOO00O0OOO0O )#line:920
    O0O0O0000O000O00O =[f"<@{O0O0OO00O000OOO00}>"for O0O0OO00O000OOO00 in [int (OOO00OO0OO0OO0O00 )for OOO00OO0OO0OO0O00 in O00O000000OO00OO0 .keys ()]]#line:921
    print (f"[SUCCESS] {len(O0O0O0000O000O00O)} scraped members")#line:922
    return O0O0O0000O000O00O #line:923
def spammer_menu ():#line:925
    try :#line:926
        with open ("token.txt")as OOOO00OOOOO000OO0 :#line:927
            O0O0OO00O0000O00O =[OO0O0OO0OO0O00O00 .strip ()for OO0O0OO0OO0O00O00 in OOOO00OOOOO000OO0 .readlines ()if OO0O0OO0OO0O00O00 .strip ()]#line:928
    except (FileNotFoundError ,KeyError ):#line:929
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:930
        return #line:931
    OOOO0O00O00OOOOOO =input ("Server ID?: ").strip ()#line:933
    O0O0OO0O0OO000O0O =input ("Message?: ").strip ()#line:934
    OOO00O0000O0000OO =input ("Random mention (True/False)?: ").strip ().lower ()=='true'#line:935
    O00OOO0OOOO00O0OO =input ("Delay between messages (in seconds)?: ").strip ()#line:936
    O0OO0O0OO0OOOOO0O =input ("Number of messages to send?: ").strip ()#line:937
    OO0OOOO00OO0OOOOO =input ("Blacklist User IDs (comma-separated) (Leave blank to skip)?: ").strip ().split (',')#line:938
    OO0OOOO00OO0OOOOO =[f"<@{OO0OOO000000OOO0O.strip()}>"for OO0OOO000000OOO0O in OO0OOOO00OO0OOOOO if OO0OOO000000OOO0O .strip ()]#line:939
    try :#line:941
        O00OOO0OOOO00O0OO =float (O00OOO0OOOO00O0OO )#line:942
        if O00OOO0OOOO00O0OO <0 :#line:943
            raise ValueError #line:944
    except ValueError :#line:945
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:946
        O00OOO0OOOO00O0OO =1.0 #line:947
    try :#line:949
        O0OO0O0OO0OOOOO0O =int (O0OO0O0OO0OOOOO0O )#line:950
        if O0OO0O0OO0OOOOO0O <=0 :#line:951
            raise ValueError #line:952
    except ValueError :#line:953
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:954
        O0OO0O0OO0OOOOO0O =1 #line:955
    O0OO0O000OOO0OOO0 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:957
    if O0OO0O000OOO0OOO0 =='2':#line:958
        O0OOO0OO0O00O0O00 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:959
        O0OOO0OO0O00O0O00 =[O000000OOO0O00O00 .strip ()for O000000OOO0O00O00 in O0OOO0OO0O00O0O00 if O000000OOO0O00O00 .strip ()]#line:960
    else :#line:961
        O0OOO0OO0O00O0O00 =fetch_channels (O0O0OO00O0000O00O [0 ],OOOO0O00O00OOOOOO )#line:962
    O00O0O0OOO00O0000 =None #line:964
    spammer (O0O0OO00O0000O00O ,OOOO0O00O00OOOOOO ,O0OOO0OO0O00O0O00 ,O0O0OO0O0OO000O0O ,OOO00O0000O0000OO ,OO0OOOO00OO0OOOOO ,O00O0O0OOO00O0000 ,O0OO0O0OO0OOOOO0O )#line:966
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:969
def buildnumget (O00O00O0OOOO0OO0O ):#line:971
  O0OO00000O0000O0O =O00O00O0OOOO0OO0O .get ('https://discord.com/login',headers ={'Accept-Encoding':'gzip, deflate'},timeout =7 )#line:972
  O00OO0OOOO0OOOO0O =O0OO00000O0000O0O .text #line:973
import discum #line:975
import random #line:976
import time #line:977
def userget (OO00OOOO000OO0O0O ,OOOOO00O000OO00O0 ,OO0OO00OOO0OOO0O0 ):#line:979
    O0O000O0O0OOO0000 =[]#line:980
    O0OOO00000O0O00O0 =discum .Client (token =OO00OOOO000OO0O0O ,log =False )#line:981
    def OO000O0O00OOO0000 (O0O000OOOOO0O0000 ):#line:983
        if O0OOO00000O0O00O0 .gateway .finishedMemberFetching (OOOOO00O000OO00O0 ):#line:984
            O0OOOO0O0OO000OOO =len (O0OOO00000O0O00O0 .gateway .session .guild (OOOOO00O000OO00O0 ).members )#line:985
            print (str (O0OOOO0O0OO000OOO )+' members fetched')#line:986
            O0OOO00000O0O00O0 .gateway .removeCommand ({'function':OO000O0O00OOO0000 ,'params':{}})#line:987
            O0OOO00000O0O00O0 .gateway .close ()#line:988
    def OOO0OOOO0OO00O0OO (OOOOOOO0OOO0O0OOO ,OOOO0O00O00O0O000 ):#line:990
        O0OOO00000O0O00O0 .gateway .fetchMembers (OOOOOOO0OOO0O0OOO ,OOOO0O00O00O0O000 ,keep ='all',wait =1 )#line:991
        O0OOO00000O0O00O0 .gateway .command ({'function':OO000O0O00OOO0000 ,'params':{}})#line:992
        O0OOO00000O0O00O0 .gateway .run ()#line:993
        O0OOO00000O0O00O0 .gateway .resetSession ()#line:994
        return O0OOO00000O0O00O0 .gateway .session .guild (OOOOOOO0OOO0O0OOO ).members #line:995
    O0O000O0O000O00O0 =OOO0OOOO0OO00O0OO (OOOOO00O000OO00O0 ,OO0OO00OOO0OOO0O0 )#line:997
    for OO00OOO0OOOO0000O in O0O000O0O000O00O0 :#line:998
        if OO00OOO0OOOO0000O not in O0O000O0O0OOO0000 :#line:999
            O0O000O0O0OOO0000 .append (f"<@{OO00OOO0OOOO0000O}>")#line:1000
    return O0O000O0O0OOO0000 #line:1001
def spammer (OO0OOOOO00000O00O ,OOO0O0OOOO00OOO00 ,OO000O00OOO000OOO ,O0OOO00000OOOOO00 ,OOOO00O00000O0O00 ,O00O0OO0O000OO000 ,OO000000O0O0O0OOO ,OO0OO0O00OOOOO000 ):#line:1006
    OO0OO00000O0O0O00 =get_session (OO000000O0O0O0OOO )#line:1007
    O0O00O000OO0OO0OO =0 #line:1008
    O0O000000OOO0OOOO =userget (OO0OOOOO00000O00O [0 ],OOO0O0OOOO00OOO00 ,OO000O00OOO000OOO [0 ])#line:1010
    O0O000000OOO0OOOO =[OO0000OOOOOO000O0 for OO0000OOOOOO000O0 in O0O000000OOO0OOOO if OO0000OOOOOO000O0 not in O00O0OO0O000OO000 ]#line:1013
    for _O0000O000OO00O0OO in range (OO0OO0O00OOOOO000 ):#line:1015
        OO0O000O000O00000 =OO0OOOOO00000O00O [O0O00O000OO0OO0OO ]#line:1016
        OOOOO0OO00O00O00O =get_headers (OO0O000O000O00000 )#line:1017
        for OO0OOOOO0O00OO000 in OO000O00OOO000OOO :#line:1018
            O0OO0000O00O0OO00 =O0OOO00000OOOOO00 #line:1019
            if OOOO00O00000O0O00 and O0O000000OOO0OOOO :#line:1020
                OOOO000O0OO0O0000 =random .choice (O0O000000OOO0OOOO )#line:1021
                O0OO0000O00O0OO00 +=f" {OOOO000O0OO0O0000}"#line:1022
            O00OOOO0OOO00O000 =OO0OO00000O0O0O00 .post (f"https://discord.com/api/v9/channels/{OO0OOOOO0O00OO000}/messages",json ={"content":O0OO0000O00O0OO00 },headers =OOOOO0OO00O00O00O )#line:1024
            if O00OOOO0OOO00O000 .status_code ==200 :#line:1025
                print (f"200 message sent: {OO0O000O000O00000}")#line:1026
            elif O00OOOO0OOO00O000 .status_code ==429 :#line:1027
                print (f"429 rate limit: {OO0O000O000O00000}")#line:1028
                OO0O00O000OOOO0O0 =O00OOOO0OOO00O000 .json ().get ("retry_after",1 )#line:1029
                time .sleep (OO0O00O000OOOO0O0 )#line:1030
            elif O00OOOO0OOO00O000 .status_code ==401 :#line:1031
                print (f"401 unknown token: {OO0O000O000O00000}")#line:1032
            else :#line:1033
                print (f"error: {OO0O000O000O00000}")#line:1034
        O0O00O000OO0OO0OO =(O0O00O000OO0OO0OO +1 )%len (OO0OOOOO00000O00O )#line:1036
        time .sleep (1 )#line:1037
import requests #line:1041
import base64 #line:1042
import colorama #line:1043
import time #line:1044
def add_emojis_from_files ():#line:1046
    try :#line:1047
        with open ("emojiname.txt")as OO00O0O0OOO0O000O ,open ("emojiurl.txt")as OO0OOOOOOOOO0O000 :#line:1048
            O0O00OO0O00O0O0OO =[OO0OO00O0O0O0O000 .strip ()for OO0OO00O0O0O0O000 in OO00O0O0OOO0O000O .read ().split (',')if OO0OO00O0O0O0O000 .strip ()]#line:1049
            O0000OO0000OO0O0O =[OOO000O0OO0O00O00 .strip ()for OOO000O0OO0O00O00 in OO0OOOOOOOOO0O000 .read ().split (',')if OOO000O0OO0O00O00 .strip ()]#line:1050
    except FileNotFoundError as O0O0O00O00OO0O0OO :#line:1051
        print (f"{colorama.Fore.RED}    [!] Error: {str(O0O0O00O00OO0O0OO)}{colorama.Fore.RESET}")#line:1052
        return #line:1053
    if len (O0O00OO0O00O0O0OO )!=len (O0000OO0000OO0O0O ):#line:1055
        print (f"{colorama.Fore.RED}    [!] Error: The number of emoji names and URLs do not match!{colorama.Fore.RESET}")#line:1056
        return #line:1057
    try :#line:1059
        with open ("token.txt")as OOO00OO0O0OO00O0O :#line:1060
            OO0O00OO00OOOOOO0 =[O0O0OOO00000OO000 .strip ()for O0O0OOO00000OO000 in OOO00OO0O0OO00O0O .readlines ()if O0O0OOO00000OO000 .strip ()]#line:1061
    except FileNotFoundError as O0O0O00O00OO0O0OO :#line:1062
        print (f"{colorama.Fore.RED}    [!] Error: {str(O0O0O00O00OO0O0OO)}{colorama.Fore.RESET}")#line:1063
        return #line:1064
    O0OO0OOO0OOO0O000 =input ("Enter the Guild ID: ").strip ()#line:1066
    OOO0O0OOOO0O0OO00 =input ("Enter the rate limit between requests (in seconds): ").strip ()#line:1067
    try :#line:1069
        OOO0O0OOOO0O0OO00 =float (OOO0O0OOOO0O0OO00 )#line:1070
        if OOO0O0OOOO0O0OO00 <0 :#line:1071
            raise ValueError #line:1072
    except ValueError :#line:1073
        print (f"{colorama.Fore.RED}    [!] Invalid rate limit. Using default rate limit of 5 seconds.{colorama.Fore.RESET}")#line:1074
        OOO0O0OOOO0O0OO00 =5.0 #line:1075
    O00OOOO0000O0O0O0 =set ()#line:1077
    for O00000O0O00O00OOO in OO0O00OO00OOOOOO0 :#line:1079
        O0000000O0OO00OOO ={'Authorization':O00000O0O00O00OOO ,'Content-Type':'application/json'}#line:1083
        OOOO0O00OOOOO000O =requests .get (f"https://discord.com/api/v9/guilds/{O0OO0OOO0OOO0O000}/emojis",headers =O0000000O0OO00OOO )#line:1086
        if OOOO0O00OOOOO000O .status_code ==200 :#line:1087
            OO00OOOOO0O0O0OOO =OOOO0O00OOOOO000O .json ()#line:1088
            for O0OOO0OOO0O00O000 in OO00OOOOO0O0O0OOO :#line:1089
                O00OOOO0000O0O0O0 .add (O0OOO0OOO0O00O000 ['name'])#line:1090
        else :#line:1091
            print (f"{colorama.Fore.RED}    [!] Error fetching existing emojis: {OOOO0O00OOOOO000O.status_code} - {OOOO0O00OOOOO000O.text}{colorama.Fore.RESET}")#line:1092
            continue #line:1093
    for O00O0O0O0O0000O00 ,OOOO000OOOOOO000O in zip (O0O00OO0O00O0O0OO ,O0000OO0000OO0O0O ):#line:1095
        if O00O0O0O0O0000O00 in O00OOOO0000O0O0O0 :#line:1096
            print (f"{colorama.Fore.YELLOW}    [*] Emoji '{O00O0O0O0O0000O00}' already exists. Skipping...{colorama.Fore.RESET}")#line:1097
            continue #line:1098
        for O00000O0O00O00OOO in OO0O00OO00OOOOOO0 :#line:1100
            try :#line:1101
                OOOO0O00OOOOO000O =requests .get (OOOO000OOOOOO000O )#line:1102
                OOOO0O00OOOOO000O .raise_for_status ()#line:1103
                OOO0OOOO0OOO0OOO0 =OOOO0O00OOOOO000O .content #line:1104
                OOO0OOOOOOO0O0O00 =base64 .b64encode (OOO0OOOO0OOO0OOO0 ).decode ('utf-8')#line:1105
                O0O000OO0O00O00O0 ={'name':O00O0O0O0O0000O00 ,'image':f"data:image/png;base64,{OOO0OOOOOOO0O0O00}"}#line:1110
                O0000000O0OO00OOO ={'Authorization':O00000O0O00O00OOO ,'Content-Type':'application/json'}#line:1115
                O0O0OO000OOO00OOO =requests .post (f"https://discord.com/api/v9/guilds/{O0OO0OOO0OOO0O000}/emojis",headers =O0000000O0OO00OOO ,json =O0O000OO0O00O00O0 )#line:1117
                if O0O0OO000OOO00OOO .status_code ==201 :#line:1118
                    print (f"{colorama.Fore.GREEN}    [+] Successfully added emoji '{O00O0O0O0O0000O00}' with token {O00000O0O00O00OOO}{colorama.Fore.RESET}")#line:1119
                    O00OOOO0000O0O0O0 .add (O00O0O0O0O0000O00 )#line:1120
                    break #line:1121
                else :#line:1122
                    print (f"{colorama.Fore.RED}    [!] Failed to add emoji '{O00O0O0O0O0000O00}' with token {O00000O0O00O00OOO}: {O0O0OO000OOO00OOO.status_code} - {O0O0OO000OOO00OOO.text}{colorama.Fore.RESET}")#line:1123
                time .sleep (OOO0O0OOOO0O0OO00 )#line:1125
            except Exception as O0O0O00O00OO0O0OO :#line:1126
                print (f"{colorama.Fore.RED}    [!] Error adding emoji '{O00O0O0O0O0000O00}' with token {O00000O0O00O00OOO}: {str(O0O0O00O00OO0O0OO)}{colorama.Fore.RESET}")#line:1127
import random #line:1129
import requests #line:1130
import time #line:1131
def pollspammer (OO0000OO0O0000OOO ,O0OOO000OOO00OO00 ,OOOOO00OOO0O0O00O ,O0O0000O000O0O000 ,OO0OO000O0O0O0OOO ,OO00O00OOOOOOOOO0 ,OO0O0OOO000O0O0O0 ,OO00O0OO00OO0OOO0 ,OOOOO00O0000O00O0 ,OO0OOO0000O0OO0O0 ,OOO0000O00OOO0O00 ):#line:1135
    O0000OO00O00OO0OO =get_session ()#line:1136
    O0OO0O0000OOOOO00 =0 #line:1137
    OOO0OO0OOO0O0000O =userget (OO0000OO0O0000OOO [0 ],O0OOO000OOO00OO00 ,OOOOO00OOO0O0O00O [0 ])#line:1139
    OOO0OO0OOO0O0000O =[OO0000O0O000000OO for OO0000O0O000000OO in OOO0OO0OOO0O0000O if OO0000O0O000000OO not in OOOOO00O0000O00O0 ]#line:1142
    for _O00OOOO0OO00OOOOO in range (OO0OOO0000O0OO0O0 ):#line:1144
        for O00OOOOO000OO0O00 in OOOOO00OOO0O0O00O :#line:1145
            OOO0O0OOO0OO0O00O =OO0000OO0O0000OOO [O0OO0O0000OOOOO00 ]#line:1146
            O00OOO00O0O00O0OO =get_headers (OOO0O0OOO0OO0O00O )#line:1147
            if OO0O0OOO000O0O0O0 and OOO0OO0OOO0O0000O :#line:1150
                OOOO0000O0O0O0O00 =random .choice (OOO0OO0OOO0O0000O )#line:1151
                OOO0OOO0OO00O000O ={"content":f"{OO00O0OO00OO0OOO0} {OOOO0000O0O0O0O00}","tts":False ,"nonce":str (random .randint (10 **17 ,10 **18 -1 ))}#line:1156
                OO000O0000O00000O =O0000OO00O00OO0OO .post (f"https://discord.com/api/v9/channels/{O00OOOOO000OO0O00}/messages",json =OOO0OOO0OO00O000O ,headers =O00OOO00O0O00O0OO )#line:1157
                if OO000O0000O00000O .status_code !=200 :#line:1158
                    print (f"Failed to send mention: {OO000O0000O00000O.status_code} - {OO000O0000O00000O.text}")#line:1159
            else :#line:1160
                OO00OO00O0OOOO00O ={"content":f"{OO00O0OO00OO0OOO0}","tts":False ,"nonce":str (random .randint (10 **17 ,10 **18 -1 ))}#line:1166
                OO0000OO0O00O00OO =O0000OO00O00OO0OO .post (f"https://discord.com/api/v9/channels/{O00OOOOO000OO0O00}/messages",json =OO00OO00O0OOOO00O ,headers =O00OOO00O0O00O0OO )#line:1167
                if OO0000OO0O00O00OO .status_code !=200 :#line:1168
                    print (f"Failed to send message: {OO0000OO0O00O00OO.status_code} - {OO0000OO0O00O00OO.text}")#line:1169
            time .sleep (OOO0000O00OOO0O00 )#line:1171
            O0O0OO0OOOOOOOO00 =[{"poll_media":{"text":O0000O0O0O0000OOO .strip ()}}for O0000O0O0O0000OOO in OO0OO000O0O0O0OOO .split (',')]#line:1174
            O00O0O0OO000O0O0O ={"mobile_network_type":"unknown","content":"","nonce":str (random .randint (10 **17 ,10 **18 -1 )),"tts":False ,"flags":0 ,"poll":{"question":{"text":O0O0000O000O0O000 },"answers":O0O0OO0OOOOOOOO00 ,"allow_multiselect":False ,"duration":OO00O00OOOOOOOOO0 ,"layout_type":1 }}#line:1188
            OO0O0OOO000000OOO =O0000OO00O00OO0OO .post (f"https://discord.com/api/v9/channels/{O00OOOOO000OO0O00}/messages",json =O00O0O0OO000O0O0O ,headers =O00OOO00O0O00O0OO )#line:1190
            if OO0O0OOO000000OOO .status_code ==200 :#line:1191
                print (f"200 poll message sent: {OOO0O0OOO0OO0O00O}")#line:1192
            elif OO0O0OOO000000OOO .status_code ==429 :#line:1193
                print (f"429 rate limit: {OOO0O0OOO0OO0O00O}")#line:1194
                O0O00O0O0OOOOO0O0 =OO0O0OOO000000OOO .json ().get ("retry_after",1 )#line:1195
                time .sleep (O0O00O0O0OOOOO0O0 )#line:1196
            elif OO0O0OOO000000OOO .status_code ==401 :#line:1197
                print (f"401 unknown token: {OOO0O0OOO0OO0O00O}")#line:1198
            else :#line:1199
                print (f"error: {OOO0O0OOO0OO0O00O} - {OO0O0OOO000000OOO.status_code}: {OO0O0OOO000000OOO.text}")#line:1200
            O0OO0O0000OOOOO00 =(O0OO0O0000OOOOO00 +1 )%len (OO0000OO0O0000OOO )#line:1202
            time .sleep (OOO0000O00OOO0O00 )#line:1203
def pollspammermenu ():#line:1206
    with open ("token.txt")as OOO0O0O0OO0O000O0 :#line:1207
        OO0O0O0000OOO0OOO =[OO00O0OO0OOOOO0OO .strip ()for OO00O0OO0OOOOO0OO in OOO0O0O0OO0O000O0 .readlines ()if OO00O0OO0OOOOO0OO .strip ()]#line:1208
    O0O00O0000OOOO0OO =input ("Enter Server ID: ").strip ()#line:1210
    OOOOO0O000OO000OO =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:1211
    if OOOOO0O000OO000OO =='2':#line:1212
        OOOOO00000O00O000 =input ("Enter Channel IDs (comma-separated): ").strip ().split (',')#line:1213
    else :#line:1214
        OOOOO00000O00O000 =[]#line:1215
        for O0OO00O0O0OO00OO0 in OO0O0O0000OOO0OOO :#line:1216
            try :#line:1217
                OOOOO00000O00O000 .extend (fetch_channels (O0OO00O0O0OO00OO0 ,O0O00O0000OOOO0OO ))#line:1218
            except Exception as O0O0O000OO0OOOOO0 :#line:1219
                print (f"[!] Failed to fetch channels for token. Error: {O0O0O000OO0OOOOO0}")#line:1220
                continue #line:1221
        random .shuffle (OOOOO00000O00O000 )#line:1222
    OOOOO0O0000O00OOO =input ("Enter poll title: ").strip ()#line:1224
    OOOO0O0O00000O00O =input ("Enter poll answers (comma-separated): ").strip ()#line:1225
    O00O00OOOO00O0OOO =int (input ("Enter poll duration (in hours 1/4/8/24/72/168/336 ): ").strip ())#line:1226
    OOO0OO00000OOOO0O =input ("Do you want to mention random users? (true/false): ").strip ().lower ()=='true'#line:1227
    OOOO0OOO0O0OO0OO0 =""#line:1228
    if OOO0OO00000OOOO0O :#line:1229
        OOOO0OOO0O0OO0OO0 =input ("Enter the message to prepend to the mention: ").strip ()#line:1230
    OO0OO0O00OOOOO0O0 =input ("Enter blacklist user IDs (comma-separated): ").strip ().split (',')#line:1231
    O0O0OO00OOO0OO0O0 =int (input ("Enter number of send poll: ").strip ())#line:1232
    OOOOOOO0O0OOO0O0O =float (input ("Enter delay between posts (in seconds): ").strip ())#line:1233
    pollspammer (OO0O0O0000OOO0OOO ,O0O00O0000OOOO0OO ,OOOOO00000O00O000 ,OOOOO0O0000O00OOO ,OOOO0O0O00000O00O ,O00O00OOOO00O0OOO ,OOO0OO00000OOOO0O ,OOOO0OOO0O0OO0OO0 ,OO0OO0O00OOOOO0O0 ,O0O0OO00OOO0OO0O0 ,OOOOOOO0O0OOO0O0O )#line:1235
def main ():#line:1238
    colorama .init ()#line:1239
    while True :#line:1240
        logo ()#line:1241
        O0O0OO0000OO0OOOO =input (f"{colorama.Fore.LIGHTMAGENTA_EX}    [Final] Select an option from above: ")#line:1242
        if O0O0OO0000OO0OOOO =="0":#line:1244
            update_group_ids ()#line:1245
        elif O0O0OO0000OO0OOOO =="1":#line:1246
            join_discord_invite ()#line:1247
        elif O0O0OO0000OO0OOOO =="2":#line:1248
            reaction_spammer ()#line:1249
        elif O0O0OO0000OO0OOOO =="3":#line:1250
            send_messages_with_mentions ()#line:1251
        elif O0O0OO0000OO0OOOO =="4":#line:1252
            spammer_menu ()#line:1253
        elif O0O0OO0000OO0OOOO =="5":#line:1254
            nickchanger ()#line:1255
        elif O0O0OO0000OO0OOOO =="6":#line:1256
            add_emojis_from_files ()#line:1257
        elif O0O0OO0000OO0OOOO =="7":#line:1258
            reaction_art ()#line:1259
        elif O0O0OO0000OO0OOOO =="8":#line:1260
            pollspammermenu ()#line:1261
        elif O0O0OO0000OO0OOOO =="0":#line:1262
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [*] Exiting the application. Goodbye!{colorama.Fore.RESET}")#line:1263
            break #line:1264
        else :#line:1265
            print (f"{colorama.Fore.RED}    [!] Invalid option selected!{colorama.Fore.RESET}")#line:1266
        input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:1268
if __name__ =="__main__":#line:1270
    main ()#line:1271
