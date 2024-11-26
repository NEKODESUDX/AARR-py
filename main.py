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
    O00O0O0O0O0OOO0O0 =requests .Session ()#line:55
    if proxy :#line:56
        O00O0O0O0O0OOO0O0 .proxies ={"http":proxy ,"https":proxy }#line:57
    return O00O0O0O0O0OOO0O0 #line:58
def get_headers (O00O0OO0OOO000OO0 ):#line:60
    return {"Authorization":O00O0OO0OOO000OO0 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:65
def send_message_with_mention (O000O00O0OOOOO000 ,O000O0OO0O0000OOO ,O0O000O00O00OO000 ,OOOO000O00OO0OO00 ):#line:68
    O00OOOO0O0O0OO000 =get_session ()#line:69
    O0O000OO000OO00O0 =get_headers (O000O00O0OOOOO000 )#line:70
    if OOOO000O00OO0OO00 :#line:72
        O0OO0OO0000O00OO0 =random .choice (OOOO000O00OO0OO00 )#line:73
        O0O000O00O00OO000 +=f" <@{O0OO0OO0000O00OO0}>"#line:74
    O00000OO00OO0O00O =O00OOOO0O0O0OO000 .post (f"https://discord.com/api/v9/channels/{O000O0OO0O0000OOO}/messages",headers =O0O000OO000OO00O0 ,json ={"content":O0O000O00O00OO000 })#line:80
    if O00000OO00OO0O00O .status_code in [200 ,201 ]:#line:81
        print (f"[+] Message sent to channel {O000O0OO0O0000OOO}")#line:82
    elif O00000OO00OO0O00O .status_code ==429 :#line:83
        print ("[-] Rate limited. Please wait before retrying.")#line:84
        O00O0000OOO00OOOO =O00000OO00OO0O00O .json ().get ("retry_after",1 )#line:85
        time .sleep (O00O0000OOO00OOOO )#line:86
    else :#line:87
        print (f"[!] Error occurred: {O00000OO00OO0O00O.status_code}")#line:88
def fetch_messages (O0O0OOO0O0O0OO00O ,OO0OOOO00OOO00O00 ,limit =100 ):#line:91
    O000O0OOO00OO0O00 ={"Authorization":O0O0OOO0O0O0OO00O ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:96
    O0O0O000000O0OO0O =requests .get (f"https://discord.com/api/v9/channels/{OO0OOOO00OOO00O00}/messages?limit={limit}",headers =O000O0OOO00OO0O00 )#line:100
    if O0O0O000000O0OO0O .status_code ==200 :#line:101
        return O0O0O000000O0OO0O .json ()#line:102
    else :#line:103
        print (f"[!] Failed to fetch messages. HTTP Status Code: {O0O0O000000O0OO0O.status_code}")#line:104
        return []#line:105
def reaction_spammer ():#line:106
    try :#line:107
        with open ("token.txt")as OOO000O0O00000000 :#line:108
            O0O0O00000O00OOO0 =[O0O00OOO0000OO000 .strip ()for O0O00OOO0000OO000 in OOO000O0O00000000 .readlines ()if O0O00OOO0000OO000 .strip ()]#line:109
    except (FileNotFoundError ,KeyError ):#line:110
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:111
        return #line:112
    OOO0OOOOO0OOOOOO0 =input ("Server ID?: ").strip ()#line:114
    O00OO0OOOO0OOOO00 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:116
    if O00OO0OOOO0OOOO00 =='2':#line:117
        O0OOO0OO0OOOO0O0O =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:118
        O0O0O0O00O0OO0O00 =[O00OOO0OOOO0000OO .strip ()for O00OOO0OOOO0000OO in O0OOO0OO0OOOO0O0O if O00OOO0OOOO0000OO .strip ()]#line:119
    else :#line:120
        O0O0O0O00O0OO0O00 =[]#line:121
        for O0O00O000000000O0 in O0O0O00000O00OOO0 :#line:122
            try :#line:123
                O0O0O0O00O0OO0O00 .extend (fetch_channels (O0O00O000000000O0 ,OOO0OOOOO0OOOOOO0 ))#line:124
            except Exception as O000O0OOOOOOO00O0 :#line:125
                print (f"[!] Failed to fetch channels for token. Error: {O000O0OOOOOOO00O0}")#line:126
                continue #line:127
    OO00000O0O00000OO =input ("Select your emoji (a, b, c, ... or custom emojis): ").strip ()#line:129
    O0O00OOOOOO0O0OOO =input ("Delay between reactions (in seconds)?: ").strip ()#line:130
    try :#line:132
        O0O00OOOOOO0O0OOO =float (O0O00OOOOOO0O0OOO )#line:133
        if O0O00OOOOOO0O0OOO <0 :#line:134
            raise ValueError #line:135
    except ValueError :#line:136
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:137
        O0O00OOOOOO0O0OOO =1.0 #line:138
    O0OOO00OO0OOO0000 =[]#line:140
    for O0OO00O0OO0OOOO00 in OO00000O0O00000OO .split (","):#line:141
        O0OO00O0OO0OOOO00 =O0OO00O0OO0OOOO00 .strip ().lower ()#line:142
        if O0OO00O0OO0OOOO00 in alphabet_to_flag :#line:143
            O0OOO00OO0OOO0000 .append (alphabet_to_flag [O0OO00O0OO0OOOO00 ])#line:144
        else :#line:145
            O0OOO00OO0OOO0000 .append (O0OO00O0OO0OOOO00 )#line:146
    if not O0OOO00OO0OOO0000 :#line:148
        print (f"{colorama.Fore.RED}    [!] No valid emojis provided!{colorama.Fore.RESET}")#line:149
        return #line:150
    for O0O00O000000000O0 in O0O0O00000O00OOO0 :#line:152
        for OOOOOOOOOOO00OOO0 in O0O0O0O00O0OO0O00 :#line:153
            try :#line:154
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {OOOOOOOOOOO00OOO0}...{colorama.Fore.RESET}")#line:155
                O0OOO0O0OO0000OO0 =fetch_messages (O0O00O000000000O0 ,OOOOOOOOOOO00OOO0 ,limit =100 )#line:156
                if not O0OOO0O0OO0000OO0 :#line:157
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:158
                    continue #line:159
                for O0000OOOOOO0O00OO in O0OOO0O0OO0000OO0 :#line:161
                    for O0OO00O0OO0OOOO00 in O0OOO00OO0OOO0000 :#line:162
                        reactionput (O0O00O000000000O0 ,OOOOOOOOOOO00OOO0 ,O0000OOOOOO0O00OO ['id'],O0OO00O0OO0OOOO00 )#line:163
                        time .sleep (O0O00OOOOOO0O0OOO )#line:164
            except Exception as O000O0OOOOOOO00O0 :#line:165
                print (f"[!] Error processing channel {OOOOOOOOOOO00OOO0}. Error: {O000O0OOOOOOO00O0}")#line:166
                continue #line:167
def update_group_ids ():#line:169
    try :#line:170
        with open ("token.txt")as OO0O0000000OOOO00 :#line:171
            OOO0O00OOO000OO0O =[OO0O000O0O0O0OOO0 .strip ()for OO0O000O0O0O0OOO0 in OO0O0000000OOOO00 .readlines ()if OO0O000O0O0O0OOO0 .strip ()]#line:172
        OOOO000000O00OO0O =OOO0O00OOO000OO0O [0 ]#line:173
    except (FileNotFoundError ,KeyError ):#line:174
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:175
        return #line:176
    OOO00O0OOO0OOOO0O ={"Authorization":OOOO000000O00OO0O ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:182
    O0O0000O0O0OO00OO =requests .get ('https://discord.com/api/v9/users/@me/channels',headers =OOO00O0OOO0OOOO0O )#line:184
    if O0O0000O0O0OO00OO .status_code ==200 :#line:185
        OOO0O0OO000OO0O00 =O0O0000O0O0OO00OO .json ()#line:186
        with open ("group_id.txt","w")as O0000OOOO000O00O0 :#line:187
            for OO0OOO00O0O00OO0O in OOO0O0OO000OO0O00 :#line:188
                if OO0OOO00O0O00OO0O ['type']==3 :#line:189
                    O0000OOOO000O00O0 .write (OO0OOO00O0O00OO0O ['id']+'\n')#line:190
        print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Group IDs updated successfully.{colorama.Fore.RESET}")#line:191
    else :#line:192
        print (f"{colorama.Fore.LIGHTRED_EX}    [!] Failed to retrieve group IDs. HTTP Status Code: {O0O0000O0O0OO00OO.status_code}{colorama.Fore.RESET}")#line:193
import requests #line:195
import requests #line:197
def fetch_channels (OO0O0O0O0O0OO0OOO ,O0O0O00O0O0OOOO00 ):#line:199
    try :#line:200
        O0000O00OO0OOOOOO =requests .Session ()#line:201
        O0OOOOO0O000OOO0O =get_headers (OO0O0O0O0O0OO0OOO )#line:202
        OOO00O0O0OO0OOOO0 =O0000O00OO0OOOOOO .get (f"https://discord.com/api/v9/guilds/{O0O0O00O0O0OOOO00}/channels",headers =O0OOOOO0O000OOO0O ,timeout =10 )#line:209
        if OOO00O0O0OO0OOOO0 .status_code ==200 :#line:212
            try :#line:213
                OOOO0OO0O0OOO00O0 =OOO00O0O0OO0OOOO0 .json ()#line:214
                return [O00OOOO0OO000O000 ['id']for O00OOOO0OO000O000 in OOOO0OO0O0OOO00O0 if O00OOOO0OO000O000 .get ('type')==0 ]#line:215
            except ValueError :#line:216
                print ("[!] Error: Response was not valid JSON.")#line:217
                return []#line:218
        elif OOO00O0O0OO0OOOO0 .status_code ==401 :#line:219
            print ("[!] Error: Unauthorized - check your token.")#line:220
        elif OOO00O0O0OO0OOOO0 .status_code ==403 :#line:221
            print ("[!] Error: Forbidden - you lack permissions.")#line:222
        elif OOO00O0O0OO0OOOO0 .status_code ==404 :#line:223
            print ("[!] Error: Server not found - check the server ID.")#line:224
        else :#line:225
            print (f"[!] Error: Unexpected status code {OOO00O0O0OO0OOOO0.status_code}.")#line:226
        return []#line:229
    except requests .exceptions .Timeout :#line:231
        print ("[!] Error: Request timed out. Check your connection or try again later.")#line:232
        return []#line:233
    except requests .exceptions .RequestException as O0OOO00OO0000O0OO :#line:234
        print (f"[!] Error: An error occurred while fetching channels: {O0OOO00OO0000O0OO}")#line:235
        return []#line:236
def extract_uids_from_messages (OO00O00000O0OOO0O ):#line:242
    O0O0OO00000O0OOOO =set ()#line:243
    for OO00000O00O0O00OO in OO00O00000O0OOO0O :#line:244
        O0O0OO00000O0OOOO .add (OO00000O00O0O00OO ['author']['id'])#line:245
    return list (O0O0OO00000O0OOOO )#line:246
def send_message_with_mention (O00O0OO00OO00O000 ,OOO0OOO000OOO0O0O ,OO0OOOO0000000OOO ,O0O0OO000O0OO0OOO ):#line:248
    O000OO0000O00OO00 =get_session ()#line:249
    O0000OO00O0OO0O0O =get_headers (O00O0OO00OO00O000 )#line:250
    if O0O0OO000O0OO0OOO :#line:252
        O0O0OOOO0O000OOOO =random .choice (O0O0OO000O0OO0OOO )#line:253
        OO0OOOO0000000OOO +=f" <@{O0O0OOOO0O000OOOO}>"#line:254
    OO00O0OOOOOOO00O0 =O000OO0000O00OO00 .post (f"https://discord.com/api/v9/channels/{OOO0OOO000OOO0O0O}/messages",headers =O0000OO00O0OO0O0O ,json ={"content":OO0OOOO0000000OOO })#line:260
    if OO00O0OOOOOOO00O0 .status_code in [200 ,201 ]:#line:261
        print (f"[+] Message sent to channel {OOO0OOO000OOO0O0O}")#line:262
    elif OO00O0OOOOOOO00O0 .status_code ==429 :#line:263
        print ("[-] Rate limited. Please wait before retrying.")#line:264
        O0O0OOOO00000000O =OO00O0OOOOOOO00O0 .json ().get ("retry_after",1 )#line:265
        time .sleep (O0O0OOOO00000000O )#line:266
    else :#line:267
        print (f"[!] Error occurred: {OO00O0OOOOOOO00O0.status_code}")#line:268
def send_messages_with_mentions ():#line:269
    try :#line:270
        with open ("token.txt")as OO0000O00O0O00O00 :#line:271
            O000OO0OOOO00OO00 =[OO0OO0O00000OOO0O .strip ()for OO0OO0O00000OOO0O in OO0000O00O0O00O00 .readlines ()if OO0OO0O00000OOO0O .strip ()]#line:272
    except (FileNotFoundError ,KeyError ):#line:273
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:274
        return #line:275
    OOO000OO0O00000OO =input ("Server ID?: ").strip ()#line:277
    OOOOOO0O0OO0000OO =input ("Delay between messages (in seconds)?: ").strip ()#line:278
    O00O0OOOO0000OO00 =input ("Number of messages to send?: ").strip ()#line:279
    O0OOOOOOO0OO0OOO0 =input ("Message content?: ").strip ()#line:280
    O000OOO00000O00O0 =input ("Blacklist User IDs (comma-separated)?: ").strip ().split (',')#line:281
    O000OOO00000O00O0 =[OOO0OOO000O0OOO00 .strip ()for OOO0OOO000O0OOO00 in O000OOO00000O00O0 if OOO0OOO000O0OOO00 .strip ()]#line:282
    try :#line:284
        OOOOOO0O0OO0000OO =float (OOOOOO0O0OO0000OO )#line:285
        if OOOOOO0O0OO0000OO <0 :#line:286
            raise ValueError #line:287
    except ValueError :#line:288
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:289
        OOOOOO0O0OO0000OO =1.0 #line:290
    try :#line:292
        O00O0OOOO0000OO00 =int (O00O0OOOO0000OO00 )#line:293
        if O00O0OOOO0000OO00 <=0 :#line:294
            raise ValueError #line:295
    except ValueError :#line:296
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:297
        O00O0OOOO0000OO00 =1 #line:298
    O0O0000O0OOO0O000 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:300
    if O0O0000O0OOO0O000 =='2':#line:301
        OOOO0O000O00OO0O0 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:302
        OOOO0O000O00OO0O0 =[O0OO0OOO0OO00OOOO .strip ()for O0OO0OOO0OO00OOOO in OOOO0O000O00OO0O0 if O0OO0OOO0OO00OOOO .strip ()]#line:303
    else :#line:304
        OOOO0O000O00OO0O0 =[]#line:305
    OOO0OOOO00OO00O0O =set ()#line:307
    for O00OO0O0OO00O00O0 in O000OO0OOOO00OO00 :#line:308
        O0O0O00OOOO0O000O =fetch_channels (O00OO0O0OO00O00O0 ,OOO000OO0O00000OO )#line:309
        for OOOOOO0000OO000OO in O0O0O00OOOO0O000O :#line:310
            O0O0O000OO0O00OOO =fetch_messages (O00OO0O0OO00O00O0 ,OOOOOO0000OO000OO ,limit =100 )#line:311
            O0OOO0OO00O00OOOO =extract_uids_from_messages (O0O0O000OO0O00OOO )#line:312
            OOO0OOOO00OO00O0O .update (O0OOO0OO00O00OOOO )#line:313
    OOO0OOOO00OO00O0O =list (set (OOO0OOOO00OO00O0O )-set (O000OOO00000O00O0 ))#line:316
    for _OO00O0OOO00OO000O in range (O00O0OOOO0000OO00 ):#line:318
        for O00OO0O0OO00O00O0 in O000OO0OOOO00OO00 :#line:319
            if OOOO0O000O00OO0O0 :#line:320
                O0O0O00OOOO0O000O =OOOO0O000O00OO0O0 #line:321
            for OOOOOO0000OO000OO in O0O0O00OOOO0O000O :#line:322
                send_message_with_mention (O00OO0O0OO00O00O0 ,OOOOOO0000OO000OO ,O0OOOOOOO0OO0OOO0 ,OOO0OOOO00OO00O0O )#line:323
                time .sleep (OOOOOO0O0OO0000OO )#line:324
def join_discord_invite ():#line:329
    try :#line:330
        with open ("token.txt")as OO00O0O00OOO000OO :#line:331
            O0000O0O000OOOOOO =[OO0O0OOOO000O0OOO .strip ()for OO0O0OOOO000O0OOO in OO00O0O00OOO000OO .readlines ()if OO0O0OOOO000O0OOO .strip ()]#line:332
    except (FileNotFoundError ,KeyError ):#line:333
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:334
        return #line:335
    O0OOO000O00OO0O00 =input ("Invite Code?: discord.gg/").strip ()#line:337
    for OOOO0OO0000000O00 in O0000O0O000OOOOOO :#line:340
        joiner (OOOO0OO0000000O00 ,O0OOO000O00OO0O00 )#line:341
import json ,time ,base64 ,random ,requests #line:343
def cookieset (O0OOOO00OOO000O00 ):#line:345
    OO0O00O0O0OOOOOOO =O0OOOO00OOO000O00 .get ("https://discord.com/app")#line:346
    return OO0O00O0O0OOOOOOO .cookies .get_dict ()#line:347
def generatexspandua (O0O0000O00O0000O0 ):#line:349
    OO0O0OOO0OOOOOO00 =["Android","Windows","Macintosh"]#line:350
    O0O000000O00O00OO =random .choice (OO0O0OOO0OOOOOO00 )#line:351
    if O0O000000O00O00OO =="Macintosh":#line:352
        O000OO0O000000OO0 =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:353
        O00000OO00OOOOOO0 ="Macintosh; Intel Mac OS X "+O000OO0O000000OO0 #line:354
        O000O000O0OO00000 ="x86_64"#line:355
    elif O0O000000O00O00OO =="Windows":#line:356
        O000OO0O000000OO0 =f'{random.choice([6.0, 10.0, 11.0])}'#line:357
        O00000OO00OOOOOO0 ="Windows NT "+O000OO0O000000OO0 +" Win64; x64"#line:358
        O000O000O0OO00000 ="x86_64"#line:359
    else :#line:360
        O000OO0O000000OO0 ="13"#line:361
        O00000OO00OOOOOO0 =f"Linux; Android 13; Pixel 6a"#line:362
        O000O000O0OO00000 ="aarch64"#line:363
    O00O0O0OOOO000O0O ={"os":O0O000000O00O00OO ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":O000OO0O000000OO0 ,"os_arch":O000O000O0OO00000 ,"system_locale":"ja-JP","client_build_number":O0O0000O00O0000O0 ,"client_event_source":None ,"design_id":0 }#line:376
    OOOO00OO000O0O0O0 =f"Mozilla/5.0 ({O00000OO00OOOOOO0}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:377
    return base64 .b64encode (json .dumps (O00O0O0OOOO000O0O ,separators =(',',':')).encode ()).decode (),OOOO00OO000O0O0O0 #line:378
def joiner (OO0O0OOO00OOOOOOO ,O0OO0000O0OO000O0 ,OOOOOO0O000OO0O00 ):#line:380
    O0OO0OOO0OOO0O0O0 =cookieset (OOOOOO0O000OO0O00 )#line:381
    O0OO0OOO0OOO0O0O0 ["locale"]="ja-JP"#line:382
    OO00000OOOO000OO0 =201211 #line:383
    O0OO0O00O000O00O0 ,OOO0OO00OOO00O0OO =generatexspandua (OO00000OOOO000OO0 )#line:384
    O00O0OOO0OO0O0000 ={"Authorization":OO0O0OOO00OOOOOOO ,"accept":"*/*","accept-language":"ja-JP","connection":"keep-alive","DNT":"1","origin":"https://discord.com","sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","referer":"https://discord.com/channels/@me","TE":"Trailers","user-agent":OOO0OO00OOO00O0OO ,"X-Super-Properties":O0OO0O00O000O00O0 ,}#line:399
    O000OO0O00O000000 =OOOOOO0O000OO0O00 .post ("https://discord.com/api/v9/invites/"+O0OO0000O0OO000O0 ,headers =O00O0OOO0OO0O0000 ,json ={},cookies =O0OO0OOO0OOO0O0O0 )#line:400
    if O000OO0O00O000000 .status_code ==200 :#line:401
        print ("[+] join this server "+OO0O0OOO00OOOOOOO )#line:402
        if "show_verification_form"in O000OO0O00O000000 .json ():#line:403
            bypass (OO0O0OOO00OOOOOOO ,O000OO0O00O000000 .json ()["guild"]["id"],OOOOOO0O000OO0O00 ,O00O0OOO0OO0O0000 )#line:404
        return #line:405
    elif "captcha_key"in O000OO0O00O000000 .text and O000OO0O00O000000 .status_code ==400 :#line:406
        print ("[!] Hcaptcha protect"+OO0O0OOO00OOOOOOO )#line:407
        return #line:408
    elif O000OO0O00O000000 .status_code ==401 :#line:409
        print ("[×] token is dead"+OO0O0OOO00OOOOOOO )#line:410
        return #line:411
    elif O000OO0O00O000000 .status_code ==403 :#line:412
        print ("[!] 403 banned "+OO0O0OOO00OOOOOOO )#line:413
        return #line:414
    elif O000OO0O00O000000 .status_code ==429 :#line:415
        O00O00OOO0O0O0OOO =O000OO0O00O000000 .json ().get ("retry_after",1 )#line:416
        print (f"[!] 429 rate limit. Retrying after {O00O00OOO0O0O0OOO} seconds.")#line:417
        time .sleep (O00O00OOO0O0O0OOO )#line:418
        return #line:419
    else :#line:420
        print ("[!] error "+OO0O0OOO00OOOOOOO )#line:421
        return #line:422
def update_group_ids ():#line:424
    O0000O0OO00O0OOOO =input ("Invite Code?: ").strip ()#line:425
    try :#line:426
        with open ("token.txt")as O000OO00O00OO000O :#line:427
            OOO00O0O0OOO0OOOO =[O0OO00O0O00000OOO .strip ()for O0OO00O0O00000OOO in O000OO00O00OO000O .readlines ()if O0OO00O0O00000OOO .strip ()]#line:428
    except (FileNotFoundError ,KeyError ):#line:429
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:430
        return #line:431
    O0OOOOO00000O0O0O =requests .Session ()#line:433
    for O00O00OO0OO000OOO in OOO00O0O0OOO0OOOO :#line:434
        joiner (O00O00OO0OO000OOO ,O0000O0OO00O0OOOO ,O0OOOOO00000O0O0O )#line:435
        time .sleep (2 )#line:436
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:438
def bypass (O0OOOO0OO0OO0000O ,O0O0OO0O00O00O000 ,O00OO0OOO0OOOOOOO ,OOO0O00OO0OO00OOO ):#line:441
    try :#line:442
        O0OOO000OO0OO000O =O00OO0OOO0OOOOOOO .get (f"https://discord.com/api/v9/guilds/{O0O0OO0O00O00O000}/member-verification?with_guild=false",headers =OOO0O00OO0OO00OOO ).json ()#line:443
        OO000OOO0OO00O0OO =O00OO0OOO0OOOOOOO .put (f"https://discord.com/api/v9/guilds/{O0O0OO0O00O00O000}/requests/@me",headers =OOO0O00OO0OO00OOO ,json =O0OOO000OO0OO000O )#line:444
        if OO000OOO0OO00O0OO .status_code ==201 :#line:445
            print (f"[+] MemberscreeningBypassed {O0OOOO0OO0OO0000O}")#line:446
            return #line:447
        else :#line:448
            print (f"[!] Bypassが出来ませんでした {O0OOOO0OO0OO0000O}")#line:449
            return #line:450
    except Exception as O000O0OO00OO0000O :#line:451
        print (f"[!] エラーが発生しました。{O000O0OO00OO0000O}")#line:452
session =requests .Session ()#line:454
def reactionput (O0OOO0OO0OOOO0000 ,OOO0O0OOO0O0OOO00 ,O00OO0O000OO000O0 ,OO0O00O0000OO0OOO ,proxy =None ):#line:457
    O0O0O00O0OO0OOO0O =get_session (proxy )#line:458
    OOOOOOOO00O000O00 =get_headers (O0O0O00O0OO0OOO0O )#line:459
    OOOOOOOO00O000O00 ["Authorization"]=O0OOO0OO0OOOO0000 #line:460
    OO0O00O0000OO0OOO =requests .utils .quote (OO0O00O0000OO0OOO )#line:462
    O0O0OOOOO00O00O00 =O0O0O00O0OO0OOO0O .put (f"https://discord.com/api/v9/channels/{OOO0O0OOO0O0OOO00}/messages/{O00OO0O000OO000O0}/reactions/{OO0O00O0000OO0OOO}/%40me?location=Message&type=0",headers =OOOOOOOO00O000O00 )#line:466
    if O0O0OOOOO00O00O00 .status_code in [200 ,204 ]:#line:467
        print (f"[+] Reaction '{OO0O00O0000OO0OOO}' added successfully to message {O00OO0O000OO000O0}")#line:468
    elif O0O0OOOOO00O00O00 .status_code ==429 :#line:469
        print ("[-] Rate limited. Please wait before retrying.")#line:470
        OOOO0OOO00OO0O0O0 =O0O0OOOOO00O00O00 .json ().get ("retry_after",1 )#line:471
        time .sleep (OOOO0OOO00OO0O0O0 )#line:472
    elif O0O0OOOOO00O00O00 .status_code ==401 :#line:473
        print ("[-] Invalid or expired token.")#line:474
    else :#line:475
        print (f"[!] Error occurred: {O0O0OOOOO00O00O00.status_code}")#line:476
def generatexspandua (OO00O0OO0OOO0OOOO ):#line:479
  OOOO000O0O00OO000 =["Android","Windows","Macintosh"]#line:480
  OOO0O0OO0000O00O0 =random .choice (OOOO000O0O00OO000 )#line:481
  if OOO0O0OO0000O00O0 =="Macintosh":#line:482
    OO0O0OO00OO0O00OO =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:483
    O00O0O0OOO00OOO00 ="Macintosh; Intel Mac OS X "+OO0O0OO00OO0O00OO #line:484
    OO0000OO0O0OOO00O ="x86_64"#line:485
  if OOO0O0OO0000O00O0 =="Windows":#line:486
    OO0O0OO00OO0O00OO =f'{random.choice([6.0,10.0,11.0])}'#line:487
    O00O0O0OOO00OOO00 ="Windows NT "+OO0O0OO00OO0O00OO +" Win64; x64"#line:488
    OO0000OO0O0OOO00O ="x86_64"#line:489
  if OOO0O0OO0000O00O0 =="Android":#line:490
    OO0O0OO00OO0O00OO ="13"#line:491
    O00O0O0OOO00OOO00 =f"Linux; Android 13; Pixel 6a"#line:492
    OO0000OO0O0OOO00O ="aarch64"#line:493
  OO000OOOO0OOOO0O0 ={"os":OOO0O0OO0000O00O0 ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":OO0O0OO00OO0O00OO ,"os_arch":OO0000OO0O0OOO00O ,"system_locale":"ja-JP","client_build_number":OO00O0OO0OOO0OOOO ,"client_event_source":None ,"design_id":0 }#line:494
  O0OOOO00OOOOO000O =f"Mozilla/5.0 ({O00O0O0OOO00OOO00}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:495
  return base64 .b64encode (json .dumps (OO000OOOO0OOOO0O0 ,separators =(',',':')).encode ()).decode (),O0OOOO00OOOOO000O #line:496
import base64 #line:498
def nickchanger ():#line:501
    try :#line:502
        with open ("token.txt")as OO0000000OOO0O0O0 :#line:503
            O0O0OO0OO0O00O0O0 =[O0O00OOO00OO00OO0 .strip ()for O0O00OOO00OO00OO0 in OO0000000OOO0O0O0 .readlines ()if O0O00OOO00OO00OO0 .strip ()]#line:504
    except (FileNotFoundError ,KeyError ):#line:505
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:506
        return #line:507
    O0O0000OO0OO0O00O =input ("Server ID?: ").strip ()#line:509
    O0000O00O000000OO =input ("Nickname?: ").strip ()#line:510
    O00OOO00OO0O0OO0O =input ("Delay (in seconds)?: ").strip ()#line:511
    try :#line:513
        O00OOO00OO0O0OO0O =float (O00OOO00OO0O0OO0O )#line:514
        if O00OOO00OO0O0OO0O <0 :#line:515
            raise ValueError #line:516
    except ValueError :#line:517
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:518
        O00OOO00OO0O0OO0O =1.0 #line:519
    for O0OOO0OO00OOO0O00 in O0O0OO0OO0O00O0O0 :#line:521
        O0O0OO000O0O00OOO ={"Authorization":O0OOO0OO00OOO0O00 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:526
        O0OOO00OOOO0OOOO0 ={"nick":O0000O00O000000OO }#line:527
        OOO0000O0OO0O00OO =requests .patch (f"https://discord.com/api/v9/guilds/{O0O0000OO0OO0O00O}/members/@me",headers =O0O0OO000O0O00OOO ,json =O0OOO00OOOO0OOOO0 )#line:528
        if OOO0000O0OO0O00OO .status_code ==200 :#line:530
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Nickname changed to '{O0000O00O000000OO}' successfully for token {O0OOO0OO00OOO0O00}.{colorama.Fore.RESET}")#line:531
        elif OOO0000O0OO0O00OO .status_code ==429 :#line:532
            print (f"{colorama.Fore.RED}    [!] Rate limited. Please wait before retrying for token {O0OOO0OO00OOO0O00}.{colorama.Fore.RESET}")#line:533
            OOO0000OOOO0OO000 =OOO0000O0OO0O00OO .json ().get ("retry_after",1 )#line:534
            time .sleep (OOO0000OOOO0OO000 )#line:535
        else :#line:536
            print (f"{colorama.Fore.RED}    [!] Error occurred: {OOO0000O0OO0O00OO.status_code} for token {O0OOO0OO00OOO0O00}.{colorama.Fore.RESET}")#line:537
        time .sleep (O00OOO00OO0O0OO0O )#line:539
import json ,websocket ,threading ,tls_client ,random ,time #line:543
session =tls_client .Session (client_identifier ="chrome112",random_tls_extension_order =True )#line:545
class Utils :#line:547
    @staticmethod #line:548
    def rangeCorrector (O0000O0OO0OOO00O0 ):#line:549
        if [0 ,99 ]not in O0000O0OO0OOO00O0 :#line:550
            O0000O0OO0OOO00O0 .insert (0 ,[0 ,99 ])#line:551
        return O0000O0OO0OOO00O0 #line:552
    @staticmethod #line:554
    def getRanges (O000O00OO00O0OO00 ,OO0OOOOO00O0OO0OO ,O00OOO0O0OOO0O000 ):#line:555
        O00OO000OOOO0OOO0 =int (O000O00OO00O0OO00 *OO0OOOOO00O0OO0OO )#line:556
        OOOOO00OOOO0000OO =[[O00OO000OOOO0OOO0 ,O00OO000OOOO0OOO0 +99 ]]#line:557
        if O00OOO0O0OOO0O000 >O00OO000OOOO0OOO0 +99 :#line:558
            OOOOO00OOOO0000OO .append ([O00OO000OOOO0OOO0 +100 ,O00OO000OOOO0OOO0 +199 ])#line:559
        return Utils .rangeCorrector (OOOOO00OOOO0000OO )#line:560
    @staticmethod #line:562
    def parseGuildMemberListUpdate (O0OO00O0O0O0O0000 ):#line:563
        O000OOO000O0OO0OO ={"online_count":O0OO00O0O0O0O0000 ["d"]["online_count"],"member_count":O0OO00O0O0O0O0000 ["d"]["member_count"],"id":O0OO00O0O0O0O0000 ["d"]["id"],"guild_id":O0OO00O0O0O0O0000 ["d"]["guild_id"],"hoisted_roles":O0OO00O0O0O0O0000 ["d"]["groups"],"types":[],"locations":[],"updates":[],}#line:573
        for O0O0OO0OOOO0OO000 in O0OO00O0O0O0O0000 ["d"]["ops"]:#line:575
            O000OOO000O0OO0OO ["types"].append (O0O0OO0OOOO0OO000 ["op"])#line:576
            if O0O0OO0OOOO0OO000 ["op"]in ("SYNC","INVALIDATE"):#line:577
                O000OOO000O0OO0OO ["locations"].append (O0O0OO0OOOO0OO000 ["range"])#line:578
                if O0O0OO0OOOO0OO000 ["op"]=="SYNC":#line:579
                    O000OOO000O0OO0OO ["updates"].append (O0O0OO0OOOO0OO000 ["items"])#line:580
                else :#line:581
                    O000OOO000O0OO0OO ["updates"].append ([])#line:582
            elif O0O0OO0OOOO0OO000 ["op"]in ("INSERT","UPDATE","DELETE"):#line:583
                O000OOO000O0OO0OO ["locations"].append (O0O0OO0OOOO0OO000 ["index"])#line:584
                if O0O0OO0OOOO0OO000 ["op"]=="DELETE":#line:585
                    O000OOO000O0OO0OO ["updates"].append ([])#line:586
                else :#line:587
                    O000OOO000O0OO0OO ["updates"].append (O0O0OO0OOOO0OO000 ["item"])#line:588
        return O000OOO000O0OO0OO #line:589
class DiscordSocket (websocket .WebSocketApp ):#line:591
    def __init__ (OO00O0OO000O0OO0O ,OOO0O00O0000O0OO0 ,OO0OO0O0OO0OOOO00 ,O000OOO00O0O00000 ):#line:592
        OO00O0OO000O0OO0O .token =OOO0O00O0000O0OO0 #line:593
        OO00O0OO000O0OO0O .guild_id =OO0OO0O0OO0OOOO00 #line:594
        OO00O0OO000O0OO0O .channel_id =O000OOO00O0O00000 #line:595
        OO00O0OO000O0OO0O .socket_headers ={"Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","Cache-Control":"no-cache","Pragma":"no-cache","Sec-WebSocket-Extensions":"permessage-deflate; client_max_window_bits","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",}#line:603
        super ().__init__ ("wss://gateway.discord.gg/?encoding=json&v=9",header =OO00O0OO000O0OO0O .socket_headers ,on_open =lambda O0000O000000OO000 :OO00O0OO000O0OO0O .sock_open (O0000O000000OO000 ),on_message =lambda O0O00O00O0OO0OO00 ,OOO0000O000OO0000 :OO00O0OO000O0OO0O .sock_message (O0O00O00O0OO0OO00 ,OOO0000O000OO0000 ),on_close =lambda OOOO0OOO0OO00OO00 ,OOO00O00OOOOOOOO0 ,OO000OOOOO0OOOOO0 :OO00O0OO000O0OO0O .sock_close (OOOO0OOO0OO00OO00 ,OOO00O00OOOOOOOO0 ,OO000OOOOO0OOOOO0 ),)#line:612
        OO00O0OO000O0OO0O .endScraping =False #line:614
        OO00O0OO000O0OO0O .guilds ={}#line:615
        OO00O0OO000O0OO0O .members ={}#line:616
        OO00O0OO000O0OO0O .ranges =[[0 ,0 ]]#line:617
        OO00O0OO000O0OO0O .lastRange =0 #line:618
        OO00O0OO000O0OO0O .packets_recv =0 #line:619
    def run (O00O0OOOO00000OO0 ):#line:621
        O00O0OOOO00000OO0 .run_forever ()#line:622
        return O00O0OOOO00000OO0 .members #line:623
    def scrapeUsers (O000OO0OO0O000O00 ):#line:625
        if not O000OO0OO0O000O00 .endScraping :#line:626
            O000OO0OO0O000O00 .send ('{"op":14,"d":{"guild_id":"'+O000OO0OO0O000O00 .guild_id +'","typing":true,"activities":true,"threads":true,"channels":{"'+O000OO0OO0O000O00 .channel_id +'":'+json .dumps (O000OO0OO0O000O00 .ranges )+"}}}")#line:635
    def sock_open (O0O000O0OO0000OOO ,OOOO00O0O0OOO0O00 ):#line:637
        O0O000O0OO0000OOO .send ('{"op":2,"d":{"token":"'+O0O000O0OO0000OOO .token +'","capabilities":125,"properties":{"os":"Windows NT","browser":"Chrome","device":"","system_locale":"it-IT","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36","browser_version":"119.0","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":103981,"client_event_source":null},"presence":{"status":"online","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}')#line:642
    def heartbeatThread (O00O000OO0OO000O0 ,O00000OOOO00O00OO ):#line:644
        try :#line:645
            while True :#line:646
                O00O000OO0OO000O0 .send ('{"op":1,"d":'+str (O00O000OO0OO000O0 .packets_recv )+"}")#line:647
                time .sleep (O00000OOOO00O00OO )#line:648
        except Exception as O0OOOO0O0OOO0O000 :#line:649
            pass #line:650
    def sock_message (OOOO00000000OO000 ,OOO00OOO0O00000OO ,OOO0O0O00O0O0OO0O ):#line:652
        O00O0O00OOOO00O00 =json .loads (OOO0O0O00O0O0OO0O )#line:653
        if O00O0O00OOOO00O00 is None :#line:654
            return #line:655
        if O00O0O00OOOO00O00 ["op"]!=11 :#line:656
            OOOO00000000OO000 .packets_recv +=1 #line:657
        if O00O0O00OOOO00O00 ["op"]==10 :#line:658
            threading .Thread (target =OOOO00000000OO000 .heartbeatThread ,args =(O00O0O00OOOO00O00 ["d"]["heartbeat_interval"]/1000 ,),daemon =True ,).start ()#line:663
        if O00O0O00OOOO00O00 ["t"]=="READY":#line:664
            for O0OO00OO0OO0OO0OO in O00O0O00OOOO00O00 ["d"]["guilds"]:#line:665
                OOOO00000000OO000 .guilds [O0OO00OO0OO0OO0OO ["id"]]={"member_count":O0OO00OO0OO0OO0OO ["member_count"]}#line:666
        if O00O0O00OOOO00O00 ["t"]=="READY_SUPPLEMENTAL":#line:667
            OOOO00000000OO000 .ranges =Utils .getRanges (0 ,100 ,OOOO00000000OO000 .guilds [OOOO00000000OO000 .guild_id ]["member_count"])#line:670
            OOOO00000000OO000 .scrapeUsers ()#line:671
        elif O00O0O00OOOO00O00 ["t"]=="GUILD_MEMBER_LIST_UPDATE":#line:672
            OOOOOOO0OO00OOO00 =Utils .parseGuildMemberListUpdate (O00O0O00OOOO00O00 )#line:673
            if OOOOOOO0OO00OOO00 ["guild_id"]==OOOO00000000OO000 .guild_id and ("SYNC"in OOOOOOO0OO00OOO00 ["types"]or "UPDATE"in OOOOOOO0OO00OOO00 ["types"]):#line:677
                for OO0O00OO0O0O0000O ,OO000OO00O0OO0O0O in enumerate (OOOOOOO0OO00OOO00 ["types"]):#line:678
                    if OO000OO00O0OO0O0O =="SYNC":#line:679
                        if len (OOOOOOO0OO00OOO00 ["updates"][OO0O00OO0O0O0000O ])==0 :#line:680
                            OOOO00000000OO000 .endScraping =True #line:681
                            break #line:682
                        for O000OOOO000OO0OO0 in OOOOOOO0OO00OOO00 ["updates"][OO0O00OO0O0O0000O ]:#line:684
                            if "member"in O000OOOO000OO0OO0 :#line:685
                                O0OO0O00OO0000O00 =O000OOOO000OO0OO0 ["member"]#line:686
                                OO00O00OOOOO0O00O ={"tag":O0OO0O00OO0000O00 ["user"]["username"]+"#"+O0OO0O00OO0000O00 ["user"]["discriminator"],"id":O0OO0O00OO0000O00 ["user"]["id"],}#line:692
                                if not O0OO0O00OO0000O00 ["user"].get ("bot"):#line:693
                                    OOOO00000000OO000 .members [O0OO0O00OO0000O00 ["user"]["id"]]=OO00O00OOOOO0O00O #line:694
                    elif OO000OO00O0OO0O0O =="UPDATE":#line:696
                        for O000OOOO000OO0OO0 in OOOOOOO0OO00OOO00 ["updates"][OO0O00OO0O0O0000O ]:#line:697
                            if "member"in O000OOOO000OO0OO0 :#line:698
                                O0OO0O00OO0000O00 =O000OOOO000OO0OO0 ["member"]#line:699
                                OO00O00OOOOO0O00O ={"tag":O0OO0O00OO0000O00 ["user"]["username"]+"#"+O0OO0O00OO0000O00 ["user"]["discriminator"],"id":O0OO0O00OO0000O00 ["user"]["id"],}#line:705
                                if not O0OO0O00OO0000O00 ["user"].get ("bot"):#line:706
                                    OOOO00000000OO000 .members [O0OO0O00OO0000O00 ["user"]["id"]]=OO00O00OOOOO0O00O #line:707
                    OOOO00000000OO000 .lastRange +=1 #line:709
                    OOOO00000000OO000 .ranges =Utils .getRanges (OOOO00000000OO000 .lastRange ,100 ,OOOO00000000OO000 .guilds [OOOO00000000OO000 .guild_id ]["member_count"])#line:712
                    time .sleep (0.45 )#line:713
                    OOOO00000000OO000 .scrapeUsers ()#line:714
            if OOOO00000000OO000 .endScraping :#line:716
                OOOO00000000OO000 .close ()#line:717
    def sock_close (OO00000000OO00OO0 ,OO00O0O0000O00OOO ,O0O0O00000O000O00 ,OO0OO0O000O00O0O0 ):#line:719
        pass #line:720
def scrape (OOO00O00000O0000O ,O000O000O000O0OO0 ,OOOO00O0OO0O0000O ):#line:722
    OOOOO000O0OOOOOOO =DiscordSocket (OOO00O00000O0000O ,O000O000O000O0OO0 ,OOOO00O0OO0O0000O )#line:723
    return OOOOO000O0OOOOOOO .run ()#line:724
def member_scrape (OO0O0O000OOO00O00 ,OO00OO0OO00O00O00 ,OOOOOOO0OOOOOO0O0 ):#line:726
    OO00O0O0O00000OO0 =[]#line:727
    for O000O0O0000O0OO00 in OO0O0O000OOO00O00 :#line:728
        OOOO00O0000000OOO ={"Authorization":O000O0O0000O0OO00 ,"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}#line:729
        OO00000000O00O00O =session .get (f"https://canary.discord.com/api/v9/guilds/{OO00OO0OO00O00O00}",headers =OOOO00O0000000OOO )#line:730
        if OO00000000O00O00O .status_code ==200 :#line:731
            OO00O0O0O00000OO0 .append (O000O0O0000O0OO00 )#line:732
            break #line:733
    if not OO00O0O0O00000OO0 :#line:734
        print ("missing access")#line:735
    O000O0O0000O0OO00 =random .choice (OO00O0O0O00000OO0 )#line:737
    O00O00OO0O0O000OO =scrape (O000O0O0000O0OO00 ,OO00OO0OO00O00O00 ,OOOOOOO0OOOOOO0O0 )#line:738
    OO00OOOOO0O000OOO =[f"<@{O000000OOOO00O0OO}>"for O000000OOOO00O0OO in [int (OOOOOO000O000O0OO )for OOOOOO000O000O0OO in O00O00OO0O0O000OO .keys ()]]#line:739
    print (f"[SUCCESS] {len(OO00OOOOO0O000OOO)} scraped members")#line:740
    return OO00OOOOO0O000OOO #line:741
def spammer_menu ():#line:743
    try :#line:744
        with open ("token.txt")as OOO0O000O000O0OOO :#line:745
            OOO0000O0O0OO0000 =[OOOO0OOO0O000OO0O .strip ()for OOOO0OOO0O000OO0O in OOO0O000O000O0OOO .readlines ()if OOOO0OOO0O000OO0O .strip ()]#line:746
    except (FileNotFoundError ,KeyError ):#line:747
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:748
        return #line:749
    O0O00O000O000OOO0 =input ("Server ID?: ").strip ()#line:751
    O0OO000OOOOOO0OOO =input ("Message?: ").strip ()#line:752
    O0OOO0O00O00000O0 =input ("Random mention (True/False)?: ").strip ().lower ()=='true'#line:753
    OOOOOO00OOO0O0O00 =input ("Delay between messages (in seconds)?: ").strip ()#line:754
    O000O0OOO000000O0 =input ("Number of messages to send?: ").strip ()#line:755
    OOOOO0O0O0OOOO0OO =input ("Blacklist User IDs (comma-separated) (Leave blank to skip)?: ").strip ().split (',')#line:756
    OOOOO0O0O0OOOO0OO =[f"<@{O0OOO000O0OO000O0.strip()}>"for O0OOO000O0OO000O0 in OOOOO0O0O0OOOO0OO if O0OOO000O0OO000O0 .strip ()]#line:757
    try :#line:759
        OOOOOO00OOO0O0O00 =float (OOOOOO00OOO0O0O00 )#line:760
        if OOOOOO00OOO0O0O00 <0 :#line:761
            raise ValueError #line:762
    except ValueError :#line:763
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:764
        OOOOOO00OOO0O0O00 =1.0 #line:765
    try :#line:767
        O000O0OOO000000O0 =int (O000O0OOO000000O0 )#line:768
        if O000O0OOO000000O0 <=0 :#line:769
            raise ValueError #line:770
    except ValueError :#line:771
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:772
        O000O0OOO000000O0 =1 #line:773
    OOO0O0OOO00OO00O0 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:775
    if OOO0O0OOO00OO00O0 =='2':#line:776
        O00OOO0O0OOOOO0OO =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:777
        O00OOO0O0OOOOO0OO =[OO0OOOO0OOOO0O000 .strip ()for OO0OOOO0OOOO0O000 in O00OOO0O0OOOOO0OO if OO0OOOO0OOOO0O000 .strip ()]#line:778
    else :#line:779
        O00OOO0O0OOOOO0OO =fetch_channels (OOO0000O0O0OO0000 [0 ],O0O00O000O000OOO0 )#line:780
    O0OO00000OOOOOO0O =None #line:782
    spammer (OOO0000O0O0OO0000 ,O0O00O000O000OOO0 ,O00OOO0O0OOOOO0OO ,O0OO000OOOOOO0OOO ,O0OOO0O00O00000O0 ,OOOOO0O0O0OOOO0OO ,O0OO00000OOOOOO0O ,O000O0OOO000000O0 )#line:784
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:786
def spammer (O0000O000O0OOO0OO ,O0O0000OO000000O0 ,O000O0OOOOOO00O00 ,O00O0OO00O00O0OOO ,O0OO0000OO000OO0O ,OOOOO00OOOO0OO0O0 ,O00000O0OOO0OOOOO ,OO00O0O0O00O0000O ):#line:788
    O0OOO000O0OOO00OO =get_session (O00000O0OOO0OOOOO )#line:789
    OOOO0OO00O00OOO0O =0 #line:790
    OO000OO0O0O0OO00O =member_scrape (O0000O000O0OOO0OO ,O0O0000OO000000O0 ,O000O0OOOOOO00O00 [0 ])#line:792
    OO000OO0O0O0OO00O =[O0000OO000OO0O0O0 for O0000OO000OO0O0O0 in OO000OO0O0O0OO00O if O0000OO000OO0O0O0 not in OOOOO00OOOO0OO0O0 ]#line:793
    for _OOO0O00OOO0OOO0OO in range (OO00O0O0O00O0000O ):#line:795
        OO00OO0OOOOOO00O0 =O0000O000O0OOO0OO [OOOO0OO00O00OOO0O ]#line:796
        OOOOOOO0O0000OOO0 =get_headers (OO00OO0OOOOOO00O0 )#line:797
        for OO00OOO0000O0OOO0 in O000O0OOOOOO00O00 :#line:798
            OOO0O000O0OOO00O0 =O00O0OO00O00O0OOO #line:799
            if O0OO0000OO000OO0O and OO000OO0O0O0OO00O :#line:800
                OO0OO0000O0OOO0O0 =random .choice (OO000OO0O0O0OO00O )#line:801
                OOO0O000O0OOO00O0 +=f" {OO0OO0000O0OOO0O0}"#line:802
            OOO00000OOOOOOOO0 =O0OOO000O0OOO00OO .post (f"https://discord.com/api/v9/channels/{OO00OOO0000O0OOO0}/messages",json ={"content":OOO0O000O0OOO00O0 },headers =OOOOOOO0O0000OOO0 )#line:804
            if OOO00000OOOOOOOO0 .status_code ==200 :#line:805
                print (f"200 message sent: {OO00OO0OOOOOO00O0}")#line:806
            elif OOO00000OOOOOOOO0 .status_code ==429 :#line:807
                print (f"429 rate limit: {OO00OO0OOOOOO00O0}")#line:808
                OO000OOO00000OO00 =OOO00000OOOOOOOO0 .json ().get ("retry_after",1 )#line:809
                time .sleep (OO000OOO00000OO00 )#line:810
            elif OOO00000OOOOOOOO0 .status_code ==401 :#line:811
                print (f"401 unknown token: {OO00OO0OOOOOO00O0}")#line:812
            else :#line:813
                print (f"error: {OO00OO0OOOOOO00O0}")#line:814
        OOOO0OO00O00OOO0O =(OOOO0OO00O00OOO0O +1 )%len (O0000O000O0OOO0OO )#line:816
        time .sleep (1 )#line:817
def main ():#line:822
    colorama .init ()#line:823
    while True :#line:824
        logo ()#line:825
        OO0O0O00OOO00OO0O =input (f"{colorama.Fore.LIGHTMAGENTA_EX}    [Final] Select an option from above: ")#line:826
        if OO0O0O00OOO00OO0O =="0":#line:828
            update_group_ids ()#line:829
        elif OO0O0O00OOO00OO0O =="1":#line:830
            join_discord_invite ()#line:831
        elif OO0O0O00OOO00OO0O =="2":#line:832
            reaction_spammer ()#line:833
        elif OO0O0O00OOO00OO0O =="3":#line:834
            send_messages_with_mentions ()#line:835
        elif OO0O0O00OOO00OO0O =="5":#line:836
            nickchanger ()#line:837
        elif OO0O0O00OOO00OO0O =="4":#line:838
            spammer_menu ()#line:839
        elif OO0O0O00OOO00OO0O =="0":#line:840
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [*] Exiting the application. Goodbye!{colorama.Fore.RESET}")#line:841
            break #line:842
        else :#line:843
            print (f"{colorama.Fore.RED}    [!] Invalid option selected!{colorama.Fore.RESET}")#line:844
        input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:846
if __name__ =="__main__":#line:848
    main ()#line:849
