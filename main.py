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
    OO0O0O00O0OOO0O0O =requests .Session ()#line:58
    if proxy :#line:59
        OO0O0O00O0OOO0O0O .proxies ={"http":proxy ,"https":proxy }#line:60
    return OO0O0O00O0OOO0O0O #line:61
def get_headers (OOOOO0O0O0O000O0O ):#line:63
    return {"Authorization":OOOOO0O0O0O000O0O ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:68
def send_message_with_mention (OO0000OOO0OOOO000 ,O00000O0OOOO00OO0 ,O00O000OO0OOOO00O ,OOOO00O00O0OOO000 ):#line:71
    OOO00O0OOO0O0OO00 =get_session ()#line:72
    OO0O00O000O000O00 =get_headers (OO0000OOO0OOOO000 )#line:73
    if OOOO00O00O0OOO000 :#line:75
        OOO0OO00OO00OO0O0 =random .choice (OOOO00O00O0OOO000 )#line:76
        O00O000OO0OOOO00O +=f" <@{OOO0OO00OO00OO0O0}>"#line:77
    OOOOO000OOOO00OO0 =OOO00O0OOO0O0OO00 .post (f"https://discord.com/api/v9/channels/{O00000O0OOOO00OO0}/messages",headers =OO0O00O000O000O00 ,json ={"content":O00O000OO0OOOO00O })#line:83
    if OOOOO000OOOO00OO0 .status_code in [200 ,201 ]:#line:84
        print (f"[+] Message sent to channel {O00000O0OOOO00OO0}")#line:85
    elif OOOOO000OOOO00OO0 .status_code ==429 :#line:86
        print ("[-] Rate limited. Please wait before retrying.")#line:87
        OO0000OO00000OOO0 =OOOOO000OOOO00OO0 .json ().get ("retry_after",1 )#line:88
        time .sleep (OO0000OO00000OOO0 )#line:89
    else :#line:90
        print (f"[!] Error occurred: {OOOOO000OOOO00OO0.status_code}")#line:91
def fetch_messages (O0O0OO000O000OO0O ,OO0OO00OO000OOOOO ,limit =100 ):#line:94
    OO0OOO000OOO00OO0 ={"Authorization":O0O0OO000O000OO0O ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:99
    O0O0OOO00O0O0OO00 =requests .get (f"https://discord.com/api/v9/channels/{OO0OO00OO000OOOOO}/messages?limit={limit}",headers =OO0OOO000OOO00OO0 )#line:103
    if O0O0OOO00O0O0OO00 .status_code ==200 :#line:104
        return O0O0OOO00O0O0OO00 .json ()#line:105
    else :#line:106
        print (f"[!] Failed to fetch messages. HTTP Status Code: {O0O0OOO00O0O0OO00.status_code}")#line:107
        return []#line:108
import concurrent .futures #line:110
def reaction_spammer ():#line:112
    try :#line:113
        with open ("token.txt")as O00000000OOOOOO00 :#line:114
            OO0OO0OO0OO000O0O =[OOOOO0O000OO00OO0 .strip ()for OOOOO0O000OO00OO0 in O00000000OOOOOO00 .readlines ()if OOOOO0O000OO00OO0 .strip ()]#line:115
    except (FileNotFoundError ,KeyError ):#line:116
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:117
        return #line:118
    O000OO0OO00OO000O =input ("Server ID?: ").strip ()#line:120
    OOO0O00OOOOO0OO0O =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:122
    if OOO0O00OOOOO0OO0O =='2':#line:123
        OOOOOOO0OOO0OOOOO =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:124
        O000O0000000000OO =[O0OOO0000OOO0O000 .strip ()for O0OOO0000OOO0O000 in OOOOOOO0OOO0OOOOO if O0OOO0000OOO0O000 .strip ()]#line:125
    else :#line:126
        O000O0000000000OO =[]#line:127
        for OOOO0OOO0000OOOO0 in OO0OO0OO0OO000O0O :#line:128
            try :#line:129
                O000O0000000000OO .extend (fetch_channels (OOOO0OOO0000OOOO0 ,O000OO0OO00OO000O ))#line:130
            except Exception as O0000OO00O0O0O00O :#line:131
                print (f"[!] Failed to fetch channels for token. Error: {O0000OO00O0O0O00O}")#line:132
                continue #line:133
    O0O00OO00000OOO0O =input ("Select your emoji (a, b, c, ... or custom emojis): ").strip ()#line:135
    OOOO00O0000O00O0O =input ("Delay between reactions (in seconds)?: ").strip ()#line:136
    try :#line:138
        OOOO00O0000O00O0O =float (OOOO00O0000O00O0O )#line:139
        if OOOO00O0000O00O0O <0 :#line:140
            raise ValueError #line:141
    except ValueError :#line:142
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:143
        OOOO00O0000O00O0O =1.0 #line:144
    O0OOOOOO000O0O0OO =[]#line:146
    for OO000OO0OOO00OOO0 in O0O00OO00000OOO0O .split (","):#line:147
        OO000OO0OOO00OOO0 =OO000OO0OOO00OOO0 .strip ().lower ()#line:148
        if OO000OO0OOO00OOO0 in alphabet_to_flag :#line:149
            O0OOOOOO000O0O0OO .append (alphabet_to_flag [OO000OO0OOO00OOO0 ])#line:150
        else :#line:151
            O0OOOOOO000O0O0OO .append (OO000OO0OOO00OOO0 )#line:152
    if not O0OOOOOO000O0O0OO :#line:154
        print (f"{colorama.Fore.RED}    [!] No valid emojis provided!{colorama.Fore.RESET}")#line:155
        return #line:156
    def OOO0OOOOO0O00O0OO (O00OOOO0O0OO0O0O0 ):#line:158
        for OO0000O0OOO0OOO00 in O000O0000000000OO :#line:159
            try :#line:160
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {OO0000O0OOO0OOO00}...{colorama.Fore.RESET}")#line:161
                OOO0O00OO00000OO0 =fetch_messages (O00OOOO0O0OO0O0O0 ,OO0000O0OOO0OOO00 ,limit =100 )#line:162
                if not OOO0O00OO00000OO0 :#line:163
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:164
                    continue #line:165
                for O0OOOOO000000OO00 in OOO0O00OO00000OO0 :#line:167
                    for O00O00OO00O000OO0 in O0OOOOOO000O0O0OO :#line:168
                        reactionput (O00OOOO0O0OO0O0O0 ,OO0000O0OOO0OOO00 ,O0OOOOO000000OO00 ['id'],O00O00OO00O000OO0 )#line:169
                        time .sleep (OOOO00O0000O00O0O )#line:170
            except Exception as OO0OOO0O00OOO0O00 :#line:171
                print (f"[!] Error processing channel {OO0000O0OOO0OOO00}. Error: {OO0OOO0O00OOO0O00}")#line:172
                continue #line:173
    with concurrent .futures .ThreadPoolExecutor ()as O0O0OO0O00000O00O :#line:175
        O000OO0O0OO0O0O00 =[O0O0OO0O00000O00O .submit (OOO0OOOOO0O00O0OO ,O0OOO000O000OO0OO )for O0OOO000O000OO0OO in OO0OO0OO0OO000O0O ]#line:176
        concurrent .futures .wait (O000OO0O0OO0O0O00 )#line:177
import requests #line:180
import json #line:181
import time #line:182
import colorama #line:183
alphabet_to_flag ={'a':'🇦','b':'🇧','c':'🇨','d':'🇩','e':'🇪','f':'🇫','g':'🇬','h':'🇭','i':'🇮','j':'🇯','k':'🇰','l':'🇱','m':'🇲','n':'🇳','o':'🇴','p':'🇵','q':'🇶','r':'🇷','s':'🇸','t':'🇹','u':'🇺','v':'🇻','w':'🇼','x':'🇽','y':'🇾','z':'🇿'}#line:191
def fetch_channels (O0O000000OO0000O0 ,O0OO0O000000O0OO0 ):#line:193
    OO00O0OO00O00OO0O =f"https://discord.com/api/v9/guilds/{O0OO0O000000O0OO0}/channels"#line:194
    O0O00OOOO0O0O0OO0 ={"Authorization":O0O000000OO0000O0 }#line:195
    O000O00O0O0O00OOO =requests .get (OO00O0OO00O00OO0O ,headers =O0O00OOOO0O0O0OO0 )#line:196
    if O000O00O0O0O00OOO .status_code ==200 :#line:197
        return [O0O0000OOOO0O0O00 ['id']for O0O0000OOOO0O0O00 in O000O00O0O0O00OOO .json ()if O0O0000OOOO0O0O00 ['type']==0 ]#line:198
    else :#line:199
        raise Exception (f"Failed to fetch channels: {O000O00O0O0O00OOO.status_code} - {O000O00O0O0O00OOO.text}")#line:200
def fetch_messages (O000000OO0OO00O0O ,OO00OOOOO0OOOO000 ,limit =100 ):#line:202
    O000OO00O0O0OOOO0 =f"https://discord.com/api/v9/channels/{OO00OOOOO0OOOO000}/messages?limit={limit}"#line:203
    OOO00000000000OOO ={"Authorization":O000000OO0OO00O0O }#line:204
    OO0OO00O0000OOO0O =requests .get (O000OO00O0O0OOOO0 ,headers =OOO00000000000OOO )#line:205
    if OO0OO00O0000OOO0O .status_code ==200 :#line:206
        return OO0OO00O0000OOO0O .json ()#line:207
    else :#line:208
        print (f"[!] Failed to fetch messages: {OO0OO00O0000OOO0O.status_code} - {OO0OO00O0000OOO0O.text}")#line:209
        return []#line:210
def reactionput (OOOOOO00OO00OOOO0 ,OO0O0O00O0O000O0O ,O00O0OO000O0O000O ,O0000O0OOO000000O ):#line:212
    O0O0O000OOO00OOOO =f"https://discord.com/api/v9/channels/{OO0O0O00O0O000O0O}/messages/{O00O0OO000O0O000O}/reactions/{O0000O0OOO000000O}/@me"#line:213
    OO0O0OOO0000OOOO0 ={"Authorization":OOOOOO00OO00OOOO0 ,"Content-Type":"application/json"}#line:214
    OOOOO0O0OO0O00OOO =requests .put (O0O0O000OOO00OOOO ,headers =OO0O0OOO0000OOOO0 )#line:215
    if OOOOO0O0OO0O00OOO .status_code not in [204 ,200 ]:#line:216
        print (f"{colorama.Fore.RED}    [!] Failed to add reaction: {OOOOO0O0OO0O00OOO.status_code} - {OOOOO0O0OO0O00OOO.text}{colorama.Fore.RESET}")#line:217
import random #line:219
def reaction_art ():#line:221
    try :#line:222
        with open ("token.txt",encoding ="utf-8")as OOO00O000O0OOO0O0 :#line:223
            OOOOOO0OOO0000OO0 =[O00000OO00O0O0000 .strip ()for O00000OO00O0O0000 in OOO00O000O0OOO0O0 .readlines ()if O00000OO00O0O0000 .strip ()]#line:224
    except (FileNotFoundError ,KeyError ):#line:225
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:226
        return #line:227
    O0O00O0O0OOO00OO0 =input ("Server ID?: ").strip ()#line:229
    OO00O0OOOO00OO000 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:231
    if OO00O0OOOO00OO000 =='2':#line:232
        O000OOOOOOOO000OO =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:233
        O0O0OO0O00O0OO0OO =[O00O000000OO0OO0O .strip ()for O00O000000OO0OO0O in O000OOOOOOOO000OO if O00O000000OO0OO0O .strip ()]#line:234
    else :#line:235
        O0O0OO0O00O0OO0OO =[]#line:236
        for OOOOOO00O000000OO in OOOOOO0OOO0000OO0 :#line:237
            try :#line:238
                O0O0OO0O00O0OO0OO .extend (fetch_channels (OOOOOO00O000000OO ,O0O00O0O0OOO00OO0 ))#line:239
            except Exception as OO0O0O00OOOOO0OO0 :#line:240
                print (f"[!] Failed to fetch channels for token. Error: {OO0O0O00OOOOO0OO0}")#line:241
                continue #line:242
        random .shuffle (O0O0OO0O00O0OO0OO )#line:243
    OO000OOO00000O000 =input ("Delay between reactions (in seconds)?: ").strip ()#line:245
    try :#line:247
        OO000OOO00000O000 =float (OO000OOO00000O000 )#line:248
        if OO000OOO00000O000 <0 :#line:249
            raise ValueError #line:250
    except ValueError :#line:251
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:252
        OO000OOO00000O000 =1.0 #line:253
    try :#line:255
        with open ("art.txt",encoding ="utf-8")as O000OOO0O0000O000 :#line:256
            O000000O00OOO0OO0 =[O0OO00O0OO00OOO0O .strip ()for O0OO00O0OO00OOO0O in O000OOO0O0000O000 .readlines ()if O0OO00O0OO00OOO0O .strip ()]#line:257
    except (FileNotFoundError ,KeyError ):#line:258
        print (f"{colorama.Fore.RED}    [!] Error: art.txt file not found or empty!{colorama.Fore.RESET}")#line:259
        return #line:260
    except UnicodeDecodeError as OO0O0O00OOOOO0OO0 :#line:261
        print (f"{colorama.Fore.RED}    [!] Error decoding art.txt: {str(OO0O0O00OOOOO0OO0)}{colorama.Fore.RESET}")#line:262
        return #line:263
    if not O000000O00OOO0OO0 :#line:265
        print (f"{colorama.Fore.RED}    [!] No valid art provided in art.txt!{colorama.Fore.RESET}")#line:266
        return #line:267
    O000000O00OOO0OO0 .reverse ()#line:270
    for OOOOOO00O000000OO in OOOOOO0OOO0000OO0 :#line:272
        for OO0OOOO0000OOO000 in O0O0OO0O00O0OO0OO :#line:273
            try :#line:274
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {OO0OOOO0000OOO000}...{colorama.Fore.RESET}")#line:275
                O0OO0O000O00O00OO =fetch_messages (OOOOOO00O000000OO ,OO0OOOO0000OOO000 ,limit =100 )#line:278
                if not O0OO0O000O00O00OO :#line:279
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:280
                    continue #line:281
                for O00OOOOOO00O0O0OO ,OOOOOO0O00000O0OO in enumerate (O0OO0O000O00O00OO ):#line:284
                    O00O0000O0000OOO0 =O000000O00OOO0OO0 [O00OOOOOO00O0O0OO %len (O000000O00OOO0OO0 )].split (',')#line:285
                    for OO00000000O00O000 in O00O0000O0000OOO0 :#line:286
                        reactionput (OOOOOO00O000000OO ,OO0OOOO0000OOO000 ,OOOOOO0O00000O0OO ['id'],OO00000000O00O000 .strip ())#line:287
                        print (f"Adding reaction '{OO00000000O00O000.strip()}' to message {OOOOOO0O00000O0OO['id']} in channel {OO0OOOO0000OOO000}")#line:288
                        time .sleep (OO000OOO00000O000 )#line:289
            except Exception as OO0O0O00OOOOO0OO0 :#line:290
                print (f"[!] Error processing channel {OO0OOOO0000OOO000}. Error: {OO0O0O00OOOOO0OO0}")#line:291
                continue #line:292
    def O0OOOOO00O0000OOO (O0O00000O0O0O0OOO ):#line:297
        for O00OO0O0O0O0O00O0 in O0O0OO0O00O0OO0OO :#line:298
            try :#line:299
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {O00OO0O0O0O0O00O0}...{colorama.Fore.RESET}")#line:300
                OOO0OOO0OOO00000O =fetch_messages (O0O00000O0O0O0OOO ,O00OO0O0O0O0O00O0 ,limit =100 )#line:301
                if not OOO0OOO0OOO00000O :#line:302
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:303
                    continue #line:304
                for O0OOOO000O0OO00O0 in OOO0OOO0OOO00000O :#line:306
                    for OO00OOO0O00OO0OO0 in O00O0000O0000OOO0 :#line:307
                        reactionput (O0O00000O0O0O0OOO ,O00OO0O0O0O0O00O0 ,O0OOOO000O0OO00O0 ['id'],OO00OOO0O00OO0OO0 )#line:308
                        time .sleep (OO000OOO00000O000 )#line:309
            except Exception as O0O00O0O0OOO000OO :#line:310
                print (f"[!] Error processing channel {O00OO0O0O0O0O00O0}. Error: {O0O00O0O0OOO000OO}")#line:311
                continue #line:312
    with concurrent .futures .ThreadPoolExecutor ()as O0OOOOO0O0O000OO0 :#line:314
        OO00OO00OO0000OO0 =[O0OOOOO0O0O000OO0 .submit (O0OOOOO00O0000OOO ,OOOO0OOOOO0OOOOOO )for OOOO0OOOOO0OOOOOO in OOOOOO0OOO0000OO0 ]#line:315
        concurrent .futures .wait (OO00OO00OO0000OO0 )#line:316
def update_group_ids ():#line:319
    try :#line:320
        with open ("token.txt")as OO0O0OOOO0OOOOOOO :#line:321
            OO0O0OO00OOO0O000 =[OOO0000O000O00OOO .strip ()for OOO0000O000O00OOO in OO0O0OOOO0OOOOOOO .readlines ()if OOO0000O000O00OOO .strip ()]#line:322
        OOO0O0O0OO0OOO000 =OO0O0OO00OOO0O000 [0 ]#line:323
    except (FileNotFoundError ,KeyError ):#line:324
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:325
        return #line:326
    O0O0OOOOO0O0O0OO0 ={"Authorization":OOO0O0O0OO0OOO000 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:332
    O0O0O0OOOOOO0OOO0 =requests .get ('https://discord.com/api/v9/users/@me/channels',headers =O0O0OOOOO0O0O0OO0 )#line:334
    if O0O0O0OOOOOO0OOO0 .status_code ==200 :#line:335
        OO0O0O0OOO0OOO00O =O0O0O0OOOOOO0OOO0 .json ()#line:336
        with open ("group_id.txt","w")as O0OOO00OO0OOOO00O :#line:337
            for OO0OO0O0O00OOOOO0 in OO0O0O0OOO0OOO00O :#line:338
                if OO0OO0O0O00OOOOO0 ['type']==3 :#line:339
                    O0OOO00OO0OOOO00O .write (OO0OO0O0O00OOOOO0 ['id']+'\n')#line:340
        print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Group IDs updated successfully.{colorama.Fore.RESET}")#line:341
    else :#line:342
        print (f"{colorama.Fore.LIGHTRED_EX}    [!] Failed to retrieve group IDs. HTTP Status Code: {O0O0O0OOOOOO0OOO0.status_code}{colorama.Fore.RESET}")#line:343
import requests #line:345
import requests #line:347
def fetch_channels (O00O00O0000O00000 ,OO0O00000O0O000O0 ):#line:349
    try :#line:350
        O0OO00OOO0OO0OO00 =requests .Session ()#line:351
        OOOO00O0O0O0OOOOO =get_headers (O00O00O0000O00000 )#line:352
        OO00O0OOOO00OO0O0 =O0OO00OOO0OO0OO00 .get (f"https://discord.com/api/v9/guilds/{OO0O00000O0O000O0}/channels",headers =OOOO00O0O0O0OOOOO ,timeout =10 )#line:359
        if OO00O0OOOO00OO0O0 .status_code ==200 :#line:362
            try :#line:363
                O0000OOOO0O0O0O0O =OO00O0OOOO00OO0O0 .json ()#line:364
                return [OOOOOO0O000O0O0OO ['id']for OOOOOO0O000O0O0OO in O0000OOOO0O0O0O0O if OOOOOO0O000O0O0OO .get ('type')==0 ]#line:365
            except ValueError :#line:366
                print ("[!] Error: Response was not valid JSON.")#line:367
                return []#line:368
        elif OO00O0OOOO00OO0O0 .status_code ==401 :#line:369
            print ("[!] Error: Unauthorized - check your token.")#line:370
        elif OO00O0OOOO00OO0O0 .status_code ==403 :#line:371
            print ("[!] Error: Forbidden - you lack permissions.")#line:372
        elif OO00O0OOOO00OO0O0 .status_code ==404 :#line:373
            print ("[!] Error: Server not found - check the server ID.")#line:374
        else :#line:375
            print (f"[!] Error: Unexpected status code {OO00O0OOOO00OO0O0.status_code}.")#line:376
        return []#line:379
    except requests .exceptions .Timeout :#line:381
        print ("[!] Error: Request timed out. Check your connection or try again later.")#line:382
        return []#line:383
    except requests .exceptions .RequestException as O0O0OOO0O0OOO00O0 :#line:384
        print (f"[!] Error: An error occurred while fetching channels: {O0O0OOO0O0OOO00O0}")#line:385
        return []#line:386
def extract_uids_from_messages (O00OOO00O00000000 ):#line:392
    O00OOO0O0O000O000 =set ()#line:393
    for O000O00OO0OOO0OOO in O00OOO00O00000000 :#line:394
        O00OOO0O0O000O000 .add (O000O00OO0OOO0OOO ['author']['id'])#line:395
    return list (O00OOO0O0O000O000 )#line:396
def send_message_with_mention (O00OO00OOO0OO0O0O ,OO00OOO0OO000000O ,OO0OO000O000000OO ,O0OO0O00OO0OO0000 ):#line:398
    O0O0OO0OO000O00O0 =get_session ()#line:399
    O0OOOO0OO000O0000 =get_headers (O00OO00OOO0OO0O0O )#line:400
    if O0OO0O00OO0OO0000 :#line:402
        O00O00OOO0OOO0OOO =random .choice (O0OO0O00OO0OO0000 )#line:403
        OO0OO000O000000OO +=f" <@{O00O00OOO0OOO0OOO}>"#line:404
    OOO00000OOOOOOO0O =O0O0OO0OO000O00O0 .post (f"https://discord.com/api/v9/channels/{OO00OOO0OO000000O}/messages",headers =O0OOOO0OO000O0000 ,json ={"content":OO0OO000O000000OO })#line:410
    if OOO00000OOOOOOO0O .status_code in [200 ,201 ]:#line:411
        print (f"[+] Message sent to channel {OO00OOO0OO000000O}")#line:412
    elif OOO00000OOOOOOO0O .status_code ==429 :#line:413
        print ("[-] Rate limited. Please wait before retrying.")#line:414
        OOOO0O00000OOO0O0 =OOO00000OOOOOOO0O .json ().get ("retry_after",1 )#line:415
        time .sleep (OOOO0O00000OOO0O0 )#line:416
    else :#line:417
        print (f"[!] Error occurred: {OOO00000OOOOOOO0O.status_code}")#line:418
def send_messages_with_mentions ():#line:419
    try :#line:420
        with open ("token.txt")as OO00OOOOOOOO00O0O :#line:421
            OOO00O0O0OO0OOO0O =[OOOO0O000OOO0OO00 .strip ()for OOOO0O000OOO0OO00 in OO00OOOOOOOO00O0O .readlines ()if OOOO0O000OOO0OO00 .strip ()]#line:422
    except (FileNotFoundError ,KeyError ):#line:423
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:424
        return #line:425
    O00O00OOOO0O00000 =input ("Server ID?: ").strip ()#line:427
    OO00O000O0OO0OOO0 =input ("Delay between messages (in seconds)?: ").strip ()#line:428
    O0O0O0O0OOO000000 =input ("Number of messages to send?: ").strip ()#line:429
    OO00O0OO00OO0OO00 =input ("Message content?: ").strip ()#line:430
    O00OOO00O0OOOO0OO =input ("Blacklist User IDs (comma-separated)?: ").strip ().split (',')#line:431
    O00OOO00O0OOOO0OO =[OOOO0O00O0OOOO000 .strip ()for OOOO0O00O0OOOO000 in O00OOO00O0OOOO0OO if OOOO0O00O0OOOO000 .strip ()]#line:432
    try :#line:434
        OO00O000O0OO0OOO0 =float (OO00O000O0OO0OOO0 )#line:435
        if OO00O000O0OO0OOO0 <0 :#line:436
            raise ValueError #line:437
    except ValueError :#line:438
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:439
        OO00O000O0OO0OOO0 =1.0 #line:440
    try :#line:442
        O0O0O0O0OOO000000 =int (O0O0O0O0OOO000000 )#line:443
        if O0O0O0O0OOO000000 <=0 :#line:444
            raise ValueError #line:445
    except ValueError :#line:446
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:447
        O0O0O0O0OOO000000 =1 #line:448
    OO0O000O0O0O0O000 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:450
    if OO0O000O0O0O0O000 =='2':#line:451
        OO00O00OO0O0OO000 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:452
        OO00O00OO0O0OO000 =[OO000O00O0OO0OO0O .strip ()for OO000O00O0OO0OO0O in OO00O00OO0O0OO000 if OO000O00O0OO0OO0O .strip ()]#line:453
    else :#line:454
        OO00O00OO0O0OO000 =[]#line:455
    O0OOOOOOOO0O0O000 =set ()#line:457
    for O0OOO00O00O000OO0 in OOO00O0O0OO0OOO0O :#line:458
        O0OOOO00000O00OO0 =fetch_channels (O0OOO00O00O000OO0 ,O00O00OOOO0O00000 )#line:459
        for OO0O00O000O0000OO in O0OOOO00000O00OO0 :#line:460
            O00O0OO0O0000O0OO =fetch_messages (O0OOO00O00O000OO0 ,OO0O00O000O0000OO ,limit =100 )#line:461
            O000000OO0O00OOO0 =extract_uids_from_messages (O00O0OO0O0000O0OO )#line:462
            O0OOOOOOOO0O0O000 .update (O000000OO0O00OOO0 )#line:463
    O0OOOOOOOO0O0O000 =list (set (O0OOOOOOOO0O0O000 )-set (O00OOO00O0OOOO0OO ))#line:466
    for _O0OO0000O0OOO0OO0 in range (O0O0O0O0OOO000000 ):#line:468
        for O0OOO00O00O000OO0 in OOO00O0O0OO0OOO0O :#line:469
            if OO00O00OO0O0OO000 :#line:470
                O0OOOO00000O00OO0 =OO00O00OO0O0OO000 #line:471
            for OO0O00O000O0000OO in O0OOOO00000O00OO0 :#line:472
                send_message_with_mention (O0OOO00O00O000OO0 ,OO0O00O000O0000OO ,OO00O0OO00OO0OO00 ,O0OOOOOOOO0O0O000 )#line:473
                time .sleep (OO00O000O0OO0OOO0 )#line:474
def join_discord_invite ():#line:479
    try :#line:480
        with open ("token.txt")as O0O0O0O00000OOO0O :#line:481
            O00O0O0OOO0OO00OO =[O000O000O0000O0O0 .strip ()for O000O000O0000O0O0 in O0O0O0O00000OOO0O .readlines ()if O000O000O0000O0O0 .strip ()]#line:482
    except (FileNotFoundError ,KeyError ):#line:483
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:484
        return #line:485
    OOO0OOO00OOOO0O0O =input ("Invite Code?: discord.gg/").strip ()#line:487
    for OO0O0O000OO0OOOO0 in O00O0O0OOO0OO00OO :#line:490
        joiner (OO0O0O000OO0OOOO0 ,OOO0OOO00OOOO0O0O )#line:491
import json ,time ,base64 ,random ,requests #line:493
def cookieset (O0000000OO00O0OO0 ):#line:495
    O00000O00000O0000 =O0000000OO00O0OO0 .get ("https://discord.com/app")#line:496
    return O00000O00000O0000 .cookies .get_dict ()#line:497
def generatexspandua (OO000000O00000OOO ):#line:499
    O00OO0O000000O00O =["Android","Windows","Macintosh"]#line:500
    O00OO0OO0O00OOOO0 =random .choice (O00OO0O000000O00O )#line:501
    if O00OO0OO0O00OOOO0 =="Macintosh":#line:502
        O0OOO00OO0OO00OOO =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:503
        OOOOOOO0OO00O0000 ="Macintosh; Intel Mac OS X "+O0OOO00OO0OO00OOO #line:504
        OOOOOOOOO0O00OOOO ="x86_64"#line:505
    elif O00OO0OO0O00OOOO0 =="Windows":#line:506
        O0OOO00OO0OO00OOO =f'{random.choice([6.0, 10.0, 11.0])}'#line:507
        OOOOOOO0OO00O0000 ="Windows NT "+O0OOO00OO0OO00OOO +" Win64; x64"#line:508
        OOOOOOOOO0O00OOOO ="x86_64"#line:509
    else :#line:510
        O0OOO00OO0OO00OOO ="13"#line:511
        OOOOOOO0OO00O0000 =f"Linux; Android 13; Pixel 6a"#line:512
        OOOOOOOOO0O00OOOO ="aarch64"#line:513
    OO00OO000000OO0OO ={"os":O00OO0OO0O00OOOO0 ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":O0OOO00OO0OO00OOO ,"os_arch":OOOOOOOOO0O00OOOO ,"system_locale":"ja-JP","client_build_number":OO000000O00000OOO ,"client_event_source":None ,"design_id":0 }#line:526
    OOO000O0000O000O0 =f"Mozilla/5.0 ({OOOOOOO0OO00O0000}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:527
    return base64 .b64encode (json .dumps (OO00OO000000OO0OO ,separators =(',',':')).encode ()).decode (),OOO000O0000O000O0 #line:528
def joiner (OOOO0O0OOOO00O0OO ,O0O0O0000000O0O00 ,OO00O000O0OOOO000 ,O00000O000O000O00 ):#line:530
  O00O0OO0O0O0000O0 =get_session (OO00O000O0OOOO000 )#line:531
  O00O0OO0000O00OO0 =cookieset (O00O0OO0O0O0000O0 )#line:532
  O00O0OO0000O00OO0 ["locale"]="ja-JP"#line:533
  O00O00O000000000O =201211 #line:534
  O0O0OO000OO0O0OOO ,O000OO0OO0OO000OO =generatexspandua (O00O00O000000000O )#line:535
  OOOO0OOOOO0O00OO0 ={"Authorization":OOOO0O0OOOO00O0OO ,"accept":"*/*","accept-language":"ja-JP","connection":"keep-alive","DNT":"1","origin":"https://discord.com","sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","referer":"https://discord.com/channels/@me","TE":"Trailers","user-agent":O000OO0OO0OO000OO ,"X-Super-Properties":O0O0OO000OO0O0OOO ,}#line:550
  OOOOO00OOOOO000O0 =O00O0OO0O0O0000O0 .post ("https://discord.com/api/v9/invites/"+O0O0O0000000O0O00 ,headers =OOOO0OOOOO0O00OO0 ,json ={},cookies =O00O0OO0000O00OO0 )#line:552
  if OOOOO00OOOOO000O0 .status_code ==200 :#line:553
    print ("[+] Probably joined "+OOOO0O0OOOO00O0OO )#line:554
    if "show_verification_form"in OOOOO00OOOOO000O0 .json ():#line:555
      bypass (OOOO0O0OOOO00O0OO ,OOOOO00OOOOO000O0 .json ()["guild"]["id"],O00O0OO0O0O0000O0 ,OOOO0OOOOO0O00OO0 )#line:556
    return #line:557
  elif "captcha_key"in OOOOO00OOOOO000O0 .text and OOOOO00OOOOO000O0 .status_code ==400 :#line:558
    print ("[!] Hcaptcha interference "+OOOO0O0OOOO00O0OO )#line:559
    return #line:560
  elif OOOOO00OOOOO000O0 .status_code ==401 :#line:561
    print ("[!] Token is dead "+OOOO0O0OOOO00O0OO )#line:562
    return #line:563
  elif OOOOO00OOOOO000O0 .status_code ==403 :#line:564
    if "message"in OOOOO00OOOOO000O0 .json ():#line:565
      if OOOOO00OOOOO000O0 .json ()["message"]=="Unknown Message":#line:566
        print ("[!] Unknown error "+OOOO0O0OOOO00O0OO )#line:567
        return #line:568
      else :#line:569
        print ("[!] Verification required "+OOOO0O0OOOO00O0OO )#line:570
        return #line:571
    else :#line:572
      print ("[!] Error occurred "+OOOO0O0OOOO00O0OO )#line:573
      return #line:574
  elif OOOOO00OOOOO000O0 .status_code ==429 :#line:575
    print ("[!] Token rate-limited "+OOOO0O0OOOO00O0OO )#line:576
    return #line:577
  elif OOOOO00OOOOO000O0 .status_code ==400 :#line:578
    if "captcha_key"in OOOOO00OOOOO000O0 .json ():#line:579
      print ("[!] Hcaptcha interference "+OOOO0O0OOOO00O0OO )#line:580
      return #line:581
    else :#line:582
      print ("[!] Error occurred "+OOOO0O0OOOO00O0OO )#line:583
      return #line:584
  elif OOOOO00OOOOO000O0 .status_code ==401 :#line:585
    print ("[!] Token is dead "+OOOO0O0OOOO00O0OO )#line:586
    return #line:587
  elif OOOOO00OOOOO000O0 .status_code ==403 :#line:588
    if "message"in OOOOO00OOOOO000O0 .json ():#line:589
      if OOOOO00OOOOO000O0 .json ()["message"]=="Unknown Message":#line:590
        print ("[!] Unknown error "+OOOO0O0OOOO00O0OO )#line:591
        return #line:592
      else :#line:593
        print ("[!] Verification required "+OOOO0O0OOOO00O0OO )#line:594
        return #line:595
    else :#line:596
      print ("[!] Error occurred "+OOOO0O0OOOO00O0OO )#line:597
  elif OOOOO00OOOOO000O0 .status_code ==429 :#line:598
    print ("[!] Token rate-limited "+OOOO0O0OOOO00O0OO )#line:599
    return #line:600
  else :#line:601
    print ("[!] Error occurred "+OOOO0O0OOOO00O0OO )#line:602
    return #line:603
def update_group_ids ():#line:606
    O0O0OO000O0O00O0O =input ("Invite Code?: ").strip ()#line:607
    try :#line:608
        with open ("token.txt")as OOOO00O000O0000O0 :#line:609
            OOOO0O000OOO0OO0O =[OO0000O0OO000O0OO .strip ()for OO0000O0OO000O0OO in OOOO00O000O0000O0 .readlines ()if OO0000O0OO000O0OO .strip ()]#line:610
    except (FileNotFoundError ,KeyError ):#line:611
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:612
        return #line:613
    O00OO0OOO0000O0O0 =requests .Session ()#line:615
    for OO00OOOO00000OOOO in OOOO0O000OOO0OO0O :#line:616
        joiner (OO00OOOO00000OOOO ,O0O0OO000O0O00O0O ,O00OO0OOO0000O0O0 )#line:617
        time .sleep (2 )#line:618
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:620
def bypass (OOOO0O00O0O0O0O0O ,OOOOOO00O0000O000 ,OOOOO000OOO00O00O ,OOOO00O0OOO0OOOO0 ):#line:623
    try :#line:624
        O00OOOO0O0OOO0O00 =OOOOO000OOO00O00O .get (f"https://discord.com/api/v9/guilds/{OOOOOO00O0000O000}/member-verification?with_guild=false",headers =OOOO00O0OOO0OOOO0 ).json ()#line:625
        OO0OO00000O0O0OO0 =OOOOO000OOO00O00O .put (f"https://discord.com/api/v9/guilds/{OOOOOO00O0000O000}/requests/@me",headers =OOOO00O0OOO0OOOO0 ,json =O00OOOO0O0OOO0O00 )#line:626
        if OO0OO00000O0O0OO0 .status_code ==201 :#line:627
            print (f"[+] MemberscreeningBypassed {OOOO0O00O0O0O0O0O}")#line:628
            return #line:629
        else :#line:630
            print (f"[!] Bypassが出来ませんでした {OOOO0O00O0O0O0O0O}")#line:631
            return #line:632
    except Exception as OO000OOO0OO0OOOO0 :#line:633
        print (f"[!] エラーが発生しました。{OO000OOO0OO0OOOO0}")#line:634
session =requests .Session ()#line:636
def reactionput (OO00OO00O0000000O ,OOO00000O0O00O0O0 ,OOOOOOO0O00O00000 ,O0000OOOO0O000OO0 ,proxy =None ):#line:639
    O0000OO0O0OOOOO0O =get_session (proxy )#line:640
    O00OO000O000000O0 =get_headers (O0000OO0O0OOOOO0O )#line:641
    O00OO000O000000O0 ["Authorization"]=OO00OO00O0000000O #line:642
    O0000OOOO0O000OO0 =requests .utils .quote (O0000OOOO0O000OO0 )#line:644
    O0O0O00O00O0O0OOO =O0000OO0O0OOOOO0O .put (f"https://discord.com/api/v9/channels/{OOO00000O0O00O0O0}/messages/{OOOOOOO0O00O00000}/reactions/{O0000OOOO0O000OO0}/%40me?location=Message&type=0",headers =O00OO000O000000O0 )#line:648
    if O0O0O00O00O0O0OOO .status_code in [200 ,204 ]:#line:649
        print (f"[+] Reaction '{O0000OOOO0O000OO0}' added successfully to message {OOOOOOO0O00O00000}")#line:650
    elif O0O0O00O00O0O0OOO .status_code ==429 :#line:651
        print ("[-] Rate limited. Please wait before retrying.")#line:652
        OO0OO0O0OO00OO00O =O0O0O00O00O0O0OOO .json ().get ("retry_after",1 )#line:653
        time .sleep (OO0OO0O0OO00OO00O )#line:654
    elif O0O0O00O00O0O0OOO .status_code ==401 :#line:655
        print ("[-] Invalid or expired token.")#line:656
    else :#line:657
        print (f"[!] Error occurred: {O0O0O00O00O0O0OOO.status_code}")#line:658
def generatexspandua (OOO0OOO00O0OO0OOO ):#line:661
  OOO00O00O0OOOO00O =["Android","Windows","Macintosh"]#line:662
  OOO0O00O0OO0O0O0O =random .choice (OOO00O00O0OOOO00O )#line:663
  if OOO0O00O0OO0O0O0O =="Macintosh":#line:664
    OOOO0O0O000000OO0 =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:665
    O000O00OOO0O0O0OO ="Macintosh; Intel Mac OS X "+OOOO0O0O000000OO0 #line:666
    OO00O0OO0O000O0O0 ="x86_64"#line:667
  if OOO0O00O0OO0O0O0O =="Windows":#line:668
    OOOO0O0O000000OO0 =f'{random.choice([6.0,10.0,11.0])}'#line:669
    O000O00OOO0O0O0OO ="Windows NT "+OOOO0O0O000000OO0 +" Win64; x64"#line:670
    OO00O0OO0O000O0O0 ="x86_64"#line:671
  if OOO0O00O0OO0O0O0O =="Android":#line:672
    OOOO0O0O000000OO0 ="13"#line:673
    O000O00OOO0O0O0OO =f"Linux; Android 13; Pixel 6a"#line:674
    OO00O0OO0O000O0O0 ="aarch64"#line:675
  OO0O0O00O0O000000 ={"os":OOO0O00O0OO0O0O0O ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":OOOO0O0O000000OO0 ,"os_arch":OO00O0OO0O000O0O0 ,"system_locale":"ja-JP","client_build_number":OOO0OOO00O0OO0OOO ,"client_event_source":None ,"design_id":0 }#line:676
  O00O0OO0O000OOO00 =f"Mozilla/5.0 ({O000O00OOO0O0O0OO}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:677
  return base64 .b64encode (json .dumps (OO0O0O00O0O000000 ,separators =(',',':')).encode ()).decode (),O00O0OO0O000OOO00 #line:678
import base64 #line:680
def nickchanger ():#line:683
    try :#line:684
        with open ("token.txt")as OOOOO0O00O00OO0OO :#line:685
            OO0000OO000O000OO =[O0OO0000000O000OO .strip ()for O0OO0000000O000OO in OOOOO0O00O00OO0OO .readlines ()if O0OO0000000O000OO .strip ()]#line:686
    except (FileNotFoundError ,KeyError ):#line:687
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:688
        return #line:689
    O00000O0OO0OOO000 =input ("Server ID?: ").strip ()#line:691
    OO0O00OOOOO000000 =input ("Nickname?: ").strip ()#line:692
    OOO0OO0OO0O00O0OO =input ("Delay (in seconds)?: ").strip ()#line:693
    try :#line:695
        OOO0OO0OO0O00O0OO =float (OOO0OO0OO0O00O0OO )#line:696
        if OOO0OO0OO0O00O0OO <0 :#line:697
            raise ValueError #line:698
    except ValueError :#line:699
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:700
        OOO0OO0OO0O00O0OO =1.0 #line:701
    for O0OO0OO0OOO0O0O00 in OO0000OO000O000OO :#line:703
        O0000O0O0O0O0OO0O ={"Authorization":O0OO0OO0OOO0O0O00 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:708
        O000OO000O0000000 ={"nick":OO0O00OOOOO000000 }#line:709
        OO0O00O000OOO0000 =requests .patch (f"https://discord.com/api/v9/guilds/{O00000O0OO0OOO000}/members/@me",headers =O0000O0O0O0O0OO0O ,json =O000OO000O0000000 )#line:710
        if OO0O00O000OOO0000 .status_code ==200 :#line:712
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Nickname changed to '{OO0O00OOOOO000000}' successfully for token {O0OO0OO0OOO0O0O00}.{colorama.Fore.RESET}")#line:713
        elif OO0O00O000OOO0000 .status_code ==429 :#line:714
            print (f"{colorama.Fore.RED}    [!] Rate limited. Please wait before retrying for token {O0OO0OO0OOO0O0O00}.{colorama.Fore.RESET}")#line:715
            OO0OOO00O000O000O =OO0O00O000OOO0000 .json ().get ("retry_after",1 )#line:716
            time .sleep (OO0OOO00O000O000O )#line:717
        else :#line:718
            print (f"{colorama.Fore.RED}    [!] Error occurred: {OO0O00O000OOO0000.status_code} for token {O0OO0OO0OOO0O0O00}.{colorama.Fore.RESET}")#line:719
        time .sleep (OOO0OO0OO0O00O0OO )#line:721
import json ,websocket ,threading ,tls_client ,random ,time #line:725
session =tls_client .Session (client_identifier ="chrome112",random_tls_extension_order =True )#line:727
class Utils :#line:729
    @staticmethod #line:730
    def rangeCorrector (O0000OOO00OOO0O00 ):#line:731
        if [0 ,99 ]not in O0000OOO00OOO0O00 :#line:732
            O0000OOO00OOO0O00 .insert (0 ,[0 ,99 ])#line:733
        return O0000OOO00OOO0O00 #line:734
    @staticmethod #line:736
    def getRanges (OOO0OO00OOOOOOO00 ,O00O0000OOOOO0000 ,O0OO0O0OOO0O0OOO0 ):#line:737
        OO0O0OOO000OO00O0 =int (OOO0OO00OOOOOOO00 *O00O0000OOOOO0000 )#line:738
        OOO0OO0O000O00000 =[[OO0O0OOO000OO00O0 ,OO0O0OOO000OO00O0 +99 ]]#line:739
        if O0OO0O0OOO0O0OOO0 >OO0O0OOO000OO00O0 +99 :#line:740
            OOO0OO0O000O00000 .append ([OO0O0OOO000OO00O0 +100 ,OO0O0OOO000OO00O0 +199 ])#line:741
        return Utils .rangeCorrector (OOO0OO0O000O00000 )#line:742
    @staticmethod #line:744
    def parseGuildMemberListUpdate (OOO00OOOO0O000O00 ):#line:745
        OO0OO00O00O000O0O ={"online_count":OOO00OOOO0O000O00 ["d"]["online_count"],"member_count":OOO00OOOO0O000O00 ["d"]["member_count"],"id":OOO00OOOO0O000O00 ["d"]["id"],"guild_id":OOO00OOOO0O000O00 ["d"]["guild_id"],"hoisted_roles":OOO00OOOO0O000O00 ["d"]["groups"],"types":[],"locations":[],"updates":[],}#line:755
        for OOO0O0O0O0OO00000 in OOO00OOOO0O000O00 ["d"]["ops"]:#line:757
            OO0OO00O00O000O0O ["types"].append (OOO0O0O0O0OO00000 ["op"])#line:758
            if OOO0O0O0O0OO00000 ["op"]in ("SYNC","INVALIDATE"):#line:759
                OO0OO00O00O000O0O ["locations"].append (OOO0O0O0O0OO00000 ["range"])#line:760
                if OOO0O0O0O0OO00000 ["op"]=="SYNC":#line:761
                    OO0OO00O00O000O0O ["updates"].append (OOO0O0O0O0OO00000 ["items"])#line:762
                else :#line:763
                    OO0OO00O00O000O0O ["updates"].append ([])#line:764
            elif OOO0O0O0O0OO00000 ["op"]in ("INSERT","UPDATE","DELETE"):#line:765
                OO0OO00O00O000O0O ["locations"].append (OOO0O0O0O0OO00000 ["index"])#line:766
                if OOO0O0O0O0OO00000 ["op"]=="DELETE":#line:767
                    OO0OO00O00O000O0O ["updates"].append ([])#line:768
                else :#line:769
                    OO0OO00O00O000O0O ["updates"].append (OOO0O0O0O0OO00000 ["item"])#line:770
        return OO0OO00O00O000O0O #line:771
class DiscordSocket (websocket .WebSocketApp ):#line:773
    def __init__ (O00O0O00O000OO0OO ,O0O00O0O000O00OOO ,OOO0O00OOO000000O ,OOOOOOO0OOOO000OO ):#line:774
        O00O0O00O000OO0OO .token =O0O00O0O000O00OOO #line:775
        O00O0O00O000OO0OO .guild_id =OOO0O00OOO000000O #line:776
        O00O0O00O000OO0OO .channel_id =OOOOOOO0OOOO000OO #line:777
        O00O0O00O000OO0OO .socket_headers ={"Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","Cache-Control":"no-cache","Pragma":"no-cache","Sec-WebSocket-Extensions":"permessage-deflate; client_max_window_bits","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",}#line:785
        super ().__init__ ("wss://gateway.discord.gg/?encoding=json&v=9",header =O00O0O00O000OO0OO .socket_headers ,on_open =lambda OOOOO00OOOOO0O00O :O00O0O00O000OO0OO .sock_open (OOOOO00OOOOO0O00O ),on_message =lambda O0O0OOOO00000O00O ,O000OOOO0OO0O000O :O00O0O00O000OO0OO .sock_message (O0O0OOOO00000O00O ,O000OOOO0OO0O000O ),on_close =lambda OOOO0O0OO000O0O00 ,OO00000OOO00O0O0O ,O0OO00O0000O0O0O0 :O00O0O00O000OO0OO .sock_close (OOOO0O0OO000O0O00 ,OO00000OOO00O0O0O ,O0OO00O0000O0O0O0 ),)#line:794
        O00O0O00O000OO0OO .endScraping =False #line:796
        O00O0O00O000OO0OO .guilds ={}#line:797
        O00O0O00O000OO0OO .members ={}#line:798
        O00O0O00O000OO0OO .ranges =[[0 ,0 ]]#line:799
        O00O0O00O000OO0OO .lastRange =0 #line:800
        O00O0O00O000OO0OO .packets_recv =0 #line:801
    def run (O00O00OOO00OO0O00 ):#line:803
        O00O00OOO00OO0O00 .run_forever ()#line:804
        return O00O00OOO00OO0O00 .members #line:805
    def scrapeUsers (O0OOO00O0OOOOOO00 ):#line:807
        if not O0OOO00O0OOOOOO00 .endScraping :#line:808
            O0OOO00O0OOOOOO00 .send ('{"op":14,"d":{"guild_id":"'+O0OOO00O0OOOOOO00 .guild_id +'","typing":true,"activities":true,"threads":true,"channels":{"'+O0OOO00O0OOOOOO00 .channel_id +'":'+json .dumps (O0OOO00O0OOOOOO00 .ranges )+"}}}")#line:817
    def sock_open (OOO00OO0OO0O0OOO0 ,OO0O00O0OO0O0OO0O ):#line:819
        OOO00OO0OO0O0OOO0 .send ('{"op":2,"d":{"token":"'+OOO00OO0OO0O0OOO0 .token +'","capabilities":125,"properties":{"os":"Windows NT","browser":"Chrome","device":"","system_locale":"it-IT","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36","browser_version":"119.0","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":103981,"client_event_source":null},"presence":{"status":"online","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}')#line:824
    def heartbeatThread (O0OO0O0OOO0O0000O ,OO000O000O00O00OO ):#line:826
        try :#line:827
            while True :#line:828
                O0OO0O0OOO0O0000O .send ('{"op":1,"d":'+str (O0OO0O0OOO0O0000O .packets_recv )+"}")#line:829
                time .sleep (OO000O000O00O00OO )#line:830
        except Exception as O0O00O0O00OOOOOO0 :#line:831
            pass #line:832
    def sock_message (O0OO0O0O0OO0O00OO ,OOO0O00OO00O0O000 ,O00O0OOO00OOOO000 ):#line:834
        O0O0OO00OOO00O0OO =json .loads (O00O0OOO00OOOO000 )#line:835
        if O0O0OO00OOO00O0OO is None :#line:836
            return #line:837
        if O0O0OO00OOO00O0OO ["op"]!=11 :#line:838
            O0OO0O0O0OO0O00OO .packets_recv +=1 #line:839
        if O0O0OO00OOO00O0OO ["op"]==10 :#line:840
            threading .Thread (target =O0OO0O0O0OO0O00OO .heartbeatThread ,args =(O0O0OO00OOO00O0OO ["d"]["heartbeat_interval"]/1000 ,),daemon =True ,).start ()#line:845
        if O0O0OO00OOO00O0OO ["t"]=="READY":#line:846
            for O0OOOO0OOOO0OO00O in O0O0OO00OOO00O0OO ["d"]["guilds"]:#line:847
                O0OO0O0O0OO0O00OO .guilds [O0OOOO0OOOO0OO00O ["id"]]={"member_count":O0OOOO0OOOO0OO00O ["member_count"]}#line:848
        if O0O0OO00OOO00O0OO ["t"]=="READY_SUPPLEMENTAL":#line:849
            O0OO0O0O0OO0O00OO .ranges =Utils .getRanges (0 ,100 ,O0OO0O0O0OO0O00OO .guilds [O0OO0O0O0OO0O00OO .guild_id ]["member_count"])#line:852
            O0OO0O0O0OO0O00OO .scrapeUsers ()#line:853
        elif O0O0OO00OOO00O0OO ["t"]=="GUILD_MEMBER_LIST_UPDATE":#line:854
            O0000OO000OOO0O0O =Utils .parseGuildMemberListUpdate (O0O0OO00OOO00O0OO )#line:855
            if O0000OO000OOO0O0O ["guild_id"]==O0OO0O0O0OO0O00OO .guild_id and ("SYNC"in O0000OO000OOO0O0O ["types"]or "UPDATE"in O0000OO000OOO0O0O ["types"]):#line:859
                for OO0O00OO00OOO0O0O ,O0OO0O0OO00OOO0O0 in enumerate (O0000OO000OOO0O0O ["types"]):#line:860
                    if O0OO0O0OO00OOO0O0 =="SYNC":#line:861
                        if len (O0000OO000OOO0O0O ["updates"][OO0O00OO00OOO0O0O ])==0 :#line:862
                            O0OO0O0O0OO0O00OO .endScraping =True #line:863
                            break #line:864
                        for OOO0O00OOO0O000OO in O0000OO000OOO0O0O ["updates"][OO0O00OO00OOO0O0O ]:#line:866
                            if "member"in OOO0O00OOO0O000OO :#line:867
                                OO00OOOOOOO0OOOO0 =OOO0O00OOO0O000OO ["member"]#line:868
                                O000O0O0OOOOOOO0O ={"tag":OO00OOOOOOO0OOOO0 ["user"]["username"]+"#"+OO00OOOOOOO0OOOO0 ["user"]["discriminator"],"id":OO00OOOOOOO0OOOO0 ["user"]["id"],}#line:874
                                if not OO00OOOOOOO0OOOO0 ["user"].get ("bot"):#line:875
                                    O0OO0O0O0OO0O00OO .members [OO00OOOOOOO0OOOO0 ["user"]["id"]]=O000O0O0OOOOOOO0O #line:876
                    elif O0OO0O0OO00OOO0O0 =="UPDATE":#line:878
                        for OOO0O00OOO0O000OO in O0000OO000OOO0O0O ["updates"][OO0O00OO00OOO0O0O ]:#line:879
                            if "member"in OOO0O00OOO0O000OO :#line:880
                                OO00OOOOOOO0OOOO0 =OOO0O00OOO0O000OO ["member"]#line:881
                                O000O0O0OOOOOOO0O ={"tag":OO00OOOOOOO0OOOO0 ["user"]["username"]+"#"+OO00OOOOOOO0OOOO0 ["user"]["discriminator"],"id":OO00OOOOOOO0OOOO0 ["user"]["id"],}#line:887
                                if not OO00OOOOOOO0OOOO0 ["user"].get ("bot"):#line:888
                                    O0OO0O0O0OO0O00OO .members [OO00OOOOOOO0OOOO0 ["user"]["id"]]=O000O0O0OOOOOOO0O #line:889
                    O0OO0O0O0OO0O00OO .lastRange +=1 #line:891
                    O0OO0O0O0OO0O00OO .ranges =Utils .getRanges (O0OO0O0O0OO0O00OO .lastRange ,100 ,O0OO0O0O0OO0O00OO .guilds [O0OO0O0O0OO0O00OO .guild_id ]["member_count"])#line:894
                    time .sleep (0.45 )#line:895
                    O0OO0O0O0OO0O00OO .scrapeUsers ()#line:896
            if O0OO0O0O0OO0O00OO .endScraping :#line:898
                O0OO0O0O0OO0O00OO .close ()#line:899
    def sock_close (OO0O0O000O0OO00OO ,OOOO0OO0O0OOO0OO0 ,O0000O0O0OOOO0OO0 ,O00OOO000O0OOOOOO ):#line:901
        pass #line:902
def scrape (O0OO000OO000O00O0 ,O0OOO0OOO00O0O000 ,O0O00OOO00000OOO0 ):#line:904
    OO000O000OOOO0O0O =DiscordSocket (O0OO000OO000O00O0 ,O0OOO0OOO00O0O000 ,O0O00OOO00000OOO0 )#line:905
    return OO000O000OOOO0O0O .run ()#line:906
def member_scrape (O00O00000O0OOO000 ,OO0O00O0O0OOO00OO ,OOO0O0O00OO000O0O ):#line:908
    OOOOO0OOO0O0OOOO0 =[]#line:909
    for O0O0OO00OO0000OOO in O00O00000O0OOO000 :#line:910
        O0000OOOO0OOOO000 ={"Authorization":O0O0OO00OO0000OOO ,"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}#line:911
        OOOOOOOOOOO00OO0O =session .get (f"https://canary.discord.com/api/v9/guilds/{OO0O00O0O0OOO00OO}",headers =O0000OOOO0OOOO000 )#line:912
        if OOOOOOOOOOO00OO0O .status_code ==200 :#line:913
            OOOOO0OOO0O0OOOO0 .append (O0O0OO00OO0000OOO )#line:914
            break #line:915
    if not OOOOO0OOO0O0OOOO0 :#line:916
        print ("missing access")#line:917
    O0O0OO00OO0000OOO =random .choice (OOOOO0OOO0O0OOOO0 )#line:919
    OOO00OOOO0O000OO0 =scrape (O0O0OO00OO0000OOO ,OO0O00O0O0OOO00OO ,OOO0O0O00OO000O0O )#line:920
    O00OOOO0000000000 =[f"<@{O0O0O0OO0OO0O0OOO}>"for O0O0O0OO0OO0O0OOO in [int (O00OO0OOOOO00OO0O )for O00OO0OOOOO00OO0O in OOO00OOOO0O000OO0 .keys ()]]#line:921
    print (f"[SUCCESS] {len(O00OOOO0000000000)} scraped members")#line:922
    return O00OOOO0000000000 #line:923
def spammer_menu ():#line:925
    try :#line:926
        with open ("token.txt")as O0000OO000OO0O0OO :#line:927
            O0OOO0O0OO0OOO0OO =[O0O0O00OO00OOOO00 .strip ()for O0O0O00OO00OOOO00 in O0000OO000OO0O0OO .readlines ()if O0O0O00OO00OOOO00 .strip ()]#line:928
    except (FileNotFoundError ,KeyError ):#line:929
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:930
        return #line:931
    OO0OOO0OO000OO0OO =input ("Server ID?: ").strip ()#line:933
    OOO0O0000OOO00O0O =input ("Message?: ").strip ()#line:934
    O0OOO0OO00O00O000 =input ("Random mention (True/False)?: ").strip ().lower ()=='true'#line:935
    OOO0OO0O0O00O0O00 =input ("Delay between messages (in seconds)?: ").strip ()#line:936
    O00OO00O0000O0OOO =input ("Number of messages to send?: ").strip ()#line:937
    O00OO0O0O0OOO0000 =input ("Blacklist User IDs (comma-separated) (Leave blank to skip)?: ").strip ().split (',')#line:938
    O00OO0O0O0OOO0000 =[f"<@{O0O0O00O000OOOO0O.strip()}>"for O0O0O00O000OOOO0O in O00OO0O0O0OOO0000 if O0O0O00O000OOOO0O .strip ()]#line:939
    try :#line:941
        OOO0OO0O0O00O0O00 =float (OOO0OO0O0O00O0O00 )#line:942
        if OOO0OO0O0O00O0O00 <0 :#line:943
            raise ValueError #line:944
    except ValueError :#line:945
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:946
        OOO0OO0O0O00O0O00 =1.0 #line:947
    try :#line:949
        O00OO00O0000O0OOO =int (O00OO00O0000O0OOO )#line:950
        if O00OO00O0000O0OOO <=0 :#line:951
            raise ValueError #line:952
    except ValueError :#line:953
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:954
        O00OO00O0000O0OOO =1 #line:955
    O0OO0OOO0O00OO000 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:957
    if O0OO0OOO0O00OO000 =='2':#line:958
        OOOO000OO0OO00000 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:959
        OOOO000OO0OO00000 =[O0O0OO000OO000OOO .strip ()for O0O0OO000OO000OOO in OOOO000OO0OO00000 if O0O0OO000OO000OOO .strip ()]#line:960
    else :#line:961
        OOOO000OO0OO00000 =fetch_channels (O0OOO0O0OO0OOO0OO [0 ],OO0OOO0OO000OO0OO )#line:962
    O0OO0O000OOO00O00 =None #line:964
    spammer (O0OOO0O0OO0OOO0OO ,OO0OOO0OO000OO0OO ,OOOO000OO0OO00000 ,OOO0O0000OOO00O0O ,O0OOO0OO00O00O000 ,O00OO0O0O0OOO0000 ,O0OO0O000OOO00O00 ,O00OO00O0000O0OOO )#line:966
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:969
def buildnumget (O0O00OOOOO000O000 ):#line:971
  O0OOOO00000O0OOOO =O0O00OOOOO000O000 .get ('https://discord.com/login',headers ={'Accept-Encoding':'gzip, deflate'},timeout =7 )#line:972
  O0000OO0OO00O00OO =O0OOOO00000O0OOOO .text #line:973
import discum #line:975
import random #line:976
import time #line:977
def userget (O0OO000OO0000O00O ,OOOO00OOOOO00O0OO ,OO0000O0O0OOO0O0O ):#line:979
    OO0OOOOOOO0000OOO =[]#line:980
    OO0OO00000O0OO000 =discum .Client (token =O0OO000OO0000O00O ,log =False )#line:981
    def O0O000OO00O0O0OOO (O0OO00O00O00OOOO0 ):#line:983
        if OO0OO00000O0OO000 .gateway .finishedMemberFetching (OOOO00OOOOO00O0OO ):#line:984
            O0OO000OOOOOO0OOO =len (OO0OO00000O0OO000 .gateway .session .guild (OOOO00OOOOO00O0OO ).members )#line:985
            print (str (O0OO000OOOOOO0OOO )+' members fetched')#line:986
            OO0OO00000O0OO000 .gateway .removeCommand ({'function':O0O000OO00O0O0OOO ,'params':{}})#line:987
            OO0OO00000O0OO000 .gateway .close ()#line:988
    def O0OOOO0000OO0O0O0 (OO0OO00000O0000OO ,OOO0OO00O0O000000 ):#line:990
        OO0OO00000O0OO000 .gateway .fetchMembers (OO0OO00000O0000OO ,OOO0OO00O0O000000 ,keep ='all',wait =1 )#line:991
        OO0OO00000O0OO000 .gateway .command ({'function':O0O000OO00O0O0OOO ,'params':{}})#line:992
        OO0OO00000O0OO000 .gateway .run ()#line:993
        OO0OO00000O0OO000 .gateway .resetSession ()#line:994
        return OO0OO00000O0OO000 .gateway .session .guild (OO0OO00000O0000OO ).members #line:995
    O00000000OO00O000 =O0OOOO0000OO0O0O0 (OOOO00OOOOO00O0OO ,OO0000O0O0OOO0O0O )#line:997
    for O000OOO0OOOOO00OO in O00000000OO00O000 :#line:998
        if O000OOO0OOOOO00OO not in OO0OOOOOOO0000OOO :#line:999
            OO0OOOOOOO0000OOO .append (f"<@{O000OOO0OOOOO00OO}>")#line:1000
    return OO0OOOOOOO0000OOO #line:1001
def spammer (OOOOOO000OOOO00OO ,OO0O00OOO0O0O0000 ,O0000OOOO000000O0 ,O00OO000O0OOOO000 ,O0O000O00O000OOOO ,OO00OOO0O0OOOO000 ,O00OO0O0O0O0O0OO0 ,OO0000O0OOO000000 ):#line:1006
    OOO000OOOO0000O0O =get_session (O00OO0O0O0O0O0OO0 )#line:1007
    OOOO0OO0OO0OO0OOO =0 #line:1008
    O0O000000OOOOOO00 =userget (OOOOOO000OOOO00OO [0 ],OO0O00OOO0O0O0000 ,O0000OOOO000000O0 [0 ])#line:1010
    O0O000000OOOOOO00 =[O00OOO0O0O0OO00OO for O00OOO0O0O0OO00OO in O0O000000OOOOOO00 if O00OOO0O0O0OO00OO not in OO00OOO0O0OOOO000 ]#line:1013
    for _O0O0OO000O0OOO00O in range (OO0000O0OOO000000 ):#line:1015
        OOO00O0O0000O0OO0 =OOOOOO000OOOO00OO [OOOO0OO0OO0OO0OOO ]#line:1016
        O0O00O0OOOO0O00O0 =get_headers (OOO00O0O0000O0OO0 )#line:1017
        for O0OOO000OO00O0O0O in O0000OOOO000000O0 :#line:1018
            O00OOOO0OO0OO0OOO =O00OO000O0OOOO000 #line:1019
            if O0O000O00O000OOOO and O0O000000OOOOOO00 :#line:1020
                OO0OOOOOOOO0O0OO0 =random .choice (O0O000000OOOOOO00 )#line:1021
                O00OOOO0OO0OO0OOO +=f" {OO0OOOOOOOO0O0OO0}"#line:1022
            O0OO00O00OO00000O =OOO000OOOO0000O0O .post (f"https://discord.com/api/v9/channels/{O0OOO000OO00O0O0O}/messages",json ={"content":O00OOOO0OO0OO0OOO },headers =O0O00O0OOOO0O00O0 )#line:1024
            if O0OO00O00OO00000O .status_code ==200 :#line:1025
                print (f"200 message sent: {OOO00O0O0000O0OO0}")#line:1026
            elif O0OO00O00OO00000O .status_code ==429 :#line:1027
                print (f"429 rate limit: {OOO00O0O0000O0OO0}")#line:1028
                OOOOO000O0OOOOO0O =O0OO00O00OO00000O .json ().get ("retry_after",1 )#line:1029
                time .sleep (OOOOO000O0OOOOO0O )#line:1030
            elif O0OO00O00OO00000O .status_code ==401 :#line:1031
                print (f"401 unknown token: {OOO00O0O0000O0OO0}")#line:1032
            else :#line:1033
                print (f"error: {OOO00O0O0000O0OO0}")#line:1034
        OOOO0OO0OO0OO0OOO =(OOOO0OO0OO0OO0OOO +1 )%len (OOOOOO000OOOO00OO )#line:1036
        time .sleep (1 )#line:1037
import requests #line:1041
import base64 #line:1042
import colorama #line:1043
import time #line:1044
def add_emojis_from_files ():#line:1046
    try :#line:1047
        with open ("emojiname.txt")as O000OOO0OO0OOO000 ,open ("emojiurl.txt")as OOOO000O000O0OOO0 :#line:1048
            OOOOO00O00000O00O =[O0OO0O000OO000O0O .strip ()for O0OO0O000OO000O0O in O000OOO0OO0OOO000 .read ().split (',')if O0OO0O000OO000O0O .strip ()]#line:1049
            OO000000O00O00O00 =[O0O0000000O0OOO0O .strip ()for O0O0000000O0OOO0O in OOOO000O000O0OOO0 .read ().split (',')if O0O0000000O0OOO0O .strip ()]#line:1050
    except FileNotFoundError as OOOO0O0OOOO0OO00O :#line:1051
        print (f"{colorama.Fore.RED}    [!] Error: {str(OOOO0O0OOOO0OO00O)}{colorama.Fore.RESET}")#line:1052
        return #line:1053
    if len (OOOOO00O00000O00O )!=len (OO000000O00O00O00 ):#line:1055
        print (f"{colorama.Fore.RED}    [!] Error: The number of emoji names and URLs do not match!{colorama.Fore.RESET}")#line:1056
        return #line:1057
    try :#line:1059
        with open ("token.txt")as OOOOO0000000OO00O :#line:1060
            O00OOOOO0O0O0OO0O =[OOO00O0OOOO0O0O0O .strip ()for OOO00O0OOOO0O0O0O in OOOOO0000000OO00O .readlines ()if OOO00O0OOOO0O0O0O .strip ()]#line:1061
    except FileNotFoundError as OOOO0O0OOOO0OO00O :#line:1062
        print (f"{colorama.Fore.RED}    [!] Error: {str(OOOO0O0OOOO0OO00O)}{colorama.Fore.RESET}")#line:1063
        return #line:1064
    OO0OOOOOO00O000OO =input ("Enter the Guild ID: ").strip ()#line:1066
    O0OO0OOO0OO0OO0OO =input ("Enter the rate limit between requests (in seconds): ").strip ()#line:1067
    try :#line:1069
        O0OO0OOO0OO0OO0OO =float (O0OO0OOO0OO0OO0OO )#line:1070
        if O0OO0OOO0OO0OO0OO <0 :#line:1071
            raise ValueError #line:1072
    except ValueError :#line:1073
        print (f"{colorama.Fore.RED}    [!] Invalid rate limit. Using default rate limit of 5 seconds.{colorama.Fore.RESET}")#line:1074
        O0OO0OOO0OO0OO0OO =5.0 #line:1075
    O0O00O0000O0O000O =set ()#line:1077
    for OO00O0000O000OOOO in O00OOOOO0O0O0OO0O :#line:1079
        O000O0O0OO0000OOO ={'Authorization':OO00O0000O000OOOO ,'Content-Type':'application/json'}#line:1083
        OOOOOOO0OO0O00O00 =requests .get (f"https://discord.com/api/v9/guilds/{OO0OOOOOO00O000OO}/emojis",headers =O000O0O0OO0000OOO )#line:1086
        if OOOOOOO0OO0O00O00 .status_code ==200 :#line:1087
            OOOO000OOO0OO0OOO =OOOOOOO0OO0O00O00 .json ()#line:1088
            for OOO0O0000O00O0O00 in OOOO000OOO0OO0OOO :#line:1089
                O0O00O0000O0O000O .add (OOO0O0000O00O0O00 ['name'])#line:1090
        else :#line:1091
            print (f"{colorama.Fore.RED}    [!] Error fetching existing emojis: {OOOOOOO0OO0O00O00.status_code} - {OOOOOOO0OO0O00O00.text}{colorama.Fore.RESET}")#line:1092
            continue #line:1093
    for O0O00OO00OO00O0O0 ,OO00OO0O0O0OOOOO0 in zip (OOOOO00O00000O00O ,OO000000O00O00O00 ):#line:1095
        if O0O00OO00OO00O0O0 in O0O00O0000O0O000O :#line:1096
            print (f"{colorama.Fore.YELLOW}    [*] Emoji '{O0O00OO00OO00O0O0}' already exists. Skipping...{colorama.Fore.RESET}")#line:1097
            continue #line:1098
        for OO00O0000O000OOOO in O00OOOOO0O0O0OO0O :#line:1100
            try :#line:1101
                OOOOOOO0OO0O00O00 =requests .get (OO00OO0O0O0OOOOO0 )#line:1102
                OOOOOOO0OO0O00O00 .raise_for_status ()#line:1103
                O00OO0OOOO0O000O0 =OOOOOOO0OO0O00O00 .content #line:1104
                O0OO0O0O0O00OOO00 =base64 .b64encode (O00OO0OOOO0O000O0 ).decode ('utf-8')#line:1105
                O00O0OOOO0O000OOO ={'name':O0O00OO00OO00O0O0 ,'image':f"data:image/png;base64,{O0OO0O0O0O00OOO00}"}#line:1110
                O000O0O0OO0000OOO ={'Authorization':OO00O0000O000OOOO ,'Content-Type':'application/json'}#line:1115
                O0O0O0O0OO000O00O =requests .post (f"https://discord.com/api/v9/guilds/{OO0OOOOOO00O000OO}/emojis",headers =O000O0O0OO0000OOO ,json =O00O0OOOO0O000OOO )#line:1117
                if O0O0O0O0OO000O00O .status_code ==201 :#line:1118
                    print (f"{colorama.Fore.GREEN}    [+] Successfully added emoji '{O0O00OO00OO00O0O0}' with token {OO00O0000O000OOOO}{colorama.Fore.RESET}")#line:1119
                    O0O00O0000O0O000O .add (O0O00OO00OO00O0O0 )#line:1120
                    break #line:1121
                else :#line:1122
                    print (f"{colorama.Fore.RED}    [!] Failed to add emoji '{O0O00OO00OO00O0O0}' with token {OO00O0000O000OOOO}: {O0O0O0O0OO000O00O.status_code} - {O0O0O0O0OO000O00O.text}{colorama.Fore.RESET}")#line:1123
                time .sleep (O0OO0OOO0OO0OO0OO )#line:1125
            except Exception as OOOO0O0OOOO0OO00O :#line:1126
                print (f"{colorama.Fore.RED}    [!] Error adding emoji '{O0O00OO00OO00O0O0}' with token {OO00O0000O000OOOO}: {str(OOOO0O0OOOO0OO00O)}{colorama.Fore.RESET}")#line:1127
import random #line:1129
import requests #line:1130
import time #line:1131
def pollspammer (OO00OOO00000O000O ,O0OOOOOO00O00OO0O ,O00O0O000O0O00O00 ,OOOOOO0O0O0OOO000 ,O0OOO0OOO0OOOOOOO ,O000OO0O00O0O0000 ,O00000O000OOO0OO0 ,OO0OOOOO0OO0O0000 ,O0O00O0OOO0OOOOO0 ,OO00OO000000OOO0O ,OO0O000O0O0000OO0 ):#line:1133
    O0O0O00OO0OO00O0O =get_session ()#line:1134
    OO0O00OO0OOOO00OO =0 #line:1135
    O00OOOO0O0OO00000 =userget (OO00OOO00000O000O [0 ],O0OOOOOO00O00OO0O ,O00O0O000O0O00O00 [0 ])#line:1137
    O00OOOO0O0OO00000 =[O0OOOOO0OO000OOOO for O0OOOOO0OO000OOOO in O00OOOO0O0OO00000 if O0OOOOO0OO000OOOO not in O0O00O0OOO0OOOOO0 ]#line:1140
    for _OOOO0O00O0O00OO0O in range (OO00OO000000OOO0O ):#line:1142
        OO000OO00OO000000 =OO00OOO00000O000O [OO0O00OO0OOOO00OO ]#line:1143
        OOOOO0OO00000O0O0 =get_headers (OO000OO00OO000000 )#line:1144
        for OO0OO0O0OO0O0OOOO in O00O0O000O0O00O00 :#line:1149
            O00OO0OO0OOOO0OO0 =[{"poll_media":{"text":OOOOO0O00OOOO0OO0 .strip ()}}for OOOOO0O00OOOO0OO0 in O0OOO0OOO0OOOOOOO .split (',')]#line:1150
            OO0OOO0OO0OO00O00 ={"mobile_network_type":"unknown","content":"","nonce":str (random .randint (10 **17 ,10 **18 -1 )),"tts":False ,"flags":0 ,"poll":{"question":{"text":OOOOOO0O0O0OOO000 },"answers":O00OO0OO0OOOO0OO0 ,"allow_multiselect":False ,"duration":O000OO0O00O0O0000 ,"layout_type":1 }}#line:1164
            if O00000O000OOO0OO0 and O00OOOO0O0OO00000 :#line:1166
                OO00O0000O0OOO0O0 =random .choice (O00OOOO0O0OO00000 )#line:1168
                OO00O0OO00O000O0O ={"content":f"{OO0OOOOO0OO0O0000} {OO00O0000O0OOO0O0}","tts":False ,"nonce":str (random .randint (10 **17 ,10 **18 -1 ))}#line:1173
                OO0000000OO00O0OO =O0O0O00OO0OO00O0O .post (f"https://discord.com/api/v9/channels/{OO0OO0O0OO0O0OOOO}/messages",json =OO00O0OO00O000O0O ,headers =OOOOO0OO00000O0O0 )#line:1174
                if OO0000000OO00O0OO .status_code !=200 :#line:1175
                    print (f"Failed to send mention: {OO0000000OO00O0OO.status_code} - {OO0000000OO00O0OO.text}")#line:1176
            OOOOOO0O0O0OOOO0O =O0O0O00OO0OO00O0O .post (f"https://discord.com/api/v9/channels/{OO0OO0O0OO0O0OOOO}/messages",json =OO0OOO0OO0OO00O00 ,headers =OOOOO0OO00000O0O0 )#line:1178
            if OOOOOO0O0O0OOOO0O .status_code ==200 :#line:1179
                print (f"200 poll message sent: {OO000OO00OO000000}")#line:1180
            elif OOOOOO0O0O0OOOO0O .status_code ==429 :#line:1181
                print (f"429 rate limit: {OO000OO00OO000000}")#line:1182
                OOO0000O0OOO00O00 =OOOOOO0O0O0OOOO0O .json ().get ("retry_after",1 )#line:1183
                time .sleep (OOO0000O0OOO00O00 )#line:1184
            elif OOOOOO0O0O0OOOO0O .status_code ==401 :#line:1185
                print (f"401 unknown token: {OO000OO00OO000000}")#line:1186
            else :#line:1187
                print (f"error: {OO000OO00OO000000} - {OOOOOO0O0O0OOOO0O.status_code}: {OOOOOO0O0O0OOOO0O.text}")#line:1188
        OO0O00OO0OOOO00OO =(OO0O00OO0OOOO00OO +1 )%len (OO00OOO00000O000O )#line:1190
        time .sleep (OO0O000O0O0000OO0 )#line:1191
def pollspammermenu ():#line:1194
    with open ("token.txt")as O0O00OOOO0OO000O0 :#line:1195
        OO0O0OOO000OO0OO0 =[OO0O0OO0O0OOOO000 .strip ()for OO0O0OO0O0OOOO000 in O0O00OOOO0OO000O0 .readlines ()if OO0O0OO0O0OOOO000 .strip ()]#line:1196
    O00O000O00O0O0000 =input ("Enter Server ID: ").strip ()#line:1198
    OO0OOOO0O0OOOOO0O =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:1199
    if OO0OOOO0O0OOOOO0O =='2':#line:1200
        OO0OOO00O00O0O000 =input ("Enter Channel IDs (comma-separated): ").strip ().split (',')#line:1201
    else :#line:1202
        OO0OOO00O00O0O000 =[]#line:1203
        for O0OOOOO000O0O000O in OO0O0OOO000OO0OO0 :#line:1204
            try :#line:1205
                OO0OOO00O00O0O000 .extend (fetch_channels (O0OOOOO000O0O000O ,O00O000O00O0O0000 ))#line:1206
            except Exception as O0O00O00O0OOOOOOO :#line:1207
                print (f"[!] Failed to fetch channels for token. Error: {O0O00O00O0OOOOOOO}")#line:1208
                continue #line:1209
        random .shuffle (OO0OOO00O00O0O000 )#line:1210
    O00O0O0O00O0O0OO0 =input ("Enter poll title: ").strip ()#line:1212
    OOOOOO000OOO0O0OO =input ("Enter poll answers (comma-separated): ").strip ()#line:1213
    O0OO0OO00OOO0OOOO =int (input ("Enter poll duration (in hours 1/4/8/24/72/168/336 ): ").strip ())#line:1214
    OO000OOO0OO0000O0 =input ("Do you want to mention random users? (true/false): ").strip ().lower ()=='true'#line:1215
    OOO0OO0O0OOO0O000 =""#line:1216
    if OO000OOO0OO0000O0 :#line:1217
        OOO0OO0O0OOO0O000 =input ("Enter the message to prepend to the mention: ").strip ()#line:1218
    O00O0O0OO0OOOOO00 =input ("Enter blacklist user IDs (comma-separated): ").strip ().split (',')#line:1219
    O00O0O00000OO0O00 =int (input ("Enter number of send poll: ").strip ())#line:1220
    O00O000000OOO0000 =float (input ("Enter delay between posts (in seconds): ").strip ())#line:1221
    pollspammer (OO0O0OOO000OO0OO0 ,O00O000O00O0O0000 ,OO0OOO00O00O0O000 ,O00O0O0O00O0O0OO0 ,OOOOOO000OOO0O0OO ,O0OO0OO00OOO0OOOO ,OO000OOO0OO0000O0 ,OOO0OO0O0OOO0O000 ,O00O0O0OO0OOOOO00 ,O00O0O00000OO0O00 ,O00O000000OOO0000 )#line:1223
def main ():#line:1226
    colorama .init ()#line:1227
    while True :#line:1228
        logo ()#line:1229
        OO0O0OO0O0O0000OO =input (f"{colorama.Fore.LIGHTMAGENTA_EX}    [Final] Select an option from above: ")#line:1230
        if OO0O0OO0O0O0000OO =="0":#line:1232
            update_group_ids ()#line:1233
        elif OO0O0OO0O0O0000OO =="1":#line:1234
            join_discord_invite ()#line:1235
        elif OO0O0OO0O0O0000OO =="2":#line:1236
            reaction_spammer ()#line:1237
        elif OO0O0OO0O0O0000OO =="3":#line:1238
            send_messages_with_mentions ()#line:1239
        elif OO0O0OO0O0O0000OO =="4":#line:1240
            spammer_menu ()#line:1241
        elif OO0O0OO0O0O0000OO =="5":#line:1242
            nickchanger ()#line:1243
        elif OO0O0OO0O0O0000OO =="6":#line:1244
            add_emojis_from_files ()#line:1245
        elif OO0O0OO0O0O0000OO =="7":#line:1246
            reaction_art ()#line:1247
        elif OO0O0OO0O0O0000OO =="8":#line:1248
            pollspammermenu ()#line:1249
        elif OO0O0OO0O0O0000OO =="0":#line:1250
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [*] Exiting the application. Goodbye!{colorama.Fore.RESET}")#line:1251
            break #line:1252
        else :#line:1253
            print (f"{colorama.Fore.RED}    [!] Invalid option selected!{colorama.Fore.RESET}")#line:1254
        input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:1256
if __name__ =="__main__":#line:1258
    main ()#line:1259
