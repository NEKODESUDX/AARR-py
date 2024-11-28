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
    OO00O00OOO00OOOO0 =requests .Session ()#line:58
    if proxy :#line:59
        OO00O00OOO00OOOO0 .proxies ={"http":proxy ,"https":proxy }#line:60
    return OO00O00OOO00OOOO0 #line:61
def get_headers (O00OOO000O0O00OO0 ):#line:63
    return {"Authorization":O00OOO000O0O00OO0 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:68
def send_message_with_mention (O0O00000O0OOO000O ,OOOO0O00000O000OO ,OOOO0OOO00O000OOO ,O000OOO0O0O0O0OO0 ):#line:71
    O0O00O0000000OOOO =get_session ()#line:72
    OOO0O0000O00O0000 =get_headers (O0O00000O0OOO000O )#line:73
    if O000OOO0O0O0O0OO0 :#line:75
        OO00OOO00O0OOOO00 =random .choice (O000OOO0O0O0O0OO0 )#line:76
        OOOO0OOO00O000OOO +=f" <@{OO00OOO00O0OOOO00}>"#line:77
    O00O0OOOOOOO0OOOO =O0O00O0000000OOOO .post (f"https://discord.com/api/v9/channels/{OOOO0O00000O000OO}/messages",headers =OOO0O0000O00O0000 ,json ={"content":OOOO0OOO00O000OOO })#line:83
    if O00O0OOOOOOO0OOOO .status_code in [200 ,201 ]:#line:84
        print (f"[+] Message sent to channel {OOOO0O00000O000OO}")#line:85
    elif O00O0OOOOOOO0OOOO .status_code ==429 :#line:86
        print ("[-] Rate limited. Please wait before retrying.")#line:87
        O000OO0O00000O0O0 =O00O0OOOOOOO0OOOO .json ().get ("retry_after",1 )#line:88
        time .sleep (O000OO0O00000O0O0 )#line:89
    else :#line:90
        print (f"[!] Error occurred: {O00O0OOOOOOO0OOOO.status_code}")#line:91
def fetch_messages (OO0O00000O0000OO0 ,OOOO0000000OO00OO ,limit =100 ):#line:94
    O0OO000O0O0O0O0O0 ={"Authorization":OO0O00000O0000OO0 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:99
    O0OOOOO0OO00OOOOO =requests .get (f"https://discord.com/api/v9/channels/{OOOO0000000OO00OO}/messages?limit={limit}",headers =O0OO000O0O0O0O0O0 )#line:103
    if O0OOOOO0OO00OOOOO .status_code ==200 :#line:104
        return O0OOOOO0OO00OOOOO .json ()#line:105
    else :#line:106
        print (f"[!] Failed to fetch messages. HTTP Status Code: {O0OOOOO0OO00OOOOO.status_code}")#line:107
        return []#line:108
import concurrent .futures #line:110
def reaction_spammer ():#line:112
    try :#line:113
        with open ("token.txt")as O0OOO0000OOO0000O :#line:114
            OO0O0O0O00000O0O0 =[O00O0OOOOOOO0O000 .strip ()for O00O0OOOOOOO0O000 in O0OOO0000OOO0000O .readlines ()if O00O0OOOOOOO0O000 .strip ()]#line:115
    except (FileNotFoundError ,KeyError ):#line:116
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:117
        return #line:118
    O0O0O0O0OO0000OO0 =input ("Server ID?: ").strip ()#line:120
    OO0OOOOOOO0000OO0 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:122
    if OO0OOOOOOO0000OO0 =='2':#line:123
        O000O00OO0000OO00 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:124
        O000OOOOOOOO0000O =[OOOOOOOO0OOOO0000 .strip ()for OOOOOOOO0OOOO0000 in O000O00OO0000OO00 if OOOOOOOO0OOOO0000 .strip ()]#line:125
    else :#line:126
        O000OOOOOOOO0000O =[]#line:127
        for OOOO0OO0O0OO0O0O0 in OO0O0O0O00000O0O0 :#line:128
            try :#line:129
                O000OOOOOOOO0000O .extend (fetch_channels (OOOO0OO0O0OO0O0O0 ,O0O0O0O0OO0000OO0 ))#line:130
            except Exception as O000O00OOO0000000 :#line:131
                print (f"[!] Failed to fetch channels for token. Error: {O000O00OOO0000000}")#line:132
                continue #line:133
    O0OOO0000OO000000 =input ("Select your emoji (a, b, c, ... or custom emojis): ").strip ()#line:135
    O0O00000000OOOOO0 =input ("Delay between reactions (in seconds)?: ").strip ()#line:136
    try :#line:138
        O0O00000000OOOOO0 =float (O0O00000000OOOOO0 )#line:139
        if O0O00000000OOOOO0 <0 :#line:140
            raise ValueError #line:141
    except ValueError :#line:142
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:143
        O0O00000000OOOOO0 =1.0 #line:144
    OO0OOO00O0OOOOOOO =[]#line:146
    for O00O0000000OOOO0O in O0OOO0000OO000000 .split (","):#line:147
        O00O0000000OOOO0O =O00O0000000OOOO0O .strip ().lower ()#line:148
        if O00O0000000OOOO0O in alphabet_to_flag :#line:149
            OO0OOO00O0OOOOOOO .append (alphabet_to_flag [O00O0000000OOOO0O ])#line:150
        else :#line:151
            OO0OOO00O0OOOOOOO .append (O00O0000000OOOO0O )#line:152
    if not OO0OOO00O0OOOOOOO :#line:154
        print (f"{colorama.Fore.RED}    [!] No valid emojis provided!{colorama.Fore.RESET}")#line:155
        return #line:156
    def O00O0O0000000OOOO (O0000O00O0000O0O0 ):#line:158
        for OO00OO0OOO0O0OOO0 in O000OOOOOOOO0000O :#line:159
            try :#line:160
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {OO00OO0OOO0O0OOO0}...{colorama.Fore.RESET}")#line:161
                OO00OO0OOOO000000 =fetch_messages (O0000O00O0000O0O0 ,OO00OO0OOO0O0OOO0 ,limit =100 )#line:162
                if not OO00OO0OOOO000000 :#line:163
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:164
                    continue #line:165
                for OO0O00O000OOO00OO in OO00OO0OOOO000000 :#line:167
                    for O0O0OOOO0OO0O00O0 in OO0OOO00O0OOOOOOO :#line:168
                        reactionput (O0000O00O0000O0O0 ,OO00OO0OOO0O0OOO0 ,OO0O00O000OOO00OO ['id'],O0O0OOOO0OO0O00O0 )#line:169
                        time .sleep (O0O00000000OOOOO0 )#line:170
            except Exception as O000OO00000O0O0O0 :#line:171
                print (f"[!] Error processing channel {OO00OO0OOO0O0OOO0}. Error: {O000OO00000O0O0O0}")#line:172
                continue #line:173
    with concurrent .futures .ThreadPoolExecutor ()as OO0OO00O00O000O0O :#line:175
        O0OOO0000O0O000O0 =[OO0OO00O00O000O0O .submit (O00O0O0000000OOOO ,OO0OO0OOOOO0OO000 )for OO0OO0OOOOO0OO000 in OO0O0O0O00000O0O0 ]#line:176
        concurrent .futures .wait (O0OOO0000O0O000O0 )#line:177
import requests #line:180
import json #line:181
import time #line:182
import colorama #line:183
alphabet_to_flag ={'a':'🇦','b':'🇧','c':'🇨','d':'🇩','e':'🇪','f':'🇫','g':'🇬','h':'🇭','i':'🇮','j':'🇯','k':'🇰','l':'🇱','m':'🇲','n':'🇳','o':'🇴','p':'🇵','q':'🇶','r':'🇷','s':'🇸','t':'🇹','u':'🇺','v':'🇻','w':'🇼','x':'🇽','y':'🇾','z':'🇿'}#line:191
def fetch_channels (OOOO000O0OO00OO00 ,OOO00O00OOOO0O0OO ):#line:193
    OO000OOO00OO0O00O =f"https://discord.com/api/v9/guilds/{OOO00O00OOOO0O0OO}/channels"#line:194
    O0OO0OOOOO000O0OO ={"Authorization":OOOO000O0OO00OO00 }#line:195
    OO0O0O00O0O0O000O =requests .get (OO000OOO00OO0O00O ,headers =O0OO0OOOOO000O0OO )#line:196
    if OO0O0O00O0O0O000O .status_code ==200 :#line:197
        return [O0O000O0000O0O00O ['id']for O0O000O0000O0O00O in OO0O0O00O0O0O000O .json ()if O0O000O0000O0O00O ['type']==0 ]#line:198
    else :#line:199
        raise Exception (f"Failed to fetch channels: {OO0O0O00O0O0O000O.status_code} - {OO0O0O00O0O0O000O.text}")#line:200
def fetch_messages (OOO00OO00OO000O00 ,OOOOOOOO0O0O0000O ,limit =100 ):#line:202
    O000OO00OO000O0OO =f"https://discord.com/api/v9/channels/{OOOOOOOO0O0O0000O}/messages?limit={limit}"#line:203
    OOO0O0OO0O000000O ={"Authorization":OOO00OO00OO000O00 }#line:204
    O0OO00O0O0O000O00 =requests .get (O000OO00OO000O0OO ,headers =OOO0O0OO0O000000O )#line:205
    if O0OO00O0O0O000O00 .status_code ==200 :#line:206
        return O0OO00O0O0O000O00 .json ()#line:207
    else :#line:208
        print (f"[!] Failed to fetch messages: {O0OO00O0O0O000O00.status_code} - {O0OO00O0O0O000O00.text}")#line:209
        return []#line:210
def reactionput (O0OO0000O0OOOOO00 ,O000000OOO0OOO0OO ,O000OOOO0OO0OO00O ,O00O0000OO000OOO0 ):#line:212
    O0000OOOO0OOOO0O0 =f"https://discord.com/api/v9/channels/{O000000OOO0OOO0OO}/messages/{O000OOOO0OO0OO00O}/reactions/{O00O0000OO000OOO0}/@me"#line:213
    OO000OO0OO0O000OO ={"Authorization":O0OO0000O0OOOOO00 ,"Content-Type":"application/json"}#line:214
    O0O0O00OO00OOO0O0 =requests .put (O0000OOOO0OOOO0O0 ,headers =OO000OO0OO0O000OO )#line:215
    if O0O0O00OO00OOO0O0 .status_code not in [204 ,200 ]:#line:216
        print (f"{colorama.Fore.RED}    [!] Failed to add reaction: {O0O0O00OO00OOO0O0.status_code} - {O0O0O00OO00OOO0O0.text}{colorama.Fore.RESET}")#line:217
import random #line:219
def reaction_art ():#line:221
    try :#line:222
        with open ("token.txt",encoding ="utf-8")as O0O0OO0O00OO00OO0 :#line:223
            OO0000O00O0O0O0OO =[O00OOO0000000O00O .strip ()for O00OOO0000000O00O in O0O0OO0O00OO00OO0 .readlines ()if O00OOO0000000O00O .strip ()]#line:224
    except (FileNotFoundError ,KeyError ):#line:225
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:226
        return #line:227
    OO00O0O00OO00O00O =input ("Server ID?: ").strip ()#line:229
    OOOO00O00OOOO0O00 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:231
    if OOOO00O00OOOO0O00 =='2':#line:232
        O0000OOO0O00O0O00 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:233
        OO0OOO00OO000OO00 =[OOO00O00OOOOOOOO0 .strip ()for OOO00O00OOOOOOOO0 in O0000OOO0O00O0O00 if OOO00O00OOOOOOOO0 .strip ()]#line:234
    else :#line:235
        OO0OOO00OO000OO00 =[]#line:236
        for OOO0OOOO0O0OO000O in OO0000O00O0O0O0OO :#line:237
            try :#line:238
                OO0OOO00OO000OO00 .extend (fetch_channels (OOO0OOOO0O0OO000O ,OO00O0O00OO00O00O ))#line:239
            except Exception as O0O00OOOOOO0OOOOO :#line:240
                print (f"[!] Failed to fetch channels for token. Error: {O0O00OOOOOO0OOOOO}")#line:241
                continue #line:242
        random .shuffle (OO0OOO00OO000OO00 )#line:243
    O00OOOO000OO0OO0O =input ("Delay between reactions (in seconds)?: ").strip ()#line:245
    try :#line:247
        O00OOOO000OO0OO0O =float (O00OOOO000OO0OO0O )#line:248
        if O00OOOO000OO0OO0O <0 :#line:249
            raise ValueError #line:250
    except ValueError :#line:251
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:252
        O00OOOO000OO0OO0O =1.0 #line:253
    try :#line:255
        with open ("art.txt",encoding ="utf-8")as OO0OO0O0O000OO0OO :#line:256
            OOO00OOO00O0O0000 =[O0OOO000OOOO0O00O .strip ()for O0OOO000OOOO0O00O in OO0OO0O0O000OO0OO .readlines ()if O0OOO000OOOO0O00O .strip ()]#line:257
    except (FileNotFoundError ,KeyError ):#line:258
        print (f"{colorama.Fore.RED}    [!] Error: art.txt file not found or empty!{colorama.Fore.RESET}")#line:259
        return #line:260
    except UnicodeDecodeError as O0O00OOOOOO0OOOOO :#line:261
        print (f"{colorama.Fore.RED}    [!] Error decoding art.txt: {str(O0O00OOOOOO0OOOOO)}{colorama.Fore.RESET}")#line:262
        return #line:263
    if not OOO00OOO00O0O0000 :#line:265
        print (f"{colorama.Fore.RED}    [!] No valid art provided in art.txt!{colorama.Fore.RESET}")#line:266
        return #line:267
    OOO00OOO00O0O0000 .reverse ()#line:270
    for OOO0OOOO0O0OO000O in OO0000O00O0O0O0OO :#line:272
        for OOO0OOOO000O0O0OO in OO0OOO00OO000OO00 :#line:273
            try :#line:274
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {OOO0OOOO000O0O0OO}...{colorama.Fore.RESET}")#line:275
                O000O00O0OOO0OOOO =fetch_messages (OOO0OOOO0O0OO000O ,OOO0OOOO000O0O0OO ,limit =100 )#line:278
                if not O000O00O0OOO0OOOO :#line:279
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:280
                    continue #line:281
                for O0O000OOOO0O000OO ,OO000OO00O0OOO000 in enumerate (O000O00O0OOO0OOOO ):#line:284
                    O0O0OO0OO00O0O0OO =OOO00OOO00O0O0000 [O0O000OOOO0O000OO %len (OOO00OOO00O0O0000 )].split (',')#line:285
                    for O0OO00OOOOO000O0O in O0O0OO0OO00O0O0OO :#line:286
                        reactionput (OOO0OOOO0O0OO000O ,OOO0OOOO000O0O0OO ,OO000OO00O0OOO000 ['id'],O0OO00OOOOO000O0O .strip ())#line:287
                        print (f"Adding reaction '{O0OO00OOOOO000O0O.strip()}' to message {OO000OO00O0OOO000['id']} in channel {OOO0OOOO000O0O0OO}")#line:288
                        time .sleep (O00OOOO000OO0OO0O )#line:289
            except Exception as O0O00OOOOOO0OOOOO :#line:290
                print (f"[!] Error processing channel {OOO0OOOO000O0O0OO}. Error: {O0O00OOOOOO0OOOOO}")#line:291
                continue #line:292
    def O0000OO00OOOOO0OO (O00OO00OO00OOOO00 ):#line:297
        for OO0O0O0O0O000O00O in OO0OOO00OO000OO00 :#line:298
            try :#line:299
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {OO0O0O0O0O000O00O}...{colorama.Fore.RESET}")#line:300
                OOO0O0OO0O000OO00 =fetch_messages (O00OO00OO00OOOO00 ,OO0O0O0O0O000O00O ,limit =100 )#line:301
                if not OOO0O0OO0O000OO00 :#line:302
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:303
                    continue #line:304
                for O0000000OOO0O00O0 in OOO0O0OO0O000OO00 :#line:306
                    for O00O0OOO00OOO0O00 in O0O0OO0OO00O0O0OO :#line:307
                        reactionput (O00OO00OO00OOOO00 ,OO0O0O0O0O000O00O ,O0000000OOO0O00O0 ['id'],O00O0OOO00OOO0O00 )#line:308
                        time .sleep (O00OOOO000OO0OO0O )#line:309
            except Exception as OO0000O0O000O000O :#line:310
                print (f"[!] Error processing channel {OO0O0O0O0O000O00O}. Error: {OO0000O0O000O000O}")#line:311
                continue #line:312
    with concurrent .futures .ThreadPoolExecutor ()as O0000OO000O00O00O :#line:314
        OOO000O000O0O000O =[O0000OO000O00O00O .submit (O0000OO00OOOOO0OO ,O0000O0O000000000 )for O0000O0O000000000 in OO0000O00O0O0O0OO ]#line:315
        concurrent .futures .wait (OOO000O000O0O000O )#line:316
def update_group_ids ():#line:319
    try :#line:320
        with open ("token.txt")as O000OOOOOO000O0O0 :#line:321
            OO000O0O0OO0O00OO =[OOOOOO000OO000000 .strip ()for OOOOOO000OO000000 in O000OOOOOO000O0O0 .readlines ()if OOOOOO000OO000000 .strip ()]#line:322
        O0O0OOOO0O00O0OO0 =OO000O0O0OO0O00OO [0 ]#line:323
    except (FileNotFoundError ,KeyError ):#line:324
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:325
        return #line:326
    O0OOO00OOO0OO00OO ={"Authorization":O0O0OOOO0O00O0OO0 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:332
    OOO0000000000O0OO =requests .get ('https://discord.com/api/v9/users/@me/channels',headers =O0OOO00OOO0OO00OO )#line:334
    if OOO0000000000O0OO .status_code ==200 :#line:335
        OOO0OOO0OOO0000O0 =OOO0000000000O0OO .json ()#line:336
        with open ("group_id.txt","w")as O0O00OOOO0O0O000O :#line:337
            for OOO000OO00O00O000 in OOO0OOO0OOO0000O0 :#line:338
                if OOO000OO00O00O000 ['type']==3 :#line:339
                    O0O00OOOO0O0O000O .write (OOO000OO00O00O000 ['id']+'\n')#line:340
        print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Group IDs updated successfully.{colorama.Fore.RESET}")#line:341
    else :#line:342
        print (f"{colorama.Fore.LIGHTRED_EX}    [!] Failed to retrieve group IDs. HTTP Status Code: {OOO0000000000O0OO.status_code}{colorama.Fore.RESET}")#line:343
import requests #line:345
import requests #line:347
def fetch_channels (OOO00000OO0O0O0OO ,O0OOOO0O00O00OO0O ):#line:349
    try :#line:350
        O0O0O0OOO00000000 =requests .Session ()#line:351
        OOO00OO00OOO00000 =get_headers (OOO00000OO0O0O0OO )#line:352
        OO00O0O00OOO0OOO0 =O0O0O0OOO00000000 .get (f"https://discord.com/api/v9/guilds/{O0OOOO0O00O00OO0O}/channels",headers =OOO00OO00OOO00000 ,timeout =10 )#line:359
        if OO00O0O00OOO0OOO0 .status_code ==200 :#line:362
            try :#line:363
                OO000O000O00O0O00 =OO00O0O00OOO0OOO0 .json ()#line:364
                return [O0000OOO0000O0000 ['id']for O0000OOO0000O0000 in OO000O000O00O0O00 if O0000OOO0000O0000 .get ('type')==0 ]#line:365
            except ValueError :#line:366
                print ("[!] Error: Response was not valid JSON.")#line:367
                return []#line:368
        elif OO00O0O00OOO0OOO0 .status_code ==401 :#line:369
            print ("[!] Error: Unauthorized - check your token.")#line:370
        elif OO00O0O00OOO0OOO0 .status_code ==403 :#line:371
            print ("[!] Error: Forbidden - you lack permissions.")#line:372
        elif OO00O0O00OOO0OOO0 .status_code ==404 :#line:373
            print ("[!] Error: Server not found - check the server ID.")#line:374
        else :#line:375
            print (f"[!] Error: Unexpected status code {OO00O0O00OOO0OOO0.status_code}.")#line:376
        return []#line:379
    except requests .exceptions .Timeout :#line:381
        print ("[!] Error: Request timed out. Check your connection or try again later.")#line:382
        return []#line:383
    except requests .exceptions .RequestException as O0000OOO00O00O0O0 :#line:384
        print (f"[!] Error: An error occurred while fetching channels: {O0000OOO00O00O0O0}")#line:385
        return []#line:386
def extract_uids_from_messages (OO000OO0O0000OO00 ):#line:392
    O0O00OO00O00O00O0 =set ()#line:393
    for O0O0O0OOO000O000O in OO000OO0O0000OO00 :#line:394
        O0O00OO00O00O00O0 .add (O0O0O0OOO000O000O ['author']['id'])#line:395
    return list (O0O00OO00O00O00O0 )#line:396
def send_message_with_mention (O00OO0O0OO0O0OO0O ,OOO00OOOOO00OOO00 ,O00OOO00O0O000000 ,O00O0000O0O0000OO ):#line:398
    OO0000000OO0OOOO0 =get_session ()#line:399
    OOO0OO000O0OO0OO0 =get_headers (O00OO0O0OO0O0OO0O )#line:400
    if O00O0000O0O0000OO :#line:402
        OOOOO0OO0O0OOOO0O =random .choice (O00O0000O0O0000OO )#line:403
        O00OOO00O0O000000 +=f" <@{OOOOO0OO0O0OOOO0O}>"#line:404
    OO000OO00000OOO0O =OO0000000OO0OOOO0 .post (f"https://discord.com/api/v9/channels/{OOO00OOOOO00OOO00}/messages",headers =OOO0OO000O0OO0OO0 ,json ={"content":O00OOO00O0O000000 })#line:410
    if OO000OO00000OOO0O .status_code in [200 ,201 ]:#line:411
        print (f"[+] Message sent to channel {OOO00OOOOO00OOO00}")#line:412
    elif OO000OO00000OOO0O .status_code ==429 :#line:413
        print ("[-] Rate limited. Please wait before retrying.")#line:414
        OOO00OOOOO00OO0O0 =OO000OO00000OOO0O .json ().get ("retry_after",1 )#line:415
        time .sleep (OOO00OOOOO00OO0O0 )#line:416
    else :#line:417
        print (f"[!] Error occurred: {OO000OO00000OOO0O.status_code}")#line:418
def send_messages_with_mentions ():#line:419
    try :#line:420
        with open ("token.txt")as O00OO00O000OOO0O0 :#line:421
            OOO0O0O0OOO0OO0O0 =[O0OO00OOO0OOO00O0 .strip ()for O0OO00OOO0OOO00O0 in O00OO00O000OOO0O0 .readlines ()if O0OO00OOO0OOO00O0 .strip ()]#line:422
    except (FileNotFoundError ,KeyError ):#line:423
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:424
        return #line:425
    OOO00OO00O0OOO0O0 =input ("Server ID?: ").strip ()#line:427
    O000O0OO0O0O0O0OO =input ("Delay between messages (in seconds)?: ").strip ()#line:428
    O0OOOO0OO0O000000 =input ("Number of messages to send?: ").strip ()#line:429
    OOO0OO0OOOO0O0000 =input ("Message content?: ").strip ()#line:430
    O00OO000O0OO00OOO =input ("Blacklist User IDs (comma-separated)?: ").strip ().split (',')#line:431
    O00OO000O0OO00OOO =[OOO0000OO000O00O0 .strip ()for OOO0000OO000O00O0 in O00OO000O0OO00OOO if OOO0000OO000O00O0 .strip ()]#line:432
    try :#line:434
        O000O0OO0O0O0O0OO =float (O000O0OO0O0O0O0OO )#line:435
        if O000O0OO0O0O0O0OO <0 :#line:436
            raise ValueError #line:437
    except ValueError :#line:438
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:439
        O000O0OO0O0O0O0OO =1.0 #line:440
    try :#line:442
        O0OOOO0OO0O000000 =int (O0OOOO0OO0O000000 )#line:443
        if O0OOOO0OO0O000000 <=0 :#line:444
            raise ValueError #line:445
    except ValueError :#line:446
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:447
        O0OOOO0OO0O000000 =1 #line:448
    O0O0OOOO0000000O0 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:450
    if O0O0OOOO0000000O0 =='2':#line:451
        O0O0OOOO0O00OOO00 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:452
        O0O0OOOO0O00OOO00 =[OO0O0OOOOO00O0OO0 .strip ()for OO0O0OOOOO00O0OO0 in O0O0OOOO0O00OOO00 if OO0O0OOOOO00O0OO0 .strip ()]#line:453
    else :#line:454
        O0O0OOOO0O00OOO00 =[]#line:455
    OOOOO0O0O00OOOOOO =set ()#line:457
    for O00OO0O00O00000O0 in OOO0O0O0OOO0OO0O0 :#line:458
        OO000O000OOO0O0OO =fetch_channels (O00OO0O00O00000O0 ,OOO00OO00O0OOO0O0 )#line:459
        for O00OOOO0O00O00O0O in OO000O000OOO0O0OO :#line:460
            O0OOO0OO00O000O00 =fetch_messages (O00OO0O00O00000O0 ,O00OOOO0O00O00O0O ,limit =100 )#line:461
            OO000OO00OO0OOOOO =extract_uids_from_messages (O0OOO0OO00O000O00 )#line:462
            OOOOO0O0O00OOOOOO .update (OO000OO00OO0OOOOO )#line:463
    OOOOO0O0O00OOOOOO =list (set (OOOOO0O0O00OOOOOO )-set (O00OO000O0OO00OOO ))#line:466
    for _OO0O00O0OOOO0O0OO in range (O0OOOO0OO0O000000 ):#line:468
        for O00OO0O00O00000O0 in OOO0O0O0OOO0OO0O0 :#line:469
            if O0O0OOOO0O00OOO00 :#line:470
                OO000O000OOO0O0OO =O0O0OOOO0O00OOO00 #line:471
            for O00OOOO0O00O00O0O in OO000O000OOO0O0OO :#line:472
                send_message_with_mention (O00OO0O00O00000O0 ,O00OOOO0O00O00O0O ,OOO0OO0OOOO0O0000 ,OOOOO0O0O00OOOOOO )#line:473
                time .sleep (O000O0OO0O0O0O0OO )#line:474
def join_discord_invite ():#line:479
    try :#line:480
        with open ("token.txt")as O00OO0OO0O0O0OOO0 :#line:481
            OOOOOOOO00OO0O000 =[O0000000O0OOO00OO .strip ()for O0000000O0OOO00OO in O00OO0OO0O0O0OOO0 .readlines ()if O0000000O0OOO00OO .strip ()]#line:482
    except (FileNotFoundError ,KeyError ):#line:483
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:484
        return #line:485
    OOOO00O000000OOO0 =input ("Invite Code?: discord.gg/").strip ()#line:487
    for OOOOOOOOO00OOO0O0 in OOOOOOOO00OO0O000 :#line:490
        joiner (OOOOOOOOO00OOO0O0 ,OOOO00O000000OOO0 )#line:491
import json ,time ,base64 ,random ,requests #line:493
def cookieset (OOO0OO000O0OO0OOO ):#line:495
    OOO0OO00O00OO0OO0 =OOO0OO000O0OO0OOO .get ("https://discord.com/app")#line:496
    return OOO0OO00O00OO0OO0 .cookies .get_dict ()#line:497
def generatexspandua (O000OOO00OOOO0O0O ):#line:499
    OO0OO0OO0000O00O0 =["Android","Windows","Macintosh"]#line:500
    OO0OOOO00000OOO00 =random .choice (OO0OO0OO0000O00O0 )#line:501
    if OO0OOOO00000OOO00 =="Macintosh":#line:502
        O00OO0O000000OO0O =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:503
        O000OO0OOO0OOO0OO ="Macintosh; Intel Mac OS X "+O00OO0O000000OO0O #line:504
        OO000OO0OOO00O0O0 ="x86_64"#line:505
    elif OO0OOOO00000OOO00 =="Windows":#line:506
        O00OO0O000000OO0O =f'{random.choice([6.0, 10.0, 11.0])}'#line:507
        O000OO0OOO0OOO0OO ="Windows NT "+O00OO0O000000OO0O +" Win64; x64"#line:508
        OO000OO0OOO00O0O0 ="x86_64"#line:509
    else :#line:510
        O00OO0O000000OO0O ="13"#line:511
        O000OO0OOO0OOO0OO =f"Linux; Android 13; Pixel 6a"#line:512
        OO000OO0OOO00O0O0 ="aarch64"#line:513
    O0OO0O00OOO0OO0OO ={"os":OO0OOOO00000OOO00 ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":O00OO0O000000OO0O ,"os_arch":OO000OO0OOO00O0O0 ,"system_locale":"ja-JP","client_build_number":O000OOO00OOOO0O0O ,"client_event_source":None ,"design_id":0 }#line:526
    OO0OOO0O0OOOOO0OO =f"Mozilla/5.0 ({O000OO0OOO0OOO0OO}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:527
    return base64 .b64encode (json .dumps (O0OO0O00OOO0OO0OO ,separators =(',',':')).encode ()).decode (),OO0OOO0O0OOOOO0OO #line:528
def joiner (OO00OO000OOOOOO00 ,O0O0O00OO0OO0O000 ,O0OO0000O00OO0O00 ,O00OOOO0OO0O0OOO0 ):#line:530
  O00OOO0OO0OO0O0OO =get_session (O0OO0000O00OO0O00 )#line:531
  O0O0O000O0O0OO000 =cookieset (O00OOO0OO0OO0O0OO )#line:532
  O0O0O000O0O0OO000 ["locale"]="ja-JP"#line:533
  OO00O0OO00O00O0OO =201211 #line:534
  OOOOO000000000OO0 ,OOOO0O00000OO000O =generatexspandua (OO00O0OO00O00O0OO )#line:535
  O0OO0OO0O0OO00OOO ={"Authorization":OO00OO000OOOOOO00 ,"accept":"*/*","accept-language":"ja-JP","connection":"keep-alive","DNT":"1","origin":"https://discord.com","sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","referer":"https://discord.com/channels/@me","TE":"Trailers","user-agent":OOOO0O00000OO000O ,"X-Super-Properties":OOOOO000000000OO0 ,}#line:550
  O00O00OO0O000OOO0 =O00OOO0OO0OO0O0OO .post ("https://discord.com/api/v9/invites/"+O0O0O00OO0OO0O000 ,headers =O0OO0OO0O0OO00OOO ,json ={},cookies =O0O0O000O0O0OO000 )#line:552
  if O00O00OO0O000OOO0 .status_code ==200 :#line:553
    print ("[+] Probably joined "+OO00OO000OOOOOO00 )#line:554
    if "show_verification_form"in O00O00OO0O000OOO0 .json ():#line:555
      bypass (OO00OO000OOOOOO00 ,O00O00OO0O000OOO0 .json ()["guild"]["id"],O00OOO0OO0OO0O0OO ,O0OO0OO0O0OO00OOO )#line:556
    return #line:557
  elif "captcha_key"in O00O00OO0O000OOO0 .text and O00O00OO0O000OOO0 .status_code ==400 :#line:558
    print ("[!] Hcaptcha interference "+OO00OO000OOOOOO00 )#line:559
    return #line:560
  elif O00O00OO0O000OOO0 .status_code ==401 :#line:561
    print ("[!] Token is dead "+OO00OO000OOOOOO00 )#line:562
    return #line:563
  elif O00O00OO0O000OOO0 .status_code ==403 :#line:564
    if "message"in O00O00OO0O000OOO0 .json ():#line:565
      if O00O00OO0O000OOO0 .json ()["message"]=="Unknown Message":#line:566
        print ("[!] Unknown error "+OO00OO000OOOOOO00 )#line:567
        return #line:568
      else :#line:569
        print ("[!] Verification required "+OO00OO000OOOOOO00 )#line:570
        return #line:571
    else :#line:572
      print ("[!] Error occurred "+OO00OO000OOOOOO00 )#line:573
      return #line:574
  elif O00O00OO0O000OOO0 .status_code ==429 :#line:575
    print ("[!] Token rate-limited "+OO00OO000OOOOOO00 )#line:576
    return #line:577
  elif O00O00OO0O000OOO0 .status_code ==400 :#line:578
    if "captcha_key"in O00O00OO0O000OOO0 .json ():#line:579
      print ("[!] Hcaptcha interference "+OO00OO000OOOOOO00 )#line:580
      return #line:581
    else :#line:582
      print ("[!] Error occurred "+OO00OO000OOOOOO00 )#line:583
      return #line:584
  elif O00O00OO0O000OOO0 .status_code ==401 :#line:585
    print ("[!] Token is dead "+OO00OO000OOOOOO00 )#line:586
    return #line:587
  elif O00O00OO0O000OOO0 .status_code ==403 :#line:588
    if "message"in O00O00OO0O000OOO0 .json ():#line:589
      if O00O00OO0O000OOO0 .json ()["message"]=="Unknown Message":#line:590
        print ("[!] Unknown error "+OO00OO000OOOOOO00 )#line:591
        return #line:592
      else :#line:593
        print ("[!] Verification required "+OO00OO000OOOOOO00 )#line:594
        return #line:595
    else :#line:596
      print ("[!] Error occurred "+OO00OO000OOOOOO00 )#line:597
  elif O00O00OO0O000OOO0 .status_code ==429 :#line:598
    print ("[!] Token rate-limited "+OO00OO000OOOOOO00 )#line:599
    return #line:600
  else :#line:601
    print ("[!] Error occurred "+OO00OO000OOOOOO00 )#line:602
    return #line:603
def update_group_ids ():#line:606
    OO0OO00OO0OO0O000 =input ("Invite Code?: ").strip ()#line:607
    try :#line:608
        with open ("token.txt")as OO0O0000OOOO00OOO :#line:609
            O0O0OOOO0OOO0OO0O =[OOOO0O0O00O000000 .strip ()for OOOO0O0O00O000000 in OO0O0000OOOO00OOO .readlines ()if OOOO0O0O00O000000 .strip ()]#line:610
    except (FileNotFoundError ,KeyError ):#line:611
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:612
        return #line:613
    OOOOO00000O00OO0O =requests .Session ()#line:615
    for O0000O0OO000000O0 in O0O0OOOO0OOO0OO0O :#line:616
        joiner (O0000O0OO000000O0 ,OO0OO00OO0OO0O000 ,OOOOO00000O00OO0O )#line:617
        time .sleep (2 )#line:618
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:620
def bypass (OO0OOO00000OO0OOO ,OO00OO0000O0O0000 ,O00O00O0OO0OOOOOO ,O00O0O000O00OOOOO ):#line:623
    try :#line:624
        OO0OOOO0O0OO0O00O =O00O00O0OO0OOOOOO .get (f"https://discord.com/api/v9/guilds/{OO00OO0000O0O0000}/member-verification?with_guild=false",headers =O00O0O000O00OOOOO ).json ()#line:625
        O00OOOOO0000O0O00 =O00O00O0OO0OOOOOO .put (f"https://discord.com/api/v9/guilds/{OO00OO0000O0O0000}/requests/@me",headers =O00O0O000O00OOOOO ,json =OO0OOOO0O0OO0O00O )#line:626
        if O00OOOOO0000O0O00 .status_code ==201 :#line:627
            print (f"[+] MemberscreeningBypassed {OO0OOO00000OO0OOO}")#line:628
            return #line:629
        else :#line:630
            print (f"[!] Bypassが出来ませんでした {OO0OOO00000OO0OOO}")#line:631
            return #line:632
    except Exception as OO0O0000OO00O000O :#line:633
        print (f"[!] エラーが発生しました。{OO0O0000OO00O000O}")#line:634
session =requests .Session ()#line:636
def reactionput (OO0000OOOO0O0O00O ,OOOOOOO0OOO0O0OO0 ,OOO00OOOO0000OO00 ,OO0OOOOO0000OOOO0 ,proxy =None ):#line:639
    O00O0OO0O00OOOO0O =get_session (proxy )#line:640
    O0OOOO00OO000O00O =get_headers (O00O0OO0O00OOOO0O )#line:641
    O0OOOO00OO000O00O ["Authorization"]=OO0000OOOO0O0O00O #line:642
    OO0OOOOO0000OOOO0 =requests .utils .quote (OO0OOOOO0000OOOO0 )#line:644
    OO00OO0OOOO000OOO =O00O0OO0O00OOOO0O .put (f"https://discord.com/api/v9/channels/{OOOOOOO0OOO0O0OO0}/messages/{OOO00OOOO0000OO00}/reactions/{OO0OOOOO0000OOOO0}/%40me?location=Message&type=0",headers =O0OOOO00OO000O00O )#line:648
    if OO00OO0OOOO000OOO .status_code in [200 ,204 ]:#line:649
        print (f"[+] Reaction '{OO0OOOOO0000OOOO0}' added successfully to message {OOO00OOOO0000OO00}")#line:650
    elif OO00OO0OOOO000OOO .status_code ==429 :#line:651
        print ("[-] Rate limited. Please wait before retrying.")#line:652
        OOOOO0OO00000O0O0 =OO00OO0OOOO000OOO .json ().get ("retry_after",1 )#line:653
        time .sleep (OOOOO0OO00000O0O0 )#line:654
    elif OO00OO0OOOO000OOO .status_code ==401 :#line:655
        print ("[-] Invalid or expired token.")#line:656
    else :#line:657
        print (f"[!] Error occurred: {OO00OO0OOOO000OOO.status_code}")#line:658
def generatexspandua (OO0O0O0O0O0O00000 ):#line:661
  O00OOO00OO000O00O =["Android","Windows","Macintosh"]#line:662
  O00O0OOO0000O0000 =random .choice (O00OOO00OO000O00O )#line:663
  if O00O0OOO0000O0000 =="Macintosh":#line:664
    O0OO00000OO00OOO0 =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:665
    OO00OOOO0O00O0O00 ="Macintosh; Intel Mac OS X "+O0OO00000OO00OOO0 #line:666
    OOO0O000O00O0O0OO ="x86_64"#line:667
  if O00O0OOO0000O0000 =="Windows":#line:668
    O0OO00000OO00OOO0 =f'{random.choice([6.0,10.0,11.0])}'#line:669
    OO00OOOO0O00O0O00 ="Windows NT "+O0OO00000OO00OOO0 +" Win64; x64"#line:670
    OOO0O000O00O0O0OO ="x86_64"#line:671
  if O00O0OOO0000O0000 =="Android":#line:672
    O0OO00000OO00OOO0 ="13"#line:673
    OO00OOOO0O00O0O00 =f"Linux; Android 13; Pixel 6a"#line:674
    OOO0O000O00O0O0OO ="aarch64"#line:675
  OO00O00O0OO0000OO ={"os":O00O0OOO0000O0000 ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":O0OO00000OO00OOO0 ,"os_arch":OOO0O000O00O0O0OO ,"system_locale":"ja-JP","client_build_number":OO0O0O0O0O0O00000 ,"client_event_source":None ,"design_id":0 }#line:676
  O00O0O0O0OO00OOO0 =f"Mozilla/5.0 ({OO00OOOO0O00O0O00}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:677
  return base64 .b64encode (json .dumps (OO00O00O0OO0000OO ,separators =(',',':')).encode ()).decode (),O00O0O0O0OO00OOO0 #line:678
import base64 #line:680
def nickchanger ():#line:683
    try :#line:684
        with open ("token.txt")as OOO0O0O00OO0O00OO :#line:685
            OO00000OO0O00OOO0 =[OOOOO000OOOOO000O .strip ()for OOOOO000OOOOO000O in OOO0O0O00OO0O00OO .readlines ()if OOOOO000OOOOO000O .strip ()]#line:686
    except (FileNotFoundError ,KeyError ):#line:687
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:688
        return #line:689
    OO0O0OO0O0OO0O000 =input ("Server ID?: ").strip ()#line:691
    OOOOOOOOOO0O0O0OO =input ("Nickname?: ").strip ()#line:692
    OOO0000OO00OOOO0O =input ("Delay (in seconds)?: ").strip ()#line:693
    try :#line:695
        OOO0000OO00OOOO0O =float (OOO0000OO00OOOO0O )#line:696
        if OOO0000OO00OOOO0O <0 :#line:697
            raise ValueError #line:698
    except ValueError :#line:699
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:700
        OOO0000OO00OOOO0O =1.0 #line:701
    for OOOO00OO0O0OO00O0 in OO00000OO0O00OOO0 :#line:703
        O0OOOOOOOOO0O0O0O ={"Authorization":OOOO00OO0O0OO00O0 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:708
        O0O0OOOO0O00OO0OO ={"nick":OOOOOOOOOO0O0O0OO }#line:709
        OO0OO00O000O00O00 =requests .patch (f"https://discord.com/api/v9/guilds/{OO0O0OO0O0OO0O000}/members/@me",headers =O0OOOOOOOOO0O0O0O ,json =O0O0OOOO0O00OO0OO )#line:710
        if OO0OO00O000O00O00 .status_code ==200 :#line:712
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Nickname changed to '{OOOOOOOOOO0O0O0OO}' successfully for token {OOOO00OO0O0OO00O0}.{colorama.Fore.RESET}")#line:713
        elif OO0OO00O000O00O00 .status_code ==429 :#line:714
            print (f"{colorama.Fore.RED}    [!] Rate limited. Please wait before retrying for token {OOOO00OO0O0OO00O0}.{colorama.Fore.RESET}")#line:715
            O0O00O0OO0OO0000O =OO0OO00O000O00O00 .json ().get ("retry_after",1 )#line:716
            time .sleep (O0O00O0OO0OO0000O )#line:717
        else :#line:718
            print (f"{colorama.Fore.RED}    [!] Error occurred: {OO0OO00O000O00O00.status_code} for token {OOOO00OO0O0OO00O0}.{colorama.Fore.RESET}")#line:719
        time .sleep (OOO0000OO00OOOO0O )#line:721
import json ,websocket ,threading ,tls_client ,random ,time #line:725
session =tls_client .Session (client_identifier ="chrome112",random_tls_extension_order =True )#line:727
class Utils :#line:729
    @staticmethod #line:730
    def rangeCorrector (OOO0000OOO0OO000O ):#line:731
        if [0 ,99 ]not in OOO0000OOO0OO000O :#line:732
            OOO0000OOO0OO000O .insert (0 ,[0 ,99 ])#line:733
        return OOO0000OOO0OO000O #line:734
    @staticmethod #line:736
    def getRanges (O0O000O0OOOO00OOO ,OOO0000000O0OO00O ,O0OO00OOOO000000O ):#line:737
        OO0O0O0O0000000OO =int (O0O000O0OOOO00OOO *OOO0000000O0OO00O )#line:738
        O0O0O00O00OOOOOOO =[[OO0O0O0O0000000OO ,OO0O0O0O0000000OO +99 ]]#line:739
        if O0OO00OOOO000000O >OO0O0O0O0000000OO +99 :#line:740
            O0O0O00O00OOOOOOO .append ([OO0O0O0O0000000OO +100 ,OO0O0O0O0000000OO +199 ])#line:741
        return Utils .rangeCorrector (O0O0O00O00OOOOOOO )#line:742
    @staticmethod #line:744
    def parseGuildMemberListUpdate (OOOOO00O0000OOO0O ):#line:745
        O0O0OO0O00O0OO0O0 ={"online_count":OOOOO00O0000OOO0O ["d"]["online_count"],"member_count":OOOOO00O0000OOO0O ["d"]["member_count"],"id":OOOOO00O0000OOO0O ["d"]["id"],"guild_id":OOOOO00O0000OOO0O ["d"]["guild_id"],"hoisted_roles":OOOOO00O0000OOO0O ["d"]["groups"],"types":[],"locations":[],"updates":[],}#line:755
        for O00OOOOO0O0OO00OO in OOOOO00O0000OOO0O ["d"]["ops"]:#line:757
            O0O0OO0O00O0OO0O0 ["types"].append (O00OOOOO0O0OO00OO ["op"])#line:758
            if O00OOOOO0O0OO00OO ["op"]in ("SYNC","INVALIDATE"):#line:759
                O0O0OO0O00O0OO0O0 ["locations"].append (O00OOOOO0O0OO00OO ["range"])#line:760
                if O00OOOOO0O0OO00OO ["op"]=="SYNC":#line:761
                    O0O0OO0O00O0OO0O0 ["updates"].append (O00OOOOO0O0OO00OO ["items"])#line:762
                else :#line:763
                    O0O0OO0O00O0OO0O0 ["updates"].append ([])#line:764
            elif O00OOOOO0O0OO00OO ["op"]in ("INSERT","UPDATE","DELETE"):#line:765
                O0O0OO0O00O0OO0O0 ["locations"].append (O00OOOOO0O0OO00OO ["index"])#line:766
                if O00OOOOO0O0OO00OO ["op"]=="DELETE":#line:767
                    O0O0OO0O00O0OO0O0 ["updates"].append ([])#line:768
                else :#line:769
                    O0O0OO0O00O0OO0O0 ["updates"].append (O00OOOOO0O0OO00OO ["item"])#line:770
        return O0O0OO0O00O0OO0O0 #line:771
class DiscordSocket (websocket .WebSocketApp ):#line:773
    def __init__ (OO0000OOO000OO000 ,OOO00OO000OO000OO ,O0000O0OOOO0O0O0O ,O0O000OOOO000000O ):#line:774
        OO0000OOO000OO000 .token =OOO00OO000OO000OO #line:775
        OO0000OOO000OO000 .guild_id =O0000O0OOOO0O0O0O #line:776
        OO0000OOO000OO000 .channel_id =O0O000OOOO000000O #line:777
        OO0000OOO000OO000 .socket_headers ={"Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","Cache-Control":"no-cache","Pragma":"no-cache","Sec-WebSocket-Extensions":"permessage-deflate; client_max_window_bits","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",}#line:785
        super ().__init__ ("wss://gateway.discord.gg/?encoding=json&v=9",header =OO0000OOO000OO000 .socket_headers ,on_open =lambda OOO00OO0000OO0000 :OO0000OOO000OO000 .sock_open (OOO00OO0000OO0000 ),on_message =lambda OO00OO0000O000000 ,O00OO0OOO00000O00 :OO0000OOO000OO000 .sock_message (OO00OO0000O000000 ,O00OO0OOO00000O00 ),on_close =lambda O0000000OOO000000 ,OO000O0OOOOO000OO ,O00OOO00OO0O00O00 :OO0000OOO000OO000 .sock_close (O0000000OOO000000 ,OO000O0OOOOO000OO ,O00OOO00OO0O00O00 ),)#line:794
        OO0000OOO000OO000 .endScraping =False #line:796
        OO0000OOO000OO000 .guilds ={}#line:797
        OO0000OOO000OO000 .members ={}#line:798
        OO0000OOO000OO000 .ranges =[[0 ,0 ]]#line:799
        OO0000OOO000OO000 .lastRange =0 #line:800
        OO0000OOO000OO000 .packets_recv =0 #line:801
    def run (OO000O00O000OOOO0 ):#line:803
        OO000O00O000OOOO0 .run_forever ()#line:804
        return OO000O00O000OOOO0 .members #line:805
    def scrapeUsers (OO0OOO0OOO0OOOOOO ):#line:807
        if not OO0OOO0OOO0OOOOOO .endScraping :#line:808
            OO0OOO0OOO0OOOOOO .send ('{"op":14,"d":{"guild_id":"'+OO0OOO0OOO0OOOOOO .guild_id +'","typing":true,"activities":true,"threads":true,"channels":{"'+OO0OOO0OOO0OOOOOO .channel_id +'":'+json .dumps (OO0OOO0OOO0OOOOOO .ranges )+"}}}")#line:817
    def sock_open (O0O00O0OO000O0O0O ,O0OO0OOOO00O00000 ):#line:819
        O0O00O0OO000O0O0O .send ('{"op":2,"d":{"token":"'+O0O00O0OO000O0O0O .token +'","capabilities":125,"properties":{"os":"Windows NT","browser":"Chrome","device":"","system_locale":"it-IT","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36","browser_version":"119.0","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":103981,"client_event_source":null},"presence":{"status":"online","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}')#line:824
    def heartbeatThread (O0O0000000000O0O0 ,O0OOOO0OOOOO0O000 ):#line:826
        try :#line:827
            while True :#line:828
                O0O0000000000O0O0 .send ('{"op":1,"d":'+str (O0O0000000000O0O0 .packets_recv )+"}")#line:829
                time .sleep (O0OOOO0OOOOO0O000 )#line:830
        except Exception as OO0O0O0OOOO0OO000 :#line:831
            pass #line:832
    def sock_message (O0OO000OOO0O0O0OO ,OOO00000O000O00OO ,O00OOOO0OO00000OO ):#line:834
        OOOO0O0000O0O0OOO =json .loads (O00OOOO0OO00000OO )#line:835
        if OOOO0O0000O0O0OOO is None :#line:836
            return #line:837
        if OOOO0O0000O0O0OOO ["op"]!=11 :#line:838
            O0OO000OOO0O0O0OO .packets_recv +=1 #line:839
        if OOOO0O0000O0O0OOO ["op"]==10 :#line:840
            threading .Thread (target =O0OO000OOO0O0O0OO .heartbeatThread ,args =(OOOO0O0000O0O0OOO ["d"]["heartbeat_interval"]/1000 ,),daemon =True ,).start ()#line:845
        if OOOO0O0000O0O0OOO ["t"]=="READY":#line:846
            for O0OOO0O0O0000O0OO in OOOO0O0000O0O0OOO ["d"]["guilds"]:#line:847
                O0OO000OOO0O0O0OO .guilds [O0OOO0O0O0000O0OO ["id"]]={"member_count":O0OOO0O0O0000O0OO ["member_count"]}#line:848
        if OOOO0O0000O0O0OOO ["t"]=="READY_SUPPLEMENTAL":#line:849
            O0OO000OOO0O0O0OO .ranges =Utils .getRanges (0 ,100 ,O0OO000OOO0O0O0OO .guilds [O0OO000OOO0O0O0OO .guild_id ]["member_count"])#line:852
            O0OO000OOO0O0O0OO .scrapeUsers ()#line:853
        elif OOOO0O0000O0O0OOO ["t"]=="GUILD_MEMBER_LIST_UPDATE":#line:854
            O000OOO0O000OOOOO =Utils .parseGuildMemberListUpdate (OOOO0O0000O0O0OOO )#line:855
            if O000OOO0O000OOOOO ["guild_id"]==O0OO000OOO0O0O0OO .guild_id and ("SYNC"in O000OOO0O000OOOOO ["types"]or "UPDATE"in O000OOO0O000OOOOO ["types"]):#line:859
                for O0OO00O0O00000OO0 ,O00OOOO000OO00O0O in enumerate (O000OOO0O000OOOOO ["types"]):#line:860
                    if O00OOOO000OO00O0O =="SYNC":#line:861
                        if len (O000OOO0O000OOOOO ["updates"][O0OO00O0O00000OO0 ])==0 :#line:862
                            O0OO000OOO0O0O0OO .endScraping =True #line:863
                            break #line:864
                        for O000O00000OOOOOOO in O000OOO0O000OOOOO ["updates"][O0OO00O0O00000OO0 ]:#line:866
                            if "member"in O000O00000OOOOOOO :#line:867
                                OOOOO0OOO0O0000O0 =O000O00000OOOOOOO ["member"]#line:868
                                O0O0OOO0OOO0OO0OO ={"tag":OOOOO0OOO0O0000O0 ["user"]["username"]+"#"+OOOOO0OOO0O0000O0 ["user"]["discriminator"],"id":OOOOO0OOO0O0000O0 ["user"]["id"],}#line:874
                                if not OOOOO0OOO0O0000O0 ["user"].get ("bot"):#line:875
                                    O0OO000OOO0O0O0OO .members [OOOOO0OOO0O0000O0 ["user"]["id"]]=O0O0OOO0OOO0OO0OO #line:876
                    elif O00OOOO000OO00O0O =="UPDATE":#line:878
                        for O000O00000OOOOOOO in O000OOO0O000OOOOO ["updates"][O0OO00O0O00000OO0 ]:#line:879
                            if "member"in O000O00000OOOOOOO :#line:880
                                OOOOO0OOO0O0000O0 =O000O00000OOOOOOO ["member"]#line:881
                                O0O0OOO0OOO0OO0OO ={"tag":OOOOO0OOO0O0000O0 ["user"]["username"]+"#"+OOOOO0OOO0O0000O0 ["user"]["discriminator"],"id":OOOOO0OOO0O0000O0 ["user"]["id"],}#line:887
                                if not OOOOO0OOO0O0000O0 ["user"].get ("bot"):#line:888
                                    O0OO000OOO0O0O0OO .members [OOOOO0OOO0O0000O0 ["user"]["id"]]=O0O0OOO0OOO0OO0OO #line:889
                    O0OO000OOO0O0O0OO .lastRange +=1 #line:891
                    O0OO000OOO0O0O0OO .ranges =Utils .getRanges (O0OO000OOO0O0O0OO .lastRange ,100 ,O0OO000OOO0O0O0OO .guilds [O0OO000OOO0O0O0OO .guild_id ]["member_count"])#line:894
                    time .sleep (0.45 )#line:895
                    O0OO000OOO0O0O0OO .scrapeUsers ()#line:896
            if O0OO000OOO0O0O0OO .endScraping :#line:898
                O0OO000OOO0O0O0OO .close ()#line:899
    def sock_close (OO00OOOOO00000O00 ,OO0O0OOO0OO0O0O0O ,OOOO000O0O0OO00OO ,O0OOOOOOO0OO0O0O0 ):#line:901
        pass #line:902
def scrape (O00O0O0OO0O0O0000 ,O00OOOOO0OOO0000O ,OOOOOO000000O000O ):#line:904
    OO0OOOOO0O0O00OO0 =DiscordSocket (O00O0O0OO0O0O0000 ,O00OOOOO0OOO0000O ,OOOOOO000000O000O )#line:905
    return OO0OOOOO0O0O00OO0 .run ()#line:906
def member_scrape (O000OOOO00000OO00 ,OO00OOO00000OO0O0 ,O00O00O0000000000 ):#line:908
    O0OO0OO00OO00OO0O =[]#line:909
    for OOO0O0000O0OO0OOO in O000OOOO00000OO00 :#line:910
        O0OO0000OOOOOO00O ={"Authorization":OOO0O0000O0OO0OOO ,"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}#line:911
        O0O00OOOOO0O0OOOO =session .get (f"https://canary.discord.com/api/v9/guilds/{OO00OOO00000OO0O0}",headers =O0OO0000OOOOOO00O )#line:912
        if O0O00OOOOO0O0OOOO .status_code ==200 :#line:913
            O0OO0OO00OO00OO0O .append (OOO0O0000O0OO0OOO )#line:914
            break #line:915
    if not O0OO0OO00OO00OO0O :#line:916
        print ("missing access")#line:917
    OOO0O0000O0OO0OOO =random .choice (O0OO0OO00OO00OO0O )#line:919
    OO000OO0O000O0OOO =scrape (OOO0O0000O0OO0OOO ,OO00OOO00000OO0O0 ,O00O00O0000000000 )#line:920
    OOOOO0O0O0O000OOO =[f"<@{O0OO0O0O0OO0OOO00}>"for O0OO0O0O0OO0OOO00 in [int (OOO00OO000OO00O0O )for OOO00OO000OO00O0O in OO000OO0O000O0OOO .keys ()]]#line:921
    print (f"[SUCCESS] {len(OOOOO0O0O0O000OOO)} scraped members")#line:922
    return OOOOO0O0O0O000OOO #line:923
def spammer_menu ():#line:925
    try :#line:926
        with open ("token.txt")as OO0OOO0O0OO0OOOOO :#line:927
            OOOOO00O00O00OOO0 =[OOOO0OO0O00O00OOO .strip ()for OOOO0OO0O00O00OOO in OO0OOO0O0OO0OOOOO .readlines ()if OOOO0OO0O00O00OOO .strip ()]#line:928
    except (FileNotFoundError ,KeyError ):#line:929
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:930
        return #line:931
    O0OOOOO00O0OO0OOO =input ("Server ID?: ").strip ()#line:933
    O0000O0O0OO00O0O0 =input ("Message?: ").strip ()#line:934
    O0O000OO0000O0OOO =input ("Random mention (True/False)?: ").strip ().lower ()=='true'#line:935
    O00000O00OO0OOO00 =input ("Delay between messages (in seconds)?: ").strip ()#line:936
    OOO00OO000000OOO0 =input ("Number of messages to send?: ").strip ()#line:937
    OO0OO0OO000OOO00O =input ("Blacklist User IDs (comma-separated) (Leave blank to skip)?: ").strip ().split (',')#line:938
    OO0OO0OO000OOO00O =[f"<@{O00OO00OOO00OO000.strip()}>"for O00OO00OOO00OO000 in OO0OO0OO000OOO00O if O00OO00OOO00OO000 .strip ()]#line:939
    try :#line:941
        O00000O00OO0OOO00 =float (O00000O00OO0OOO00 )#line:942
        if O00000O00OO0OOO00 <0 :#line:943
            raise ValueError #line:944
    except ValueError :#line:945
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:946
        O00000O00OO0OOO00 =1.0 #line:947
    try :#line:949
        OOO00OO000000OOO0 =int (OOO00OO000000OOO0 )#line:950
        if OOO00OO000000OOO0 <=0 :#line:951
            raise ValueError #line:952
    except ValueError :#line:953
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:954
        OOO00OO000000OOO0 =1 #line:955
    O00OOOOOOO0000000 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:957
    if O00OOOOOOO0000000 =='2':#line:958
        OOO00000O0000O0O0 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:959
        OOO00000O0000O0O0 =[O0OO0O0OO0O0OOO0O .strip ()for O0OO0O0OO0O0OOO0O in OOO00000O0000O0O0 if O0OO0O0OO0O0OOO0O .strip ()]#line:960
    else :#line:961
        OOO00000O0000O0O0 =fetch_channels (OOOOO00O00O00OOO0 [0 ],O0OOOOO00O0OO0OOO )#line:962
    OO00OOOOO0O00O000 =None #line:964
    spammer (OOOOO00O00O00OOO0 ,O0OOOOO00O0OO0OOO ,OOO00000O0000O0O0 ,O0000O0O0OO00O0O0 ,O0O000OO0000O0OOO ,OO0OO0OO000OOO00O ,OO00OOOOO0O00O000 ,OOO00OO000000OOO0 )#line:966
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:969
def buildnumget (OOOO00O000OO0OO0O ):#line:971
  OOO0OO00OO0O0O0OO =OOOO00O000OO0OO0O .get ('https://discord.com/login',headers ={'Accept-Encoding':'gzip, deflate'},timeout =7 )#line:972
  OOO0O0OOOOOOOOO0O =OOO0OO00OO0O0O0OO .text #line:973
import discum #line:975
import random #line:976
import time #line:977
def userget (O000OOOO0000000O0 ,OOOO0O0OOOOOOOOO0 ,OOO0OO0OOOO00O0OO ):#line:979
    OO000O0OO0O00OOOO =[]#line:980
    OO00O00OO000OO00O =discum .Client (token =O000OOOO0000000O0 ,log =False )#line:981
    def OOO0OO0000O0O00OO (O0OO0OOO0O0OOO000 ):#line:983
        if OO00O00OO000OO00O .gateway .finishedMemberFetching (OOOO0O0OOOOOOOOO0 ):#line:984
            OOOOOOO0O00O000OO =len (OO00O00OO000OO00O .gateway .session .guild (OOOO0O0OOOOOOOOO0 ).members )#line:985
            print (str (OOOOOOO0O00O000OO )+' members fetched')#line:986
            OO00O00OO000OO00O .gateway .removeCommand ({'function':OOO0OO0000O0O00OO ,'params':{}})#line:987
            OO00O00OO000OO00O .gateway .close ()#line:988
    def O0000OO0O0O0O0OOO (OOOOO0O0OOO00O0O0 ,OO00OOOOO0OO0O0OO ):#line:990
        OO00O00OO000OO00O .gateway .fetchMembers (OOOOO0O0OOO00O0O0 ,OO00OOOOO0OO0O0OO ,keep ='all',wait =1 )#line:991
        OO00O00OO000OO00O .gateway .command ({'function':OOO0OO0000O0O00OO ,'params':{}})#line:992
        OO00O00OO000OO00O .gateway .run ()#line:993
        OO00O00OO000OO00O .gateway .resetSession ()#line:994
        return OO00O00OO000OO00O .gateway .session .guild (OOOOO0O0OOO00O0O0 ).members #line:995
    OO0OOOO0OOOO0O0O0 =O0000OO0O0O0O0OOO (OOOO0O0OOOOOOOOO0 ,OOO0OO0OOOO00O0OO )#line:997
    for O0000O0O0000O00O0 in OO0OOOO0OOOO0O0O0 :#line:998
        if O0000O0O0000O00O0 not in OO000O0OO0O00OOOO :#line:999
            OO000O0OO0O00OOOO .append (f"<@{O0000O0O0000O00O0}>")#line:1000
    return OO000O0OO0O00OOOO #line:1001
def spammer (O0O00OOOOOO0OOO00 ,O0O0O0O00OO0O0OOO ,O0OO00O0O00O0OO0O ,O0O0O0OO0OO00OO0O ,O00OO00O0000OO000 ,O0O00O0OO00OO00OO ,OO0O0OO0OOOO00000 ,O0O00OO000OOOOO0O ):#line:1006
    OO00OOOO000O000OO =get_session (OO0O0OO0OOOO00000 )#line:1007
    O0O0OO0OO0OO0O0O0 =0 #line:1008
    O0000O00OO0O0OOO0 =userget (O0O00OOOOOO0OOO00 [0 ],O0O0O0O00OO0O0OOO ,O0OO00O0O00O0OO0O [0 ])#line:1010
    O0000O00OO0O0OOO0 =[OOOOOOOOOO0O00OOO for OOOOOOOOOO0O00OOO in O0000O00OO0O0OOO0 if OOOOOOOOOO0O00OOO not in O0O00O0OO00OO00OO ]#line:1013
    for _OOO000000O0OOO000 in range (O0O00OO000OOOOO0O ):#line:1015
        O000OOO0000000O0O =O0O00OOOOOO0OOO00 [O0O0OO0OO0OO0O0O0 ]#line:1016
        OO0000OOO00OO0OOO =get_headers (O000OOO0000000O0O )#line:1017
        for OOOO0OO0000O00000 in O0OO00O0O00O0OO0O :#line:1018
            OOOOO00OOOOOOOO00 =O0O0O0OO0OO00OO0O #line:1019
            if O00OO00O0000OO000 and O0000O00OO0O0OOO0 :#line:1020
                OO0O0O000OO00OOOO =random .choice (O0000O00OO0O0OOO0 )#line:1021
                OOOOO00OOOOOOOO00 +=f" {OO0O0O000OO00OOOO}"#line:1022
            O00OOO0O00OO00OOO =OO00OOOO000O000OO .post (f"https://discord.com/api/v9/channels/{OOOO0OO0000O00000}/messages",json ={"content":OOOOO00OOOOOOOO00 },headers =OO0000OOO00OO0OOO )#line:1024
            if O00OOO0O00OO00OOO .status_code ==200 :#line:1025
                print (f"200 message sent: {O000OOO0000000O0O}")#line:1026
            elif O00OOO0O00OO00OOO .status_code ==429 :#line:1027
                print (f"429 rate limit: {O000OOO0000000O0O}")#line:1028
                OOO0O0OOO0O0OO0OO =O00OOO0O00OO00OOO .json ().get ("retry_after",1 )#line:1029
                time .sleep (OOO0O0OOO0O0OO0OO )#line:1030
            elif O00OOO0O00OO00OOO .status_code ==401 :#line:1031
                print (f"401 unknown token: {O000OOO0000000O0O}")#line:1032
            else :#line:1033
                print (f"error: {O000OOO0000000O0O}")#line:1034
        O0O0OO0OO0OO0O0O0 =(O0O0OO0OO0OO0O0O0 +1 )%len (O0O00OOOOOO0OOO00 )#line:1036
        time .sleep (1 )#line:1037
import requests #line:1041
import base64 #line:1042
import colorama #line:1043
import time #line:1044
def add_emojis_from_files ():#line:1046
    try :#line:1047
        with open ("emojiname.txt")as OO00O00O0OO00O0O0 ,open ("emojiurl.txt")as OO0O0OOO0O00O00OO :#line:1048
            O000O00O0OO0OOOOO =[OO00OOO00O00OOO00 .strip ()for OO00OOO00O00OOO00 in OO00O00O0OO00O0O0 .read ().split (',')if OO00OOO00O00OOO00 .strip ()]#line:1049
            O000OO000000OO0O0 =[O00O000000O0O0O0O .strip ()for O00O000000O0O0O0O in OO0O0OOO0O00O00OO .read ().split (',')if O00O000000O0O0O0O .strip ()]#line:1050
    except FileNotFoundError as OO0000O0O0OO000OO :#line:1051
        print (f"{colorama.Fore.RED}    [!] Error: {str(OO0000O0O0OO000OO)}{colorama.Fore.RESET}")#line:1052
        return #line:1053
    if len (O000O00O0OO0OOOOO )!=len (O000OO000000OO0O0 ):#line:1055
        print (f"{colorama.Fore.RED}    [!] Error: The number of emoji names and URLs do not match!{colorama.Fore.RESET}")#line:1056
        return #line:1057
    try :#line:1059
        with open ("token.txt")as OO0O0OOOO0OOO00OO :#line:1060
            OOOOO0OOO00OO0O00 =[OOOOOOOOOO0O0O0O0 .strip ()for OOOOOOOOOO0O0O0O0 in OO0O0OOOO0OOO00OO .readlines ()if OOOOOOOOOO0O0O0O0 .strip ()]#line:1061
    except FileNotFoundError as OO0000O0O0OO000OO :#line:1062
        print (f"{colorama.Fore.RED}    [!] Error: {str(OO0000O0O0OO000OO)}{colorama.Fore.RESET}")#line:1063
        return #line:1064
    O0OOO0OOO000O0O0O =input ("Enter the Guild ID: ").strip ()#line:1066
    O00000OOO0O000O0O =input ("Enter the rate limit between requests (in seconds): ").strip ()#line:1067
    try :#line:1069
        O00000OOO0O000O0O =float (O00000OOO0O000O0O )#line:1070
        if O00000OOO0O000O0O <0 :#line:1071
            raise ValueError #line:1072
    except ValueError :#line:1073
        print (f"{colorama.Fore.RED}    [!] Invalid rate limit. Using default rate limit of 5 seconds.{colorama.Fore.RESET}")#line:1074
        O00000OOO0O000O0O =5.0 #line:1075
    OOO0000OO0OOO00OO =set ()#line:1077
    for O00O0O000O0OO0OO0 in OOOOO0OOO00OO0O00 :#line:1079
        OOOO0O0O00O00OO00 ={'Authorization':O00O0O000O0OO0OO0 ,'Content-Type':'application/json'}#line:1083
        OOOOOO0O0000O0O00 =requests .get (f"https://discord.com/api/v9/guilds/{O0OOO0OOO000O0O0O}/emojis",headers =OOOO0O0O00O00OO00 )#line:1086
        if OOOOOO0O0000O0O00 .status_code ==200 :#line:1087
            O0OOO0O0OOO0OO0OO =OOOOOO0O0000O0O00 .json ()#line:1088
            for OOOOO00000OOOO00O in O0OOO0O0OOO0OO0OO :#line:1089
                OOO0000OO0OOO00OO .add (OOOOO00000OOOO00O ['name'])#line:1090
        else :#line:1091
            print (f"{colorama.Fore.RED}    [!] Error fetching existing emojis: {OOOOOO0O0000O0O00.status_code} - {OOOOOO0O0000O0O00.text}{colorama.Fore.RESET}")#line:1092
            continue #line:1093
    for O000O0OOO0O00OO00 ,O0O0OO0O0OOOO0000 in zip (O000O00O0OO0OOOOO ,O000OO000000OO0O0 ):#line:1095
        if O000O0OOO0O00OO00 in OOO0000OO0OOO00OO :#line:1096
            print (f"{colorama.Fore.YELLOW}    [*] Emoji '{O000O0OOO0O00OO00}' already exists. Skipping...{colorama.Fore.RESET}")#line:1097
            continue #line:1098
        for O00O0O000O0OO0OO0 in OOOOO0OOO00OO0O00 :#line:1100
            try :#line:1101
                OOOOOO0O0000O0O00 =requests .get (O0O0OO0O0OOOO0000 )#line:1102
                OOOOOO0O0000O0O00 .raise_for_status ()#line:1103
                OO00O0O00OO0OO000 =OOOOOO0O0000O0O00 .content #line:1104
                OOOO0OOOO000O0O00 =base64 .b64encode (OO00O0O00OO0OO000 ).decode ('utf-8')#line:1105
                O00OO0O0O00OO000O ={'name':O000O0OOO0O00OO00 ,'image':f"data:image/png;base64,{OOOO0OOOO000O0O00}"}#line:1110
                OOOO0O0O00O00OO00 ={'Authorization':O00O0O000O0OO0OO0 ,'Content-Type':'application/json'}#line:1115
                O00OO000O0O00O0OO =requests .post (f"https://discord.com/api/v9/guilds/{O0OOO0OOO000O0O0O}/emojis",headers =OOOO0O0O00O00OO00 ,json =O00OO0O0O00OO000O )#line:1117
                if O00OO000O0O00O0OO .status_code ==201 :#line:1118
                    print (f"{colorama.Fore.GREEN}    [+] Successfully added emoji '{O000O0OOO0O00OO00}' with token {O00O0O000O0OO0OO0}{colorama.Fore.RESET}")#line:1119
                    OOO0000OO0OOO00OO .add (O000O0OOO0O00OO00 )#line:1120
                    break #line:1121
                else :#line:1122
                    print (f"{colorama.Fore.RED}    [!] Failed to add emoji '{O000O0OOO0O00OO00}' with token {O00O0O000O0OO0OO0}: {O00OO000O0O00O0OO.status_code} - {O00OO000O0O00O0OO.text}{colorama.Fore.RESET}")#line:1123
                time .sleep (O00000OOO0O000O0O )#line:1125
            except Exception as OO0000O0O0OO000OO :#line:1126
                print (f"{colorama.Fore.RED}    [!] Error adding emoji '{O000O0OOO0O00OO00}' with token {O00O0O000O0OO0OO0}: {str(OO0000O0O0OO000OO)}{colorama.Fore.RESET}")#line:1127
import random #line:1129
import requests #line:1130
import time #line:1131
def pollspammer (OOO0O0O0000OO0O0O ,OO0O000O00O0OOO00 ,O0O0O0O0000OOO000 ,O0OO0000OOOOO000O ,O0O0O0O0OO000O0OO ,OO00OO0OOOO00O0OO ,OOOO000O0OO0O00OO ,OO0O0OOOO000O000O ,OOO0OOOOO000000O0 ,OOO0O000OO00OOO00 ,OO00O0OOOOO000000 ):#line:1133
    O0O00OO0O00OOOOO0 =get_session ()#line:1134
    O000O000000000OOO =0 #line:1135
    OOO00O00000OOO0O0 =userget (OOO0O0O0000OO0O0O [0 ],OO0O000O00O0OOO00 ,O0O0O0O0000OOO000 [0 ])#line:1137
    OOO00O00000OOO0O0 =[OOO0O00O0O0OO0O0O for OOO0O00O0O0OO0O0O in OOO00O00000OOO0O0 if OOO0O00O0O0OO0O0O not in OOO0OOOOO000000O0 ]#line:1140
    for _OO0OO0OO00OOO0O0O in range (OOO0O000OO00OOO00 ):#line:1142
        O00O0OO00OO00000O =OOO0O0O0000OO0O0O [O000O000000000OOO ]#line:1143
        O0OO00OOOO0OOOOO0 =get_headers (O00O0OO00OO00000O )#line:1144
        for O0000OOO0000OOO00 in O0O0O0O0000OOO000 :#line:1149
            OOO0OO0OOO00O0OOO =[{"poll_media":{"text":OOO00OO00O0OO0OOO .strip ()}}for OOO00OO00O0OO0OOO in O0O0O0O0OO000O0OO .split (',')]#line:1150
            OOOOO000OO0000000 ={"mobile_network_type":"unknown","content":"","nonce":str (random .randint (10 **17 ,10 **18 -1 )),"tts":False ,"flags":0 ,"poll":{"question":{"text":O0OO0000OOOOO000O },"answers":OOO0OO0OOO00O0OOO ,"allow_multiselect":False ,"duration":OO00OO0OOOO00O0OO ,"layout_type":1 }}#line:1164
            if OOOO000O0OO0O00OO and OOO00O00000OOO0O0 :#line:1166
                OO0OOOOO0O00OO000 =random .choice (OOO00O00000OOO0O0 )#line:1168
                O000O00O00OOOOOOO ={"content":f"{OO0O0OOOO000O000O} {OO0OOOOO0O00OO000}","tts":False ,"nonce":str (random .randint (10 **17 ,10 **18 -1 ))}#line:1173
                OO00O00O0O000OOO0 =O0O00OO0O00OOOOO0 .post (f"https://discord.com/api/v9/channels/{O0000OOO0000OOO00}/messages",json =O000O00O00OOOOOOO ,headers =O0OO00OOOO0OOOOO0 )#line:1174
                if OO00O00O0O000OOO0 .status_code !=200 :#line:1175
                    print (f"Failed to send mention: {OO00O00O0O000OOO0.status_code} - {OO00O00O0O000OOO0.text}")#line:1176
            O000000OO00000O00 =O0O00OO0O00OOOOO0 .post (f"https://discord.com/api/v9/channels/{O0000OOO0000OOO00}/messages",json =OOOOO000OO0000000 ,headers =O0OO00OOOO0OOOOO0 )#line:1178
            if O000000OO00000O00 .status_code ==200 :#line:1179
                print (f"200 poll message sent: {O00O0OO00OO00000O}")#line:1180
            elif O000000OO00000O00 .status_code ==429 :#line:1181
                print (f"429 rate limit: {O00O0OO00OO00000O}")#line:1182
                O0OO000OO0O00OOO0 =O000000OO00000O00 .json ().get ("retry_after",1 )#line:1183
                time .sleep (O0OO000OO0O00OOO0 )#line:1184
            elif O000000OO00000O00 .status_code ==401 :#line:1185
                print (f"401 unknown token: {O00O0OO00OO00000O}")#line:1186
            else :#line:1187
                print (f"error: {O00O0OO00OO00000O} - {O000000OO00000O00.status_code}: {O000000OO00000O00.text}")#line:1188
        O000O000000000OOO =(O000O000000000OOO +1 )%len (OOO0O0O0000OO0O0O )#line:1190
        time .sleep (OO00O0OOOOO000000 )#line:1191
def pollspammermenu ():#line:1194
    with open ("token.txt")as OO0O0OOO00O00O0OO :#line:1195
        OO0OO0OOOO00OOO0O =[O0OO0OOOO0O000OO0 .strip ()for O0OO0OOOO0O000OO0 in OO0O0OOO00O00O0OO .readlines ()if O0OO0OOOO0O000OO0 .strip ()]#line:1196
    O00O0O0O0OO000000 =input ("Enter Server ID: ").strip ()#line:1198
    O0O00OOOO00O0O00O =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:1199
    if O0O00OOOO00O0O00O =='2':#line:1200
        O0O00OO0O0O0O00O0 =input ("Enter Channel IDs (comma-separated): ").strip ().split (',')#line:1201
    else :#line:1202
        O0O00OO0O0O0O00O0 =[]#line:1203
        for O000OOOO00O0OO0OO in OO0OO0OOOO00OOO0O :#line:1204
            try :#line:1205
                O0O00OO0O0O0O00O0 .extend (fetch_channels (O000OOOO00O0OO0OO ,O00O0O0O0OO000000 ))#line:1206
            except Exception as OO00O0000OOO00O00 :#line:1207
                print (f"[!] Failed to fetch channels for token. Error: {OO00O0000OOO00O00}")#line:1208
                continue #line:1209
        random .shuffle (O0O00OO0O0O0O00O0 )#line:1210
    O0O00000OO0O0000O =input ("Enter poll title: ").strip ()#line:1212
    O0OOO00O00OO0O0O0 =input ("Enter poll answers (comma-separated): ").strip ()#line:1213
    OO00O0O0OOO0OO0OO =int (input ("Enter poll duration (in hours 1/4/8/24/72/168/336 ): ").strip ())#line:1214
    OOO0OOOO000O00000 =input ("Do you want to mention random users? (true/false): ").strip ().lower ()=='true'#line:1215
    OO0O0O0000OO0OO0O =""#line:1216
    if OOO0OOOO000O00000 :#line:1217
        OO0O0O0000OO0OO0O =input ("Enter the message to prepend to the mention: ").strip ()#line:1218
    O0O0O0O0O0OOO0O0O =input ("Enter blacklist user IDs (comma-separated): ").strip ().split (',')#line:1219
    O0OOOO0O0O0OO0O00 =int (input ("Enter number of send poll: ").strip ())#line:1220
    OO000O00O0O0OO0O0 =float (input ("Enter delay between posts (in seconds): ").strip ())#line:1221
    pollspammer (OO0OO0OOOO00OOO0O ,O00O0O0O0OO000000 ,O0O00OO0O0O0O00O0 ,O0O00000OO0O0000O ,O0OOO00O00OO0O0O0 ,OO00O0O0OOO0OO0OO ,OOO0OOOO000O00000 ,OO0O0O0000OO0OO0O ,O0O0O0O0O0OOO0O0O ,O0OOOO0O0O0OO0O00 ,OO000O00O0O0OO0O0 )#line:1223
def main ():#line:1226
    colorama .init ()#line:1227
    while True :#line:1228
        logo ()#line:1229
        OOO00O0O00000O00O =input (f"{colorama.Fore.LIGHTMAGENTA_EX}    [Final] Select an option from above: ")#line:1230
        if OOO00O0O00000O00O =="0":#line:1232
            update_group_ids ()#line:1233
        elif OOO00O0O00000O00O =="1":#line:1234
            join_discord_invite ()#line:1235
        elif OOO00O0O00000O00O =="2":#line:1236
            reaction_spammer ()#line:1237
        elif OOO00O0O00000O00O =="3":#line:1238
            send_messages_with_mentions ()#line:1239
        elif OOO00O0O00000O00O =="4":#line:1240
            spammer_menu ()#line:1241
        elif OOO00O0O00000O00O =="5":#line:1242
            nickchanger ()#line:1243
        elif OOO00O0O00000O00O =="6":#line:1244
            add_emojis_from_files ()#line:1245
        elif OOO00O0O00000O00O =="7":#line:1246
            reaction_art ()#line:1247
        elif OOO00O0O00000O00O =="8":#line:1248
            pollspammermenu ()#line:1249
        elif OOO00O0O00000O00O =="0":#line:1250
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [*] Exiting the application. Goodbye!{colorama.Fore.RESET}")#line:1251
            break #line:1252
        else :#line:1253
            print (f"{colorama.Fore.RED}    [!] Invalid option selected!{colorama.Fore.RESET}")#line:1254
        input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:1256
if __name__ =="__main__":#line:1258
    main ()#line:1259
