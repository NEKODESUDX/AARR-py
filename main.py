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
    OOOO00OO000O0OO00 =requests .Session ()#line:57
    if proxy :#line:58
        OOOO00OO000O0OO00 .proxies ={"http":proxy ,"https":proxy }#line:59
    return OOOO00OO000O0OO00 #line:60
def get_headers (OO000O0000O00OOO0 ):#line:62
    return {"Authorization":OO000O0000O00OOO0 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:67
def send_message_with_mention (OOO0OOOO0000O0OOO ,O00O000000OO0O0O0 ,O0OOOOO0O0O0O0OO0 ,OO0OO00OO0OO0O000 ):#line:70
    OO00O00O0O00O0OOO =get_session ()#line:71
    O0O0O000O0000OOO0 =get_headers (OOO0OOOO0000O0OOO )#line:72
    if OO0OO00OO0OO0O000 :#line:74
        OOO0O0OO0000O0O00 =random .choice (OO0OO00OO0OO0O000 )#line:75
        O0OOOOO0O0O0O0OO0 +=f" <@{OOO0O0OO0000O0O00}>"#line:76
    OO00000OOO00O00O0 =OO00O00O0O00O0OOO .post (f"https://discord.com/api/v9/channels/{O00O000000OO0O0O0}/messages",headers =O0O0O000O0000OOO0 ,json ={"content":O0OOOOO0O0O0O0OO0 })#line:82
    if OO00000OOO00O00O0 .status_code in [200 ,201 ]:#line:83
        print (f"[+] Message sent to channel {O00O000000OO0O0O0}")#line:84
    elif OO00000OOO00O00O0 .status_code ==429 :#line:85
        print ("[-] Rate limited. Please wait before retrying.")#line:86
        OOO00O0O000OOO00O =OO00000OOO00O00O0 .json ().get ("retry_after",1 )#line:87
        time .sleep (OOO00O0O000OOO00O )#line:88
    else :#line:89
        print (f"[!] Error occurred: {OO00000OOO00O00O0.status_code}")#line:90
def fetch_messages (OO00O000000O000O0 ,OO0000000O00000OO ,limit =100 ):#line:93
    O0O00O0O0O0O0O0OO ={"Authorization":OO00O000000O000O0 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:98
    O00OO0O00OOO0OO0O =requests .get (f"https://discord.com/api/v9/channels/{OO0000000O00000OO}/messages?limit={limit}",headers =O0O00O0O0O0O0O0OO )#line:102
    if O00OO0O00OOO0OO0O .status_code ==200 :#line:103
        return O00OO0O00OOO0OO0O .json ()#line:104
    else :#line:105
        print (f"[!] Failed to fetch messages. HTTP Status Code: {O00OO0O00OOO0OO0O.status_code}")#line:106
        return []#line:107
import concurrent .futures #line:109
def reaction_spammer ():#line:111
    try :#line:112
        with open ("token.txt")as O0OOO0OO0O0OOOOOO :#line:113
            O000O00OOOO00O00O =[OO0OO00000OOO0OO0 .strip ()for OO0OO00000OOO0OO0 in O0OOO0OO0O0OOOOOO .readlines ()if OO0OO00000OOO0OO0 .strip ()]#line:114
    except (FileNotFoundError ,KeyError ):#line:115
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:116
        return #line:117
    OO00O0000O00000OO =input ("Server ID?: ").strip ()#line:119
    O0000O0O0000OO0O0 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:121
    if O0000O0O0000OO0O0 =='2':#line:122
        O0O0O0OOO000O0000 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:123
        OO0OO0OOO0OO0O0OO =[OOO00OO0O00O0OO00 .strip ()for OOO00OO0O00O0OO00 in O0O0O0OOO000O0000 if OOO00OO0O00O0OO00 .strip ()]#line:124
    else :#line:125
        OO0OO0OOO0OO0O0OO =[]#line:126
        for OO0OOO0OO0O0OOOOO in O000O00OOOO00O00O :#line:127
            try :#line:128
                OO0OO0OOO0OO0O0OO .extend (fetch_channels (OO0OOO0OO0O0OOOOO ,OO00O0000O00000OO ))#line:129
            except Exception as O0OOO000O0000OOOO :#line:130
                print (f"[!] Failed to fetch channels for token. Error: {O0OOO000O0000OOOO}")#line:131
                continue #line:132
    O0000OOO0OO000OOO =input ("Select your emoji (a, b, c, ... or custom emojis): ").strip ()#line:134
    O0O000OOO0OO0OOO0 =input ("Delay between reactions (in seconds)?: ").strip ()#line:135
    try :#line:137
        O0O000OOO0OO0OOO0 =float (O0O000OOO0OO0OOO0 )#line:138
        if O0O000OOO0OO0OOO0 <0 :#line:139
            raise ValueError #line:140
    except ValueError :#line:141
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:142
        O0O000OOO0OO0OOO0 =1.0 #line:143
    OO0OOOO000O000O00 =[]#line:145
    for O0OOO0OOOO00000OO in O0000OOO0OO000OOO .split (","):#line:146
        O0OOO0OOOO00000OO =O0OOO0OOOO00000OO .strip ().lower ()#line:147
        if O0OOO0OOOO00000OO in alphabet_to_flag :#line:148
            OO0OOOO000O000O00 .append (alphabet_to_flag [O0OOO0OOOO00000OO ])#line:149
        else :#line:150
            OO0OOOO000O000O00 .append (O0OOO0OOOO00000OO )#line:151
    if not OO0OOOO000O000O00 :#line:153
        print (f"{colorama.Fore.RED}    [!] No valid emojis provided!{colorama.Fore.RESET}")#line:154
        return #line:155
    def OOO0O0OOOOOO0O00O (O000OO0OOO0OO00OO ):#line:157
        for O0OOOOO00OO00O0OO in OO0OO0OOO0OO0O0OO :#line:158
            try :#line:159
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {O0OOOOO00OO00O0OO}...{colorama.Fore.RESET}")#line:160
                OOO0OO0O00O0OOO00 =fetch_messages (O000OO0OOO0OO00OO ,O0OOOOO00OO00O0OO ,limit =100 )#line:161
                if not OOO0OO0O00O0OOO00 :#line:162
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:163
                    continue #line:164
                for O0OO0O0OOO0OOO000 in OOO0OO0O00O0OOO00 :#line:166
                    for OOO0000O0O00OO0O0 in OO0OOOO000O000O00 :#line:167
                        reactionput (O000OO0OOO0OO00OO ,O0OOOOO00OO00O0OO ,O0OO0O0OOO0OOO000 ['id'],OOO0000O0O00OO0O0 )#line:168
                        time .sleep (O0O000OOO0OO0OOO0 )#line:169
            except Exception as OOOO000O0O0O0O0O0 :#line:170
                print (f"[!] Error processing channel {O0OOOOO00OO00O0OO}. Error: {OOOO000O0O0O0O0O0}")#line:171
                continue #line:172
    with concurrent .futures .ThreadPoolExecutor ()as O00OO00000OO000OO :#line:174
        O000O00O00OOO0OO0 =[O00OO00000OO000OO .submit (OOO0O0OOOOOO0O00O ,OO00O0O0O0000OOO0 )for OO00O0O0O0000OOO0 in O000O00OOOO00O00O ]#line:175
        concurrent .futures .wait (O000O00O00OOO0OO0 )#line:176
import requests #line:179
import json #line:180
import time #line:181
import colorama #line:182
alphabet_to_flag ={'a':'🇦','b':'🇧','c':'🇨','d':'🇩','e':'🇪','f':'🇫','g':'🇬','h':'🇭','i':'🇮','j':'🇯','k':'🇰','l':'🇱','m':'🇲','n':'🇳','o':'🇴','p':'🇵','q':'🇶','r':'🇷','s':'🇸','t':'🇹','u':'🇺','v':'🇻','w':'🇼','x':'🇽','y':'🇾','z':'🇿'}#line:190
def fetch_channels (O00OOO0O000OOOOOO ,OO0OOOO000O0O0OO0 ):#line:192
    OOO0OOO0OO0O0O00O =f"https://discord.com/api/v9/guilds/{OO0OOOO000O0O0OO0}/channels"#line:193
    O000OO0OO0O0000O0 ={"Authorization":O00OOO0O000OOOOOO }#line:194
    OO00O00O0OOO000O0 =requests .get (OOO0OOO0OO0O0O00O ,headers =O000OO0OO0O0000O0 )#line:195
    if OO00O00O0OOO000O0 .status_code ==200 :#line:196
        return [OOO0OOOO0OO0000O0 ['id']for OOO0OOOO0OO0000O0 in OO00O00O0OOO000O0 .json ()if OOO0OOOO0OO0000O0 ['type']==0 ]#line:197
    else :#line:198
        raise Exception (f"Failed to fetch channels: {OO00O00O0OOO000O0.status_code} - {OO00O00O0OOO000O0.text}")#line:199
def fetch_messages (O00000000000O0O0O ,O00OOO0O0OO0000O0 ,limit =100 ):#line:201
    O00OOO0O000OOO000 =f"https://discord.com/api/v9/channels/{O00OOO0O0OO0000O0}/messages?limit={limit}"#line:202
    OOO0O00OO00O00000 ={"Authorization":O00000000000O0O0O }#line:203
    OOOOO0OOO000O0000 =requests .get (O00OOO0O000OOO000 ,headers =OOO0O00OO00O00000 )#line:204
    if OOOOO0OOO000O0000 .status_code ==200 :#line:205
        return OOOOO0OOO000O0000 .json ()#line:206
    else :#line:207
        print (f"[!] Failed to fetch messages: {OOOOO0OOO000O0000.status_code} - {OOOOO0OOO000O0000.text}")#line:208
        return []#line:209
def reactionput (OO000OO0OO0O0OO00 ,OOO000OOOOO000OO0 ,OOOO0O00OO0O0OOOO ,O000O00O0OOO0OOO0 ):#line:211
    O000000O00O00O0O0 =f"https://discord.com/api/v9/channels/{OOO000OOOOO000OO0}/messages/{OOOO0O00OO0O0OOOO}/reactions/{O000O00O0OOO0OOO0}/@me"#line:212
    OO0OOOOO00OOO00O0 ={"Authorization":OO000OO0OO0O0OO00 ,"Content-Type":"application/json"}#line:213
    OOO0O0O0000O00OO0 =requests .put (O000000O00O00O0O0 ,headers =OO0OOOOO00OOO00O0 )#line:214
    if OOO0O0O0000O00OO0 .status_code not in [204 ,200 ]:#line:215
        print (f"{colorama.Fore.RED}    [!] Failed to add reaction: {OOO0O0O0000O00OO0.status_code} - {OOO0O0O0000O00OO0.text}{colorama.Fore.RESET}")#line:216
import random #line:218
def reaction_art ():#line:220
    try :#line:221
        with open ("token.txt",encoding ="utf-8")as OO0O0OO0O0O00000O :#line:222
            O0OOOO0OOOOO0000O =[OO0OO00OO000O00OO .strip ()for OO0OO00OO000O00OO in OO0O0OO0O0O00000O .readlines ()if OO0OO00OO000O00OO .strip ()]#line:223
    except (FileNotFoundError ,KeyError ):#line:224
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:225
        return #line:226
    OO00O000O00OOOO00 =input ("Server ID?: ").strip ()#line:228
    O0O00O0000000000O =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:230
    if O0O00O0000000000O =='2':#line:231
        OO000OOO0OOOOOOO0 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:232
        OO000OOOOO0O00O00 =[O0OOO0OOO0O0OOO00 .strip ()for O0OOO0OOO0O0OOO00 in OO000OOO0OOOOOOO0 if O0OOO0OOO0O0OOO00 .strip ()]#line:233
    else :#line:234
        OO000OOOOO0O00O00 =[]#line:235
        for O000OOOO0OO0OOO00 in O0OOOO0OOOOO0000O :#line:236
            try :#line:237
                OO000OOOOO0O00O00 .extend (fetch_channels (O000OOOO0OO0OOO00 ,OO00O000O00OOOO00 ))#line:238
            except Exception as O000OO0OOO000000O :#line:239
                print (f"[!] Failed to fetch channels for token. Error: {O000OO0OOO000000O}")#line:240
                continue #line:241
        random .shuffle (OO000OOOOO0O00O00 )#line:242
    O000000000000O0O0 =input ("Delay between reactions (in seconds)?: ").strip ()#line:244
    try :#line:246
        O000000000000O0O0 =float (O000000000000O0O0 )#line:247
        if O000000000000O0O0 <0 :#line:248
            raise ValueError #line:249
    except ValueError :#line:250
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:251
        O000000000000O0O0 =1.0 #line:252
    try :#line:254
        with open ("art.txt",encoding ="utf-8")as OOOOO0OOO00OOO0OO :#line:255
            O00O0O000O0O0O0O0 =[OO0OO00O0OO00O0OO .strip ()for OO0OO00O0OO00O0OO in OOOOO0OOO00OOO0OO .readlines ()if OO0OO00O0OO00O0OO .strip ()]#line:256
    except (FileNotFoundError ,KeyError ):#line:257
        print (f"{colorama.Fore.RED}    [!] Error: art.txt file not found or empty!{colorama.Fore.RESET}")#line:258
        return #line:259
    except UnicodeDecodeError as O000OO0OOO000000O :#line:260
        print (f"{colorama.Fore.RED}    [!] Error decoding art.txt: {str(O000OO0OOO000000O)}{colorama.Fore.RESET}")#line:261
        return #line:262
    if not O00O0O000O0O0O0O0 :#line:264
        print (f"{colorama.Fore.RED}    [!] No valid art provided in art.txt!{colorama.Fore.RESET}")#line:265
        return #line:266
    O00O0O000O0O0O0O0 .reverse ()#line:269
    for O000OOOO0OO0OOO00 in O0OOOO0OOOOO0000O :#line:271
        for OOO000OO00O00OO0O in OO000OOOOO0O00O00 :#line:272
            try :#line:273
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {OOO000OO00O00OO0O}...{colorama.Fore.RESET}")#line:274
                OOOO00OO000OOO00O =fetch_messages (O000OOOO0OO0OOO00 ,OOO000OO00O00OO0O ,limit =100 )#line:277
                if not OOOO00OO000OOO00O :#line:278
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:279
                    continue #line:280
                for O0OO0OOOO0OO00OO0 ,O0O00OOO000OOO0OO in enumerate (OOOO00OO000OOO00O ):#line:283
                    O0O00OO0000O0O0OO =O00O0O000O0O0O0O0 [O0OO0OOOO0OO00OO0 %len (O00O0O000O0O0O0O0 )].split (',')#line:284
                    for OO0OO0OO00O0O0OOO in O0O00OO0000O0O0OO :#line:285
                        reactionput (O000OOOO0OO0OOO00 ,OOO000OO00O00OO0O ,O0O00OOO000OOO0OO ['id'],OO0OO0OO00O0O0OOO .strip ())#line:286
                        print (f"Adding reaction '{OO0OO0OO00O0O0OOO.strip()}' to message {O0O00OOO000OOO0OO['id']} in channel {OOO000OO00O00OO0O}")#line:287
                        time .sleep (O000000000000O0O0 )#line:288
            except Exception as O000OO0OOO000000O :#line:289
                print (f"[!] Error processing channel {OOO000OO00O00OO0O}. Error: {O000OO0OOO000000O}")#line:290
                continue #line:291
    def O0O000O0O0OOOO0OO (O0OO00OOOOOOOOO0O ):#line:296
        for OO0OO000OOOOOOO0O in OO000OOOOO0O00O00 :#line:297
            try :#line:298
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {OO0OO000OOOOOOO0O}...{colorama.Fore.RESET}")#line:299
                O0OOO0OO0OO00OOO0 =fetch_messages (O0OO00OOOOOOOOO0O ,OO0OO000OOOOOOO0O ,limit =100 )#line:300
                if not O0OOO0OO0OO00OOO0 :#line:301
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:302
                    continue #line:303
                for O00O00OO00OOOOOOO in O0OOO0OO0OO00OOO0 :#line:305
                    for O000000000000OO0O in O0O00OO0000O0O0OO :#line:306
                        reactionput (O0OO00OOOOOOOOO0O ,OO0OO000OOOOOOO0O ,O00O00OO00OOOOOOO ['id'],O000000000000OO0O )#line:307
                        time .sleep (O000000000000O0O0 )#line:308
            except Exception as O0O0OOO0OOO0OO00O :#line:309
                print (f"[!] Error processing channel {OO0OO000OOOOOOO0O}. Error: {O0O0OOO0OOO0OO00O}")#line:310
                continue #line:311
    with concurrent .futures .ThreadPoolExecutor ()as O0O0OO0OO0000O0OO :#line:313
        OO00O0OOO0000O0OO =[O0O0OO0OO0000O0OO .submit (O0O000O0O0OOOO0OO ,O0000OO0OOO0O0OO0 )for O0000OO0OOO0O0OO0 in O0OOOO0OOOOO0000O ]#line:314
        concurrent .futures .wait (OO00O0OOO0000O0OO )#line:315
def update_group_ids ():#line:318
    try :#line:319
        with open ("token.txt")as O0O0O000OOOOO000O :#line:320
            OOOO000OOO00OO000 =[O00O00000OO0000OO .strip ()for O00O00000OO0000OO in O0O0O000OOOOO000O .readlines ()if O00O00000OO0000OO .strip ()]#line:321
        OO0OOOO0OOOO0O00O =OOOO000OOO00OO000 [0 ]#line:322
    except (FileNotFoundError ,KeyError ):#line:323
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:324
        return #line:325
    OO0O00OO0O0O0OOO0 ={"Authorization":OO0OOOO0OOOO0O00O ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:331
    OO0O0OOO00000000O =requests .get ('https://discord.com/api/v9/users/@me/channels',headers =OO0O00OO0O0O0OOO0 )#line:333
    if OO0O0OOO00000000O .status_code ==200 :#line:334
        O00O0OO0000OOOOOO =OO0O0OOO00000000O .json ()#line:335
        with open ("group_id.txt","w")as OOOOO0OO000OO0OOO :#line:336
            for OO0O000O0OOO00O0O in O00O0OO0000OOOOOO :#line:337
                if OO0O000O0OOO00O0O ['type']==3 :#line:338
                    OOOOO0OO000OO0OOO .write (OO0O000O0OOO00O0O ['id']+'\n')#line:339
        print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Group IDs updated successfully.{colorama.Fore.RESET}")#line:340
    else :#line:341
        print (f"{colorama.Fore.LIGHTRED_EX}    [!] Failed to retrieve group IDs. HTTP Status Code: {OO0O0OOO00000000O.status_code}{colorama.Fore.RESET}")#line:342
import requests #line:344
import requests #line:346
def fetch_channels (O00OO00OOO0OO00OO ,OO00O0OOOOO0OO0O0 ):#line:348
    try :#line:349
        OO000OO00OOO0OO0O =requests .Session ()#line:350
        OOO0OOOO000O0O0O0 =get_headers (O00OO00OOO0OO00OO )#line:351
        OOOO000O00OOOOOOO =OO000OO00OOO0OO0O .get (f"https://discord.com/api/v9/guilds/{OO00O0OOOOO0OO0O0}/channels",headers =OOO0OOOO000O0O0O0 ,timeout =10 )#line:358
        if OOOO000O00OOOOOOO .status_code ==200 :#line:361
            try :#line:362
                O00OO0O0O000O000O =OOOO000O00OOOOOOO .json ()#line:363
                return [O0000OO0O0O00000O ['id']for O0000OO0O0O00000O in O00OO0O0O000O000O if O0000OO0O0O00000O .get ('type')==0 ]#line:364
            except ValueError :#line:365
                print ("[!] Error: Response was not valid JSON.")#line:366
                return []#line:367
        elif OOOO000O00OOOOOOO .status_code ==401 :#line:368
            print ("[!] Error: Unauthorized - check your token.")#line:369
        elif OOOO000O00OOOOOOO .status_code ==403 :#line:370
            print ("[!] Error: Forbidden - you lack permissions.")#line:371
        elif OOOO000O00OOOOOOO .status_code ==404 :#line:372
            print ("[!] Error: Server not found - check the server ID.")#line:373
        else :#line:374
            print (f"[!] Error: Unexpected status code {OOOO000O00OOOOOOO.status_code}.")#line:375
        return []#line:378
    except requests .exceptions .Timeout :#line:380
        print ("[!] Error: Request timed out. Check your connection or try again later.")#line:381
        return []#line:382
    except requests .exceptions .RequestException as O0O0O0O0000O0O000 :#line:383
        print (f"[!] Error: An error occurred while fetching channels: {O0O0O0O0000O0O000}")#line:384
        return []#line:385
def extract_uids_from_messages (OO0O000OOOO0O0OOO ):#line:391
    O0O0O0OO00OO00O0O =set ()#line:392
    for O00O000O0OOO000O0 in OO0O000OOOO0O0OOO :#line:393
        O0O0O0OO00OO00O0O .add (O00O000O0OOO000O0 ['author']['id'])#line:394
    return list (O0O0O0OO00OO00O0O )#line:395
def send_message_with_mention (OO000O0O0O0O0OOO0 ,OOO0000OO0O00OO00 ,O00000OO0O00O00OO ,O0OOO0O0OOOOO00O0 ):#line:397
    OOOO0O00O0OO000OO =get_session ()#line:398
    OOO000O00000OO0OO =get_headers (OO000O0O0O0O0OOO0 )#line:399
    if O0OOO0O0OOOOO00O0 :#line:401
        OOO0O0OO0OOOO00O0 =random .choice (O0OOO0O0OOOOO00O0 )#line:402
        O00000OO0O00O00OO +=f" <@{OOO0O0OO0OOOO00O0}>"#line:403
    OO0O000O00OOO000O =OOOO0O00O0OO000OO .post (f"https://discord.com/api/v9/channels/{OOO0000OO0O00OO00}/messages",headers =OOO000O00000OO0OO ,json ={"content":O00000OO0O00O00OO })#line:409
    if OO0O000O00OOO000O .status_code in [200 ,201 ]:#line:410
        print (f"[+] Message sent to channel {OOO0000OO0O00OO00}")#line:411
    elif OO0O000O00OOO000O .status_code ==429 :#line:412
        print ("[-] Rate limited. Please wait before retrying.")#line:413
        OO0OO0OOO00000O0O =OO0O000O00OOO000O .json ().get ("retry_after",1 )#line:414
        time .sleep (OO0OO0OOO00000O0O )#line:415
    else :#line:416
        print (f"[!] Error occurred: {OO0O000O00OOO000O.status_code}")#line:417
def send_messages_with_mentions ():#line:418
    try :#line:419
        with open ("token.txt")as OO000OOOOO0OOOOO0 :#line:420
            O00000O0OOO0OO0OO =[O0000OO0OO00000OO .strip ()for O0000OO0OO00000OO in OO000OOOOO0OOOOO0 .readlines ()if O0000OO0OO00000OO .strip ()]#line:421
    except (FileNotFoundError ,KeyError ):#line:422
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:423
        return #line:424
    O0000OO00OOOOO000 =input ("Server ID?: ").strip ()#line:426
    OO0O00OO000O00O0O =input ("Delay between messages (in seconds)?: ").strip ()#line:427
    OOOOO0O0O0OO0OOOO =input ("Number of messages to send?: ").strip ()#line:428
    OO0O00000000OOOO0 =input ("Message content?: ").strip ()#line:429
    OOO0OOO00O000O000 =input ("Blacklist User IDs (comma-separated)?: ").strip ().split (',')#line:430
    OOO0OOO00O000O000 =[OO0000OO00O0OO0O0 .strip ()for OO0000OO00O0OO0O0 in OOO0OOO00O000O000 if OO0000OO00O0OO0O0 .strip ()]#line:431
    try :#line:433
        OO0O00OO000O00O0O =float (OO0O00OO000O00O0O )#line:434
        if OO0O00OO000O00O0O <0 :#line:435
            raise ValueError #line:436
    except ValueError :#line:437
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:438
        OO0O00OO000O00O0O =1.0 #line:439
    try :#line:441
        OOOOO0O0O0OO0OOOO =int (OOOOO0O0O0OO0OOOO )#line:442
        if OOOOO0O0O0OO0OOOO <=0 :#line:443
            raise ValueError #line:444
    except ValueError :#line:445
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:446
        OOOOO0O0O0OO0OOOO =1 #line:447
    O000O0O0O0O00OO00 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:449
    if O000O0O0O0O00OO00 =='2':#line:450
        O0OOO0O0O0OO000OO =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:451
        O0OOO0O0O0OO000OO =[O00OOOO00OO0OOOOO .strip ()for O00OOOO00OO0OOOOO in O0OOO0O0O0OO000OO if O00OOOO00OO0OOOOO .strip ()]#line:452
    else :#line:453
        O0OOO0O0O0OO000OO =[]#line:454
    O0O0O0O0O000O0OOO =set ()#line:456
    for OO00OOO000OOOO00O in O00000O0OOO0OO0OO :#line:457
        OOOO0O000OO00OOOO =fetch_channels (OO00OOO000OOOO00O ,O0000OO00OOOOO000 )#line:458
        for OO00O0OOOO00O0O00 in OOOO0O000OO00OOOO :#line:459
            OOOO0000OO0OO0000 =fetch_messages (OO00OOO000OOOO00O ,OO00O0OOOO00O0O00 ,limit =100 )#line:460
            OO0OO0000OO0000O0 =extract_uids_from_messages (OOOO0000OO0OO0000 )#line:461
            O0O0O0O0O000O0OOO .update (OO0OO0000OO0000O0 )#line:462
    O0O0O0O0O000O0OOO =list (set (O0O0O0O0O000O0OOO )-set (OOO0OOO00O000O000 ))#line:465
    for _OO000000000O0000O in range (OOOOO0O0O0OO0OOOO ):#line:467
        for OO00OOO000OOOO00O in O00000O0OOO0OO0OO :#line:468
            if O0OOO0O0O0OO000OO :#line:469
                OOOO0O000OO00OOOO =O0OOO0O0O0OO000OO #line:470
            for OO00O0OOOO00O0O00 in OOOO0O000OO00OOOO :#line:471
                send_message_with_mention (OO00OOO000OOOO00O ,OO00O0OOOO00O0O00 ,OO0O00000000OOOO0 ,O0O0O0O0O000O0OOO )#line:472
                time .sleep (OO0O00OO000O00O0O )#line:473
def join_discord_invite ():#line:478
    try :#line:479
        with open ("token.txt")as OOO00O00O0OO00OOO :#line:480
            OO0O0OOOOO0OO00O0 =[O0OOOO0000O00OOO0 .strip ()for O0OOOO0000O00OOO0 in OOO00O00O0OO00OOO .readlines ()if O0OOOO0000O00OOO0 .strip ()]#line:481
    except (FileNotFoundError ,KeyError ):#line:482
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:483
        return #line:484
    O0OOOO00OOO0O0O00 =input ("Invite Code?: discord.gg/").strip ()#line:486
    for OOOO000OOO0O0000O in OO0O0OOOOO0OO00O0 :#line:489
        joiner (OOOO000OOO0O0000O ,O0OOOO00OOO0O0O00 )#line:490
import json ,time ,base64 ,random ,requests #line:492
def cookieset (OO00OOO0OOO00OO0O ):#line:494
    OO0OO00OOOOO0OOO0 =OO00OOO0OOO00OO0O .get ("https://discord.com/app")#line:495
    return OO0OO00OOOOO0OOO0 .cookies .get_dict ()#line:496
def generatexspandua (OOOO00OOO00OO000O ):#line:498
    OO0O00OO0O0OOOO0O =["Android","Windows","Macintosh"]#line:499
    OO00000OOO00O0OO0 =random .choice (OO0O00OO0O0OOOO0O )#line:500
    if OO00000OOO00O0OO0 =="Macintosh":#line:501
        OO0O0OO0O00O0OOO0 =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:502
        O00000OOOOO000OO0 ="Macintosh; Intel Mac OS X "+OO0O0OO0O00O0OOO0 #line:503
        O0000OO0000OOO00O ="x86_64"#line:504
    elif OO00000OOO00O0OO0 =="Windows":#line:505
        OO0O0OO0O00O0OOO0 =f'{random.choice([6.0, 10.0, 11.0])}'#line:506
        O00000OOOOO000OO0 ="Windows NT "+OO0O0OO0O00O0OOO0 +" Win64; x64"#line:507
        O0000OO0000OOO00O ="x86_64"#line:508
    else :#line:509
        OO0O0OO0O00O0OOO0 ="13"#line:510
        O00000OOOOO000OO0 =f"Linux; Android 13; Pixel 6a"#line:511
        O0000OO0000OOO00O ="aarch64"#line:512
    OO000O00O0O0OO0O0 ={"os":OO00000OOO00O0OO0 ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":OO0O0OO0O00O0OOO0 ,"os_arch":O0000OO0000OOO00O ,"system_locale":"ja-JP","client_build_number":OOOO00OOO00OO000O ,"client_event_source":None ,"design_id":0 }#line:525
    O00OO0OOO0O0O00OO =f"Mozilla/5.0 ({O00000OOOOO000OO0}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:526
    return base64 .b64encode (json .dumps (OO000O00O0O0OO0O0 ,separators =(',',':')).encode ()).decode (),O00OO0OOO0O0O00OO #line:527
def joiner (O0O0000OO0OO00OO0 ,O0O0O0OOOO0O00OO0 ,OOO00OOO00OO0O000 ,OOOO0OOO0OOOO0OOO ):#line:529
  OO0000OOOOO00OOO0 =get_session (OOO00OOO00OO0O000 )#line:530
  O00OOOOOOOOO000OO =cookieset (OO0000OOOOO00OOO0 )#line:531
  O00OOOOOOOOO000OO ["locale"]="ja-JP"#line:532
  OOOOO00O0OOO000O0 =201211 #line:533
  OOO0O0O0000OOOOO0 ,O0OOOOOOOO000OO0O =generatexspandua (OOOOO00O0OOO000O0 )#line:534
  O0000OOO0OO000OO0 ={"Authorization":O0O0000OO0OO00OO0 ,"accept":"*/*","accept-language":"ja-JP","connection":"keep-alive","DNT":"1","origin":"https://discord.com","sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","referer":"https://discord.com/channels/@me","TE":"Trailers","user-agent":O0OOOOOOOO000OO0O ,"X-Super-Properties":OOO0O0O0000OOOOO0 ,}#line:549
  OOO0O00O0O0O0000O =OO0000OOOOO00OOO0 .post ("https://discord.com/api/v9/invites/"+O0O0O0OOOO0O00OO0 ,headers =O0000OOO0OO000OO0 ,json ={},cookies =O00OOOOOOOOO000OO )#line:551
  if OOO0O00O0O0O0000O .status_code ==200 :#line:552
    print ("[+] Probably joined "+O0O0000OO0OO00OO0 )#line:553
    if "show_verification_form"in OOO0O00O0O0O0000O .json ():#line:554
      bypass (O0O0000OO0OO00OO0 ,OOO0O00O0O0O0000O .json ()["guild"]["id"],OO0000OOOOO00OOO0 ,O0000OOO0OO000OO0 )#line:555
    return #line:556
  elif "captcha_key"in OOO0O00O0O0O0000O .text and OOO0O00O0O0O0000O .status_code ==400 :#line:557
    print ("[!] Hcaptcha interference "+O0O0000OO0OO00OO0 )#line:558
    return #line:559
  elif OOO0O00O0O0O0000O .status_code ==401 :#line:560
    print ("[!] Token is dead "+O0O0000OO0OO00OO0 )#line:561
    return #line:562
  elif OOO0O00O0O0O0000O .status_code ==403 :#line:563
    if "message"in OOO0O00O0O0O0000O .json ():#line:564
      if OOO0O00O0O0O0000O .json ()["message"]=="Unknown Message":#line:565
        print ("[!] Unknown error "+O0O0000OO0OO00OO0 )#line:566
        return #line:567
      else :#line:568
        print ("[!] Verification required "+O0O0000OO0OO00OO0 )#line:569
        return #line:570
    else :#line:571
      print ("[!] Error occurred "+O0O0000OO0OO00OO0 )#line:572
      return #line:573
  elif OOO0O00O0O0O0000O .status_code ==429 :#line:574
    print ("[!] Token rate-limited "+O0O0000OO0OO00OO0 )#line:575
    return #line:576
  elif OOO0O00O0O0O0000O .status_code ==400 :#line:577
    if "captcha_key"in OOO0O00O0O0O0000O .json ():#line:578
      print ("[!] Hcaptcha interference "+O0O0000OO0OO00OO0 )#line:579
      return #line:580
    else :#line:581
      print ("[!] Error occurred "+O0O0000OO0OO00OO0 )#line:582
      return #line:583
  elif OOO0O00O0O0O0000O .status_code ==401 :#line:584
    print ("[!] Token is dead "+O0O0000OO0OO00OO0 )#line:585
    return #line:586
  elif OOO0O00O0O0O0000O .status_code ==403 :#line:587
    if "message"in OOO0O00O0O0O0000O .json ():#line:588
      if OOO0O00O0O0O0000O .json ()["message"]=="Unknown Message":#line:589
        print ("[!] Unknown error "+O0O0000OO0OO00OO0 )#line:590
        return #line:591
      else :#line:592
        print ("[!] Verification required "+O0O0000OO0OO00OO0 )#line:593
        return #line:594
    else :#line:595
      print ("[!] Error occurred "+O0O0000OO0OO00OO0 )#line:596
  elif OOO0O00O0O0O0000O .status_code ==429 :#line:597
    print ("[!] Token rate-limited "+O0O0000OO0OO00OO0 )#line:598
    return #line:599
  else :#line:600
    print ("[!] Error occurred "+O0O0000OO0OO00OO0 )#line:601
    return #line:602
def update_group_ids ():#line:605
    O0000000OO0O0000O =input ("Invite Code?: ").strip ()#line:606
    try :#line:607
        with open ("token.txt")as OOOO0O0O0O0OOOO0O :#line:608
            OO0OOOOO0O0O0OOO0 =[OO0000O000OOOO00O .strip ()for OO0000O000OOOO00O in OOOO0O0O0O0OOOO0O .readlines ()if OO0000O000OOOO00O .strip ()]#line:609
    except (FileNotFoundError ,KeyError ):#line:610
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:611
        return #line:612
    OOO0O000OO0O00000 =requests .Session ()#line:614
    for O0O0000O0O00O00OO in OO0OOOOO0O0O0OOO0 :#line:615
        joiner (O0O0000O0O00O00OO ,O0000000OO0O0000O ,OOO0O000OO0O00000 )#line:616
        time .sleep (2 )#line:617
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:619
def bypass (O0000OOOO0O0OOOO0 ,OO00OO00OOO0OO00O ,OO0OO0OO000O0O000 ,O000O00O000000OOO ):#line:622
    try :#line:623
        OOO00OO0O000O00O0 =OO0OO0OO000O0O000 .get (f"https://discord.com/api/v9/guilds/{OO00OO00OOO0OO00O}/member-verification?with_guild=false",headers =O000O00O000000OOO ).json ()#line:624
        O0OOOOOO0OO0OOOO0 =OO0OO0OO000O0O000 .put (f"https://discord.com/api/v9/guilds/{OO00OO00OOO0OO00O}/requests/@me",headers =O000O00O000000OOO ,json =OOO00OO0O000O00O0 )#line:625
        if O0OOOOOO0OO0OOOO0 .status_code ==201 :#line:626
            print (f"[+] MemberscreeningBypassed {O0000OOOO0O0OOOO0}")#line:627
            return #line:628
        else :#line:629
            print (f"[!] Bypassが出来ませんでした {O0000OOOO0O0OOOO0}")#line:630
            return #line:631
    except Exception as O0OOO0OOO000O0OOO :#line:632
        print (f"[!] エラーが発生しました。{O0OOO0OOO000O0OOO}")#line:633
session =requests .Session ()#line:635
def reactionput (OOO00OO0O0O00OOOO ,O000OOO0OOO0OO0OO ,OOO000O0O00OO0O00 ,OOOOO00OO0000OO00 ,proxy =None ):#line:638
    O00OOOOOOO0OO0OOO =get_session (proxy )#line:639
    OOOOO0O0O000O0O0O =get_headers (O00OOOOOOO0OO0OOO )#line:640
    OOOOO0O0O000O0O0O ["Authorization"]=OOO00OO0O0O00OOOO #line:641
    OOOOO00OO0000OO00 =requests .utils .quote (OOOOO00OO0000OO00 )#line:643
    OOO000OO00O000000 =O00OOOOOOO0OO0OOO .put (f"https://discord.com/api/v9/channels/{O000OOO0OOO0OO0OO}/messages/{OOO000O0O00OO0O00}/reactions/{OOOOO00OO0000OO00}/%40me?location=Message&type=0",headers =OOOOO0O0O000O0O0O )#line:647
    if OOO000OO00O000000 .status_code in [200 ,204 ]:#line:648
        print (f"[+] Reaction '{OOOOO00OO0000OO00}' added successfully to message {OOO000O0O00OO0O00}")#line:649
    elif OOO000OO00O000000 .status_code ==429 :#line:650
        print ("[-] Rate limited. Please wait before retrying.")#line:651
        O0000OO0OO000OOO0 =OOO000OO00O000000 .json ().get ("retry_after",1 )#line:652
        time .sleep (O0000OO0OO000OOO0 )#line:653
    elif OOO000OO00O000000 .status_code ==401 :#line:654
        print ("[-] Invalid or expired token.")#line:655
    else :#line:656
        print (f"[!] Error occurred: {OOO000OO00O000000.status_code}")#line:657
def generatexspandua (O0000OO0O0OO00OOO ):#line:660
  OO0OO00OO00OO00OO =["Android","Windows","Macintosh"]#line:661
  OOO00OOOO0OOOO0O0 =random .choice (OO0OO00OO00OO00OO )#line:662
  if OOO00OOOO0OOOO0O0 =="Macintosh":#line:663
    OOO00O0000OOOO00O =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:664
    OO0O0O00000OOO000 ="Macintosh; Intel Mac OS X "+OOO00O0000OOOO00O #line:665
    O0OO00OO0OOOOO0O0 ="x86_64"#line:666
  if OOO00OOOO0OOOO0O0 =="Windows":#line:667
    OOO00O0000OOOO00O =f'{random.choice([6.0,10.0,11.0])}'#line:668
    OO0O0O00000OOO000 ="Windows NT "+OOO00O0000OOOO00O +" Win64; x64"#line:669
    O0OO00OO0OOOOO0O0 ="x86_64"#line:670
  if OOO00OOOO0OOOO0O0 =="Android":#line:671
    OOO00O0000OOOO00O ="13"#line:672
    OO0O0O00000OOO000 =f"Linux; Android 13; Pixel 6a"#line:673
    O0OO00OO0OOOOO0O0 ="aarch64"#line:674
  O0000OO000OOO00OO ={"os":OOO00OOOO0OOOO0O0 ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":OOO00O0000OOOO00O ,"os_arch":O0OO00OO0OOOOO0O0 ,"system_locale":"ja-JP","client_build_number":O0000OO0O0OO00OOO ,"client_event_source":None ,"design_id":0 }#line:675
  OOOOO00OOOOO00OOO =f"Mozilla/5.0 ({OO0O0O00000OOO000}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:676
  return base64 .b64encode (json .dumps (O0000OO000OOO00OO ,separators =(',',':')).encode ()).decode (),OOOOO00OOOOO00OOO #line:677
import base64 #line:679
def nickchanger ():#line:682
    try :#line:683
        with open ("token.txt")as OO00OOO0O0O0O0OOO :#line:684
            OOOOO00O000OO0O0O =[OOOOO0O00O0OOOOO0 .strip ()for OOOOO0O00O0OOOOO0 in OO00OOO0O0O0O0OOO .readlines ()if OOOOO0O00O0OOOOO0 .strip ()]#line:685
    except (FileNotFoundError ,KeyError ):#line:686
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:687
        return #line:688
    O0O00O0000O000000 =input ("Server ID?: ").strip ()#line:690
    O00OOOOOOO00OO00O =input ("Nickname?: ").strip ()#line:691
    O000OO0OOO00OOOO0 =input ("Delay (in seconds)?: ").strip ()#line:692
    try :#line:694
        O000OO0OOO00OOOO0 =float (O000OO0OOO00OOOO0 )#line:695
        if O000OO0OOO00OOOO0 <0 :#line:696
            raise ValueError #line:697
    except ValueError :#line:698
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:699
        O000OO0OOO00OOOO0 =1.0 #line:700
    for O0O0OO0O000O0O000 in OOOOO00O000OO0O0O :#line:702
        OO0O0O0OO00OO0OOO ={"Authorization":O0O0OO0O000O0O000 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:707
        OO0OO00O00O000O00 ={"nick":O00OOOOOOO00OO00O }#line:708
        OO000O0O0O00O0OO0 =requests .patch (f"https://discord.com/api/v9/guilds/{O0O00O0000O000000}/members/@me",headers =OO0O0O0OO00OO0OOO ,json =OO0OO00O00O000O00 )#line:709
        if OO000O0O0O00O0OO0 .status_code ==200 :#line:711
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Nickname changed to '{O00OOOOOOO00OO00O}' successfully for token {O0O0OO0O000O0O000}.{colorama.Fore.RESET}")#line:712
        elif OO000O0O0O00O0OO0 .status_code ==429 :#line:713
            print (f"{colorama.Fore.RED}    [!] Rate limited. Please wait before retrying for token {O0O0OO0O000O0O000}.{colorama.Fore.RESET}")#line:714
            O0OOOOO0000OOO000 =OO000O0O0O00O0OO0 .json ().get ("retry_after",1 )#line:715
            time .sleep (O0OOOOO0000OOO000 )#line:716
        else :#line:717
            print (f"{colorama.Fore.RED}    [!] Error occurred: {OO000O0O0O00O0OO0.status_code} for token {O0O0OO0O000O0O000}.{colorama.Fore.RESET}")#line:718
        time .sleep (O000OO0OOO00OOOO0 )#line:720
import json ,websocket ,threading ,tls_client ,random ,time #line:724
session =tls_client .Session (client_identifier ="chrome112",random_tls_extension_order =True )#line:726
class Utils :#line:728
    @staticmethod #line:729
    def rangeCorrector (OOO0OO000O00O0O0O ):#line:730
        if [0 ,99 ]not in OOO0OO000O00O0O0O :#line:731
            OOO0OO000O00O0O0O .insert (0 ,[0 ,99 ])#line:732
        return OOO0OO000O00O0O0O #line:733
    @staticmethod #line:735
    def getRanges (O0OOOOO0000O0O0OO ,OOOOOOOO0O0OO0OO0 ,OO0O0O000OO0O00O0 ):#line:736
        O000O00000OO0000O =int (O0OOOOO0000O0O0OO *OOOOOOOO0O0OO0OO0 )#line:737
        OOOOOOOOO0000OO00 =[[O000O00000OO0000O ,O000O00000OO0000O +99 ]]#line:738
        if OO0O0O000OO0O00O0 >O000O00000OO0000O +99 :#line:739
            OOOOOOOOO0000OO00 .append ([O000O00000OO0000O +100 ,O000O00000OO0000O +199 ])#line:740
        return Utils .rangeCorrector (OOOOOOOOO0000OO00 )#line:741
    @staticmethod #line:743
    def parseGuildMemberListUpdate (OOOO00OO000OO0OOO ):#line:744
        OO0O0OOOOO0OOO0OO ={"online_count":OOOO00OO000OO0OOO ["d"]["online_count"],"member_count":OOOO00OO000OO0OOO ["d"]["member_count"],"id":OOOO00OO000OO0OOO ["d"]["id"],"guild_id":OOOO00OO000OO0OOO ["d"]["guild_id"],"hoisted_roles":OOOO00OO000OO0OOO ["d"]["groups"],"types":[],"locations":[],"updates":[],}#line:754
        for O000O0OOOOOO00000 in OOOO00OO000OO0OOO ["d"]["ops"]:#line:756
            OO0O0OOOOO0OOO0OO ["types"].append (O000O0OOOOOO00000 ["op"])#line:757
            if O000O0OOOOOO00000 ["op"]in ("SYNC","INVALIDATE"):#line:758
                OO0O0OOOOO0OOO0OO ["locations"].append (O000O0OOOOOO00000 ["range"])#line:759
                if O000O0OOOOOO00000 ["op"]=="SYNC":#line:760
                    OO0O0OOOOO0OOO0OO ["updates"].append (O000O0OOOOOO00000 ["items"])#line:761
                else :#line:762
                    OO0O0OOOOO0OOO0OO ["updates"].append ([])#line:763
            elif O000O0OOOOOO00000 ["op"]in ("INSERT","UPDATE","DELETE"):#line:764
                OO0O0OOOOO0OOO0OO ["locations"].append (O000O0OOOOOO00000 ["index"])#line:765
                if O000O0OOOOOO00000 ["op"]=="DELETE":#line:766
                    OO0O0OOOOO0OOO0OO ["updates"].append ([])#line:767
                else :#line:768
                    OO0O0OOOOO0OOO0OO ["updates"].append (O000O0OOOOOO00000 ["item"])#line:769
        return OO0O0OOOOO0OOO0OO #line:770
class DiscordSocket (websocket .WebSocketApp ):#line:772
    def __init__ (O0OOOOOO0000O0OOO ,O0OO0O0OO00000O0O ,O000OOO0000O0OO00 ,OO0OO00O0O00OO000 ):#line:773
        O0OOOOOO0000O0OOO .token =O0OO0O0OO00000O0O #line:774
        O0OOOOOO0000O0OOO .guild_id =O000OOO0000O0OO00 #line:775
        O0OOOOOO0000O0OOO .channel_id =OO0OO00O0O00OO000 #line:776
        O0OOOOOO0000O0OOO .socket_headers ={"Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","Cache-Control":"no-cache","Pragma":"no-cache","Sec-WebSocket-Extensions":"permessage-deflate; client_max_window_bits","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",}#line:784
        super ().__init__ ("wss://gateway.discord.gg/?encoding=json&v=9",header =O0OOOOOO0000O0OOO .socket_headers ,on_open =lambda O0OO000OOOO000O0O :O0OOOOOO0000O0OOO .sock_open (O0OO000OOOO000O0O ),on_message =lambda O00OO00O00000O0OO ,O0OOOOOO0OOO000O0 :O0OOOOOO0000O0OOO .sock_message (O00OO00O00000O0OO ,O0OOOOOO0OOO000O0 ),on_close =lambda O000O0O0O00O0O0O0 ,O0O0O0O0OO0000OOO ,O00OOO0OOOO00000O :O0OOOOOO0000O0OOO .sock_close (O000O0O0O00O0O0O0 ,O0O0O0O0OO0000OOO ,O00OOO0OOOO00000O ),)#line:793
        O0OOOOOO0000O0OOO .endScraping =False #line:795
        O0OOOOOO0000O0OOO .guilds ={}#line:796
        O0OOOOOO0000O0OOO .members ={}#line:797
        O0OOOOOO0000O0OOO .ranges =[[0 ,0 ]]#line:798
        O0OOOOOO0000O0OOO .lastRange =0 #line:799
        O0OOOOOO0000O0OOO .packets_recv =0 #line:800
    def run (O0O0OO00O00000O0O ):#line:802
        O0O0OO00O00000O0O .run_forever ()#line:803
        return O0O0OO00O00000O0O .members #line:804
    def scrapeUsers (O00O00O000O0O00OO ):#line:806
        if not O00O00O000O0O00OO .endScraping :#line:807
            O00O00O000O0O00OO .send ('{"op":14,"d":{"guild_id":"'+O00O00O000O0O00OO .guild_id +'","typing":true,"activities":true,"threads":true,"channels":{"'+O00O00O000O0O00OO .channel_id +'":'+json .dumps (O00O00O000O0O00OO .ranges )+"}}}")#line:816
    def sock_open (OOO00O000OO00OO00 ,OOO00O00O00OO000O ):#line:818
        OOO00O000OO00OO00 .send ('{"op":2,"d":{"token":"'+OOO00O000OO00OO00 .token +'","capabilities":125,"properties":{"os":"Windows NT","browser":"Chrome","device":"","system_locale":"it-IT","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36","browser_version":"119.0","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":103981,"client_event_source":null},"presence":{"status":"online","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}')#line:823
    def heartbeatThread (O00OO0O0OO0O00O00 ,O0OO0OO00OOO0O0OO ):#line:825
        try :#line:826
            while True :#line:827
                O00OO0O0OO0O00O00 .send ('{"op":1,"d":'+str (O00OO0O0OO0O00O00 .packets_recv )+"}")#line:828
                time .sleep (O0OO0OO00OOO0O0OO )#line:829
        except Exception as O0OO000OO0OO00OOO :#line:830
            pass #line:831
    def sock_message (O00O00000OOO0OO0O ,O0OOOO00O00000O0O ,OO000O0000O000O0O ):#line:833
        O00000000O00O00OO =json .loads (OO000O0000O000O0O )#line:834
        if O00000000O00O00OO is None :#line:835
            return #line:836
        if O00000000O00O00OO ["op"]!=11 :#line:837
            O00O00000OOO0OO0O .packets_recv +=1 #line:838
        if O00000000O00O00OO ["op"]==10 :#line:839
            threading .Thread (target =O00O00000OOO0OO0O .heartbeatThread ,args =(O00000000O00O00OO ["d"]["heartbeat_interval"]/1000 ,),daemon =True ,).start ()#line:844
        if O00000000O00O00OO ["t"]=="READY":#line:845
            for O0O00O0O0O0O0O00O in O00000000O00O00OO ["d"]["guilds"]:#line:846
                O00O00000OOO0OO0O .guilds [O0O00O0O0O0O0O00O ["id"]]={"member_count":O0O00O0O0O0O0O00O ["member_count"]}#line:847
        if O00000000O00O00OO ["t"]=="READY_SUPPLEMENTAL":#line:848
            O00O00000OOO0OO0O .ranges =Utils .getRanges (0 ,100 ,O00O00000OOO0OO0O .guilds [O00O00000OOO0OO0O .guild_id ]["member_count"])#line:851
            O00O00000OOO0OO0O .scrapeUsers ()#line:852
        elif O00000000O00O00OO ["t"]=="GUILD_MEMBER_LIST_UPDATE":#line:853
            OO0O0OO0OO0OO0OOO =Utils .parseGuildMemberListUpdate (O00000000O00O00OO )#line:854
            if OO0O0OO0OO0OO0OOO ["guild_id"]==O00O00000OOO0OO0O .guild_id and ("SYNC"in OO0O0OO0OO0OO0OOO ["types"]or "UPDATE"in OO0O0OO0OO0OO0OOO ["types"]):#line:858
                for O0000OOOOOO0O000O ,O0O00O0OO0OO0O00O in enumerate (OO0O0OO0OO0OO0OOO ["types"]):#line:859
                    if O0O00O0OO0OO0O00O =="SYNC":#line:860
                        if len (OO0O0OO0OO0OO0OOO ["updates"][O0000OOOOOO0O000O ])==0 :#line:861
                            O00O00000OOO0OO0O .endScraping =True #line:862
                            break #line:863
                        for O0O0OOOOOOOOO0O0O in OO0O0OO0OO0OO0OOO ["updates"][O0000OOOOOO0O000O ]:#line:865
                            if "member"in O0O0OOOOOOOOO0O0O :#line:866
                                OOOOO0000O0O00O00 =O0O0OOOOOOOOO0O0O ["member"]#line:867
                                O0OO0000OOOO0O00O ={"tag":OOOOO0000O0O00O00 ["user"]["username"]+"#"+OOOOO0000O0O00O00 ["user"]["discriminator"],"id":OOOOO0000O0O00O00 ["user"]["id"],}#line:873
                                if not OOOOO0000O0O00O00 ["user"].get ("bot"):#line:874
                                    O00O00000OOO0OO0O .members [OOOOO0000O0O00O00 ["user"]["id"]]=O0OO0000OOOO0O00O #line:875
                    elif O0O00O0OO0OO0O00O =="UPDATE":#line:877
                        for O0O0OOOOOOOOO0O0O in OO0O0OO0OO0OO0OOO ["updates"][O0000OOOOOO0O000O ]:#line:878
                            if "member"in O0O0OOOOOOOOO0O0O :#line:879
                                OOOOO0000O0O00O00 =O0O0OOOOOOOOO0O0O ["member"]#line:880
                                O0OO0000OOOO0O00O ={"tag":OOOOO0000O0O00O00 ["user"]["username"]+"#"+OOOOO0000O0O00O00 ["user"]["discriminator"],"id":OOOOO0000O0O00O00 ["user"]["id"],}#line:886
                                if not OOOOO0000O0O00O00 ["user"].get ("bot"):#line:887
                                    O00O00000OOO0OO0O .members [OOOOO0000O0O00O00 ["user"]["id"]]=O0OO0000OOOO0O00O #line:888
                    O00O00000OOO0OO0O .lastRange +=1 #line:890
                    O00O00000OOO0OO0O .ranges =Utils .getRanges (O00O00000OOO0OO0O .lastRange ,100 ,O00O00000OOO0OO0O .guilds [O00O00000OOO0OO0O .guild_id ]["member_count"])#line:893
                    time .sleep (0.45 )#line:894
                    O00O00000OOO0OO0O .scrapeUsers ()#line:895
            if O00O00000OOO0OO0O .endScraping :#line:897
                O00O00000OOO0OO0O .close ()#line:898
    def sock_close (OOO00O0000OOOO000 ,OO00OO0O0O0OOOOO0 ,OO0O0O0O00000OOO0 ,OOO00OO0OOOO0O0O0 ):#line:900
        pass #line:901
def scrape (O0000OOO000OO0O0O ,O0OO000000O000OOO ,OO0O00O0O0O0OO00O ):#line:903
    O00OO0000OO00OO0O =DiscordSocket (O0000OOO000OO0O0O ,O0OO000000O000OOO ,OO0O00O0O0O0OO00O )#line:904
    return O00OO0000OO00OO0O .run ()#line:905
def member_scrape (OO0O0OOOO000OO00O ,OO0OO0OO00OO0O000 ,O00OOO000OO0OOO00 ):#line:907
    OO0OOOOO0O0OOOOOO =[]#line:908
    for O00000O0000O00O00 in OO0O0OOOO000OO00O :#line:909
        OOO00O0O0000OOO00 ={"Authorization":O00000O0000O00O00 ,"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}#line:910
        O0OOO0OO0OO00O0OO =session .get (f"https://canary.discord.com/api/v9/guilds/{OO0OO0OO00OO0O000}",headers =OOO00O0O0000OOO00 )#line:911
        if O0OOO0OO0OO00O0OO .status_code ==200 :#line:912
            OO0OOOOO0O0OOOOOO .append (O00000O0000O00O00 )#line:913
            break #line:914
    if not OO0OOOOO0O0OOOOOO :#line:915
        print ("missing access")#line:916
    O00000O0000O00O00 =random .choice (OO0OOOOO0O0OOOOOO )#line:918
    OOO00O00O0OO0O0O0 =scrape (O00000O0000O00O00 ,OO0OO0OO00OO0O000 ,O00OOO000OO0OOO00 )#line:919
    O0OOOOOOO0OO00O00 =[f"<@{O0OO0OO00OOOOO0O0}>"for O0OO0OO00OOOOO0O0 in [int (O0OOO0O0O0OO0OOOO )for O0OOO0O0O0OO0OOOO in OOO00O00O0OO0O0O0 .keys ()]]#line:920
    print (f"[SUCCESS] {len(O0OOOOOOO0OO00O00)} scraped members")#line:921
    return O0OOOOOOO0OO00O00 #line:922
def spammer_menu ():#line:924
    try :#line:925
        with open ("token.txt")as O0O0O00OOOOOOO00O :#line:926
            O0OO00OO000O0O0OO =[OOOO00OOO0O00O0O0 .strip ()for OOOO00OOO0O00O0O0 in O0O0O00OOOOOOO00O .readlines ()if OOOO00OOO0O00O0O0 .strip ()]#line:927
    except (FileNotFoundError ,KeyError ):#line:928
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:929
        return #line:930
    OO00O00O0000000OO =input ("Server ID?: ").strip ()#line:932
    O000OOOO0O00O0O00 =input ("Message?: ").strip ()#line:933
    O0000000000O0OO00 =input ("Random mention (True/False)?: ").strip ().lower ()=='true'#line:934
    O0O0OOOO000O0O0O0 =input ("Delay between messages (in seconds)?: ").strip ()#line:935
    O000O0O0000OO0O0O =input ("Number of messages to send?: ").strip ()#line:936
    O0O0OOOO0O0O0O00O =input ("Blacklist User IDs (comma-separated) (Leave blank to skip)?: ").strip ().split (',')#line:937
    O0O0OOOO0O0O0O00O =[f"<@{OOOOOOO0O00OOO000.strip()}>"for OOOOOOO0O00OOO000 in O0O0OOOO0O0O0O00O if OOOOOOO0O00OOO000 .strip ()]#line:938
    try :#line:940
        O0O0OOOO000O0O0O0 =float (O0O0OOOO000O0O0O0 )#line:941
        if O0O0OOOO000O0O0O0 <0 :#line:942
            raise ValueError #line:943
    except ValueError :#line:944
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:945
        O0O0OOOO000O0O0O0 =1.0 #line:946
    try :#line:948
        O000O0O0000OO0O0O =int (O000O0O0000OO0O0O )#line:949
        if O000O0O0000OO0O0O <=0 :#line:950
            raise ValueError #line:951
    except ValueError :#line:952
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:953
        O000O0O0000OO0O0O =1 #line:954
    OOOO0OOOOO00000O0 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:956
    if OOOO0OOOOO00000O0 =='2':#line:957
        OOOOO0000OO00OOOO =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:958
        OOOOO0000OO00OOOO =[O0000O0O00OOO0OO0 .strip ()for O0000O0O00OOO0OO0 in OOOOO0000OO00OOOO if O0000O0O00OOO0OO0 .strip ()]#line:959
    else :#line:960
        OOOOO0000OO00OOOO =fetch_channels (O0OO00OO000O0O0OO [0 ],OO00O00O0000000OO )#line:961
    O000OO0OOO0OO000O =None #line:963
    spammer (O0OO00OO000O0O0OO ,OO00O00O0000000OO ,OOOOO0000OO00OOOO ,O000OOOO0O00O0O00 ,O0000000000O0OO00 ,O0O0OOOO0O0O0O00O ,O000OO0OOO0OO000O ,O000O0O0000OO0O0O )#line:965
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:967
import discum #line:969
import random #line:970
import time #line:971
def userget (O0O0000O0OOO00O00 ,O0OOO00O000O0O0OO ,OOOOOO00O0OO000O0 ):#line:973
    O0OOO0O0O0O0O00OO =[]#line:974
    OO00O0000OO0OOOO0 =discum .Client (token =O0O0000O0OOO00O00 ,log =False )#line:975
    try :#line:976
        OO00O0000OO0OOOO0 .gateway .close ()#line:977
    except :#line:978
        print ("Err")#line:979
    def OO0O0O00OOO0OOOO0 (O00OO0OO00000OOO0 ,O0OOOOOOOO0O0OO0O ):#line:981
        if OO00O0000OO0OOOO0 .gateway .finishedMemberFetching (O0OOOOOOOO0O0OO0O ):#line:982
            OOOOOOO00O0OOOOOO =len (OO00O0000OO0OOOO0 .gateway .session .guild (O0OOOOOOOO0O0OO0O ).members )#line:983
            print (str (OOOOOOO00O0OOOOOO )+' members fetched')#line:984
            OO00O0000OO0OOOO0 .gateway .removeCommand ({'function':OO0O0O00OOO0OOOO0 ,'params':{'guild_id':O0OOOOOOOO0O0OO0O }})#line:985
            OO00O0000OO0OOOO0 .gateway .close ()#line:986
    def OOOOOOO00OOO0000O (OO0O000OOOO0000O0 ,O0O00OO00O0OOO00O ):#line:988
        OO00O0000OO0OOOO0 .gateway .fetchMembers (OO0O000OOOO0000O0 ,O0O00OO00O0OOO00O ,keep ='all',wait =1 )#line:989
        OO00O0000OO0OOOO0 .gateway .command ({'function':OO0O0O00OOO0OOOO0 ,'params':{'guild_id':OO0O000OOOO0000O0 }})#line:990
        OO00O0000OO0OOOO0 .gateway .run ()#line:991
        OO00O0000OO0OOOO0 .gateway .resetSession ()#line:992
        return OO00O0000OO0OOOO0 .gateway .session .guild (OO0O000OOOO0000O0 ).members #line:993
    OOO0000O0O00OOOOO =OOOOOOO00OOO0000O (O0OOO00O000O0O0OO ,OOOOOO00O0OO000O0 )#line:995
    for O00000OOOO0OO0OO0 in OOO0000O0O00OOOOO :#line:996
        if O00000OOOO0OO0OO0 not in O0OOO0O0O0O0O00OO :#line:997
            O0OOO0O0O0O0O00OO .append (f"<@{O00000OOOO0OO0OO0}>")#line:998
    return O0OOO0O0O0O0O00OO #line:999
def spammer (OOOO0O00OOOOOOOOO ,OO0O0O0OO0OOOO0OO ,O000O0OO0O00O0000 ,OOOO000OO0O0O0O00 ,OO0OOO0OO000O0OOO ,O00OOO00O0O000O00 ,OO0000O00000O00OO ,OOO0OOO0000O0O0OO ):#line:1003
    OO00O0OO0000OOOOO =get_session (OO0000O00000O00OO )#line:1004
    O000000O0O0OO0O00 =0 #line:1005
    O0OOOO0OOOO0OOO00 =userget (OOOO0O00OOOOOOOOO [0 ],OO0O0O0OO0OOOO0OO ,O000O0OO0O00O0000 [0 ])#line:1007
    O0OOOO0OOOO0OOO00 =[OOOO0O0OO0O000O0O for OOOO0O0OO0O000O0O in O0OOOO0OOOO0OOO00 if OOOO0O0OO0O000O0O not in O00OOO00O0O000O00 ]#line:1010
    for _OOO00000O000O0OO0 in range (OOO0OOO0000O0O0OO ):#line:1012
        O0OO00O00OOO0OOOO =OOOO0O00OOOOOOOOO [O000000O0O0OO0O00 ]#line:1013
        OOO00O00O000OO0O0 =get_headers (O0OO00O00OOO0OOOO )#line:1014
        for OO0O000OO0OOOOOO0 in O000O0OO0O00O0000 :#line:1015
            O000000OO0O00O000 =OOOO000OO0O0O0O00 #line:1016
            if OO0OOO0OO000O0OOO and O0OOOO0OOOO0OOO00 :#line:1017
                O000O00OO00OO00OO =random .choice (O0OOOO0OOOO0OOO00 )#line:1018
                O000000OO0O00O000 +=f" {O000O00OO00OO00OO}"#line:1019
            O0OO000000OO0OOOO =OO00O0OO0000OOOOO .post (f"https://discord.com/api/v9/channels/{OO0O000OO0OOOOOO0}/messages",json ={"content":O000000OO0O00O000 },headers =OOO00O00O000OO0O0 )#line:1021
            if O0OO000000OO0OOOO .status_code ==200 :#line:1022
                print (f"200 message sent: {O0OO00O00OOO0OOOO}")#line:1023
            elif O0OO000000OO0OOOO .status_code ==429 :#line:1024
                print (f"429 rate limit: {O0OO00O00OOO0OOOO}")#line:1025
                OOOOOOO0O00OOO00O =O0OO000000OO0OOOO .json ().get ("retry_after",1 )#line:1026
                time .sleep (OOOOOOO0O00OOO00O )#line:1027
            elif O0OO000000OO0OOOO .status_code ==401 :#line:1028
                print (f"401 unknown token: {O0OO00O00OOO0OOOO}")#line:1029
            else :#line:1030
                print (f"error: {O0OO00O00OOO0OOOO}")#line:1031
        O000000O0O0OO0O00 =(O000000O0O0OO0O00 +1 )%len (OOOO0O00OOOOOOOOO )#line:1033
        time .sleep (1 )#line:1034
import requests #line:1038
import base64 #line:1039
import colorama #line:1040
import time #line:1041
def add_emojis_from_files ():#line:1043
    try :#line:1044
        with open ("emojiname.txt")as O000OO0O0O000000O ,open ("emojiurl.txt")as O0O00OOO00000O0OO :#line:1045
            OO0OOO0OO0O0O0000 =[O0O000OO0000O0000 .strip ()for O0O000OO0000O0000 in O000OO0O0O000000O .read ().split (',')if O0O000OO0000O0000 .strip ()]#line:1046
            OO000O000O0O00O00 =[O000O0000000O0OO0 .strip ()for O000O0000000O0OO0 in O0O00OOO00000O0OO .read ().split (',')if O000O0000000O0OO0 .strip ()]#line:1047
    except FileNotFoundError as O00O00O00OOO000O0 :#line:1048
        print (f"{colorama.Fore.RED}    [!] Error: {str(O00O00O00OOO000O0)}{colorama.Fore.RESET}")#line:1049
        return #line:1050
    if len (OO0OOO0OO0O0O0000 )!=len (OO000O000O0O00O00 ):#line:1052
        print (f"{colorama.Fore.RED}    [!] Error: The number of emoji names and URLs do not match!{colorama.Fore.RESET}")#line:1053
        return #line:1054
    try :#line:1056
        with open ("token.txt")as O00000OO0O00OO0O0 :#line:1057
            OOO00OO0O000000O0 =[OO0000O00OO0000O0 .strip ()for OO0000O00OO0000O0 in O00000OO0O00OO0O0 .readlines ()if OO0000O00OO0000O0 .strip ()]#line:1058
    except FileNotFoundError as O00O00O00OOO000O0 :#line:1059
        print (f"{colorama.Fore.RED}    [!] Error: {str(O00O00O00OOO000O0)}{colorama.Fore.RESET}")#line:1060
        return #line:1061
    OO0O000O0O0OO0O0O =input ("Enter the Guild ID: ").strip ()#line:1063
    O000OO000O0OOOOO0 =input ("Enter the rate limit between requests (in seconds): ").strip ()#line:1064
    try :#line:1066
        O000OO000O0OOOOO0 =float (O000OO000O0OOOOO0 )#line:1067
        if O000OO000O0OOOOO0 <0 :#line:1068
            raise ValueError #line:1069
    except ValueError :#line:1070
        print (f"{colorama.Fore.RED}    [!] Invalid rate limit. Using default rate limit of 5 seconds.{colorama.Fore.RESET}")#line:1071
        O000OO000O0OOOOO0 =5.0 #line:1072
    OOO000OO0O0000000 =set ()#line:1074
    for OO00OO00000OO00OO in OOO00OO0O000000O0 :#line:1076
        O0OO0OOOOOOO0000O ={'Authorization':OO00OO00000OO00OO ,'Content-Type':'application/json'}#line:1080
        OO0O00O0OOO0O00O0 =requests .get (f"https://discord.com/api/v9/guilds/{OO0O000O0O0OO0O0O}/emojis",headers =O0OO0OOOOOOO0000O )#line:1083
        if OO0O00O0OOO0O00O0 .status_code ==200 :#line:1084
            O0OO0O0O0OOOO00O0 =OO0O00O0OOO0O00O0 .json ()#line:1085
            for OOO00OOOOO0OO00OO in O0OO0O0O0OOOO00O0 :#line:1086
                OOO000OO0O0000000 .add (OOO00OOOOO0OO00OO ['name'])#line:1087
        else :#line:1088
            print (f"{colorama.Fore.RED}    [!] Error fetching existing emojis: {OO0O00O0OOO0O00O0.status_code} - {OO0O00O0OOO0O00O0.text}{colorama.Fore.RESET}")#line:1089
            continue #line:1090
    for OOO0O0O00OOOO0OOO ,OO000000OO00O0O00 in zip (OO0OOO0OO0O0O0000 ,OO000O000O0O00O00 ):#line:1092
        if OOO0O0O00OOOO0OOO in OOO000OO0O0000000 :#line:1093
            print (f"{colorama.Fore.YELLOW}    [*] Emoji '{OOO0O0O00OOOO0OOO}' already exists. Skipping...{colorama.Fore.RESET}")#line:1094
            continue #line:1095
        for OO00OO00000OO00OO in OOO00OO0O000000O0 :#line:1097
            try :#line:1098
                OO0O00O0OOO0O00O0 =requests .get (OO000000OO00O0O00 )#line:1099
                OO0O00O0OOO0O00O0 .raise_for_status ()#line:1100
                OOOO0000O0O0O00O0 =OO0O00O0OOO0O00O0 .content #line:1101
                O0O0O0O0OO0O00000 =base64 .b64encode (OOOO0000O0O0O00O0 ).decode ('utf-8')#line:1102
                OOOO00O00O0000000 ={'name':OOO0O0O00OOOO0OOO ,'image':f"data:image/png;base64,{O0O0O0O0OO0O00000}"}#line:1107
                O0OO0OOOOOOO0000O ={'Authorization':OO00OO00000OO00OO ,'Content-Type':'application/json'}#line:1112
                OOO0OOO0OO000O0OO =requests .post (f"https://discord.com/api/v9/guilds/{OO0O000O0O0OO0O0O}/emojis",headers =O0OO0OOOOOOO0000O ,json =OOOO00O00O0000000 )#line:1114
                if OOO0OOO0OO000O0OO .status_code ==201 :#line:1115
                    print (f"{colorama.Fore.GREEN}    [+] Successfully added emoji '{OOO0O0O00OOOO0OOO}' with token {OO00OO00000OO00OO}{colorama.Fore.RESET}")#line:1116
                    OOO000OO0O0000000 .add (OOO0O0O00OOOO0OOO )#line:1117
                    break #line:1118
                else :#line:1119
                    print (f"{colorama.Fore.RED}    [!] Failed to add emoji '{OOO0O0O00OOOO0OOO}' with token {OO00OO00000OO00OO}: {OOO0OOO0OO000O0OO.status_code} - {OOO0OOO0OO000O0OO.text}{colorama.Fore.RESET}")#line:1120
                time .sleep (O000OO000O0OOOOO0 )#line:1122
            except Exception as O00O00O00OOO000O0 :#line:1123
                print (f"{colorama.Fore.RED}    [!] Error adding emoji '{OOO0O0O00OOOO0OOO}' with token {OO00OO00000OO00OO}: {str(O00O00O00OOO000O0)}{colorama.Fore.RESET}")#line:1124
def main ():#line:1126
    colorama .init ()#line:1127
    while True :#line:1128
        logo ()#line:1129
        O00000OO0O00O000O =input (f"{colorama.Fore.LIGHTMAGENTA_EX}    [Final] Select an option from above: ")#line:1130
        if O00000OO0O00O000O =="0":#line:1132
            update_group_ids ()#line:1133
        elif O00000OO0O00O000O =="1":#line:1134
            join_discord_invite ()#line:1135
        elif O00000OO0O00O000O =="2":#line:1136
            reaction_spammer ()#line:1137
        elif O00000OO0O00O000O =="3":#line:1138
            send_messages_with_mentions ()#line:1139
        elif O00000OO0O00O000O =="4":#line:1140
            spammer_menu ()#line:1141
        elif O00000OO0O00O000O =="5":#line:1142
            nickchanger ()#line:1143
        elif O00000OO0O00O000O =="6":#line:1144
            add_emojis_from_files ()#line:1145
        elif O00000OO0O00O000O =="7":#line:1146
            reaction_art ()#line:1147
        elif O00000OO0O00O000O =="0":#line:1148
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [*] Exiting the application. Goodbye!{colorama.Fore.RESET}")#line:1149
            break #line:1150
        else :#line:1151
            print (f"{colorama.Fore.RED}    [!] Invalid option selected!{colorama.Fore.RESET}")#line:1152
        input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:1154
if __name__ =="__main__":#line:1156
    main ()#line:1157
