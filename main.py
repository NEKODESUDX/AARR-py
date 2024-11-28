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
    O0O00000O000O0O0O =requests .Session ()#line:58
    if proxy :#line:59
        O0O00000O000O0O0O .proxies ={"http":proxy ,"https":proxy }#line:60
    return O0O00000O000O0O0O #line:61
def get_headers (OO0OO0000OOOO0O0O ):#line:63
    return {"Authorization":OO0OO0000OOOO0O0O ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:68
def send_message_with_mention (O00000OOOOOO0OO0O ,OO0OO000OOO00O0OO ,OOO0000000OOOO0O0 ,O0O0OO00O0OO00OO0 ):#line:71
    OO0O00O00000OOOOO =get_session ()#line:72
    O0OO0O000OO00O00O =get_headers (O00000OOOOOO0OO0O )#line:73
    if O0O0OO00O0OO00OO0 :#line:75
        OOOOO0OOO000O0O0O =random .choice (O0O0OO00O0OO00OO0 )#line:76
        OOO0000000OOOO0O0 +=f" <@{OOOOO0OOO000O0O0O}>"#line:77
    OOO0OOOOO0000O000 =OO0O00O00000OOOOO .post (f"https://discord.com/api/v9/channels/{OO0OO000OOO00O0OO}/messages",headers =O0OO0O000OO00O00O ,json ={"content":OOO0000000OOOO0O0 })#line:83
    if OOO0OOOOO0000O000 .status_code in [200 ,201 ]:#line:84
        print (f"[+] Message sent to channel {OO0OO000OOO00O0OO}")#line:85
    elif OOO0OOOOO0000O000 .status_code ==429 :#line:86
        print ("[-] Rate limited. Please wait before retrying.")#line:87
        OOO00OO0OOO00OOOO =OOO0OOOOO0000O000 .json ().get ("retry_after",1 )#line:88
        time .sleep (OOO00OO0OOO00OOOO )#line:89
    else :#line:90
        print (f"[!] Error occurred: {OOO0OOOOO0000O000.status_code}")#line:91
def fetch_messages (O0OOO00OOOO0OOOO0 ,O000O00OO0O00OO0O ,limit =100 ):#line:94
    OOO0OOO00O00OO00O ={"Authorization":O0OOO00OOOO0OOOO0 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:99
    O0OO00O000O0OO0OO =requests .get (f"https://discord.com/api/v9/channels/{O000O00OO0O00OO0O}/messages?limit={limit}",headers =OOO0OOO00O00OO00O )#line:103
    if O0OO00O000O0OO0OO .status_code ==200 :#line:104
        return O0OO00O000O0OO0OO .json ()#line:105
    else :#line:106
        print (f"[!] Failed to fetch messages. HTTP Status Code: {O0OO00O000O0OO0OO.status_code}")#line:107
        return []#line:108
import concurrent .futures #line:110
def reaction_spammer ():#line:112
    try :#line:113
        with open ("token.txt")as O00O00O0OO0OO0000 :#line:114
            OOOOOOO0OO000OO00 =[OO000O000OO0OO00O .strip ()for OO000O000OO0OO00O in O00O00O0OO0OO0000 .readlines ()if OO000O000OO0OO00O .strip ()]#line:115
    except (FileNotFoundError ,KeyError ):#line:116
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:117
        return #line:118
    O0OOOO000O0OO0OOO =input ("Server ID?: ").strip ()#line:120
    O0O0OOOO0O0OOO0O0 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:122
    if O0O0OOOO0O0OOO0O0 =='2':#line:123
        OOO00000O0OOO0O0O =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:124
        OO00OO00000OO0OOO =[O0O0OOOO0OO00O0OO .strip ()for O0O0OOOO0OO00O0OO in OOO00000O0OOO0O0O if O0O0OOOO0OO00O0OO .strip ()]#line:125
    else :#line:126
        OO00OO00000OO0OOO =[]#line:127
        for O0O0OOO000O0O0OOO in OOOOOOO0OO000OO00 :#line:128
            try :#line:129
                OO00OO00000OO0OOO .extend (fetch_channels (O0O0OOO000O0O0OOO ,O0OOOO000O0OO0OOO ))#line:130
            except Exception as OO0OOOO000O0O0OOO :#line:131
                print (f"[!] Failed to fetch channels for token. Error: {OO0OOOO000O0O0OOO}")#line:132
                continue #line:133
    OO0O0O000OOO0OOOO =input ("Select your emoji (a, b, c, ... or custom emojis): ").strip ()#line:135
    OOOOOOO0000OOOO00 =input ("Delay between reactions (in seconds)?: ").strip ()#line:136
    try :#line:138
        OOOOOOO0000OOOO00 =float (OOOOOOO0000OOOO00 )#line:139
        if OOOOOOO0000OOOO00 <0 :#line:140
            raise ValueError #line:141
    except ValueError :#line:142
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:143
        OOOOOOO0000OOOO00 =1.0 #line:144
    OOOOO0OO0O00O00O0 =[]#line:146
    for O0O0000OOOO0O0O00 in OO0O0O000OOO0OOOO .split (","):#line:147
        O0O0000OOOO0O0O00 =O0O0000OOOO0O0O00 .strip ().lower ()#line:148
        if O0O0000OOOO0O0O00 in alphabet_to_flag :#line:149
            OOOOO0OO0O00O00O0 .append (alphabet_to_flag [O0O0000OOOO0O0O00 ])#line:150
        else :#line:151
            OOOOO0OO0O00O00O0 .append (O0O0000OOOO0O0O00 )#line:152
    if not OOOOO0OO0O00O00O0 :#line:154
        print (f"{colorama.Fore.RED}    [!] No valid emojis provided!{colorama.Fore.RESET}")#line:155
        return #line:156
    def O00OOO0OOOOOOOOOO (O000OOOOOO0OO0OOO ):#line:158
        for O0OO0000O000O00OO in OO00OO00000OO0OOO :#line:159
            try :#line:160
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {O0OO0000O000O00OO}...{colorama.Fore.RESET}")#line:161
                OOO0OO00OO000O0OO =fetch_messages (O000OOOOOO0OO0OOO ,O0OO0000O000O00OO ,limit =100 )#line:162
                if not OOO0OO00OO000O0OO :#line:163
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:164
                    continue #line:165
                for O0O00OOO0OOO00O0O in OOO0OO00OO000O0OO :#line:167
                    for O000OO000O0O0OO00 in OOOOO0OO0O00O00O0 :#line:168
                        reactionput (O000OOOOOO0OO0OOO ,O0OO0000O000O00OO ,O0O00OOO0OOO00O0O ['id'],O000OO000O0O0OO00 )#line:169
                        time .sleep (OOOOOOO0000OOOO00 )#line:170
            except Exception as O0OO0OO000O0O0OO0 :#line:171
                print (f"[!] Error processing channel {O0OO0000O000O00OO}. Error: {O0OO0OO000O0O0OO0}")#line:172
                continue #line:173
    with concurrent .futures .ThreadPoolExecutor ()as O00OOO0000OO0OOO0 :#line:175
        OO0O0OOO0OOO00000 =[O00OOO0000OO0OOO0 .submit (O00OOO0OOOOOOOOOO ,O0O0O0OO000000000 )for O0O0O0OO000000000 in OOOOOOO0OO000OO00 ]#line:176
        concurrent .futures .wait (OO0O0OOO0OOO00000 )#line:177
import requests #line:180
import json #line:181
import time #line:182
import colorama #line:183
alphabet_to_flag ={'a':'🇦','b':'🇧','c':'🇨','d':'🇩','e':'🇪','f':'🇫','g':'🇬','h':'🇭','i':'🇮','j':'🇯','k':'🇰','l':'🇱','m':'🇲','n':'🇳','o':'🇴','p':'🇵','q':'🇶','r':'🇷','s':'🇸','t':'🇹','u':'🇺','v':'🇻','w':'🇼','x':'🇽','y':'🇾','z':'🇿'}#line:191
def fetch_channels (OOO0OOOOO00O0O0O0 ,OOO000OOO00OOO0OO ):#line:193
    OO0OOOO0O0OO0OOOO =f"https://discord.com/api/v9/guilds/{OOO000OOO00OOO0OO}/channels"#line:194
    O000OO000OO0000O0 ={"Authorization":OOO0OOOOO00O0O0O0 }#line:195
    O0O000O0O00OOOO0O =requests .get (OO0OOOO0O0OO0OOOO ,headers =O000OO000OO0000O0 )#line:196
    if O0O000O0O00OOOO0O .status_code ==200 :#line:197
        return [O0OO0OOO0O00OOOO0 ['id']for O0OO0OOO0O00OOOO0 in O0O000O0O00OOOO0O .json ()if O0OO0OOO0O00OOOO0 ['type']==0 ]#line:198
    else :#line:199
        raise Exception (f"Failed to fetch channels: {O0O000O0O00OOOO0O.status_code} - {O0O000O0O00OOOO0O.text}")#line:200
def fetch_messages (O00OO0OOOOOOOO0O0 ,OO00O0OOO000OOOOO ,limit =100 ):#line:202
    OOO00O0OOOOO0O0O0 =f"https://discord.com/api/v9/channels/{OO00O0OOO000OOOOO}/messages?limit={limit}"#line:203
    OOO000OOO0O00O00O ={"Authorization":O00OO0OOOOOOOO0O0 }#line:204
    OOOO00000OO00OO00 =requests .get (OOO00O0OOOOO0O0O0 ,headers =OOO000OOO0O00O00O )#line:205
    if OOOO00000OO00OO00 .status_code ==200 :#line:206
        return OOOO00000OO00OO00 .json ()#line:207
    else :#line:208
        print (f"[!] Failed to fetch messages: {OOOO00000OO00OO00.status_code} - {OOOO00000OO00OO00.text}")#line:209
        return []#line:210
def reactionput (O0O0OO00OOOO00000 ,OOO0000OO0O00000O ,O0OOO00OO00OO0OOO ,O0OOO0OOO00000O0O ):#line:212
    O00OOOO00O000OOO0 =f"https://discord.com/api/v9/channels/{OOO0000OO0O00000O}/messages/{O0OOO00OO00OO0OOO}/reactions/{O0OOO0OOO00000O0O}/@me"#line:213
    OO00000OOOOO0000O ={"Authorization":O0O0OO00OOOO00000 ,"Content-Type":"application/json"}#line:214
    O00O0OO0O0O00O00O =requests .put (O00OOOO00O000OOO0 ,headers =OO00000OOOOO0000O )#line:215
    if O00O0OO0O0O00O00O .status_code not in [204 ,200 ]:#line:216
        print (f"{colorama.Fore.RED}    [!] Failed to add reaction: {O00O0OO0O0O00O00O.status_code} - {O00O0OO0O0O00O00O.text}{colorama.Fore.RESET}")#line:217
import random #line:219
def reaction_art ():#line:221
    try :#line:222
        with open ("token.txt",encoding ="utf-8")as O000O000O0O0OO0O0 :#line:223
            OO00OO00O00O0O00O =[OOO00O0O0OOOOO000 .strip ()for OOO00O0O0OOOOO000 in O000O000O0O0OO0O0 .readlines ()if OOO00O0O0OOOOO000 .strip ()]#line:224
    except (FileNotFoundError ,KeyError ):#line:225
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:226
        return #line:227
    OOOO0OO0OO00OO0OO =input ("Server ID?: ").strip ()#line:229
    O0O00OO00000O0000 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:231
    if O0O00OO00000O0000 =='2':#line:232
        OO000O0OO000O0O00 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:233
        OOO0OOO0O00OO000O =[O00OO0OOOOOO0OOO0 .strip ()for O00OO0OOOOOO0OOO0 in OO000O0OO000O0O00 if O00OO0OOOOOO0OOO0 .strip ()]#line:234
    else :#line:235
        OOO0OOO0O00OO000O =[]#line:236
        for O0O0000O0000O0O0O in OO00OO00O00O0O00O :#line:237
            try :#line:238
                OOO0OOO0O00OO000O .extend (fetch_channels (O0O0000O0000O0O0O ,OOOO0OO0OO00OO0OO ))#line:239
            except Exception as O00OOOOO0OOOO0000 :#line:240
                print (f"[!] Failed to fetch channels for token. Error: {O00OOOOO0OOOO0000}")#line:241
                continue #line:242
        random .shuffle (OOO0OOO0O00OO000O )#line:243
    OOOO0O00O00O0OOO0 =input ("Delay between reactions (in seconds)?: ").strip ()#line:245
    try :#line:247
        OOOO0O00O00O0OOO0 =float (OOOO0O00O00O0OOO0 )#line:248
        if OOOO0O00O00O0OOO0 <0 :#line:249
            raise ValueError #line:250
    except ValueError :#line:251
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:252
        OOOO0O00O00O0OOO0 =1.0 #line:253
    try :#line:255
        with open ("art.txt",encoding ="utf-8")as O00OOOOOO000O0000 :#line:256
            O000000000O00O0OO =[O0O0O0000O0OOO0O0 .strip ()for O0O0O0000O0OOO0O0 in O00OOOOOO000O0000 .readlines ()if O0O0O0000O0OOO0O0 .strip ()]#line:257
    except (FileNotFoundError ,KeyError ):#line:258
        print (f"{colorama.Fore.RED}    [!] Error: art.txt file not found or empty!{colorama.Fore.RESET}")#line:259
        return #line:260
    except UnicodeDecodeError as O00OOOOO0OOOO0000 :#line:261
        print (f"{colorama.Fore.RED}    [!] Error decoding art.txt: {str(O00OOOOO0OOOO0000)}{colorama.Fore.RESET}")#line:262
        return #line:263
    if not O000000000O00O0OO :#line:265
        print (f"{colorama.Fore.RED}    [!] No valid art provided in art.txt!{colorama.Fore.RESET}")#line:266
        return #line:267
    O000000000O00O0OO .reverse ()#line:270
    for O0O0000O0000O0O0O in OO00OO00O00O0O00O :#line:272
        for O0OO000000O00OOOO in OOO0OOO0O00OO000O :#line:273
            try :#line:274
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {O0OO000000O00OOOO}...{colorama.Fore.RESET}")#line:275
                OOO0O0O00O0OO00OO =fetch_messages (O0O0000O0000O0O0O ,O0OO000000O00OOOO ,limit =100 )#line:278
                if not OOO0O0O00O0OO00OO :#line:279
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:280
                    continue #line:281
                for O00000O0O00OO0OO0 ,OOO0O0OOO0O0O000O in enumerate (OOO0O0O00O0OO00OO ):#line:284
                    O00O000O000O0OOOO =O000000000O00O0OO [O00000O0O00OO0OO0 %len (O000000000O00O0OO )].split (',')#line:285
                    for OO0O000O0OO0O0OOO in O00O000O000O0OOOO :#line:286
                        reactionput (O0O0000O0000O0O0O ,O0OO000000O00OOOO ,OOO0O0OOO0O0O000O ['id'],OO0O000O0OO0O0OOO .strip ())#line:287
                        print (f"Adding reaction '{OO0O000O0OO0O0OOO.strip()}' to message {OOO0O0OOO0O0O000O['id']} in channel {O0OO000000O00OOOO}")#line:288
                        time .sleep (OOOO0O00O00O0OOO0 )#line:289
            except Exception as O00OOOOO0OOOO0000 :#line:290
                print (f"[!] Error processing channel {O0OO000000O00OOOO}. Error: {O00OOOOO0OOOO0000}")#line:291
                continue #line:292
    def OOOO0O0O0O000000O (O0O0O000O00O00000 ):#line:297
        for OOOO00O0OOO00O00O in OOO0OOO0O00OO000O :#line:298
            try :#line:299
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {OOOO00O0OOO00O00O}...{colorama.Fore.RESET}")#line:300
                OOO0O00O0O00O0O0O =fetch_messages (O0O0O000O00O00000 ,OOOO00O0OOO00O00O ,limit =100 )#line:301
                if not OOO0O00O0O00O0O0O :#line:302
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:303
                    continue #line:304
                for O00000O00OO0O00O0 in OOO0O00O0O00O0O0O :#line:306
                    for O0OO00OOOOO0000O0 in O00O000O000O0OOOO :#line:307
                        reactionput (O0O0O000O00O00000 ,OOOO00O0OOO00O00O ,O00000O00OO0O00O0 ['id'],O0OO00OOOOO0000O0 )#line:308
                        time .sleep (OOOO0O00O00O0OOO0 )#line:309
            except Exception as O000000OOOO00OO00 :#line:310
                print (f"[!] Error processing channel {OOOO00O0OOO00O00O}. Error: {O000000OOOO00OO00}")#line:311
                continue #line:312
    with concurrent .futures .ThreadPoolExecutor ()as O0000O0O0O00OOOOO :#line:314
        O0OOOO0OOOOOOOO00 =[O0000O0O0O00OOOOO .submit (OOOO0O0O0O000000O ,O00OOOO000000OO0O )for O00OOOO000000OO0O in OO00OO00O00O0O00O ]#line:315
        concurrent .futures .wait (O0OOOO0OOOOOOOO00 )#line:316
def update_group_ids ():#line:319
    try :#line:320
        with open ("token.txt")as O00O0O0O0OO0O0000 :#line:321
            OOO0O0O0OOO0OO00O =[OOOOOOO0O0OO0O00O .strip ()for OOOOOOO0O0OO0O00O in O00O0O0O0OO0O0000 .readlines ()if OOOOOOO0O0OO0O00O .strip ()]#line:322
        O00OO0O000OO00O0O =OOO0O0O0OOO0OO00O [0 ]#line:323
    except (FileNotFoundError ,KeyError ):#line:324
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:325
        return #line:326
    O0O0O0OOO0OO0O000 ={"Authorization":O00OO0O000OO00O0O ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:332
    OO000000OO000O000 =requests .get ('https://discord.com/api/v9/users/@me/channels',headers =O0O0O0OOO0OO0O000 )#line:334
    if OO000000OO000O000 .status_code ==200 :#line:335
        O0OOOO0O00O0O0OOO =OO000000OO000O000 .json ()#line:336
        with open ("group_id.txt","w")as OO0O0O0OO00O00O00 :#line:337
            for OOO000O0OO0OOO0OO in O0OOOO0O00O0O0OOO :#line:338
                if OOO000O0OO0OOO0OO ['type']==3 :#line:339
                    OO0O0O0OO00O00O00 .write (OOO000O0OO0OOO0OO ['id']+'\n')#line:340
        print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Group IDs updated successfully.{colorama.Fore.RESET}")#line:341
    else :#line:342
        print (f"{colorama.Fore.LIGHTRED_EX}    [!] Failed to retrieve group IDs. HTTP Status Code: {OO000000OO000O000.status_code}{colorama.Fore.RESET}")#line:343
import requests #line:345
import requests #line:347
def fetch_channels (O0O00O0OOOO0O00OO ,OOOOO0OO0OO0OO000 ):#line:349
    try :#line:350
        O0O0000O0OOO000O0 =requests .Session ()#line:351
        OO0O00O000O0O0O0O =get_headers (O0O00O0OOOO0O00OO )#line:352
        OO0O000O00OOOO0O0 =O0O0000O0OOO000O0 .get (f"https://discord.com/api/v9/guilds/{OOOOO0OO0OO0OO000}/channels",headers =OO0O00O000O0O0O0O ,timeout =10 )#line:359
        if OO0O000O00OOOO0O0 .status_code ==200 :#line:362
            try :#line:363
                O00OOO0O00OO000O0 =OO0O000O00OOOO0O0 .json ()#line:364
                return [O000OOOO000OO00O0 ['id']for O000OOOO000OO00O0 in O00OOO0O00OO000O0 if O000OOOO000OO00O0 .get ('type')==0 ]#line:365
            except ValueError :#line:366
                print ("[!] Error: Response was not valid JSON.")#line:367
                return []#line:368
        elif OO0O000O00OOOO0O0 .status_code ==401 :#line:369
            print ("[!] Error: Unauthorized - check your token.")#line:370
        elif OO0O000O00OOOO0O0 .status_code ==403 :#line:371
            print ("[!] Error: Forbidden - you lack permissions.")#line:372
        elif OO0O000O00OOOO0O0 .status_code ==404 :#line:373
            print ("[!] Error: Server not found - check the server ID.")#line:374
        else :#line:375
            print (f"[!] Error: Unexpected status code {OO0O000O00OOOO0O0.status_code}.")#line:376
        return []#line:379
    except requests .exceptions .Timeout :#line:381
        print ("[!] Error: Request timed out. Check your connection or try again later.")#line:382
        return []#line:383
    except requests .exceptions .RequestException as OO0O0OOO0O0O00OO0 :#line:384
        print (f"[!] Error: An error occurred while fetching channels: {OO0O0OOO0O0O00OO0}")#line:385
        return []#line:386
def extract_uids_from_messages (OO00O0OO0O00OO0O0 ):#line:392
    OOOOO000O000OO00O =set ()#line:393
    for O0O0OOO0OOO0OOOOO in OO00O0OO0O00OO0O0 :#line:394
        OOOOO000O000OO00O .add (O0O0OOO0OOO0OOOOO ['author']['id'])#line:395
    return list (OOOOO000O000OO00O )#line:396
def send_message_with_mention (O0O00OOOO0OOOOOO0 ,OO000OOOOO00O0OOO ,O0O0OOO0O0OOOO00O ,OO0OOO0OOOO0O0OOO ):#line:398
    OOO000OO000OO00O0 =get_session ()#line:399
    O000000000OOOO0O0 =get_headers (O0O00OOOO0OOOOOO0 )#line:400
    if OO0OOO0OOOO0O0OOO :#line:402
        OOO0O0O00OOOO0O00 =random .choice (OO0OOO0OOOO0O0OOO )#line:403
        O0O0OOO0O0OOOO00O +=f" <@{OOO0O0O00OOOO0O00}>"#line:404
    OO0O0O00OO000O0O0 =OOO000OO000OO00O0 .post (f"https://discord.com/api/v9/channels/{OO000OOOOO00O0OOO}/messages",headers =O000000000OOOO0O0 ,json ={"content":O0O0OOO0O0OOOO00O })#line:410
    if OO0O0O00OO000O0O0 .status_code in [200 ,201 ]:#line:411
        print (f"[+] Message sent to channel {OO000OOOOO00O0OOO}")#line:412
    elif OO0O0O00OO000O0O0 .status_code ==429 :#line:413
        print ("[-] Rate limited. Please wait before retrying.")#line:414
        O0OO0O0O0O000OOOO =OO0O0O00OO000O0O0 .json ().get ("retry_after",1 )#line:415
        time .sleep (O0OO0O0O0O000OOOO )#line:416
    else :#line:417
        print (f"[!] Error occurred: {OO0O0O00OO000O0O0.status_code}")#line:418
def send_messages_with_mentions ():#line:419
    try :#line:420
        with open ("token.txt")as O0O0OO0O000O0O0OO :#line:421
            OOOO0O0OO0OO0O0OO =[O0OO00OO0O0000000 .strip ()for O0OO00OO0O0000000 in O0O0OO0O000O0O0OO .readlines ()if O0OO00OO0O0000000 .strip ()]#line:422
    except (FileNotFoundError ,KeyError ):#line:423
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:424
        return #line:425
    O000O00O000O0O0O0 =input ("Server ID?: ").strip ()#line:427
    O0OO0O00O0OOO0O00 =input ("Delay between messages (in seconds)?: ").strip ()#line:428
    O0OOO0O0OOO0OOOOO =input ("Number of messages to send?: ").strip ()#line:429
    OOO0OO00O0OO0000O =input ("Message content?: ").strip ()#line:430
    O0OO0O000OOO000OO =input ("Blacklist User IDs (comma-separated)?: ").strip ().split (',')#line:431
    O0OO0O000OOO000OO =[O0O0OOO0OO0000O00 .strip ()for O0O0OOO0OO0000O00 in O0OO0O000OOO000OO if O0O0OOO0OO0000O00 .strip ()]#line:432
    try :#line:434
        O0OO0O00O0OOO0O00 =float (O0OO0O00O0OOO0O00 )#line:435
        if O0OO0O00O0OOO0O00 <0 :#line:436
            raise ValueError #line:437
    except ValueError :#line:438
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:439
        O0OO0O00O0OOO0O00 =1.0 #line:440
    try :#line:442
        O0OOO0O0OOO0OOOOO =int (O0OOO0O0OOO0OOOOO )#line:443
        if O0OOO0O0OOO0OOOOO <=0 :#line:444
            raise ValueError #line:445
    except ValueError :#line:446
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:447
        O0OOO0O0OOO0OOOOO =1 #line:448
    OOO0O0O0OOOO00O0O =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:450
    if OOO0O0O0OOOO00O0O =='2':#line:451
        OO0000O00OOO0O00O =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:452
        OO0000O00OOO0O00O =[OO0OOOO0O0OOOOO0O .strip ()for OO0OOOO0O0OOOOO0O in OO0000O00OOO0O00O if OO0OOOO0O0OOOOO0O .strip ()]#line:453
    else :#line:454
        OO0000O00OOO0O00O =[]#line:455
    OOOOOOOOOOO00OO00 =set ()#line:457
    for O0O0OO00O000000OO in OOOO0O0OO0OO0O0OO :#line:458
        OO0O00OOO0000OOO0 =fetch_channels (O0O0OO00O000000OO ,O000O00O000O0O0O0 )#line:459
        for OOO0O0O0O0000OOOO in OO0O00OOO0000OOO0 :#line:460
            O00O000OOO00O000O =fetch_messages (O0O0OO00O000000OO ,OOO0O0O0O0000OOOO ,limit =100 )#line:461
            OO0OO0O0OOO0O0O00 =extract_uids_from_messages (O00O000OOO00O000O )#line:462
            OOOOOOOOOOO00OO00 .update (OO0OO0O0OOO0O0O00 )#line:463
    OOOOOOOOOOO00OO00 =list (set (OOOOOOOOOOO00OO00 )-set (O0OO0O000OOO000OO ))#line:466
    for _OO000OOOO00000OO0 in range (O0OOO0O0OOO0OOOOO ):#line:468
        for O0O0OO00O000000OO in OOOO0O0OO0OO0O0OO :#line:469
            if OO0000O00OOO0O00O :#line:470
                OO0O00OOO0000OOO0 =OO0000O00OOO0O00O #line:471
            for OOO0O0O0O0000OOOO in OO0O00OOO0000OOO0 :#line:472
                send_message_with_mention (O0O0OO00O000000OO ,OOO0O0O0O0000OOOO ,OOO0OO00O0OO0000O ,OOOOOOOOOOO00OO00 )#line:473
                time .sleep (O0OO0O00O0OOO0O00 )#line:474
def join_discord_invite ():#line:479
    try :#line:480
        with open ("token.txt")as O0O0O000O000000O0 :#line:481
            OOO0O00OO00OOOO00 =[OOOO0OOOOOOOO0OO0 .strip ()for OOOO0OOOOOOOO0OO0 in O0O0O000O000000O0 .readlines ()if OOOO0OOOOOOOO0OO0 .strip ()]#line:482
    except (FileNotFoundError ,KeyError ):#line:483
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:484
        return #line:485
    OOOO0OO00OOOO0OO0 =input ("Invite Code?: discord.gg/").strip ()#line:487
    for O00O0O0OOOO0OO000 in OOO0O00OO00OOOO00 :#line:490
        joiner (O00O0O0OOOO0OO000 ,OOOO0OO00OOOO0OO0 )#line:491
import json ,time ,base64 ,random ,requests #line:493
def cookieset (O0O000OOO0O000O00 ):#line:495
    O0OO0O00O0O0000OO =O0O000OOO0O000O00 .get ("https://discord.com/app")#line:496
    return O0OO0O00O0O0000OO .cookies .get_dict ()#line:497
def generatexspandua (OO0OO0OO00O0OOO00 ):#line:499
    O0OO00OO00OOO0O00 =["Android","Windows","Macintosh"]#line:500
    OOO000000O000O000 =random .choice (O0OO00OO00OOO0O00 )#line:501
    if OOO000000O000O000 =="Macintosh":#line:502
        OO0OO00OO00OO0OOO =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:503
        OOOOOOO0O0OO000O0 ="Macintosh; Intel Mac OS X "+OO0OO00OO00OO0OOO #line:504
        O00O00O000O00O0OO ="x86_64"#line:505
    elif OOO000000O000O000 =="Windows":#line:506
        OO0OO00OO00OO0OOO =f'{random.choice([6.0, 10.0, 11.0])}'#line:507
        OOOOOOO0O0OO000O0 ="Windows NT "+OO0OO00OO00OO0OOO +" Win64; x64"#line:508
        O00O00O000O00O0OO ="x86_64"#line:509
    else :#line:510
        OO0OO00OO00OO0OOO ="13"#line:511
        OOOOOOO0O0OO000O0 =f"Linux; Android 13; Pixel 6a"#line:512
        O00O00O000O00O0OO ="aarch64"#line:513
    O00O0OOO0OO0O0O0O ={"os":OOO000000O000O000 ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":OO0OO00OO00OO0OOO ,"os_arch":O00O00O000O00O0OO ,"system_locale":"ja-JP","client_build_number":OO0OO0OO00O0OOO00 ,"client_event_source":None ,"design_id":0 }#line:526
    OOO0O0O0OOOO0OOOO =f"Mozilla/5.0 ({OOOOOOO0O0OO000O0}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:527
    return base64 .b64encode (json .dumps (O00O0OOO0OO0O0O0O ,separators =(',',':')).encode ()).decode (),OOO0O0O0OOOO0OOOO #line:528
def joiner (O000OOO0O0OO00000 ,O00O00O0000O0000O ,O0OO0OOOOO0000O00 ,OOO0OO00OOOO0O000 ):#line:530
  O0000O0O0O0O00O0O =get_session (O0OO0OOOOO0000O00 )#line:531
  OOO00O0OOOO00O000 =cookieset (O0000O0O0O0O00O0O )#line:532
  OOO00O0OOOO00O000 ["locale"]="ja-JP"#line:533
  O0OO0O00OO0O000OO =201211 #line:534
  O0O0000OOO0O0OO00 ,OO0OOO0O0OO0OO00O =generatexspandua (O0OO0O00OO0O000OO )#line:535
  O0OOOOOOO0O0O0O00 ={"Authorization":O000OOO0O0OO00000 ,"accept":"*/*","accept-language":"ja-JP","connection":"keep-alive","DNT":"1","origin":"https://discord.com","sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","referer":"https://discord.com/channels/@me","TE":"Trailers","user-agent":OO0OOO0O0OO0OO00O ,"X-Super-Properties":O0O0000OOO0O0OO00 ,}#line:550
  O0O0O00O0OO00OOO0 =O0000O0O0O0O00O0O .post ("https://discord.com/api/v9/invites/"+O00O00O0000O0000O ,headers =O0OOOOOOO0O0O0O00 ,json ={},cookies =OOO00O0OOOO00O000 )#line:552
  if O0O0O00O0OO00OOO0 .status_code ==200 :#line:553
    print ("[+] Probably joined "+O000OOO0O0OO00000 )#line:554
    if "show_verification_form"in O0O0O00O0OO00OOO0 .json ():#line:555
      bypass (O000OOO0O0OO00000 ,O0O0O00O0OO00OOO0 .json ()["guild"]["id"],O0000O0O0O0O00O0O ,O0OOOOOOO0O0O0O00 )#line:556
    return #line:557
  elif "captcha_key"in O0O0O00O0OO00OOO0 .text and O0O0O00O0OO00OOO0 .status_code ==400 :#line:558
    print ("[!] Hcaptcha interference "+O000OOO0O0OO00000 )#line:559
    return #line:560
  elif O0O0O00O0OO00OOO0 .status_code ==401 :#line:561
    print ("[!] Token is dead "+O000OOO0O0OO00000 )#line:562
    return #line:563
  elif O0O0O00O0OO00OOO0 .status_code ==403 :#line:564
    if "message"in O0O0O00O0OO00OOO0 .json ():#line:565
      if O0O0O00O0OO00OOO0 .json ()["message"]=="Unknown Message":#line:566
        print ("[!] Unknown error "+O000OOO0O0OO00000 )#line:567
        return #line:568
      else :#line:569
        print ("[!] Verification required "+O000OOO0O0OO00000 )#line:570
        return #line:571
    else :#line:572
      print ("[!] Error occurred "+O000OOO0O0OO00000 )#line:573
      return #line:574
  elif O0O0O00O0OO00OOO0 .status_code ==429 :#line:575
    print ("[!] Token rate-limited "+O000OOO0O0OO00000 )#line:576
    return #line:577
  elif O0O0O00O0OO00OOO0 .status_code ==400 :#line:578
    if "captcha_key"in O0O0O00O0OO00OOO0 .json ():#line:579
      print ("[!] Hcaptcha interference "+O000OOO0O0OO00000 )#line:580
      return #line:581
    else :#line:582
      print ("[!] Error occurred "+O000OOO0O0OO00000 )#line:583
      return #line:584
  elif O0O0O00O0OO00OOO0 .status_code ==401 :#line:585
    print ("[!] Token is dead "+O000OOO0O0OO00000 )#line:586
    return #line:587
  elif O0O0O00O0OO00OOO0 .status_code ==403 :#line:588
    if "message"in O0O0O00O0OO00OOO0 .json ():#line:589
      if O0O0O00O0OO00OOO0 .json ()["message"]=="Unknown Message":#line:590
        print ("[!] Unknown error "+O000OOO0O0OO00000 )#line:591
        return #line:592
      else :#line:593
        print ("[!] Verification required "+O000OOO0O0OO00000 )#line:594
        return #line:595
    else :#line:596
      print ("[!] Error occurred "+O000OOO0O0OO00000 )#line:597
  elif O0O0O00O0OO00OOO0 .status_code ==429 :#line:598
    print ("[!] Token rate-limited "+O000OOO0O0OO00000 )#line:599
    return #line:600
  else :#line:601
    print ("[!] Error occurred "+O000OOO0O0OO00000 )#line:602
    return #line:603
def update_group_ids ():#line:606
    OO00O0OOOO0OO00OO =input ("Invite Code?: ").strip ()#line:607
    try :#line:608
        with open ("token.txt")as OOOOOOOO000O00OOO :#line:609
            O00O0O000O0O0O000 =[O0O0O0OO00OO0O000 .strip ()for O0O0O0OO00OO0O000 in OOOOOOOO000O00OOO .readlines ()if O0O0O0OO00OO0O000 .strip ()]#line:610
    except (FileNotFoundError ,KeyError ):#line:611
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:612
        return #line:613
    O000O0OO0O0OO00OO =requests .Session ()#line:615
    for O0O00O0OOO0OO0O00 in O00O0O000O0O0O000 :#line:616
        joiner (O0O00O0OOO0OO0O00 ,OO00O0OOOO0OO00OO ,O000O0OO0O0OO00OO )#line:617
        time .sleep (2 )#line:618
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:620
def bypass (O00OO0OO00O0O000O ,OOOO0OO00O000OO00 ,O00OO00OO0O0O0O0O ,OOOO0OO0000OOO00O ):#line:623
    try :#line:624
        OO0000O0000000OOO =O00OO00OO0O0O0O0O .get (f"https://discord.com/api/v9/guilds/{OOOO0OO00O000OO00}/member-verification?with_guild=false",headers =OOOO0OO0000OOO00O ).json ()#line:625
        OOO0O0O0O0O00OOOO =O00OO00OO0O0O0O0O .put (f"https://discord.com/api/v9/guilds/{OOOO0OO00O000OO00}/requests/@me",headers =OOOO0OO0000OOO00O ,json =OO0000O0000000OOO )#line:626
        if OOO0O0O0O0O00OOOO .status_code ==201 :#line:627
            print (f"[+] MemberscreeningBypassed {O00OO0OO00O0O000O}")#line:628
            return #line:629
        else :#line:630
            print (f"[!] Bypassが出来ませんでした {O00OO0OO00O0O000O}")#line:631
            return #line:632
    except Exception as OO0OOO0O0000O00O0 :#line:633
        print (f"[!] エラーが発生しました。{OO0OOO0O0000O00O0}")#line:634
session =requests .Session ()#line:636
def reactionput (O0OOO00O00O000OOO ,O000000OO0O0000O0 ,O0O00OO0OO000O0OO ,O00O00O00O00OOO00 ,proxy =None ):#line:639
    OOOOOOO00O0O0OOO0 =get_session (proxy )#line:640
    OO0O0O00OOO000OOO =get_headers (OOOOOOO00O0O0OOO0 )#line:641
    OO0O0O00OOO000OOO ["Authorization"]=O0OOO00O00O000OOO #line:642
    O00O00O00O00OOO00 =requests .utils .quote (O00O00O00O00OOO00 )#line:644
    OOOO000OOO00O00O0 =OOOOOOO00O0O0OOO0 .put (f"https://discord.com/api/v9/channels/{O000000OO0O0000O0}/messages/{O0O00OO0OO000O0OO}/reactions/{O00O00O00O00OOO00}/%40me?location=Message&type=0",headers =OO0O0O00OOO000OOO )#line:648
    if OOOO000OOO00O00O0 .status_code in [200 ,204 ]:#line:649
        print (f"[+] Reaction '{O00O00O00O00OOO00}' added successfully to message {O0O00OO0OO000O0OO}")#line:650
    elif OOOO000OOO00O00O0 .status_code ==429 :#line:651
        print ("[-] Rate limited. Please wait before retrying.")#line:652
        O000O0O00OOOO00OO =OOOO000OOO00O00O0 .json ().get ("retry_after",1 )#line:653
        time .sleep (O000O0O00OOOO00OO )#line:654
    elif OOOO000OOO00O00O0 .status_code ==401 :#line:655
        print ("[-] Invalid or expired token.")#line:656
    else :#line:657
        print (f"[!] Error occurred: {OOOO000OOO00O00O0.status_code}")#line:658
def generatexspandua (OOO00O0000OOO0O00 ):#line:661
  O0000O00O0O0O0OO0 =["Android","Windows","Macintosh"]#line:662
  OOOO0O00OOO000OO0 =random .choice (O0000O00O0O0O0OO0 )#line:663
  if OOOO0O00OOO000OO0 =="Macintosh":#line:664
    OO0O00O0O0OO0OO00 =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:665
    O0O0OO0O0OO00O00O ="Macintosh; Intel Mac OS X "+OO0O00O0O0OO0OO00 #line:666
    O0O0O00OO0O0000OO ="x86_64"#line:667
  if OOOO0O00OOO000OO0 =="Windows":#line:668
    OO0O00O0O0OO0OO00 =f'{random.choice([6.0,10.0,11.0])}'#line:669
    O0O0OO0O0OO00O00O ="Windows NT "+OO0O00O0O0OO0OO00 +" Win64; x64"#line:670
    O0O0O00OO0O0000OO ="x86_64"#line:671
  if OOOO0O00OOO000OO0 =="Android":#line:672
    OO0O00O0O0OO0OO00 ="13"#line:673
    O0O0OO0O0OO00O00O =f"Linux; Android 13; Pixel 6a"#line:674
    O0O0O00OO0O0000OO ="aarch64"#line:675
  OOOOO00000OOOO0O0 ={"os":OOOO0O00OOO000OO0 ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":OO0O00O0O0OO0OO00 ,"os_arch":O0O0O00OO0O0000OO ,"system_locale":"ja-JP","client_build_number":OOO00O0000OOO0O00 ,"client_event_source":None ,"design_id":0 }#line:676
  OOOO0OO0000OO0000 =f"Mozilla/5.0 ({O0O0OO0O0OO00O00O}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:677
  return base64 .b64encode (json .dumps (OOOOO00000OOOO0O0 ,separators =(',',':')).encode ()).decode (),OOOO0OO0000OO0000 #line:678
import base64 #line:680
def nickchanger ():#line:683
    try :#line:684
        with open ("token.txt")as O0000OO0OO0O00000 :#line:685
            OOOOOO0000000O0O0 =[OO0000OOO0000OO00 .strip ()for OO0000OOO0000OO00 in O0000OO0OO0O00000 .readlines ()if OO0000OOO0000OO00 .strip ()]#line:686
    except (FileNotFoundError ,KeyError ):#line:687
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:688
        return #line:689
    OOOO0000O000O0000 =input ("Server ID?: ").strip ()#line:691
    OOO00O00O000OO000 =input ("Nickname?: ").strip ()#line:692
    O0O000O00O0O0O000 =input ("Delay (in seconds)?: ").strip ()#line:693
    try :#line:695
        O0O000O00O0O0O000 =float (O0O000O00O0O0O000 )#line:696
        if O0O000O00O0O0O000 <0 :#line:697
            raise ValueError #line:698
    except ValueError :#line:699
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:700
        O0O000O00O0O0O000 =1.0 #line:701
    for OOOOOO000O0O0OOO0 in OOOOOO0000000O0O0 :#line:703
        O00O00O000O0000OO ={"Authorization":OOOOOO000O0O0OOO0 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:708
        O00OO00OOOO0O0O00 ={"nick":OOO00O00O000OO000 }#line:709
        OOOO00OO0OO0O0O00 =requests .patch (f"https://discord.com/api/v9/guilds/{OOOO0000O000O0000}/members/@me",headers =O00O00O000O0000OO ,json =O00OO00OOOO0O0O00 )#line:710
        if OOOO00OO0OO0O0O00 .status_code ==200 :#line:712
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Nickname changed to '{OOO00O00O000OO000}' successfully for token {OOOOOO000O0O0OOO0}.{colorama.Fore.RESET}")#line:713
        elif OOOO00OO0OO0O0O00 .status_code ==429 :#line:714
            print (f"{colorama.Fore.RED}    [!] Rate limited. Please wait before retrying for token {OOOOOO000O0O0OOO0}.{colorama.Fore.RESET}")#line:715
            OO0OOOOOO0OOO0000 =OOOO00OO0OO0O0O00 .json ().get ("retry_after",1 )#line:716
            time .sleep (OO0OOOOOO0OOO0000 )#line:717
        else :#line:718
            print (f"{colorama.Fore.RED}    [!] Error occurred: {OOOO00OO0OO0O0O00.status_code} for token {OOOOOO000O0O0OOO0}.{colorama.Fore.RESET}")#line:719
        time .sleep (O0O000O00O0O0O000 )#line:721
import json ,websocket ,threading ,tls_client ,random ,time #line:725
session =tls_client .Session (client_identifier ="chrome112",random_tls_extension_order =True )#line:727
class Utils :#line:729
    @staticmethod #line:730
    def rangeCorrector (O000O0OO0OOOOO00O ):#line:731
        if [0 ,99 ]not in O000O0OO0OOOOO00O :#line:732
            O000O0OO0OOOOO00O .insert (0 ,[0 ,99 ])#line:733
        return O000O0OO0OOOOO00O #line:734
    @staticmethod #line:736
    def getRanges (O000O0O0O0O00O00O ,O00OOO000OOOO00O0 ,O00OO0O00O00OOOOO ):#line:737
        O0O00O0O000OO0000 =int (O000O0O0O0O00O00O *O00OOO000OOOO00O0 )#line:738
        O0OOO00O0O0O00O00 =[[O0O00O0O000OO0000 ,O0O00O0O000OO0000 +99 ]]#line:739
        if O00OO0O00O00OOOOO >O0O00O0O000OO0000 +99 :#line:740
            O0OOO00O0O0O00O00 .append ([O0O00O0O000OO0000 +100 ,O0O00O0O000OO0000 +199 ])#line:741
        return Utils .rangeCorrector (O0OOO00O0O0O00O00 )#line:742
    @staticmethod #line:744
    def parseGuildMemberListUpdate (O000000O0O000OOO0 ):#line:745
        OOOOOOOOOOO000000 ={"online_count":O000000O0O000OOO0 ["d"]["online_count"],"member_count":O000000O0O000OOO0 ["d"]["member_count"],"id":O000000O0O000OOO0 ["d"]["id"],"guild_id":O000000O0O000OOO0 ["d"]["guild_id"],"hoisted_roles":O000000O0O000OOO0 ["d"]["groups"],"types":[],"locations":[],"updates":[],}#line:755
        for O000O0OO00OO000O0 in O000000O0O000OOO0 ["d"]["ops"]:#line:757
            OOOOOOOOOOO000000 ["types"].append (O000O0OO00OO000O0 ["op"])#line:758
            if O000O0OO00OO000O0 ["op"]in ("SYNC","INVALIDATE"):#line:759
                OOOOOOOOOOO000000 ["locations"].append (O000O0OO00OO000O0 ["range"])#line:760
                if O000O0OO00OO000O0 ["op"]=="SYNC":#line:761
                    OOOOOOOOOOO000000 ["updates"].append (O000O0OO00OO000O0 ["items"])#line:762
                else :#line:763
                    OOOOOOOOOOO000000 ["updates"].append ([])#line:764
            elif O000O0OO00OO000O0 ["op"]in ("INSERT","UPDATE","DELETE"):#line:765
                OOOOOOOOOOO000000 ["locations"].append (O000O0OO00OO000O0 ["index"])#line:766
                if O000O0OO00OO000O0 ["op"]=="DELETE":#line:767
                    OOOOOOOOOOO000000 ["updates"].append ([])#line:768
                else :#line:769
                    OOOOOOOOOOO000000 ["updates"].append (O000O0OO00OO000O0 ["item"])#line:770
        return OOOOOOOOOOO000000 #line:771
class DiscordSocket (websocket .WebSocketApp ):#line:773
    def __init__ (O0O0000O000O00O0O ,OOO000O0000000OOO ,OOOO0OOO0O0O0OO0O ,O0OOO0OO0O0000000 ):#line:774
        O0O0000O000O00O0O .token =OOO000O0000000OOO #line:775
        O0O0000O000O00O0O .guild_id =OOOO0OOO0O0O0OO0O #line:776
        O0O0000O000O00O0O .channel_id =O0OOO0OO0O0000000 #line:777
        O0O0000O000O00O0O .socket_headers ={"Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","Cache-Control":"no-cache","Pragma":"no-cache","Sec-WebSocket-Extensions":"permessage-deflate; client_max_window_bits","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",}#line:785
        super ().__init__ ("wss://gateway.discord.gg/?encoding=json&v=9",header =O0O0000O000O00O0O .socket_headers ,on_open =lambda OO0O0O0OO00O0O00O :O0O0000O000O00O0O .sock_open (OO0O0O0OO00O0O00O ),on_message =lambda O0O0OOO000O00OOO0 ,OO00O00O000OOO0O0 :O0O0000O000O00O0O .sock_message (O0O0OOO000O00OOO0 ,OO00O00O000OOO0O0 ),on_close =lambda OO00000OOOOO00O00 ,OO0O00OOO0000OO0O ,O00O00000O0OO00OO :O0O0000O000O00O0O .sock_close (OO00000OOOOO00O00 ,OO0O00OOO0000OO0O ,O00O00000O0OO00OO ),)#line:794
        O0O0000O000O00O0O .endScraping =False #line:796
        O0O0000O000O00O0O .guilds ={}#line:797
        O0O0000O000O00O0O .members ={}#line:798
        O0O0000O000O00O0O .ranges =[[0 ,0 ]]#line:799
        O0O0000O000O00O0O .lastRange =0 #line:800
        O0O0000O000O00O0O .packets_recv =0 #line:801
    def run (O00OOOOOOO000O0O0 ):#line:803
        O00OOOOOOO000O0O0 .run_forever ()#line:804
        return O00OOOOOOO000O0O0 .members #line:805
    def scrapeUsers (O000OO00O00OOO0O0 ):#line:807
        if not O000OO00O00OOO0O0 .endScraping :#line:808
            O000OO00O00OOO0O0 .send ('{"op":14,"d":{"guild_id":"'+O000OO00O00OOO0O0 .guild_id +'","typing":true,"activities":true,"threads":true,"channels":{"'+O000OO00O00OOO0O0 .channel_id +'":'+json .dumps (O000OO00O00OOO0O0 .ranges )+"}}}")#line:817
    def sock_open (OOO000O00O00000OO ,OO000OO00O0OOOO0O ):#line:819
        OOO000O00O00000OO .send ('{"op":2,"d":{"token":"'+OOO000O00O00000OO .token +'","capabilities":125,"properties":{"os":"Windows NT","browser":"Chrome","device":"","system_locale":"it-IT","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36","browser_version":"119.0","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":103981,"client_event_source":null},"presence":{"status":"online","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}')#line:824
    def heartbeatThread (OOO0O0O00O00O0000 ,OOO0O0O00OO0OO000 ):#line:826
        try :#line:827
            while True :#line:828
                OOO0O0O00O00O0000 .send ('{"op":1,"d":'+str (OOO0O0O00O00O0000 .packets_recv )+"}")#line:829
                time .sleep (OOO0O0O00OO0OO000 )#line:830
        except Exception as O00000OO0O0000OO0 :#line:831
            pass #line:832
    def sock_message (O0OOO0O00OO0O0O0O ,OO0O0O00OOOOOO000 ,O00OOO000000OO0O0 ):#line:834
        OO0OOOO0O00OOOOOO =json .loads (O00OOO000000OO0O0 )#line:835
        if OO0OOOO0O00OOOOOO is None :#line:836
            return #line:837
        if OO0OOOO0O00OOOOOO ["op"]!=11 :#line:838
            O0OOO0O00OO0O0O0O .packets_recv +=1 #line:839
        if OO0OOOO0O00OOOOOO ["op"]==10 :#line:840
            threading .Thread (target =O0OOO0O00OO0O0O0O .heartbeatThread ,args =(OO0OOOO0O00OOOOOO ["d"]["heartbeat_interval"]/1000 ,),daemon =True ,).start ()#line:845
        if OO0OOOO0O00OOOOOO ["t"]=="READY":#line:846
            for O0O0OOOO000OO000O in OO0OOOO0O00OOOOOO ["d"]["guilds"]:#line:847
                O0OOO0O00OO0O0O0O .guilds [O0O0OOOO000OO000O ["id"]]={"member_count":O0O0OOOO000OO000O ["member_count"]}#line:848
        if OO0OOOO0O00OOOOOO ["t"]=="READY_SUPPLEMENTAL":#line:849
            O0OOO0O00OO0O0O0O .ranges =Utils .getRanges (0 ,100 ,O0OOO0O00OO0O0O0O .guilds [O0OOO0O00OO0O0O0O .guild_id ]["member_count"])#line:852
            O0OOO0O00OO0O0O0O .scrapeUsers ()#line:853
        elif OO0OOOO0O00OOOOOO ["t"]=="GUILD_MEMBER_LIST_UPDATE":#line:854
            O00OOO0000O00OO00 =Utils .parseGuildMemberListUpdate (OO0OOOO0O00OOOOOO )#line:855
            if O00OOO0000O00OO00 ["guild_id"]==O0OOO0O00OO0O0O0O .guild_id and ("SYNC"in O00OOO0000O00OO00 ["types"]or "UPDATE"in O00OOO0000O00OO00 ["types"]):#line:859
                for OO0OOOOO0O00OOO00 ,O0OO0OO0O0OO0OOO0 in enumerate (O00OOO0000O00OO00 ["types"]):#line:860
                    if O0OO0OO0O0OO0OOO0 =="SYNC":#line:861
                        if len (O00OOO0000O00OO00 ["updates"][OO0OOOOO0O00OOO00 ])==0 :#line:862
                            O0OOO0O00OO0O0O0O .endScraping =True #line:863
                            break #line:864
                        for O00O00OO00O0000OO in O00OOO0000O00OO00 ["updates"][OO0OOOOO0O00OOO00 ]:#line:866
                            if "member"in O00O00OO00O0000OO :#line:867
                                OOOO00OO00O0OOOO0 =O00O00OO00O0000OO ["member"]#line:868
                                O000OOO0OOOO0O0O0 ={"tag":OOOO00OO00O0OOOO0 ["user"]["username"]+"#"+OOOO00OO00O0OOOO0 ["user"]["discriminator"],"id":OOOO00OO00O0OOOO0 ["user"]["id"],}#line:874
                                if not OOOO00OO00O0OOOO0 ["user"].get ("bot"):#line:875
                                    O0OOO0O00OO0O0O0O .members [OOOO00OO00O0OOOO0 ["user"]["id"]]=O000OOO0OOOO0O0O0 #line:876
                    elif O0OO0OO0O0OO0OOO0 =="UPDATE":#line:878
                        for O00O00OO00O0000OO in O00OOO0000O00OO00 ["updates"][OO0OOOOO0O00OOO00 ]:#line:879
                            if "member"in O00O00OO00O0000OO :#line:880
                                OOOO00OO00O0OOOO0 =O00O00OO00O0000OO ["member"]#line:881
                                O000OOO0OOOO0O0O0 ={"tag":OOOO00OO00O0OOOO0 ["user"]["username"]+"#"+OOOO00OO00O0OOOO0 ["user"]["discriminator"],"id":OOOO00OO00O0OOOO0 ["user"]["id"],}#line:887
                                if not OOOO00OO00O0OOOO0 ["user"].get ("bot"):#line:888
                                    O0OOO0O00OO0O0O0O .members [OOOO00OO00O0OOOO0 ["user"]["id"]]=O000OOO0OOOO0O0O0 #line:889
                    O0OOO0O00OO0O0O0O .lastRange +=1 #line:891
                    O0OOO0O00OO0O0O0O .ranges =Utils .getRanges (O0OOO0O00OO0O0O0O .lastRange ,100 ,O0OOO0O00OO0O0O0O .guilds [O0OOO0O00OO0O0O0O .guild_id ]["member_count"])#line:894
                    time .sleep (0.45 )#line:895
                    O0OOO0O00OO0O0O0O .scrapeUsers ()#line:896
            if O0OOO0O00OO0O0O0O .endScraping :#line:898
                O0OOO0O00OO0O0O0O .close ()#line:899
    def sock_close (O000OO00O0O0O0O00 ,OOOOOOO00O0OO00OO ,OO000O0O0OO000O0O ,OO00OO00O0O00O000 ):#line:901
        pass #line:902
def scrape (OOO0OOOOO0O00O00O ,OOO0O0O0O00OO0O00 ,O0O00O0OOO0OOO0OO ):#line:904
    O00OOOO0OOO00O0O0 =DiscordSocket (OOO0OOOOO0O00O00O ,OOO0O0O0O00OO0O00 ,O0O00O0OOO0OOO0OO )#line:905
    return O00OOOO0OOO00O0O0 .run ()#line:906
def member_scrape (OOOO0O0000O000O00 ,O0000O0O000O0O0O0 ,O000O0O0OOO0OO00O ):#line:908
    O0O0O00O0OO0OOOO0 =[]#line:909
    for O00O00OOO0O0OO0O0 in OOOO0O0000O000O00 :#line:910
        OOO00OOO0O0OOOO00 ={"Authorization":O00O00OOO0O0OO0O0 ,"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}#line:911
        OO000000OO0O00O0O =session .get (f"https://canary.discord.com/api/v9/guilds/{O0000O0O000O0O0O0}",headers =OOO00OOO0O0OOOO00 )#line:912
        if OO000000OO0O00O0O .status_code ==200 :#line:913
            O0O0O00O0OO0OOOO0 .append (O00O00OOO0O0OO0O0 )#line:914
            break #line:915
    if not O0O0O00O0OO0OOOO0 :#line:916
        print ("missing access")#line:917
    O00O00OOO0O0OO0O0 =random .choice (O0O0O00O0OO0OOOO0 )#line:919
    OO0O0O0O0OOOO00OO =scrape (O00O00OOO0O0OO0O0 ,O0000O0O000O0O0O0 ,O000O0O0OOO0OO00O )#line:920
    OOOO0O0O0OOO00O0O =[f"<@{O000000OO0O0OOOO0}>"for O000000OO0O0OOOO0 in [int (O00OOOO0O00OOO000 )for O00OOOO0O00OOO000 in OO0O0O0O0OOOO00OO .keys ()]]#line:921
    print (f"[SUCCESS] {len(OOOO0O0O0OOO00O0O)} scraped members")#line:922
    return OOOO0O0O0OOO00O0O #line:923
def spammer_menu ():#line:925
    try :#line:926
        with open ("token.txt")as O0OOOOO0OOO00O000 :#line:927
            O0O00O0O0O00O00OO =[O00O00O00OOOO00O0 .strip ()for O00O00O00OOOO00O0 in O0OOOOO0OOO00O000 .readlines ()if O00O00O00OOOO00O0 .strip ()]#line:928
    except (FileNotFoundError ,KeyError ):#line:929
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:930
        return #line:931
    OO00OO0O0OOO0O0O0 =input ("Server ID?: ").strip ()#line:933
    O00OO000OOO0OOO0O =input ("Message?: ").strip ()#line:934
    OOO00OOOO0O00O000 =input ("Random mention (True/False)?: ").strip ().lower ()=='true'#line:935
    O000000O0OO00OOOO =input ("Delay between messages (in seconds)?: ").strip ()#line:936
    OOOOOOOOO000O0OOO =input ("Number of messages to send?: ").strip ()#line:937
    O000O0O00OOO00OO0 =input ("Blacklist User IDs (comma-separated) (Leave blank to skip)?: ").strip ().split (',')#line:938
    O000O0O00OOO00OO0 =[f"<@{O0O0OOO0O00O00O0O.strip()}>"for O0O0OOO0O00O00O0O in O000O0O00OOO00OO0 if O0O0OOO0O00O00O0O .strip ()]#line:939
    try :#line:941
        O000000O0OO00OOOO =float (O000000O0OO00OOOO )#line:942
        if O000000O0OO00OOOO <0 :#line:943
            raise ValueError #line:944
    except ValueError :#line:945
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:946
        O000000O0OO00OOOO =1.0 #line:947
    try :#line:949
        OOOOOOOOO000O0OOO =int (OOOOOOOOO000O0OOO )#line:950
        if OOOOOOOOO000O0OOO <=0 :#line:951
            raise ValueError #line:952
    except ValueError :#line:953
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:954
        OOOOOOOOO000O0OOO =1 #line:955
    O0OO0OO0OOO00O0OO =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:957
    if O0OO0OO0OOO00O0OO =='2':#line:958
        OOO000O0OOOOO0OOO =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:959
        OOO000O0OOOOO0OOO =[OOO0OOO000O0OO000 .strip ()for OOO0OOO000O0OO000 in OOO000O0OOOOO0OOO if OOO0OOO000O0OO000 .strip ()]#line:960
    else :#line:961
        OOO000O0OOOOO0OOO =fetch_channels (O0O00O0O0O00O00OO [0 ],OO00OO0O0OOO0O0O0 )#line:962
    O0OOOO00O0000O000 =None #line:964
    spammer (O0O00O0O0O00O00OO ,OO00OO0O0OOO0O0O0 ,OOO000O0OOOOO0OOO ,O00OO000OOO0OOO0O ,OOO00OOOO0O00O000 ,O000O0O00OOO00OO0 ,O0OOOO00O0000O000 ,OOOOOOOOO000O0OOO )#line:966
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:969
def buildnumget (OO000O0OOOOO00OO0 ):#line:971
  OOOO00O000000OOO0 =OO000O0OOOOO00OO0 .get ('https://discord.com/login',headers ={'Accept-Encoding':'gzip, deflate'},timeout =7 )#line:972
  OO00O0OO0OO0OO00O =OOOO00O000000OOO0 .text #line:973
import discum #line:975
import random #line:976
import time #line:977
def userget (OOOOO0O0O00O00O0O ,O0O0000000000OO0O ,O0OOOO0000O0OOO00 ):#line:979
    O0OO0OOOO000OOO00 =[]#line:980
    OO0OO00O0OO0000O0 =discum .Client (token =OOOOO0O0O00O00O0O ,log =False )#line:981
    def O000OOO0OOOOO00OO (O0O000OOOO0OO0OO0 ):#line:983
        if OO0OO00O0OO0000O0 .gateway .finishedMemberFetching (O0O0000000000OO0O ):#line:984
            OO000O00O00OOOO0O =len (OO0OO00O0OO0000O0 .gateway .session .guild (O0O0000000000OO0O ).members )#line:985
            print (str (OO000O00O00OOOO0O )+' members fetched')#line:986
            OO0OO00O0OO0000O0 .gateway .removeCommand ({'function':O000OOO0OOOOO00OO ,'params':{}})#line:987
            OO0OO00O0OO0000O0 .gateway .close ()#line:988
    def OO0OOOOO00000OO00 (O000O0OO00O0O0000 ,OO0OOO0OOO0OOO0OO ):#line:990
        OO0OO00O0OO0000O0 .gateway .fetchMembers (O000O0OO00O0O0000 ,OO0OOO0OOO0OOO0OO ,keep ='all',wait =1 )#line:991
        OO0OO00O0OO0000O0 .gateway .command ({'function':O000OOO0OOOOO00OO ,'params':{}})#line:992
        OO0OO00O0OO0000O0 .gateway .run ()#line:993
        OO0OO00O0OO0000O0 .gateway .resetSession ()#line:994
        return OO0OO00O0OO0000O0 .gateway .session .guild (O000O0OO00O0O0000 ).members #line:995
    OOOO0000O00000OOO =OO0OOOOO00000OO00 (O0O0000000000OO0O ,O0OOOO0000O0OOO00 )#line:997
    for OO0O000OO000O00OO in OOOO0000O00000OOO :#line:998
        if OO0O000OO000O00OO not in O0OO0OOOO000OOO00 :#line:999
            O0OO0OOOO000OOO00 .append (f"<@{OO0O000OO000O00OO}>")#line:1000
    return O0OO0OOOO000OOO00 #line:1001
def spammer (O00O00000O00OO0OO ,O0O0O000OO0O0OOO0 ,O0OOOO0000O0OO00O ,O0OOOOO00OOO0OO00 ,OOO000O000OO000OO ,OOO0O0OO00OOO00OO ,O00O0O0O0OOO0O0OO ,OOO000OOOO0OO0O00 ):#line:1006
    O0OO00OO000OO0OOO =get_session (O00O0O0O0OOO0O0OO )#line:1007
    O000OOOOO000O0000 =0 #line:1008
    OOOOO000O0OOO0OOO =userget (O00O00000O00OO0OO [0 ],O0O0O000OO0O0OOO0 ,O0OOOO0000O0OO00O [0 ])#line:1010
    OOOOO000O0OOO0OOO =[O00000OO00OO0O0O0 for O00000OO00OO0O0O0 in OOOOO000O0OOO0OOO if O00000OO00OO0O0O0 not in OOO0O0OO00OOO00OO ]#line:1013
    for _OOOOOO0O0O000OOOO in range (OOO000OOOO0OO0O00 ):#line:1015
        OO0O00OOOOO0OOO00 =O00O00000O00OO0OO [O000OOOOO000O0000 ]#line:1016
        O0OO0OO00O00O00O0 =get_headers (OO0O00OOOOO0OOO00 )#line:1017
        for O00OO00OO0O00OOO0 in O0OOOO0000O0OO00O :#line:1018
            OOO0000OO0OOO00OO =O0OOOOO00OOO0OO00 #line:1019
            if OOO000O000OO000OO and OOOOO000O0OOO0OOO :#line:1020
                O00OOO000000O0O00 =random .choice (OOOOO000O0OOO0OOO )#line:1021
                OOO0000OO0OOO00OO +=f" {O00OOO000000O0O00}"#line:1022
            O0OO000O00OO0O0O0 =O0OO00OO000OO0OOO .post (f"https://discord.com/api/v9/channels/{O00OO00OO0O00OOO0}/messages",json ={"content":OOO0000OO0OOO00OO },headers =O0OO0OO00O00O00O0 )#line:1024
            if O0OO000O00OO0O0O0 .status_code ==200 :#line:1025
                print (f"200 message sent: {OO0O00OOOOO0OOO00}")#line:1026
            elif O0OO000O00OO0O0O0 .status_code ==429 :#line:1027
                print (f"429 rate limit: {OO0O00OOOOO0OOO00}")#line:1028
                O00O0O000OO0O0OO0 =O0OO000O00OO0O0O0 .json ().get ("retry_after",1 )#line:1029
                time .sleep (O00O0O000OO0O0OO0 )#line:1030
            elif O0OO000O00OO0O0O0 .status_code ==401 :#line:1031
                print (f"401 unknown token: {OO0O00OOOOO0OOO00}")#line:1032
            else :#line:1033
                print (f"error: {OO0O00OOOOO0OOO00}")#line:1034
        O000OOOOO000O0000 =(O000OOOOO000O0000 +1 )%len (O00O00000O00OO0OO )#line:1036
        time .sleep (1 )#line:1037
import requests #line:1041
import base64 #line:1042
import colorama #line:1043
import time #line:1044
def add_emojis_from_files ():#line:1046
    try :#line:1047
        with open ("emojiname.txt")as OOOO0OOOO000O0O0O ,open ("emojiurl.txt")as O0OOO00OO0000OOO0 :#line:1048
            O0OOO0OOOOOOO0OO0 =[OO0O0O0O0OO000O00 .strip ()for OO0O0O0O0OO000O00 in OOOO0OOOO000O0O0O .read ().split (',')if OO0O0O0O0OO000O00 .strip ()]#line:1049
            O0000000O0O00O00O =[O000O0OOOO0OO0O00 .strip ()for O000O0OOOO0OO0O00 in O0OOO00OO0000OOO0 .read ().split (',')if O000O0OOOO0OO0O00 .strip ()]#line:1050
    except FileNotFoundError as O0OO0OOOOO0OOOO0O :#line:1051
        print (f"{colorama.Fore.RED}    [!] Error: {str(O0OO0OOOOO0OOOO0O)}{colorama.Fore.RESET}")#line:1052
        return #line:1053
    if len (O0OOO0OOOOOOO0OO0 )!=len (O0000000O0O00O00O ):#line:1055
        print (f"{colorama.Fore.RED}    [!] Error: The number of emoji names and URLs do not match!{colorama.Fore.RESET}")#line:1056
        return #line:1057
    try :#line:1059
        with open ("token.txt")as O0OOOOOOO000000O0 :#line:1060
            OOO000OOOO0000OO0 =[OO000000O0OOOO0O0 .strip ()for OO000000O0OOOO0O0 in O0OOOOOOO000000O0 .readlines ()if OO000000O0OOOO0O0 .strip ()]#line:1061
    except FileNotFoundError as O0OO0OOOOO0OOOO0O :#line:1062
        print (f"{colorama.Fore.RED}    [!] Error: {str(O0OO0OOOOO0OOOO0O)}{colorama.Fore.RESET}")#line:1063
        return #line:1064
    O00OO0OOO0O0OOOOO =input ("Enter the Guild ID: ").strip ()#line:1066
    OOO00OO0OO0O00O0O =input ("Enter the rate limit between requests (in seconds): ").strip ()#line:1067
    try :#line:1069
        OOO00OO0OO0O00O0O =float (OOO00OO0OO0O00O0O )#line:1070
        if OOO00OO0OO0O00O0O <0 :#line:1071
            raise ValueError #line:1072
    except ValueError :#line:1073
        print (f"{colorama.Fore.RED}    [!] Invalid rate limit. Using default rate limit of 5 seconds.{colorama.Fore.RESET}")#line:1074
        OOO00OO0OO0O00O0O =5.0 #line:1075
    O00OO00OOOOOO00OO =set ()#line:1077
    for OO0O00O0O0O0O0O00 in OOO000OOOO0000OO0 :#line:1079
        O00O0OO0O00OO00O0 ={'Authorization':OO0O00O0O0O0O0O00 ,'Content-Type':'application/json'}#line:1083
        O00O0000OOO00O00O =requests .get (f"https://discord.com/api/v9/guilds/{O00OO0OOO0O0OOOOO}/emojis",headers =O00O0OO0O00OO00O0 )#line:1086
        if O00O0000OOO00O00O .status_code ==200 :#line:1087
            OOOO000O0OOO0O00O =O00O0000OOO00O00O .json ()#line:1088
            for OO0O0O0O00OOO000O in OOOO000O0OOO0O00O :#line:1089
                O00OO00OOOOOO00OO .add (OO0O0O0O00OOO000O ['name'])#line:1090
        else :#line:1091
            print (f"{colorama.Fore.RED}    [!] Error fetching existing emojis: {O00O0000OOO00O00O.status_code} - {O00O0000OOO00O00O.text}{colorama.Fore.RESET}")#line:1092
            continue #line:1093
    for OO0O0OO0OOOO0OO00 ,O000O0000OO00000O in zip (O0OOO0OOOOOOO0OO0 ,O0000000O0O00O00O ):#line:1095
        if OO0O0OO0OOOO0OO00 in O00OO00OOOOOO00OO :#line:1096
            print (f"{colorama.Fore.YELLOW}    [*] Emoji '{OO0O0OO0OOOO0OO00}' already exists. Skipping...{colorama.Fore.RESET}")#line:1097
            continue #line:1098
        for OO0O00O0O0O0O0O00 in OOO000OOOO0000OO0 :#line:1100
            try :#line:1101
                O00O0000OOO00O00O =requests .get (O000O0000OO00000O )#line:1102
                O00O0000OOO00O00O .raise_for_status ()#line:1103
                O0O000O000OO000O0 =O00O0000OOO00O00O .content #line:1104
                OO000O00O0OOO0OOO =base64 .b64encode (O0O000O000OO000O0 ).decode ('utf-8')#line:1105
                O00OOOOO0OO000OO0 ={'name':OO0O0OO0OOOO0OO00 ,'image':f"data:image/png;base64,{OO000O00O0OOO0OOO}"}#line:1110
                O00O0OO0O00OO00O0 ={'Authorization':OO0O00O0O0O0O0O00 ,'Content-Type':'application/json'}#line:1115
                OOO00O000O00O00O0 =requests .post (f"https://discord.com/api/v9/guilds/{O00OO0OOO0O0OOOOO}/emojis",headers =O00O0OO0O00OO00O0 ,json =O00OOOOO0OO000OO0 )#line:1117
                if OOO00O000O00O00O0 .status_code ==201 :#line:1118
                    print (f"{colorama.Fore.GREEN}    [+] Successfully added emoji '{OO0O0OO0OOOO0OO00}' with token {OO0O00O0O0O0O0O00}{colorama.Fore.RESET}")#line:1119
                    O00OO00OOOOOO00OO .add (OO0O0OO0OOOO0OO00 )#line:1120
                    break #line:1121
                else :#line:1122
                    print (f"{colorama.Fore.RED}    [!] Failed to add emoji '{OO0O0OO0OOOO0OO00}' with token {OO0O00O0O0O0O0O00}: {OOO00O000O00O00O0.status_code} - {OOO00O000O00O00O0.text}{colorama.Fore.RESET}")#line:1123
                time .sleep (OOO00OO0OO0O00O0O )#line:1125
            except Exception as O0OO0OOOOO0OOOO0O :#line:1126
                print (f"{colorama.Fore.RED}    [!] Error adding emoji '{OO0O0OO0OOOO0OO00}' with token {OO0O00O0O0O0O0O00}: {str(O0OO0OOOOO0OOOO0O)}{colorama.Fore.RESET}")#line:1127
import random #line:1129
import requests #line:1130
import time #line:1131
def pollspammer (O000OOOO0OOOOOOO0 ,O0000O0OOO0O000O0 ,O0OOO00000O00O0OO ,OO0O0O00OOO0O00OO ,O0OOO0OO00000000O ,O00O00O0O0000000O ,OO0O000OOOO0OO0O0 ,OOO0OO000OO00OOOO ,OO0O0OO00000000O0 ,O00OO00OO00OOO00O ,OOOO0O0O000OO00OO ):#line:1134
    O0O000OOO00000OO0 =get_session ()#line:1135
    O0000OOO00OO000OO =0 #line:1136
    O00000OO0OOO000OO =userget (O000OOOO0OOOOOOO0 [0 ],O0000O0OOO0O000O0 ,O0OOO00000O00O0OO [0 ])#line:1138
    O00000OO0OOO000OO =[O0O0O000OOO0O00OO for O0O0O000OOO0O00OO in O00000OO0OOO000OO if O0O0O000OOO0O00OO not in OO0O0OO00000000O0 ]#line:1141
    for _OOOOOO00OOO000OO0 in range (O00OO00OO00OOO00O ):#line:1143
        for O00OO000OOOO0OOO0 in O0OOO00000O00O0OO :#line:1144
            OOO0OOOO00OOO00OO =O000OOOO0OOOOOOO0 [O0000OOO00OO000OO ]#line:1145
            OOO0OOO0000OOOOO0 =get_headers (OOO0OOOO00OOO00OO )#line:1146
            if OO0O000OOOO0OO0O0 and O00000OO0OOO000OO :#line:1149
                O0O0O00OO00OO0OOO =random .choice (O00000OO0OOO000OO )#line:1150
                O000O00OOOO0OO00O ={"content":f"{OOO0OO000OO00OOOO} {O0O0O00OO00OO0OOO}","tts":False ,"nonce":str (random .randint (10 **17 ,10 **18 -1 ))}#line:1155
                OO0OOO00O00O00OOO =O0O000OOO00000OO0 .post (f"https://discord.com/api/v9/channels/{O00OO000OOOO0OOO0}/messages",json =O000O00OOOO0OO00O ,headers =OOO0OOO0000OOOOO0 )#line:1156
                if OO0OOO00O00O00OOO .status_code !=200 :#line:1157
                    print (f"Failed to send mention: {OO0OOO00O00O00OOO.status_code} - {OO0OOO00O00O00OOO.text}")#line:1158
            OO000OOO0000OO0OO =[{"poll_media":{"text":O0O0O000OOOO0O0O0 .strip ()}}for O0O0O000OOOO0O0O0 in O0OOO0OO00000000O .split (',')]#line:1160
            OOO0OO00O00O0O00O ={"mobile_network_type":"unknown","content":"","nonce":str (random .randint (10 **17 ,10 **18 -1 )),"tts":False ,"flags":0 ,"poll":{"question":{"text":OO0O0O00OOO0O00OO },"answers":OO000OOO0000OO0OO ,"allow_multiselect":False ,"duration":O00O00O0O0000000O ,"layout_type":1 }}#line:1174
            O0OOOO0O00O0OOO0O =O0O000OOO00000OO0 .post (f"https://discord.com/api/v9/channels/{O00OO000OOOO0OOO0}/messages",json =OOO0OO00O00O0O00O ,headers =OOO0OOO0000OOOOO0 )#line:1176
            if O0OOOO0O00O0OOO0O .status_code ==200 :#line:1177
                print (f"200 poll message sent: {OOO0OOOO00OOO00OO}")#line:1178
            elif O0OOOO0O00O0OOO0O .status_code ==429 :#line:1179
                print (f"429 rate limit: {OOO0OOOO00OOO00OO}")#line:1180
                OO00OO0O000OO0O0O =O0OOOO0O00O0OOO0O .json ().get ("retry_after",1 )#line:1181
                time .sleep (OO00OO0O000OO0O0O )#line:1182
            elif O0OOOO0O00O0OOO0O .status_code ==401 :#line:1183
                print (f"401 unknown token: {OOO0OOOO00OOO00OO}")#line:1184
            else :#line:1185
                print (f"error: {OOO0OOOO00OOO00OO} - {O0OOOO0O00O0OOO0O.status_code}: {O0OOOO0O00O0OOO0O.text}")#line:1186
            O0000OOO00OO000OO =(O0000OOO00OO000OO +1 )%len (O000OOOO0OOOOOOO0 )#line:1188
            time .sleep (OOOO0O0O000OO00OO )#line:1189
def pollspammermenu ():#line:1192
    with open ("token.txt")as O0O00O00OO0O0O00O :#line:1193
        OOO0OO00OO0OOO000 =[O0O000000OOO0O0OO .strip ()for O0O000000OOO0O0OO in O0O00O00OO0O0O00O .readlines ()if O0O000000OOO0O0OO .strip ()]#line:1194
    OO0O00OO0O00O00O0 =input ("Enter Server ID: ").strip ()#line:1196
    OO0OOO00O00000O0O =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:1197
    if OO0OOO00O00000O0O =='2':#line:1198
        OO0O0O0OO0O00OO00 =input ("Enter Channel IDs (comma-separated): ").strip ().split (',')#line:1199
    else :#line:1200
        OO0O0O0OO0O00OO00 =[]#line:1201
        for OO0000OOOOO0O00OO in OOO0OO00OO0OOO000 :#line:1202
            try :#line:1203
                OO0O0O0OO0O00OO00 .extend (fetch_channels (OO0000OOOOO0O00OO ,OO0O00OO0O00O00O0 ))#line:1204
            except Exception as O0O00OO0OO0O00000 :#line:1205
                print (f"[!] Failed to fetch channels for token. Error: {O0O00OO0OO0O00000}")#line:1206
                continue #line:1207
        random .shuffle (OO0O0O0OO0O00OO00 )#line:1208
    OO00OOOOOO000O0O0 =input ("Enter poll title: ").strip ()#line:1210
    OO0OOO00O0000O000 =input ("Enter poll answers (comma-separated): ").strip ()#line:1211
    O000OO0O0O00OOOOO =int (input ("Enter poll duration (in hours 1/4/8/24/72/168/336 ): ").strip ())#line:1212
    OO0O0OOOO0OO0O00O =input ("Do you want to mention random users? (true/false): ").strip ().lower ()=='true'#line:1213
    O0O0O00OO0O0O000O =""#line:1214
    if OO0O0OOOO0OO0O00O :#line:1215
        O0O0O00OO0O0O000O =input ("Enter the message to prepend to the mention: ").strip ()#line:1216
    O000O0OOO0OO0O0OO =input ("Enter blacklist user IDs (comma-separated): ").strip ().split (',')#line:1217
    OO0OO0OOOOO0OOO0O =int (input ("Enter number of send poll: ").strip ())#line:1218
    OOO0O0O0OO0000O00 =float (input ("Enter delay between posts (in seconds): ").strip ())#line:1219
    pollspammer (OOO0OO00OO0OOO000 ,OO0O00OO0O00O00O0 ,OO0O0O0OO0O00OO00 ,OO00OOOOOO000O0O0 ,OO0OOO00O0000O000 ,O000OO0O0O00OOOOO ,OO0O0OOOO0OO0O00O ,O0O0O00OO0O0O000O ,O000O0OOO0OO0O0OO ,OO0OO0OOOOO0OOO0O ,OOO0O0O0OO0000O00 )#line:1221
def main ():#line:1224
    colorama .init ()#line:1225
    while True :#line:1226
        logo ()#line:1227
        O0OO0OOOOOOOO0O00 =input (f"{colorama.Fore.LIGHTMAGENTA_EX}    [Final] Select an option from above: ")#line:1228
        if O0OO0OOOOOOOO0O00 =="0":#line:1230
            update_group_ids ()#line:1231
        elif O0OO0OOOOOOOO0O00 =="1":#line:1232
            join_discord_invite ()#line:1233
        elif O0OO0OOOOOOOO0O00 =="2":#line:1234
            reaction_spammer ()#line:1235
        elif O0OO0OOOOOOOO0O00 =="3":#line:1236
            send_messages_with_mentions ()#line:1237
        elif O0OO0OOOOOOOO0O00 =="4":#line:1238
            spammer_menu ()#line:1239
        elif O0OO0OOOOOOOO0O00 =="5":#line:1240
            nickchanger ()#line:1241
        elif O0OO0OOOOOOOO0O00 =="6":#line:1242
            add_emojis_from_files ()#line:1243
        elif O0OO0OOOOOOOO0O00 =="7":#line:1244
            reaction_art ()#line:1245
        elif O0OO0OOOOOOOO0O00 =="8":#line:1246
            pollspammermenu ()#line:1247
        elif O0OO0OOOOOOOO0O00 =="0":#line:1248
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [*] Exiting the application. Goodbye!{colorama.Fore.RESET}")#line:1249
            break #line:1250
        else :#line:1251
            print (f"{colorama.Fore.RED}    [!] Invalid option selected!{colorama.Fore.RESET}")#line:1252
        input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:1254
if __name__ =="__main__":#line:1256
    main ()#line:1257
