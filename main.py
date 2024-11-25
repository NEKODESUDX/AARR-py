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

    [0] exit
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    {colorama.Fore.RESET}
    """)#line:51
def get_session (proxy =None ):#line:54
    OOOOO00O0O0O000O0 =requests .Session ()#line:55
    if proxy :#line:56
        OOOOO00O0O0O000O0 .proxies ={"http":proxy ,"https":proxy }#line:57
    return OOOOO00O0O0O000O0 #line:58
def get_headers (O0O0000OOOOOOO00O ):#line:60
    return {"Authorization":O0O0000OOOOOOO00O ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:65
def send_message_with_mention (O0O00O0OO0000OO00 ,OO000O0O0OO00O0O0 ,OOOOOO0O00000O0OO ,O00O00O000000OOOO ):#line:68
    OOO0OOO0O0O00OOO0 =get_session ()#line:69
    OO0O0O000O00O0000 =get_headers (O0O00O0OO0000OO00 )#line:70
    if O00O00O000000OOOO :#line:72
        OOOOO0O00OO00000O =random .choice (O00O00O000000OOOO )#line:73
        OOOOOO0O00000O0OO +=f" <@{OOOOO0O00OO00000O}>"#line:74
    OO0OO00OO000O0OOO =OOO0OOO0O0O00OOO0 .post (f"https://discord.com/api/v9/channels/{OO000O0O0OO00O0O0}/messages",headers =OO0O0O000O00O0000 ,json ={"content":OOOOOO0O00000O0OO })#line:80
    if OO0OO00OO000O0OOO .status_code in [200 ,201 ]:#line:81
        print (f"[+] Message sent to channel {OO000O0O0OO00O0O0}")#line:82
    elif OO0OO00OO000O0OOO .status_code ==429 :#line:83
        print ("[-] Rate limited. Please wait before retrying.")#line:84
        OOO0O0O0OOOOO00O0 =OO0OO00OO000O0OOO .json ().get ("retry_after",1 )#line:85
        time .sleep (OOO0O0O0OOOOO00O0 )#line:86
    else :#line:87
        print (f"[!] Error occurred: {OO0OO00OO000O0OOO.status_code}")#line:88
def fetch_messages (OO000OOOOO0O0000O ,OOO0O00O0OOOO0OOO ,limit =100 ):#line:91
    OOOO00O00OOOO0OO0 ={"Authorization":OO000OOOOO0O0000O ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:96
    O0O00O000OO000000 =requests .get (f"https://discord.com/api/v9/channels/{OOO0O00O0OOOO0OOO}/messages?limit={limit}",headers =OOOO00O00OOOO0OO0 )#line:100
    if O0O00O000OO000000 .status_code ==200 :#line:101
        return O0O00O000OO000000 .json ()#line:102
    else :#line:103
        print (f"[!] Failed to fetch messages. HTTP Status Code: {O0O00O000OO000000.status_code}")#line:104
        return []#line:105
import concurrent .futures #line:106
def reaction_spammer ():#line:108
    try :#line:109
        with open ("token.txt")as O00000OO00000000O :#line:110
            OOO0O0OO00O00OOO0 =[O0000OO0O0O00OO00 .strip ()for O0000OO0O0O00OO00 in O00000OO00000000O .readlines ()if O0000OO0O0O00OO00 .strip ()]#line:111
    except (FileNotFoundError ,KeyError ):#line:112
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:113
        return #line:114
    OOOOOO00OOO00OO00 =input ("Server ID?: ").strip ()#line:116
    OO0O0O0O0OO0OOO0O =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:118
    if OO0O0O0O0OO0OOO0O =='2':#line:119
        OO0O00OOO0OO0OOO0 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:120
        OO0O00O0O0000000O =[O00OO00O000O0O000 .strip ()for O00OO00O000O0O000 in OO0O00OOO0OO0OOO0 if O00OO00O000O0O000 .strip ()]#line:121
    else :#line:122
        OO0O00O0O0000000O =[]#line:123
        for O0O0O0O0O0OOO0OOO in OOO0O0OO00O00OOO0 :#line:124
            try :#line:125
                OO0O00O0O0000000O .extend (fetch_channels (O0O0O0O0O0OOO0OOO ,OOOOOO00OOO00OO00 ))#line:126
            except Exception as OOO000OO0O00OO0OO :#line:127
                print (f"[!] Failed to fetch channels for token. Error: {OOO000OO0O00OO0OO}")#line:128
                continue #line:129
    O0O0O00OO0OO00O00 =input ("Select your emoji (a, b, c, ... or custom emojis): ").strip ()#line:131
    OOOO0O000OOOO0O0O =input ("Delay between reactions (in seconds)?: ").strip ()#line:132
    try :#line:134
        OOOO0O000OOOO0O0O =float (OOOO0O000OOOO0O0O )#line:135
        if OOOO0O000OOOO0O0O <0 :#line:136
            raise ValueError #line:137
    except ValueError :#line:138
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:139
        OOOO0O000OOOO0O0O =1.0 #line:140
    OO0O0OOO000O0OOOO =[]#line:142
    for OOOOO0O000OOOO0OO in O0O0O00OO0OO00O00 .split (","):#line:143
        OOOOO0O000OOOO0OO =OOOOO0O000OOOO0OO .strip ().lower ()#line:144
        if OOOOO0O000OOOO0OO in alphabet_to_flag :#line:145
            OO0O0OOO000O0OOOO .append (alphabet_to_flag [OOOOO0O000OOOO0OO ])#line:146
        else :#line:147
            OO0O0OOO000O0OOOO .append (OOOOO0O000OOOO0OO )#line:148
    if not OO0O0OOO000O0OOOO :#line:150
        print (f"{colorama.Fore.RED}    [!] No valid emojis provided!{colorama.Fore.RESET}")#line:151
        return #line:152
    def O0OOO000OOOO0O000 (O00O0O0000O0O00OO ):#line:154
        for OO00OO0OOO00O000O in OO0O00O0O0000000O :#line:155
            try :#line:156
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {OO00OO0OOO00O000O}...{colorama.Fore.RESET}")#line:157
                OOOO0OO000O00OOO0 =fetch_messages (O00O0O0000O0O00OO ,OO00OO0OOO00O000O ,limit =100 )#line:158
                if not OOOO0OO000O00OOO0 :#line:159
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:160
                    continue #line:161
                for O0O0OO0OOOO0O0000 in OOOO0OO000O00OOO0 :#line:163
                    for OO000OO000O000O0O in OO0O0OOO000O0OOOO :#line:164
                        reactionput (O00O0O0000O0O00OO ,OO00OO0OOO00O000O ,O0O0OO0OOOO0O0000 ['id'],OO000OO000O000O0O )#line:165
                        time .sleep (OOOO0O000OOOO0O0O )#line:166
            except Exception as O00000OO0O00O00O0 :#line:167
                print (f"[!] Error processing channel {OO00OO0OOO00O000O}. Error: {O00000OO0O00O00O0}")#line:168
                continue #line:169
    with concurrent .futures .ThreadPoolExecutor ()as OO0OOOOO00O00OO00 :#line:171
        OO0O0OOOO0OO0OO0O =[OO0OOOOO00O00OO00 .submit (O0OOO000OOOO0O000 ,OOOOO0O0OOO00O000 )for OOOOO0O0OOO00O000 in OOO0O0OO00O00OOO0 ]#line:172
        concurrent .futures .wait (OO0O0OOOO0OO0OO0O )#line:173
def update_group_ids ():#line:176
    try :#line:177
        with open ("token.txt")as OOOO0OOO000O0000O :#line:178
            O0000OO00O000OOOO =[OOO0OO0O0O00O0O0O .strip ()for OOO0OO0O0O00O0O0O in OOOO0OOO000O0000O .readlines ()if OOO0OO0O0O00O0O0O .strip ()]#line:179
        O0OO0O0000O0O0O0O =O0000OO00O000OOOO [0 ]#line:180
    except (FileNotFoundError ,KeyError ):#line:181
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:182
        return #line:183
    OO0O00OO000O0OOOO ={"Authorization":O0OO0O0000O0O0O0O ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:189
    O000O00O0O0000OO0 =requests .get ('https://discord.com/api/v9/users/@me/channels',headers =OO0O00OO000O0OOOO )#line:191
    if O000O00O0O0000OO0 .status_code ==200 :#line:192
        OO000000OOO0OO0O0 =O000O00O0O0000OO0 .json ()#line:193
        with open ("group_id.txt","w")as O00O00O0O0O0O000O :#line:194
            for O0O000O00000OOO00 in OO000000OOO0OO0O0 :#line:195
                if O0O000O00000OOO00 ['type']==3 :#line:196
                    O00O00O0O0O0O000O .write (O0O000O00000OOO00 ['id']+'\n')#line:197
        print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Group IDs updated successfully.{colorama.Fore.RESET}")#line:198
    else :#line:199
        print (f"{colorama.Fore.LIGHTRED_EX}    [!] Failed to retrieve group IDs. HTTP Status Code: {O000O00O0O0000OO0.status_code}{colorama.Fore.RESET}")#line:200
import requests #line:202
import requests #line:204
def fetch_channels (OO000O00O00000000 ,O0OO0000OOOO0OOO0 ):#line:206
    try :#line:207
        O0000OO0O00O0000O =requests .Session ()#line:208
        OO00O0O0OOOO0O0OO =get_headers (OO000O00O00000000 )#line:209
        OOOOOOOOOOO000000 =O0000OO0O00O0000O .get (f"https://discord.com/api/v9/guilds/{O0OO0000OOOO0OOO0}/channels",headers =OO00O0O0OOOO0O0OO ,timeout =10 )#line:216
        if OOOOOOOOOOO000000 .status_code ==200 :#line:219
            try :#line:220
                O0000O00O00OO0O0O =OOOOOOOOOOO000000 .json ()#line:221
                return [O0O0O00OOO0OOO000 ['id']for O0O0O00OOO0OOO000 in O0000O00O00OO0O0O if O0O0O00OOO0OOO000 .get ('type')==0 ]#line:222
            except ValueError :#line:223
                print ("[!] Error: Response was not valid JSON.")#line:224
                return []#line:225
        elif OOOOOOOOOOO000000 .status_code ==401 :#line:226
            print ("[!] Error: Unauthorized - check your token.")#line:227
        elif OOOOOOOOOOO000000 .status_code ==403 :#line:228
            print ("[!] Error: Forbidden - you lack permissions.")#line:229
        elif OOOOOOOOOOO000000 .status_code ==404 :#line:230
            print ("[!] Error: Server not found - check the server ID.")#line:231
        else :#line:232
            print (f"[!] Error: Unexpected status code {OOOOOOOOOOO000000.status_code}.")#line:233
        return []#line:236
    except requests .exceptions .Timeout :#line:238
        print ("[!] Error: Request timed out. Check your connection or try again later.")#line:239
        return []#line:240
    except requests .exceptions .RequestException as O00OO0O0OO0000O0O :#line:241
        print (f"[!] Error: An error occurred while fetching channels: {O00OO0O0OO0000O0O}")#line:242
        return []#line:243
def extract_uids_from_messages (OO00OOOO0000OO000 ):#line:249
    O000OO0OO0O00OO0O =set ()#line:250
    for O000O0O0O00O0OOO0 in OO00OOOO0000OO000 :#line:251
        O000OO0OO0O00OO0O .add (O000O0O0O00O0OOO0 ['author']['id'])#line:252
    return list (O000OO0OO0O00OO0O )#line:253
def send_message_with_mention (O0O0O00OO00OOOOOO ,OO0OOOO0O0000O00O ,O00O0O00000OOOOO0 ,O0OOOO00O00O0O0O0 ):#line:255
    O0OOO0OO0O000000O =get_session ()#line:256
    OOOO0O0OOOO00O0O0 =get_headers (O0O0O00OO00OOOOOO )#line:257
    if O0OOOO00O00O0O0O0 :#line:259
        O0O0OO0OOO000000O =random .choice (O0OOOO00O00O0O0O0 )#line:260
        O00O0O00000OOOOO0 +=f" <@{O0O0OO0OOO000000O}>"#line:261
    O0000OOO00OO0O000 =O0OOO0OO0O000000O .post (f"https://discord.com/api/v9/channels/{OO0OOOO0O0000O00O}/messages",headers =OOOO0O0OOOO00O0O0 ,json ={"content":O00O0O00000OOOOO0 })#line:267
    if O0000OOO00OO0O000 .status_code in [200 ,201 ]:#line:268
        print (f"[+] Message sent to channel {OO0OOOO0O0000O00O}")#line:269
    elif O0000OOO00OO0O000 .status_code ==429 :#line:270
        print ("[-] Rate limited. Please wait before retrying.")#line:271
        O00O0000O0OO0O0O0 =O0000OOO00OO0O000 .json ().get ("retry_after",1 )#line:272
        time .sleep (O00O0000O0OO0O0O0 )#line:273
    else :#line:274
        print (f"[!] Error occurred: {O0000OOO00OO0O000.status_code}")#line:275
def send_messages_with_mentions ():#line:276
    try :#line:277
        with open ("token.txt")as O000O0O0O0O00OOO0 :#line:278
            OO0OO0OO00OO0O0O0 =[OOO0OOOOO0OOOO0OO .strip ()for OOO0OOOOO0OOOO0OO in O000O0O0O0O00OOO0 .readlines ()if OOO0OOOOO0OOOO0OO .strip ()]#line:279
    except (FileNotFoundError ,KeyError ):#line:280
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:281
        return #line:282
    OO0O000OO0OO000OO =input ("Server ID?: ").strip ()#line:284
    OO00OO0O000OOO0O0 =input ("Delay between messages (in seconds)?: ").strip ()#line:285
    OO00O000OOOO0OOOO =input ("Number of messages to send?: ").strip ()#line:286
    O00000000OOOOOOOO =input ("Message content?: ").strip ()#line:287
    O0000O0O000OO0OO0 =input ("Blacklist User IDs (comma-separated)?: ").strip ().split (',')#line:288
    O0000O0O000OO0OO0 =[OOO00OOO0OOOO00OO .strip ()for OOO00OOO0OOOO00OO in O0000O0O000OO0OO0 if OOO00OOO0OOOO00OO .strip ()]#line:289
    try :#line:291
        OO00OO0O000OOO0O0 =float (OO00OO0O000OOO0O0 )#line:292
        if OO00OO0O000OOO0O0 <0 :#line:293
            raise ValueError #line:294
    except ValueError :#line:295
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:296
        OO00OO0O000OOO0O0 =1.0 #line:297
    try :#line:299
        OO00O000OOOO0OOOO =int (OO00O000OOOO0OOOO )#line:300
        if OO00O000OOOO0OOOO <=0 :#line:301
            raise ValueError #line:302
    except ValueError :#line:303
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:304
        OO00O000OOOO0OOOO =1 #line:305
    OO0O00OOO0O0O0OOO =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:307
    if OO0O00OOO0O0O0OOO =='2':#line:308
        OOO0OO00000O0000O =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:309
        OOO0OO00000O0000O =[OOO0O00OO0O00O0O0 .strip ()for OOO0O00OO0O00O0O0 in OOO0OO00000O0000O if OOO0O00OO0O00O0O0 .strip ()]#line:310
    else :#line:311
        OOO0OO00000O0000O =[]#line:312
    O0000O0O0OO0000O0 =set ()#line:314
    for OOOOO0000O000O0OO in OO0OO0OO00OO0O0O0 :#line:315
        OOOO00OO00OO000OO =fetch_channels (OOOOO0000O000O0OO ,OO0O000OO0OO000OO )#line:316
        if OOO0OO00000O0000O :#line:317
            OOOO00OO00OO000OO =OOO0OO00000O0000O #line:318
        for OOOO00000O0OO0OOO in OOOO00OO00OO000OO :#line:319
            O0OO0OO000O0OOOOO =fetch_messages (OOOOO0000O000O0OO ,OOOO00000O0OO0OOO ,limit =100 )#line:320
            O0OOOO00OOOOOO0OO =extract_uids_from_messages (O0OO0OO000O0OOOOO )#line:321
            O0000O0O0OO0000O0 .update (O0OOOO00OOOOOO0OO )#line:322
    O0000O0O0OO0000O0 =list (set (O0000O0O0OO0000O0 )-set (O0000O0O000OO0OO0 ))#line:325
    for _OO00OOOO000OOOOOO in range (OO00O000OOOO0OOOO ):#line:327
        for OOOOO0000O000O0OO in OO0OO0OO00OO0O0O0 :#line:328
            for OOOO00000O0OO0OOO in OOOO00OO00OO000OO :#line:329
                send_message_with_mention (OOOOO0000O000O0OO ,OOOO00000O0OO0OOO ,O00000000OOOOOOOO ,O0000O0O0OO0000O0 )#line:330
                time .sleep (OO00OO0O000OOO0O0 )#line:331
def join_discord_invite ():#line:335
    try :#line:336
        with open ("token.txt")as O00OOOO00O000000O :#line:337
            OOO00O0OO0O00O0O0 =[OOO00O00000OOO0O0 .strip ()for OOO00O00000OOO0O0 in O00OOOO00O000000O .readlines ()if OOO00O00000OOO0O0 .strip ()]#line:338
    except (FileNotFoundError ,KeyError ):#line:339
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:340
        return #line:341
    O0OO00O0OOOO0000O =input ("Invite Code?: discord.gg/").strip ()#line:343
    for OOO00OOOO0O0O00OO in OOO00O0OO0O00O0O0 :#line:346
        joiner (OOO00OOOO0O0O00OO ,O0OO00O0OOOO0000O )#line:347
import json ,time ,base64 ,random ,requests #line:349
def cookieset (OOO000OO00OO00000 ):#line:351
    OO0OOO0O0O000OOO0 =OOO000OO00OO00000 .get ("https://discord.com/app")#line:352
    return OO0OOO0O0O000OOO0 .cookies .get_dict ()#line:353
def generatexspandua (O0000O00OOOOO0000 ):#line:355
    O000000OOO00OOO0O =["Android","Windows","Macintosh"]#line:356
    O0O00O0OOOO000OOO =random .choice (O000000OOO00OOO0O )#line:357
    if O0O00O0OOOO000OOO =="Macintosh":#line:358
        OOO00OO0OOOOOOO0O =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:359
        OO0OOO000OOO00OO0 ="Macintosh; Intel Mac OS X "+OOO00OO0OOOOOOO0O #line:360
        OO00O0O00O000O000 ="x86_64"#line:361
    elif O0O00O0OOOO000OOO =="Windows":#line:362
        OOO00OO0OOOOOOO0O =f'{random.choice([6.0, 10.0, 11.0])}'#line:363
        OO0OOO000OOO00OO0 ="Windows NT "+OOO00OO0OOOOOOO0O +" Win64; x64"#line:364
        OO00O0O00O000O000 ="x86_64"#line:365
    else :#line:366
        OOO00OO0OOOOOOO0O ="13"#line:367
        OO0OOO000OOO00OO0 =f"Linux; Android 13; Pixel 6a"#line:368
        OO00O0O00O000O000 ="aarch64"#line:369
    OOOO0000OOO0O0OO0 ={"os":O0O00O0OOOO000OOO ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":OOO00OO0OOOOOOO0O ,"os_arch":OO00O0O00O000O000 ,"system_locale":"ja-JP","client_build_number":O0000O00OOOOO0000 ,"client_event_source":None ,"design_id":0 }#line:382
    OOO0O0000OO00O0O0 =f"Mozilla/5.0 ({OO0OOO000OOO00OO0}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:383
    return base64 .b64encode (json .dumps (OOOO0000OOO0O0OO0 ,separators =(',',':')).encode ()).decode (),OOO0O0000OO00O0O0 #line:384
def joiner (OO0OOO000O00OO0O0 ,OO0OO0OO0000OO00O ,OO0O0OO0OO0O000O0 ):#line:386
    OOO00O000000O0OOO =cookieset (OO0O0OO0OO0O000O0 )#line:387
    OOO00O000000O0OOO ["locale"]="ja-JP"#line:388
    O0O00000OOO0OOO00 =201211 #line:389
    OOOOO0O0O0OO0000O ,O0OO000000O0000OO =generatexspandua (O0O00000OOO0OOO00 )#line:390
    OOOOOO000OO0O00OO ={"Authorization":OO0OOO000O00OO0O0 ,"accept":"*/*","accept-language":"ja-JP","connection":"keep-alive","DNT":"1","origin":"https://discord.com","sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","referer":"https://discord.com/channels/@me","TE":"Trailers","user-agent":O0OO000000O0000OO ,"X-Super-Properties":OOOOO0O0O0OO0000O ,}#line:405
    OOOO00O000000000O =OO0O0OO0OO0O000O0 .post ("https://discord.com/api/v9/invites/"+OO0OO0OO0000OO00O ,headers =OOOOOO000OO0O00OO ,json ={},cookies =OOO00O000000O0OOO )#line:406
    if OOOO00O000000000O .status_code ==200 :#line:407
        print ("[+] join this server "+OO0OOO000O00OO0O0 )#line:408
        if "show_verification_form"in OOOO00O000000000O .json ():#line:409
            bypass (OO0OOO000O00OO0O0 ,OOOO00O000000000O .json ()["guild"]["id"],OO0O0OO0OO0O000O0 ,OOOOOO000OO0O00OO )#line:410
        return #line:411
    elif "captcha_key"in OOOO00O000000000O .text and OOOO00O000000000O .status_code ==400 :#line:412
        print ("[!] Hcaptcha protect"+OO0OOO000O00OO0O0 )#line:413
        return #line:414
    elif OOOO00O000000000O .status_code ==401 :#line:415
        print ("[×] token is dead"+OO0OOO000O00OO0O0 )#line:416
        return #line:417
    elif OOOO00O000000000O .status_code ==403 :#line:418
        print ("[!] 403 banned "+OO0OOO000O00OO0O0 )#line:419
        return #line:420
    elif OOOO00O000000000O .status_code ==429 :#line:421
        OOOO0000OO0OOO0OO =OOOO00O000000000O .json ().get ("retry_after",1 )#line:422
        print (f"[!] 429 rate limit. Retrying after {OOOO0000OO0OOO0OO} seconds.")#line:423
        time .sleep (OOOO0000OO0OOO0OO )#line:424
        return #line:425
    else :#line:426
        print ("[!] error "+OO0OOO000O00OO0O0 )#line:427
        return #line:428
def update_group_ids ():#line:430
    O00OOOO0OO00OOOOO =input ("Invite Code?: ").strip ()#line:431
    try :#line:432
        with open ("token.txt")as O0OOO0000O00000OO :#line:433
            O00O00O0O0OOO0000 =[O0000O00O000O0O0O .strip ()for O0000O00O000O0O0O in O0OOO0000O00000OO .readlines ()if O0000O00O000O0O0O .strip ()]#line:434
    except (FileNotFoundError ,KeyError ):#line:435
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:436
        return #line:437
    O0OO0O0OO0OO000O0 =requests .Session ()#line:439
    for OO000O0O0OO00O00O in O00O00O0O0OOO0000 :#line:440
        joiner (OO000O0O0OO00O00O ,O00OOOO0OO00OOOOO ,O0OO0O0OO0OO000O0 )#line:441
        time .sleep (2 )#line:442
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:444
def bypass (OO00OO0OO00OO0OOO ,O0O0O0O0O0OOO00OO ,OOO0O0OO0OOOO000O ,O0OOOOO0OO0000OO0 ):#line:447
    try :#line:448
        OO0O000O00O000O00 =OOO0O0OO0OOOO000O .get (f"https://discord.com/api/v9/guilds/{O0O0O0O0O0OOO00OO}/member-verification?with_guild=false",headers =O0OOOOO0OO0000OO0 ).json ()#line:449
        OO0O0O0O0OOOO0OO0 =OOO0O0OO0OOOO000O .put (f"https://discord.com/api/v9/guilds/{O0O0O0O0O0OOO00OO}/requests/@me",headers =O0OOOOO0OO0000OO0 ,json =OO0O000O00O000O00 )#line:450
        if OO0O0O0O0OOOO0OO0 .status_code ==201 :#line:451
            print (f"[+] MemberscreeningBypassed {OO00OO0OO00OO0OOO}")#line:452
            return #line:453
        else :#line:454
            print (f"[!] Bypassが出来ませんでした {OO00OO0OO00OO0OOO}")#line:455
            return #line:456
    except Exception as OO000OOOOOO0O00OO :#line:457
        print (f"[!] エラーが発生しました。{OO000OOOOOO0O00OO}")#line:458
session =requests .Session ()#line:460
def reactionput (OOOOOOOOOOO0OOO00 ,OOO0O0OOO0OOO00OO ,O0O00OO0OO0O0O000 ,O00O0OO0O0OOOOO00 ,proxy =None ):#line:463
    OO00O0OO00O00O0OO =get_session (proxy )#line:464
    O0OOO0OOOO0O0OOO0 =get_headers (OO00O0OO00O00O0OO )#line:465
    O0OOO0OOOO0O0OOO0 ["Authorization"]=OOOOOOOOOOO0OOO00 #line:466
    O00O0OO0O0OOOOO00 =requests .utils .quote (O00O0OO0O0OOOOO00 )#line:468
    OOO00OOO0000OOOOO =OO00O0OO00O00O0OO .put (f"https://discord.com/api/v9/channels/{OOO0O0OOO0OOO00OO}/messages/{O0O00OO0OO0O0O000}/reactions/{O00O0OO0O0OOOOO00}/%40me?location=Message&type=0",headers =O0OOO0OOOO0O0OOO0 )#line:472
    if OOO00OOO0000OOOOO .status_code in [200 ,204 ]:#line:473
        print (f"[+] Reaction '{O00O0OO0O0OOOOO00}' added successfully to message {O0O00OO0OO0O0O000}")#line:474
    elif OOO00OOO0000OOOOO .status_code ==429 :#line:475
        print ("[-] Rate limited. Please wait before retrying.")#line:476
        O000O0OO0O0OOO00O =OOO00OOO0000OOOOO .json ().get ("retry_after",1 )#line:477
        time .sleep (O000O0OO0O0OOO00O )#line:478
    elif OOO00OOO0000OOOOO .status_code ==401 :#line:479
        print ("[-] Invalid or expired token.")#line:480
    else :#line:481
        print (f"[!] Error occurred: {OOO00OOO0000OOOOO.status_code}")#line:482
def generatexspandua (OOOOOOO0000O0O00O ):#line:485
  O000OO00O0O000O0O =["Android","Windows","Macintosh"]#line:486
  O0O00000O0OO00O00 =random .choice (O000OO00O0O000O0O )#line:487
  if O0O00000O0OO00O00 =="Macintosh":#line:488
    O0O00O000O00OOOOO =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:489
    O00O0OOOOO00OO0OO ="Macintosh; Intel Mac OS X "+O0O00O000O00OOOOO #line:490
    O000000O00OO0O0O0 ="x86_64"#line:491
  if O0O00000O0OO00O00 =="Windows":#line:492
    O0O00O000O00OOOOO =f'{random.choice([6.0,10.0,11.0])}'#line:493
    O00O0OOOOO00OO0OO ="Windows NT "+O0O00O000O00OOOOO +" Win64; x64"#line:494
    O000000O00OO0O0O0 ="x86_64"#line:495
  if O0O00000O0OO00O00 =="Android":#line:496
    O0O00O000O00OOOOO ="13"#line:497
    O00O0OOOOO00OO0OO =f"Linux; Android 13; Pixel 6a"#line:498
    O000000O00OO0O0O0 ="aarch64"#line:499
  O00OO0OO00O00O00O ={"os":O0O00000O0OO00O00 ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":O0O00O000O00OOOOO ,"os_arch":O000000O00OO0O0O0 ,"system_locale":"ja-JP","client_build_number":OOOOOOO0000O0O00O ,"client_event_source":None ,"design_id":0 }#line:500
  OOOOO000000OOOO0O =f"Mozilla/5.0 ({O00O0OOOOO00OO0OO}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:501
  return base64 .b64encode (json .dumps (O00OO0OO00O00O00O ,separators =(',',':')).encode ()).decode (),OOOOO000000OOOO0O #line:502
import base64 #line:504
def nickchanger ():#line:507
    try :#line:508
        with open ("token.txt")as O0O00OO00O00OO00O :#line:509
            OO0OOOO0O0O0O00O0 =[OO00O0OO0000O000O .strip ()for OO00O0OO0000O000O in O0O00OO00O00OO00O .readlines ()if OO00O0OO0000O000O .strip ()]#line:510
    except (FileNotFoundError ,KeyError ):#line:511
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:512
        return #line:513
    O0OOO000OO0O0000O =input ("Server ID?: ").strip ()#line:515
    OOOOOO00OOOOO0O0O =input ("Nickname?: ").strip ()#line:516
    OO0O00O000OOO0000 =input ("Delay (in seconds)?: ").strip ()#line:517
    try :#line:519
        OO0O00O000OOO0000 =float (OO0O00O000OOO0000 )#line:520
        if OO0O00O000OOO0000 <0 :#line:521
            raise ValueError #line:522
    except ValueError :#line:523
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:524
        OO0O00O000OOO0000 =1.0 #line:525
    for OOOO0OOOO00OOO000 in OO0OOOO0O0O0O00O0 :#line:527
        OO000OO0O0000O0OO ={"Authorization":OOOO0OOOO00OOO000 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:532
        O0O0OOOOO0000O0O0 ={"nick":OOOOOO00OOOOO0O0O }#line:533
        OO0O00O0OOOOOOO00 =requests .patch (f"https://discord.com/api/v9/guilds/{O0OOO000OO0O0000O}/members/@me",headers =OO000OO0O0000O0OO ,json =O0O0OOOOO0000O0O0 )#line:534
        if OO0O00O0OOOOOOO00 .status_code ==200 :#line:536
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Nickname changed to '{OOOOOO00OOOOO0O0O}' successfully for token {OOOO0OOOO00OOO000}.{colorama.Fore.RESET}")#line:537
        elif OO0O00O0OOOOOOO00 .status_code ==429 :#line:538
            print (f"{colorama.Fore.RED}    [!] Rate limited. Please wait before retrying for token {OOOO0OOOO00OOO000}.{colorama.Fore.RESET}")#line:539
            O0O0OO0O0O00OOO00 =OO0O00O0OOOOOOO00 .json ().get ("retry_after",1 )#line:540
            time .sleep (O0O0OO0O0O00OOO00 )#line:541
        else :#line:542
            print (f"{colorama.Fore.RED}    [!] Error occurred: {OO0O00O0OOOOOOO00.status_code} for token {OOOO0OOOO00OOO000}.{colorama.Fore.RESET}")#line:543
        time .sleep (OO0O00O000OOO0000 )#line:545
import json ,websocket ,threading ,tls_client ,random ,time #line:549
session =tls_client .Session (client_identifier ="chrome112",random_tls_extension_order =True )#line:551
class Utils :#line:553
    @staticmethod #line:554
    def rangeCorrector (O0000OOOO00O00O0O ):#line:555
        if [0 ,99 ]not in O0000OOOO00O00O0O :#line:556
            O0000OOOO00O00O0O .insert (0 ,[0 ,99 ])#line:557
        return O0000OOOO00O00O0O #line:558
    @staticmethod #line:560
    def getRanges (OOOOO0O0OO0O0OO00 ,O00O0O000OOO0OOO0 ,OOOO0O00OOOO0OOOO ):#line:561
        O000OO0OOOOOOO00O =int (OOOOO0O0OO0O0OO00 *O00O0O000OOO0OOO0 )#line:562
        OOOO00OOOOOOO00OO =[[O000OO0OOOOOOO00O ,O000OO0OOOOOOO00O +99 ]]#line:563
        if OOOO0O00OOOO0OOOO >O000OO0OOOOOOO00O +99 :#line:564
            OOOO00OOOOOOO00OO .append ([O000OO0OOOOOOO00O +100 ,O000OO0OOOOOOO00O +199 ])#line:565
        return Utils .rangeCorrector (OOOO00OOOOOOO00OO )#line:566
    @staticmethod #line:568
    def parseGuildMemberListUpdate (O0OO0OOOO00000OOO ):#line:569
        O0OO00O0O0OOOO0OO ={"online_count":O0OO0OOOO00000OOO ["d"]["online_count"],"member_count":O0OO0OOOO00000OOO ["d"]["member_count"],"id":O0OO0OOOO00000OOO ["d"]["id"],"guild_id":O0OO0OOOO00000OOO ["d"]["guild_id"],"hoisted_roles":O0OO0OOOO00000OOO ["d"]["groups"],"types":[],"locations":[],"updates":[],}#line:579
        for OO0O0000O0O000OO0 in O0OO0OOOO00000OOO ["d"]["ops"]:#line:581
            O0OO00O0O0OOOO0OO ["types"].append (OO0O0000O0O000OO0 ["op"])#line:582
            if OO0O0000O0O000OO0 ["op"]in ("SYNC","INVALIDATE"):#line:583
                O0OO00O0O0OOOO0OO ["locations"].append (OO0O0000O0O000OO0 ["range"])#line:584
                if OO0O0000O0O000OO0 ["op"]=="SYNC":#line:585
                    O0OO00O0O0OOOO0OO ["updates"].append (OO0O0000O0O000OO0 ["items"])#line:586
                else :#line:587
                    O0OO00O0O0OOOO0OO ["updates"].append ([])#line:588
            elif OO0O0000O0O000OO0 ["op"]in ("INSERT","UPDATE","DELETE"):#line:589
                O0OO00O0O0OOOO0OO ["locations"].append (OO0O0000O0O000OO0 ["index"])#line:590
                if OO0O0000O0O000OO0 ["op"]=="DELETE":#line:591
                    O0OO00O0O0OOOO0OO ["updates"].append ([])#line:592
                else :#line:593
                    O0OO00O0O0OOOO0OO ["updates"].append (OO0O0000O0O000OO0 ["item"])#line:594
        return O0OO00O0O0OOOO0OO #line:595
class DiscordSocket (websocket .WebSocketApp ):#line:597
    def __init__ (O0OO000O0O00OOOOO ,O0OOOO0000O00O00O ,O000O00O00OOOO00O ,OO00O000OO0O0OOOO ):#line:598
        O0OO000O0O00OOOOO .token =O0OOOO0000O00O00O #line:599
        O0OO000O0O00OOOOO .guild_id =O000O00O00OOOO00O #line:600
        O0OO000O0O00OOOOO .channel_id =OO00O000OO0O0OOOO #line:601
        O0OO000O0O00OOOOO .socket_headers ={"Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","Cache-Control":"no-cache","Pragma":"no-cache","Sec-WebSocket-Extensions":"permessage-deflate; client_max_window_bits","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",}#line:609
        super ().__init__ ("wss://gateway.discord.gg/?encoding=json&v=9",header =O0OO000O0O00OOOOO .socket_headers ,on_open =lambda O0O0OO0OO00OO0000 :O0OO000O0O00OOOOO .sock_open (O0O0OO0OO00OO0000 ),on_message =lambda OO0O0OO0O0O00OO0O ,OOO0OOO00OOO0O000 :O0OO000O0O00OOOOO .sock_message (OO0O0OO0O0O00OO0O ,OOO0OOO00OOO0O000 ),on_close =lambda O00O0O00OO00O00O0 ,OO000O00OO0OO0O00 ,O00OO00O0O00O0O00 :O0OO000O0O00OOOOO .sock_close (O00O0O00OO00O00O0 ,OO000O00OO0OO0O00 ,O00OO00O0O00O0O00 ),)#line:618
        O0OO000O0O00OOOOO .endScraping =False #line:620
        O0OO000O0O00OOOOO .guilds ={}#line:621
        O0OO000O0O00OOOOO .members ={}#line:622
        O0OO000O0O00OOOOO .ranges =[[0 ,0 ]]#line:623
        O0OO000O0O00OOOOO .lastRange =0 #line:624
        O0OO000O0O00OOOOO .packets_recv =0 #line:625
    def run (OO0000000OOO0O0O0 ):#line:627
        OO0000000OOO0O0O0 .run_forever ()#line:628
        return OO0000000OOO0O0O0 .members #line:629
    def scrapeUsers (O00O000O000000OO0 ):#line:631
        if not O00O000O000000OO0 .endScraping :#line:632
            O00O000O000000OO0 .send ('{"op":14,"d":{"guild_id":"'+O00O000O000000OO0 .guild_id +'","typing":true,"activities":true,"threads":true,"channels":{"'+O00O000O000000OO0 .channel_id +'":'+json .dumps (O00O000O000000OO0 .ranges )+"}}}")#line:641
    def sock_open (OO0O0O00OO00O000O ,O0OO0000OOOO0O0O0 ):#line:643
        OO0O0O00OO00O000O .send ('{"op":2,"d":{"token":"'+OO0O0O00OO00O000O .token +'","capabilities":125,"properties":{"os":"Windows NT","browser":"Chrome","device":"","system_locale":"it-IT","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36","browser_version":"119.0","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":103981,"client_event_source":null},"presence":{"status":"online","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}')#line:648
    def heartbeatThread (OO0OOOOOO0OOO0OO0 ,O000O0O00OOOO0OOO ):#line:650
        try :#line:651
            while True :#line:652
                OO0OOOOOO0OOO0OO0 .send ('{"op":1,"d":'+str (OO0OOOOOO0OOO0OO0 .packets_recv )+"}")#line:653
                time .sleep (O000O0O00OOOO0OOO )#line:654
        except Exception as O0O0O0OO0OOO00OOO :#line:655
            pass #line:656
    def sock_message (O00OOO0OO000OO0OO ,O00OO00OOOO000O00 ,OO0OO0O00000OOOOO ):#line:658
        O000O0O000O00OOOO =json .loads (OO0OO0O00000OOOOO )#line:659
        if O000O0O000O00OOOO is None :#line:660
            return #line:661
        if O000O0O000O00OOOO ["op"]!=11 :#line:662
            O00OOO0OO000OO0OO .packets_recv +=1 #line:663
        if O000O0O000O00OOOO ["op"]==10 :#line:664
            threading .Thread (target =O00OOO0OO000OO0OO .heartbeatThread ,args =(O000O0O000O00OOOO ["d"]["heartbeat_interval"]/1000 ,),daemon =True ,).start ()#line:669
        if O000O0O000O00OOOO ["t"]=="READY":#line:670
            for O0OOOOOOOO00O00O0 in O000O0O000O00OOOO ["d"]["guilds"]:#line:671
                O00OOO0OO000OO0OO .guilds [O0OOOOOOOO00O00O0 ["id"]]={"member_count":O0OOOOOOOO00O00O0 ["member_count"]}#line:672
        if O000O0O000O00OOOO ["t"]=="READY_SUPPLEMENTAL":#line:673
            O00OOO0OO000OO0OO .ranges =Utils .getRanges (0 ,100 ,O00OOO0OO000OO0OO .guilds [O00OOO0OO000OO0OO .guild_id ]["member_count"])#line:676
            O00OOO0OO000OO0OO .scrapeUsers ()#line:677
        elif O000O0O000O00OOOO ["t"]=="GUILD_MEMBER_LIST_UPDATE":#line:678
            OOOO0O0O0O0OOO0O0 =Utils .parseGuildMemberListUpdate (O000O0O000O00OOOO )#line:679
            if OOOO0O0O0O0OOO0O0 ["guild_id"]==O00OOO0OO000OO0OO .guild_id and ("SYNC"in OOOO0O0O0O0OOO0O0 ["types"]or "UPDATE"in OOOO0O0O0O0OOO0O0 ["types"]):#line:683
                for OO000OO0OOOO0OOO0 ,OOO0O0O0O0O00O00O in enumerate (OOOO0O0O0O0OOO0O0 ["types"]):#line:684
                    if OOO0O0O0O0O00O00O =="SYNC":#line:685
                        if len (OOOO0O0O0O0OOO0O0 ["updates"][OO000OO0OOOO0OOO0 ])==0 :#line:686
                            O00OOO0OO000OO0OO .endScraping =True #line:687
                            break #line:688
                        for OO0OOOOO00O000OO0 in OOOO0O0O0O0OOO0O0 ["updates"][OO000OO0OOOO0OOO0 ]:#line:690
                            if "member"in OO0OOOOO00O000OO0 :#line:691
                                OOOO0OO0O0OO0000O =OO0OOOOO00O000OO0 ["member"]#line:692
                                OO0000O0OOOOOO0OO ={"tag":OOOO0OO0O0OO0000O ["user"]["username"]+"#"+OOOO0OO0O0OO0000O ["user"]["discriminator"],"id":OOOO0OO0O0OO0000O ["user"]["id"],}#line:698
                                if not OOOO0OO0O0OO0000O ["user"].get ("bot"):#line:699
                                    O00OOO0OO000OO0OO .members [OOOO0OO0O0OO0000O ["user"]["id"]]=OO0000O0OOOOOO0OO #line:700
                    elif OOO0O0O0O0O00O00O =="UPDATE":#line:702
                        for OO0OOOOO00O000OO0 in OOOO0O0O0O0OOO0O0 ["updates"][OO000OO0OOOO0OOO0 ]:#line:703
                            if "member"in OO0OOOOO00O000OO0 :#line:704
                                OOOO0OO0O0OO0000O =OO0OOOOO00O000OO0 ["member"]#line:705
                                OO0000O0OOOOOO0OO ={"tag":OOOO0OO0O0OO0000O ["user"]["username"]+"#"+OOOO0OO0O0OO0000O ["user"]["discriminator"],"id":OOOO0OO0O0OO0000O ["user"]["id"],}#line:711
                                if not OOOO0OO0O0OO0000O ["user"].get ("bot"):#line:712
                                    O00OOO0OO000OO0OO .members [OOOO0OO0O0OO0000O ["user"]["id"]]=OO0000O0OOOOOO0OO #line:713
                    O00OOO0OO000OO0OO .lastRange +=1 #line:715
                    O00OOO0OO000OO0OO .ranges =Utils .getRanges (O00OOO0OO000OO0OO .lastRange ,100 ,O00OOO0OO000OO0OO .guilds [O00OOO0OO000OO0OO .guild_id ]["member_count"])#line:718
                    time .sleep (0.45 )#line:719
                    O00OOO0OO000OO0OO .scrapeUsers ()#line:720
            if O00OOO0OO000OO0OO .endScraping :#line:722
                O00OOO0OO000OO0OO .close ()#line:723
    def sock_close (O0O00000OO00OO0O0 ,O000OO0OO0OOO0O00 ,O0O000O0O00O0OO0O ,OOO0000O00OOOO0O0 ):#line:725
        pass #line:726
def scrape (OOO000O0000O00O0O ,OO0000O00OO00O0O0 ,OOO0O0O0O0OOO000O ):#line:728
    O0O0OOOO0O00000OO =DiscordSocket (OOO000O0000O00O0O ,OO0000O00OO00O0O0 ,OOO0O0O0O0OOO000O )#line:729
    return O0O0OOOO0O00000OO .run ()#line:730
def member_scrape (O0OOO0O0OOOO0O0OO ,OOOO0O0OOO00OOO0O ,O00OOO00OO000O000 ):#line:732
    OOO00O0OO0OOOOOO0 =[]#line:733
    for O000OO0OOO0O0O00O in O0OOO0O0OOOO0O0OO :#line:734
        OO0OO0000O0OOOOOO ={"Authorization":O000OO0OOO0O0O00O ,"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}#line:735
        O00OO0000O0000OOO =session .get (f"https://canary.discord.com/api/v9/guilds/{OOOO0O0OOO00OOO0O}",headers =OO0OO0000O0OOOOOO )#line:736
        if O00OO0000O0000OOO .status_code ==200 :#line:737
            OOO00O0OO0OOOOOO0 .append (O000OO0OOO0O0O00O )#line:738
            break #line:739
    if not OOO00O0OO0OOOOOO0 :#line:740
        print ("missing access")#line:741
    O000OO0OOO0O0O00O =random .choice (OOO00O0OO0OOOOOO0 )#line:743
    OOO000O00O0OO000O =scrape (O000OO0OOO0O0O00O ,OOOO0O0OOO00OOO0O ,O00OOO00OO000O000 )#line:744
    O0O0O0OO000000000 =[f"<@{O00O00O00O00OO000}>"for O00O00O00O00OO000 in [int (OOO000O0O0OO0O0OO )for OOO000O0O0OO0O0OO in OOO000O00O0OO000O .keys ()]]#line:745
    print (f"[SUCCESS] {len(O0O0O0OO000000000)} scraped members")#line:746
    return O0O0O0OO000000000 #line:747
def spammer_menu ():#line:749
    try :#line:750
        with open ("token.txt")as O0000O0000OO0O00O :#line:751
            OOO0O0OO00O0000O0 =[O0O0O0OO00O000000 .strip ()for O0O0O0OO00O000000 in O0000O0000OO0O00O .readlines ()if O0O0O0OO00O000000 .strip ()]#line:752
    except (FileNotFoundError ,KeyError ):#line:753
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:754
        return #line:755
    O00O0000O00OOO0OO =input ("Server ID?: ").strip ()#line:757
    OOO00O00O000OO00O =input ("Message?: ").strip ()#line:758
    O0O0O00000OO0OOOO =input ("Random mention (True/False)?: ").strip ().lower ()=='true'#line:759
    OOO000OOOO000O000 =input ("Delay between messages (in seconds)?: ").strip ()#line:760
    O0O000OOO0O00OO0O =input ("Number of messages to send?: ").strip ()#line:761
    OO000OO0O00OO00OO =input ("Blacklist User IDs (comma-separated) (Leave blank to skip)?: ").strip ().split (',')#line:762
    OO000OO0O00OO00OO =[f"<@{OOO0O00O0OO00OOO0.strip()}>"for OOO0O00O0OO00OOO0 in OO000OO0O00OO00OO if OOO0O00O0OO00OOO0 .strip ()]#line:763
    try :#line:765
        OOO000OOOO000O000 =float (OOO000OOOO000O000 )#line:766
        if OOO000OOOO000O000 <0 :#line:767
            raise ValueError #line:768
    except ValueError :#line:769
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:770
        OOO000OOOO000O000 =1.0 #line:771
    try :#line:773
        O0O000OOO0O00OO0O =int (O0O000OOO0O00OO0O )#line:774
        if O0O000OOO0O00OO0O <=0 :#line:775
            raise ValueError #line:776
    except ValueError :#line:777
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:778
        O0O000OOO0O00OO0O =1 #line:779
    OOO0O0OOOO000OOOO =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:781
    if OOO0O0OOOO000OOOO =='2':#line:782
        OO00O0OO0OO0OOO0O =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:783
        OO00O0OO0OO0OOO0O =[OOOO0000OOO0000O0 .strip ()for OOOO0000OOO0000O0 in OO00O0OO0OO0OOO0O if OOOO0000OOO0000O0 .strip ()]#line:784
    else :#line:785
        OO00O0OO0OO0OOO0O =fetch_channels (OOO0O0OO00O0000O0 [0 ],O00O0000O00OOO0OO )#line:786
    O0OOO00O00OO000OO =None #line:788
    spammer (OOO0O0OO00O0000O0 ,O00O0000O00OOO0OO ,OO00O0OO0OO0OOO0O ,OOO00O00O000OO00O ,O0O0O00000OO0OOOO ,OO000OO0O00OO00OO ,O0OOO00O00OO000OO ,O0O000OOO0O00OO0O )#line:790
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:792
def spammer (OO00O000O0O0O0O0O ,O00O00O0OOO0O000O ,OOO000OOOO0OO0OOO ,OOOO000O0O00O0O0O ,OOO0OOOOOO0000O0O ,O0000O0000O00O00O ,O00OOOOO0O0OOO0O0 ,OO00OO0O000OO000O ):#line:794
    O0OO0O00O0OOOO0OO =get_session (O00OOOOO0O0OOO0O0 )#line:795
    OOOO00O0OOO00000O =0 #line:796
    OO0OOOO0OO0000O0O =member_scrape (OO00O000O0O0O0O0O ,O00O00O0OOO0O000O ,OOO000OOOO0OO0OOO [0 ])#line:798
    OO0OOOO0OO0000O0O =[OOOO0O000OOO0000O for OOOO0O000OOO0000O in OO0OOOO0OO0000O0O if OOOO0O000OOO0000O not in O0000O0000O00O00O ]#line:799
    for _O00000OOOO0OO00OO in range (OO00OO0O000OO000O ):#line:801
        OOOOO0000OOO00O00 =OO00O000O0O0O0O0O [OOOO00O0OOO00000O ]#line:802
        O000OO0OOO0OOO0O0 =get_headers (OOOOO0000OOO00O00 )#line:803
        for OOO00O0O000O0O00O in OOO000OOOO0OO0OOO :#line:804
            OOOOOOO0OOO000OO0 =OOOO000O0O00O0O0O #line:805
            if OOO0OOOOOO0000O0O and OO0OOOO0OO0000O0O :#line:806
                OO00O00O00O00000O =random .choice (OO0OOOO0OO0000O0O )#line:807
                OOOOOOO0OOO000OO0 +=f" {OO00O00O00O00000O}"#line:808
            O0OO000OO0O0O0O00 =O0OO0O00O0OOOO0OO .post (f"https://discord.com/api/v9/channels/{OOO00O0O000O0O00O}/messages",json ={"content":OOOOOOO0OOO000OO0 },headers =O000OO0OOO0OOO0O0 )#line:810
            if O0OO000OO0O0O0O00 .status_code ==200 :#line:811
                print (f"200 message sent: {OOOOO0000OOO00O00}")#line:812
            elif O0OO000OO0O0O0O00 .status_code ==429 :#line:813
                print (f"429 rate limit: {OOOOO0000OOO00O00}")#line:814
                O000O0OOO0OO0O000 =O0OO000OO0O0O0O00 .json ().get ("retry_after",1 )#line:815
                time .sleep (O000O0OOO0OO0O000 )#line:816
            elif O0OO000OO0O0O0O00 .status_code ==401 :#line:817
                print (f"401 unknown token: {OOOOO0000OOO00O00}")#line:818
            else :#line:819
                print (f"error: {OOOOO0000OOO00O00}")#line:820
        OOOO00O0OOO00000O =(OOOO00O0OOO00000O +1 )%len (OO00O000O0O0O0O0O )#line:822
        time .sleep (1 )#line:823
def main ():#line:828
    colorama .init ()#line:829
    while True :#line:830
        logo ()#line:831
        O0OO0OO000OOO0OO0 =input (f"{colorama.Fore.LIGHTMAGENTA_EX}    [Final] Select an option from above: ")#line:832
        if O0OO0OO000OOO0OO0 =="0":#line:834
            update_group_ids ()#line:835
        elif O0OO0OO000OOO0OO0 =="1":#line:836
            join_discord_invite ()#line:837
        elif O0OO0OO000OOO0OO0 =="2":#line:838
            reaction_spammer ()#line:839
        elif O0OO0OO000OOO0OO0 =="3":#line:840
            send_messages_with_mentions ()#line:841
        elif O0OO0OO000OOO0OO0 =="5":#line:842
            nickchanger ()#line:843
        elif O0OO0OO000OOO0OO0 =="4":#line:844
            spammer_menu ()#line:845
        elif O0OO0OO000OOO0OO0 =="0":#line:846
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [*] Exiting the application. Goodbye!{colorama.Fore.RESET}")#line:847
            break #line:848
        else :#line:849
            print (f"{colorama.Fore.RED}    [!] Invalid option selected!{colorama.Fore.RESET}")#line:850
        input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:852
if __name__ =="__main__":#line:854
    main ()
