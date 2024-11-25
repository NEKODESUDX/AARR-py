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
    OO0OO0000OO0OOOO0 =requests .Session ()#line:55
    if proxy :#line:56
        OO0OO0000OO0OOOO0 .proxies ={"http":proxy ,"https":proxy }#line:57
    return OO0OO0000OO0OOOO0 #line:58
def get_headers (OOO0O0O0O0OOOOO0O ):#line:60
    return {"Authorization":OOO0O0O0O0OOOOO0O ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:65
def send_message_with_mention (O00O0OO0O0O00OOO0 ,O0O00000000OO0OO0 ,O0O0O000OOO0OOOO0 ,O00OO00OOOOO0OOO0 ):#line:68
    OO00O0O0OOO0O0000 =get_session ()#line:69
    O0000OOOO00OO0000 =get_headers (O00O0OO0O0O00OOO0 )#line:70
    if O00OO00OOOOO0OOO0 :#line:72
        O0OOO0OOOOO0OOOOO =random .choice (O00OO00OOOOO0OOO0 )#line:73
        O0O0O000OOO0OOOO0 +=f" <@{O0OOO0OOOOO0OOOOO}>"#line:74
    OO0O00OO0000O0O00 =OO00O0O0OOO0O0000 .post (f"https://discord.com/api/v9/channels/{O0O00000000OO0OO0}/messages",headers =O0000OOOO00OO0000 ,json ={"content":O0O0O000OOO0OOOO0 })#line:80
    if OO0O00OO0000O0O00 .status_code in [200 ,201 ]:#line:81
        print (f"[+] Message sent to channel {O0O00000000OO0OO0}")#line:82
    elif OO0O00OO0000O0O00 .status_code ==429 :#line:83
        print ("[-] Rate limited. Please wait before retrying.")#line:84
        O000OO00O00O0O0O0 =OO0O00OO0000O0O00 .json ().get ("retry_after",1 )#line:85
        time .sleep (O000OO00O00O0O0O0 )#line:86
    else :#line:87
        print (f"[!] Error occurred: {OO0O00OO0000O0O00.status_code}")#line:88
def fetch_messages (O0O0O00OO0OOO0OO0 ,O0O0O0000OOO0O000 ,limit =100 ):#line:91
    OO00O0O00O00O00O0 ={"Authorization":O0O0O00OO0OOO0OO0 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:96
    OOOO0O00OOO0OOOO0 =requests .get (f"https://discord.com/api/v9/channels/{O0O0O0000OOO0O000}/messages?limit={limit}",headers =OO00O0O00O00O00O0 )#line:100
    if OOOO0O00OOO0OOOO0 .status_code ==200 :#line:101
        return OOOO0O00OOO0OOOO0 .json ()#line:102
    else :#line:103
        print (f"[!] Failed to fetch messages. HTTP Status Code: {OOOO0O00OOO0OOOO0.status_code}")#line:104
        return []#line:105
def reaction_spammer ():#line:106
    try :#line:107
        with open ("token.txt")as O0O0O000OO00OO0O0 :#line:108
            OOOO000OOOOO0OO0O =[OOO0O0OO00OOO00O0 .strip ()for OOO0O0OO00OOO00O0 in O0O0O000OO00OO0O0 .readlines ()if OOO0O0OO00OOO00O0 .strip ()]#line:109
    except (FileNotFoundError ,KeyError ):#line:110
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:111
        return #line:112
    O0O00O0O0O00000OO =input ("Server ID?: ").strip ()#line:114
    OOOOO0O00O00O000O =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:116
    if OOOOO0O00O00O000O =='2':#line:117
        OO0OO00OO00000OOO =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:118
        O00OOO0OOOO00OOO0 =[O000O0OOOOO0OO00O .strip ()for O000O0OOOOO0OO00O in OO0OO00OO00000OOO if O000O0OOOOO0OO00O .strip ()]#line:119
    else :#line:120
        O00OOO0OOOO00OOO0 =[]#line:121
        for O0OOOO0O0000OOOOO in OOOO000OOOOO0OO0O :#line:122
            try :#line:123
                O00OOO0OOOO00OOO0 .extend (fetch_channels (O0OOOO0O0000OOOOO ,O0O00O0O0O00000OO ))#line:124
            except Exception as O00OO00OO0OO0000O :#line:125
                print (f"[!] Failed to fetch channels for token. Error: {O00OO00OO0OO0000O}")#line:126
                continue #line:127
    O0O0OO0000OOO000O =input ("Select your emoji (a, b, c, ... or custom emojis): ").strip ()#line:129
    O000OOO0O00OOO0OO =input ("Delay between reactions (in seconds)?: ").strip ()#line:130
    try :#line:132
        O000OOO0O00OOO0OO =float (O000OOO0O00OOO0OO )#line:133
        if O000OOO0O00OOO0OO <0 :#line:134
            raise ValueError #line:135
    except ValueError :#line:136
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:137
        O000OOO0O00OOO0OO =1.0 #line:138
    OO00O00O000O0O0OO =[]#line:140
    for OO0OO00O000O00000 in O0O0OO0000OOO000O .split (","):#line:141
        OO0OO00O000O00000 =OO0OO00O000O00000 .strip ().lower ()#line:142
        if OO0OO00O000O00000 in alphabet_to_flag :#line:143
            OO00O00O000O0O0OO .append (alphabet_to_flag [OO0OO00O000O00000 ])#line:144
        else :#line:145
            OO00O00O000O0O0OO .append (OO0OO00O000O00000 )#line:146
    if not OO00O00O000O0O0OO :#line:148
        print (f"{colorama.Fore.RED}    [!] No valid emojis provided!{colorama.Fore.RESET}")#line:149
        return #line:150
    for O0OOOO0O0000OOOOO in OOOO000OOOOO0OO0O :#line:152
        for OO00O00OOOO0OOO0O in O00OOO0OOOO00OOO0 :#line:153
            try :#line:154
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {OO00O00OOOO0OOO0O}...{colorama.Fore.RESET}")#line:155
                OO0000O00OO000O0O =fetch_messages (O0OOOO0O0000OOOOO ,OO00O00OOOO0OOO0O ,limit =100 )#line:156
                if not OO0000O00OO000O0O :#line:157
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:158
                    continue #line:159
                for OO0OOO0OO00O00OO0 in OO0000O00OO000O0O :#line:161
                    for OO0OO00O000O00000 in OO00O00O000O0O0OO :#line:162
                        reactionput (O0OOOO0O0000OOOOO ,OO00O00OOOO0OOO0O ,OO0OOO0OO00O00OO0 ['id'],OO0OO00O000O00000 )#line:163
                        time .sleep (O000OOO0O00OOO0OO )#line:164
            except Exception as O00OO00OO0OO0000O :#line:165
                print (f"[!] Error processing channel {OO00O00OOOO0OOO0O}. Error: {O00OO00OO0OO0000O}")#line:166
                continue #line:167
def update_group_ids ():#line:169
    try :#line:170
        with open ("token.txt")as O0O0000O0O0O00OO0 :#line:171
            O000O0OO00OOOO00O =[OO0OO0OOOOOOOO0O0 .strip ()for OO0OO0OOOOOOOO0O0 in O0O0000O0O0O00OO0 .readlines ()if OO0OO0OOOOOOOO0O0 .strip ()]#line:172
        O00OOOO00000O0O0O =O000O0OO00OOOO00O [0 ]#line:173
    except (FileNotFoundError ,KeyError ):#line:174
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:175
        return #line:176
    OOO0O0O0O00O0OOO0 ={"Authorization":O00OOOO00000O0O0O ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:182
    O0OO0OOOOO000000O =requests .get ('https://discord.com/api/v9/users/@me/channels',headers =OOO0O0O0O00O0OOO0 )#line:184
    if O0OO0OOOOO000000O .status_code ==200 :#line:185
        O0OOO0OOO0OO00000 =O0OO0OOOOO000000O .json ()#line:186
        with open ("group_id.txt","w")as OOO00O0O00OOOO0OO :#line:187
            for O0O00O00OO00O0O00 in O0OOO0OOO0OO00000 :#line:188
                if O0O00O00OO00O0O00 ['type']==3 :#line:189
                    OOO00O0O00OOOO0OO .write (O0O00O00OO00O0O00 ['id']+'\n')#line:190
        print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Group IDs updated successfully.{colorama.Fore.RESET}")#line:191
    else :#line:192
        print (f"{colorama.Fore.LIGHTRED_EX}    [!] Failed to retrieve group IDs. HTTP Status Code: {O0OO0OOOOO000000O.status_code}{colorama.Fore.RESET}")#line:193
import requests #line:195
import requests #line:197
def fetch_channels (OO0000O00OOO00O00 ,O000O0OOOOOOO0OOO ):#line:199
    try :#line:200
        OO0O000O00O0O0OOO =requests .Session ()#line:201
        O0OO0O0O0OO000O0O =get_headers (OO0000O00OOO00O00 )#line:202
        O0O0O00O0OOOO0OO0 =OO0O000O00O0O0OOO .get (f"https://discord.com/api/v9/guilds/{O000O0OOOOOOO0OOO}/channels",headers =O0OO0O0O0OO000O0O ,timeout =10 )#line:209
        if O0O0O00O0OOOO0OO0 .status_code ==200 :#line:212
            try :#line:213
                OO00O0OOO0OO0O0OO =O0O0O00O0OOOO0OO0 .json ()#line:214
                return [OO00OOO0O0O0O000O ['id']for OO00OOO0O0O0O000O in OO00O0OOO0OO0O0OO if OO00OOO0O0O0O000O .get ('type')==0 ]#line:215
            except ValueError :#line:216
                print ("[!] Error: Response was not valid JSON.")#line:217
                return []#line:218
        elif O0O0O00O0OOOO0OO0 .status_code ==401 :#line:219
            print ("[!] Error: Unauthorized - check your token.")#line:220
        elif O0O0O00O0OOOO0OO0 .status_code ==403 :#line:221
            print ("[!] Error: Forbidden - you lack permissions.")#line:222
        elif O0O0O00O0OOOO0OO0 .status_code ==404 :#line:223
            print ("[!] Error: Server not found - check the server ID.")#line:224
        else :#line:225
            print (f"[!] Error: Unexpected status code {O0O0O00O0OOOO0OO0.status_code}.")#line:226
        return []#line:229
    except requests .exceptions .Timeout :#line:231
        print ("[!] Error: Request timed out. Check your connection or try again later.")#line:232
        return []#line:233
    except requests .exceptions .RequestException as OOOOO0OO0O0OO00OO :#line:234
        print (f"[!] Error: An error occurred while fetching channels: {OOOOO0OO0O0OO00OO}")#line:235
        return []#line:236
def extract_uids_from_messages (O0O0O0O00O0OO0000 ):#line:242
    OO0OOOO00OO000000 =set ()#line:243
    for O0O0O0OOO0OOO00O0 in O0O0O0O00O0OO0000 :#line:244
        OO0OOOO00OO000000 .add (O0O0O0OOO0OOO00O0 ['author']['id'])#line:245
    return list (OO0OOOO00OO000000 )#line:246
def send_message_with_mention (OO0OOOOOO0OO00O0O ,O0000OOO0O0OO00O0 ,O000O00O0O0O0O000 ,O000OOO0OO0000OOO ):#line:248
    O0000OOOOOOOOOOOO =get_session ()#line:249
    OOO00OOO0O0O0OOOO =get_headers (OO0OOOOOO0OO00O0O )#line:250
    if O000OOO0OO0000OOO :#line:252
        O00000O0O0OOO0OOO =random .choice (O000OOO0OO0000OOO )#line:253
        O000O00O0O0O0O000 +=f" <@{O00000O0O0OOO0OOO}>"#line:254
    O0OO0OO000000O00O =O0000OOOOOOOOOOOO .post (f"https://discord.com/api/v9/channels/{O0000OOO0O0OO00O0}/messages",headers =OOO00OOO0O0O0OOOO ,json ={"content":O000O00O0O0O0O000 })#line:260
    if O0OO0OO000000O00O .status_code in [200 ,201 ]:#line:261
        print (f"[+] Message sent to channel {O0000OOO0O0OO00O0}")#line:262
    elif O0OO0OO000000O00O .status_code ==429 :#line:263
        print ("[-] Rate limited. Please wait before retrying.")#line:264
        OO0OOOO0O00OOOO0O =O0OO0OO000000O00O .json ().get ("retry_after",1 )#line:265
        time .sleep (OO0OOOO0O00OOOO0O )#line:266
    else :#line:267
        print (f"[!] Error occurred: {O0OO0OO000000O00O.status_code}")#line:268
def send_messages_with_mentions ():#line:269
    try :#line:270
        with open ("token.txt")as O00OO0OO0O000O00O :#line:271
            OOO0O0O0OO00O000O =[O00OO0OOO0OOO000O .strip ()for O00OO0OOO0OOO000O in O00OO0OO0O000O00O .readlines ()if O00OO0OOO0OOO000O .strip ()]#line:272
    except (FileNotFoundError ,KeyError ):#line:273
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:274
        return #line:275
    O0O000OOO000O0O0O =input ("Server ID?: ").strip ()#line:277
    O0O000O0O00OOO0O0 =input ("Delay between messages (in seconds)?: ").strip ()#line:278
    O0OOOOOOO00000000 =input ("Number of messages to send?: ").strip ()#line:279
    OO00OOOOOOOOO00O0 =input ("Message content?: ").strip ()#line:280
    OOO000O000O00OO0O =input ("Blacklist User IDs (comma-separated)?: ").strip ().split (',')#line:281
    OOO000O000O00OO0O =[OO0OOOOOO0OOO0OO0 .strip ()for OO0OOOOOO0OOO0OO0 in OOO000O000O00OO0O if OO0OOOOOO0OOO0OO0 .strip ()]#line:282
    try :#line:284
        O0O000O0O00OOO0O0 =float (O0O000O0O00OOO0O0 )#line:285
        if O0O000O0O00OOO0O0 <0 :#line:286
            raise ValueError #line:287
    except ValueError :#line:288
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:289
        O0O000O0O00OOO0O0 =1.0 #line:290
    try :#line:292
        O0OOOOOOO00000000 =int (O0OOOOOOO00000000 )#line:293
        if O0OOOOOOO00000000 <=0 :#line:294
            raise ValueError #line:295
    except ValueError :#line:296
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:297
        O0OOOOOOO00000000 =1 #line:298
    O0O0000O0OOOO0O00 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:300
    if O0O0000O0OOOO0O00 =='2':#line:301
        O0OOOO0OOO0OO0O00 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:302
        O0OOOO0OOO0OO0O00 =[OO000000OOO0O0O0O .strip ()for OO000000OOO0O0O0O in O0OOOO0OOO0OO0O00 if OO000000OOO0O0O0O .strip ()]#line:303
    else :#line:304
        O0OOOO0OOO0OO0O00 =[]#line:305
    O00O0OO0O0000OO00 =set ()#line:307
    for OOOOO0O00O000O0OO in OOO0O0O0OO00O000O :#line:308
        O0OO0000O000O00OO =fetch_channels (OOOOO0O00O000O0OO ,O0O000OOO000O0O0O )#line:309
        if O0OOOO0OOO0OO0O00 :#line:310
            O0OO0000O000O00OO =O0OOOO0OOO0OO0O00 #line:311
        for OOO00OOOOOO0O0OO0 in O0OO0000O000O00OO :#line:312
            OO00OOOO000000OOO =fetch_messages (OOOOO0O00O000O0OO ,OOO00OOOOOO0O0OO0 ,limit =100 )#line:313
            OO00O0O00O00O0OOO =extract_uids_from_messages (OO00OOOO000000OOO )#line:314
            O00O0OO0O0000OO00 .update (OO00O0O00O00O0OOO )#line:315
    O00O0OO0O0000OO00 =list (set (O00O0OO0O0000OO00 )-set (OOO000O000O00OO0O ))#line:318
    for _OO00O0OO000O0OO0O in range (O0OOOOOOO00000000 ):#line:320
        for OOOOO0O00O000O0OO in OOO0O0O0OO00O000O :#line:321
            for OOO00OOOOOO0O0OO0 in O0OO0000O000O00OO :#line:322
                send_message_with_mention (OOOOO0O00O000O0OO ,OOO00OOOOOO0O0OO0 ,OO00OOOOOOOOO00O0 ,O00O0OO0O0000OO00 )#line:323
                time .sleep (O0O000O0O00OOO0O0 )#line:324
def join_discord_invite ():#line:328
    try :#line:329
        with open ("token.txt")as OOOO0OOOOO00000OO :#line:330
            O00O0OOO0O0000OOO =[O0O00000OOO0OOO0O .strip ()for O0O00000OOO0OOO0O in OOOO0OOOOO00000OO .readlines ()if O0O00000OOO0OOO0O .strip ()]#line:331
    except (FileNotFoundError ,KeyError ):#line:332
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:333
        return #line:334
    OO00O0OOO0O000OO0 =input ("Invite Code?: discord.gg/").strip ()#line:336
    for O0000OOOOOOOOOO0O in O00O0OOO0O0000OOO :#line:339
        joiner (O0000OOOOOOOOOO0O ,OO00O0OOO0O000OO0 )#line:340
import json ,time ,base64 ,random ,requests #line:342
def cookieset (O000OOOOO0O0OOOO0 ):#line:344
    OOO0OOO0O0O0OO0O0 =O000OOOOO0O0OOOO0 .get ("https://discord.com/app")#line:345
    return OOO0OOO0O0O0OO0O0 .cookies .get_dict ()#line:346
def generatexspandua (O0O00OOO0O00O0OOO ):#line:348
    OO0O0000O0O00O0O0 =["Android","Windows","Macintosh"]#line:349
    OO000O0OO0O0OOOOO =random .choice (OO0O0000O0O00O0O0 )#line:350
    if OO000O0OO0O0OOOOO =="Macintosh":#line:351
        O00OOO000000O0O00 =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:352
        O0OOO0OO000O00OO0 ="Macintosh; Intel Mac OS X "+O00OOO000000O0O00 #line:353
        OO00OO00O00O0OOOO ="x86_64"#line:354
    elif OO000O0OO0O0OOOOO =="Windows":#line:355
        O00OOO000000O0O00 =f'{random.choice([6.0, 10.0, 11.0])}'#line:356
        O0OOO0OO000O00OO0 ="Windows NT "+O00OOO000000O0O00 +" Win64; x64"#line:357
        OO00OO00O00O0OOOO ="x86_64"#line:358
    else :#line:359
        O00OOO000000O0O00 ="13"#line:360
        O0OOO0OO000O00OO0 =f"Linux; Android 13; Pixel 6a"#line:361
        OO00OO00O00O0OOOO ="aarch64"#line:362
    OOOOO0O0O0O0O00OO ={"os":OO000O0OO0O0OOOOO ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":O00OOO000000O0O00 ,"os_arch":OO00OO00O00O0OOOO ,"system_locale":"ja-JP","client_build_number":O0O00OOO0O00O0OOO ,"client_event_source":None ,"design_id":0 }#line:375
    OO0OOO00OO0OO0OO0 =f"Mozilla/5.0 ({O0OOO0OO000O00OO0}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:376
    return base64 .b64encode (json .dumps (OOOOO0O0O0O0O00OO ,separators =(',',':')).encode ()).decode (),OO0OOO00OO0OO0OO0 #line:377
def joiner (OOO0O00OO00OO00O0 ,O0O00OO00O0O000O0 ,O0O0OO0O0O0O00O0O ):#line:379
    O0O00O0O0O000OO0O =cookieset (O0O0OO0O0O0O00O0O )#line:380
    O0O00O0O0O000OO0O ["locale"]="ja-JP"#line:381
    O0O00OO0OOO000OOO =201211 #line:382
    O0OOO000O0O0OO0O0 ,O000O0OO00000OOO0 =generatexspandua (O0O00OO0OOO000OOO )#line:383
    O000O000O00O000O0 ={"Authorization":OOO0O00OO00OO00O0 ,"accept":"*/*","accept-language":"ja-JP","connection":"keep-alive","DNT":"1","origin":"https://discord.com","sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","referer":"https://discord.com/channels/@me","TE":"Trailers","user-agent":O000O0OO00000OOO0 ,"X-Super-Properties":O0OOO000O0O0OO0O0 ,}#line:398
    O00OO000OOO0OO0O0 =O0O0OO0O0O0O00O0O .post ("https://discord.com/api/v9/invites/"+O0O00OO00O0O000O0 ,headers =O000O000O00O000O0 ,json ={},cookies =O0O00O0O0O000OO0O )#line:399
    if O00OO000OOO0OO0O0 .status_code ==200 :#line:400
        print ("[+] join this server "+OOO0O00OO00OO00O0 )#line:401
        if "show_verification_form"in O00OO000OOO0OO0O0 .json ():#line:402
            bypass (OOO0O00OO00OO00O0 ,O00OO000OOO0OO0O0 .json ()["guild"]["id"],O0O0OO0O0O0O00O0O ,O000O000O00O000O0 )#line:403
        return #line:404
    elif "captcha_key"in O00OO000OOO0OO0O0 .text and O00OO000OOO0OO0O0 .status_code ==400 :#line:405
        print ("[!] Hcaptcha protect"+OOO0O00OO00OO00O0 )#line:406
        return #line:407
    elif O00OO000OOO0OO0O0 .status_code ==401 :#line:408
        print ("[×] token is dead"+OOO0O00OO00OO00O0 )#line:409
        return #line:410
    elif O00OO000OOO0OO0O0 .status_code ==403 :#line:411
        print ("[!] 403 banned "+OOO0O00OO00OO00O0 )#line:412
        return #line:413
    elif O00OO000OOO0OO0O0 .status_code ==429 :#line:414
        OO0O00OOOO0OO0OO0 =O00OO000OOO0OO0O0 .json ().get ("retry_after",1 )#line:415
        print (f"[!] 429 rate limit. Retrying after {OO0O00OOOO0OO0OO0} seconds.")#line:416
        time .sleep (OO0O00OOOO0OO0OO0 )#line:417
        return #line:418
    else :#line:419
        print ("[!] error "+OOO0O00OO00OO00O0 )#line:420
        return #line:421
def update_group_ids ():#line:423
    OOO00O00OO0OO0O0O =input ("Invite Code?: ").strip ()#line:424
    try :#line:425
        with open ("token.txt")as OOOO00O00OOOOO000 :#line:426
            OO0OO0000OO00OOO0 =[O000O0O0000O0O00O .strip ()for O000O0O0000O0O00O in OOOO00O00OOOOO000 .readlines ()if O000O0O0000O0O00O .strip ()]#line:427
    except (FileNotFoundError ,KeyError ):#line:428
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:429
        return #line:430
    OOOOO00O0O0O0O000 =requests .Session ()#line:432
    for OO0OOO0OO00000O00 in OO0OO0000OO00OOO0 :#line:433
        joiner (OO0OOO0OO00000O00 ,OOO00O00OO0OO0O0O ,OOOOO00O0O0O0O000 )#line:434
        time .sleep (2 )#line:435
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:437
def bypass (O0OO0O0000O00O000 ,O0OOO00O0O00OO00O ,OO0OO00OOOOO0O00O ,OOOOO0OO00OOOO0OO ):#line:440
    try :#line:441
        OOO000O0OOO00OOOO =OO0OO00OOOOO0O00O .get (f"https://discord.com/api/v9/guilds/{O0OOO00O0O00OO00O}/member-verification?with_guild=false",headers =OOOOO0OO00OOOO0OO ).json ()#line:442
        O00OO0O00O0O0000O =OO0OO00OOOOO0O00O .put (f"https://discord.com/api/v9/guilds/{O0OOO00O0O00OO00O}/requests/@me",headers =OOOOO0OO00OOOO0OO ,json =OOO000O0OOO00OOOO )#line:443
        if O00OO0O00O0O0000O .status_code ==201 :#line:444
            print (f"[+] MemberscreeningBypassed {O0OO0O0000O00O000}")#line:445
            return #line:446
        else :#line:447
            print (f"[!] Bypassが出来ませんでした {O0OO0O0000O00O000}")#line:448
            return #line:449
    except Exception as OOOO00OO0O0O000OO :#line:450
        print (f"[!] エラーが発生しました。{OOOO00OO0O0O000OO}")#line:451
session =requests .Session ()#line:453
def reactionput (O0OOOOOO000O0OO0O ,OO0000OO0O00OOOOO ,O0000O00OOOOO000O ,O0OOOOO000OOO00OO ,proxy =None ):#line:456
    OO000O0000O0O0OO0 =get_session (proxy )#line:457
    OO0OO00O0OO0O0000 =get_headers (OO000O0000O0O0OO0 )#line:458
    OO0OO00O0OO0O0000 ["Authorization"]=O0OOOOOO000O0OO0O #line:459
    O0OOOOO000OOO00OO =requests .utils .quote (O0OOOOO000OOO00OO )#line:461
    OOOO0OO0O0O0OO00O =OO000O0000O0O0OO0 .put (f"https://discord.com/api/v9/channels/{OO0000OO0O00OOOOO}/messages/{O0000O00OOOOO000O}/reactions/{O0OOOOO000OOO00OO}/%40me?location=Message&type=0",headers =OO0OO00O0OO0O0000 )#line:465
    if OOOO0OO0O0O0OO00O .status_code in [200 ,204 ]:#line:466
        print (f"[+] Reaction '{O0OOOOO000OOO00OO}' added successfully to message {O0000O00OOOOO000O}")#line:467
    elif OOOO0OO0O0O0OO00O .status_code ==429 :#line:468
        print ("[-] Rate limited. Please wait before retrying.")#line:469
        O0O0OO00O00O000O0 =OOOO0OO0O0O0OO00O .json ().get ("retry_after",1 )#line:470
        time .sleep (O0O0OO00O00O000O0 )#line:471
    elif OOOO0OO0O0O0OO00O .status_code ==401 :#line:472
        print ("[-] Invalid or expired token.")#line:473
    else :#line:474
        print (f"[!] Error occurred: {OOOO0OO0O0O0OO00O.status_code}")#line:475
def generatexspandua (OO00000OOOOO0O0O0 ):#line:478
  OOO0O0OOOO0O00O00 =["Android","Windows","Macintosh"]#line:479
  OO00OO000OOOO000O =random .choice (OOO0O0OOOO0O00O00 )#line:480
  if OO00OO000OOOO000O =="Macintosh":#line:481
    OO0000OO000OO00O0 =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:482
    O00OO0O000O0OO0OO ="Macintosh; Intel Mac OS X "+OO0000OO000OO00O0 #line:483
    O00O0OO00000OOOO0 ="x86_64"#line:484
  if OO00OO000OOOO000O =="Windows":#line:485
    OO0000OO000OO00O0 =f'{random.choice([6.0,10.0,11.0])}'#line:486
    O00OO0O000O0OO0OO ="Windows NT "+OO0000OO000OO00O0 +" Win64; x64"#line:487
    O00O0OO00000OOOO0 ="x86_64"#line:488
  if OO00OO000OOOO000O =="Android":#line:489
    OO0000OO000OO00O0 ="13"#line:490
    O00OO0O000O0OO0OO =f"Linux; Android 13; Pixel 6a"#line:491
    O00O0OO00000OOOO0 ="aarch64"#line:492
  O000OO0O0O0OOO00O ={"os":OO00OO000OOOO000O ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":OO0000OO000OO00O0 ,"os_arch":O00O0OO00000OOOO0 ,"system_locale":"ja-JP","client_build_number":OO00000OOOOO0O0O0 ,"client_event_source":None ,"design_id":0 }#line:493
  O0O0000000OO000O0 =f"Mozilla/5.0 ({O00OO0O000O0OO0OO}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:494
  return base64 .b64encode (json .dumps (O000OO0O0O0OOO00O ,separators =(',',':')).encode ()).decode (),O0O0000000OO000O0 #line:495
import base64 #line:497
def nickchanger ():#line:500
    try :#line:501
        with open ("token.txt")as O0O0OO0OO00O00000 :#line:502
            O0O000O0O0O00O0O0 =[O0OOO0OOOOO000O00 .strip ()for O0OOO0OOOOO000O00 in O0O0OO0OO00O00000 .readlines ()if O0OOO0OOOOO000O00 .strip ()]#line:503
    except (FileNotFoundError ,KeyError ):#line:504
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:505
        return #line:506
    OOOOO0O00OOO00OO0 =input ("Server ID?: ").strip ()#line:508
    OOOOOOO0O0O00O00O =input ("Nickname?: ").strip ()#line:509
    O00OOO0O0OOO0O0O0 =input ("Delay (in seconds)?: ").strip ()#line:510
    try :#line:512
        O00OOO0O0OOO0O0O0 =float (O00OOO0O0OOO0O0O0 )#line:513
        if O00OOO0O0OOO0O0O0 <0 :#line:514
            raise ValueError #line:515
    except ValueError :#line:516
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:517
        O00OOO0O0OOO0O0O0 =1.0 #line:518
    for O00O000O0OO0OOO00 in O0O000O0O0O00O0O0 :#line:520
        OO0OO00O0OOOOOOO0 ={"Authorization":O00O000O0OO0OOO00 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:525
        O00OO000OO0O000O0 ={"nick":OOOOOOO0O0O00O00O }#line:526
        O00000O0OOOOO0OO0 =requests .patch (f"https://discord.com/api/v9/guilds/{OOOOO0O00OOO00OO0}/members/@me",headers =OO0OO00O0OOOOOOO0 ,json =O00OO000OO0O000O0 )#line:527
        if O00000O0OOOOO0OO0 .status_code ==200 :#line:529
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Nickname changed to '{OOOOOOO0O0O00O00O}' successfully for token {O00O000O0OO0OOO00}.{colorama.Fore.RESET}")#line:530
        elif O00000O0OOOOO0OO0 .status_code ==429 :#line:531
            print (f"{colorama.Fore.RED}    [!] Rate limited. Please wait before retrying for token {O00O000O0OO0OOO00}.{colorama.Fore.RESET}")#line:532
            O00OOOO00O000OO0O =O00000O0OOOOO0OO0 .json ().get ("retry_after",1 )#line:533
            time .sleep (O00OOOO00O000OO0O )#line:534
        else :#line:535
            print (f"{colorama.Fore.RED}    [!] Error occurred: {O00000O0OOOOO0OO0.status_code} for token {O00O000O0OO0OOO00}.{colorama.Fore.RESET}")#line:536
        time .sleep (O00OOO0O0OOO0O0O0 )#line:538
import json ,websocket ,threading ,tls_client ,random ,time #line:542
session =tls_client .Session (client_identifier ="chrome112",random_tls_extension_order =True )#line:544
class Utils :#line:546
    @staticmethod #line:547
    def rangeCorrector (OO0O0O000O00OOOOO ):#line:548
        if [0 ,99 ]not in OO0O0O000O00OOOOO :#line:549
            OO0O0O000O00OOOOO .insert (0 ,[0 ,99 ])#line:550
        return OO0O0O000O00OOOOO #line:551
    @staticmethod #line:553
    def getRanges (O000OO0O00O0O00O0 ,OO0O00OO00O0000O0 ,O00OO0000O00OOO0O ):#line:554
        OOOO00000OO000O0O =int (O000OO0O00O0O00O0 *OO0O00OO00O0000O0 )#line:555
        O00O0OOOO0O0OOOOO =[[OOOO00000OO000O0O ,OOOO00000OO000O0O +99 ]]#line:556
        if O00OO0000O00OOO0O >OOOO00000OO000O0O +99 :#line:557
            O00O0OOOO0O0OOOOO .append ([OOOO00000OO000O0O +100 ,OOOO00000OO000O0O +199 ])#line:558
        return Utils .rangeCorrector (O00O0OOOO0O0OOOOO )#line:559
    @staticmethod #line:561
    def parseGuildMemberListUpdate (O0OO00000OOO0O00O ):#line:562
        O0000OO0OOO000000 ={"online_count":O0OO00000OOO0O00O ["d"]["online_count"],"member_count":O0OO00000OOO0O00O ["d"]["member_count"],"id":O0OO00000OOO0O00O ["d"]["id"],"guild_id":O0OO00000OOO0O00O ["d"]["guild_id"],"hoisted_roles":O0OO00000OOO0O00O ["d"]["groups"],"types":[],"locations":[],"updates":[],}#line:572
        for OO0OO0O00000OOO00 in O0OO00000OOO0O00O ["d"]["ops"]:#line:574
            O0000OO0OOO000000 ["types"].append (OO0OO0O00000OOO00 ["op"])#line:575
            if OO0OO0O00000OOO00 ["op"]in ("SYNC","INVALIDATE"):#line:576
                O0000OO0OOO000000 ["locations"].append (OO0OO0O00000OOO00 ["range"])#line:577
                if OO0OO0O00000OOO00 ["op"]=="SYNC":#line:578
                    O0000OO0OOO000000 ["updates"].append (OO0OO0O00000OOO00 ["items"])#line:579
                else :#line:580
                    O0000OO0OOO000000 ["updates"].append ([])#line:581
            elif OO0OO0O00000OOO00 ["op"]in ("INSERT","UPDATE","DELETE"):#line:582
                O0000OO0OOO000000 ["locations"].append (OO0OO0O00000OOO00 ["index"])#line:583
                if OO0OO0O00000OOO00 ["op"]=="DELETE":#line:584
                    O0000OO0OOO000000 ["updates"].append ([])#line:585
                else :#line:586
                    O0000OO0OOO000000 ["updates"].append (OO0OO0O00000OOO00 ["item"])#line:587
        return O0000OO0OOO000000 #line:588
class DiscordSocket (websocket .WebSocketApp ):#line:590
    def __init__ (O0OO0O00O0OOOO000 ,OOO0O0O00OO00OOOO ,O0O000OO00000O000 ,OO0OO00O000OOO0O0 ):#line:591
        O0OO0O00O0OOOO000 .token =OOO0O0O00OO00OOOO #line:592
        O0OO0O00O0OOOO000 .guild_id =O0O000OO00000O000 #line:593
        O0OO0O00O0OOOO000 .channel_id =OO0OO00O000OOO0O0 #line:594
        O0OO0O00O0OOOO000 .socket_headers ={"Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","Cache-Control":"no-cache","Pragma":"no-cache","Sec-WebSocket-Extensions":"permessage-deflate; client_max_window_bits","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",}#line:602
        super ().__init__ ("wss://gateway.discord.gg/?encoding=json&v=9",header =O0OO0O00O0OOOO000 .socket_headers ,on_open =lambda O000O0O000O00OO0O :O0OO0O00O0OOOO000 .sock_open (O000O0O000O00OO0O ),on_message =lambda OOO0OO0O0O0OO00OO ,OO000O0O0OO00000O :O0OO0O00O0OOOO000 .sock_message (OOO0OO0O0O0OO00OO ,OO000O0O0OO00000O ),on_close =lambda OOOOO0OOOOO000OOO ,O0O0O0OO0O0O00OO0 ,O00O00OO000O000O0 :O0OO0O00O0OOOO000 .sock_close (OOOOO0OOOOO000OOO ,O0O0O0OO0O0O00OO0 ,O00O00OO000O000O0 ),)#line:611
        O0OO0O00O0OOOO000 .endScraping =False #line:613
        O0OO0O00O0OOOO000 .guilds ={}#line:614
        O0OO0O00O0OOOO000 .members ={}#line:615
        O0OO0O00O0OOOO000 .ranges =[[0 ,0 ]]#line:616
        O0OO0O00O0OOOO000 .lastRange =0 #line:617
        O0OO0O00O0OOOO000 .packets_recv =0 #line:618
    def run (OO0O00OOO0O0O00O0 ):#line:620
        OO0O00OOO0O0O00O0 .run_forever ()#line:621
        return OO0O00OOO0O0O00O0 .members #line:622
    def scrapeUsers (OO000OO00000OOOO0 ):#line:624
        if not OO000OO00000OOOO0 .endScraping :#line:625
            OO000OO00000OOOO0 .send ('{"op":14,"d":{"guild_id":"'+OO000OO00000OOOO0 .guild_id +'","typing":true,"activities":true,"threads":true,"channels":{"'+OO000OO00000OOOO0 .channel_id +'":'+json .dumps (OO000OO00000OOOO0 .ranges )+"}}}")#line:634
    def sock_open (O00O0O00OOOOOOO00 ,O0O000O0OOO0OOO00 ):#line:636
        O00O0O00OOOOOOO00 .send ('{"op":2,"d":{"token":"'+O00O0O00OOOOOOO00 .token +'","capabilities":125,"properties":{"os":"Windows NT","browser":"Chrome","device":"","system_locale":"it-IT","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36","browser_version":"119.0","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":103981,"client_event_source":null},"presence":{"status":"online","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}')#line:641
    def heartbeatThread (O00OOO000OO0O0OO0 ,O0O0OOO0000O0OOO0 ):#line:643
        try :#line:644
            while True :#line:645
                O00OOO000OO0O0OO0 .send ('{"op":1,"d":'+str (O00OOO000OO0O0OO0 .packets_recv )+"}")#line:646
                time .sleep (O0O0OOO0000O0OOO0 )#line:647
        except Exception as O0OO0000000OO0O0O :#line:648
            pass #line:649
    def sock_message (O00OO0O00000000OO ,O0O00OOO0OO000OOO ,OO0O000000OO0000O ):#line:651
        O0OO00000000O0OOO =json .loads (OO0O000000OO0000O )#line:652
        if O0OO00000000O0OOO is None :#line:653
            return #line:654
        if O0OO00000000O0OOO ["op"]!=11 :#line:655
            O00OO0O00000000OO .packets_recv +=1 #line:656
        if O0OO00000000O0OOO ["op"]==10 :#line:657
            threading .Thread (target =O00OO0O00000000OO .heartbeatThread ,args =(O0OO00000000O0OOO ["d"]["heartbeat_interval"]/1000 ,),daemon =True ,).start ()#line:662
        if O0OO00000000O0OOO ["t"]=="READY":#line:663
            for O000OOO0OO0O00O00 in O0OO00000000O0OOO ["d"]["guilds"]:#line:664
                O00OO0O00000000OO .guilds [O000OOO0OO0O00O00 ["id"]]={"member_count":O000OOO0OO0O00O00 ["member_count"]}#line:665
        if O0OO00000000O0OOO ["t"]=="READY_SUPPLEMENTAL":#line:666
            O00OO0O00000000OO .ranges =Utils .getRanges (0 ,100 ,O00OO0O00000000OO .guilds [O00OO0O00000000OO .guild_id ]["member_count"])#line:669
            O00OO0O00000000OO .scrapeUsers ()#line:670
        elif O0OO00000000O0OOO ["t"]=="GUILD_MEMBER_LIST_UPDATE":#line:671
            O0000OO0000OOO0OO =Utils .parseGuildMemberListUpdate (O0OO00000000O0OOO )#line:672
            if O0000OO0000OOO0OO ["guild_id"]==O00OO0O00000000OO .guild_id and ("SYNC"in O0000OO0000OOO0OO ["types"]or "UPDATE"in O0000OO0000OOO0OO ["types"]):#line:676
                for OO0OO00O0OO00O0OO ,OO00OOOO0O00000O0 in enumerate (O0000OO0000OOO0OO ["types"]):#line:677
                    if OO00OOOO0O00000O0 =="SYNC":#line:678
                        if len (O0000OO0000OOO0OO ["updates"][OO0OO00O0OO00O0OO ])==0 :#line:679
                            O00OO0O00000000OO .endScraping =True #line:680
                            break #line:681
                        for O00O00O000O0O0O00 in O0000OO0000OOO0OO ["updates"][OO0OO00O0OO00O0OO ]:#line:683
                            if "member"in O00O00O000O0O0O00 :#line:684
                                OOO00OOOO0O00OOO0 =O00O00O000O0O0O00 ["member"]#line:685
                                OO00OO0OOOOO00OOO ={"tag":OOO00OOOO0O00OOO0 ["user"]["username"]+"#"+OOO00OOOO0O00OOO0 ["user"]["discriminator"],"id":OOO00OOOO0O00OOO0 ["user"]["id"],}#line:691
                                if not OOO00OOOO0O00OOO0 ["user"].get ("bot"):#line:692
                                    O00OO0O00000000OO .members [OOO00OOOO0O00OOO0 ["user"]["id"]]=OO00OO0OOOOO00OOO #line:693
                    elif OO00OOOO0O00000O0 =="UPDATE":#line:695
                        for O00O00O000O0O0O00 in O0000OO0000OOO0OO ["updates"][OO0OO00O0OO00O0OO ]:#line:696
                            if "member"in O00O00O000O0O0O00 :#line:697
                                OOO00OOOO0O00OOO0 =O00O00O000O0O0O00 ["member"]#line:698
                                OO00OO0OOOOO00OOO ={"tag":OOO00OOOO0O00OOO0 ["user"]["username"]+"#"+OOO00OOOO0O00OOO0 ["user"]["discriminator"],"id":OOO00OOOO0O00OOO0 ["user"]["id"],}#line:704
                                if not OOO00OOOO0O00OOO0 ["user"].get ("bot"):#line:705
                                    O00OO0O00000000OO .members [OOO00OOOO0O00OOO0 ["user"]["id"]]=OO00OO0OOOOO00OOO #line:706
                    O00OO0O00000000OO .lastRange +=1 #line:708
                    O00OO0O00000000OO .ranges =Utils .getRanges (O00OO0O00000000OO .lastRange ,100 ,O00OO0O00000000OO .guilds [O00OO0O00000000OO .guild_id ]["member_count"])#line:711
                    time .sleep (0.45 )#line:712
                    O00OO0O00000000OO .scrapeUsers ()#line:713
            if O00OO0O00000000OO .endScraping :#line:715
                O00OO0O00000000OO .close ()#line:716
    def sock_close (OO000OOO000OO000O ,O0000O00000OOOO0O ,O000OOOO00OOO000O ,O0OO000000OOO0O0O ):#line:718
        pass #line:719
def scrape (OOO0O00O0OO0OOOO0 ,OO0000OO0O00000O0 ,OO000OO00OO0O0OOO ):#line:721
    OOO0OOO0OOO0OO00O =DiscordSocket (OOO0O00O0OO0OOOO0 ,OO0000OO0O00000O0 ,OO000OO00OO0O0OOO )#line:722
    return OOO0OOO0OOO0OO00O .run ()#line:723
def member_scrape (O0OOO000O0OOOO0OO ,OO0O000OOOO0O00OO ,O00O0000OOOOO00OO ):#line:725
    O0000O000O0OO0O0O =[]#line:726
    for OOOOOO00O00OOO00O in O0OOO000O0OOOO0OO :#line:727
        OO00000O0OO0O00OO ={"Authorization":OOOOOO00O00OOO00O ,"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}#line:728
        OOO0000O0OO00000O =session .get (f"https://canary.discord.com/api/v9/guilds/{OO0O000OOOO0O00OO}",headers =OO00000O0OO0O00OO )#line:729
        if OOO0000O0OO00000O .status_code ==200 :#line:730
            O0000O000O0OO0O0O .append (OOOOOO00O00OOO00O )#line:731
            break #line:732
    if not O0000O000O0OO0O0O :#line:733
        print ("missing access")#line:734
    OOOOOO00O00OOO00O =random .choice (O0000O000O0OO0O0O )#line:736
    OO0000OOO0OO0OO0O =scrape (OOOOOO00O00OOO00O ,OO0O000OOOO0O00OO ,O00O0000OOOOO00OO )#line:737
    O00OO00O00OOO00O0 =[f"<@{O000OOO0O0OOO0O0O}>"for O000OOO0O0OOO0O0O in [int (O0O000OO0OO000OO0 )for O0O000OO0OO000OO0 in OO0000OOO0OO0OO0O .keys ()]]#line:738
    print (f"[SUCCESS] {len(O00OO00O00OOO00O0)} scraped members")#line:739
    return O00OO00O00OOO00O0 #line:740
def spammer_menu ():#line:742
    try :#line:743
        with open ("token.txt")as O00OO00OOO0O0OOOO :#line:744
            O0O0OO0000OO00O00 =[OO0OOO00OO0OOOO0O .strip ()for OO0OOO00OO0OOOO0O in O00OO00OOO0O0OOOO .readlines ()if OO0OOO00OO0OOOO0O .strip ()]#line:745
    except (FileNotFoundError ,KeyError ):#line:746
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:747
        return #line:748
    OO00O0O00OO0O00O0 =input ("Server ID?: ").strip ()#line:750
    OOOOOOOO0000OOOO0 =input ("Message?: ").strip ()#line:751
    OO0O0000OOO0OOO0O =input ("Random mention (True/False)?: ").strip ().lower ()=='true'#line:752
    O0OO00OO0O00O0OO0 =input ("Delay between messages (in seconds)?: ").strip ()#line:753
    O000O0OO0OOOOO000 =input ("Number of messages to send?: ").strip ()#line:754
    OOO0OO000O0O0OOOO =input ("Blacklist User IDs (comma-separated) (Leave blank to skip)?: ").strip ().split (',')#line:755
    OOO0OO000O0O0OOOO =[f"<@{O0OOO0000OO0OO000.strip()}>"for O0OOO0000OO0OO000 in OOO0OO000O0O0OOOO if O0OOO0000OO0OO000 .strip ()]#line:756
    try :#line:758
        O0OO00OO0O00O0OO0 =float (O0OO00OO0O00O0OO0 )#line:759
        if O0OO00OO0O00O0OO0 <0 :#line:760
            raise ValueError #line:761
    except ValueError :#line:762
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:763
        O0OO00OO0O00O0OO0 =1.0 #line:764
    try :#line:766
        O000O0OO0OOOOO000 =int (O000O0OO0OOOOO000 )#line:767
        if O000O0OO0OOOOO000 <=0 :#line:768
            raise ValueError #line:769
    except ValueError :#line:770
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:771
        O000O0OO0OOOOO000 =1 #line:772
    O00O00OO0O00O00OO =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:774
    if O00O00OO0O00O00OO =='2':#line:775
        OO0OOOO0OO00O0OO0 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:776
        OO0OOOO0OO00O0OO0 =[OOO00O0O0000OOO0O .strip ()for OOO00O0O0000OOO0O in OO0OOOO0OO00O0OO0 if OOO00O0O0000OOO0O .strip ()]#line:777
    else :#line:778
        OO0OOOO0OO00O0OO0 =fetch_channels (O0O0OO0000OO00O00 [0 ],OO00O0O00OO0O00O0 )#line:779
    O000O00OO00OO0OO0 =None #line:781
    spammer (O0O0OO0000OO00O00 ,OO00O0O00OO0O00O0 ,OO0OOOO0OO00O0OO0 ,OOOOOOOO0000OOOO0 ,OO0O0000OOO0OOO0O ,OOO0OO000O0O0OOOO ,O000O00OO00OO0OO0 ,O000O0OO0OOOOO000 )#line:783
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:785
def spammer (O0OO0OO0OOOOO0OO0 ,OOOOOO00OO0O0000O ,O00O0O0OOO0OOOOOO ,OOO0OO0OOOOO0O000 ,OOO0000OOO0O0O0OO ,OOO00000000O0000O ,O0OO00OO0OOOO00O0 ,OO0OOO0O0OOOO00O0 ):#line:787
    O000O00O00O0000OO =get_session (O0OO00OO0OOOO00O0 )#line:788
    O00OO000OOO00OO00 =0 #line:789
    OOOO0OO00O0O0O000 =member_scrape (O0OO0OO0OOOOO0OO0 ,OOOOOO00OO0O0000O ,O00O0O0OOO0OOOOOO [0 ])#line:791
    OOOO0OO00O0O0O000 =[O0O0O0O0OOOO000OO for O0O0O0O0OOOO000OO in OOOO0OO00O0O0O000 if O0O0O0O0OOOO000OO not in OOO00000000O0000O ]#line:792
    for _O0O00OOO00O00O0O0 in range (OO0OOO0O0OOOO00O0 ):#line:794
        OO0O00O00O0O00OO0 =O0OO0OO0OOOOO0OO0 [O00OO000OOO00OO00 ]#line:795
        O00O0OO00O0000OOO =get_headers (OO0O00O00O0O00OO0 )#line:796
        for OO0OO00O0O0000OO0 in O00O0O0OOO0OOOOOO :#line:797
            O0000O0O000O0OO00 =OOO0OO0OOOOO0O000 #line:798
            if OOO0000OOO0O0O0OO and OOOO0OO00O0O0O000 :#line:799
                O00O0O0O0O00O0OOO =random .choice (OOOO0OO00O0O0O000 )#line:800
                O0000O0O000O0OO00 +=f" {O00O0O0O0O00O0OOO}"#line:801
            OO0O0O0000OO00OO0 =O000O00O00O0000OO .post (f"https://discord.com/api/v9/channels/{OO0OO00O0O0000OO0}/messages",json ={"content":O0000O0O000O0OO00 },headers =O00O0OO00O0000OOO )#line:803
            if OO0O0O0000OO00OO0 .status_code ==200 :#line:804
                print (f"200 message sent: {OO0O00O00O0O00OO0}")#line:805
            elif OO0O0O0000OO00OO0 .status_code ==429 :#line:806
                print (f"429 rate limit: {OO0O00O00O0O00OO0}")#line:807
                O0OOOO00000OOOOOO =OO0O0O0000OO00OO0 .json ().get ("retry_after",1 )#line:808
                time .sleep (O0OOOO00000OOOOOO )#line:809
            elif OO0O0O0000OO00OO0 .status_code ==401 :#line:810
                print (f"401 unknown token: {OO0O00O00O0O00OO0}")#line:811
            else :#line:812
                print (f"error: {OO0O00O00O0O00OO0}")#line:813
        O00OO000OOO00OO00 =(O00OO000OOO00OO00 +1 )%len (O0OO0OO0OOOOO0OO0 )#line:815
        time .sleep (1 )#line:816
def main ():#line:821
    colorama .init ()#line:822
    while True :#line:823
        logo ()#line:824
        OO0O00OO0OO0000OO =input (f"{colorama.Fore.LIGHTMAGENTA_EX}    [Final] Select an option from above: ")#line:825
        if OO0O00OO0OO0000OO =="0":#line:827
            update_group_ids ()#line:828
        elif OO0O00OO0OO0000OO =="1":#line:829
            join_discord_invite ()#line:830
        elif OO0O00OO0OO0000OO =="2":#line:831
            reaction_spammer ()#line:832
        elif OO0O00OO0OO0000OO =="3":#line:833
            send_messages_with_mentions ()#line:834
        elif OO0O00OO0OO0000OO =="5":#line:835
            nickchanger ()#line:836
        elif OO0O00OO0OO0000OO =="4":#line:837
            spammer_menu ()#line:838
        elif OO0O00OO0OO0000OO =="0":#line:839
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [*] Exiting the application. Goodbye!{colorama.Fore.RESET}")#line:840
            break #line:841
        else :#line:842
            print (f"{colorama.Fore.RED}    [!] Invalid option selected!{colorama.Fore.RESET}")#line:843
        input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:845
if __name__ =="__main__":#line:847
    main ()#line:848
