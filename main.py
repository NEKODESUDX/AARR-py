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
    O00OOO0OOO00OO0OO =requests .Session ()#line:57
    if proxy :#line:58
        O00OOO0OOO00OO0OO .proxies ={"http":proxy ,"https":proxy }#line:59
    return O00OOO0OOO00OO0OO #line:60
def get_headers (O00OO000O0000000O ):#line:62
    return {"Authorization":O00OO000O0000000O ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:67
def send_message_with_mention (O0O0O0O0O0OOO0OO0 ,O0O00000000000O0O ,OOO0OO0O0O0O0O0O0 ,OOO0O00OOO0000OO0 ):#line:70
    OOOO0OOOO00O000OO =get_session ()#line:71
    OOO000OOOO00O0000 =get_headers (O0O0O0O0O0OOO0OO0 )#line:72
    if OOO0O00OOO0000OO0 :#line:74
        OOOOOO000OO00OOO0 =random .choice (OOO0O00OOO0000OO0 )#line:75
        OOO0OO0O0O0O0O0O0 +=f" <@{OOOOOO000OO00OOO0}>"#line:76
    OO0O000OO00OOO00O =OOOO0OOOO00O000OO .post (f"https://discord.com/api/v9/channels/{O0O00000000000O0O}/messages",headers =OOO000OOOO00O0000 ,json ={"content":OOO0OO0O0O0O0O0O0 })#line:82
    if OO0O000OO00OOO00O .status_code in [200 ,201 ]:#line:83
        print (f"[+] Message sent to channel {O0O00000000000O0O}")#line:84
    elif OO0O000OO00OOO00O .status_code ==429 :#line:85
        print ("[-] Rate limited. Please wait before retrying.")#line:86
        OO00000OOO0OO0O00 =OO0O000OO00OOO00O .json ().get ("retry_after",1 )#line:87
        time .sleep (OO00000OOO0OO0O00 )#line:88
    else :#line:89
        print (f"[!] Error occurred: {OO0O000OO00OOO00O.status_code}")#line:90
def fetch_messages (O0000O00O00OO00OO ,OOO00O0O00OOOO0O0 ,limit =100 ):#line:93
    O00OOO000OO0000OO ={"Authorization":O0000O00O00OO00OO ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:98
    OOOO00O0OOO0OOO00 =requests .get (f"https://discord.com/api/v9/channels/{OOO00O0O00OOOO0O0}/messages?limit={limit}",headers =O00OOO000OO0000OO )#line:102
    if OOOO00O0OOO0OOO00 .status_code ==200 :#line:103
        return OOOO00O0OOO0OOO00 .json ()#line:104
    else :#line:105
        print (f"[!] Failed to fetch messages. HTTP Status Code: {OOOO00O0OOO0OOO00.status_code}")#line:106
        return []#line:107
import concurrent .futures #line:108
def reaction_spammer ():#line:110
    try :#line:111
        with open ("token.txt")as OOO0O0O0OOOOOOO0O :#line:112
            O00O0OO000OO0OOOO =[OOO0OOO0000O0O000 .strip ()for OOO0OOO0000O0O000 in OOO0O0O0OOOOOOO0O .readlines ()if OOO0OOO0000O0O000 .strip ()]#line:113
    except (FileNotFoundError ,KeyError ):#line:114
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:115
        return #line:116
    OO0OO000OOO0OO00O =input ("Server ID?: ").strip ()#line:118
    O0OOOO000O00OO0O0 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:120
    if O0OOOO000O00OO0O0 =='2':#line:121
        OOOO00OO000OOO00O =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:122
        O0OOOOOOO00OO0O0O =[O00O00OOO00O0O00O .strip ()for O00O00OOO00O0O00O in OOOO00OO000OOO00O if O00O00OOO00O0O00O .strip ()]#line:123
    else :#line:124
        O0OOOOOOO00OO0O0O =[]#line:125
        for O0000O000OOO000O0 in O00O0OO000OO0OOOO :#line:126
            try :#line:127
                O0OOOOOOO00OO0O0O .extend (fetch_channels (O0000O000OOO000O0 ,OO0OO000OOO0OO00O ))#line:128
            except Exception as O000OO00OO0000OO0 :#line:129
                print (f"[!] Failed to fetch channels for token. Error: {O000OO00OO0000OO0}")#line:130
                continue #line:131
    OOOOO0O0OO00OOO00 =input ("Select your emoji (a, b, c, ... or custom emojis): ").strip ()#line:133
    OOO00000O0O0OOOO0 =input ("Delay between reactions (in seconds)?: ").strip ()#line:134
    try :#line:136
        OOO00000O0O0OOOO0 =float (OOO00000O0O0OOOO0 )#line:137
        if OOO00000O0O0OOOO0 <0 :#line:138
            raise ValueError #line:139
    except ValueError :#line:140
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:141
        OOO00000O0O0OOOO0 =1.0 #line:142
    OO000OOO0OO0O0O0O =[]#line:144
    for OO00OO00OOO00OOOO in OOOOO0O0OO00OOO00 .split (","):#line:145
        OO00OO00OOO00OOOO =OO00OO00OOO00OOOO .strip ().lower ()#line:146
        if OO00OO00OOO00OOOO in alphabet_to_flag :#line:147
            OO000OOO0OO0O0O0O .append (alphabet_to_flag [OO00OO00OOO00OOOO ])#line:148
        else :#line:149
            OO000OOO0OO0O0O0O .append (OO00OO00OOO00OOOO )#line:150
    if not OO000OOO0OO0O0O0O :#line:152
        print (f"{colorama.Fore.RED}    [!] No valid emojis provided!{colorama.Fore.RESET}")#line:153
        return #line:154
import requests #line:156
import json #line:157
import time #line:158
import colorama #line:159
alphabet_to_flag ={'a':'🇦','b':'🇧','c':'🇨','d':'🇩','e':'🇪','f':'🇫','g':'🇬','h':'🇭','i':'🇮','j':'🇯','k':'🇰','l':'🇱','m':'🇲','n':'🇳','o':'🇴','p':'🇵','q':'🇶','r':'🇷','s':'🇸','t':'🇹','u':'🇺','v':'🇻','w':'🇼','x':'🇽','y':'🇾','z':'🇿'}#line:167
def fetch_channels (OO0000O00O0O0O00O ,OO0OOO0O0OO0OOO00 ):#line:169
    OOOO0O0OO00OO00O0 =f"https://discord.com/api/v9/guilds/{OO0OOO0O0OO0OOO00}/channels"#line:170
    OO0OO00O0O000O0OO ={"Authorization":OO0000O00O0O0O00O }#line:171
    OOO00O0OO000000O0 =requests .get (OOOO0O0OO00OO00O0 ,headers =OO0OO00O0O000O0OO )#line:172
    if OOO00O0OO000000O0 .status_code ==200 :#line:173
        return [OOOO00000OO00O00O ['id']for OOOO00000OO00O00O in OOO00O0OO000000O0 .json ()if OOOO00000OO00O00O ['type']==0 ]#line:174
    else :#line:175
        raise Exception (f"Failed to fetch channels: {OOO00O0OO000000O0.status_code} - {OOO00O0OO000000O0.text}")#line:176
def fetch_messages (OOO000O0OOOO000OO ,O0O0OO0OO00O0O0OO ,limit =100 ):#line:178
    OO0O0OO0O0OOOO0OO =f"https://discord.com/api/v9/channels/{O0O0OO0OO00O0O0OO}/messages?limit={limit}"#line:179
    O0O00O0000OOO00OO ={"Authorization":OOO000O0OOOO000OO }#line:180
    OO0OO000OO000OO00 =requests .get (OO0O0OO0O0OOOO0OO ,headers =O0O00O0000OOO00OO )#line:181
    if OO0OO000OO000OO00 .status_code ==200 :#line:182
        return OO0OO000OO000OO00 .json ()#line:183
    else :#line:184
        print (f"[!] Failed to fetch messages: {OO0OO000OO000OO00.status_code} - {OO0OO000OO000OO00.text}")#line:185
        return []#line:186
def reactionput (O000OO00OOOOO0OO0 ,O0OOOOO0OOOO0OO00 ,OO00OO0000O000O0O ,O0O0O0000OO0OOOO0 ):#line:188
    O0000OO00O0OO0OO0 =f"https://discord.com/api/v9/channels/{O0OOOOO0OOOO0OO00}/messages/{OO00OO0000O000O0O}/reactions/{O0O0O0000OO0OOOO0}/@me"#line:189
    OO0O0OO0OO00O00OO ={"Authorization":O000OO00OOOOO0OO0 ,"Content-Type":"application/json"}#line:190
    O0O00OO0000000O0O =requests .put (O0000OO00O0OO0OO0 ,headers =OO0O0OO0OO00O00OO )#line:191
    if O0O00OO0000000O0O .status_code not in [204 ,200 ]:#line:192
        print (f"{colorama.Fore.RED}    [!] Failed to add reaction: {O0O00OO0000000O0O.status_code} - {O0O00OO0000000O0O.text}{colorama.Fore.RESET}")#line:193
import random #line:195
def reaction_art ():#line:197
    try :#line:198
        with open ("token.txt",encoding ="utf-8")as O0O000OO0OOOOOOOO :#line:199
            O00O0O0O0O0OO000O =[O00000O00OOO000OO .strip ()for O00000O00OOO000OO in O0O000OO0OOOOOOOO .readlines ()if O00000O00OOO000OO .strip ()]#line:200
    except (FileNotFoundError ,KeyError ):#line:201
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:202
        return #line:203
    O00O0000O0O00OOO0 =input ("Server ID?: ").strip ()#line:205
    O0OO0O000O0O0OOOO =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:207
    if O0OO0O000O0O0OOOO =='2':#line:208
        O0O000OO0O0OO0OO0 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:209
        O0OO000OOOOOOO000 =[OO0OOO00O0O0000OO .strip ()for OO0OOO00O0O0000OO in O0O000OO0O0OO0OO0 if OO0OOO00O0O0000OO .strip ()]#line:210
    else :#line:211
        O0OO000OOOOOOO000 =[]#line:212
        for OO0000O0O0OOO00O0 in O00O0O0O0O0OO000O :#line:213
            try :#line:214
                O0OO000OOOOOOO000 .extend (fetch_channels (OO0000O0O0OOO00O0 ,O00O0000O0O00OOO0 ))#line:215
            except Exception as OO00OOO0OOO0O0000 :#line:216
                print (f"[!] Failed to fetch channels for token. Error: {OO00OOO0OOO0O0000}")#line:217
                continue #line:218
        random .shuffle (O0OO000OOOOOOO000 )#line:219
    O000O0OOOO000000O =input ("Delay between reactions (in seconds)?: ").strip ()#line:221
    try :#line:223
        O000O0OOOO000000O =float (O000O0OOOO000000O )#line:224
        if O000O0OOOO000000O <0 :#line:225
            raise ValueError #line:226
    except ValueError :#line:227
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:228
        O000O0OOOO000000O =1.0 #line:229
    try :#line:231
        with open ("art.txt",encoding ="utf-8")as OO0O00O0O0O0000OO :#line:232
            OOOO00O0OO00O00OO =[O00O000OO0O0OO000 .strip ()for O00O000OO0O0OO000 in OO0O00O0O0O0000OO .readlines ()if O00O000OO0O0OO000 .strip ()]#line:233
    except (FileNotFoundError ,KeyError ):#line:234
        print (f"{colorama.Fore.RED}    [!] Error: art.txt file not found or empty!{colorama.Fore.RESET}")#line:235
        return #line:236
    except UnicodeDecodeError as OO00OOO0OOO0O0000 :#line:237
        print (f"{colorama.Fore.RED}    [!] Error decoding art.txt: {str(OO00OOO0OOO0O0000)}{colorama.Fore.RESET}")#line:238
        return #line:239
    if not OOOO00O0OO00O00OO :#line:241
        print (f"{colorama.Fore.RED}    [!] No valid art provided in art.txt!{colorama.Fore.RESET}")#line:242
        return #line:243
    OOOO00O0OO00O00OO .reverse ()#line:246
    for OO0000O0O0OOO00O0 in O00O0O0O0O0OO000O :#line:248
        for O0O00O000000O0000 in O0OO000OOOOOOO000 :#line:249
            try :#line:250
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {O0O00O000000O0000}...{colorama.Fore.RESET}")#line:251
                O00000000OOO0O0OO =fetch_messages (OO0000O0O0OOO00O0 ,O0O00O000000O0000 ,limit =100 )#line:254
                if not O00000000OOO0O0OO :#line:255
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:256
                    continue #line:257
                for OO000O000O00O0OOO ,O00O0O00O0OO0OOO0 in enumerate (O00000000OOO0O0OO ):#line:260
                    OO00O000OO0O0O0O0 =OOOO00O0OO00O00OO [OO000O000O00O0OOO %len (OOOO00O0OO00O00OO )].split (',')#line:261
                    for O000O00O00O0OO00O in OO00O000OO0O0O0O0 :#line:262
                        reactionput (OO0000O0O0OOO00O0 ,O0O00O000000O0000 ,O00O0O00O0OO0OOO0 ['id'],O000O00O00O0OO00O .strip ())#line:263
                        print (f"Adding reaction '{O000O00O00O0OO00O.strip()}' to message {O00O0O00O0OO0OOO0['id']} in channel {O0O00O000000O0000}")#line:264
                        time .sleep (O000O0OOOO000000O )#line:265
            except Exception as OO00OOO0OOO0O0000 :#line:266
                print (f"[!] Error processing channel {O0O00O000000O0000}. Error: {OO00OOO0OOO0O0000}")#line:267
                continue #line:268
    def OOOO0O00000OOO00O (O00OO0O0000OOO000 ):#line:273
        for OO0000OO0OOOO0O00 in O0OO000OOOOOOO000 :#line:274
            try :#line:275
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {OO0000OO0OOOO0O00}...{colorama.Fore.RESET}")#line:276
                OO0OO00O0O0OOO0O0 =fetch_messages (O00OO0O0000OOO000 ,OO0000OO0OOOO0O00 ,limit =100 )#line:277
                if not OO0OO00O0O0OOO0O0 :#line:278
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:279
                    continue #line:280
                for O0O000OO0O0OO0000 in OO0OO00O0O0OOO0O0 :#line:282
                    for OO00000OO0O0O000O in OO00O000OO0O0O0O0 :#line:283
                        reactionput (O00OO0O0000OOO000 ,OO0000OO0OOOO0O00 ,O0O000OO0O0OO0000 ['id'],OO00000OO0O0O000O )#line:284
                        time .sleep (O000O0OOOO000000O )#line:285
            except Exception as O0O0OOOO00OOO0000 :#line:286
                print (f"[!] Error processing channel {OO0000OO0OOOO0O00}. Error: {O0O0OOOO00OOO0000}")#line:287
                continue #line:288
    with concurrent .futures .ThreadPoolExecutor ()as OO00O000O00O00OOO :#line:290
        O0OOOO00OOO0O0OOO =[OO00O000O00O00OOO .submit (OOOO0O00000OOO00O ,O00O0O0OOOOOOO00O )for O00O0O0OOOOOOO00O in O00O0O0O0O0OO000O ]#line:291
        concurrent .futures .wait (O0OOOO00OOO0O0OOO )#line:292
def update_group_ids ():#line:295
    try :#line:296
        with open ("token.txt")as OOOOO0OO0OO0O0O0O :#line:297
            O0OO000OO0O0O000O =[OOOOO0OO0OO0OOOO0 .strip ()for OOOOO0OO0OO0OOOO0 in OOOOO0OO0OO0O0O0O .readlines ()if OOOOO0OO0OO0OOOO0 .strip ()]#line:298
        OO0000000OOOO0OO0 =O0OO000OO0O0O000O [0 ]#line:299
    except (FileNotFoundError ,KeyError ):#line:300
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:301
        return #line:302
    O00OO00OO0OO0O000 ={"Authorization":OO0000000OOOO0OO0 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:308
    OOO0O00000OO00O0O =requests .get ('https://discord.com/api/v9/users/@me/channels',headers =O00OO00OO0OO0O000 )#line:310
    if OOO0O00000OO00O0O .status_code ==200 :#line:311
        OO000O00O0O0OOOO0 =OOO0O00000OO00O0O .json ()#line:312
        with open ("group_id.txt","w")as O0OOO0OO0OO0OOO00 :#line:313
            for O00O00OOOO0O00O0O in OO000O00O0O0OOOO0 :#line:314
                if O00O00OOOO0O00O0O ['type']==3 :#line:315
                    O0OOO0OO0OO0OOO00 .write (O00O00OOOO0O00O0O ['id']+'\n')#line:316
        print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Group IDs updated successfully.{colorama.Fore.RESET}")#line:317
    else :#line:318
        print (f"{colorama.Fore.LIGHTRED_EX}    [!] Failed to retrieve group IDs. HTTP Status Code: {OOO0O00000OO00O0O.status_code}{colorama.Fore.RESET}")#line:319
import requests #line:321
import requests #line:323
def fetch_channels (O0OO00OO0OO00OO00 ,O000O0OO0OO00000O ):#line:325
    try :#line:326
        OOOOO000O00OO0O00 =requests .Session ()#line:327
        O00OOO0O0OOOOOO00 =get_headers (O0OO00OO0OO00OO00 )#line:328
        OOOO00OO00000O000 =OOOOO000O00OO0O00 .get (f"https://discord.com/api/v9/guilds/{O000O0OO0OO00000O}/channels",headers =O00OOO0O0OOOOOO00 ,timeout =10 )#line:335
        if OOOO00OO00000O000 .status_code ==200 :#line:338
            try :#line:339
                O0O0OO00O00OO0OOO =OOOO00OO00000O000 .json ()#line:340
                return [OO00O0O0OOO0O0OOO ['id']for OO00O0O0OOO0O0OOO in O0O0OO00O00OO0OOO if OO00O0O0OOO0O0OOO .get ('type')==0 ]#line:341
            except ValueError :#line:342
                print ("[!] Error: Response was not valid JSON.")#line:343
                return []#line:344
        elif OOOO00OO00000O000 .status_code ==401 :#line:345
            print ("[!] Error: Unauthorized - check your token.")#line:346
        elif OOOO00OO00000O000 .status_code ==403 :#line:347
            print ("[!] Error: Forbidden - you lack permissions.")#line:348
        elif OOOO00OO00000O000 .status_code ==404 :#line:349
            print ("[!] Error: Server not found - check the server ID.")#line:350
        else :#line:351
            print (f"[!] Error: Unexpected status code {OOOO00OO00000O000.status_code}.")#line:352
        return []#line:355
    except requests .exceptions .Timeout :#line:357
        print ("[!] Error: Request timed out. Check your connection or try again later.")#line:358
        return []#line:359
    except requests .exceptions .RequestException as OO000O000O00O0OO0 :#line:360
        print (f"[!] Error: An error occurred while fetching channels: {OO000O000O00O0OO0}")#line:361
        return []#line:362
def extract_uids_from_messages (O000OO00000OO0OO0 ):#line:368
    O0O0OOOOO00O0OOO0 =set ()#line:369
    for OO00000OOO0O0OOO0 in O000OO00000OO0OO0 :#line:370
        O0O0OOOOO00O0OOO0 .add (OO00000OOO0O0OOO0 ['author']['id'])#line:371
    return list (O0O0OOOOO00O0OOO0 )#line:372
def send_message_with_mention (OOOO0OOO0000O00OO ,O00OO00O000000OOO ,OO000O0O000OOO0O0 ,OO0OOOOO00OO0000O ):#line:374
    OO0O00OO00O00O0O0 =get_session ()#line:375
    OOOO0O000OO0O0OOO =get_headers (OOOO0OOO0000O00OO )#line:376
    if OO0OOOOO00OO0000O :#line:378
        OO00O000O0O00OO0O =random .choice (OO0OOOOO00OO0000O )#line:379
        OO000O0O000OOO0O0 +=f" <@{OO00O000O0O00OO0O}>"#line:380
    OO0OO0000O00OO0OO =OO0O00OO00O00O0O0 .post (f"https://discord.com/api/v9/channels/{O00OO00O000000OOO}/messages",headers =OOOO0O000OO0O0OOO ,json ={"content":OO000O0O000OOO0O0 })#line:386
    if OO0OO0000O00OO0OO .status_code in [200 ,201 ]:#line:387
        print (f"[+] Message sent to channel {O00OO00O000000OOO}")#line:388
    elif OO0OO0000O00OO0OO .status_code ==429 :#line:389
        print ("[-] Rate limited. Please wait before retrying.")#line:390
        OOOO00000OOOO0O0O =OO0OO0000O00OO0OO .json ().get ("retry_after",1 )#line:391
        time .sleep (OOOO00000OOOO0O0O )#line:392
    else :#line:393
        print (f"[!] Error occurred: {OO0OO0000O00OO0OO.status_code}")#line:394
def send_messages_with_mentions ():#line:395
    try :#line:396
        with open ("token.txt")as OOOOOO00O00OOOO00 :#line:397
            O0O0OO00O0O000000 =[O00000O0O00O000OO .strip ()for O00000O0O00O000OO in OOOOOO00O00OOOO00 .readlines ()if O00000O0O00O000OO .strip ()]#line:398
    except (FileNotFoundError ,KeyError ):#line:399
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:400
        return #line:401
    O0OO0OO00000O00O0 =input ("Server ID?: ").strip ()#line:403
    OOO000O00O0O000OO =input ("Delay between messages (in seconds)?: ").strip ()#line:404
    OO000OOO0OO00OOOO =input ("Number of messages to send?: ").strip ()#line:405
    O00000OOO00000000 =input ("Message content?: ").strip ()#line:406
    O00OOO0O0OO00000O =input ("Blacklist User IDs (comma-separated)?: ").strip ().split (',')#line:407
    O00OOO0O0OO00000O =[OOOOO0O0O0OOOO000 .strip ()for OOOOO0O0O0OOOO000 in O00OOO0O0OO00000O if OOOOO0O0O0OOOO000 .strip ()]#line:408
    try :#line:410
        OOO000O00O0O000OO =float (OOO000O00O0O000OO )#line:411
        if OOO000O00O0O000OO <0 :#line:412
            raise ValueError #line:413
    except ValueError :#line:414
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:415
        OOO000O00O0O000OO =1.0 #line:416
    try :#line:418
        OO000OOO0OO00OOOO =int (OO000OOO0OO00OOOO )#line:419
        if OO000OOO0OO00OOOO <=0 :#line:420
            raise ValueError #line:421
    except ValueError :#line:422
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:423
        OO000OOO0OO00OOOO =1 #line:424
    O00O00OOOO000000O =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:426
    if O00O00OOOO000000O =='2':#line:427
        O00O00O0O0OOOOOOO =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:428
        O00O00O0O0OOOOOOO =[OO00OOO00OO0OOOOO .strip ()for OO00OOO00OO0OOOOO in O00O00O0O0OOOOOOO if OO00OOO00OO0OOOOO .strip ()]#line:429
    else :#line:430
        O00O00O0O0OOOOOOO =[]#line:431
    OO00O0O0O0OOOO00O =set ()#line:433
    for OO00000O000OOO000 in O0O0OO00O0O000000 :#line:434
        O0O0O000O0000O0O0 =fetch_channels (OO00000O000OOO000 ,O0OO0OO00000O00O0 )#line:435
        for OO0OOO000000O0000 in O0O0O000O0000O0O0 :#line:436
            O0000O0O00O00O0O0 =fetch_messages (OO00000O000OOO000 ,OO0OOO000000O0000 ,limit =100 )#line:437
            OOOO000O0000O0OOO =extract_uids_from_messages (O0000O0O00O00O0O0 )#line:438
            OO00O0O0O0OOOO00O .update (OOOO000O0000O0OOO )#line:439
    OO00O0O0O0OOOO00O =list (set (OO00O0O0O0OOOO00O )-set (O00OOO0O0OO00000O ))#line:442
    for _OO0OOO0000O0OOOOO in range (OO000OOO0OO00OOOO ):#line:444
        for OO00000O000OOO000 in O0O0OO00O0O000000 :#line:445
            if O00O00O0O0OOOOOOO :#line:446
                O0O0O000O0000O0O0 =O00O00O0O0OOOOOOO #line:447
            for OO0OOO000000O0000 in O0O0O000O0000O0O0 :#line:448
                send_message_with_mention (OO00000O000OOO000 ,OO0OOO000000O0000 ,O00000OOO00000000 ,OO00O0O0O0OOOO00O )#line:449
                time .sleep (OOO000O00O0O000OO )#line:450
def join_discord_invite ():#line:455
    try :#line:456
        with open ("token.txt")as O0OO0OOO0O0O0O00O :#line:457
            OO0000O00000OO0OO =[OOOO0OOO000O0OO0O .strip ()for OOOO0OOO000O0OO0O in O0OO0OOO0O0O0O00O .readlines ()if OOOO0OOO000O0OO0O .strip ()]#line:458
    except (FileNotFoundError ,KeyError ):#line:459
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:460
        return #line:461
    O00O00O000000OO0O =input ("Invite Code?: discord.gg/").strip ()#line:463
    for OO00OO0O00OO00000 in OO0000O00000OO0OO :#line:466
        joiner (OO00OO0O00OO00000 ,O00O00O000000OO0O )#line:467
import json ,time ,base64 ,random ,requests #line:469
def cookieset (O00O0O0OO00OO0000 ):#line:471
    OOO0000OOO00O000O =O00O0O0OO00OO0000 .get ("https://discord.com/app")#line:472
    return OOO0000OOO00O000O .cookies .get_dict ()#line:473
def generatexspandua (OO0OOO00OOOO0OOOO ):#line:475
    OO0OO0OOO0O0OO000 =["Android","Windows","Macintosh"]#line:476
    O0OO0000000OO0000 =random .choice (OO0OO0OOO0O0OO000 )#line:477
    if O0OO0000000OO0000 =="Macintosh":#line:478
        O0O000O000O0O0000 =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:479
        OO0OO0O000O00O000 ="Macintosh; Intel Mac OS X "+O0O000O000O0O0000 #line:480
        O0OO00OOO00OOOO00 ="x86_64"#line:481
    elif O0OO0000000OO0000 =="Windows":#line:482
        O0O000O000O0O0000 =f'{random.choice([6.0, 10.0, 11.0])}'#line:483
        OO0OO0O000O00O000 ="Windows NT "+O0O000O000O0O0000 +" Win64; x64"#line:484
        O0OO00OOO00OOOO00 ="x86_64"#line:485
    else :#line:486
        O0O000O000O0O0000 ="13"#line:487
        OO0OO0O000O00O000 =f"Linux; Android 13; Pixel 6a"#line:488
        O0OO00OOO00OOOO00 ="aarch64"#line:489
    OO0O0O000O00O00O0 ={"os":O0OO0000000OO0000 ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":O0O000O000O0O0000 ,"os_arch":O0OO00OOO00OOOO00 ,"system_locale":"ja-JP","client_build_number":OO0OOO00OOOO0OOOO ,"client_event_source":None ,"design_id":0 }#line:502
    O0OOOO000OOOOOOO0 =f"Mozilla/5.0 ({OO0OO0O000O00O000}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:503
    return base64 .b64encode (json .dumps (OO0O0O000O00O00O0 ,separators =(',',':')).encode ()).decode (),O0OOOO000OOOOOOO0 #line:504
def joiner (O0O0O00OO0OOO0OO0 ,O0OOOOO000OOOO0O0 ,O0OOOOOO0O0OOOO0O ):#line:506
    O0O0O0O00O0OO0000 =cookieset (O0OOOOOO0O0OOOO0O )#line:507
    O0O0O0O00O0OO0000 ["locale"]="ja-JP"#line:508
    OO00OOO00O0O0OOOO =201211 #line:509
    O0OO0OOO000000O0O ,OOOO00O0O00O00OO0 =generatexspandua (OO00OOO00O0O0OOOO )#line:510
    OOO0OO0OO00000O00 ={"Authorization":O0O0O00OO0OOO0OO0 ,"accept":"*/*","accept-language":"ja-JP","connection":"keep-alive","DNT":"1","origin":"https://discord.com","sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","referer":"https://discord.com/channels/@me","TE":"Trailers","user-agent":OOOO00O0O00O00OO0 ,"X-Super-Properties":O0OO0OOO000000O0O ,}#line:525
    OOO00OO00O000O00O =O0OOOOOO0O0OOOO0O .post ("https://discord.com/api/v9/invites/"+O0OOOOO000OOOO0O0 ,headers =OOO0OO0OO00000O00 ,json ={},cookies =O0O0O0O00O0OO0000 )#line:526
    if OOO00OO00O000O00O .status_code ==200 :#line:527
        print ("[+] join this server "+O0O0O00OO0OOO0OO0 )#line:528
        if "show_verification_form"in OOO00OO00O000O00O .json ():#line:529
            bypass (O0O0O00OO0OOO0OO0 ,OOO00OO00O000O00O .json ()["guild"]["id"],O0OOOOOO0O0OOOO0O ,OOO0OO0OO00000O00 )#line:530
        return #line:531
    elif "captcha_key"in OOO00OO00O000O00O .text and OOO00OO00O000O00O .status_code ==400 :#line:532
        print ("[!] Hcaptcha protect"+O0O0O00OO0OOO0OO0 )#line:533
        return #line:534
    elif OOO00OO00O000O00O .status_code ==401 :#line:535
        print ("[×] token is dead"+O0O0O00OO0OOO0OO0 )#line:536
        return #line:537
    elif OOO00OO00O000O00O .status_code ==403 :#line:538
        print ("[!] 403 banned "+O0O0O00OO0OOO0OO0 )#line:539
        return #line:540
    elif OOO00OO00O000O00O .status_code ==429 :#line:541
        OO000OOO0O00O0OOO =OOO00OO00O000O00O .json ().get ("retry_after",1 )#line:542
        print (f"[!] 429 rate limit. Retrying after {OO000OOO0O00O0OOO} seconds.")#line:543
        time .sleep (OO000OOO0O00O0OOO )#line:544
        return #line:545
    else :#line:546
        print ("[!] error "+O0O0O00OO0OOO0OO0 )#line:547
        return #line:548
def update_group_ids ():#line:550
    OOO0OO0000OOOOOO0 =input ("Invite Code?: ").strip ()#line:551
    try :#line:552
        with open ("token.txt")as OO0O0OO0OOOOO00OO :#line:553
            O00000OOOO00OO00O =[O00OO0O0OO00O00O0 .strip ()for O00OO0O0OO00O00O0 in OO0O0OO0OOOOO00OO .readlines ()if O00OO0O0OO00O00O0 .strip ()]#line:554
    except (FileNotFoundError ,KeyError ):#line:555
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:556
        return #line:557
    O0OO000O0OOO0OOOO =requests .Session ()#line:559
    for OOOOO0O0OO0O00000 in O00000OOOO00OO00O :#line:560
        joiner (OOOOO0O0OO0O00000 ,OOO0OO0000OOOOOO0 ,O0OO000O0OOO0OOOO )#line:561
        time .sleep (2 )#line:562
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:564
def bypass (O000OOOOO00OOOOOO ,OO000OOOOO000OOO0 ,OOO0O000OO0OOOO0O ,O00OOO00O00OOO0O0 ):#line:567
    try :#line:568
        O0O0OO0OO0O0OO000 =OOO0O000OO0OOOO0O .get (f"https://discord.com/api/v9/guilds/{OO000OOOOO000OOO0}/member-verification?with_guild=false",headers =O00OOO00O00OOO0O0 ).json ()#line:569
        OO000000OO0O0OO0O =OOO0O000OO0OOOO0O .put (f"https://discord.com/api/v9/guilds/{OO000OOOOO000OOO0}/requests/@me",headers =O00OOO00O00OOO0O0 ,json =O0O0OO0OO0O0OO000 )#line:570
        if OO000000OO0O0OO0O .status_code ==201 :#line:571
            print (f"[+] MemberscreeningBypassed {O000OOOOO00OOOOOO}")#line:572
            return #line:573
        else :#line:574
            print (f"[!] Bypassが出来ませんでした {O000OOOOO00OOOOOO}")#line:575
            return #line:576
    except Exception as OO00O0O0O000OO000 :#line:577
        print (f"[!] エラーが発生しました。{OO00O0O0O000OO000}")#line:578
session =requests .Session ()#line:580
def reactionput (O00O000OO00O0O000 ,O00OOOO0000000O0O ,O0OO000OOOOO00OO0 ,O00O0O00000OO0000 ,proxy =None ):#line:583
    O0O00OOO0O0OOOOOO =get_session (proxy )#line:584
    O00000OO0OOO00O00 =get_headers (O0O00OOO0O0OOOOOO )#line:585
    O00000OO0OOO00O00 ["Authorization"]=O00O000OO00O0O000 #line:586
    O00O0O00000OO0000 =requests .utils .quote (O00O0O00000OO0000 )#line:588
    OO0OO00000000O000 =O0O00OOO0O0OOOOOO .put (f"https://discord.com/api/v9/channels/{O00OOOO0000000O0O}/messages/{O0OO000OOOOO00OO0}/reactions/{O00O0O00000OO0000}/%40me?location=Message&type=0",headers =O00000OO0OOO00O00 )#line:592
    if OO0OO00000000O000 .status_code in [200 ,204 ]:#line:593
        print (f"[+] Reaction '{O00O0O00000OO0000}' added successfully to message {O0OO000OOOOO00OO0}")#line:594
    elif OO0OO00000000O000 .status_code ==429 :#line:595
        print ("[-] Rate limited. Please wait before retrying.")#line:596
        O000OOO0OOOO0O0O0 =OO0OO00000000O000 .json ().get ("retry_after",1 )#line:597
        time .sleep (O000OOO0OOOO0O0O0 )#line:598
    elif OO0OO00000000O000 .status_code ==401 :#line:599
        print ("[-] Invalid or expired token.")#line:600
    else :#line:601
        print (f"[!] Error occurred: {OO0OO00000000O000.status_code}")#line:602
def generatexspandua (O00000O00OOOO00OO ):#line:605
  O00OO000OOOOOOO00 =["Android","Windows","Macintosh"]#line:606
  OO0OO0O00OOO00O0O =random .choice (O00OO000OOOOOOO00 )#line:607
  if OO0OO0O00OOO00O0O =="Macintosh":#line:608
    O00O0OOO0OOO0OOOO =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:609
    OOO000O0O00OOO0OO ="Macintosh; Intel Mac OS X "+O00O0OOO0OOO0OOOO #line:610
    O0O00O000O00OO00O ="x86_64"#line:611
  if OO0OO0O00OOO00O0O =="Windows":#line:612
    O00O0OOO0OOO0OOOO =f'{random.choice([6.0,10.0,11.0])}'#line:613
    OOO000O0O00OOO0OO ="Windows NT "+O00O0OOO0OOO0OOOO +" Win64; x64"#line:614
    O0O00O000O00OO00O ="x86_64"#line:615
  if OO0OO0O00OOO00O0O =="Android":#line:616
    O00O0OOO0OOO0OOOO ="13"#line:617
    OOO000O0O00OOO0OO =f"Linux; Android 13; Pixel 6a"#line:618
    O0O00O000O00OO00O ="aarch64"#line:619
  OOOO000OO0O00OO00 ={"os":OO0OO0O00OOO00O0O ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":O00O0OOO0OOO0OOOO ,"os_arch":O0O00O000O00OO00O ,"system_locale":"ja-JP","client_build_number":O00000O00OOOO00OO ,"client_event_source":None ,"design_id":0 }#line:620
  O000OOOO00O000O00 =f"Mozilla/5.0 ({OOO000O0O00OOO0OO}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:621
  return base64 .b64encode (json .dumps (OOOO000OO0O00OO00 ,separators =(',',':')).encode ()).decode (),O000OOOO00O000O00 #line:622
import base64 #line:624
def nickchanger ():#line:627
    try :#line:628
        with open ("token.txt")as O000OOO00000O0OOO :#line:629
            O0OO0O0O0OOO0O000 =[OO00O0OO00O0000O0 .strip ()for OO00O0OO00O0000O0 in O000OOO00000O0OOO .readlines ()if OO00O0OO00O0000O0 .strip ()]#line:630
    except (FileNotFoundError ,KeyError ):#line:631
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:632
        return #line:633
    O0O00O00OO0OOO00O =input ("Server ID?: ").strip ()#line:635
    OO0OOO00OOOOO0OOO =input ("Nickname?: ").strip ()#line:636
    O0O0OOO00O00OO000 =input ("Delay (in seconds)?: ").strip ()#line:637
    try :#line:639
        O0O0OOO00O00OO000 =float (O0O0OOO00O00OO000 )#line:640
        if O0O0OOO00O00OO000 <0 :#line:641
            raise ValueError #line:642
    except ValueError :#line:643
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:644
        O0O0OOO00O00OO000 =1.0 #line:645
    for OOOOO000OOO0O000O in O0OO0O0O0OOO0O000 :#line:647
        O0OO00OO0OOO0000O ={"Authorization":OOOOO000OOO0O000O ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:652
        O0OO0OOOO0OOOOOO0 ={"nick":OO0OOO00OOOOO0OOO }#line:653
        O0OO00OOOOO0O0000 =requests .patch (f"https://discord.com/api/v9/guilds/{O0O00O00OO0OOO00O}/members/@me",headers =O0OO00OO0OOO0000O ,json =O0OO0OOOO0OOOOOO0 )#line:654
        if O0OO00OOOOO0O0000 .status_code ==200 :#line:656
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Nickname changed to '{OO0OOO00OOOOO0OOO}' successfully for token {OOOOO000OOO0O000O}.{colorama.Fore.RESET}")#line:657
        elif O0OO00OOOOO0O0000 .status_code ==429 :#line:658
            print (f"{colorama.Fore.RED}    [!] Rate limited. Please wait before retrying for token {OOOOO000OOO0O000O}.{colorama.Fore.RESET}")#line:659
            O0000OOO00O0OO00O =O0OO00OOOOO0O0000 .json ().get ("retry_after",1 )#line:660
            time .sleep (O0000OOO00O0OO00O )#line:661
        else :#line:662
            print (f"{colorama.Fore.RED}    [!] Error occurred: {O0OO00OOOOO0O0000.status_code} for token {OOOOO000OOO0O000O}.{colorama.Fore.RESET}")#line:663
        time .sleep (O0O0OOO00O00OO000 )#line:665
import json ,websocket ,threading ,tls_client ,random ,time #line:669
session =tls_client .Session (client_identifier ="chrome112",random_tls_extension_order =True )#line:671
class Utils :#line:673
    @staticmethod #line:674
    def rangeCorrector (O0O000000O000OO00 ):#line:675
        if [0 ,99 ]not in O0O000000O000OO00 :#line:676
            O0O000000O000OO00 .insert (0 ,[0 ,99 ])#line:677
        return O0O000000O000OO00 #line:678
    @staticmethod #line:680
    def getRanges (O00OOO0000O000O00 ,OO00O00OOOO0OO0O0 ,O0000O0OOO00OO00O ):#line:681
        O0OOO0O0OO0OO00O0 =int (O00OOO0000O000O00 *OO00O00OOOO0OO0O0 )#line:682
        OOO00O00OO0O00O00 =[[O0OOO0O0OO0OO00O0 ,O0OOO0O0OO0OO00O0 +99 ]]#line:683
        if O0000O0OOO00OO00O >O0OOO0O0OO0OO00O0 +99 :#line:684
            OOO00O00OO0O00O00 .append ([O0OOO0O0OO0OO00O0 +100 ,O0OOO0O0OO0OO00O0 +199 ])#line:685
        return Utils .rangeCorrector (OOO00O00OO0O00O00 )#line:686
    @staticmethod #line:688
    def parseGuildMemberListUpdate (OOO00O000O0OOOOO0 ):#line:689
        O00O0O0OO0O000O00 ={"online_count":OOO00O000O0OOOOO0 ["d"]["online_count"],"member_count":OOO00O000O0OOOOO0 ["d"]["member_count"],"id":OOO00O000O0OOOOO0 ["d"]["id"],"guild_id":OOO00O000O0OOOOO0 ["d"]["guild_id"],"hoisted_roles":OOO00O000O0OOOOO0 ["d"]["groups"],"types":[],"locations":[],"updates":[],}#line:699
        for O0OO00OO0O0O0000O in OOO00O000O0OOOOO0 ["d"]["ops"]:#line:701
            O00O0O0OO0O000O00 ["types"].append (O0OO00OO0O0O0000O ["op"])#line:702
            if O0OO00OO0O0O0000O ["op"]in ("SYNC","INVALIDATE"):#line:703
                O00O0O0OO0O000O00 ["locations"].append (O0OO00OO0O0O0000O ["range"])#line:704
                if O0OO00OO0O0O0000O ["op"]=="SYNC":#line:705
                    O00O0O0OO0O000O00 ["updates"].append (O0OO00OO0O0O0000O ["items"])#line:706
                else :#line:707
                    O00O0O0OO0O000O00 ["updates"].append ([])#line:708
            elif O0OO00OO0O0O0000O ["op"]in ("INSERT","UPDATE","DELETE"):#line:709
                O00O0O0OO0O000O00 ["locations"].append (O0OO00OO0O0O0000O ["index"])#line:710
                if O0OO00OO0O0O0000O ["op"]=="DELETE":#line:711
                    O00O0O0OO0O000O00 ["updates"].append ([])#line:712
                else :#line:713
                    O00O0O0OO0O000O00 ["updates"].append (O0OO00OO0O0O0000O ["item"])#line:714
        return O00O0O0OO0O000O00 #line:715
class DiscordSocket (websocket .WebSocketApp ):#line:717
    def __init__ (OO0000O000O0OOOOO ,OO0O0OOOOO0OOO00O ,OO0O000OOO000O0O0 ,OOOO0OOOOOO000O0O ):#line:718
        OO0000O000O0OOOOO .token =OO0O0OOOOO0OOO00O #line:719
        OO0000O000O0OOOOO .guild_id =OO0O000OOO000O0O0 #line:720
        OO0000O000O0OOOOO .channel_id =OOOO0OOOOOO000O0O #line:721
        OO0000O000O0OOOOO .socket_headers ={"Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","Cache-Control":"no-cache","Pragma":"no-cache","Sec-WebSocket-Extensions":"permessage-deflate; client_max_window_bits","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",}#line:729
        super ().__init__ ("wss://gateway.discord.gg/?encoding=json&v=9",header =OO0000O000O0OOOOO .socket_headers ,on_open =lambda O0000OOOOOOOOOOO0 :OO0000O000O0OOOOO .sock_open (O0000OOOOOOOOOOO0 ),on_message =lambda O0O0OO0O0OO00000O ,O0O000O0O0000OOOO :OO0000O000O0OOOOO .sock_message (O0O0OO0O0OO00000O ,O0O000O0O0000OOOO ),on_close =lambda O0OO0O0OO0OO0000O ,OOOO00O0000000000 ,O0O000O0OOO0O0OOO :OO0000O000O0OOOOO .sock_close (O0OO0O0OO0OO0000O ,OOOO00O0000000000 ,O0O000O0OOO0O0OOO ),)#line:738
        OO0000O000O0OOOOO .endScraping =False #line:740
        OO0000O000O0OOOOO .guilds ={}#line:741
        OO0000O000O0OOOOO .members ={}#line:742
        OO0000O000O0OOOOO .ranges =[[0 ,0 ]]#line:743
        OO0000O000O0OOOOO .lastRange =0 #line:744
        OO0000O000O0OOOOO .packets_recv =0 #line:745
    def run (OOO0OO00O00O00O0O ):#line:747
        OOO0OO00O00O00O0O .run_forever ()#line:748
        return OOO0OO00O00O00O0O .members #line:749
    def scrapeUsers (OOOOO00OOOOO0OOO0 ):#line:751
        if not OOOOO00OOOOO0OOO0 .endScraping :#line:752
            OOOOO00OOOOO0OOO0 .send ('{"op":14,"d":{"guild_id":"'+OOOOO00OOOOO0OOO0 .guild_id +'","typing":true,"activities":true,"threads":true,"channels":{"'+OOOOO00OOOOO0OOO0 .channel_id +'":'+json .dumps (OOOOO00OOOOO0OOO0 .ranges )+"}}}")#line:761
    def sock_open (OOOO0O000OOOOOOO0 ,OO0O00OO0O000O000 ):#line:763
        OOOO0O000OOOOOOO0 .send ('{"op":2,"d":{"token":"'+OOOO0O000OOOOOOO0 .token +'","capabilities":125,"properties":{"os":"Windows NT","browser":"Chrome","device":"","system_locale":"it-IT","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36","browser_version":"119.0","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":103981,"client_event_source":null},"presence":{"status":"online","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}')#line:768
    def heartbeatThread (O00OO0OOOOO0O000O ,OOOO00OO0000O000O ):#line:770
        try :#line:771
            while True :#line:772
                O00OO0OOOOO0O000O .send ('{"op":1,"d":'+str (O00OO0OOOOO0O000O .packets_recv )+"}")#line:773
                time .sleep (OOOO00OO0000O000O )#line:774
        except Exception as OOO0OO000O0OOO000 :#line:775
            pass #line:776
    def sock_message (OO000O0OO00OOO0OO ,O0OOO00O0000OO000 ,OO0OO0O00OO00OO00 ):#line:778
        O00000OOO000O000O =json .loads (OO0OO0O00OO00OO00 )#line:779
        if O00000OOO000O000O is None :#line:780
            return #line:781
        if O00000OOO000O000O ["op"]!=11 :#line:782
            OO000O0OO00OOO0OO .packets_recv +=1 #line:783
        if O00000OOO000O000O ["op"]==10 :#line:784
            threading .Thread (target =OO000O0OO00OOO0OO .heartbeatThread ,args =(O00000OOO000O000O ["d"]["heartbeat_interval"]/1000 ,),daemon =True ,).start ()#line:789
        if O00000OOO000O000O ["t"]=="READY":#line:790
            for O00O00OOOOOO000OO in O00000OOO000O000O ["d"]["guilds"]:#line:791
                OO000O0OO00OOO0OO .guilds [O00O00OOOOOO000OO ["id"]]={"member_count":O00O00OOOOOO000OO ["member_count"]}#line:792
        if O00000OOO000O000O ["t"]=="READY_SUPPLEMENTAL":#line:793
            OO000O0OO00OOO0OO .ranges =Utils .getRanges (0 ,100 ,OO000O0OO00OOO0OO .guilds [OO000O0OO00OOO0OO .guild_id ]["member_count"])#line:796
            OO000O0OO00OOO0OO .scrapeUsers ()#line:797
        elif O00000OOO000O000O ["t"]=="GUILD_MEMBER_LIST_UPDATE":#line:798
            O00OO00OO0OOOOO00 =Utils .parseGuildMemberListUpdate (O00000OOO000O000O )#line:799
            if O00OO00OO0OOOOO00 ["guild_id"]==OO000O0OO00OOO0OO .guild_id and ("SYNC"in O00OO00OO0OOOOO00 ["types"]or "UPDATE"in O00OO00OO0OOOOO00 ["types"]):#line:803
                for O0O0O0OO00OOOOOOO ,OOOOO000O00O0O0O0 in enumerate (O00OO00OO0OOOOO00 ["types"]):#line:804
                    if OOOOO000O00O0O0O0 =="SYNC":#line:805
                        if len (O00OO00OO0OOOOO00 ["updates"][O0O0O0OO00OOOOOOO ])==0 :#line:806
                            OO000O0OO00OOO0OO .endScraping =True #line:807
                            break #line:808
                        for O000OOOOO00O0OO00 in O00OO00OO0OOOOO00 ["updates"][O0O0O0OO00OOOOOOO ]:#line:810
                            if "member"in O000OOOOO00O0OO00 :#line:811
                                O00OO00OO0O0OOOO0 =O000OOOOO00O0OO00 ["member"]#line:812
                                O0OO00000O00OOO0O ={"tag":O00OO00OO0O0OOOO0 ["user"]["username"]+"#"+O00OO00OO0O0OOOO0 ["user"]["discriminator"],"id":O00OO00OO0O0OOOO0 ["user"]["id"],}#line:818
                                if not O00OO00OO0O0OOOO0 ["user"].get ("bot"):#line:819
                                    OO000O0OO00OOO0OO .members [O00OO00OO0O0OOOO0 ["user"]["id"]]=O0OO00000O00OOO0O #line:820
                    elif OOOOO000O00O0O0O0 =="UPDATE":#line:822
                        for O000OOOOO00O0OO00 in O00OO00OO0OOOOO00 ["updates"][O0O0O0OO00OOOOOOO ]:#line:823
                            if "member"in O000OOOOO00O0OO00 :#line:824
                                O00OO00OO0O0OOOO0 =O000OOOOO00O0OO00 ["member"]#line:825
                                O0OO00000O00OOO0O ={"tag":O00OO00OO0O0OOOO0 ["user"]["username"]+"#"+O00OO00OO0O0OOOO0 ["user"]["discriminator"],"id":O00OO00OO0O0OOOO0 ["user"]["id"],}#line:831
                                if not O00OO00OO0O0OOOO0 ["user"].get ("bot"):#line:832
                                    OO000O0OO00OOO0OO .members [O00OO00OO0O0OOOO0 ["user"]["id"]]=O0OO00000O00OOO0O #line:833
                    OO000O0OO00OOO0OO .lastRange +=1 #line:835
                    OO000O0OO00OOO0OO .ranges =Utils .getRanges (OO000O0OO00OOO0OO .lastRange ,100 ,OO000O0OO00OOO0OO .guilds [OO000O0OO00OOO0OO .guild_id ]["member_count"])#line:838
                    time .sleep (0.45 )#line:839
                    OO000O0OO00OOO0OO .scrapeUsers ()#line:840
            if OO000O0OO00OOO0OO .endScraping :#line:842
                OO000O0OO00OOO0OO .close ()#line:843
    def sock_close (OO0OO00OOOOO0OO00 ,OO000000000O00OO0 ,OO0OOO0OOOO0OOO0O ,OO0OOO0O00000OO00 ):#line:845
        pass #line:846
def scrape (O0O000O0OO000O0O0 ,OOOOO000OO0O000OO ,OO0OOOOOO00O0OOOO ):#line:848
    O0000O0O0O00000OO =DiscordSocket (O0O000O0OO000O0O0 ,OOOOO000OO0O000OO ,OO0OOOOOO00O0OOOO )#line:849
    return O0000O0O0O00000OO .run ()#line:850
def member_scrape (O0O0OOO0O0000OOO0 ,OOO0OO0OOO0O0OO00 ,OO00000O00OO0O0O0 ):#line:852
    O000000000OOOOOOO =[]#line:853
    for OOO0OOO0O00OO0O0O in O0O0OOO0O0000OOO0 :#line:854
        OOO000OOO0OOOOO00 ={"Authorization":OOO0OOO0O00OO0O0O ,"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}#line:855
        O00000000O00OO000 =session .get (f"https://canary.discord.com/api/v9/guilds/{OOO0OO0OOO0O0OO00}",headers =OOO000OOO0OOOOO00 )#line:856
        if O00000000O00OO000 .status_code ==200 :#line:857
            O000000000OOOOOOO .append (OOO0OOO0O00OO0O0O )#line:858
            break #line:859
    if not O000000000OOOOOOO :#line:860
        print ("missing access")#line:861
    OOO0OOO0O00OO0O0O =random .choice (O000000000OOOOOOO )#line:863
    O00OOO00O0OO0000O =scrape (OOO0OOO0O00OO0O0O ,OOO0OO0OOO0O0OO00 ,OO00000O00OO0O0O0 )#line:864
    O0O0O000O0O0OO0OO =[f"<@{OO0000O0O000OOO0O}>"for OO0000O0O000OOO0O in [int (OO00O00O00OOO000O )for OO00O00O00OOO000O in O00OOO00O0OO0000O .keys ()]]#line:865
    print (f"[SUCCESS] {len(O0O0O000O0O0OO0OO)} scraped members")#line:866
    return O0O0O000O0O0OO0OO #line:867
def spammer_menu ():#line:869
    try :#line:870
        with open ("token.txt")as OO0O0OO0OOO00O00O :#line:871
            OO0OOOOO0O0O0O0O0 =[OO00OOOOO0000OOOO .strip ()for OO00OOOOO0000OOOO in OO0O0OO0OOO00O00O .readlines ()if OO00OOOOO0000OOOO .strip ()]#line:872
    except (FileNotFoundError ,KeyError ):#line:873
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:874
        return #line:875
    OOOOOO00OO000OO0O =input ("Server ID?: ").strip ()#line:877
    OOO0O0OO00OO0OO0O =input ("Message?: ").strip ()#line:878
    OO0OOOOO0OO0OO000 =input ("Random mention (True/False)?: ").strip ().lower ()=='true'#line:879
    O0OO000O0000OOO00 =input ("Delay between messages (in seconds)?: ").strip ()#line:880
    O00OO0O0OOO000OOO =input ("Number of messages to send?: ").strip ()#line:881
    O00O00000O0000OO0 =input ("Blacklist User IDs (comma-separated) (Leave blank to skip)?: ").strip ().split (',')#line:882
    O00O00000O0000OO0 =[f"<@{O000OOO0000OOO0OO.strip()}>"for O000OOO0000OOO0OO in O00O00000O0000OO0 if O000OOO0000OOO0OO .strip ()]#line:883
    try :#line:885
        O0OO000O0000OOO00 =float (O0OO000O0000OOO00 )#line:886
        if O0OO000O0000OOO00 <0 :#line:887
            raise ValueError #line:888
    except ValueError :#line:889
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:890
        O0OO000O0000OOO00 =1.0 #line:891
    try :#line:893
        O00OO0O0OOO000OOO =int (O00OO0O0OOO000OOO )#line:894
        if O00OO0O0OOO000OOO <=0 :#line:895
            raise ValueError #line:896
    except ValueError :#line:897
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:898
        O00OO0O0OOO000OOO =1 #line:899
    O000OOO00OO0OOOO0 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:901
    if O000OOO00OO0OOOO0 =='2':#line:902
        O0000OO000O000OO0 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:903
        O0000OO000O000OO0 =[OOOOO0OO00OO000O0 .strip ()for OOOOO0OO00OO000O0 in O0000OO000O000OO0 if OOOOO0OO00OO000O0 .strip ()]#line:904
    else :#line:905
        O0000OO000O000OO0 =fetch_channels (OO0OOOOO0O0O0O0O0 [0 ],OOOOOO00OO000OO0O )#line:906
    OO0O0O00OO0OOO0OO =None #line:908
    spammer (OO0OOOOO0O0O0O0O0 ,OOOOOO00OO000OO0O ,O0000OO000O000OO0 ,OOO0O0OO00OO0OO0O ,OO0OOOOO0OO0OO000 ,O00O00000O0000OO0 ,OO0O0O00OO0OOO0OO ,O00OO0O0OOO000OOO )#line:910
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:912
def spammer (O000OOOO00O0000O0 ,OOO0OOO00O0OO0O00 ,O00O0000O000O0O0O ,OO00000OO00O0O0OO ,OO0O0OOOO00OO0000 ,OOOO00O0OO0000OO0 ,O00O0O0O000000OOO ,O000O0O0O00OO000O ):#line:914
    OO00OOOOOO0OO000O =get_session (O00O0O0O000000OOO )#line:915
    O00O00000OO00O0O0 =0 #line:916
    OO000O0O00000O0O0 =member_scrape (O000OOOO00O0000O0 ,OOO0OOO00O0OO0O00 ,O00O0000O000O0O0O [0 ])#line:918
    OO000O0O00000O0O0 =[OOOOOO0OOO000O000 for OOOOOO0OOO000O000 in OO000O0O00000O0O0 if OOOOOO0OOO000O000 not in OOOO00O0OO0000OO0 ]#line:919
    for _O000OO00OO0000OOO in range (O000O0O0O00OO000O ):#line:921
        O00000000O0OOOOO0 =O000OOOO00O0000O0 [O00O00000OO00O0O0 ]#line:922
        OOOOOO0O0OOOOO0OO =get_headers (O00000000O0OOOOO0 )#line:923
        for O0OOO00OO00O0OO0O in O00O0000O000O0O0O :#line:924
            OOO000O00O0O0OO00 =OO00000OO00O0O0OO #line:925
            if OO0O0OOOO00OO0000 and OO000O0O00000O0O0 :#line:926
                O00OO00O0OOOO0OO0 =random .choice (OO000O0O00000O0O0 )#line:927
                OOO000O00O0O0OO00 +=f" {O00OO00O0OOOO0OO0}"#line:928
            O0OOO0OO0O00OO0O0 =OO00OOOOOO0OO000O .post (f"https://discord.com/api/v9/channels/{O0OOO00OO00O0OO0O}/messages",json ={"content":OOO000O00O0O0OO00 },headers =OOOOOO0O0OOOOO0OO )#line:930
            if O0OOO0OO0O00OO0O0 .status_code ==200 :#line:931
                print (f"200 message sent: {O00000000O0OOOOO0}")#line:932
            elif O0OOO0OO0O00OO0O0 .status_code ==429 :#line:933
                print (f"429 rate limit: {O00000000O0OOOOO0}")#line:934
                OO000OOO00000OOO0 =O0OOO0OO0O00OO0O0 .json ().get ("retry_after",1 )#line:935
                time .sleep (OO000OOO00000OOO0 )#line:936
            elif O0OOO0OO0O00OO0O0 .status_code ==401 :#line:937
                print (f"401 unknown token: {O00000000O0OOOOO0}")#line:938
            else :#line:939
                print (f"error: {O00000000O0OOOOO0}")#line:940
        O00O00000OO00O0O0 =(O00O00000OO00O0O0 +1 )%len (O000OOOO00O0000O0 )#line:942
        time .sleep (1 )#line:943
import requests #line:947
import base64 #line:948
import colorama #line:949
import time #line:950
def add_emojis_from_files ():#line:952
    try :#line:953
        with open ("emojiname.txt")as O000O00O0OOO0OO0O ,open ("emojiurl.txt")as O0OOO0OO0O000OOOO :#line:954
            O000OOO0O00000OOO =[O00OO0O00000O00O0 .strip ()for O00OO0O00000O00O0 in O000O00O0OOO0OO0O .read ().split (',')if O00OO0O00000O00O0 .strip ()]#line:955
            OOOOO000O0O000OOO =[O0000OO0O0000000O .strip ()for O0000OO0O0000000O in O0OOO0OO0O000OOOO .read ().split (',')if O0000OO0O0000000O .strip ()]#line:956
    except FileNotFoundError as OOOO00000OOO00OOO :#line:957
        print (f"{colorama.Fore.RED}    [!] Error: {str(OOOO00000OOO00OOO)}{colorama.Fore.RESET}")#line:958
        return #line:959
    if len (O000OOO0O00000OOO )!=len (OOOOO000O0O000OOO ):#line:961
        print (f"{colorama.Fore.RED}    [!] Error: The number of emoji names and URLs do not match!{colorama.Fore.RESET}")#line:962
        return #line:963
    try :#line:965
        with open ("token.txt")as OO00OOOO0OOOO0000 :#line:966
            OO000OOOOO0O00O0O =[OO0OO0OO0O0O00O0O .strip ()for OO0OO0OO0O0O00O0O in OO00OOOO0OOOO0000 .readlines ()if OO0OO0OO0O0O00O0O .strip ()]#line:967
    except FileNotFoundError as OOOO00000OOO00OOO :#line:968
        print (f"{colorama.Fore.RED}    [!] Error: {str(OOOO00000OOO00OOO)}{colorama.Fore.RESET}")#line:969
        return #line:970
    OO00O0O0OOO0OOOO0 =input ("Enter the Guild ID: ").strip ()#line:972
    O000OOOO00OO0000O =input ("Enter the rate limit between requests (in seconds): ").strip ()#line:973
    try :#line:975
        O000OOOO00OO0000O =float (O000OOOO00OO0000O )#line:976
        if O000OOOO00OO0000O <0 :#line:977
            raise ValueError #line:978
    except ValueError :#line:979
        print (f"{colorama.Fore.RED}    [!] Invalid rate limit. Using default rate limit of 5 seconds.{colorama.Fore.RESET}")#line:980
        O000OOOO00OO0000O =5.0 #line:981
    OOO0OOO000OO0O000 =set ()#line:983
    for O00O000OO00O0O00O in OO000OOOOO0O00O0O :#line:985
        O0O0OO00OO000OO00 ={'Authorization':O00O000OO00O0O00O ,'Content-Type':'application/json'}#line:989
        OOOOO0O0OO00OO000 =requests .get (f"https://discord.com/api/v9/guilds/{OO00O0O0OOO0OOOO0}/emojis",headers =O0O0OO00OO000OO00 )#line:992
        if OOOOO0O0OO00OO000 .status_code ==200 :#line:993
            O0O0OOO0O00O0OOO0 =OOOOO0O0OO00OO000 .json ()#line:994
            for OOOOO0O000OO000O0 in O0O0OOO0O00O0OOO0 :#line:995
                OOO0OOO000OO0O000 .add (OOOOO0O000OO000O0 ['name'])#line:996
        else :#line:997
            print (f"{colorama.Fore.RED}    [!] Error fetching existing emojis: {OOOOO0O0OO00OO000.status_code} - {OOOOO0O0OO00OO000.text}{colorama.Fore.RESET}")#line:998
            continue #line:999
    for O00OOO000000OOO00 ,OO0OOO0OO0O0O0O00 in zip (O000OOO0O00000OOO ,OOOOO000O0O000OOO ):#line:1001
        if O00OOO000000OOO00 in OOO0OOO000OO0O000 :#line:1002
            print (f"{colorama.Fore.YELLOW}    [*] Emoji '{O00OOO000000OOO00}' already exists. Skipping...{colorama.Fore.RESET}")#line:1003
            continue #line:1004
        for O00O000OO00O0O00O in OO000OOOOO0O00O0O :#line:1006
            try :#line:1007
                OOOOO0O0OO00OO000 =requests .get (OO0OOO0OO0O0O0O00 )#line:1008
                OOOOO0O0OO00OO000 .raise_for_status ()#line:1009
                O0O000OOO000OOOOO =OOOOO0O0OO00OO000 .content #line:1010
                O0O0000O0OOOO0O0O =base64 .b64encode (O0O000OOO000OOOOO ).decode ('utf-8')#line:1011
                O00O0OO0OOO0000O0 ={'name':O00OOO000000OOO00 ,'image':f"data:image/png;base64,{O0O0000O0OOOO0O0O}"}#line:1016
                O0O0OO00OO000OO00 ={'Authorization':O00O000OO00O0O00O ,'Content-Type':'application/json'}#line:1021
                O0O0OOO0O000O0000 =requests .post (f"https://discord.com/api/v9/guilds/{OO00O0O0OOO0OOOO0}/emojis",headers =O0O0OO00OO000OO00 ,json =O00O0OO0OOO0000O0 )#line:1023
                if O0O0OOO0O000O0000 .status_code ==201 :#line:1024
                    print (f"{colorama.Fore.GREEN}    [+] Successfully added emoji '{O00OOO000000OOO00}' with token {O00O000OO00O0O00O}{colorama.Fore.RESET}")#line:1025
                    OOO0OOO000OO0O000 .add (O00OOO000000OOO00 )#line:1026
                    break #line:1027
                else :#line:1028
                    print (f"{colorama.Fore.RED}    [!] Failed to add emoji '{O00OOO000000OOO00}' with token {O00O000OO00O0O00O}: {O0O0OOO0O000O0000.status_code} - {O0O0OOO0O000O0000.text}{colorama.Fore.RESET}")#line:1029
                time .sleep (O000OOOO00OO0000O )#line:1031
            except Exception as OOOO00000OOO00OOO :#line:1032
                print (f"{colorama.Fore.RED}    [!] Error adding emoji '{O00OOO000000OOO00}' with token {O00O000OO00O0O00O}: {str(OOOO00000OOO00OOO)}{colorama.Fore.RESET}")#line:1033
def main ():#line:1035
    colorama .init ()#line:1036
    while True :#line:1037
        logo ()#line:1038
        OOO00OO0000OO0O0O =input (f"{colorama.Fore.LIGHTMAGENTA_EX}    [Final] Select an option from above: ")#line:1039
        if OOO00OO0000OO0O0O =="0":#line:1041
            update_group_ids ()#line:1042
        elif OOO00OO0000OO0O0O =="1":#line:1043
            join_discord_invite ()#line:1044
        elif OOO00OO0000OO0O0O =="2":#line:1045
            reaction_spammer ()#line:1046
        elif OOO00OO0000OO0O0O =="3":#line:1047
            send_messages_with_mentions ()#line:1048
        elif OOO00OO0000OO0O0O =="4":#line:1049
            spammer_menu ()#line:1050
        elif OOO00OO0000OO0O0O =="5":#line:1051
            nickchanger ()#line:1052
        elif OOO00OO0000OO0O0O =="6":#line:1053
            add_emojis_from_files ()#line:1054
        elif OOO00OO0000OO0O0O =="7":#line:1055
            reaction_art ()#line:1056
        elif OOO00OO0000OO0O0O =="0":#line:1057
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [*] Exiting the application. Goodbye!{colorama.Fore.RESET}")#line:1058
            break #line:1059
        else :#line:1060
            print (f"{colorama.Fore.RED}    [!] Invalid option selected!{colorama.Fore.RESET}")#line:1061
        input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:1063
if __name__ =="__main__":#line:1065
    main ()#line:1066
