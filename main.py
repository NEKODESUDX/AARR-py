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
    OO00O000O0O0OOOOO =requests .Session ()#line:58
    if proxy :#line:59
        OO00O000O0O0OOOOO .proxies ={"http":proxy ,"https":proxy }#line:60
    return OO00O000O0O0OOOOO #line:61
def get_headers (OOOO0OOO0O0OO0000 ):#line:63
    return {"Authorization":OOOO0OOO0O0OO0000 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:68
def send_message_with_mention (OOOO0OOO000OOO0OO ,OO0O0OOOOO00O0OO0 ,OO000OO0OOO0OO00O ,O00O0O0O0OOO000O0 ):#line:71
    OOOOO0OOO000OO000 =get_session ()#line:72
    OO000O0OO0OO000O0 =get_headers (OOOO0OOO000OOO0OO )#line:73
    if O00O0O0O0OOO000O0 :#line:75
        OO000OO0000O0OOO0 =random .choice (O00O0O0O0OOO000O0 )#line:76
        OO000OO0OOO0OO00O +=f" <@{OO000OO0000O0OOO0}>"#line:77
    O00000000O00000OO =OOOOO0OOO000OO000 .post (f"https://discord.com/api/v9/channels/{OO0O0OOOOO00O0OO0}/messages",headers =OO000O0OO0OO000O0 ,json ={"content":OO000OO0OOO0OO00O })#line:83
    if O00000000O00000OO .status_code in [200 ,201 ]:#line:84
        print (f"[+] Message sent to channel {OO0O0OOOOO00O0OO0}")#line:85
    elif O00000000O00000OO .status_code ==429 :#line:86
        print ("[-] Rate limited. Please wait before retrying.")#line:87
        OO00O0OO0O0O00OO0 =O00000000O00000OO .json ().get ("retry_after",1 )#line:88
        time .sleep (OO00O0OO0O0O00OO0 )#line:89
    else :#line:90
        print (f"[!] Error occurred: {O00000000O00000OO.status_code}")#line:91
def fetch_messages (O00OO0OO000OO0O00 ,O00OOOOOOOOOOO00O ,limit =100 ):#line:94
    O0OOO0OOO0O00OO00 ={"Authorization":O00OO0OO000OO0O00 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:99
    OO0O00O0000O000O0 =requests .get (f"https://discord.com/api/v9/channels/{O00OOOOOOOOOOO00O}/messages?limit={limit}",headers =O0OOO0OOO0O00OO00 )#line:103
    if OO0O00O0000O000O0 .status_code ==200 :#line:104
        return OO0O00O0000O000O0 .json ()#line:105
    else :#line:106
        print (f"[!] Failed to fetch messages. HTTP Status Code: {OO0O00O0000O000O0.status_code}")#line:107
        return []#line:108
import concurrent .futures #line:110
def reaction_spammer ():#line:112
    try :#line:113
        with open ("token.txt")as O00O00O0OO00O000O :#line:114
            O0000O0O0O0O0O00O =[O0O0O000OOOOOOOOO .strip ()for O0O0O000OOOOOOOOO in O00O00O0OO00O000O .readlines ()if O0O0O000OOOOOOOOO .strip ()]#line:115
    except (FileNotFoundError ,KeyError ):#line:116
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:117
        return #line:118
    OOOOOO0O0O0O0O0O0 =input ("Server ID?: ").strip ()#line:120
    OOOO0OO00OOO0O0OO =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:122
    if OOOO0OO00OOO0O0OO =='2':#line:123
        O0OO00OOO0OO0O0O0 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:124
        OOO0OO000O0O0000O =[OO0O0000OOO0OO0OO .strip ()for OO0O0000OOO0OO0OO in O0OO00OOO0OO0O0O0 if OO0O0000OOO0OO0OO .strip ()]#line:125
    else :#line:126
        OOO0OO000O0O0000O =[]#line:127
        for OO0O0OOOO0O0OO000 in O0000O0O0O0O0O00O :#line:128
            try :#line:129
                OOO0OO000O0O0000O .extend (fetch_channels (OO0O0OOOO0O0OO000 ,OOOOOO0O0O0O0O0O0 ))#line:130
            except Exception as OOOO00O0OOO000OO0 :#line:131
                print (f"[!] Failed to fetch channels for token. Error: {OOOO00O0OOO000OO0}")#line:132
                continue #line:133
    O0O0OO0OOOO00OOOO =input ("Select your emoji (a, b, c, ... or custom emojis): ").strip ()#line:135
    O000OO00OO0O0OO0O =input ("Delay between reactions (in seconds)?: ").strip ()#line:136
    try :#line:138
        O000OO00OO0O0OO0O =float (O000OO00OO0O0OO0O )#line:139
        if O000OO00OO0O0OO0O <0 :#line:140
            raise ValueError #line:141
    except ValueError :#line:142
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:143
        O000OO00OO0O0OO0O =1.0 #line:144
    OO0000OOOOO0O00OO =[]#line:146
    for OO0O000OOOOO00000 in O0O0OO0OOOO00OOOO .split (","):#line:147
        OO0O000OOOOO00000 =OO0O000OOOOO00000 .strip ().lower ()#line:148
        if OO0O000OOOOO00000 in alphabet_to_flag :#line:149
            OO0000OOOOO0O00OO .append (alphabet_to_flag [OO0O000OOOOO00000 ])#line:150
        else :#line:151
            OO0000OOOOO0O00OO .append (OO0O000OOOOO00000 )#line:152
    if not OO0000OOOOO0O00OO :#line:154
        print (f"{colorama.Fore.RED}    [!] No valid emojis provided!{colorama.Fore.RESET}")#line:155
        return #line:156
    def O0O00O0O00OOO0O0O (O0O0O0OO00OO0O00O ):#line:158
        for OOOO000OO0OO000OO in OOO0OO000O0O0000O :#line:159
            try :#line:160
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {OOOO000OO0OO000OO}...{colorama.Fore.RESET}")#line:161
                O0OOOOOOO00O0OO00 =fetch_messages (O0O0O0OO00OO0O00O ,OOOO000OO0OO000OO ,limit =100 )#line:162
                if not O0OOOOOOO00O0OO00 :#line:163
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:164
                    continue #line:165
                for OOO0O000O000OO0OO in O0OOOOOOO00O0OO00 :#line:167
                    for O0OOO0O00O0000OO0 in OO0000OOOOO0O00OO :#line:168
                        reactionput (O0O0O0OO00OO0O00O ,OOOO000OO0OO000OO ,OOO0O000O000OO0OO ['id'],O0OOO0O00O0000OO0 )#line:169
                        time .sleep (O000OO00OO0O0OO0O )#line:170
            except Exception as O0OOO000O0O000OOO :#line:171
                print (f"[!] Error processing channel {OOOO000OO0OO000OO}. Error: {O0OOO000O0O000OOO}")#line:172
                continue #line:173
    with concurrent .futures .ThreadPoolExecutor ()as O00OOO0OO0OO00O00 :#line:175
        OOOOO0O0OO0OO000O =[O00OOO0OO0OO00O00 .submit (O0O00O0O00OOO0O0O ,O00OOO0000OO0O0O0 )for O00OOO0000OO0O0O0 in O0000O0O0O0O0O00O ]#line:176
        concurrent .futures .wait (OOOOO0O0OO0OO000O )#line:177
import requests #line:180
import json #line:181
import time #line:182
import colorama #line:183
alphabet_to_flag ={'a':'🇦','b':'🇧','c':'🇨','d':'🇩','e':'🇪','f':'🇫','g':'🇬','h':'🇭','i':'🇮','j':'🇯','k':'🇰','l':'🇱','m':'🇲','n':'🇳','o':'🇴','p':'🇵','q':'🇶','r':'🇷','s':'🇸','t':'🇹','u':'🇺','v':'🇻','w':'🇼','x':'🇽','y':'🇾','z':'🇿'}#line:191
def fetch_channels (O0O00OOOO0O00O000 ,OO00O0OOO0O00O000 ):#line:193
    O0O00000O0OO0O00O =f"https://discord.com/api/v9/guilds/{OO00O0OOO0O00O000}/channels"#line:194
    O0OOOO00OOOO000OO ={"Authorization":O0O00OOOO0O00O000 }#line:195
    O00O000000OOOOOOO =requests .get (O0O00000O0OO0O00O ,headers =O0OOOO00OOOO000OO )#line:196
    if O00O000000OOOOOOO .status_code ==200 :#line:197
        return [O000OO0000O0O000O ['id']for O000OO0000O0O000O in O00O000000OOOOOOO .json ()if O000OO0000O0O000O ['type']==0 ]#line:198
    else :#line:199
        raise Exception (f"Failed to fetch channels: {O00O000000OOOOOOO.status_code} - {O00O000000OOOOOOO.text}")#line:200
def fetch_messages (O0000O00O0OO0O0OO ,OOO00O000000OOO0O ,limit =100 ):#line:202
    O00OO00O00OOO0OO0 =f"https://discord.com/api/v9/channels/{OOO00O000000OOO0O}/messages?limit={limit}"#line:203
    OO0OO0OOOOOOOO0O0 ={"Authorization":O0000O00O0OO0O0OO }#line:204
    O0000O00000O0OOOO =requests .get (O00OO00O00OOO0OO0 ,headers =OO0OO0OOOOOOOO0O0 )#line:205
    if O0000O00000O0OOOO .status_code ==200 :#line:206
        return O0000O00000O0OOOO .json ()#line:207
    else :#line:208
        print (f"[!] Failed to fetch messages: {O0000O00000O0OOOO.status_code} - {O0000O00000O0OOOO.text}")#line:209
        return []#line:210
def reactionput (OO000000OOO0O0OO0 ,O0O0OOOOOOO000000 ,O00O00O0OO00OOO00 ,O0O0O000O00OOO00O ):#line:212
    O0OOOOOO0OO0O00O0 =f"https://discord.com/api/v9/channels/{O0O0OOOOOOO000000}/messages/{O00O00O0OO00OOO00}/reactions/{O0O0O000O00OOO00O}/@me"#line:213
    OOOOO000OOOOOOOOO ={"Authorization":OO000000OOO0O0OO0 ,"Content-Type":"application/json"}#line:214
    OOOO0O000OO00O000 =requests .put (O0OOOOOO0OO0O00O0 ,headers =OOOOO000OOOOOOOOO )#line:215
    if OOOO0O000OO00O000 .status_code not in [204 ,200 ]:#line:216
        print (f"{colorama.Fore.RED}    [!] Failed to add reaction: {OOOO0O000OO00O000.status_code} - {OOOO0O000OO00O000.text}{colorama.Fore.RESET}")#line:217
import random #line:219
def reaction_art ():#line:221
    try :#line:222
        with open ("token.txt",encoding ="utf-8")as O000O0OO0OO00OO0O :#line:223
            O0O0OOO00000O00O0 =[O00000OOOO00O0OO0 .strip ()for O00000OOOO00O0OO0 in O000O0OO0OO00OO0O .readlines ()if O00000OOOO00O0OO0 .strip ()]#line:224
    except (FileNotFoundError ,KeyError ):#line:225
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:226
        return #line:227
    OOO00OO0OOO000O00 =input ("Server ID?: ").strip ()#line:229
    O00OO0O0O00O0O000 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:231
    if O00OO0O0O00O0O000 =='2':#line:232
        O00OO0OOOO0OOO0O0 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:233
        O00O00O000OO000O0 =[O0O0O0OO00O0OO00O .strip ()for O0O0O0OO00O0OO00O in O00OO0OOOO0OOO0O0 if O0O0O0OO00O0OO00O .strip ()]#line:234
    else :#line:235
        O00O00O000OO000O0 =[]#line:236
        for OO0O0O0O00O0O0O0O in O0O0OOO00000O00O0 :#line:237
            try :#line:238
                O00O00O000OO000O0 .extend (fetch_channels (OO0O0O0O00O0O0O0O ,OOO00OO0OOO000O00 ))#line:239
            except Exception as O0O000000OOOO0O0O :#line:240
                print (f"[!] Failed to fetch channels for token. Error: {O0O000000OOOO0O0O}")#line:241
                continue #line:242
        random .shuffle (O00O00O000OO000O0 )#line:243
    OOO0OO000O0O00O00 =input ("Delay between reactions (in seconds)?: ").strip ()#line:245
    try :#line:247
        OOO0OO000O0O00O00 =float (OOO0OO000O0O00O00 )#line:248
        if OOO0OO000O0O00O00 <0 :#line:249
            raise ValueError #line:250
    except ValueError :#line:251
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:252
        OOO0OO000O0O00O00 =1.0 #line:253
    try :#line:255
        with open ("art.txt",encoding ="utf-8")as OO00O0O00O000O00O :#line:256
            OOO0O0OO0OOOOOOO0 =[OO00OOOO000O00000 .strip ()for OO00OOOO000O00000 in OO00O0O00O000O00O .readlines ()if OO00OOOO000O00000 .strip ()]#line:257
    except (FileNotFoundError ,KeyError ):#line:258
        print (f"{colorama.Fore.RED}    [!] Error: art.txt file not found or empty!{colorama.Fore.RESET}")#line:259
        return #line:260
    except UnicodeDecodeError as O0O000000OOOO0O0O :#line:261
        print (f"{colorama.Fore.RED}    [!] Error decoding art.txt: {str(O0O000000OOOO0O0O)}{colorama.Fore.RESET}")#line:262
        return #line:263
    if not OOO0O0OO0OOOOOOO0 :#line:265
        print (f"{colorama.Fore.RED}    [!] No valid art provided in art.txt!{colorama.Fore.RESET}")#line:266
        return #line:267
    OOO0O0OO0OOOOOOO0 .reverse ()#line:270
    for OO0O0O0O00O0O0O0O in O0O0OOO00000O00O0 :#line:272
        for OOO00O0OOOOOO0000 in O00O00O000OO000O0 :#line:273
            try :#line:274
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {OOO00O0OOOOOO0000}...{colorama.Fore.RESET}")#line:275
                OOO0OO0OOOOO0OOOO =fetch_messages (OO0O0O0O00O0O0O0O ,OOO00O0OOOOOO0000 ,limit =100 )#line:278
                if not OOO0OO0OOOOO0OOOO :#line:279
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:280
                    continue #line:281
                for OOO000OO0OOOO000O ,OOO000000OOOO0O0O in enumerate (OOO0OO0OOOOO0OOOO ):#line:284
                    OO000O0O000O00O0O =OOO0O0OO0OOOOOOO0 [OOO000OO0OOOO000O %len (OOO0O0OO0OOOOOOO0 )].split (',')#line:285
                    for OOO0O0OO0000000O0 in OO000O0O000O00O0O :#line:286
                        reactionput (OO0O0O0O00O0O0O0O ,OOO00O0OOOOOO0000 ,OOO000000OOOO0O0O ['id'],OOO0O0OO0000000O0 .strip ())#line:287
                        print (f"Adding reaction '{OOO0O0OO0000000O0.strip()}' to message {OOO000000OOOO0O0O['id']} in channel {OOO00O0OOOOOO0000}")#line:288
                        time .sleep (OOO0OO000O0O00O00 )#line:289
            except Exception as O0O000000OOOO0O0O :#line:290
                print (f"[!] Error processing channel {OOO00O0OOOOOO0000}. Error: {O0O000000OOOO0O0O}")#line:291
                continue #line:292
    def O0OO00O00O000OO0O (O0OO00O00000OOOOO ):#line:297
        for OO0OOO0O00OOOOOOO in O00O00O000OO000O0 :#line:298
            try :#line:299
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {OO0OOO0O00OOOOOOO}...{colorama.Fore.RESET}")#line:300
                O0O0000O0O0O0OOOO =fetch_messages (O0OO00O00000OOOOO ,OO0OOO0O00OOOOOOO ,limit =100 )#line:301
                if not O0O0000O0O0O0OOOO :#line:302
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:303
                    continue #line:304
                for O0OOO0000O00OO00O in O0O0000O0O0O0OOOO :#line:306
                    for OOOOOO0O0OO0O0000 in OO000O0O000O00O0O :#line:307
                        reactionput (O0OO00O00000OOOOO ,OO0OOO0O00OOOOOOO ,O0OOO0000O00OO00O ['id'],OOOOOO0O0OO0O0000 )#line:308
                        time .sleep (OOO0OO000O0O00O00 )#line:309
            except Exception as OOOOOO0O00000OOO0 :#line:310
                print (f"[!] Error processing channel {OO0OOO0O00OOOOOOO}. Error: {OOOOOO0O00000OOO0}")#line:311
                continue #line:312
    with concurrent .futures .ThreadPoolExecutor ()as O0O0O0O0000O00O0O :#line:314
        OOOOOOO00OO00OOO0 =[O0O0O0O0000O00O0O .submit (O0OO00O00O000OO0O ,O0OOOOO0000OOO00O )for O0OOOOO0000OOO00O in O0O0OOO00000O00O0 ]#line:315
        concurrent .futures .wait (OOOOOOO00OO00OOO0 )#line:316
def update_group_ids ():#line:319
    try :#line:320
        with open ("token.txt")as O0OOO00000OO0OOOO :#line:321
            O0O0O00OO0O0O00O0 =[O0OO0O0O0O0OOO0O0 .strip ()for O0OO0O0O0O0OOO0O0 in O0OOO00000OO0OOOO .readlines ()if O0OO0O0O0O0OOO0O0 .strip ()]#line:322
        OOOO0OO00O0O0OOOO =O0O0O00OO0O0O00O0 [0 ]#line:323
    except (FileNotFoundError ,KeyError ):#line:324
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:325
        return #line:326
    OO000O0OOO0000OOO ={"Authorization":OOOO0OO00O0O0OOOO ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:332
    OO000O0O0OO0O0OO0 =requests .get ('https://discord.com/api/v9/users/@me/channels',headers =OO000O0OOO0000OOO )#line:334
    if OO000O0O0OO0O0OO0 .status_code ==200 :#line:335
        O00O0O00O0O00O0OO =OO000O0O0OO0O0OO0 .json ()#line:336
        with open ("group_id.txt","w")as O000OO00O000OO000 :#line:337
            for OOO0O00OO0O0OOOOO in O00O0O00O0O00O0OO :#line:338
                if OOO0O00OO0O0OOOOO ['type']==3 :#line:339
                    O000OO00O000OO000 .write (OOO0O00OO0O0OOOOO ['id']+'\n')#line:340
        print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Group IDs updated successfully.{colorama.Fore.RESET}")#line:341
    else :#line:342
        print (f"{colorama.Fore.LIGHTRED_EX}    [!] Failed to retrieve group IDs. HTTP Status Code: {OO000O0O0OO0O0OO0.status_code}{colorama.Fore.RESET}")#line:343
import requests #line:345
import requests #line:347
def fetch_channels (O0OO0OOOO0O0OOO0O ,OOOO0OO00OOOO0OO0 ):#line:349
    try :#line:350
        O0O0O000O0OO000O0 =requests .Session ()#line:351
        O0OOO0O000O00O0OO =get_headers (O0OO0OOOO0O0OOO0O )#line:352
        OO0O00O00O00OO0O0 =O0O0O000O0OO000O0 .get (f"https://discord.com/api/v9/guilds/{OOOO0OO00OOOO0OO0}/channels",headers =O0OOO0O000O00O0OO ,timeout =10 )#line:359
        if OO0O00O00O00OO0O0 .status_code ==200 :#line:362
            try :#line:363
                OOO0O0OOOOO00O0O0 =OO0O00O00O00OO0O0 .json ()#line:364
                return [OOOO0O00OO0O0OO00 ['id']for OOOO0O00OO0O0OO00 in OOO0O0OOOOO00O0O0 if OOOO0O00OO0O0OO00 .get ('type')==0 ]#line:365
            except ValueError :#line:366
                print ("[!] Error: Response was not valid JSON.")#line:367
                return []#line:368
        elif OO0O00O00O00OO0O0 .status_code ==401 :#line:369
            print ("[!] Error: Unauthorized - check your token.")#line:370
        elif OO0O00O00O00OO0O0 .status_code ==403 :#line:371
            print ("[!] Error: Forbidden - you lack permissions.")#line:372
        elif OO0O00O00O00OO0O0 .status_code ==404 :#line:373
            print ("[!] Error: Server not found - check the server ID.")#line:374
        else :#line:375
            print (f"[!] Error: Unexpected status code {OO0O00O00O00OO0O0.status_code}.")#line:376
        return []#line:379
    except requests .exceptions .Timeout :#line:381
        print ("[!] Error: Request timed out. Check your connection or try again later.")#line:382
        return []#line:383
    except requests .exceptions .RequestException as O00OO0OOOOO0OO00O :#line:384
        print (f"[!] Error: An error occurred while fetching channels: {O00OO0OOOOO0OO00O}")#line:385
        return []#line:386
def extract_uids_from_messages (OOO00OO0OOOO0OO0O ):#line:392
    OO000O0OO0O0OO00O =set ()#line:393
    for O0OO000O00O0O0OO0 in OOO00OO0OOOO0OO0O :#line:394
        OO000O0OO0O0OO00O .add (O0OO000O00O0O0OO0 ['author']['id'])#line:395
    return list (OO000O0OO0O0OO00O )#line:396
def send_message_with_mention (OOOO00O0OO00O0O00 ,O00000O0O00OO0OO0 ,O000O00O000O00000 ,O00O00O0OO00O00OO ):#line:398
    O00OOOO0O0O0O0O00 =get_session ()#line:399
    OOOO000OO0OOO000O =get_headers (OOOO00O0OO00O0O00 )#line:400
    if O00O00O0OO00O00OO :#line:402
        O00O0OO00O0O0OOO0 =random .choice (O00O00O0OO00O00OO )#line:403
        O000O00O000O00000 +=f" <@{O00O0OO00O0O0OOO0}>"#line:404
    OO0OOOOOOOOOO0O00 =O00OOOO0O0O0O0O00 .post (f"https://discord.com/api/v9/channels/{O00000O0O00OO0OO0}/messages",headers =OOOO000OO0OOO000O ,json ={"content":O000O00O000O00000 })#line:410
    if OO0OOOOOOOOOO0O00 .status_code in [200 ,201 ]:#line:411
        print (f"[+] Message sent to channel {O00000O0O00OO0OO0}")#line:412
    elif OO0OOOOOOOOOO0O00 .status_code ==429 :#line:413
        print ("[-] Rate limited. Please wait before retrying.")#line:414
        OO00OO0O0OOOOOO0O =OO0OOOOOOOOOO0O00 .json ().get ("retry_after",1 )#line:415
        time .sleep (OO00OO0O0OOOOOO0O )#line:416
    else :#line:417
        print (f"[!] Error occurred: {OO0OOOOOOOOOO0O00.status_code}")#line:418
def send_messages_with_mentions ():#line:419
    try :#line:420
        with open ("token.txt")as O0OOOOOOOO000O0O0 :#line:421
            O0O0O0OOOO0O0O000 =[OO0O000O00O00OOOO .strip ()for OO0O000O00O00OOOO in O0OOOOOOOO000O0O0 .readlines ()if OO0O000O00O00OOOO .strip ()]#line:422
    except (FileNotFoundError ,KeyError ):#line:423
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:424
        return #line:425
    OOO0O0OOOO00000O0 =input ("Server ID?: ").strip ()#line:427
    OO00OO00OO000OO0O =input ("Delay between messages (in seconds)?: ").strip ()#line:428
    OO0O0O0O00OOO00O0 =input ("Number of messages to send?: ").strip ()#line:429
    O00O00O000O0OOO0O =input ("Message content?: ").strip ()#line:430
    OOO0O0O000OOOO0OO =input ("Blacklist User IDs (comma-separated)?: ").strip ().split (',')#line:431
    OOO0O0O000OOOO0OO =[OO0OO0O0OOOO00O0O .strip ()for OO0OO0O0OOOO00O0O in OOO0O0O000OOOO0OO if OO0OO0O0OOOO00O0O .strip ()]#line:432
    try :#line:434
        OO00OO00OO000OO0O =float (OO00OO00OO000OO0O )#line:435
        if OO00OO00OO000OO0O <0 :#line:436
            raise ValueError #line:437
    except ValueError :#line:438
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:439
        OO00OO00OO000OO0O =1.0 #line:440
    try :#line:442
        OO0O0O0O00OOO00O0 =int (OO0O0O0O00OOO00O0 )#line:443
        if OO0O0O0O00OOO00O0 <=0 :#line:444
            raise ValueError #line:445
    except ValueError :#line:446
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:447
        OO0O0O0O00OOO00O0 =1 #line:448
    OO00O0O0000OOO00O =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:450
    if OO00O0O0000OOO00O =='2':#line:451
        OO0O00000OOO0O0O0 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:452
        OO0O00000OOO0O0O0 =[O0O0000OOOOOO0O0O .strip ()for O0O0000OOOOOO0O0O in OO0O00000OOO0O0O0 if O0O0000OOOOOO0O0O .strip ()]#line:453
    else :#line:454
        OO0O00000OOO0O0O0 =[]#line:455
    OO0OO0O0OO0OO0000 =set ()#line:457
    for OO00O00O0OOOO0OO0 in O0O0O0OOOO0O0O000 :#line:458
        O0O0000O00O00OOO0 =fetch_channels (OO00O00O0OOOO0OO0 ,OOO0O0OOOO00000O0 )#line:459
        for OO0O000O0OO0OO000 in O0O0000O00O00OOO0 :#line:460
            OO000O00O0000OOO0 =fetch_messages (OO00O00O0OOOO0OO0 ,OO0O000O0OO0OO000 ,limit =100 )#line:461
            OO0O00OO00OO0OO0O =extract_uids_from_messages (OO000O00O0000OOO0 )#line:462
            OO0OO0O0OO0OO0000 .update (OO0O00OO00OO0OO0O )#line:463
    OO0OO0O0OO0OO0000 =list (set (OO0OO0O0OO0OO0000 )-set (OOO0O0O000OOOO0OO ))#line:466
    for _OO00O0OOO0OO000OO in range (OO0O0O0O00OOO00O0 ):#line:468
        for OO00O00O0OOOO0OO0 in O0O0O0OOOO0O0O000 :#line:469
            if OO0O00000OOO0O0O0 :#line:470
                O0O0000O00O00OOO0 =OO0O00000OOO0O0O0 #line:471
            for OO0O000O0OO0OO000 in O0O0000O00O00OOO0 :#line:472
                send_message_with_mention (OO00O00O0OOOO0OO0 ,OO0O000O0OO0OO000 ,O00O00O000O0OOO0O ,OO0OO0O0OO0OO0000 )#line:473
                time .sleep (OO00OO00OO000OO0O )#line:474
def join_discord_invite ():#line:479
    try :#line:480
        with open ("token.txt")as O0O0O00OOOOO000OO :#line:481
            OO0OO0000OO00OOOO =[OOOO0OO00O00O00O0 .strip ()for OOOO0OO00O00O00O0 in O0O0O00OOOOO000OO .readlines ()if OOOO0OO00O00O00O0 .strip ()]#line:482
    except (FileNotFoundError ,KeyError ):#line:483
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:484
        return #line:485
    OOOO00OOO00O0OOOO =input ("Invite Code?: discord.gg/").strip ()#line:487
    for OOO0OOO00OO0000OO in OO0OO0000OO00OOOO :#line:490
        joiner (OOO0OOO00OO0000OO ,OOOO00OOO00O0OOOO )#line:491
import json ,time ,base64 ,random ,requests #line:493
def cookieset (O00OO0OO0OO0O000O ):#line:495
    O0OO00O0O0OOOOOO0 =O00OO0OO0OO0O000O .get ("https://discord.com/app")#line:496
    return O0OO00O0O0OOOOOO0 .cookies .get_dict ()#line:497
def generatexspandua (O0OO0OO0OOOOOO0OO ):#line:499
    OO000OO0000OO0O0O =["Android","Windows","Macintosh"]#line:500
    O0OO0OO0OOO0O000O =random .choice (OO000OO0000OO0O0O )#line:501
    if O0OO0OO0OOO0O000O =="Macintosh":#line:502
        O0O00O0O000OO00OO =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:503
        O0O0O0O00O00O0O00 ="Macintosh; Intel Mac OS X "+O0O00O0O000OO00OO #line:504
        O00O00OO0OOOO000O ="x86_64"#line:505
    elif O0OO0OO0OOO0O000O =="Windows":#line:506
        O0O00O0O000OO00OO =f'{random.choice([6.0, 10.0, 11.0])}'#line:507
        O0O0O0O00O00O0O00 ="Windows NT "+O0O00O0O000OO00OO +" Win64; x64"#line:508
        O00O00OO0OOOO000O ="x86_64"#line:509
    else :#line:510
        O0O00O0O000OO00OO ="13"#line:511
        O0O0O0O00O00O0O00 =f"Linux; Android 13; Pixel 6a"#line:512
        O00O00OO0OOOO000O ="aarch64"#line:513
    O0O00O0OO0000OOOO ={"os":O0OO0OO0OOO0O000O ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":O0O00O0O000OO00OO ,"os_arch":O00O00OO0OOOO000O ,"system_locale":"ja-JP","client_build_number":O0OO0OO0OOOOOO0OO ,"client_event_source":None ,"design_id":0 }#line:526
    O0OOO0OOOOO00O0O0 =f"Mozilla/5.0 ({O0O0O0O00O00O0O00}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:527
    return base64 .b64encode (json .dumps (O0O00O0OO0000OOOO ,separators =(',',':')).encode ()).decode (),O0OOO0OOOOO00O0O0 #line:528
def joiner (OO0OO0OO0OO000OOO ,O0O0000OO000O00O0 ,O000OOOOOOOO0O0O0 ,OO0OOOOO0000OO0OO ):#line:530
  O0OOO0O0O00OO00OO =get_session (O000OOOOOOOO0O0O0 )#line:531
  OOO0O0OOO00O0OOOO =cookieset (O0OOO0O0O00OO00OO )#line:532
  OOO0O0OOO00O0OOOO ["locale"]="ja-JP"#line:533
  OOO0O00O0O0O00O00 =201211 #line:534
  O0OO00OOO0O0000O0 ,OOOO000OOOO00O00O =generatexspandua (OOO0O00O0O0O00O00 )#line:535
  O00000OOOOO0O00O0 ={"Authorization":OO0OO0OO0OO000OOO ,"accept":"*/*","accept-language":"ja-JP","connection":"keep-alive","DNT":"1","origin":"https://discord.com","sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","referer":"https://discord.com/channels/@me","TE":"Trailers","user-agent":OOOO000OOOO00O00O ,"X-Super-Properties":O0OO00OOO0O0000O0 ,}#line:550
  O0OOOO0OOO0OOOO00 =O0OOO0O0O00OO00OO .post ("https://discord.com/api/v9/invites/"+O0O0000OO000O00O0 ,headers =O00000OOOOO0O00O0 ,json ={},cookies =OOO0O0OOO00O0OOOO )#line:552
  if O0OOOO0OOO0OOOO00 .status_code ==200 :#line:553
    print ("[+] Probably joined "+OO0OO0OO0OO000OOO )#line:554
    if "show_verification_form"in O0OOOO0OOO0OOOO00 .json ():#line:555
      bypass (OO0OO0OO0OO000OOO ,O0OOOO0OOO0OOOO00 .json ()["guild"]["id"],O0OOO0O0O00OO00OO ,O00000OOOOO0O00O0 )#line:556
    return #line:557
  elif "captcha_key"in O0OOOO0OOO0OOOO00 .text and O0OOOO0OOO0OOOO00 .status_code ==400 :#line:558
    print ("[!] Hcaptcha interference "+OO0OO0OO0OO000OOO )#line:559
    return #line:560
  elif O0OOOO0OOO0OOOO00 .status_code ==401 :#line:561
    print ("[!] Token is dead "+OO0OO0OO0OO000OOO )#line:562
    return #line:563
  elif O0OOOO0OOO0OOOO00 .status_code ==403 :#line:564
    if "message"in O0OOOO0OOO0OOOO00 .json ():#line:565
      if O0OOOO0OOO0OOOO00 .json ()["message"]=="Unknown Message":#line:566
        print ("[!] Unknown error "+OO0OO0OO0OO000OOO )#line:567
        return #line:568
      else :#line:569
        print ("[!] Verification required "+OO0OO0OO0OO000OOO )#line:570
        return #line:571
    else :#line:572
      print ("[!] Error occurred "+OO0OO0OO0OO000OOO )#line:573
      return #line:574
  elif O0OOOO0OOO0OOOO00 .status_code ==429 :#line:575
    print ("[!] Token rate-limited "+OO0OO0OO0OO000OOO )#line:576
    return #line:577
  elif O0OOOO0OOO0OOOO00 .status_code ==400 :#line:578
    if "captcha_key"in O0OOOO0OOO0OOOO00 .json ():#line:579
      print ("[!] Hcaptcha interference "+OO0OO0OO0OO000OOO )#line:580
      return #line:581
    else :#line:582
      print ("[!] Error occurred "+OO0OO0OO0OO000OOO )#line:583
      return #line:584
  elif O0OOOO0OOO0OOOO00 .status_code ==401 :#line:585
    print ("[!] Token is dead "+OO0OO0OO0OO000OOO )#line:586
    return #line:587
  elif O0OOOO0OOO0OOOO00 .status_code ==403 :#line:588
    if "message"in O0OOOO0OOO0OOOO00 .json ():#line:589
      if O0OOOO0OOO0OOOO00 .json ()["message"]=="Unknown Message":#line:590
        print ("[!] Unknown error "+OO0OO0OO0OO000OOO )#line:591
        return #line:592
      else :#line:593
        print ("[!] Verification required "+OO0OO0OO0OO000OOO )#line:594
        return #line:595
    else :#line:596
      print ("[!] Error occurred "+OO0OO0OO0OO000OOO )#line:597
  elif O0OOOO0OOO0OOOO00 .status_code ==429 :#line:598
    print ("[!] Token rate-limited "+OO0OO0OO0OO000OOO )#line:599
    return #line:600
  else :#line:601
    print ("[!] Error occurred "+OO0OO0OO0OO000OOO )#line:602
    return #line:603
def update_group_ids ():#line:606
    OO0O0OO0O0OO0OOOO =input ("Invite Code?: ").strip ()#line:607
    try :#line:608
        with open ("token.txt")as O00OO0000O00OO0O0 :#line:609
            OOO00O0O0000O000O =[O0000OO00OO0OOO00 .strip ()for O0000OO00OO0OOO00 in O00OO0000O00OO0O0 .readlines ()if O0000OO00OO0OOO00 .strip ()]#line:610
    except (FileNotFoundError ,KeyError ):#line:611
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:612
        return #line:613
    O0O000000O0O0OOO0 =requests .Session ()#line:615
    for OO0OO0OO00OOO0O0O in OOO00O0O0000O000O :#line:616
        joiner (OO0OO0OO00OOO0O0O ,OO0O0OO0O0OO0OOOO ,O0O000000O0O0OOO0 )#line:617
        time .sleep (2 )#line:618
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:620
def bypass (OO00OO00O0OO0O000 ,OOOOO000O0OOOOOO0 ,O00OOOO00OOO00O00 ,OOOOOOOO0O0OOO0OO ):#line:623
    try :#line:624
        OOOO0O0O0O0O000OO =O00OOOO00OOO00O00 .get (f"https://discord.com/api/v9/guilds/{OOOOO000O0OOOOOO0}/member-verification?with_guild=false",headers =OOOOOOOO0O0OOO0OO ).json ()#line:625
        OOO0000OO00OO0O0O =O00OOOO00OOO00O00 .put (f"https://discord.com/api/v9/guilds/{OOOOO000O0OOOOOO0}/requests/@me",headers =OOOOOOOO0O0OOO0OO ,json =OOOO0O0O0O0O000OO )#line:626
        if OOO0000OO00OO0O0O .status_code ==201 :#line:627
            print (f"[+] MemberscreeningBypassed {OO00OO00O0OO0O000}")#line:628
            return #line:629
        else :#line:630
            print (f"[!] Bypassが出来ませんでした {OO00OO00O0OO0O000}")#line:631
            return #line:632
    except Exception as OOO00OOOOO0OO0000 :#line:633
        print (f"[!] エラーが発生しました。{OOO00OOOOO0OO0000}")#line:634
session =requests .Session ()#line:636
def reactionput (O000OOOOO0O00O0O0 ,O0OOO0OO0OO0O0OOO ,O0000OOO00O0O0OOO ,O0O0O00OOO0OOOOO0 ,proxy =None ):#line:639
    O0O0O0000000O00OO =get_session (proxy )#line:640
    OO0OO0O000O00O0OO =get_headers (O0O0O0000000O00OO )#line:641
    OO0OO0O000O00O0OO ["Authorization"]=O000OOOOO0O00O0O0 #line:642
    O0O0O00OOO0OOOOO0 =requests .utils .quote (O0O0O00OOO0OOOOO0 )#line:644
    O00OOOO0O0O000000 =O0O0O0000000O00OO .put (f"https://discord.com/api/v9/channels/{O0OOO0OO0OO0O0OOO}/messages/{O0000OOO00O0O0OOO}/reactions/{O0O0O00OOO0OOOOO0}/%40me?location=Message&type=0",headers =OO0OO0O000O00O0OO )#line:648
    if O00OOOO0O0O000000 .status_code in [200 ,204 ]:#line:649
        print (f"[+] Reaction '{O0O0O00OOO0OOOOO0}' added successfully to message {O0000OOO00O0O0OOO}")#line:650
    elif O00OOOO0O0O000000 .status_code ==429 :#line:651
        print ("[-] Rate limited. Please wait before retrying.")#line:652
        OOO0O00OO0O00O00O =O00OOOO0O0O000000 .json ().get ("retry_after",1 )#line:653
        time .sleep (OOO0O00OO0O00O00O )#line:654
    elif O00OOOO0O0O000000 .status_code ==401 :#line:655
        print ("[-] Invalid or expired token.")#line:656
    else :#line:657
        print (f"[!] Error occurred: {O00OOOO0O0O000000.status_code}")#line:658
def generatexspandua (O00000O00OOOOO0O0 ):#line:661
  O0000OO0O0000OOOO =["Android","Windows","Macintosh"]#line:662
  OOO0O0O000000OOOO =random .choice (O0000OO0O0000OOOO )#line:663
  if OOO0O0O000000OOOO =="Macintosh":#line:664
    OOOOOO00O00O000OO =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:665
    OO0O000000OO0000O ="Macintosh; Intel Mac OS X "+OOOOOO00O00O000OO #line:666
    O0000O000O0OO0O0O ="x86_64"#line:667
  if OOO0O0O000000OOOO =="Windows":#line:668
    OOOOOO00O00O000OO =f'{random.choice([6.0,10.0,11.0])}'#line:669
    OO0O000000OO0000O ="Windows NT "+OOOOOO00O00O000OO +" Win64; x64"#line:670
    O0000O000O0OO0O0O ="x86_64"#line:671
  if OOO0O0O000000OOOO =="Android":#line:672
    OOOOOO00O00O000OO ="13"#line:673
    OO0O000000OO0000O =f"Linux; Android 13; Pixel 6a"#line:674
    O0000O000O0OO0O0O ="aarch64"#line:675
  O00O0O0OO0O00OO00 ={"os":OOO0O0O000000OOOO ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":OOOOOO00O00O000OO ,"os_arch":O0000O000O0OO0O0O ,"system_locale":"ja-JP","client_build_number":O00000O00OOOOO0O0 ,"client_event_source":None ,"design_id":0 }#line:676
  OO0O00OO00OO0OOOO =f"Mozilla/5.0 ({OO0O000000OO0000O}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:677
  return base64 .b64encode (json .dumps (O00O0O0OO0O00OO00 ,separators =(',',':')).encode ()).decode (),OO0O00OO00OO0OOOO #line:678
import base64 #line:680
def nickchanger ():#line:683
    try :#line:684
        with open ("token.txt")as O00OO0O00O0O0OO00 :#line:685
            OOO00O0OO00OO0000 =[O0O0O00OO0OO0OO00 .strip ()for O0O0O00OO0OO0OO00 in O00OO0O00O0O0OO00 .readlines ()if O0O0O00OO0OO0OO00 .strip ()]#line:686
    except (FileNotFoundError ,KeyError ):#line:687
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:688
        return #line:689
    O0O00O0OO0000OO00 =input ("Server ID?: ").strip ()#line:691
    OOOOO000O00O0O000 =input ("Nickname?: ").strip ()#line:692
    O00OOO00O0O0OO000 =input ("Delay (in seconds)?: ").strip ()#line:693
    try :#line:695
        O00OOO00O0O0OO000 =float (O00OOO00O0O0OO000 )#line:696
        if O00OOO00O0O0OO000 <0 :#line:697
            raise ValueError #line:698
    except ValueError :#line:699
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:700
        O00OOO00O0O0OO000 =1.0 #line:701
    for OO0O00OO0O0OOO00O in OOO00O0OO00OO0000 :#line:703
        O0OOOO0OOO00O0OOO ={"Authorization":OO0O00OO0O0OOO00O ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:708
        OOOO0000O00O0OO00 ={"nick":OOOOO000O00O0O000 }#line:709
        OO0OOO0OOO0OOO000 =requests .patch (f"https://discord.com/api/v9/guilds/{O0O00O0OO0000OO00}/members/@me",headers =O0OOOO0OOO00O0OOO ,json =OOOO0000O00O0OO00 )#line:710
        if OO0OOO0OOO0OOO000 .status_code ==200 :#line:712
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Nickname changed to '{OOOOO000O00O0O000}' successfully for token {OO0O00OO0O0OOO00O}.{colorama.Fore.RESET}")#line:713
        elif OO0OOO0OOO0OOO000 .status_code ==429 :#line:714
            print (f"{colorama.Fore.RED}    [!] Rate limited. Please wait before retrying for token {OO0O00OO0O0OOO00O}.{colorama.Fore.RESET}")#line:715
            OOO0O0O0OOO000OO0 =OO0OOO0OOO0OOO000 .json ().get ("retry_after",1 )#line:716
            time .sleep (OOO0O0O0OOO000OO0 )#line:717
        else :#line:718
            print (f"{colorama.Fore.RED}    [!] Error occurred: {OO0OOO0OOO0OOO000.status_code} for token {OO0O00OO0O0OOO00O}.{colorama.Fore.RESET}")#line:719
        time .sleep (O00OOO00O0O0OO000 )#line:721
import json ,websocket ,threading ,tls_client ,random ,time #line:725
session =tls_client .Session (client_identifier ="chrome112",random_tls_extension_order =True )#line:727
class Utils :#line:729
    @staticmethod #line:730
    def rangeCorrector (OOOO0O0O00OOO0OOO ):#line:731
        if [0 ,99 ]not in OOOO0O0O00OOO0OOO :#line:732
            OOOO0O0O00OOO0OOO .insert (0 ,[0 ,99 ])#line:733
        return OOOO0O0O00OOO0OOO #line:734
    @staticmethod #line:736
    def getRanges (O000000OOO00O00OO ,O00OOOOOO00O00OOO ,O0OO00OOOO000O0OO ):#line:737
        OOOOOOOOO00OOO0OO =int (O000000OOO00O00OO *O00OOOOOO00O00OOO )#line:738
        O00OOOO0OO0O00O0O =[[OOOOOOOOO00OOO0OO ,OOOOOOOOO00OOO0OO +99 ]]#line:739
        if O0OO00OOOO000O0OO >OOOOOOOOO00OOO0OO +99 :#line:740
            O00OOOO0OO0O00O0O .append ([OOOOOOOOO00OOO0OO +100 ,OOOOOOOOO00OOO0OO +199 ])#line:741
        return Utils .rangeCorrector (O00OOOO0OO0O00O0O )#line:742
    @staticmethod #line:744
    def parseGuildMemberListUpdate (OOO0OOO00O0OO0O0O ):#line:745
        OOO00OOOOOO00O0OO ={"online_count":OOO0OOO00O0OO0O0O ["d"]["online_count"],"member_count":OOO0OOO00O0OO0O0O ["d"]["member_count"],"id":OOO0OOO00O0OO0O0O ["d"]["id"],"guild_id":OOO0OOO00O0OO0O0O ["d"]["guild_id"],"hoisted_roles":OOO0OOO00O0OO0O0O ["d"]["groups"],"types":[],"locations":[],"updates":[],}#line:755
        for OOOOOO0OO000OO0OO in OOO0OOO00O0OO0O0O ["d"]["ops"]:#line:757
            OOO00OOOOOO00O0OO ["types"].append (OOOOOO0OO000OO0OO ["op"])#line:758
            if OOOOOO0OO000OO0OO ["op"]in ("SYNC","INVALIDATE"):#line:759
                OOO00OOOOOO00O0OO ["locations"].append (OOOOOO0OO000OO0OO ["range"])#line:760
                if OOOOOO0OO000OO0OO ["op"]=="SYNC":#line:761
                    OOO00OOOOOO00O0OO ["updates"].append (OOOOOO0OO000OO0OO ["items"])#line:762
                else :#line:763
                    OOO00OOOOOO00O0OO ["updates"].append ([])#line:764
            elif OOOOOO0OO000OO0OO ["op"]in ("INSERT","UPDATE","DELETE"):#line:765
                OOO00OOOOOO00O0OO ["locations"].append (OOOOOO0OO000OO0OO ["index"])#line:766
                if OOOOOO0OO000OO0OO ["op"]=="DELETE":#line:767
                    OOO00OOOOOO00O0OO ["updates"].append ([])#line:768
                else :#line:769
                    OOO00OOOOOO00O0OO ["updates"].append (OOOOOO0OO000OO0OO ["item"])#line:770
        return OOO00OOOOOO00O0OO #line:771
class DiscordSocket (websocket .WebSocketApp ):#line:773
    def __init__ (OOOO000O0O0OOO000 ,O0OO000000O0000O0 ,O000O0O0OOOO0OOOO ,O0O0O0OOO0OOOOOO0 ):#line:774
        OOOO000O0O0OOO000 .token =O0OO000000O0000O0 #line:775
        OOOO000O0O0OOO000 .guild_id =O000O0O0OOOO0OOOO #line:776
        OOOO000O0O0OOO000 .channel_id =O0O0O0OOO0OOOOOO0 #line:777
        OOOO000O0O0OOO000 .socket_headers ={"Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","Cache-Control":"no-cache","Pragma":"no-cache","Sec-WebSocket-Extensions":"permessage-deflate; client_max_window_bits","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",}#line:785
        super ().__init__ ("wss://gateway.discord.gg/?encoding=json&v=9",header =OOOO000O0O0OOO000 .socket_headers ,on_open =lambda OO0OOO0OO0OO000O0 :OOOO000O0O0OOO000 .sock_open (OO0OOO0OO0OO000O0 ),on_message =lambda OO0O00O0OOOO0OOOO ,O000O0O000OO0O0O0 :OOOO000O0O0OOO000 .sock_message (OO0O00O0OOOO0OOOO ,O000O0O000OO0O0O0 ),on_close =lambda O0OO0OO0OO000O000 ,OO00000OO0000O00O ,O0O0O00000OO00OO0 :OOOO000O0O0OOO000 .sock_close (O0OO0OO0OO000O000 ,OO00000OO0000O00O ,O0O0O00000OO00OO0 ),)#line:794
        OOOO000O0O0OOO000 .endScraping =False #line:796
        OOOO000O0O0OOO000 .guilds ={}#line:797
        OOOO000O0O0OOO000 .members ={}#line:798
        OOOO000O0O0OOO000 .ranges =[[0 ,0 ]]#line:799
        OOOO000O0O0OOO000 .lastRange =0 #line:800
        OOOO000O0O0OOO000 .packets_recv =0 #line:801
    def run (O000O00OO0OOO0O0O ):#line:803
        O000O00OO0OOO0O0O .run_forever ()#line:804
        return O000O00OO0OOO0O0O .members #line:805
    def scrapeUsers (OOOOOO0O00OO0OOOO ):#line:807
        if not OOOOOO0O00OO0OOOO .endScraping :#line:808
            OOOOOO0O00OO0OOOO .send ('{"op":14,"d":{"guild_id":"'+OOOOOO0O00OO0OOOO .guild_id +'","typing":true,"activities":true,"threads":true,"channels":{"'+OOOOOO0O00OO0OOOO .channel_id +'":'+json .dumps (OOOOOO0O00OO0OOOO .ranges )+"}}}")#line:817
    def sock_open (O0OOOO0000OO0OOOO ,OO00O000O000OO0O0 ):#line:819
        O0OOOO0000OO0OOOO .send ('{"op":2,"d":{"token":"'+O0OOOO0000OO0OOOO .token +'","capabilities":125,"properties":{"os":"Windows NT","browser":"Chrome","device":"","system_locale":"it-IT","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36","browser_version":"119.0","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":103981,"client_event_source":null},"presence":{"status":"online","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}')#line:824
    def heartbeatThread (OO00O0OOO0000OO00 ,O0O0OOOOO00OO00O0 ):#line:826
        try :#line:827
            while True :#line:828
                OO00O0OOO0000OO00 .send ('{"op":1,"d":'+str (OO00O0OOO0000OO00 .packets_recv )+"}")#line:829
                time .sleep (O0O0OOOOO00OO00O0 )#line:830
        except Exception as O00OO00OO0000O000 :#line:831
            pass #line:832
    def sock_message (O00OO0OOO0O00OOOO ,O0OOOOOOO00000OO0 ,O000O00O00O0O0OOO ):#line:834
        O0OO0OO0000OO00O0 =json .loads (O000O00O00O0O0OOO )#line:835
        if O0OO0OO0000OO00O0 is None :#line:836
            return #line:837
        if O0OO0OO0000OO00O0 ["op"]!=11 :#line:838
            O00OO0OOO0O00OOOO .packets_recv +=1 #line:839
        if O0OO0OO0000OO00O0 ["op"]==10 :#line:840
            threading .Thread (target =O00OO0OOO0O00OOOO .heartbeatThread ,args =(O0OO0OO0000OO00O0 ["d"]["heartbeat_interval"]/1000 ,),daemon =True ,).start ()#line:845
        if O0OO0OO0000OO00O0 ["t"]=="READY":#line:846
            for OOO000O0O00000000 in O0OO0OO0000OO00O0 ["d"]["guilds"]:#line:847
                O00OO0OOO0O00OOOO .guilds [OOO000O0O00000000 ["id"]]={"member_count":OOO000O0O00000000 ["member_count"]}#line:848
        if O0OO0OO0000OO00O0 ["t"]=="READY_SUPPLEMENTAL":#line:849
            O00OO0OOO0O00OOOO .ranges =Utils .getRanges (0 ,100 ,O00OO0OOO0O00OOOO .guilds [O00OO0OOO0O00OOOO .guild_id ]["member_count"])#line:852
            O00OO0OOO0O00OOOO .scrapeUsers ()#line:853
        elif O0OO0OO0000OO00O0 ["t"]=="GUILD_MEMBER_LIST_UPDATE":#line:854
            O0OO0O0O000O0OO00 =Utils .parseGuildMemberListUpdate (O0OO0OO0000OO00O0 )#line:855
            if O0OO0O0O000O0OO00 ["guild_id"]==O00OO0OOO0O00OOOO .guild_id and ("SYNC"in O0OO0O0O000O0OO00 ["types"]or "UPDATE"in O0OO0O0O000O0OO00 ["types"]):#line:859
                for OO0OOOO000OOOOO0O ,OOOO0000O00OOO000 in enumerate (O0OO0O0O000O0OO00 ["types"]):#line:860
                    if OOOO0000O00OOO000 =="SYNC":#line:861
                        if len (O0OO0O0O000O0OO00 ["updates"][OO0OOOO000OOOOO0O ])==0 :#line:862
                            O00OO0OOO0O00OOOO .endScraping =True #line:863
                            break #line:864
                        for OO00000OO0OO0O000 in O0OO0O0O000O0OO00 ["updates"][OO0OOOO000OOOOO0O ]:#line:866
                            if "member"in OO00000OO0OO0O000 :#line:867
                                O0000O0O00OO0O0O0 =OO00000OO0OO0O000 ["member"]#line:868
                                O0O00O00OO000O000 ={"tag":O0000O0O00OO0O0O0 ["user"]["username"]+"#"+O0000O0O00OO0O0O0 ["user"]["discriminator"],"id":O0000O0O00OO0O0O0 ["user"]["id"],}#line:874
                                if not O0000O0O00OO0O0O0 ["user"].get ("bot"):#line:875
                                    O00OO0OOO0O00OOOO .members [O0000O0O00OO0O0O0 ["user"]["id"]]=O0O00O00OO000O000 #line:876
                    elif OOOO0000O00OOO000 =="UPDATE":#line:878
                        for OO00000OO0OO0O000 in O0OO0O0O000O0OO00 ["updates"][OO0OOOO000OOOOO0O ]:#line:879
                            if "member"in OO00000OO0OO0O000 :#line:880
                                O0000O0O00OO0O0O0 =OO00000OO0OO0O000 ["member"]#line:881
                                O0O00O00OO000O000 ={"tag":O0000O0O00OO0O0O0 ["user"]["username"]+"#"+O0000O0O00OO0O0O0 ["user"]["discriminator"],"id":O0000O0O00OO0O0O0 ["user"]["id"],}#line:887
                                if not O0000O0O00OO0O0O0 ["user"].get ("bot"):#line:888
                                    O00OO0OOO0O00OOOO .members [O0000O0O00OO0O0O0 ["user"]["id"]]=O0O00O00OO000O000 #line:889
                    O00OO0OOO0O00OOOO .lastRange +=1 #line:891
                    O00OO0OOO0O00OOOO .ranges =Utils .getRanges (O00OO0OOO0O00OOOO .lastRange ,100 ,O00OO0OOO0O00OOOO .guilds [O00OO0OOO0O00OOOO .guild_id ]["member_count"])#line:894
                    time .sleep (0.45 )#line:895
                    O00OO0OOO0O00OOOO .scrapeUsers ()#line:896
            if O00OO0OOO0O00OOOO .endScraping :#line:898
                O00OO0OOO0O00OOOO .close ()#line:899
    def sock_close (O0OO000O0O00O0000 ,O0OO0000OOOO0OOOO ,OO0000OO00O00OOOO ,OO000OO00O0O00OO0 ):#line:901
        pass #line:902
def scrape (OO00O0O0O000O00O0 ,O000OO00OO0000OO0 ,OOOOO00O0O00O0OOO ):#line:904
    O00OOO0OOO00OOO0O =DiscordSocket (OO00O0O0O000O00O0 ,O000OO00OO0000OO0 ,OOOOO00O0O00O0OOO )#line:905
    return O00OOO0OOO00OOO0O .run ()#line:906
def member_scrape (O000OO0OO00OO0OOO ,OOOOOOO0O0OO0O000 ,O0OOOOOO0O000O000 ):#line:908
    O0O0O0O0O000O0OOO =[]#line:909
    for O000000OO0O0000OO in O000OO0OO00OO0OOO :#line:910
        OO0O0OO000OO0OO00 ={"Authorization":O000000OO0O0000OO ,"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}#line:911
        OO00OOOOO0O0O0O0O =session .get (f"https://canary.discord.com/api/v9/guilds/{OOOOOOO0O0OO0O000}",headers =OO0O0OO000OO0OO00 )#line:912
        if OO00OOOOO0O0O0O0O .status_code ==200 :#line:913
            O0O0O0O0O000O0OOO .append (O000000OO0O0000OO )#line:914
            break #line:915
    if not O0O0O0O0O000O0OOO :#line:916
        print ("missing access")#line:917
    O000000OO0O0000OO =random .choice (O0O0O0O0O000O0OOO )#line:919
    OOO000O0OO000O000 =scrape (O000000OO0O0000OO ,OOOOOOO0O0OO0O000 ,O0OOOOOO0O000O000 )#line:920
    OOO0OOOOOO0000OOO =[f"<@{OO0000O000O0O0O00}>"for OO0000O000O0O0O00 in [int (O00OOOO0O0000O000 )for O00OOOO0O0000O000 in OOO000O0OO000O000 .keys ()]]#line:921
    print (f"[SUCCESS] {len(OOO0OOOOOO0000OOO)} scraped members")#line:922
    return OOO0OOOOOO0000OOO #line:923
def spammer_menu ():#line:925
    try :#line:926
        with open ("token.txt")as O0OOO000O0OOO0OO0 :#line:927
            O0O0O0O0O00O0OO0O =[O0OOOO0O00O000O0O .strip ()for O0OOOO0O00O000O0O in O0OOO000O0OOO0OO0 .readlines ()if O0OOOO0O00O000O0O .strip ()]#line:928
    except (FileNotFoundError ,KeyError ):#line:929
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:930
        return #line:931
    OOOOOOOO000O0OO0O =input ("Server ID?: ").strip ()#line:933
    O0O0OO00OO000OO0O =input ("Message?: ").strip ()#line:934
    OO0OO0O00000O00O0 =input ("Random mention (True/False)?: ").strip ().lower ()=='true'#line:935
    OO000O0O0O0OO0OO0 =input ("Delay between messages (in seconds)?: ").strip ()#line:936
    OOO00O000OOOO00OO =input ("Number of messages to send?: ").strip ()#line:937
    OOO00000000O00000 =input ("Blacklist User IDs (comma-separated) (Leave blank to skip)?: ").strip ().split (',')#line:938
    OOO00000000O00000 =[f"<@{OO00O0O000O0OO00O.strip()}>"for OO00O0O000O0OO00O in OOO00000000O00000 if OO00O0O000O0OO00O .strip ()]#line:939
    try :#line:941
        OO000O0O0O0OO0OO0 =float (OO000O0O0O0OO0OO0 )#line:942
        if OO000O0O0O0OO0OO0 <0 :#line:943
            raise ValueError #line:944
    except ValueError :#line:945
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:946
        OO000O0O0O0OO0OO0 =1.0 #line:947
    try :#line:949
        OOO00O000OOOO00OO =int (OOO00O000OOOO00OO )#line:950
        if OOO00O000OOOO00OO <=0 :#line:951
            raise ValueError #line:952
    except ValueError :#line:953
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:954
        OOO00O000OOOO00OO =1 #line:955
    OOO00OOOOO0000000 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:957
    if OOO00OOOOO0000000 =='2':#line:958
        OOOO0O0O0OOOOOO00 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:959
        OOOO0O0O0OOOOOO00 =[OO00000OOO000O0OO .strip ()for OO00000OOO000O0OO in OOOO0O0O0OOOOOO00 if OO00000OOO000O0OO .strip ()]#line:960
    else :#line:961
        OOOO0O0O0OOOOOO00 =fetch_channels (O0O0O0O0O00O0OO0O [0 ],OOOOOOOO000O0OO0O )#line:962
    O0OOO0OOO000O0O00 =None #line:964
    spammer (O0O0O0O0O00O0OO0O ,OOOOOOOO000O0OO0O ,OOOO0O0O0OOOOOO00 ,O0O0OO00OO000OO0O ,OO0OO0O00000O00O0 ,OOO00000000O00000 ,O0OOO0OOO000O0O00 ,OOO00O000OOOO00OO )#line:966
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:969
def buildnumget (O00OO0000O0O0O0OO ):#line:971
  OO00O0O000OOO0OO0 =O00OO0000O0O0O0OO .get ('https://discord.com/login',headers ={'Accept-Encoding':'gzip, deflate'},timeout =7 )#line:972
  OOOO00000OOO0O0O0 =OO00O0O000OOO0OO0 .text #line:973
import discum #line:975
import random #line:976
import time #line:977
def userget (OO00O00O0O00OO0O0 ,O0O0O0O00OO0OO0O0 ,O00O0000O00OO000O ):#line:979
    O0O000O0O00O000OO =[]#line:980
    OO0O0O00OO0O0O0OO =discum .Client (token =OO00O00O0O00OO0O0 ,log =False )#line:981
    def OO0OOO0OO0OOO0OOO (OOO00OOOOOO0000O0 ):#line:983
        if OO0O0O00OO0O0O0OO .gateway .finishedMemberFetching (O0O0O0O00OO0OO0O0 ):#line:984
            O0O00OO0O0OOOOO0O =len (OO0O0O00OO0O0O0OO .gateway .session .guild (O0O0O0O00OO0OO0O0 ).members )#line:985
            print (str (O0O00OO0O0OOOOO0O )+' members fetched')#line:986
            OO0O0O00OO0O0O0OO .gateway .removeCommand ({'function':OO0OOO0OO0OOO0OOO ,'params':{}})#line:987
            OO0O0O00OO0O0O0OO .gateway .close ()#line:988
    def O0000O000OOO0000O (O000OOOOOO00O00O0 ,O00OOOOO0OOO000O0 ):#line:990
        OO0O0O00OO0O0O0OO .gateway .fetchMembers (O000OOOOOO00O00O0 ,O00OOOOO0OOO000O0 ,keep ='all',wait =1 )#line:991
        OO0O0O00OO0O0O0OO .gateway .command ({'function':OO0OOO0OO0OOO0OOO ,'params':{}})#line:992
        OO0O0O00OO0O0O0OO .gateway .run ()#line:993
        OO0O0O00OO0O0O0OO .gateway .resetSession ()#line:994
        return OO0O0O00OO0O0O0OO .gateway .session .guild (O000OOOOOO00O00O0 ).members #line:995
    O0O0O0000OOOO000O =O0000O000OOO0000O (O0O0O0O00OO0OO0O0 ,O00O0000O00OO000O )#line:997
    for OOO00O0OOO0O0000O in O0O0O0000OOOO000O :#line:998
        if OOO00O0OOO0O0000O not in O0O000O0O00O000OO :#line:999
            O0O000O0O00O000OO .append (f"<@{OOO00O0OOO0O0000O}>")#line:1000
    return O0O000O0O00O000OO #line:1001
def spammer (O0O00OO000O0000O0 ,OOOOO00O0O00O0OO0 ,O00O0O0OOO00OO00O ,OOO000O0OOO0OOO0O ,O00000OO00OO000O0 ,O00O0OO0OO000OO0O ,OO0O0O0OO0000OOOO ,O0OOO00OO00OO0OO0 ):#line:1006
    OO0O0OO00O0OO0OOO =get_session (OO0O0O0OO0000OOOO )#line:1007
    O0000O00O000OOOO0 =0 #line:1008
    O000O0OO00000000O =userget (O0O00OO000O0000O0 [0 ],OOOOO00O0O00O0OO0 ,O00O0O0OOO00OO00O [0 ])#line:1010
    O000O0OO00000000O =[OOOO000OOOOO0OO00 for OOOO000OOOOO0OO00 in O000O0OO00000000O if OOOO000OOOOO0OO00 not in O00O0OO0OO000OO0O ]#line:1013
    for _OO00OOOOOOO000O00 in range (O0OOO00OO00OO0OO0 ):#line:1015
        O0OO00O00OOOO00OO =O0O00OO000O0000O0 [O0000O00O000OOOO0 ]#line:1016
        O0O0OO0000O000OO0 =get_headers (O0OO00O00OOOO00OO )#line:1017
        for OOO0O0000O00O0O00 in O00O0O0OOO00OO00O :#line:1018
            OOO0O00O00OO0000O =OOO000O0OOO0OOO0O #line:1019
            if O00000OO00OO000O0 and O000O0OO00000000O :#line:1020
                OO00OOO000OO00O00 =random .choice (O000O0OO00000000O )#line:1021
                OOO0O00O00OO0000O +=f" {OO00OOO000OO00O00}"#line:1022
            OOOOO00O00000000O =OO0O0OO00O0OO0OOO .post (f"https://discord.com/api/v9/channels/{OOO0O0000O00O0O00}/messages",json ={"content":OOO0O00O00OO0000O },headers =O0O0OO0000O000OO0 )#line:1024
            if OOOOO00O00000000O .status_code ==200 :#line:1025
                print (f"200 message sent: {O0OO00O00OOOO00OO}")#line:1026
            elif OOOOO00O00000000O .status_code ==429 :#line:1027
                print (f"429 rate limit: {O0OO00O00OOOO00OO}")#line:1028
                O000O00OO0000OO0O =OOOOO00O00000000O .json ().get ("retry_after",1 )#line:1029
                time .sleep (O000O00OO0000OO0O )#line:1030
            elif OOOOO00O00000000O .status_code ==401 :#line:1031
                print (f"401 unknown token: {O0OO00O00OOOO00OO}")#line:1032
            else :#line:1033
                print (f"error: {O0OO00O00OOOO00OO}")#line:1034
        O0000O00O000OOOO0 =(O0000O00O000OOOO0 +1 )%len (O0O00OO000O0000O0 )#line:1036
        time .sleep (1 )#line:1037
import requests #line:1041
import base64 #line:1042
import colorama #line:1043
import time #line:1044
def add_emojis_from_files ():#line:1046
    try :#line:1047
        with open ("emojiname.txt")as OO00OO00OO0OOO0O0 ,open ("emojiurl.txt")as OOOOO0O00OOO0O00O :#line:1048
            O0000O000O0OO000O =[OOO0OO0000O0000OO .strip ()for OOO0OO0000O0000OO in OO00OO00OO0OOO0O0 .read ().split (',')if OOO0OO0000O0000OO .strip ()]#line:1049
            OO00O0O0000OO000O =[OOOO00OO0O0OOOOO0 .strip ()for OOOO00OO0O0OOOOO0 in OOOOO0O00OOO0O00O .read ().split (',')if OOOO00OO0O0OOOOO0 .strip ()]#line:1050
    except FileNotFoundError as O00OO0O000O00OOO0 :#line:1051
        print (f"{colorama.Fore.RED}    [!] Error: {str(O00OO0O000O00OOO0)}{colorama.Fore.RESET}")#line:1052
        return #line:1053
    if len (O0000O000O0OO000O )!=len (OO00O0O0000OO000O ):#line:1055
        print (f"{colorama.Fore.RED}    [!] Error: The number of emoji names and URLs do not match!{colorama.Fore.RESET}")#line:1056
        return #line:1057
    try :#line:1059
        with open ("token.txt")as OO00OOO0OOO0O0O0O :#line:1060
            O0OOOO0OOO000O000 =[OO00O0O0O00000O0O .strip ()for OO00O0O0O00000O0O in OO00OOO0OOO0O0O0O .readlines ()if OO00O0O0O00000O0O .strip ()]#line:1061
    except FileNotFoundError as O00OO0O000O00OOO0 :#line:1062
        print (f"{colorama.Fore.RED}    [!] Error: {str(O00OO0O000O00OOO0)}{colorama.Fore.RESET}")#line:1063
        return #line:1064
    O000000OOO0O00O0O =input ("Enter the Guild ID: ").strip ()#line:1066
    O0OO0OOOOOOOOOO00 =input ("Enter the rate limit between requests (in seconds): ").strip ()#line:1067
    try :#line:1069
        O0OO0OOOOOOOOOO00 =float (O0OO0OOOOOOOOOO00 )#line:1070
        if O0OO0OOOOOOOOOO00 <0 :#line:1071
            raise ValueError #line:1072
    except ValueError :#line:1073
        print (f"{colorama.Fore.RED}    [!] Invalid rate limit. Using default rate limit of 5 seconds.{colorama.Fore.RESET}")#line:1074
        O0OO0OOOOOOOOOO00 =5.0 #line:1075
    OO00O0OOO0O000OOO =set ()#line:1077
    for OO0OOO0OOO000OOOO in O0OOOO0OOO000O000 :#line:1079
        O0000O0O0OOOO0000 ={'Authorization':OO0OOO0OOO000OOOO ,'Content-Type':'application/json'}#line:1083
        O0OO0OO0O00O0OOOO =requests .get (f"https://discord.com/api/v9/guilds/{O000000OOO0O00O0O}/emojis",headers =O0000O0O0OOOO0000 )#line:1086
        if O0OO0OO0O00O0OOOO .status_code ==200 :#line:1087
            O0OO000OOO0O0OO0O =O0OO0OO0O00O0OOOO .json ()#line:1088
            for O00OO0O00O0O000O0 in O0OO000OOO0O0OO0O :#line:1089
                OO00O0OOO0O000OOO .add (O00OO0O00O0O000O0 ['name'])#line:1090
        else :#line:1091
            print (f"{colorama.Fore.RED}    [!] Error fetching existing emojis: {O0OO0OO0O00O0OOOO.status_code} - {O0OO0OO0O00O0OOOO.text}{colorama.Fore.RESET}")#line:1092
            continue #line:1093
    for O00OOO0OO0OO0O0O0 ,OO0O000O00O00O0OO in zip (O0000O000O0OO000O ,OO00O0O0000OO000O ):#line:1095
        if O00OOO0OO0OO0O0O0 in OO00O0OOO0O000OOO :#line:1096
            print (f"{colorama.Fore.YELLOW}    [*] Emoji '{O00OOO0OO0OO0O0O0}' already exists. Skipping...{colorama.Fore.RESET}")#line:1097
            continue #line:1098
        for OO0OOO0OOO000OOOO in O0OOOO0OOO000O000 :#line:1100
            try :#line:1101
                O0OO0OO0O00O0OOOO =requests .get (OO0O000O00O00O0OO )#line:1102
                O0OO0OO0O00O0OOOO .raise_for_status ()#line:1103
                O000O00OOOOO0000O =O0OO0OO0O00O0OOOO .content #line:1104
                OOOO0O0OO0O00000O =base64 .b64encode (O000O00OOOOO0000O ).decode ('utf-8')#line:1105
                OOO0O00000OOO0OO0 ={'name':O00OOO0OO0OO0O0O0 ,'image':f"data:image/png;base64,{OOOO0O0OO0O00000O}"}#line:1110
                O0000O0O0OOOO0000 ={'Authorization':OO0OOO0OOO000OOOO ,'Content-Type':'application/json'}#line:1115
                OOOO0O0OO00O00O0O =requests .post (f"https://discord.com/api/v9/guilds/{O000000OOO0O00O0O}/emojis",headers =O0000O0O0OOOO0000 ,json =OOO0O00000OOO0OO0 )#line:1117
                if OOOO0O0OO00O00O0O .status_code ==201 :#line:1118
                    print (f"{colorama.Fore.GREEN}    [+] Successfully added emoji '{O00OOO0OO0OO0O0O0}' with token {OO0OOO0OOO000OOOO}{colorama.Fore.RESET}")#line:1119
                    OO00O0OOO0O000OOO .add (O00OOO0OO0OO0O0O0 )#line:1120
                    break #line:1121
                else :#line:1122
                    print (f"{colorama.Fore.RED}    [!] Failed to add emoji '{O00OOO0OO0OO0O0O0}' with token {OO0OOO0OOO000OOOO}: {OOOO0O0OO00O00O0O.status_code} - {OOOO0O0OO00O00O0O.text}{colorama.Fore.RESET}")#line:1123
                time .sleep (O0OO0OOOOOOOOOO00 )#line:1125
            except Exception as O00OO0O000O00OOO0 :#line:1126
                print (f"{colorama.Fore.RED}    [!] Error adding emoji '{O00OOO0OO0OO0O0O0}' with token {OO0OOO0OOO000OOOO}: {str(O00OO0O000O00OOO0)}{colorama.Fore.RESET}")#line:1127
import random #line:1129
import time #line:1130
def pollspammer (O00O00O0O000O00OO ,O000O000O00O0OO0O ,O00O0O0O0OO0O0OO0 ,OO0O000OO00O0O0O0 ,O0O0O0O00OO000OOO ,OOOO0OO0O00O0OO00 ,OO00O00O00O000OOO ,OO0O0O000OOO0O00O ,O00O0O0O00O0000OO ,O0000O0O0OO00OOOO ,O0OO0O000O000O00O ,OO000OOO00O0O0O0O ):#line:1132
    O00OOO0OO0O000OOO =get_session ()#line:1133
    OO000O0O000000OOO =0 #line:1134
    OO00OO0000000OOO0 =userget (O00O00O0O000O00OO [0 ],O000O000O00O0OO0O ,O00O0O0O0OO0O0OO0 [0 ])#line:1136
    OO00OO0000000OOO0 =[O0000O00OO0OO00OO for O0000O00OO0OO00OO in OO00OO0000000OOO0 if O0000O00OO0OO00OO not in O00O0O0O00O0000OO ]#line:1139
    for _O0OOO0000OO00O000 in range (O0000O0O0OO00OOOO ):#line:1141
        OOOOOOO0O0O00000O =O00O00O0O000O00OO [OO000O0O000000OOO ]#line:1142
        OOO0O00OO0O0O0O0O =get_headers (OOOOOOO0O0O00000O )#line:1143
        for O00O0OO0000OOOO0O in O00O0O0O0OO0O0OO0 :#line:1148
            OOO0000O0000O00O0 =[{"poll_media":{"text":O00OOO0O0O000OOO0 .strip ()}}for O00OOO0O0O000OOO0 in O0O0O0O00OO000OOO .split (',')]#line:1149
            OO0OOOOOOO0O0OO00 ={"mobile_network_type":"unknown","content":"","nonce":str (random .randint (10 **17 ,10 **18 -1 )),"tts":False ,"flags":0 ,"poll":{"question":{"text":OO0O000OO00O0O0O0 },"answers":OOO0000O0000O00O0 ,"allow_multiselect":False ,"duration":OOOO0OO0O00O0OO00 ,"layout_type":1 }}#line:1163
            if OO00O00O00O000OOO and OO00OO0000000OOO0 :#line:1165
                OO0O00O0O0OOOO0OO =random .choice (OO00OO0000000OOO0 )#line:1167
                OO00O000OO0O0OOO0 ={"content":f"{OO0O0O000OOO0O00O} {OO0O00O0O0OOOO0OO}","tts":False ,"nonce":str (random .randint (10 **17 ,10 **18 -1 ))}#line:1172
                OOO0OO0O00OO0O0OO =O00OOO0OO0O000OOO .post (f"https://discord.com/api/v9/channels/{O00O0OO0000OOOO0O}/messages",json =OO00O000OO0O0OOO0 ,headers =OOO0O00OO0O0O0O0O )#line:1173
                if OOO0OO0O00OO0O0OO .status_code !=200 :#line:1174
                    print (f"Failed to send mention: {OOO0OO0O00OO0O0OO.status_code} - {OOO0OO0O00OO0O0OO.text}")#line:1175
            OO0000OO00O0OOO0O =O00OOO0OO0O000OOO .post (f"https://discord.com/api/v9/channels/{O00O0OO0000OOOO0O}/messages",json =OO0OOOOOOO0O0OO00 ,headers =OOO0O00OO0O0O0O0O )#line:1177
            if OO0000OO00O0OOO0O .status_code ==200 :#line:1178
                print (f"200 poll message sent: {OOOOOOO0O0O00000O}")#line:1179
            elif OO0000OO00O0OOO0O .status_code ==429 :#line:1180
                print (f"429 rate limit: {OOOOOOO0O0O00000O}")#line:1181
                O0O00000O0O0O0OOO =OO0000OO00O0OOO0O .json ().get ("retry_after",1 )#line:1182
                time .sleep (O0O00000O0O0O0OOO )#line:1183
            elif OO0000OO00O0OOO0O .status_code ==401 :#line:1184
                print (f"401 unknown token: {OOOOOOO0O0O00000O}")#line:1185
            else :#line:1186
                print (f"error: {OOOOOOO0O0O00000O} - {OO0000OO00O0OOO0O.status_code}: {OO0000OO00O0OOO0O.text}")#line:1187
        OO000O0O000000OOO =(OO000O0O000000OOO +1 )%len (O00O00O0O000O00OO )#line:1189
        time .sleep (OO000OOO00O0O0O0O )#line:1190
        time .sleep (O0OO0O000O000O00O )#line:1191
def pollspammermenu ():#line:1194
    with open ("token.txt")as OOO0OO0O0O0O0000O :#line:1195
        O000O00O0O00OOO0O =[OOOOOOOOOO0O00OOO .strip ()for OOOOOOOOOO0O00OOO in OOO0OO0O0O0O0000O .readlines ()if OOOOOOOOOO0O00OOO .strip ()]#line:1196
    OOO0O00OO0O0O0000 =input ("Enter Server ID: ").strip ()#line:1198
    O00000000O00O0000 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:1199
    if O00000000O00O0000 =='2':#line:1200
        O00OO00O00O0O0OO0 =input ("Enter Channel IDs (comma-separated): ").strip ().split (',')#line:1201
    else :#line:1202
        O00OO00O00O0O0OO0 =[]#line:1203
        for O0O00O00O0OOOO000 in O000O00O0O00OOO0O :#line:1204
            try :#line:1205
                O00OO00O00O0O0OO0 .extend (fetch_channels (O0O00O00O0OOOO000 ,OOO0O00OO0O0O0000 ))#line:1206
            except Exception as OOOOOO0O00000O000 :#line:1207
                print (f"[!] Failed to fetch channels for token. Error: {OOOOOO0O00000O000}")#line:1208
                continue #line:1209
        random .shuffle (O00OO00O00O0O0OO0 )#line:1210
    O00000O0OO00OO0OO =input ("Enter poll title: ").strip ()#line:1212
    O000OO0O0OOOOOOO0 =input ("Enter poll answers (comma-separated): ").strip ()#line:1213
    O00OO0O0O0000000O =int (input ("Enter poll duration (in hours 1/4/8/24/72/168/336 ): ").strip ())#line:1214
    OO0OO0OOOO0OOOOO0 =input ("Do you want to mention random users? (true/false): ").strip ().lower ()=='true'#line:1215
    OO00OOOO0OOOO000O =""#line:1216
    if OO0OO0OOOO0OOOOO0 :#line:1217
        OO00OOOO0OOOO000O =input ("Enter the message to prepend to the mention: ").strip ()#line:1218
    O00000O0OO0OO000O =input ("Enter blacklist user IDs (comma-separated): ").strip ().split (',')#line:1219
    O0OO00O000000000O =int (input ("Enter number of send poll: ").strip ())#line:1220
    OOOOO0000O0O0O000 =float (input ("Enter delay between posts (in seconds): ").strip ())#line:1221
    O0OO0O00OOOO0OO0O =float (input ("Enter rate limit (in seconds): ").strip ())#line:1222
    pollspammer (O000O00O0O00OOO0O ,OOO0O00OO0O0O0000 ,O00OO00O00O0O0OO0 ,O00000O0OO00OO0OO ,O000OO0O0OOOOOOO0 ,O00OO0O0O0000000O ,OO0OO0OOOO0OOOOO0 ,OO00OOOO0OOOO000O ,O00000O0OO0OO000O ,O0OO00O000000000O ,OOOOO0000O0O0O000 ,O0OO0O00OOOO0OO0O )#line:1224
def main ():#line:1227
    colorama .init ()#line:1228
    while True :#line:1229
        logo ()#line:1230
        O0O00O0O00OO00OO0 =input (f"{colorama.Fore.LIGHTMAGENTA_EX}    [Final] Select an option from above: ")#line:1231
        if O0O00O0O00OO00OO0 =="0":#line:1233
            update_group_ids ()#line:1234
        elif O0O00O0O00OO00OO0 =="1":#line:1235
            join_discord_invite ()#line:1236
        elif O0O00O0O00OO00OO0 =="2":#line:1237
            reaction_spammer ()#line:1238
        elif O0O00O0O00OO00OO0 =="3":#line:1239
            send_messages_with_mentions ()#line:1240
        elif O0O00O0O00OO00OO0 =="4":#line:1241
            spammer_menu ()#line:1242
        elif O0O00O0O00OO00OO0 =="5":#line:1243
            nickchanger ()#line:1244
        elif O0O00O0O00OO00OO0 =="6":#line:1245
            add_emojis_from_files ()#line:1246
        elif O0O00O0O00OO00OO0 =="7":#line:1247
            reaction_art ()#line:1248
        elif O0O00O0O00OO00OO0 =="8":#line:1249
            pollspammermenu ()#line:1250
        elif O0O00O0O00OO00OO0 =="0":#line:1251
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [*] Exiting the application. Goodbye!{colorama.Fore.RESET}")#line:1252
            break #line:1253
        else :#line:1254
            print (f"{colorama.Fore.RED}    [!] Invalid option selected!{colorama.Fore.RESET}")#line:1255
        input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:1257
if __name__ =="__main__":#line:1259
    main ()#line:1260
