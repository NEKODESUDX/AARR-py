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

    [0] exit
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    {colorama.Fore.RESET}
    """)#line:51
def get_session (proxy =None ):#line:54
    O0OO00OOO0000OOO0 =requests .Session ()#line:55
    if proxy :#line:56
        O0OO00OOO0000OOO0 .proxies ={"http":proxy ,"https":proxy }#line:57
    return O0OO00OOO0000OOO0 #line:58
def get_headers (O0O00O00O000000O0 ):#line:60
    return {"Authorization":O0O00O00O000000O0 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:65
def send_message_with_mention (OOO00O0000OOOOOOO ,O0O0O0OOO00OOO0OO ,OO0O0OO00O0000OO0 ,O00OOOOOO0O00OOOO ):#line:68
    OO0O000OOO00O000O =get_session ()#line:69
    O0000OO0OO0O00O00 =get_headers (OOO00O0000OOOOOOO )#line:70
    if O00OOOOOO0O00OOOO :#line:72
        OOOO0O000O00OO000 =random .choice (O00OOOOOO0O00OOOO )#line:73
        OO0O0OO00O0000OO0 +=f" <@{OOOO0O000O00OO000}>"#line:74
    O00OO00OOOOOOOOOO =OO0O000OOO00O000O .post (f"https://discord.com/api/v9/channels/{O0O0O0OOO00OOO0OO}/messages",headers =O0000OO0OO0O00O00 ,json ={"content":OO0O0OO00O0000OO0 })#line:80
    if O00OO00OOOOOOOOOO .status_code in [200 ,201 ]:#line:81
        print (f"[+] Message sent to channel {O0O0O0OOO00OOO0OO}")#line:82
    elif O00OO00OOOOOOOOOO .status_code ==429 :#line:83
        print ("[-] Rate limited. Please wait before retrying.")#line:84
        O0OO0000OOO00OOOO =O00OO00OOOOOOOOOO .json ().get ("retry_after",1 )#line:85
        time .sleep (O0OO0000OOO00OOOO )#line:86
    else :#line:87
        print (f"[!] Error occurred: {O00OO00OOOOOOOOOO.status_code}")#line:88
def fetch_messages (O000000O0OO0OOOO0 ,OOOO00000OOOO00OO ,limit =100 ):#line:91
    OOOO0O00O000O00O0 ={"Authorization":O000000O0OO0OOOO0 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:96
    O0OO0O0OOO000OO0O =requests .get (f"https://discord.com/api/v9/channels/{OOOO00000OOOO00OO}/messages?limit={limit}",headers =OOOO0O00O000O00O0 )#line:100
    if O0OO0O0OOO000OO0O .status_code ==200 :#line:101
        return O0OO0O0OOO000OO0O .json ()#line:102
    else :#line:103
        print (f"[!] Failed to fetch messages. HTTP Status Code: {O0OO0O0OOO000OO0O.status_code}")#line:104
        return []#line:105
import concurrent .futures #line:106
def reaction_spammer ():#line:108
    try :#line:109
        with open ("token.txt")as O0OOOOOOOOOOO0OOO :#line:110
            O0O0000OOO0O000O0 =[OO000OOO0OO00O00O .strip ()for OO000OOO0OO00O00O in O0OOOOOOOOOOO0OOO .readlines ()if OO000OOO0OO00O00O .strip ()]#line:111
    except (FileNotFoundError ,KeyError ):#line:112
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:113
        return #line:114
    OOO0O0000OOO00000 =input ("Server ID?: ").strip ()#line:116
    OO0OOO0O0000O00O0 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:118
    if OO0OOO0O0000O00O0 =='2':#line:119
        OOOO000O0OOOOOOOO =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:120
        OOOO000O0OOOOO000 =[O0O0O0O00OOOO00OO .strip ()for O0O0O0O00OOOO00OO in OOOO000O0OOOOOOOO if O0O0O0O00OOOO00OO .strip ()]#line:121
    else :#line:122
        OOOO000O0OOOOO000 =[]#line:123
        for O000O0OOO000OO0OO in O0O0000OOO0O000O0 :#line:124
            try :#line:125
                OOOO000O0OOOOO000 .extend (fetch_channels (O000O0OOO000OO0OO ,OOO0O0000OOO00000 ))#line:126
            except Exception as O00OO00OOOOO0OO00 :#line:127
                print (f"[!] Failed to fetch channels for token. Error: {O00OO00OOOOO0OO00}")#line:128
                continue #line:129
    O00000OOOOO000000 =input ("Select your emoji (a, b, c, ... or custom emojis): ").strip ()#line:131
    O0OO0O0O00000OOOO =input ("Delay between reactions (in seconds)?: ").strip ()#line:132
    try :#line:134
        O0OO0O0O00000OOOO =float (O0OO0O0O00000OOOO )#line:135
        if O0OO0O0O00000OOOO <0 :#line:136
            raise ValueError #line:137
    except ValueError :#line:138
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:139
        O0OO0O0O00000OOOO =1.0 #line:140
    OOO0OOOO0OOO0OOOO =[]#line:142
    for OOOOOO00OO0O00O00 in O00000OOOOO000000 .split (","):#line:143
        OOOOOO00OO0O00O00 =OOOOOO00OO0O00O00 .strip ().lower ()#line:144
        if OOOOOO00OO0O00O00 in alphabet_to_flag :#line:145
            OOO0OOOO0OOO0OOOO .append (alphabet_to_flag [OOOOOO00OO0O00O00 ])#line:146
        else :#line:147
            OOO0OOOO0OOO0OOOO .append (OOOOOO00OO0O00O00 )#line:148
    if not OOO0OOOO0OOO0OOOO :#line:150
        print (f"{colorama.Fore.RED}    [!] No valid emojis provided!{colorama.Fore.RESET}")#line:151
        return #line:152
    def O0OO0OO0000OOO000 (OO0O0OO0OOOO0OO00 ):#line:154
        for OO00O0O000O000O0O in OOOO000O0OOOOO000 :#line:155
            try :#line:156
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {OO00O0O000O000O0O}...{colorama.Fore.RESET}")#line:157
                OOO00O0O000OOOOO0 =fetch_messages (OO0O0OO0OOOO0OO00 ,OO00O0O000O000O0O ,limit =100 )#line:158
                if not OOO00O0O000OOOOO0 :#line:159
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:160
                    continue #line:161
                for OO0O00OOO0O00O0OO in OOO00O0O000OOOOO0 :#line:163
                    for OO00O00OO000O00OO in OOO0OOOO0OOO0OOOO :#line:164
                        reactionput (OO0O0OO0OOOO0OO00 ,OO00O0O000O000O0O ,OO0O00OOO0O00O0OO ['id'],OO00O00OO000O00OO )#line:165
                        time .sleep (O0OO0O0O00000OOOO )#line:166
            except Exception as O00O0OOOO00O0OO0O :#line:167
                print (f"[!] Error processing channel {OO00O0O000O000O0O}. Error: {O00O0OOOO00O0OO0O}")#line:168
                continue #line:169
    with concurrent .futures .ThreadPoolExecutor ()as OOO0OO0O0O000OO00 :#line:171
        OO000O00O000OOO0O =[OOO0OO0O0O000OO00 .submit (O0OO0OO0000OOO000 ,O0OOOOO0O00O00O00 )for O0OOOOO0O00O00O00 in O0O0000OOO0O000O0 ]#line:172
        concurrent .futures .wait (OO000O00O000OOO0O )#line:173
def update_group_ids ():#line:176
    try :#line:177
        with open ("token.txt")as OO0OOOOOO0OOO0O00 :#line:178
            OOOO0OO0OOO00O0O0 =[OOO00O000000O0O0O .strip ()for OOO00O000000O0O0O in OO0OOOOOO0OOO0O00 .readlines ()if OOO00O000000O0O0O .strip ()]#line:179
        O0O0OOO0OOO0O0O0O =OOOO0OO0OOO00O0O0 [0 ]#line:180
    except (FileNotFoundError ,KeyError ):#line:181
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:182
        return #line:183
    OOO0O00O00O000000 ={"Authorization":O0O0OOO0OOO0O0O0O ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:189
    O000OO0000000000O =requests .get ('https://discord.com/api/v9/users/@me/channels',headers =OOO0O00O00O000000 )#line:191
    if O000OO0000000000O .status_code ==200 :#line:192
        OOOOOO00000OO00O0 =O000OO0000000000O .json ()#line:193
        with open ("group_id.txt","w")as OO00000OOO000O0O0 :#line:194
            for O0OO0O0OOO0O0OO00 in OOOOOO00000OO00O0 :#line:195
                if O0OO0O0OOO0O0OO00 ['type']==3 :#line:196
                    OO00000OOO000O0O0 .write (O0OO0O0OOO0O0OO00 ['id']+'\n')#line:197
        print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Group IDs updated successfully.{colorama.Fore.RESET}")#line:198
    else :#line:199
        print (f"{colorama.Fore.LIGHTRED_EX}    [!] Failed to retrieve group IDs. HTTP Status Code: {O000OO0000000000O.status_code}{colorama.Fore.RESET}")#line:200
import requests #line:202
import requests #line:204
def fetch_channels (O0O0O0000OO000O00 ,O000000O0OOO0O00O ):#line:206
    try :#line:207
        OOO0O000OO0O000OO =requests .Session ()#line:208
        OO00OOOO0OO00OO0O =get_headers (O0O0O0000OO000O00 )#line:209
        OOOO000OOOOOOOO0O =OOO0O000OO0O000OO .get (f"https://discord.com/api/v9/guilds/{O000000O0OOO0O00O}/channels",headers =OO00OOOO0OO00OO0O ,timeout =10 )#line:216
        if OOOO000OOOOOOOO0O .status_code ==200 :#line:219
            try :#line:220
                O0OO0O0O00O00O00O =OOOO000OOOOOOOO0O .json ()#line:221
                return [OOO0OO0000OOO00OO ['id']for OOO0OO0000OOO00OO in O0OO0O0O00O00O00O if OOO0OO0000OOO00OO .get ('type')==0 ]#line:222
            except ValueError :#line:223
                print ("[!] Error: Response was not valid JSON.")#line:224
                return []#line:225
        elif OOOO000OOOOOOOO0O .status_code ==401 :#line:226
            print ("[!] Error: Unauthorized - check your token.")#line:227
        elif OOOO000OOOOOOOO0O .status_code ==403 :#line:228
            print ("[!] Error: Forbidden - you lack permissions.")#line:229
        elif OOOO000OOOOOOOO0O .status_code ==404 :#line:230
            print ("[!] Error: Server not found - check the server ID.")#line:231
        else :#line:232
            print (f"[!] Error: Unexpected status code {OOOO000OOOOOOOO0O.status_code}.")#line:233
        return []#line:236
    except requests .exceptions .Timeout :#line:238
        print ("[!] Error: Request timed out. Check your connection or try again later.")#line:239
        return []#line:240
    except requests .exceptions .RequestException as OO000O00O0O00O00O :#line:241
        print (f"[!] Error: An error occurred while fetching channels: {OO000O00O0O00O00O}")#line:242
        return []#line:243
def extract_uids_from_messages (OO00O0OOOO0OO0OO0 ):#line:249
    OOO00OOOO0O0O0OO0 =set ()#line:250
    for O0OOO00O0O0O0O00O in OO00O0OOOO0OO0OO0 :#line:251
        OOO00OOOO0O0O0OO0 .add (O0OOO00O0O0O0O00O ['author']['id'])#line:252
    return list (OOO00OOOO0O0O0OO0 )#line:253
def send_message_with_mention (O0OOOOOOOOO0OO00O ,OO00OO0OOOO000000 ,OOOO0O0O00OO00000 ,O0OOO00O00OO0OOO0 ):#line:255
    OO000O0O00OO0O0OO =get_session ()#line:256
    OO000O0OO00O0OO0O =get_headers (O0OOOOOOOOO0OO00O )#line:257
    if O0OOO00O00OO0OOO0 :#line:259
        O00000O0O0O000OO0 =random .choice (O0OOO00O00OO0OOO0 )#line:260
        OOOO0O0O00OO00000 +=f" <@{O00000O0O0O000OO0}>"#line:261
    O0O0OO0O00OO00OOO =OO000O0O00OO0O0OO .post (f"https://discord.com/api/v9/channels/{OO00OO0OOOO000000}/messages",headers =OO000O0OO00O0OO0O ,json ={"content":OOOO0O0O00OO00000 })#line:267
    if O0O0OO0O00OO00OOO .status_code in [200 ,201 ]:#line:268
        print (f"[+] Message sent to channel {OO00OO0OOOO000000}")#line:269
    elif O0O0OO0O00OO00OOO .status_code ==429 :#line:270
        print ("[-] Rate limited. Please wait before retrying.")#line:271
        O0000000O000OOO00 =O0O0OO0O00OO00OOO .json ().get ("retry_after",1 )#line:272
        time .sleep (O0000000O000OOO00 )#line:273
    else :#line:274
        print (f"[!] Error occurred: {O0O0OO0O00OO00OOO.status_code}")#line:275
def send_messages_with_mentions ():#line:276
    try :#line:277
        with open ("token.txt")as O00O0O0OOOO00000O :#line:278
            OOOOO0OO000000000 =[O000OOO00O0O0000O .strip ()for O000OOO00O0O0000O in O00O0O0OOOO00000O .readlines ()if O000OOO00O0O0000O .strip ()]#line:279
    except (FileNotFoundError ,KeyError ):#line:280
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:281
        return #line:282
    O0OO0OOO000000000 =input ("Server ID?: ").strip ()#line:284
    OOOO0OOOOOO0OO000 =input ("Delay between messages (in seconds)?: ").strip ()#line:285
    O0O00O0OO0OO00O0O =input ("Number of messages to send?: ").strip ()#line:286
    OO00O0O00OOO00000 =input ("Message content?: ").strip ()#line:287
    OOOO0O0O00OOOO000 =input ("Blacklist User IDs (comma-separated)?: ").strip ().split (',')#line:288
    OOOO0O0O00OOOO000 =[OO000OO0OO00000OO .strip ()for OO000OO0OO00000OO in OOOO0O0O00OOOO000 if OO000OO0OO00000OO .strip ()]#line:289
    try :#line:291
        OOOO0OOOOOO0OO000 =float (OOOO0OOOOOO0OO000 )#line:292
        if OOOO0OOOOOO0OO000 <0 :#line:293
            raise ValueError #line:294
    except ValueError :#line:295
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:296
        OOOO0OOOOOO0OO000 =1.0 #line:297
    try :#line:299
        O0O00O0OO0OO00O0O =int (O0O00O0OO0OO00O0O )#line:300
        if O0O00O0OO0OO00O0O <=0 :#line:301
            raise ValueError #line:302
    except ValueError :#line:303
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:304
        O0O00O0OO0OO00O0O =1 #line:305
    OO0OO0O0OOO00OOO0 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:307
    if OO0OO0O0OOO00OOO0 =='2':#line:308
        OO0OOO0000OO00OOO =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:309
        OO0OOO0000OO00OOO =[O000OO0O000OO0000 .strip ()for O000OO0O000OO0000 in OO0OOO0000OO00OOO if O000OO0O000OO0000 .strip ()]#line:310
    else :#line:311
        OO0OOO0000OO00OOO =[]#line:312
    OO00O0O0000O0OOOO =set ()#line:314
    for O00O0O0000OO0O00O in OOOOO0OO000000000 :#line:315
        OOO0000O0000O000O =fetch_channels (O00O0O0000OO0O00O ,O0OO0OOO000000000 )#line:316
        for O0O00O00000OO0O00 in OOO0000O0000O000O :#line:317
            O000OOO0O000OO0O0 =fetch_messages (O00O0O0000OO0O00O ,O0O00O00000OO0O00 ,limit =100 )#line:318
            OOOOOO00O0OOO0OO0 =extract_uids_from_messages (O000OOO0O000OO0O0 )#line:319
            OO00O0O0000O0OOOO .update (OOOOOO00O0OOO0OO0 )#line:320
    OO00O0O0000O0OOOO =list (set (OO00O0O0000O0OOOO )-set (OOOO0O0O00OOOO000 ))#line:323
    for _O0OO0OOO00OO0OOOO in range (O0O00O0OO0OO00O0O ):#line:325
        for O00O0O0000OO0O00O in OOOOO0OO000000000 :#line:326
            if OO0OOO0000OO00OOO :#line:327
                OOO0000O0000O000O =OO0OOO0000OO00OOO #line:328
            for O0O00O00000OO0O00 in OOO0000O0000O000O :#line:329
                send_message_with_mention (O00O0O0000OO0O00O ,O0O00O00000OO0O00 ,OO00O0O00OOO00000 ,OO00O0O0000O0OOOO )#line:330
                time .sleep (OOOO0OOOOOO0OO000 )#line:331
def join_discord_invite ():#line:336
    try :#line:337
        with open ("token.txt")as OO00OOOO00OO0O0O0 :#line:338
            OO0O00OOOO0OOO0O0 =[O000000OO00OOOO00 .strip ()for O000000OO00OOOO00 in OO00OOOO00OO0O0O0 .readlines ()if O000000OO00OOOO00 .strip ()]#line:339
    except (FileNotFoundError ,KeyError ):#line:340
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:341
        return #line:342
    OO0OO00O0OO00OO00 =input ("Invite Code?: discord.gg/").strip ()#line:344
    for OO0OOO0OO000O000O in OO0O00OOOO0OOO0O0 :#line:347
        joiner (OO0OOO0OO000O000O ,OO0OO00O0OO00OO00 )#line:348
import json ,time ,base64 ,random ,requests #line:350
def cookieset (O00OOOO00O0O00000 ):#line:352
    OOOOO0OOO00O000OO =O00OOOO00O0O00000 .get ("https://discord.com/app")#line:353
    return OOOOO0OOO00O000OO .cookies .get_dict ()#line:354
def generatexspandua (OOOO000OOOOO0OOOO ):#line:356
    OO00000OOOOO0O0OO =["Android","Windows","Macintosh"]#line:357
    OO0O00O0OO0OOOO00 =random .choice (OO00000OOOOO0O0OO )#line:358
    if OO0O00O0OO0OOOO00 =="Macintosh":#line:359
        O00OO0OO0OO000O00 =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:360
        OO0O0O0OO00OOOO0O ="Macintosh; Intel Mac OS X "+O00OO0OO0OO000O00 #line:361
        O0OO0OO0OO0O000OO ="x86_64"#line:362
    elif OO0O00O0OO0OOOO00 =="Windows":#line:363
        O00OO0OO0OO000O00 =f'{random.choice([6.0, 10.0, 11.0])}'#line:364
        OO0O0O0OO00OOOO0O ="Windows NT "+O00OO0OO0OO000O00 +" Win64; x64"#line:365
        O0OO0OO0OO0O000OO ="x86_64"#line:366
    else :#line:367
        O00OO0OO0OO000O00 ="13"#line:368
        OO0O0O0OO00OOOO0O =f"Linux; Android 13; Pixel 6a"#line:369
        O0OO0OO0OO0O000OO ="aarch64"#line:370
    OO00OOO0O0O000000 ={"os":OO0O00O0OO0OOOO00 ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":O00OO0OO0OO000O00 ,"os_arch":O0OO0OO0OO0O000OO ,"system_locale":"ja-JP","client_build_number":OOOO000OOOOO0OOOO ,"client_event_source":None ,"design_id":0 }#line:383
    OO0O000OO0OOOO0O0 =f"Mozilla/5.0 ({OO0O0O0OO00OOOO0O}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:384
    return base64 .b64encode (json .dumps (OO00OOO0O0O000000 ,separators =(',',':')).encode ()).decode (),OO0O000OO0OOOO0O0 #line:385
def joiner (O0OOO000000O00OO0 ,OO0OO00O000O00OOO ,OO0O0OOO0OO00O0OO ):#line:387
    OOO0OOO0O0OO0OO00 =cookieset (OO0O0OOO0OO00O0OO )#line:388
    OOO0OOO0O0OO0OO00 ["locale"]="ja-JP"#line:389
    O00OOO0O0OOO0O0O0 =201211 #line:390
    O00OO0O0OO00OO0OO ,OO00O0OO00000O0O0 =generatexspandua (O00OOO0O0OOO0O0O0 )#line:391
    OOOO00O00OO00OO0O ={"Authorization":O0OOO000000O00OO0 ,"accept":"*/*","accept-language":"ja-JP","connection":"keep-alive","DNT":"1","origin":"https://discord.com","sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","referer":"https://discord.com/channels/@me","TE":"Trailers","user-agent":OO00O0OO00000O0O0 ,"X-Super-Properties":O00OO0O0OO00OO0OO ,}#line:406
    O00000O0O0OO0OO0O =OO0O0OOO0OO00O0OO .post ("https://discord.com/api/v9/invites/"+OO0OO00O000O00OOO ,headers =OOOO00O00OO00OO0O ,json ={},cookies =OOO0OOO0O0OO0OO00 )#line:407
    if O00000O0O0OO0OO0O .status_code ==200 :#line:408
        print ("[+] join this server "+O0OOO000000O00OO0 )#line:409
        if "show_verification_form"in O00000O0O0OO0OO0O .json ():#line:410
            bypass (O0OOO000000O00OO0 ,O00000O0O0OO0OO0O .json ()["guild"]["id"],OO0O0OOO0OO00O0OO ,OOOO00O00OO00OO0O )#line:411
        return #line:412
    elif "captcha_key"in O00000O0O0OO0OO0O .text and O00000O0O0OO0OO0O .status_code ==400 :#line:413
        print ("[!] Hcaptcha protect"+O0OOO000000O00OO0 )#line:414
        return #line:415
    elif O00000O0O0OO0OO0O .status_code ==401 :#line:416
        print ("[×] token is dead"+O0OOO000000O00OO0 )#line:417
        return #line:418
    elif O00000O0O0OO0OO0O .status_code ==403 :#line:419
        print ("[!] 403 banned "+O0OOO000000O00OO0 )#line:420
        return #line:421
    elif O00000O0O0OO0OO0O .status_code ==429 :#line:422
        O000OO0O0O00OOOOO =O00000O0O0OO0OO0O .json ().get ("retry_after",1 )#line:423
        print (f"[!] 429 rate limit. Retrying after {O000OO0O0O00OOOOO} seconds.")#line:424
        time .sleep (O000OO0O0O00OOOOO )#line:425
        return #line:426
    else :#line:427
        print ("[!] error "+O0OOO000000O00OO0 )#line:428
        return #line:429
def update_group_ids ():#line:431
    OO000OO0OO0O0000O =input ("Invite Code?: ").strip ()#line:432
    try :#line:433
        with open ("token.txt")as OO0O0O00OO0OO0O00 :#line:434
            OOO00OO0OOOOOOO0O =[OO0OOOO000OOOO0O0 .strip ()for OO0OOOO000OOOO0O0 in OO0O0O00OO0OO0O00 .readlines ()if OO0OOOO000OOOO0O0 .strip ()]#line:435
    except (FileNotFoundError ,KeyError ):#line:436
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:437
        return #line:438
    O00OO00OOO00OO0OO =requests .Session ()#line:440
    for O000O00OOO0O0OOOO in OOO00OO0OOOOOOO0O :#line:441
        joiner (O000O00OOO0O0OOOO ,OO000OO0OO0O0000O ,O00OO00OOO00OO0OO )#line:442
        time .sleep (2 )#line:443
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:445
def bypass (O0O00OO0000OOO0O0 ,OO000OOO0000000O0 ,OOO000O0OOO0O0000 ,O000OO00O0O0O00O0 ):#line:448
    try :#line:449
        OO000O0O00OOOOO00 =OOO000O0OOO0O0000 .get (f"https://discord.com/api/v9/guilds/{OO000OOO0000000O0}/member-verification?with_guild=false",headers =O000OO00O0O0O00O0 ).json ()#line:450
        OOO0O0OOO0OOO0OOO =OOO000O0OOO0O0000 .put (f"https://discord.com/api/v9/guilds/{OO000OOO0000000O0}/requests/@me",headers =O000OO00O0O0O00O0 ,json =OO000O0O00OOOOO00 )#line:451
        if OOO0O0OOO0OOO0OOO .status_code ==201 :#line:452
            print (f"[+] MemberscreeningBypassed {O0O00OO0000OOO0O0}")#line:453
            return #line:454
        else :#line:455
            print (f"[!] Bypassが出来ませんでした {O0O00OO0000OOO0O0}")#line:456
            return #line:457
    except Exception as O0O0OO0OO0O0000O0 :#line:458
        print (f"[!] エラーが発生しました。{O0O0OO0OO0O0000O0}")#line:459
session =requests .Session ()#line:461
def reactionput (O0O0O0OOOO0OO000O ,O0O00OOOOO0O00OO0 ,O0O0O0OO0O0O0O0O0 ,OO00OO0OO00O0OO00 ,proxy =None ):#line:464
    OOO00OO0000OOO0O0 =get_session (proxy )#line:465
    O000O0000O0O00OOO =get_headers (OOO00OO0000OOO0O0 )#line:466
    O000O0000O0O00OOO ["Authorization"]=O0O0O0OOOO0OO000O #line:467
    OO00OO0OO00O0OO00 =requests .utils .quote (OO00OO0OO00O0OO00 )#line:469
    OO00OOOO0OO0OOO00 =OOO00OO0000OOO0O0 .put (f"https://discord.com/api/v9/channels/{O0O00OOOOO0O00OO0}/messages/{O0O0O0OO0O0O0O0O0}/reactions/{OO00OO0OO00O0OO00}/%40me?location=Message&type=0",headers =O000O0000O0O00OOO )#line:473
    if OO00OOOO0OO0OOO00 .status_code in [200 ,204 ]:#line:474
        print (f"[+] Reaction '{OO00OO0OO00O0OO00}' added successfully to message {O0O0O0OO0O0O0O0O0}")#line:475
    elif OO00OOOO0OO0OOO00 .status_code ==429 :#line:476
        print ("[-] Rate limited. Please wait before retrying.")#line:477
        O0O0O0000OOO0O0OO =OO00OOOO0OO0OOO00 .json ().get ("retry_after",1 )#line:478
        time .sleep (O0O0O0000OOO0O0OO )#line:479
    elif OO00OOOO0OO0OOO00 .status_code ==401 :#line:480
        print ("[-] Invalid or expired token.")#line:481
    else :#line:482
        print (f"[!] Error occurred: {OO00OOOO0OO0OOO00.status_code}")#line:483
def generatexspandua (OOO000O00OOOOOOOO ):#line:486
  OOO0OO0OOO00O0OOO =["Android","Windows","Macintosh"]#line:487
  OOOO00OO0OO0OOOO0 =random .choice (OOO0OO0OOO00O0OOO )#line:488
  if OOOO00OO0OO0OOOO0 =="Macintosh":#line:489
    OO00OOO0OOOO0OO0O =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:490
    O000000OO00OO0OO0 ="Macintosh; Intel Mac OS X "+OO00OOO0OOOO0OO0O #line:491
    O000OOO0O0O0O000O ="x86_64"#line:492
  if OOOO00OO0OO0OOOO0 =="Windows":#line:493
    OO00OOO0OOOO0OO0O =f'{random.choice([6.0,10.0,11.0])}'#line:494
    O000000OO00OO0OO0 ="Windows NT "+OO00OOO0OOOO0OO0O +" Win64; x64"#line:495
    O000OOO0O0O0O000O ="x86_64"#line:496
  if OOOO00OO0OO0OOOO0 =="Android":#line:497
    OO00OOO0OOOO0OO0O ="13"#line:498
    O000000OO00OO0OO0 =f"Linux; Android 13; Pixel 6a"#line:499
    O000OOO0O0O0O000O ="aarch64"#line:500
  O0O0OOO000O000OO0 ={"os":OOOO00OO0OO0OOOO0 ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":OO00OOO0OOOO0OO0O ,"os_arch":O000OOO0O0O0O000O ,"system_locale":"ja-JP","client_build_number":OOO000O00OOOOOOOO ,"client_event_source":None ,"design_id":0 }#line:501
  O00OOOOO0O00OOO0O =f"Mozilla/5.0 ({O000000OO00OO0OO0}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:502
  return base64 .b64encode (json .dumps (O0O0OOO000O000OO0 ,separators =(',',':')).encode ()).decode (),O00OOOOO0O00OOO0O #line:503
import base64 #line:505
def nickchanger ():#line:508
    try :#line:509
        with open ("token.txt")as OOOO0OOOO00O0OOO0 :#line:510
            OOO0OO00000OO0OOO =[OO0O000O0OO0O0O0O .strip ()for OO0O000O0OO0O0O0O in OOOO0OOOO00O0OOO0 .readlines ()if OO0O000O0OO0O0O0O .strip ()]#line:511
    except (FileNotFoundError ,KeyError ):#line:512
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:513
        return #line:514
    OOO0O0O0000O00O00 =input ("Server ID?: ").strip ()#line:516
    O00OOO00OOOO00OO0 =input ("Nickname?: ").strip ()#line:517
    OO0O0O0OOOOOOOO0O =input ("Delay (in seconds)?: ").strip ()#line:518
    try :#line:520
        OO0O0O0OOOOOOOO0O =float (OO0O0O0OOOOOOOO0O )#line:521
        if OO0O0O0OOOOOOOO0O <0 :#line:522
            raise ValueError #line:523
    except ValueError :#line:524
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:525
        OO0O0O0OOOOOOOO0O =1.0 #line:526
    for OO0O00OOO0OOO0OO0 in OOO0OO00000OO0OOO :#line:528
        O00000OO00OOOOO00 ={"Authorization":OO0O00OOO0OOO0OO0 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:533
        OO00OOOO0000O0OOO ={"nick":O00OOO00OOOO00OO0 }#line:534
        OO000O000O0000O00 =requests .patch (f"https://discord.com/api/v9/guilds/{OOO0O0O0000O00O00}/members/@me",headers =O00000OO00OOOOO00 ,json =OO00OOOO0000O0OOO )#line:535
        if OO000O000O0000O00 .status_code ==200 :#line:537
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Nickname changed to '{O00OOO00OOOO00OO0}' successfully for token {OO0O00OOO0OOO0OO0}.{colorama.Fore.RESET}")#line:538
        elif OO000O000O0000O00 .status_code ==429 :#line:539
            print (f"{colorama.Fore.RED}    [!] Rate limited. Please wait before retrying for token {OO0O00OOO0OOO0OO0}.{colorama.Fore.RESET}")#line:540
            OOOO0OOO0O0OOOOOO =OO000O000O0000O00 .json ().get ("retry_after",1 )#line:541
            time .sleep (OOOO0OOO0O0OOOOOO )#line:542
        else :#line:543
            print (f"{colorama.Fore.RED}    [!] Error occurred: {OO000O000O0000O00.status_code} for token {OO0O00OOO0OOO0OO0}.{colorama.Fore.RESET}")#line:544
        time .sleep (OO0O0O0OOOOOOOO0O )#line:546
import json ,websocket ,threading ,tls_client ,random ,time #line:550
session =tls_client .Session (client_identifier ="chrome112",random_tls_extension_order =True )#line:552
class Utils :#line:554
    @staticmethod #line:555
    def rangeCorrector (O000O0OO0OO0OO0OO ):#line:556
        if [0 ,99 ]not in O000O0OO0OO0OO0OO :#line:557
            O000O0OO0OO0OO0OO .insert (0 ,[0 ,99 ])#line:558
        return O000O0OO0OO0OO0OO #line:559
    @staticmethod #line:561
    def getRanges (OO000O000OO000O0O ,O00OOO0O00O0OOO00 ,O00O0000000OOO00O ):#line:562
        OOOO0O00O0O00OOO0 =int (OO000O000OO000O0O *O00OOO0O00O0OOO00 )#line:563
        O0O0OO0OOO00OO00O =[[OOOO0O00O0O00OOO0 ,OOOO0O00O0O00OOO0 +99 ]]#line:564
        if O00O0000000OOO00O >OOOO0O00O0O00OOO0 +99 :#line:565
            O0O0OO0OOO00OO00O .append ([OOOO0O00O0O00OOO0 +100 ,OOOO0O00O0O00OOO0 +199 ])#line:566
        return Utils .rangeCorrector (O0O0OO0OOO00OO00O )#line:567
    @staticmethod #line:569
    def parseGuildMemberListUpdate (OOO0O0OOO0O00O0O0 ):#line:570
        O0O0O00000O0OOO00 ={"online_count":OOO0O0OOO0O00O0O0 ["d"]["online_count"],"member_count":OOO0O0OOO0O00O0O0 ["d"]["member_count"],"id":OOO0O0OOO0O00O0O0 ["d"]["id"],"guild_id":OOO0O0OOO0O00O0O0 ["d"]["guild_id"],"hoisted_roles":OOO0O0OOO0O00O0O0 ["d"]["groups"],"types":[],"locations":[],"updates":[],}#line:580
        for OO00O00O0OO000O0O in OOO0O0OOO0O00O0O0 ["d"]["ops"]:#line:582
            O0O0O00000O0OOO00 ["types"].append (OO00O00O0OO000O0O ["op"])#line:583
            if OO00O00O0OO000O0O ["op"]in ("SYNC","INVALIDATE"):#line:584
                O0O0O00000O0OOO00 ["locations"].append (OO00O00O0OO000O0O ["range"])#line:585
                if OO00O00O0OO000O0O ["op"]=="SYNC":#line:586
                    O0O0O00000O0OOO00 ["updates"].append (OO00O00O0OO000O0O ["items"])#line:587
                else :#line:588
                    O0O0O00000O0OOO00 ["updates"].append ([])#line:589
            elif OO00O00O0OO000O0O ["op"]in ("INSERT","UPDATE","DELETE"):#line:590
                O0O0O00000O0OOO00 ["locations"].append (OO00O00O0OO000O0O ["index"])#line:591
                if OO00O00O0OO000O0O ["op"]=="DELETE":#line:592
                    O0O0O00000O0OOO00 ["updates"].append ([])#line:593
                else :#line:594
                    O0O0O00000O0OOO00 ["updates"].append (OO00O00O0OO000O0O ["item"])#line:595
        return O0O0O00000O0OOO00 #line:596
class DiscordSocket (websocket .WebSocketApp ):#line:598
    def __init__ (O00OO00000O0O00O0 ,OOOO0OOOOOO0000O0 ,OO00O0OO0OOOOOO0O ,O000OO00OOOO000O0 ):#line:599
        O00OO00000O0O00O0 .token =OOOO0OOOOOO0000O0 #line:600
        O00OO00000O0O00O0 .guild_id =OO00O0OO0OOOOOO0O #line:601
        O00OO00000O0O00O0 .channel_id =O000OO00OOOO000O0 #line:602
        O00OO00000O0O00O0 .socket_headers ={"Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","Cache-Control":"no-cache","Pragma":"no-cache","Sec-WebSocket-Extensions":"permessage-deflate; client_max_window_bits","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",}#line:610
        super ().__init__ ("wss://gateway.discord.gg/?encoding=json&v=9",header =O00OO00000O0O00O0 .socket_headers ,on_open =lambda O00OO0O00O0OOO000 :O00OO00000O0O00O0 .sock_open (O00OO0O00O0OOO000 ),on_message =lambda O0O0O00O0O000O000 ,OOO00OOO00O00OO0O :O00OO00000O0O00O0 .sock_message (O0O0O00O0O000O000 ,OOO00OOO00O00OO0O ),on_close =lambda O0O00OOOOO000000O ,O00OO0OO000OO0O0O ,O00O0O0O00OO0O000 :O00OO00000O0O00O0 .sock_close (O0O00OOOOO000000O ,O00OO0OO000OO0O0O ,O00O0O0O00OO0O000 ),)#line:619
        O00OO00000O0O00O0 .endScraping =False #line:621
        O00OO00000O0O00O0 .guilds ={}#line:622
        O00OO00000O0O00O0 .members ={}#line:623
        O00OO00000O0O00O0 .ranges =[[0 ,0 ]]#line:624
        O00OO00000O0O00O0 .lastRange =0 #line:625
        O00OO00000O0O00O0 .packets_recv =0 #line:626
    def run (OO0O000O0O0O0O0O0 ):#line:628
        OO0O000O0O0O0O0O0 .run_forever ()#line:629
        return OO0O000O0O0O0O0O0 .members #line:630
    def scrapeUsers (O0OO0O0OO0OO00OOO ):#line:632
        if not O0OO0O0OO0OO00OOO .endScraping :#line:633
            O0OO0O0OO0OO00OOO .send ('{"op":14,"d":{"guild_id":"'+O0OO0O0OO0OO00OOO .guild_id +'","typing":true,"activities":true,"threads":true,"channels":{"'+O0OO0O0OO0OO00OOO .channel_id +'":'+json .dumps (O0OO0O0OO0OO00OOO .ranges )+"}}}")#line:642
    def sock_open (OOO000O0O0OOOO000 ,O000OOO0O0O0O0OO0 ):#line:644
        OOO000O0O0OOOO000 .send ('{"op":2,"d":{"token":"'+OOO000O0O0OOOO000 .token +'","capabilities":125,"properties":{"os":"Windows NT","browser":"Chrome","device":"","system_locale":"it-IT","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36","browser_version":"119.0","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":103981,"client_event_source":null},"presence":{"status":"online","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}')#line:649
    def heartbeatThread (OOO00OO00OO0000OO ,O0OO000O0O0OO0000 ):#line:651
        try :#line:652
            while True :#line:653
                OOO00OO00OO0000OO .send ('{"op":1,"d":'+str (OOO00OO00OO0000OO .packets_recv )+"}")#line:654
                time .sleep (O0OO000O0O0OO0000 )#line:655
        except Exception as O00000O0OOOO0OOOO :#line:656
            pass #line:657
    def sock_message (O0O0O0O0OO00OOOOO ,O00O0O0O000OO0000 ,O00OOOO0OOOO000OO ):#line:659
        O0OO0OOO0OO00O0OO =json .loads (O00OOOO0OOOO000OO )#line:660
        if O0OO0OOO0OO00O0OO is None :#line:661
            return #line:662
        if O0OO0OOO0OO00O0OO ["op"]!=11 :#line:663
            O0O0O0O0OO00OOOOO .packets_recv +=1 #line:664
        if O0OO0OOO0OO00O0OO ["op"]==10 :#line:665
            threading .Thread (target =O0O0O0O0OO00OOOOO .heartbeatThread ,args =(O0OO0OOO0OO00O0OO ["d"]["heartbeat_interval"]/1000 ,),daemon =True ,).start ()#line:670
        if O0OO0OOO0OO00O0OO ["t"]=="READY":#line:671
            for OO00O000000O000OO in O0OO0OOO0OO00O0OO ["d"]["guilds"]:#line:672
                O0O0O0O0OO00OOOOO .guilds [OO00O000000O000OO ["id"]]={"member_count":OO00O000000O000OO ["member_count"]}#line:673
        if O0OO0OOO0OO00O0OO ["t"]=="READY_SUPPLEMENTAL":#line:674
            O0O0O0O0OO00OOOOO .ranges =Utils .getRanges (0 ,100 ,O0O0O0O0OO00OOOOO .guilds [O0O0O0O0OO00OOOOO .guild_id ]["member_count"])#line:677
            O0O0O0O0OO00OOOOO .scrapeUsers ()#line:678
        elif O0OO0OOO0OO00O0OO ["t"]=="GUILD_MEMBER_LIST_UPDATE":#line:679
            O0O000OOOOOOO0O0O =Utils .parseGuildMemberListUpdate (O0OO0OOO0OO00O0OO )#line:680
            if O0O000OOOOOOO0O0O ["guild_id"]==O0O0O0O0OO00OOOOO .guild_id and ("SYNC"in O0O000OOOOOOO0O0O ["types"]or "UPDATE"in O0O000OOOOOOO0O0O ["types"]):#line:684
                for O0OO0O00O00O0OO00 ,O00O00OOOO000000O in enumerate (O0O000OOOOOOO0O0O ["types"]):#line:685
                    if O00O00OOOO000000O =="SYNC":#line:686
                        if len (O0O000OOOOOOO0O0O ["updates"][O0OO0O00O00O0OO00 ])==0 :#line:687
                            O0O0O0O0OO00OOOOO .endScraping =True #line:688
                            break #line:689
                        for OOO00O000OOOO0O0O in O0O000OOOOOOO0O0O ["updates"][O0OO0O00O00O0OO00 ]:#line:691
                            if "member"in OOO00O000OOOO0O0O :#line:692
                                O0000000000O00000 =OOO00O000OOOO0O0O ["member"]#line:693
                                O0OOOOOOOO0O00O00 ={"tag":O0000000000O00000 ["user"]["username"]+"#"+O0000000000O00000 ["user"]["discriminator"],"id":O0000000000O00000 ["user"]["id"],}#line:699
                                if not O0000000000O00000 ["user"].get ("bot"):#line:700
                                    O0O0O0O0OO00OOOOO .members [O0000000000O00000 ["user"]["id"]]=O0OOOOOOOO0O00O00 #line:701
                    elif O00O00OOOO000000O =="UPDATE":#line:703
                        for OOO00O000OOOO0O0O in O0O000OOOOOOO0O0O ["updates"][O0OO0O00O00O0OO00 ]:#line:704
                            if "member"in OOO00O000OOOO0O0O :#line:705
                                O0000000000O00000 =OOO00O000OOOO0O0O ["member"]#line:706
                                O0OOOOOOOO0O00O00 ={"tag":O0000000000O00000 ["user"]["username"]+"#"+O0000000000O00000 ["user"]["discriminator"],"id":O0000000000O00000 ["user"]["id"],}#line:712
                                if not O0000000000O00000 ["user"].get ("bot"):#line:713
                                    O0O0O0O0OO00OOOOO .members [O0000000000O00000 ["user"]["id"]]=O0OOOOOOOO0O00O00 #line:714
                    O0O0O0O0OO00OOOOO .lastRange +=1 #line:716
                    O0O0O0O0OO00OOOOO .ranges =Utils .getRanges (O0O0O0O0OO00OOOOO .lastRange ,100 ,O0O0O0O0OO00OOOOO .guilds [O0O0O0O0OO00OOOOO .guild_id ]["member_count"])#line:719
                    time .sleep (0.45 )#line:720
                    O0O0O0O0OO00OOOOO .scrapeUsers ()#line:721
            if O0O0O0O0OO00OOOOO .endScraping :#line:723
                O0O0O0O0OO00OOOOO .close ()#line:724
    def sock_close (OOO000O0OO0OO0OOO ,OOOOOOO0OO0O00OOO ,O00OOO0OOO0OO0OO0 ,OO0000OO0000OO0O0 ):#line:726
        pass #line:727
def scrape (OO00O0O00O0O00OOO ,OOOO00O0OOOO00OO0 ,OOO0OO000OOO0000O ):#line:729
    O00O000O0O00OO000 =DiscordSocket (OO00O0O00O0O00OOO ,OOOO00O0OOOO00OO0 ,OOO0OO000OOO0000O )#line:730
    return O00O000O0O00OO000 .run ()#line:731
def member_scrape (OO00OO00O000O0O00 ,OOO0O0O0O0O00OO00 ,O0OO0OOOO00000OO0 ):#line:733
    O0O0O0OOOO000O0OO =[]#line:734
    for OO00OOOOO00OOOO00 in OO00OO00O000O0O00 :#line:735
        O0O0OO0OO000OO0OO ={"Authorization":OO00OOOOO00OOOO00 ,"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}#line:736
        OOOO0OOOOOOOOO0OO =session .get (f"https://canary.discord.com/api/v9/guilds/{OOO0O0O0O0O00OO00}",headers =O0O0OO0OO000OO0OO )#line:737
        if OOOO0OOOOOOOOO0OO .status_code ==200 :#line:738
            O0O0O0OOOO000O0OO .append (OO00OOOOO00OOOO00 )#line:739
            break #line:740
    if not O0O0O0OOOO000O0OO :#line:741
        print ("missing access")#line:742
    OO00OOOOO00OOOO00 =random .choice (O0O0O0OOOO000O0OO )#line:744
    O0OO00OO0O0O00000 =scrape (OO00OOOOO00OOOO00 ,OOO0O0O0O0O00OO00 ,O0OO0OOOO00000OO0 )#line:745
    OO000000OOOOOO0OO =[f"<@{O00O0O0O0000O0OO0}>"for O00O0O0O0000O0OO0 in [int (O000OOOO000OOOO00 )for O000OOOO000OOOO00 in O0OO00OO0O0O00000 .keys ()]]#line:746
    print (f"[SUCCESS] {len(OO000000OOOOOO0OO)} scraped members")#line:747
    return OO000000OOOOOO0OO #line:748
def spammer_menu ():#line:750
    try :#line:751
        with open ("token.txt")as OOO00O000O0O0000O :#line:752
            O0OO0O0O0OO0OOOO0 =[O0OOOO0000O0000OO .strip ()for O0OOOO0000O0000OO in OOO00O000O0O0000O .readlines ()if O0OOOO0000O0000OO .strip ()]#line:753
    except (FileNotFoundError ,KeyError ):#line:754
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:755
        return #line:756
    OOO000OOO0000OO00 =input ("Server ID?: ").strip ()#line:758
    OO00OO000O0O0O000 =input ("Message?: ").strip ()#line:759
    O000O000000OO000O =input ("Random mention (True/False)?: ").strip ().lower ()=='true'#line:760
    OOO0OOOOO0O0O000O =input ("Delay between messages (in seconds)?: ").strip ()#line:761
    O0OO0O0O0OO000O00 =input ("Number of messages to send?: ").strip ()#line:762
    O0O00O0000OOO0000 =input ("Blacklist User IDs (comma-separated) (Leave blank to skip)?: ").strip ().split (',')#line:763
    O0O00O0000OOO0000 =[f"<@{OO0O0OO0OO0OO0OO0.strip()}>"for OO0O0OO0OO0OO0OO0 in O0O00O0000OOO0000 if OO0O0OO0OO0OO0OO0 .strip ()]#line:764
    try :#line:766
        OOO0OOOOO0O0O000O =float (OOO0OOOOO0O0O000O )#line:767
        if OOO0OOOOO0O0O000O <0 :#line:768
            raise ValueError #line:769
    except ValueError :#line:770
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:771
        OOO0OOOOO0O0O000O =1.0 #line:772
    try :#line:774
        O0OO0O0O0OO000O00 =int (O0OO0O0O0OO000O00 )#line:775
        if O0OO0O0O0OO000O00 <=0 :#line:776
            raise ValueError #line:777
    except ValueError :#line:778
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:779
        O0OO0O0O0OO000O00 =1 #line:780
    OO000O0OOOOOOOOO0 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:782
    if OO000O0OOOOOOOOO0 =='2':#line:783
        OO0OO0O00O000O000 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:784
        OO0OO0O00O000O000 =[OOOO0OO0O0O0OOO00 .strip ()for OOOO0OO0O0O0OOO00 in OO0OO0O00O000O000 if OOOO0OO0O0O0OOO00 .strip ()]#line:785
    else :#line:786
        OO0OO0O00O000O000 =fetch_channels (O0OO0O0O0OO0OOOO0 [0 ],OOO000OOO0000OO00 )#line:787
    OO0O0OO0OOOOO00OO =None #line:789
    spammer (O0OO0O0O0OO0OOOO0 ,OOO000OOO0000OO00 ,OO0OO0O00O000O000 ,OO00OO000O0O0O000 ,O000O000000OO000O ,O0O00O0000OOO0000 ,OO0O0OO0OOOOO00OO ,O0OO0O0O0OO000O00 )#line:791
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:793
def spammer (OO00OOOO0OO0000O0 ,OO0O00OO00O00O00O ,OO0O00OO00O0O000O ,OO0OOOO00O0O0OOO0 ,O0OO000O0O0O00OOO ,OOO0OOO0OO0O00O00 ,O00OO00OOO000O0OO ,O0OOO0O0O0OOO0O00 ):#line:795
    O000O0OO0O0OO0OOO =get_session (O00OO00OOO000O0OO )#line:796
    O000O0O00O0OO0OO0 =0 #line:797
    O00OOOO0000O0O0OO =member_scrape (OO00OOOO0OO0000O0 ,OO0O00OO00O00O00O ,OO0O00OO00O0O000O [0 ])#line:799
    O00OOOO0000O0O0OO =[OOO00OO0OOOOOO00O for OOO00OO0OOOOOO00O in O00OOOO0000O0O0OO if OOO00OO0OOOOOO00O not in OOO0OOO0OO0O00O00 ]#line:800
    for _O00OOO0OOOO00000O in range (O0OOO0O0O0OOO0O00 ):#line:802
        O0O0O00OO0OO0OOO0 =OO00OOOO0OO0000O0 [O000O0O00O0OO0OO0 ]#line:803
        O0OOOO0O0OOO00O00 =get_headers (O0O0O00OO0OO0OOO0 )#line:804
        for OO000O0OO00O0O00O in OO0O00OO00O0O000O :#line:805
            O0OO0O00OO0OOOO0O =OO0OOOO00O0O0OOO0 #line:806
            if O0OO000O0O0O00OOO and O00OOOO0000O0O0OO :#line:807
                O0O000O000OO0O0OO =random .choice (O00OOOO0000O0O0OO )#line:808
                O0OO0O00OO0OOOO0O +=f" {O0O000O000OO0O0OO}"#line:809
            OOOOOO000O0O0OOOO =O000O0OO0O0OO0OOO .post (f"https://discord.com/api/v9/channels/{OO000O0OO00O0O00O}/messages",json ={"content":O0OO0O00OO0OOOO0O },headers =O0OOOO0O0OOO00O00 )#line:811
            if OOOOOO000O0O0OOOO .status_code ==200 :#line:812
                print (f"200 message sent: {O0O0O00OO0OO0OOO0}")#line:813
            elif OOOOOO000O0O0OOOO .status_code ==429 :#line:814
                print (f"429 rate limit: {O0O0O00OO0OO0OOO0}")#line:815
                OO000O0O00OOO0OOO =OOOOOO000O0O0OOOO .json ().get ("retry_after",1 )#line:816
                time .sleep (OO000O0O00OOO0OOO )#line:817
            elif OOOOOO000O0O0OOOO .status_code ==401 :#line:818
                print (f"401 unknown token: {O0O0O00OO0OO0OOO0}")#line:819
            else :#line:820
                print (f"error: {O0O0O00OO0OO0OOO0}")#line:821
        O000O0O00O0OO0OO0 =(O000O0O00O0OO0OO0 +1 )%len (OO00OOOO0OO0000O0 )#line:823
        time .sleep (1 )#line:824
import requests #line:828
import base64 #line:829
import colorama #line:830
import time #line:831
def add_emojis_from_files ():#line:833
    try :#line:834
        with open ("emojiname.txt")as O000OO0O0O00000OO ,open ("emojiurl.txt")as O0OOOOO0O0OO0000O :#line:835
            OO0O0000O00OOO00O =[O0OO0OO0O00O00O0O .strip ()for O0OO0OO0O00O00O0O in O000OO0O0O00000OO .read ().split (',')if O0OO0OO0O00O00O0O .strip ()]#line:836
            OO0O000OOO0OOO0OO =[OO0OO000OOO0OO000 .strip ()for OO0OO000OOO0OO000 in O0OOOOO0O0OO0000O .read ().split (',')if OO0OO000OOO0OO000 .strip ()]#line:837
    except FileNotFoundError as O00OO0O0O0O00000O :#line:838
        print (f"{colorama.Fore.RED}    [!] Error: {str(O00OO0O0O0O00000O)}{colorama.Fore.RESET}")#line:839
        return #line:840
    if len (OO0O0000O00OOO00O )!=len (OO0O000OOO0OOO0OO ):#line:842
        print (f"{colorama.Fore.RED}    [!] Error: The number of emoji names and URLs do not match!{colorama.Fore.RESET}")#line:843
        return #line:844
    try :#line:846
        with open ("token.txt")as OO0O0O00OO00OOO00 :#line:847
            OOO00O0O0OOOOOO00 =[O00000O00OOO0OOO0 .strip ()for O00000O00OOO0OOO0 in OO0O0O00OO00OOO00 .readlines ()if O00000O00OOO0OOO0 .strip ()]#line:848
    except FileNotFoundError as O00OO0O0O0O00000O :#line:849
        print (f"{colorama.Fore.RED}    [!] Error: {str(O00OO0O0O0O00000O)}{colorama.Fore.RESET}")#line:850
        return #line:851
    O00000O0O0OOO0000 =input ("Enter the Guild ID: ").strip ()#line:853
    OO0OO0O0OO00OOOOO =input ("Enter the rate limit between requests (in seconds): ").strip ()#line:854
    try :#line:856
        OO0OO0O0OO00OOOOO =float (OO0OO0O0OO00OOOOO )#line:857
        if OO0OO0O0OO00OOOOO <0 :#line:858
            raise ValueError #line:859
    except ValueError :#line:860
        print (f"{colorama.Fore.RED}    [!] Invalid rate limit. Using default rate limit of 5 seconds.{colorama.Fore.RESET}")#line:861
        OO0OO0O0OO00OOOOO =5.0 #line:862
    OOOO00OO0000O0OOO =set ()#line:864
    for OO0000OOO0OOOO0OO in OOO00O0O0OOOOOO00 :#line:866
        OOO0000O0000O0OOO ={'Authorization':OO0000OOO0OOOO0OO ,'Content-Type':'application/json'}#line:870
        O00O0O00O0000OO00 =requests .get (f"https://discord.com/api/v9/guilds/{O00000O0O0OOO0000}/emojis",headers =OOO0000O0000O0OOO )#line:873
        if O00O0O00O0000OO00 .status_code ==200 :#line:874
            O0OO00OOOOOOOO0O0 =O00O0O00O0000OO00 .json ()#line:875
            for OOOOOOOOO0O0O0O0O in O0OO00OOOOOOOO0O0 :#line:876
                OOOO00OO0000O0OOO .add (OOOOOOOOO0O0O0O0O ['name'])#line:877
        else :#line:878
            print (f"{colorama.Fore.RED}    [!] Error fetching existing emojis: {O00O0O00O0000OO00.status_code} - {O00O0O00O0000OO00.text}{colorama.Fore.RESET}")#line:879
            continue #line:880
    for O00O000O000OO00OO ,O0O00OO00O00O0O0O in zip (OO0O0000O00OOO00O ,OO0O000OOO0OOO0OO ):#line:882
        if O00O000O000OO00OO in OOOO00OO0000O0OOO :#line:883
            print (f"{colorama.Fore.YELLOW}    [*] Emoji '{O00O000O000OO00OO}' already exists. Skipping...{colorama.Fore.RESET}")#line:884
            continue #line:885
        for OO0000OOO0OOOO0OO in OOO00O0O0OOOOOO00 :#line:887
            try :#line:888
                O00O0O00O0000OO00 =requests .get (O0O00OO00O00O0O0O )#line:889
                O00O0O00O0000OO00 .raise_for_status ()#line:890
                OOOO0O0OO0OO0OO00 =O00O0O00O0000OO00 .content #line:891
                O0OO000OOO000O0OO =base64 .b64encode (OOOO0O0OO0OO0OO00 ).decode ('utf-8')#line:892
                OOO0OO00O0O00O0OO ={'name':O00O000O000OO00OO ,'image':f"data:image/png;base64,{O0OO000OOO000O0OO}"}#line:897
                OOO0000O0000O0OOO ={'Authorization':OO0000OOO0OOOO0OO ,'Content-Type':'application/json'}#line:902
                O0OO0O0OO000OOOOO =requests .post (f"https://discord.com/api/v9/guilds/{O00000O0O0OOO0000}/emojis",headers =OOO0000O0000O0OOO ,json =OOO0OO00O0O00O0OO )#line:904
                if O0OO0O0OO000OOOOO .status_code ==201 :#line:905
                    print (f"{colorama.Fore.GREEN}    [+] Successfully added emoji '{O00O000O000OO00OO}' with token {OO0000OOO0OOOO0OO}{colorama.Fore.RESET}")#line:906
                    OOOO00OO0000O0OOO .add (O00O000O000OO00OO )#line:907
                    break #line:908
                else :#line:909
                    print (f"{colorama.Fore.RED}    [!] Failed to add emoji '{O00O000O000OO00OO}' with token {OO0000OOO0OOOO0OO}: {O0OO0O0OO000OOOOO.status_code} - {O0OO0O0OO000OOOOO.text}{colorama.Fore.RESET}")#line:910
                time .sleep (OO0OO0O0OO00OOOOO )#line:912
            except Exception as O00OO0O0O0O00000O :#line:913
                print (f"{colorama.Fore.RED}    [!] Error adding emoji '{O00O000O000OO00OO}' with token {OO0000OOO0OOOO0OO}: {str(O00OO0O0O0O00000O)}{colorama.Fore.RESET}")#line:914
def main ():#line:916
    colorama .init ()#line:917
    while True :#line:918
        logo ()#line:919
        OOO00O00O0OO00O00 =input (f"{colorama.Fore.LIGHTMAGENTA_EX}    [Final] Select an option from above: ")#line:920
        if OOO00O00O0OO00O00 =="g":#line:922
            update_group_ids ()#line:923
        elif OOO00O00O0OO00O00 =="1":#line:924
            join_discord_invite ()#line:925
        elif OOO00O00O0OO00O00 =="2":#line:926
            reaction_spammer ()#line:927
        elif OOO00O00O0OO00O00 =="3":#line:928
            send_messages_with_mentions ()#line:929
        elif OOO00O00O0OO00O00 =="4":#line:930
            spammer_menu ()#line:931
        elif OOO00O00O0OO00O00 =="5":#line:932
            nickchanger ()#line:933
        elif OOO00O00O0OO00O00 =="6":#line:934
            add_emojis_from_files ()#line:935
        elif OOO00O00O0OO00O00 =="0":#line:936
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [*] Exiting the application. Goodbye!{colorama.Fore.RESET}")#line:937
            break #line:938
        else :#line:939
            print (f"{colorama.Fore.RED}    [!] Invalid option selected!{colorama.Fore.RESET}")#line:940
        input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:942
if __name__ =="__main__":#line:944
    main ()#line:945
