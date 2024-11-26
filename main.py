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
    O00O00O0O0OO0OO00 =requests .Session ()#line:55
    if proxy :#line:56
        O00O00O0O0OO0OO00 .proxies ={"http":proxy ,"https":proxy }#line:57
    return O00O00O0O0OO0OO00 #line:58
def get_headers (OO00O00O000OO00OO ):#line:60
    return {"Authorization":OO00O00O000OO00OO ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:65
def send_message_with_mention (O00OO0O0O00O000OO ,OOOOO00OOO00O0O00 ,OOOO00OO0OOO00O00 ,O00OOO0OO000OO0OO ):#line:68
    OO0O0O000O00O0OO0 =get_session ()#line:69
    OOOO0O00O000OOO00 =get_headers (O00OO0O0O00O000OO )#line:70
    if O00OOO0OO000OO0OO :#line:72
        OOO000OOOO0OO000O =random .choice (O00OOO0OO000OO0OO )#line:73
        OOOO00OO0OOO00O00 +=f" <@{OOO000OOOO0OO000O}>"#line:74
    O000OO0O0O0OOOO00 =OO0O0O000O00O0OO0 .post (f"https://discord.com/api/v9/channels/{OOOOO00OOO00O0O00}/messages",headers =OOOO0O00O000OOO00 ,json ={"content":OOOO00OO0OOO00O00 })#line:80
    if O000OO0O0O0OOOO00 .status_code in [200 ,201 ]:#line:81
        print (f"[+] Message sent to channel {OOOOO00OOO00O0O00}")#line:82
    elif O000OO0O0O0OOOO00 .status_code ==429 :#line:83
        print ("[-] Rate limited. Please wait before retrying.")#line:84
        O00O00OO000O0OOOO =O000OO0O0O0OOOO00 .json ().get ("retry_after",1 )#line:85
        time .sleep (O00O00OO000O0OOOO )#line:86
    else :#line:87
        print (f"[!] Error occurred: {O000OO0O0O0OOOO00.status_code}")#line:88
def fetch_messages (OO0OOO0O00O0OO00O ,O0000O0OOO00O0OOO ,limit =100 ):#line:91
    O0O00O0OO000O0O0O ={"Authorization":OO0OOO0O00O0OO00O ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:96
    OO0O0O0O0O000000O =requests .get (f"https://discord.com/api/v9/channels/{O0000O0OOO00O0OOO}/messages?limit={limit}",headers =O0O00O0OO000O0O0O )#line:100
    if OO0O0O0O0O000000O .status_code ==200 :#line:101
        return OO0O0O0O0O000000O .json ()#line:102
    else :#line:103
        print (f"[!] Failed to fetch messages. HTTP Status Code: {OO0O0O0O0O000000O.status_code}")#line:104
        return []#line:105
import concurrent .futures #line:106
def reaction_spammer ():#line:108
    try :#line:109
        with open ("token.txt")as OO0OO00O00O0O00OO :#line:110
            OO0O0000O00O000O0 =[O00000OOO000000O0 .strip ()for O00000OOO000000O0 in OO0OO00O00O0O00OO .readlines ()if O00000OOO000000O0 .strip ()]#line:111
    except (FileNotFoundError ,KeyError ):#line:112
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:113
        return #line:114
    O000O00OO0O0O0OO0 =input ("Server ID?: ").strip ()#line:116
    O000000OO000000O0 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:118
    if O000000OO000000O0 =='2':#line:119
        O00OOOO0OO000OO00 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:120
        OOOO0O0OOOO000000 =[O00O000O0OOOO0000 .strip ()for O00O000O0OOOO0000 in O00OOOO0OO000OO00 if O00O000O0OOOO0000 .strip ()]#line:121
    else :#line:122
        OOOO0O0OOOO000000 =[]#line:123
        for OOOOO00O0OOO0OO00 in OO0O0000O00O000O0 :#line:124
            try :#line:125
                OOOO0O0OOOO000000 .extend (fetch_channels (OOOOO00O0OOO0OO00 ,O000O00OO0O0O0OO0 ))#line:126
            except Exception as O0OOOO0OOO0O00O0O :#line:127
                print (f"[!] Failed to fetch channels for token. Error: {O0OOOO0OOO0O00O0O}")#line:128
                continue #line:129
    O000OO0O00O0OO0O0 =input ("Select your emoji (a, b, c, ... or custom emojis): ").strip ()#line:131
    OOOOO0OOOOO00O00O =input ("Delay between reactions (in seconds)?: ").strip ()#line:132
    try :#line:134
        OOOOO0OOOOO00O00O =float (OOOOO0OOOOO00O00O )#line:135
        if OOOOO0OOOOO00O00O <0 :#line:136
            raise ValueError #line:137
    except ValueError :#line:138
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:139
        OOOOO0OOOOO00O00O =1.0 #line:140
    O0O0OO00000OOOO0O =[]#line:142
    for O000000OOO000OOOO in O000OO0O00O0OO0O0 .split (","):#line:143
        O000000OOO000OOOO =O000000OOO000OOOO .strip ().lower ()#line:144
        if O000000OOO000OOOO in alphabet_to_flag :#line:145
            O0O0OO00000OOOO0O .append (alphabet_to_flag [O000000OOO000OOOO ])#line:146
        else :#line:147
            O0O0OO00000OOOO0O .append (O000000OOO000OOOO )#line:148
    if not O0O0OO00000OOOO0O :#line:150
        print (f"{colorama.Fore.RED}    [!] No valid emojis provided!{colorama.Fore.RESET}")#line:151
        return #line:152
    def OOOO00OO0OO0O0OOO (OO0OOOOO0OOO00000 ):#line:154
        for OOO00O0000O00O0OO in OOOO0O0OOOO000000 :#line:155
            try :#line:156
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {OOO00O0000O00O0OO}...{colorama.Fore.RESET}")#line:157
                O0O0O0O0O0O00OOO0 =fetch_messages (OO0OOOOO0OOO00000 ,OOO00O0000O00O0OO ,limit =100 )#line:158
                if not O0O0O0O0O0O00OOO0 :#line:159
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:160
                    continue #line:161
                for O0OOO0O000000O00O in O0O0O0O0O0O00OOO0 :#line:163
                    for OOO0O0OO000O0O000 in O0O0OO00000OOOO0O :#line:164
                        reactionput (OO0OOOOO0OOO00000 ,OOO00O0000O00O0OO ,O0OOO0O000000O00O ['id'],OOO0O0OO000O0O000 )#line:165
                        time .sleep (OOOOO0OOOOO00O00O )#line:166
            except Exception as O0000000000OOO0O0 :#line:167
                print (f"[!] Error processing channel {OOO00O0000O00O0OO}. Error: {O0000000000OOO0O0}")#line:168
                continue #line:169
    with concurrent .futures .ThreadPoolExecutor ()as O0O0O0000O0OOOOO0 :#line:171
        O0OOO00OO00O00000 =[O0O0O0000O0OOOOO0 .submit (OOOO00OO0OO0O0OOO ,O00O000000O0OOO00 )for O00O000000O0OOO00 in OO0O0000O00O000O0 ]#line:172
        concurrent .futures .wait (O0OOO00OO00O00000 )#line:173
def update_group_ids ():#line:176
    try :#line:177
        with open ("token.txt")as O000O00O00OO0OOO0 :#line:178
            O000OO0OO00O00O00 =[O00O0OO0O0OO0OOO0 .strip ()for O00O0OO0O0OO0OOO0 in O000O00O00OO0OOO0 .readlines ()if O00O0OO0O0OO0OOO0 .strip ()]#line:179
        OO0000O00000OO0OO =O000OO0OO00O00O00 [0 ]#line:180
    except (FileNotFoundError ,KeyError ):#line:181
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:182
        return #line:183
    O0O000O00OO0000OO ={"Authorization":OO0000O00000OO0OO ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:189
    OOO00O0OO00OO000O =requests .get ('https://discord.com/api/v9/users/@me/channels',headers =O0O000O00OO0000OO )#line:191
    if OOO00O0OO00OO000O .status_code ==200 :#line:192
        O0O00OO0O000OO00O =OOO00O0OO00OO000O .json ()#line:193
        with open ("group_id.txt","w")as O00O0OOO00OO00000 :#line:194
            for OOO0OOOOOO00O0O00 in O0O00OO0O000OO00O :#line:195
                if OOO0OOOOOO00O0O00 ['type']==3 :#line:196
                    O00O0OOO00OO00000 .write (OOO0OOOOOO00O0O00 ['id']+'\n')#line:197
        print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Group IDs updated successfully.{colorama.Fore.RESET}")#line:198
    else :#line:199
        print (f"{colorama.Fore.LIGHTRED_EX}    [!] Failed to retrieve group IDs. HTTP Status Code: {OOO00O0OO00OO000O.status_code}{colorama.Fore.RESET}")#line:200
import requests #line:202
import requests #line:204
def fetch_channels (OO0OOO000O0O00OO0 ,OO0000O0OO0O00000 ):#line:206
    try :#line:207
        O00OO0OOOOOOOOOOO =requests .Session ()#line:208
        O00OOO0OOO0OO0O0O =get_headers (OO0OOO000O0O00OO0 )#line:209
        OO0OO0O0OO00OOO00 =O00OO0OOOOOOOOOOO .get (f"https://discord.com/api/v9/guilds/{OO0000O0OO0O00000}/channels",headers =O00OOO0OOO0OO0O0O ,timeout =10 )#line:216
        if OO0OO0O0OO00OOO00 .status_code ==200 :#line:219
            try :#line:220
                O00O00OOO0OOOOOOO =OO0OO0O0OO00OOO00 .json ()#line:221
                return [O00OOOO0O00O0OOO0 ['id']for O00OOOO0O00O0OOO0 in O00O00OOO0OOOOOOO if O00OOOO0O00O0OOO0 .get ('type')==0 ]#line:222
            except ValueError :#line:223
                print ("[!] Error: Response was not valid JSON.")#line:224
                return []#line:225
        elif OO0OO0O0OO00OOO00 .status_code ==401 :#line:226
            print ("[!] Error: Unauthorized - check your token.")#line:227
        elif OO0OO0O0OO00OOO00 .status_code ==403 :#line:228
            print ("[!] Error: Forbidden - you lack permissions.")#line:229
        elif OO0OO0O0OO00OOO00 .status_code ==404 :#line:230
            print ("[!] Error: Server not found - check the server ID.")#line:231
        else :#line:232
            print (f"[!] Error: Unexpected status code {OO0OO0O0OO00OOO00.status_code}.")#line:233
        return []#line:236
    except requests .exceptions .Timeout :#line:238
        print ("[!] Error: Request timed out. Check your connection or try again later.")#line:239
        return []#line:240
    except requests .exceptions .RequestException as OO0000O0OO0O0O000 :#line:241
        print (f"[!] Error: An error occurred while fetching channels: {OO0000O0OO0O0O000}")#line:242
        return []#line:243
def extract_uids_from_messages (OOO0OOOO0OO0000OO ):#line:249
    OO0O00000O00000O0 =set ()#line:250
    for O0OOO0O000O00O000 in OOO0OOOO0OO0000OO :#line:251
        OO0O00000O00000O0 .add (O0OOO0O000O00O000 ['author']['id'])#line:252
    return list (OO0O00000O00000O0 )#line:253
def send_message_with_mention (O00OOOOOOO0OO00O0 ,O0OO0O0O0OOOO0000 ,OOO00O0000O0O0O00 ,OOO0O00000O0O0OO0 ):#line:255
    O0OO0O0O00OOOOOO0 =get_session ()#line:256
    OOOOOO0OO0OO0000O =get_headers (O00OOOOOOO0OO00O0 )#line:257
    if OOO0O00000O0O0OO0 :#line:259
        OOOO00000000O0O0O =random .choice (OOO0O00000O0O0OO0 )#line:260
        OOO00O0000O0O0O00 +=f" <@{OOOO00000000O0O0O}>"#line:261
    O0O0OOO0O0O0OO0O0 =O0OO0O0O00OOOOOO0 .post (f"https://discord.com/api/v9/channels/{O0OO0O0O0OOOO0000}/messages",headers =OOOOOO0OO0OO0000O ,json ={"content":OOO00O0000O0O0O00 })#line:267
    if O0O0OOO0O0O0OO0O0 .status_code in [200 ,201 ]:#line:268
        print (f"[+] Message sent to channel {O0OO0O0O0OOOO0000}")#line:269
    elif O0O0OOO0O0O0OO0O0 .status_code ==429 :#line:270
        print ("[-] Rate limited. Please wait before retrying.")#line:271
        OO0O0000OO000O0O0 =O0O0OOO0O0O0OO0O0 .json ().get ("retry_after",1 )#line:272
        time .sleep (OO0O0000OO000O0O0 )#line:273
    else :#line:274
        print (f"[!] Error occurred: {O0O0OOO0O0O0OO0O0.status_code}")#line:275
def send_messages_with_mentions ():#line:276
    try :#line:277
        with open ("token.txt")as O0O00O00000O0O0O0 :#line:278
            OO000O0000OO000OO =[O0O00000OO0O0OOOO .strip ()for O0O00000OO0O0OOOO in O0O00O00000O0O0O0 .readlines ()if O0O00000OO0O0OOOO .strip ()]#line:279
    except (FileNotFoundError ,KeyError ):#line:280
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:281
        return #line:282
    OOOO00O00O0OOO00O =input ("Server ID?: ").strip ()#line:284
    OO0O0O0O000OOO000 =input ("Delay between messages (in seconds)?: ").strip ()#line:285
    O0000O0O0O0O0OOOO =input ("Number of messages to send?: ").strip ()#line:286
    O0OOO0O0OOOO0O0O0 =input ("Message content?: ").strip ()#line:287
    OOOOO0OOO000OO0O0 =input ("Blacklist User IDs (comma-separated)?: ").strip ().split (',')#line:288
    OOOOO0OOO000OO0O0 =[O0OOO0OO0OOO0O000 .strip ()for O0OOO0OO0OOO0O000 in OOOOO0OOO000OO0O0 if O0OOO0OO0OOO0O000 .strip ()]#line:289
    try :#line:291
        OO0O0O0O000OOO000 =float (OO0O0O0O000OOO000 )#line:292
        if OO0O0O0O000OOO000 <0 :#line:293
            raise ValueError #line:294
    except ValueError :#line:295
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:296
        OO0O0O0O000OOO000 =1.0 #line:297
    try :#line:299
        O0000O0O0O0O0OOOO =int (O0000O0O0O0O0OOOO )#line:300
        if O0000O0O0O0O0OOOO <=0 :#line:301
            raise ValueError #line:302
    except ValueError :#line:303
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:304
        O0000O0O0O0O0OOOO =1 #line:305
    O0OOO0O0O000OO00O =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:307
    if O0OOO0O0O000OO00O =='2':#line:308
        OOOO0OOOOO00O0O0O =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:309
        OOOO0OOOOO00O0O0O =[O0OOOO0O0000000O0 .strip ()for O0OOOO0O0000000O0 in OOOO0OOOOO00O0O0O if O0OOOO0O0000000O0 .strip ()]#line:310
    else :#line:311
        OOOO0OOOOO00O0O0O =[]#line:312
    O00OO0OOO0O000OO0 =set ()#line:314
    for OO00O00O00OOO0O00 in OO000O0000OO000OO :#line:315
        OO0000000OO0OOO0O =fetch_channels (OO00O00O00OOO0O00 ,OOOO00O00O0OOO00O )#line:316
        for O0O00OO00O0O0O000 in OO0000000OO0OOO0O :#line:317
            OO0O00O000000O0OO =fetch_messages (OO00O00O00OOO0O00 ,O0O00OO00O0O0O000 ,limit =100 )#line:318
            OOOO0OO0000O0O000 =extract_uids_from_messages (OO0O00O000000O0OO )#line:319
            O00OO0OOO0O000OO0 .update (OOOO0OO0000O0O000 )#line:320
    O00OO0OOO0O000OO0 =list (set (O00OO0OOO0O000OO0 )-set (OOOOO0OOO000OO0O0 ))#line:323
    for _O0O00OO0O00OO0O0O in range (O0000O0O0O0O0OOOO ):#line:325
        for OO00O00O00OOO0O00 in OO000O0000OO000OO :#line:326
            if OOOO0OOOOO00O0O0O :#line:327
                OO0000000OO0OOO0O =OOOO0OOOOO00O0O0O #line:328
            for O0O00OO00O0O0O000 in OO0000000OO0OOO0O :#line:329
                send_message_with_mention (OO00O00O00OOO0O00 ,O0O00OO00O0O0O000 ,O0OOO0O0OOOO0O0O0 ,O00OO0OOO0O000OO0 )#line:330
                time .sleep (OO0O0O0O000OOO000 )#line:331
def join_discord_invite ():#line:337
    try :#line:338
        with open ("token.txt")as O0OO00O0O00OO0OOO :#line:339
            O0OO0O0OOO00OO000 =[OOOO0O0O0OOO0O000 .strip ()for OOOO0O0O0OOO0O000 in O0OO00O0O00OO0OOO .readlines ()if OOOO0O0O0OOO0O000 .strip ()]#line:340
    except (FileNotFoundError ,KeyError ):#line:341
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:342
        return #line:343
    O0000OO00O0O00O0O =input ("Invite Code?: discord.gg/").strip ()#line:345
    for O00OOO0O00OO0O0OO in O0OO0O0OOO00OO000 :#line:348
        joiner (O00OOO0O00OO0O0OO ,O0000OO00O0O00O0O )#line:349
import json ,time ,base64 ,random ,requests #line:351
def cookieset (OOO0OOOO00OOO0000 ):#line:353
    O0O0O0O00O00OOOO0 =OOO0OOOO00OOO0000 .get ("https://discord.com/app")#line:354
    return O0O0O0O00O00OOOO0 .cookies .get_dict ()#line:355
def generatexspandua (OOO00OO0OOO00OOOO ):#line:357
    OO0OO00OOO00000O0 =["Android","Windows","Macintosh"]#line:358
    OO000O00OOO00O00O =random .choice (OO0OO00OOO00000O0 )#line:359
    if OO000O00OOO00O00O =="Macintosh":#line:360
        O000000OOO000O0OO =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:361
        O00OOOO0OOOO0O00O ="Macintosh; Intel Mac OS X "+O000000OOO000O0OO #line:362
        O0O000000O00OO000 ="x86_64"#line:363
    elif OO000O00OOO00O00O =="Windows":#line:364
        O000000OOO000O0OO =f'{random.choice([6.0, 10.0, 11.0])}'#line:365
        O00OOOO0OOOO0O00O ="Windows NT "+O000000OOO000O0OO +" Win64; x64"#line:366
        O0O000000O00OO000 ="x86_64"#line:367
    else :#line:368
        O000000OOO000O0OO ="13"#line:369
        O00OOOO0OOOO0O00O =f"Linux; Android 13; Pixel 6a"#line:370
        O0O000000O00OO000 ="aarch64"#line:371
    OO0O000OOOO0OOO0O ={"os":OO000O00OOO00O00O ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":O000000OOO000O0OO ,"os_arch":O0O000000O00OO000 ,"system_locale":"ja-JP","client_build_number":OOO00OO0OOO00OOOO ,"client_event_source":None ,"design_id":0 }#line:384
    O0O0000OOO0OOOOOO =f"Mozilla/5.0 ({O00OOOO0OOOO0O00O}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:385
    return base64 .b64encode (json .dumps (OO0O000OOOO0OOO0O ,separators =(',',':')).encode ()).decode (),O0O0000OOO0OOOOOO #line:386
def joiner (O0OO0000O00O0OOO0 ,OO0OO0O00OO00O0O0 ,OOO0O000000OO000O ):#line:388
    OOO00O00OOO0OO00O =cookieset (OOO0O000000OO000O )#line:389
    OOO00O00OOO0OO00O ["locale"]="ja-JP"#line:390
    OO0O0OO0O0OOOO0O0 =201211 #line:391
    O00O000000O000OOO ,OO00OOOO000OO0OOO =generatexspandua (OO0O0OO0O0OOOO0O0 )#line:392
    O0OOO00O00000O0OO ={"Authorization":O0OO0000O00O0OOO0 ,"accept":"*/*","accept-language":"ja-JP","connection":"keep-alive","DNT":"1","origin":"https://discord.com","sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","referer":"https://discord.com/channels/@me","TE":"Trailers","user-agent":OO00OOOO000OO0OOO ,"X-Super-Properties":O00O000000O000OOO ,}#line:407
    O0O000O000OO0O0O0 =OOO0O000000OO000O .post ("https://discord.com/api/v9/invites/"+OO0OO0O00OO00O0O0 ,headers =O0OOO00O00000O0OO ,json ={},cookies =OOO00O00OOO0OO00O )#line:408
    if O0O000O000OO0O0O0 .status_code ==200 :#line:409
        print ("[+] join this server "+O0OO0000O00O0OOO0 )#line:410
        if "show_verification_form"in O0O000O000OO0O0O0 .json ():#line:411
            bypass (O0OO0000O00O0OOO0 ,O0O000O000OO0O0O0 .json ()["guild"]["id"],OOO0O000000OO000O ,O0OOO00O00000O0OO )#line:412
        return #line:413
    elif "captcha_key"in O0O000O000OO0O0O0 .text and O0O000O000OO0O0O0 .status_code ==400 :#line:414
        print ("[!] Hcaptcha protect"+O0OO0000O00O0OOO0 )#line:415
        return #line:416
    elif O0O000O000OO0O0O0 .status_code ==401 :#line:417
        print ("[×] token is dead"+O0OO0000O00O0OOO0 )#line:418
        return #line:419
    elif O0O000O000OO0O0O0 .status_code ==403 :#line:420
        print ("[!] 403 banned "+O0OO0000O00O0OOO0 )#line:421
        return #line:422
    elif O0O000O000OO0O0O0 .status_code ==429 :#line:423
        OO0000O00O000O00O =O0O000O000OO0O0O0 .json ().get ("retry_after",1 )#line:424
        print (f"[!] 429 rate limit. Retrying after {OO0000O00O000O00O} seconds.")#line:425
        time .sleep (OO0000O00O000O00O )#line:426
        return #line:427
    else :#line:428
        print ("[!] error "+O0OO0000O00O0OOO0 )#line:429
        return #line:430
def update_group_ids ():#line:432
    O00O000O0OO0O0OOO =input ("Invite Code?: ").strip ()#line:433
    try :#line:434
        with open ("token.txt")as O0OOOOOO0OOOO00O0 :#line:435
            OO000O0OO0OOOO0OO =[OO00O0O0000O000O0 .strip ()for OO00O0O0000O000O0 in O0OOOOOO0OOOO00O0 .readlines ()if OO00O0O0000O000O0 .strip ()]#line:436
    except (FileNotFoundError ,KeyError ):#line:437
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:438
        return #line:439
    OOOOOO00000OO0OOO =requests .Session ()#line:441
    for O0OO0O00OO0O0OO0O in OO000O0OO0OOOO0OO :#line:442
        joiner (O0OO0O00OO0O0OO0O ,O00O000O0OO0O0OOO ,OOOOOO00000OO0OOO )#line:443
        time .sleep (2 )#line:444
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:446
def bypass (O0OO0O00O00O0O0O0 ,O0O00O00OOO0O0O00 ,OOO0O0O0OOOOOO0OO ,O00OOOO0O0O0OOO0O ):#line:449
    try :#line:450
        O0OO0OOOO00OO0O00 =OOO0O0O0OOOOOO0OO .get (f"https://discord.com/api/v9/guilds/{O0O00O00OOO0O0O00}/member-verification?with_guild=false",headers =O00OOOO0O0O0OOO0O ).json ()#line:451
        OOO0O0OO000OO0O00 =OOO0O0O0OOOOOO0OO .put (f"https://discord.com/api/v9/guilds/{O0O00O00OOO0O0O00}/requests/@me",headers =O00OOOO0O0O0OOO0O ,json =O0OO0OOOO00OO0O00 )#line:452
        if OOO0O0OO000OO0O00 .status_code ==201 :#line:453
            print (f"[+] MemberscreeningBypassed {O0OO0O00O00O0O0O0}")#line:454
            return #line:455
        else :#line:456
            print (f"[!] Bypassが出来ませんでした {O0OO0O00O00O0O0O0}")#line:457
            return #line:458
    except Exception as O0000O0O00O0OO00O :#line:459
        print (f"[!] エラーが発生しました。{O0000O0O00O0OO00O}")#line:460
session =requests .Session ()#line:462
def reactionput (O00O0000O0OO00000 ,O0O0OO00000000000 ,OOOOO00OOO00O000O ,OO0O0000O0000OO00 ,proxy =None ):#line:465
    O0O00OOOOOO00O00O =get_session (proxy )#line:466
    OO00O000O0O0OOO00 =get_headers (O0O00OOOOOO00O00O )#line:467
    OO00O000O0O0OOO00 ["Authorization"]=O00O0000O0OO00000 #line:468
    OO0O0000O0000OO00 =requests .utils .quote (OO0O0000O0000OO00 )#line:470
    O00O00O0O0OOO0OOO =O0O00OOOOOO00O00O .put (f"https://discord.com/api/v9/channels/{O0O0OO00000000000}/messages/{OOOOO00OOO00O000O}/reactions/{OO0O0000O0000OO00}/%40me?location=Message&type=0",headers =OO00O000O0O0OOO00 )#line:474
    if O00O00O0O0OOO0OOO .status_code in [200 ,204 ]:#line:475
        print (f"[+] Reaction '{OO0O0000O0000OO00}' added successfully to message {OOOOO00OOO00O000O}")#line:476
    elif O00O00O0O0OOO0OOO .status_code ==429 :#line:477
        print ("[-] Rate limited. Please wait before retrying.")#line:478
        OO00OO0O0OOO0000O =O00O00O0O0OOO0OOO .json ().get ("retry_after",1 )#line:479
        time .sleep (OO00OO0O0OOO0000O )#line:480
    elif O00O00O0O0OOO0OOO .status_code ==401 :#line:481
        print ("[-] Invalid or expired token.")#line:482
    else :#line:483
        print (f"[!] Error occurred: {O00O00O0O0OOO0OOO.status_code}")#line:484
def generatexspandua (O0O000OO0O00O0O00 ):#line:487
  OO0OO000OOOOOOO00 =["Android","Windows","Macintosh"]#line:488
  OO0OOO0OOO0O00OO0 =random .choice (OO0OO000OOOOOOO00 )#line:489
  if OO0OOO0OOO0O00OO0 =="Macintosh":#line:490
    O000OO0OO000O0O00 =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:491
    OOOOO0O0OOOOOO0OO ="Macintosh; Intel Mac OS X "+O000OO0OO000O0O00 #line:492
    O00OOO000OOO00O00 ="x86_64"#line:493
  if OO0OOO0OOO0O00OO0 =="Windows":#line:494
    O000OO0OO000O0O00 =f'{random.choice([6.0,10.0,11.0])}'#line:495
    OOOOO0O0OOOOOO0OO ="Windows NT "+O000OO0OO000O0O00 +" Win64; x64"#line:496
    O00OOO000OOO00O00 ="x86_64"#line:497
  if OO0OOO0OOO0O00OO0 =="Android":#line:498
    O000OO0OO000O0O00 ="13"#line:499
    OOOOO0O0OOOOOO0OO =f"Linux; Android 13; Pixel 6a"#line:500
    O00OOO000OOO00O00 ="aarch64"#line:501
  OOO000OOOO000O0O0 ={"os":OO0OOO0OOO0O00OO0 ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":O000OO0OO000O0O00 ,"os_arch":O00OOO000OOO00O00 ,"system_locale":"ja-JP","client_build_number":O0O000OO0O00O0O00 ,"client_event_source":None ,"design_id":0 }#line:502
  OO00000OOO0000O00 =f"Mozilla/5.0 ({OOOOO0O0OOOOOO0OO}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:503
  return base64 .b64encode (json .dumps (OOO000OOOO000O0O0 ,separators =(',',':')).encode ()).decode (),OO00000OOO0000O00 #line:504
import base64 #line:506
def nickchanger ():#line:509
    try :#line:510
        with open ("token.txt")as O00O0OOOO00O0000O :#line:511
            OO000OOO00O00O0O0 =[OO0000O000OOOOOOO .strip ()for OO0000O000OOOOOOO in O00O0OOOO00O0000O .readlines ()if OO0000O000OOOOOOO .strip ()]#line:512
    except (FileNotFoundError ,KeyError ):#line:513
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:514
        return #line:515
    OO00O0O0O000000O0 =input ("Server ID?: ").strip ()#line:517
    O000O0O0O0OO0O000 =input ("Nickname?: ").strip ()#line:518
    OOOO0OO000000O00O =input ("Delay (in seconds)?: ").strip ()#line:519
    try :#line:521
        OOOO0OO000000O00O =float (OOOO0OO000000O00O )#line:522
        if OOOO0OO000000O00O <0 :#line:523
            raise ValueError #line:524
    except ValueError :#line:525
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:526
        OOOO0OO000000O00O =1.0 #line:527
    for OO0OOO0O0OOOO0000 in OO000OOO00O00O0O0 :#line:529
        O0OO0O0O0OOOOO000 ={"Authorization":OO0OOO0O0OOOO0000 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:534
        O000000O0000OOO00 ={"nick":O000O0O0O0OO0O000 }#line:535
        OOOOO000000OOOOO0 =requests .patch (f"https://discord.com/api/v9/guilds/{OO00O0O0O000000O0}/members/@me",headers =O0OO0O0O0OOOOO000 ,json =O000000O0000OOO00 )#line:536
        if OOOOO000000OOOOO0 .status_code ==200 :#line:538
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Nickname changed to '{O000O0O0O0OO0O000}' successfully for token {OO0OOO0O0OOOO0000}.{colorama.Fore.RESET}")#line:539
        elif OOOOO000000OOOOO0 .status_code ==429 :#line:540
            print (f"{colorama.Fore.RED}    [!] Rate limited. Please wait before retrying for token {OO0OOO0O0OOOO0000}.{colorama.Fore.RESET}")#line:541
            O00OO0O0O0O000OOO =OOOOO000000OOOOO0 .json ().get ("retry_after",1 )#line:542
            time .sleep (O00OO0O0O0O000OOO )#line:543
        else :#line:544
            print (f"{colorama.Fore.RED}    [!] Error occurred: {OOOOO000000OOOOO0.status_code} for token {OO0OOO0O0OOOO0000}.{colorama.Fore.RESET}")#line:545
        time .sleep (OOOO0OO000000O00O )#line:547
import json ,websocket ,threading ,tls_client ,random ,time #line:551
session =tls_client .Session (client_identifier ="chrome112",random_tls_extension_order =True )#line:553
class Utils :#line:555
    @staticmethod #line:556
    def rangeCorrector (O000OOOO0O00OO0O0 ):#line:557
        if [0 ,99 ]not in O000OOOO0O00OO0O0 :#line:558
            O000OOOO0O00OO0O0 .insert (0 ,[0 ,99 ])#line:559
        return O000OOOO0O00OO0O0 #line:560
    @staticmethod #line:562
    def getRanges (O00O0OOO0OOO00000 ,OOOO00OOO0OOOOO0O ,OOOO0OOOOO0O000OO ):#line:563
        O00OO0000OO00OO0O =int (O00O0OOO0OOO00000 *OOOO00OOO0OOOOO0O )#line:564
        O0OO0O0O00O000O00 =[[O00OO0000OO00OO0O ,O00OO0000OO00OO0O +99 ]]#line:565
        if OOOO0OOOOO0O000OO >O00OO0000OO00OO0O +99 :#line:566
            O0OO0O0O00O000O00 .append ([O00OO0000OO00OO0O +100 ,O00OO0000OO00OO0O +199 ])#line:567
        return Utils .rangeCorrector (O0OO0O0O00O000O00 )#line:568
    @staticmethod #line:570
    def parseGuildMemberListUpdate (OOOOOOO00OO0OO0OO ):#line:571
        O0O000OO0O0O0O0O0 ={"online_count":OOOOOOO00OO0OO0OO ["d"]["online_count"],"member_count":OOOOOOO00OO0OO0OO ["d"]["member_count"],"id":OOOOOOO00OO0OO0OO ["d"]["id"],"guild_id":OOOOOOO00OO0OO0OO ["d"]["guild_id"],"hoisted_roles":OOOOOOO00OO0OO0OO ["d"]["groups"],"types":[],"locations":[],"updates":[],}#line:581
        for O00000OO0O000O000 in OOOOOOO00OO0OO0OO ["d"]["ops"]:#line:583
            O0O000OO0O0O0O0O0 ["types"].append (O00000OO0O000O000 ["op"])#line:584
            if O00000OO0O000O000 ["op"]in ("SYNC","INVALIDATE"):#line:585
                O0O000OO0O0O0O0O0 ["locations"].append (O00000OO0O000O000 ["range"])#line:586
                if O00000OO0O000O000 ["op"]=="SYNC":#line:587
                    O0O000OO0O0O0O0O0 ["updates"].append (O00000OO0O000O000 ["items"])#line:588
                else :#line:589
                    O0O000OO0O0O0O0O0 ["updates"].append ([])#line:590
            elif O00000OO0O000O000 ["op"]in ("INSERT","UPDATE","DELETE"):#line:591
                O0O000OO0O0O0O0O0 ["locations"].append (O00000OO0O000O000 ["index"])#line:592
                if O00000OO0O000O000 ["op"]=="DELETE":#line:593
                    O0O000OO0O0O0O0O0 ["updates"].append ([])#line:594
                else :#line:595
                    O0O000OO0O0O0O0O0 ["updates"].append (O00000OO0O000O000 ["item"])#line:596
        return O0O000OO0O0O0O0O0 #line:597
class DiscordSocket (websocket .WebSocketApp ):#line:599
    def __init__ (OO0O00OOO00OOO0OO ,O000OOO0O00O00000 ,O0O00O00OOOOOO00O ,O0O0O0OO00O0OOO0O ):#line:600
        OO0O00OOO00OOO0OO .token =O000OOO0O00O00000 #line:601
        OO0O00OOO00OOO0OO .guild_id =O0O00O00OOOOOO00O #line:602
        OO0O00OOO00OOO0OO .channel_id =O0O0O0OO00O0OOO0O #line:603
        OO0O00OOO00OOO0OO .socket_headers ={"Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","Cache-Control":"no-cache","Pragma":"no-cache","Sec-WebSocket-Extensions":"permessage-deflate; client_max_window_bits","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",}#line:611
        super ().__init__ ("wss://gateway.discord.gg/?encoding=json&v=9",header =OO0O00OOO00OOO0OO .socket_headers ,on_open =lambda OO0O00000OO0O00O0 :OO0O00OOO00OOO0OO .sock_open (OO0O00000OO0O00O0 ),on_message =lambda O0OOO00OOO0O0OOOO ,OO0OO00O0000O0000 :OO0O00OOO00OOO0OO .sock_message (O0OOO00OOO0O0OOOO ,OO0OO00O0000O0000 ),on_close =lambda OO0OOO0OOO00OOO00 ,O00O000O0000000OO ,O00OO0O0OOOOOOOOO :OO0O00OOO00OOO0OO .sock_close (OO0OOO0OOO00OOO00 ,O00O000O0000000OO ,O00OO0O0OOOOOOOOO ),)#line:620
        OO0O00OOO00OOO0OO .endScraping =False #line:622
        OO0O00OOO00OOO0OO .guilds ={}#line:623
        OO0O00OOO00OOO0OO .members ={}#line:624
        OO0O00OOO00OOO0OO .ranges =[[0 ,0 ]]#line:625
        OO0O00OOO00OOO0OO .lastRange =0 #line:626
        OO0O00OOO00OOO0OO .packets_recv =0 #line:627
    def run (O00OO0000OOOOOO0O ):#line:629
        O00OO0000OOOOOO0O .run_forever ()#line:630
        return O00OO0000OOOOOO0O .members #line:631
    def scrapeUsers (OOO0O0O0OOO0OO0O0 ):#line:633
        if not OOO0O0O0OOO0OO0O0 .endScraping :#line:634
            OOO0O0O0OOO0OO0O0 .send ('{"op":14,"d":{"guild_id":"'+OOO0O0O0OOO0OO0O0 .guild_id +'","typing":true,"activities":true,"threads":true,"channels":{"'+OOO0O0O0OOO0OO0O0 .channel_id +'":'+json .dumps (OOO0O0O0OOO0OO0O0 .ranges )+"}}}")#line:643
    def sock_open (O0O00O0O0OO0000O0 ,OOOO0OO00O00OO0O0 ):#line:645
        O0O00O0O0OO0000O0 .send ('{"op":2,"d":{"token":"'+O0O00O0O0OO0000O0 .token +'","capabilities":125,"properties":{"os":"Windows NT","browser":"Chrome","device":"","system_locale":"it-IT","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36","browser_version":"119.0","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":103981,"client_event_source":null},"presence":{"status":"online","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}')#line:650
    def heartbeatThread (OO00OO00000OOO0O0 ,O0OO000O0O0OO0O00 ):#line:652
        try :#line:653
            while True :#line:654
                OO00OO00000OOO0O0 .send ('{"op":1,"d":'+str (OO00OO00000OOO0O0 .packets_recv )+"}")#line:655
                time .sleep (O0OO000O0O0OO0O00 )#line:656
        except Exception as O0O0OO0O0OO0OO0OO :#line:657
            pass #line:658
    def sock_message (OO0OO000000O0O000 ,OOOOO0O0O0OO0OO00 ,O00OOO0O00O000OOO ):#line:660
        O00O0OO00O0O0O0O0 =json .loads (O00OOO0O00O000OOO )#line:661
        if O00O0OO00O0O0O0O0 is None :#line:662
            return #line:663
        if O00O0OO00O0O0O0O0 ["op"]!=11 :#line:664
            OO0OO000000O0O000 .packets_recv +=1 #line:665
        if O00O0OO00O0O0O0O0 ["op"]==10 :#line:666
            threading .Thread (target =OO0OO000000O0O000 .heartbeatThread ,args =(O00O0OO00O0O0O0O0 ["d"]["heartbeat_interval"]/1000 ,),daemon =True ,).start ()#line:671
        if O00O0OO00O0O0O0O0 ["t"]=="READY":#line:672
            for O00OOOOO0000O00OO in O00O0OO00O0O0O0O0 ["d"]["guilds"]:#line:673
                OO0OO000000O0O000 .guilds [O00OOOOO0000O00OO ["id"]]={"member_count":O00OOOOO0000O00OO ["member_count"]}#line:674
        if O00O0OO00O0O0O0O0 ["t"]=="READY_SUPPLEMENTAL":#line:675
            OO0OO000000O0O000 .ranges =Utils .getRanges (0 ,100 ,OO0OO000000O0O000 .guilds [OO0OO000000O0O000 .guild_id ]["member_count"])#line:678
            OO0OO000000O0O000 .scrapeUsers ()#line:679
        elif O00O0OO00O0O0O0O0 ["t"]=="GUILD_MEMBER_LIST_UPDATE":#line:680
            OOO0O0OOO000000O0 =Utils .parseGuildMemberListUpdate (O00O0OO00O0O0O0O0 )#line:681
            if OOO0O0OOO000000O0 ["guild_id"]==OO0OO000000O0O000 .guild_id and ("SYNC"in OOO0O0OOO000000O0 ["types"]or "UPDATE"in OOO0O0OOO000000O0 ["types"]):#line:685
                for O0OO0O00O000O0O00 ,O000OO0OOOOOOOOOO in enumerate (OOO0O0OOO000000O0 ["types"]):#line:686
                    if O000OO0OOOOOOOOOO =="SYNC":#line:687
                        if len (OOO0O0OOO000000O0 ["updates"][O0OO0O00O000O0O00 ])==0 :#line:688
                            OO0OO000000O0O000 .endScraping =True #line:689
                            break #line:690
                        for O0OO00OO000O0OO0O in OOO0O0OOO000000O0 ["updates"][O0OO0O00O000O0O00 ]:#line:692
                            if "member"in O0OO00OO000O0OO0O :#line:693
                                O00OOOO00OOO0O0O0 =O0OO00OO000O0OO0O ["member"]#line:694
                                OOO000O0O0O00OO0O ={"tag":O00OOOO00OOO0O0O0 ["user"]["username"]+"#"+O00OOOO00OOO0O0O0 ["user"]["discriminator"],"id":O00OOOO00OOO0O0O0 ["user"]["id"],}#line:700
                                if not O00OOOO00OOO0O0O0 ["user"].get ("bot"):#line:701
                                    OO0OO000000O0O000 .members [O00OOOO00OOO0O0O0 ["user"]["id"]]=OOO000O0O0O00OO0O #line:702
                    elif O000OO0OOOOOOOOOO =="UPDATE":#line:704
                        for O0OO00OO000O0OO0O in OOO0O0OOO000000O0 ["updates"][O0OO0O00O000O0O00 ]:#line:705
                            if "member"in O0OO00OO000O0OO0O :#line:706
                                O00OOOO00OOO0O0O0 =O0OO00OO000O0OO0O ["member"]#line:707
                                OOO000O0O0O00OO0O ={"tag":O00OOOO00OOO0O0O0 ["user"]["username"]+"#"+O00OOOO00OOO0O0O0 ["user"]["discriminator"],"id":O00OOOO00OOO0O0O0 ["user"]["id"],}#line:713
                                if not O00OOOO00OOO0O0O0 ["user"].get ("bot"):#line:714
                                    OO0OO000000O0O000 .members [O00OOOO00OOO0O0O0 ["user"]["id"]]=OOO000O0O0O00OO0O #line:715
                    OO0OO000000O0O000 .lastRange +=1 #line:717
                    OO0OO000000O0O000 .ranges =Utils .getRanges (OO0OO000000O0O000 .lastRange ,100 ,OO0OO000000O0O000 .guilds [OO0OO000000O0O000 .guild_id ]["member_count"])#line:720
                    time .sleep (0.45 )#line:721
                    OO0OO000000O0O000 .scrapeUsers ()#line:722
            if OO0OO000000O0O000 .endScraping :#line:724
                OO0OO000000O0O000 .close ()#line:725
    def sock_close (O000O0O0OO0O0O0O0 ,O00O00000O00OO0OO ,O00OOO0O00O000000 ,O0O0O0O0OO000O0OO ):#line:727
        pass #line:728
def scrape (OO00O0OO0OO00OOOO ,OOOOOOOO0OOOOOO0O ,O0O000OOO000OOOOO ):#line:730
    OOO00O0OO00O0O000 =DiscordSocket (OO00O0OO0OO00OOOO ,OOOOOOOO0OOOOOO0O ,O0O000OOO000OOOOO )#line:731
    return OOO00O0OO00O0O000 .run ()#line:732
def member_scrape (O0OOOO0OO0OOO00O0 ,O00O00000O0O00OO0 ,OOO0000O00OO000OO ):#line:734
    OO000OO0O0O0O00O0 =[]#line:735
    for OOO0O000OO0O0O0O0 in O0OOOO0OO0OOO00O0 :#line:736
        OOOO00O0000OO0OO0 ={"Authorization":OOO0O000OO0O0O0O0 ,"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}#line:737
        OO00OOO000OO0O0OO =session .get (f"https://canary.discord.com/api/v9/guilds/{O00O00000O0O00OO0}",headers =OOOO00O0000OO0OO0 )#line:738
        if OO00OOO000OO0O0OO .status_code ==200 :#line:739
            OO000OO0O0O0O00O0 .append (OOO0O000OO0O0O0O0 )#line:740
            break #line:741
    if not OO000OO0O0O0O00O0 :#line:742
        print ("missing access")#line:743
    OOO0O000OO0O0O0O0 =random .choice (OO000OO0O0O0O00O0 )#line:745
    OO00000O00O00OO00 =scrape (OOO0O000OO0O0O0O0 ,O00O00000O0O00OO0 ,OOO0000O00OO000OO )#line:746
    O0O0O0OO0OO0OOOO0 =[f"<@{OO0O00O00OOOOOOO0}>"for OO0O00O00OOOOOOO0 in [int (O0O0000OOO0OO0000 )for O0O0000OOO0OO0000 in OO00000O00O00OO00 .keys ()]]#line:747
    print (f"[SUCCESS] {len(O0O0O0OO0OO0OOOO0)} scraped members")#line:748
    return O0O0O0OO0OO0OOOO0 #line:749
def spammer_menu ():#line:751
    try :#line:752
        with open ("token.txt")as O00O0O00O00OO0000 :#line:753
            OO0O000OOO0000OOO =[OOO0OOO0OOOOO0OO0 .strip ()for OOO0OOO0OOOOO0OO0 in O00O0O00O00OO0000 .readlines ()if OOO0OOO0OOOOO0OO0 .strip ()]#line:754
    except (FileNotFoundError ,KeyError ):#line:755
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:756
        return #line:757
    O0O00OO0O0OOO0000 =input ("Server ID?: ").strip ()#line:759
    OO0O00OO0OO00O0O0 =input ("Message?: ").strip ()#line:760
    O0OO0OOO00OOOOO0O =input ("Random mention (True/False)?: ").strip ().lower ()=='true'#line:761
    O00OO0OO00O0O000O =input ("Delay between messages (in seconds)?: ").strip ()#line:762
    OOO000000OO0O0OOO =input ("Number of messages to send?: ").strip ()#line:763
    OO00OO000OO000O0O =input ("Blacklist User IDs (comma-separated) (Leave blank to skip)?: ").strip ().split (',')#line:764
    OO00OO000OO000O0O =[f"<@{OO00O0OO00O0O0000.strip()}>"for OO00O0OO00O0O0000 in OO00OO000OO000O0O if OO00O0OO00O0O0000 .strip ()]#line:765
    try :#line:767
        O00OO0OO00O0O000O =float (O00OO0OO00O0O000O )#line:768
        if O00OO0OO00O0O000O <0 :#line:769
            raise ValueError #line:770
    except ValueError :#line:771
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:772
        O00OO0OO00O0O000O =1.0 #line:773
    try :#line:775
        OOO000000OO0O0OOO =int (OOO000000OO0O0OOO )#line:776
        if OOO000000OO0O0OOO <=0 :#line:777
            raise ValueError #line:778
    except ValueError :#line:779
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:780
        OOO000000OO0O0OOO =1 #line:781
    OO00OOOO0000O0000 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:783
    if OO00OOOO0000O0000 =='2':#line:784
        OO00OOOO00O0O0O00 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:785
        OO00OOOO00O0O0O00 =[OOOOO00000O00OOOO .strip ()for OOOOO00000O00OOOO in OO00OOOO00O0O0O00 if OOOOO00000O00OOOO .strip ()]#line:786
    else :#line:787
        OO00OOOO00O0O0O00 =fetch_channels (OO0O000OOO0000OOO [0 ],O0O00OO0O0OOO0000 )#line:788
    O0OOOO0O0OOOO0000 =None #line:790
    spammer (OO0O000OOO0000OOO ,O0O00OO0O0OOO0000 ,OO00OOOO00O0O0O00 ,OO0O00OO0OO00O0O0 ,O0OO0OOO00OOOOO0O ,OO00OO000OO000O0O ,O0OOOO0O0OOOO0000 ,OOO000000OO0O0OOO )#line:792
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:794
def spammer (OOOOO00OOO0OO0OO0 ,O0OO0O0OO0000O0OO ,OOO0OOO00OO00O000 ,O0OOOOO000OO000O0 ,OOOO0O0OOOOO0OO00 ,O0OOO0000OO00OO0O ,O0OOOOOOO0OOO0OOO ,O0000OO000O000OO0 ):#line:796
    O0O000O0OO0OO0O00 =get_session (O0OOOOOOO0OOO0OOO )#line:797
    O0000OO0O0O00O0OO =0 #line:798
    O00000O0O0OO0000O =member_scrape (OOOOO00OOO0OO0OO0 ,O0OO0O0OO0000O0OO ,OOO0OOO00OO00O000 [0 ])#line:800
    O00000O0O0OO0000O =[OOO0OO0OO00O0OOOO for OOO0OO0OO00O0OOOO in O00000O0O0OO0000O if OOO0OO0OO00O0OOOO not in O0OOO0000OO00OO0O ]#line:801
    for _OOOO0O000OO0OOOOO in range (O0000OO000O000OO0 ):#line:803
        OO0OO000O00OOOOO0 =OOOOO00OOO0OO0OO0 [O0000OO0O0O00O0OO ]#line:804
        OO00OO0O0O00OOOOO =get_headers (OO0OO000O00OOOOO0 )#line:805
        for O0OO000O0000O00OO in OOO0OOO00OO00O000 :#line:806
            O00O0O000O00OOOO0 =O0OOOOO000OO000O0 #line:807
            if OOOO0O0OOOOO0OO00 and O00000O0O0OO0000O :#line:808
                OOOO00OO0OO00000O =random .choice (O00000O0O0OO0000O )#line:809
                O00O0O000O00OOOO0 +=f" {OOOO00OO0OO00000O}"#line:810
            OOO00OOOOO00OO00O =O0O000O0OO0OO0O00 .post (f"https://discord.com/api/v9/channels/{O0OO000O0000O00OO}/messages",json ={"content":O00O0O000O00OOOO0 },headers =OO00OO0O0O00OOOOO )#line:812
            if OOO00OOOOO00OO00O .status_code ==200 :#line:813
                print (f"200 message sent: {OO0OO000O00OOOOO0}")#line:814
            elif OOO00OOOOO00OO00O .status_code ==429 :#line:815
                print (f"429 rate limit: {OO0OO000O00OOOOO0}")#line:816
                O00OOOOOO000O000O =OOO00OOOOO00OO00O .json ().get ("retry_after",1 )#line:817
                time .sleep (O00OOOOOO000O000O )#line:818
            elif OOO00OOOOO00OO00O .status_code ==401 :#line:819
                print (f"401 unknown token: {OO0OO000O00OOOOO0}")#line:820
            else :#line:821
                print (f"error: {OO0OO000O00OOOOO0}")#line:822
        O0000OO0O0O00O0OO =(O0000OO0O0O00O0OO +1 )%len (OOOOO00OOO0OO0OO0 )#line:824
        time .sleep (1 )#line:825
def main ():#line:830
    colorama .init ()#line:831
    while True :#line:832
        logo ()#line:833
        OOO0000OO0OOOO00O =input (f"{colorama.Fore.LIGHTMAGENTA_EX}    [Final] Select an option from above: ")#line:834
        if OOO0000OO0OOOO00O =="0":#line:836
            update_group_ids ()#line:837
        elif OOO0000OO0OOOO00O =="1":#line:838
            join_discord_invite ()#line:839
        elif OOO0000OO0OOOO00O =="2":#line:840
            reaction_spammer ()#line:841
        elif OOO0000OO0OOOO00O =="3":#line:842
            send_messages_with_mentions ()#line:843
        elif OOO0000OO0OOOO00O =="5":#line:844
            nickchanger ()#line:845
        elif OOO0000OO0OOOO00O =="4":#line:846
            spammer_menu ()#line:847
        elif OOO0000OO0OOOO00O =="0":#line:848
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [*] Exiting the application. Goodbye!{colorama.Fore.RESET}")#line:849
            break #line:850
        else :#line:851
            print (f"{colorama.Fore.RED}    [!] Invalid option selected!{colorama.Fore.RESET}")#line:852
        input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:854
if __name__ =="__main__":#line:856
    main ()#line:857
