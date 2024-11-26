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
    O000000O0OO0OOOOO =requests .Session ()#line:57
    if proxy :#line:58
        O000000O0OO0OOOOO .proxies ={"http":proxy ,"https":proxy }#line:59
    return O000000O0OO0OOOOO #line:60
def get_headers (OOOO0OO0OO0O00OO0 ):#line:62
    return {"Authorization":OOOO0OO0OO0O00OO0 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:67
def send_message_with_mention (O0OO0O0OOOO00O0OO ,O0OOOOO0000O0O00O ,OO00000OO000OO00O ,O0OO0OO0OO00O0000 ):#line:70
    OOO0OO0OO00O0O0OO =get_session ()#line:71
    OO00O0O00OOO0OOOO =get_headers (O0OO0O0OOOO00O0OO )#line:72
    if O0OO0OO0OO00O0000 :#line:74
        OOOO0OO0O00O0OO00 =random .choice (O0OO0OO0OO00O0000 )#line:75
        OO00000OO000OO00O +=f" <@{OOOO0OO0O00O0OO00}>"#line:76
    OO00000OO00O00O0O =OOO0OO0OO00O0O0OO .post (f"https://discord.com/api/v9/channels/{O0OOOOO0000O0O00O}/messages",headers =OO00O0O00OOO0OOOO ,json ={"content":OO00000OO000OO00O })#line:82
    if OO00000OO00O00O0O .status_code in [200 ,201 ]:#line:83
        print (f"[+] Message sent to channel {O0OOOOO0000O0O00O}")#line:84
    elif OO00000OO00O00O0O .status_code ==429 :#line:85
        print ("[-] Rate limited. Please wait before retrying.")#line:86
        O00OOO0O00OOOO0O0 =OO00000OO00O00O0O .json ().get ("retry_after",1 )#line:87
        time .sleep (O00OOO0O00OOOO0O0 )#line:88
    else :#line:89
        print (f"[!] Error occurred: {OO00000OO00O00O0O.status_code}")#line:90
def fetch_messages (O0OO00O0OO00OOO00 ,OOOOOO0OOOO00O000 ,limit =100 ):#line:93
    O0O00O000OOO0OOOO ={"Authorization":O0OO00O0OO00OOO00 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:98
    OOO0O0OO0O00O0000 =requests .get (f"https://discord.com/api/v9/channels/{OOOOOO0OOOO00O000}/messages?limit={limit}",headers =O0O00O000OOO0OOOO )#line:102
    if OOO0O0OO0O00O0000 .status_code ==200 :#line:103
        return OOO0O0OO0O00O0000 .json ()#line:104
    else :#line:105
        print (f"[!] Failed to fetch messages. HTTP Status Code: {OOO0O0OO0O00O0000.status_code}")#line:106
        return []#line:107
import concurrent .futures #line:108
def reaction_spammer ():#line:110
    try :#line:111
        with open ("token.txt")as O0O000O0OO00O0OOO :#line:112
            OO0OO00OOOO0O0O0O =[O0OO00O00O000O0OO .strip ()for O0OO00O00O000O0OO in O0O000O0OO00O0OOO .readlines ()if O0OO00O00O000O0OO .strip ()]#line:113
    except (FileNotFoundError ,KeyError ):#line:114
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:115
        return #line:116
    O0O000O0O00OO0O0O =input ("Server ID?: ").strip ()#line:118
    O000OO0O0OOO0OO0O =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:120
    if O000OO0O0OOO0OO0O =='2':#line:121
        OOOOOOOOO0OOOOO00 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:122
        OO0OO0OO000O0O0OO =[O0OOO0O00O0000O00 .strip ()for O0OOO0O00O0000O00 in OOOOOOOOO0OOOOO00 if O0OOO0O00O0000O00 .strip ()]#line:123
    else :#line:124
        OO0OO0OO000O0O0OO =[]#line:125
        for O0O0000OO00OOOOOO in OO0OO00OOOO0O0O0O :#line:126
            try :#line:127
                OO0OO0OO000O0O0OO .extend (fetch_channels (O0O0000OO00OOOOOO ,O0O000O0O00OO0O0O ))#line:128
            except Exception as OOOO000000O0OOOO0 :#line:129
                print (f"[!] Failed to fetch channels for token. Error: {OOOO000000O0OOOO0}")#line:130
                continue #line:131
    O00OO0OOOO0OO0OOO =input ("Select your emoji (a, b, c, ... or custom emojis): ").strip ()#line:133
    O0O0OO0O0O00OOO00 =input ("Delay between reactions (in seconds)?: ").strip ()#line:134
    try :#line:136
        O0O0OO0O0O00OOO00 =float (O0O0OO0O0O00OOO00 )#line:137
        if O0O0OO0O0O00OOO00 <0 :#line:138
            raise ValueError #line:139
    except ValueError :#line:140
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:141
        O0O0OO0O0O00OOO00 =1.0 #line:142
    O0OOO00000OOOOOOO =[]#line:144
    for OOO0O00000OOO00OO in O00OO0OOOO0OO0OOO .split (","):#line:145
        OOO0O00000OOO00OO =OOO0O00000OOO00OO .strip ().lower ()#line:146
        if OOO0O00000OOO00OO in alphabet_to_flag :#line:147
            O0OOO00000OOOOOOO .append (alphabet_to_flag [OOO0O00000OOO00OO ])#line:148
        else :#line:149
            O0OOO00000OOOOOOO .append (OOO0O00000OOO00OO )#line:150
    if not O0OOO00000OOOOOOO :#line:152
        print (f"{colorama.Fore.RED}    [!] No valid emojis provided!{colorama.Fore.RESET}")#line:153
        return #line:154
import requests #line:156
import json #line:157
import time #line:158
import colorama #line:159
alphabet_to_flag ={'a':'🇦','b':'🇧','c':'🇨','d':'🇩','e':'🇪','f':'🇫','g':'🇬','h':'🇭','i':'🇮','j':'🇯','k':'🇰','l':'🇱','m':'🇲','n':'🇳','o':'🇴','p':'🇵','q':'🇶','r':'🇷','s':'🇸','t':'🇹','u':'🇺','v':'🇻','w':'🇼','x':'🇽','y':'🇾','z':'🇿'}#line:167
def fetch_channels (O0OO000OOOO000OOO ,O00OOO000O0000O0O ):#line:169
    OOO0O0O0OOO0OO00O =f"https://discord.com/api/v9/guilds/{O00OOO000O0000O0O}/channels"#line:170
    OOOOOOO00OO0O000O ={"Authorization":O0OO000OOOO000OOO }#line:171
    OOOO0OOOOOOO0O000 =requests .get (OOO0O0O0OOO0OO00O ,headers =OOOOOOO00OO0O000O )#line:172
    if OOOO0OOOOOOO0O000 .status_code ==200 :#line:173
        return [OOO0OOO000O0000OO ['id']for OOO0OOO000O0000OO in OOOO0OOOOOOO0O000 .json ()if OOO0OOO000O0000OO ['type']==0 ]#line:174
    else :#line:175
        raise Exception (f"Failed to fetch channels: {OOOO0OOOOOOO0O000.status_code} - {OOOO0OOOOOOO0O000.text}")#line:176
def fetch_messages (O0OO00OOOO0000O0O ,O0OOOO00O000O0OO0 ,limit =100 ):#line:178
    OO00O0O00O00O0000 =f"https://discord.com/api/v9/channels/{O0OOOO00O000O0OO0}/messages?limit={limit}"#line:179
    O0OOO00O00000OOO0 ={"Authorization":O0OO00OOOO0000O0O }#line:180
    OO000O0OOOOO0O0OO =requests .get (OO00O0O00O00O0000 ,headers =O0OOO00O00000OOO0 )#line:181
    if OO000O0OOOOO0O0OO .status_code ==200 :#line:182
        return OO000O0OOOOO0O0OO .json ()#line:183
    else :#line:184
        print (f"[!] Failed to fetch messages: {OO000O0OOOOO0O0OO.status_code} - {OO000O0OOOOO0O0OO.text}")#line:185
        return []#line:186
def reactionput (O00OO0OOO0000O0O0 ,OOO0OO000O00000O0 ,O00O000O000000OO0 ,O00O00OO000O00000 ):#line:188
    O0OO0O0O00OOOO00O =f"https://discord.com/api/v9/channels/{OOO0OO000O00000O0}/messages/{O00O000O000000OO0}/reactions/{O00O00OO000O00000}/@me"#line:189
    OO0OO0OO0O00O0000 ={"Authorization":O00OO0OOO0000O0O0 ,"Content-Type":"application/json"}#line:190
    OOOO00OO0OOOO00O0 =requests .put (O0OO0O0O00OOOO00O ,headers =OO0OO0OO0O00O0000 )#line:191
    if OOOO00OO0OOOO00O0 .status_code not in [204 ,200 ]:#line:192
        print (f"{colorama.Fore.RED}    [!] Failed to add reaction: {OOOO00OO0OOOO00O0.status_code} - {OOOO00OO0OOOO00O0.text}{colorama.Fore.RESET}")#line:193
def reaction_art ():#line:195
    try :#line:196
        with open ("token.txt",encoding ="utf-8")as OOOOOOOO0OOOOOOOO :#line:197
            O00OO00O0000OOO0O =[OOOO0000OO00O000O .strip ()for OOOO0000OO00O000O in OOOOOOOO0OOOOOOOO .readlines ()if OOOO0000OO00O000O .strip ()]#line:198
    except (FileNotFoundError ,KeyError ):#line:199
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:200
        return #line:201
    O000O0OO0OOO0O0O0 =input ("Server ID?: ").strip ()#line:203
    OOO00OOO0OO0O0O0O =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:205
    if OOO00OOO0OO0O0O0O =='2':#line:206
        O00OOO00O0OO0OO0O =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:207
        OOOOOO000O00000O0 =[O0OOO0OO00O0O0OOO .strip ()for O0OOO0OO00O0O0OOO in O00OOO00O0OO0OO0O if O0OOO0OO00O0O0OOO .strip ()]#line:208
    else :#line:209
        OOOOOO000O00000O0 =[]#line:210
        for O0OO0O00O00OO00O0 in O00OO00O0000OOO0O :#line:211
            try :#line:212
                OOOOOO000O00000O0 .extend (fetch_channels (O0OO0O00O00OO00O0 ,O000O0OO0OOO0O0O0 ))#line:213
            except Exception as OOO0OOO0OOOOOO000 :#line:214
                print (f"[!] Failed to fetch channels for token. Error: {OOO0OOO0OOOOOO000}")#line:215
                continue #line:216
    OO00O0OO000OO00O0 =input ("Delay between reactions (in seconds)?: ").strip ()#line:218
    try :#line:220
        OO00O0OO000OO00O0 =float (OO00O0OO000OO00O0 )#line:221
        if OO00O0OO000OO00O0 <0 :#line:222
            raise ValueError #line:223
    except ValueError :#line:224
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:225
        OO00O0OO000OO00O0 =1.0 #line:226
    try :#line:228
        with open ("art.txt",encoding ="utf-8")as OO0O0O00OOO00OO00 :#line:229
            OOOOO0O0000O0O0O0 =[O000O0OOOO0OOOO00 .strip ()for O000O0OOOO0OOOO00 in OO0O0O00OOO00OO00 .readlines ()if O000O0OOOO0OOOO00 .strip ()]#line:230
    except (FileNotFoundError ,KeyError ):#line:231
        print (f"{colorama.Fore.RED}    [!] Error: art.txt file not found or empty!{colorama.Fore.RESET}")#line:232
        return #line:233
    except UnicodeDecodeError as OOO0OOO0OOOOOO000 :#line:234
        print (f"{colorama.Fore.RED}    [!] Error decoding art.txt: {str(OOO0OOO0OOOOOO000)}{colorama.Fore.RESET}")#line:235
        return #line:236
    if not OOOOO0O0000O0O0O0 :#line:238
        print (f"{colorama.Fore.RED}    [!] No valid art provided in art.txt!{colorama.Fore.RESET}")#line:239
        return #line:240
    for O0OO0O00O00OO00O0 in O00OO00O0000OOO0O :#line:242
        for OO0OOO000OO000000 in OOOOOO000O00000O0 :#line:243
            try :#line:244
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {OO0OOO000OO000000}...{colorama.Fore.RESET}")#line:245
                O0O000OO0O0O0OO0O =fetch_messages (O0OO0O00O00OO00O0 ,OO0OOO000OO000000 ,limit =len (OOOOO0O0000O0O0O0 ))#line:246
                if not O0O000OO0O0O0OO0O :#line:247
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:248
                    continue #line:249
                for O0O0OOOO0OOO0O0OO ,O00OOOOO00OOO00OO in enumerate (O0O000OO0O0O0OO0O ):#line:251
                    O0OOO000O00000OOO =OOOOO0O0000O0O0O0 [O0O0OOOO0OOO0O0OO %len (OOOOO0O0000O0O0O0 )].split (',')#line:252
                    for O0000O0O0OOOO000O in O0OOO000O00000OOO :#line:253
                        reactionput (O0OO0O00O00OO00O0 ,OO0OOO000OO000000 ,O00OOOOO00OOO00OO ['id'],O0000O0O0OOOO000O .strip ())#line:254
                        print (f"Adding reaction '{O0000O0O0OOOO000O.strip()}' to message {O00OOOOO00OOO00OO['id']} in channel {OO0OOO000OO000000}")#line:255
                        time .sleep (OO00O0OO000OO00O0 )#line:256
            except Exception as OOO0OOO0OOOOOO000 :#line:257
                print (f"[!] Error processing channel {OO0OOO000OO000000}. Error: {OOO0OOO0OOOOOO000}")#line:258
                continue #line:259
    def OO00OOOO0000OO0OO (OOO0000OO0OOOO000 ):#line:264
        for O00O0000O000OO00O in OOOOOO000O00000O0 :#line:265
            try :#line:266
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {O00O0000O000OO00O}...{colorama.Fore.RESET}")#line:267
                OOOO000O0OOO00O0O =fetch_messages (OOO0000OO0OOOO000 ,O00O0000O000OO00O ,limit =100 )#line:268
                if not OOOO000O0OOO00O0O :#line:269
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:270
                    continue #line:271
                for OO0O000OOOO0O0000 in OOOO000O0OOO00O0O :#line:273
                    for O000OO0OOO0OO000O in O0OOO000O00000OOO :#line:274
                        reactionput (OOO0000OO0OOOO000 ,O00O0000O000OO00O ,OO0O000OOOO0O0000 ['id'],O000OO0OOO0OO000O )#line:275
                        time .sleep (OO00O0OO000OO00O0 )#line:276
            except Exception as OO000O0O0OO0000O0 :#line:277
                print (f"[!] Error processing channel {O00O0000O000OO00O}. Error: {OO000O0O0OO0000O0}")#line:278
                continue #line:279
    with concurrent .futures .ThreadPoolExecutor ()as OO0OOO000O0O0OOO0 :#line:281
        OOO0OOOO00OOOO000 =[OO0OOO000O0O0OOO0 .submit (OO00OOOO0000OO0OO ,O0000O0OOO00OOOOO )for O0000O0OOO00OOOOO in O00OO00O0000OOO0O ]#line:282
        concurrent .futures .wait (OOO0OOOO00OOOO000 )#line:283
def update_group_ids ():#line:286
    try :#line:287
        with open ("token.txt")as O000O000O0OO00O00 :#line:288
            O00O0OOO0O00000OO =[OOO00OOO00O0O0O0O .strip ()for OOO00OOO00O0O0O0O in O000O000O0OO00O00 .readlines ()if OOO00OOO00O0O0O0O .strip ()]#line:289
        O0O0000000OOO0OO0 =O00O0OOO0O00000OO [0 ]#line:290
    except (FileNotFoundError ,KeyError ):#line:291
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:292
        return #line:293
    OO0O00O000OO0OO00 ={"Authorization":O0O0000000OOO0OO0 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:299
    O0OO00OOO000O0O0O =requests .get ('https://discord.com/api/v9/users/@me/channels',headers =OO0O00O000OO0OO00 )#line:301
    if O0OO00OOO000O0O0O .status_code ==200 :#line:302
        OOOOO00O00OOO000O =O0OO00OOO000O0O0O .json ()#line:303
        with open ("group_id.txt","w")as O0000OO000O00OO0O :#line:304
            for OO0O0000O0000OOOO in OOOOO00O00OOO000O :#line:305
                if OO0O0000O0000OOOO ['type']==3 :#line:306
                    O0000OO000O00OO0O .write (OO0O0000O0000OOOO ['id']+'\n')#line:307
        print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Group IDs updated successfully.{colorama.Fore.RESET}")#line:308
    else :#line:309
        print (f"{colorama.Fore.LIGHTRED_EX}    [!] Failed to retrieve group IDs. HTTP Status Code: {O0OO00OOO000O0O0O.status_code}{colorama.Fore.RESET}")#line:310
import requests #line:312
import requests #line:314
def fetch_channels (OO0O00O0OO000OOOO ,OO00O0OOO0O0O0O0O ):#line:316
    try :#line:317
        OO0000O00O0OOOOO0 =requests .Session ()#line:318
        O0O0O0O0OOO0OO0OO =get_headers (OO0O00O0OO000OOOO )#line:319
        O000OOOOO00O0OO0O =OO0000O00O0OOOOO0 .get (f"https://discord.com/api/v9/guilds/{OO00O0OOO0O0O0O0O}/channels",headers =O0O0O0O0OOO0OO0OO ,timeout =10 )#line:326
        if O000OOOOO00O0OO0O .status_code ==200 :#line:329
            try :#line:330
                OOO0OOO0OOO0O0O0O =O000OOOOO00O0OO0O .json ()#line:331
                return [O00OOO000OO00O00O ['id']for O00OOO000OO00O00O in OOO0OOO0OOO0O0O0O if O00OOO000OO00O00O .get ('type')==0 ]#line:332
            except ValueError :#line:333
                print ("[!] Error: Response was not valid JSON.")#line:334
                return []#line:335
        elif O000OOOOO00O0OO0O .status_code ==401 :#line:336
            print ("[!] Error: Unauthorized - check your token.")#line:337
        elif O000OOOOO00O0OO0O .status_code ==403 :#line:338
            print ("[!] Error: Forbidden - you lack permissions.")#line:339
        elif O000OOOOO00O0OO0O .status_code ==404 :#line:340
            print ("[!] Error: Server not found - check the server ID.")#line:341
        else :#line:342
            print (f"[!] Error: Unexpected status code {O000OOOOO00O0OO0O.status_code}.")#line:343
        return []#line:346
    except requests .exceptions .Timeout :#line:348
        print ("[!] Error: Request timed out. Check your connection or try again later.")#line:349
        return []#line:350
    except requests .exceptions .RequestException as O0O0OO0OOOO0O00O0 :#line:351
        print (f"[!] Error: An error occurred while fetching channels: {O0O0OO0OOOO0O00O0}")#line:352
        return []#line:353
def extract_uids_from_messages (O0O0OO0OOO0OO00O0 ):#line:359
    OOO00OO00OO0O0OOO =set ()#line:360
    for OO00OO0OOOO0000O0 in O0O0OO0OOO0OO00O0 :#line:361
        OOO00OO00OO0O0OOO .add (OO00OO0OOOO0000O0 ['author']['id'])#line:362
    return list (OOO00OO00OO0O0OOO )#line:363
def send_message_with_mention (OOO0OOO00O0O00OO0 ,O0OO0000O0O0O0O00 ,OO0O0O0OO0OO00000 ,O00OO00OO00O0O00O ):#line:365
    O0000O0OO0O0OOOOO =get_session ()#line:366
    O0O00OO0O00OOO00O =get_headers (OOO0OOO00O0O00OO0 )#line:367
    if O00OO00OO00O0O00O :#line:369
        OO00O0OO0OOO0OO0O =random .choice (O00OO00OO00O0O00O )#line:370
        OO0O0O0OO0OO00000 +=f" <@{OO00O0OO0OOO0OO0O}>"#line:371
    O0OOOOOOO00OO0O00 =O0000O0OO0O0OOOOO .post (f"https://discord.com/api/v9/channels/{O0OO0000O0O0O0O00}/messages",headers =O0O00OO0O00OOO00O ,json ={"content":OO0O0O0OO0OO00000 })#line:377
    if O0OOOOOOO00OO0O00 .status_code in [200 ,201 ]:#line:378
        print (f"[+] Message sent to channel {O0OO0000O0O0O0O00}")#line:379
    elif O0OOOOOOO00OO0O00 .status_code ==429 :#line:380
        print ("[-] Rate limited. Please wait before retrying.")#line:381
        OO00OOO0OOOOOOOO0 =O0OOOOOOO00OO0O00 .json ().get ("retry_after",1 )#line:382
        time .sleep (OO00OOO0OOOOOOOO0 )#line:383
    else :#line:384
        print (f"[!] Error occurred: {O0OOOOOOO00OO0O00.status_code}")#line:385
def send_messages_with_mentions ():#line:386
    try :#line:387
        with open ("token.txt")as O0OOOO0OOOOOOOO0O :#line:388
            OO0OOO00OO0OOO0O0 =[O000OOO00000O0O00 .strip ()for O000OOO00000O0O00 in O0OOOO0OOOOOOOO0O .readlines ()if O000OOO00000O0O00 .strip ()]#line:389
    except (FileNotFoundError ,KeyError ):#line:390
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:391
        return #line:392
    OOOOOOOOOOO0O0OO0 =input ("Server ID?: ").strip ()#line:394
    OOO000OOOO00OOOO0 =input ("Delay between messages (in seconds)?: ").strip ()#line:395
    OO000000O0O00OOO0 =input ("Number of messages to send?: ").strip ()#line:396
    O000O0O0OO0000000 =input ("Message content?: ").strip ()#line:397
    OOOOO0OOO0O000O0O =input ("Blacklist User IDs (comma-separated)?: ").strip ().split (',')#line:398
    OOOOO0OOO0O000O0O =[OOOO0OO0OOOOO00OO .strip ()for OOOO0OO0OOOOO00OO in OOOOO0OOO0O000O0O if OOOO0OO0OOOOO00OO .strip ()]#line:399
    try :#line:401
        OOO000OOOO00OOOO0 =float (OOO000OOOO00OOOO0 )#line:402
        if OOO000OOOO00OOOO0 <0 :#line:403
            raise ValueError #line:404
    except ValueError :#line:405
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:406
        OOO000OOOO00OOOO0 =1.0 #line:407
    try :#line:409
        OO000000O0O00OOO0 =int (OO000000O0O00OOO0 )#line:410
        if OO000000O0O00OOO0 <=0 :#line:411
            raise ValueError #line:412
    except ValueError :#line:413
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:414
        OO000000O0O00OOO0 =1 #line:415
    OO00000O0O0OOO0O0 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:417
    if OO00000O0O0OOO0O0 =='2':#line:418
        O00OO00O0OOO00O0O =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:419
        O00OO00O0OOO00O0O =[O00OOO0OOOOO0O0O0 .strip ()for O00OOO0OOOOO0O0O0 in O00OO00O0OOO00O0O if O00OOO0OOOOO0O0O0 .strip ()]#line:420
    else :#line:421
        O00OO00O0OOO00O0O =[]#line:422
    O0OOO0OO00O000O00 =set ()#line:424
    for OOOO0000000OOOOO0 in OO0OOO00OO0OOO0O0 :#line:425
        OO0OO00O0000OOO0O =fetch_channels (OOOO0000000OOOOO0 ,OOOOOOOOOOO0O0OO0 )#line:426
        for O0O000O000OOOOO0O in OO0OO00O0000OOO0O :#line:427
            O000O0O0OO0O0OO00 =fetch_messages (OOOO0000000OOOOO0 ,O0O000O000OOOOO0O ,limit =100 )#line:428
            O0O00OO0000O0000O =extract_uids_from_messages (O000O0O0OO0O0OO00 )#line:429
            O0OOO0OO00O000O00 .update (O0O00OO0000O0000O )#line:430
    O0OOO0OO00O000O00 =list (set (O0OOO0OO00O000O00 )-set (OOOOO0OOO0O000O0O ))#line:433
    for _OOOO00OOO0O0OO00O in range (OO000000O0O00OOO0 ):#line:435
        for OOOO0000000OOOOO0 in OO0OOO00OO0OOO0O0 :#line:436
            if O00OO00O0OOO00O0O :#line:437
                OO0OO00O0000OOO0O =O00OO00O0OOO00O0O #line:438
            for O0O000O000OOOOO0O in OO0OO00O0000OOO0O :#line:439
                send_message_with_mention (OOOO0000000OOOOO0 ,O0O000O000OOOOO0O ,O000O0O0OO0000000 ,O0OOO0OO00O000O00 )#line:440
                time .sleep (OOO000OOOO00OOOO0 )#line:441
def join_discord_invite ():#line:446
    try :#line:447
        with open ("token.txt")as OO00O0OOO000OO000 :#line:448
            OO00OO000OOO0OOO0 =[OO0O0OO0OOOOOOO00 .strip ()for OO0O0OO0OOOOOOO00 in OO00O0OOO000OO000 .readlines ()if OO0O0OO0OOOOOOO00 .strip ()]#line:449
    except (FileNotFoundError ,KeyError ):#line:450
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:451
        return #line:452
    O000OOOOO0OOOOOO0 =input ("Invite Code?: discord.gg/").strip ()#line:454
    for OO0000000OOO0OOOO in OO00OO000OOO0OOO0 :#line:457
        joiner (OO0000000OOO0OOOO ,O000OOOOO0OOOOOO0 )#line:458
import json ,time ,base64 ,random ,requests #line:460
def cookieset (OOO00OO0000OOO0OO ):#line:462
    OO0O00O000OO0O000 =OOO00OO0000OOO0OO .get ("https://discord.com/app")#line:463
    return OO0O00O000OO0O000 .cookies .get_dict ()#line:464
def generatexspandua (O0O00OO000OO00O0O ):#line:466
    O0O00O000OO00O0O0 =["Android","Windows","Macintosh"]#line:467
    OOOOO0OO00O000OO0 =random .choice (O0O00O000OO00O0O0 )#line:468
    if OOOOO0OO00O000OO0 =="Macintosh":#line:469
        OO0O0000O0000O000 =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:470
        O0000OOO00OOOOO00 ="Macintosh; Intel Mac OS X "+OO0O0000O0000O000 #line:471
        O00OO00OO00OOO0OO ="x86_64"#line:472
    elif OOOOO0OO00O000OO0 =="Windows":#line:473
        OO0O0000O0000O000 =f'{random.choice([6.0, 10.0, 11.0])}'#line:474
        O0000OOO00OOOOO00 ="Windows NT "+OO0O0000O0000O000 +" Win64; x64"#line:475
        O00OO00OO00OOO0OO ="x86_64"#line:476
    else :#line:477
        OO0O0000O0000O000 ="13"#line:478
        O0000OOO00OOOOO00 =f"Linux; Android 13; Pixel 6a"#line:479
        O00OO00OO00OOO0OO ="aarch64"#line:480
    O00O00O00O00O0OOO ={"os":OOOOO0OO00O000OO0 ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":OO0O0000O0000O000 ,"os_arch":O00OO00OO00OOO0OO ,"system_locale":"ja-JP","client_build_number":O0O00OO000OO00O0O ,"client_event_source":None ,"design_id":0 }#line:493
    OO0000O0O000O0O00 =f"Mozilla/5.0 ({O0000OOO00OOOOO00}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:494
    return base64 .b64encode (json .dumps (O00O00O00O00O0OOO ,separators =(',',':')).encode ()).decode (),OO0000O0O000O0O00 #line:495
def joiner (O0O0OO0OOO0O0000O ,O0OOO00O00O0OO0OO ,O0OO0O00OOOO000O0 ):#line:497
    OO00OOOOOOO0OOOO0 =cookieset (O0OO0O00OOOO000O0 )#line:498
    OO00OOOOOOO0OOOO0 ["locale"]="ja-JP"#line:499
    O00OOOO0000O0OOOO =201211 #line:500
    OO00O0O00O0000000 ,OO0OOOOOO00000O00 =generatexspandua (O00OOOO0000O0OOOO )#line:501
    OOOOOO0O00O0OOO0O ={"Authorization":O0O0OO0OOO0O0000O ,"accept":"*/*","accept-language":"ja-JP","connection":"keep-alive","DNT":"1","origin":"https://discord.com","sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","referer":"https://discord.com/channels/@me","TE":"Trailers","user-agent":OO0OOOOOO00000O00 ,"X-Super-Properties":OO00O0O00O0000000 ,}#line:516
    OOOO0OO0O0O00OOOO =O0OO0O00OOOO000O0 .post ("https://discord.com/api/v9/invites/"+O0OOO00O00O0OO0OO ,headers =OOOOOO0O00O0OOO0O ,json ={},cookies =OO00OOOOOOO0OOOO0 )#line:517
    if OOOO0OO0O0O00OOOO .status_code ==200 :#line:518
        print ("[+] join this server "+O0O0OO0OOO0O0000O )#line:519
        if "show_verification_form"in OOOO0OO0O0O00OOOO .json ():#line:520
            bypass (O0O0OO0OOO0O0000O ,OOOO0OO0O0O00OOOO .json ()["guild"]["id"],O0OO0O00OOOO000O0 ,OOOOOO0O00O0OOO0O )#line:521
        return #line:522
    elif "captcha_key"in OOOO0OO0O0O00OOOO .text and OOOO0OO0O0O00OOOO .status_code ==400 :#line:523
        print ("[!] Hcaptcha protect"+O0O0OO0OOO0O0000O )#line:524
        return #line:525
    elif OOOO0OO0O0O00OOOO .status_code ==401 :#line:526
        print ("[×] token is dead"+O0O0OO0OOO0O0000O )#line:527
        return #line:528
    elif OOOO0OO0O0O00OOOO .status_code ==403 :#line:529
        print ("[!] 403 banned "+O0O0OO0OOO0O0000O )#line:530
        return #line:531
    elif OOOO0OO0O0O00OOOO .status_code ==429 :#line:532
        OOOO000OO0OO0OOOO =OOOO0OO0O0O00OOOO .json ().get ("retry_after",1 )#line:533
        print (f"[!] 429 rate limit. Retrying after {OOOO000OO0OO0OOOO} seconds.")#line:534
        time .sleep (OOOO000OO0OO0OOOO )#line:535
        return #line:536
    else :#line:537
        print ("[!] error "+O0O0OO0OOO0O0000O )#line:538
        return #line:539
def update_group_ids ():#line:541
    OOOO0O0OO00O0O0OO =input ("Invite Code?: ").strip ()#line:542
    try :#line:543
        with open ("token.txt")as O0000O00O0O00000O :#line:544
            O0O0000OOO0O0000O =[OOOOO0OOOOO0O0O00 .strip ()for OOOOO0OOOOO0O0O00 in O0000O00O0O00000O .readlines ()if OOOOO0OOOOO0O0O00 .strip ()]#line:545
    except (FileNotFoundError ,KeyError ):#line:546
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:547
        return #line:548
    OOOOOO0O0OOO00O0O =requests .Session ()#line:550
    for O000O00O0O0OOOOO0 in O0O0000OOO0O0000O :#line:551
        joiner (O000O00O0O0OOOOO0 ,OOOO0O0OO00O0O0OO ,OOOOOO0O0OOO00O0O )#line:552
        time .sleep (2 )#line:553
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:555
def bypass (O0O0000000000OOOO ,OOOOO0O0OO0000OOO ,OOO0O0O0O0000O000 ,O0O0OO0OO0OOOO0O0 ):#line:558
    try :#line:559
        O00OO00O0O0000OOO =OOO0O0O0O0000O000 .get (f"https://discord.com/api/v9/guilds/{OOOOO0O0OO0000OOO}/member-verification?with_guild=false",headers =O0O0OO0OO0OOOO0O0 ).json ()#line:560
        OO0000O0OOO0OOO0O =OOO0O0O0O0000O000 .put (f"https://discord.com/api/v9/guilds/{OOOOO0O0OO0000OOO}/requests/@me",headers =O0O0OO0OO0OOOO0O0 ,json =O00OO00O0O0000OOO )#line:561
        if OO0000O0OOO0OOO0O .status_code ==201 :#line:562
            print (f"[+] MemberscreeningBypassed {O0O0000000000OOOO}")#line:563
            return #line:564
        else :#line:565
            print (f"[!] Bypassが出来ませんでした {O0O0000000000OOOO}")#line:566
            return #line:567
    except Exception as OO00OOO0OO0000O00 :#line:568
        print (f"[!] エラーが発生しました。{OO00OOO0OO0000O00}")#line:569
session =requests .Session ()#line:571
def reactionput (O000OOOOO00OOO0OO ,O00000O0OOO0OO0O0 ,OOOOO0OOOO0O0000O ,O0OOO000O0OO00O00 ,proxy =None ):#line:574
    OO00O00OOOOOO0OO0 =get_session (proxy )#line:575
    OO0OOO000O00O0O0O =get_headers (OO00O00OOOOOO0OO0 )#line:576
    OO0OOO000O00O0O0O ["Authorization"]=O000OOOOO00OOO0OO #line:577
    O0OOO000O0OO00O00 =requests .utils .quote (O0OOO000O0OO00O00 )#line:579
    O0OOOO0OOO0O00000 =OO00O00OOOOOO0OO0 .put (f"https://discord.com/api/v9/channels/{O00000O0OOO0OO0O0}/messages/{OOOOO0OOOO0O0000O}/reactions/{O0OOO000O0OO00O00}/%40me?location=Message&type=0",headers =OO0OOO000O00O0O0O )#line:583
    if O0OOOO0OOO0O00000 .status_code in [200 ,204 ]:#line:584
        print (f"[+] Reaction '{O0OOO000O0OO00O00}' added successfully to message {OOOOO0OOOO0O0000O}")#line:585
    elif O0OOOO0OOO0O00000 .status_code ==429 :#line:586
        print ("[-] Rate limited. Please wait before retrying.")#line:587
        OO000OOOO0O0O0OO0 =O0OOOO0OOO0O00000 .json ().get ("retry_after",1 )#line:588
        time .sleep (OO000OOOO0O0O0OO0 )#line:589
    elif O0OOOO0OOO0O00000 .status_code ==401 :#line:590
        print ("[-] Invalid or expired token.")#line:591
    else :#line:592
        print (f"[!] Error occurred: {O0OOOO0OOO0O00000.status_code}")#line:593
def generatexspandua (OO0OO00OOO00OO00O ):#line:596
  O00000OO0000O0OO0 =["Android","Windows","Macintosh"]#line:597
  O0OO000OOO000OO00 =random .choice (O00000OO0000O0OO0 )#line:598
  if O0OO000OOO000OO00 =="Macintosh":#line:599
    O00O0O0OO0OOOO00O =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:600
    OOOOOO0O00OOOO0O0 ="Macintosh; Intel Mac OS X "+O00O0O0OO0OOOO00O #line:601
    OO0O000O0000OOO00 ="x86_64"#line:602
  if O0OO000OOO000OO00 =="Windows":#line:603
    O00O0O0OO0OOOO00O =f'{random.choice([6.0,10.0,11.0])}'#line:604
    OOOOOO0O00OOOO0O0 ="Windows NT "+O00O0O0OO0OOOO00O +" Win64; x64"#line:605
    OO0O000O0000OOO00 ="x86_64"#line:606
  if O0OO000OOO000OO00 =="Android":#line:607
    O00O0O0OO0OOOO00O ="13"#line:608
    OOOOOO0O00OOOO0O0 =f"Linux; Android 13; Pixel 6a"#line:609
    OO0O000O0000OOO00 ="aarch64"#line:610
  O0OO00O0O000OOO00 ={"os":O0OO000OOO000OO00 ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":O00O0O0OO0OOOO00O ,"os_arch":OO0O000O0000OOO00 ,"system_locale":"ja-JP","client_build_number":OO0OO00OOO00OO00O ,"client_event_source":None ,"design_id":0 }#line:611
  OOO000000O0O0OO00 =f"Mozilla/5.0 ({OOOOOO0O00OOOO0O0}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:612
  return base64 .b64encode (json .dumps (O0OO00O0O000OOO00 ,separators =(',',':')).encode ()).decode (),OOO000000O0O0OO00 #line:613
import base64 #line:615
def nickchanger ():#line:618
    try :#line:619
        with open ("token.txt")as OOO0O0OO000O0OO00 :#line:620
            OO0O000O000OO0O00 =[O00OOO00O0OO0O0O0 .strip ()for O00OOO00O0OO0O0O0 in OOO0O0OO000O0OO00 .readlines ()if O00OOO00O0OO0O0O0 .strip ()]#line:621
    except (FileNotFoundError ,KeyError ):#line:622
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:623
        return #line:624
    OO0000O0OOOOO00OO =input ("Server ID?: ").strip ()#line:626
    OOOOOOOOO0OO00000 =input ("Nickname?: ").strip ()#line:627
    OOOOOO00O000O0OOO =input ("Delay (in seconds)?: ").strip ()#line:628
    try :#line:630
        OOOOOO00O000O0OOO =float (OOOOOO00O000O0OOO )#line:631
        if OOOOOO00O000O0OOO <0 :#line:632
            raise ValueError #line:633
    except ValueError :#line:634
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:635
        OOOOOO00O000O0OOO =1.0 #line:636
    for O0OO0OO000OOOOO00 in OO0O000O000OO0O00 :#line:638
        O0O00O00OOOO0OOOO ={"Authorization":O0OO0OO000OOOOO00 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:643
        O0O0OO0OOOO0OOO00 ={"nick":OOOOOOOOO0OO00000 }#line:644
        O000O0O00000O0000 =requests .patch (f"https://discord.com/api/v9/guilds/{OO0000O0OOOOO00OO}/members/@me",headers =O0O00O00OOOO0OOOO ,json =O0O0OO0OOOO0OOO00 )#line:645
        if O000O0O00000O0000 .status_code ==200 :#line:647
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Nickname changed to '{OOOOOOOOO0OO00000}' successfully for token {O0OO0OO000OOOOO00}.{colorama.Fore.RESET}")#line:648
        elif O000O0O00000O0000 .status_code ==429 :#line:649
            print (f"{colorama.Fore.RED}    [!] Rate limited. Please wait before retrying for token {O0OO0OO000OOOOO00}.{colorama.Fore.RESET}")#line:650
            O000OO0O000O0OO0O =O000O0O00000O0000 .json ().get ("retry_after",1 )#line:651
            time .sleep (O000OO0O000O0OO0O )#line:652
        else :#line:653
            print (f"{colorama.Fore.RED}    [!] Error occurred: {O000O0O00000O0000.status_code} for token {O0OO0OO000OOOOO00}.{colorama.Fore.RESET}")#line:654
        time .sleep (OOOOOO00O000O0OOO )#line:656
import json ,websocket ,threading ,tls_client ,random ,time #line:660
session =tls_client .Session (client_identifier ="chrome112",random_tls_extension_order =True )#line:662
class Utils :#line:664
    @staticmethod #line:665
    def rangeCorrector (O00OOO00OOOOO0O00 ):#line:666
        if [0 ,99 ]not in O00OOO00OOOOO0O00 :#line:667
            O00OOO00OOOOO0O00 .insert (0 ,[0 ,99 ])#line:668
        return O00OOO00OOOOO0O00 #line:669
    @staticmethod #line:671
    def getRanges (OO00OO0OOOO0O000O ,O0O000O00O0000OOO ,O0O00OOO0O0O0OOOO ):#line:672
        O000OOOO00O00OO00 =int (OO00OO0OOOO0O000O *O0O000O00O0000OOO )#line:673
        OO0O000O0000OO0OO =[[O000OOOO00O00OO00 ,O000OOOO00O00OO00 +99 ]]#line:674
        if O0O00OOO0O0O0OOOO >O000OOOO00O00OO00 +99 :#line:675
            OO0O000O0000OO0OO .append ([O000OOOO00O00OO00 +100 ,O000OOOO00O00OO00 +199 ])#line:676
        return Utils .rangeCorrector (OO0O000O0000OO0OO )#line:677
    @staticmethod #line:679
    def parseGuildMemberListUpdate (O000O0O0OOO000O0O ):#line:680
        OOOOO0OO00O0O00OO ={"online_count":O000O0O0OOO000O0O ["d"]["online_count"],"member_count":O000O0O0OOO000O0O ["d"]["member_count"],"id":O000O0O0OOO000O0O ["d"]["id"],"guild_id":O000O0O0OOO000O0O ["d"]["guild_id"],"hoisted_roles":O000O0O0OOO000O0O ["d"]["groups"],"types":[],"locations":[],"updates":[],}#line:690
        for O0000OOOO0O000OO0 in O000O0O0OOO000O0O ["d"]["ops"]:#line:692
            OOOOO0OO00O0O00OO ["types"].append (O0000OOOO0O000OO0 ["op"])#line:693
            if O0000OOOO0O000OO0 ["op"]in ("SYNC","INVALIDATE"):#line:694
                OOOOO0OO00O0O00OO ["locations"].append (O0000OOOO0O000OO0 ["range"])#line:695
                if O0000OOOO0O000OO0 ["op"]=="SYNC":#line:696
                    OOOOO0OO00O0O00OO ["updates"].append (O0000OOOO0O000OO0 ["items"])#line:697
                else :#line:698
                    OOOOO0OO00O0O00OO ["updates"].append ([])#line:699
            elif O0000OOOO0O000OO0 ["op"]in ("INSERT","UPDATE","DELETE"):#line:700
                OOOOO0OO00O0O00OO ["locations"].append (O0000OOOO0O000OO0 ["index"])#line:701
                if O0000OOOO0O000OO0 ["op"]=="DELETE":#line:702
                    OOOOO0OO00O0O00OO ["updates"].append ([])#line:703
                else :#line:704
                    OOOOO0OO00O0O00OO ["updates"].append (O0000OOOO0O000OO0 ["item"])#line:705
        return OOOOO0OO00O0O00OO #line:706
class DiscordSocket (websocket .WebSocketApp ):#line:708
    def __init__ (OOO00OOO00O0000O0 ,O000OO0OO0OO0OO0O ,OOO0O00OOOOO0OOOO ,O0OO0O000OOO00OO0 ):#line:709
        OOO00OOO00O0000O0 .token =O000OO0OO0OO0OO0O #line:710
        OOO00OOO00O0000O0 .guild_id =OOO0O00OOOOO0OOOO #line:711
        OOO00OOO00O0000O0 .channel_id =O0OO0O000OOO00OO0 #line:712
        OOO00OOO00O0000O0 .socket_headers ={"Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","Cache-Control":"no-cache","Pragma":"no-cache","Sec-WebSocket-Extensions":"permessage-deflate; client_max_window_bits","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",}#line:720
        super ().__init__ ("wss://gateway.discord.gg/?encoding=json&v=9",header =OOO00OOO00O0000O0 .socket_headers ,on_open =lambda O0O0OO0OO000O0OO0 :OOO00OOO00O0000O0 .sock_open (O0O0OO0OO000O0OO0 ),on_message =lambda O0O0O0OOO0O0O000O ,O0O00O0OOO00OOO0O :OOO00OOO00O0000O0 .sock_message (O0O0O0OOO0O0O000O ,O0O00O0OOO00OOO0O ),on_close =lambda OOOO0O00O00O00O0O ,O0O00O0O0OO0OOO00 ,O00OO000O00O0O00O :OOO00OOO00O0000O0 .sock_close (OOOO0O00O00O00O0O ,O0O00O0O0OO0OOO00 ,O00OO000O00O0O00O ),)#line:729
        OOO00OOO00O0000O0 .endScraping =False #line:731
        OOO00OOO00O0000O0 .guilds ={}#line:732
        OOO00OOO00O0000O0 .members ={}#line:733
        OOO00OOO00O0000O0 .ranges =[[0 ,0 ]]#line:734
        OOO00OOO00O0000O0 .lastRange =0 #line:735
        OOO00OOO00O0000O0 .packets_recv =0 #line:736
    def run (O0O0OOOO0O0OOOOO0 ):#line:738
        O0O0OOOO0O0OOOOO0 .run_forever ()#line:739
        return O0O0OOOO0O0OOOOO0 .members #line:740
    def scrapeUsers (O000O0000OO00OOO0 ):#line:742
        if not O000O0000OO00OOO0 .endScraping :#line:743
            O000O0000OO00OOO0 .send ('{"op":14,"d":{"guild_id":"'+O000O0000OO00OOO0 .guild_id +'","typing":true,"activities":true,"threads":true,"channels":{"'+O000O0000OO00OOO0 .channel_id +'":'+json .dumps (O000O0000OO00OOO0 .ranges )+"}}}")#line:752
    def sock_open (OO0OO00O0O0000O00 ,O000OOOOO0OO0OOO0 ):#line:754
        OO0OO00O0O0000O00 .send ('{"op":2,"d":{"token":"'+OO0OO00O0O0000O00 .token +'","capabilities":125,"properties":{"os":"Windows NT","browser":"Chrome","device":"","system_locale":"it-IT","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36","browser_version":"119.0","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":103981,"client_event_source":null},"presence":{"status":"online","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}')#line:759
    def heartbeatThread (OOO00O000O0000OOO ,O00O000OOOOOO00O0 ):#line:761
        try :#line:762
            while True :#line:763
                OOO00O000O0000OOO .send ('{"op":1,"d":'+str (OOO00O000O0000OOO .packets_recv )+"}")#line:764
                time .sleep (O00O000OOOOOO00O0 )#line:765
        except Exception as O0O0000O0O00OO00O :#line:766
            pass #line:767
    def sock_message (O0OO0OO000OO000O0 ,OO000OO00O0O0OOO0 ,O00OOO0OO00O00OOO ):#line:769
        O0OOO0OOO0O000O00 =json .loads (O00OOO0OO00O00OOO )#line:770
        if O0OOO0OOO0O000O00 is None :#line:771
            return #line:772
        if O0OOO0OOO0O000O00 ["op"]!=11 :#line:773
            O0OO0OO000OO000O0 .packets_recv +=1 #line:774
        if O0OOO0OOO0O000O00 ["op"]==10 :#line:775
            threading .Thread (target =O0OO0OO000OO000O0 .heartbeatThread ,args =(O0OOO0OOO0O000O00 ["d"]["heartbeat_interval"]/1000 ,),daemon =True ,).start ()#line:780
        if O0OOO0OOO0O000O00 ["t"]=="READY":#line:781
            for OO0O000OO000O0000 in O0OOO0OOO0O000O00 ["d"]["guilds"]:#line:782
                O0OO0OO000OO000O0 .guilds [OO0O000OO000O0000 ["id"]]={"member_count":OO0O000OO000O0000 ["member_count"]}#line:783
        if O0OOO0OOO0O000O00 ["t"]=="READY_SUPPLEMENTAL":#line:784
            O0OO0OO000OO000O0 .ranges =Utils .getRanges (0 ,100 ,O0OO0OO000OO000O0 .guilds [O0OO0OO000OO000O0 .guild_id ]["member_count"])#line:787
            O0OO0OO000OO000O0 .scrapeUsers ()#line:788
        elif O0OOO0OOO0O000O00 ["t"]=="GUILD_MEMBER_LIST_UPDATE":#line:789
            O00O00O000000OO00 =Utils .parseGuildMemberListUpdate (O0OOO0OOO0O000O00 )#line:790
            if O00O00O000000OO00 ["guild_id"]==O0OO0OO000OO000O0 .guild_id and ("SYNC"in O00O00O000000OO00 ["types"]or "UPDATE"in O00O00O000000OO00 ["types"]):#line:794
                for OOO0000000OO0OO00 ,O00O00O00O0OOO00O in enumerate (O00O00O000000OO00 ["types"]):#line:795
                    if O00O00O00O0OOO00O =="SYNC":#line:796
                        if len (O00O00O000000OO00 ["updates"][OOO0000000OO0OO00 ])==0 :#line:797
                            O0OO0OO000OO000O0 .endScraping =True #line:798
                            break #line:799
                        for OOO0O00O0OOOOOOOO in O00O00O000000OO00 ["updates"][OOO0000000OO0OO00 ]:#line:801
                            if "member"in OOO0O00O0OOOOOOOO :#line:802
                                O0000OOO0O00O0000 =OOO0O00O0OOOOOOOO ["member"]#line:803
                                O00OOO0O000OOO0OO ={"tag":O0000OOO0O00O0000 ["user"]["username"]+"#"+O0000OOO0O00O0000 ["user"]["discriminator"],"id":O0000OOO0O00O0000 ["user"]["id"],}#line:809
                                if not O0000OOO0O00O0000 ["user"].get ("bot"):#line:810
                                    O0OO0OO000OO000O0 .members [O0000OOO0O00O0000 ["user"]["id"]]=O00OOO0O000OOO0OO #line:811
                    elif O00O00O00O0OOO00O =="UPDATE":#line:813
                        for OOO0O00O0OOOOOOOO in O00O00O000000OO00 ["updates"][OOO0000000OO0OO00 ]:#line:814
                            if "member"in OOO0O00O0OOOOOOOO :#line:815
                                O0000OOO0O00O0000 =OOO0O00O0OOOOOOOO ["member"]#line:816
                                O00OOO0O000OOO0OO ={"tag":O0000OOO0O00O0000 ["user"]["username"]+"#"+O0000OOO0O00O0000 ["user"]["discriminator"],"id":O0000OOO0O00O0000 ["user"]["id"],}#line:822
                                if not O0000OOO0O00O0000 ["user"].get ("bot"):#line:823
                                    O0OO0OO000OO000O0 .members [O0000OOO0O00O0000 ["user"]["id"]]=O00OOO0O000OOO0OO #line:824
                    O0OO0OO000OO000O0 .lastRange +=1 #line:826
                    O0OO0OO000OO000O0 .ranges =Utils .getRanges (O0OO0OO000OO000O0 .lastRange ,100 ,O0OO0OO000OO000O0 .guilds [O0OO0OO000OO000O0 .guild_id ]["member_count"])#line:829
                    time .sleep (0.45 )#line:830
                    O0OO0OO000OO000O0 .scrapeUsers ()#line:831
            if O0OO0OO000OO000O0 .endScraping :#line:833
                O0OO0OO000OO000O0 .close ()#line:834
    def sock_close (OO00O0OOO000OOOO0 ,OOO000O0O00000O00 ,OOO00OO00OOO0O0OO ,O0O00O000OOO00000 ):#line:836
        pass #line:837
def scrape (O0O00OO000O000OOO ,OO00O0O00O0O0OOOO ,OOO0OO00000OO000O ):#line:839
    OOO000OO0O0OO0OO0 =DiscordSocket (O0O00OO000O000OOO ,OO00O0O00O0O0OOOO ,OOO0OO00000OO000O )#line:840
    return OOO000OO0O0OO0OO0 .run ()#line:841
def member_scrape (OO0OOO0O0O0O0O000 ,O000O0OOOOOOOOOO0 ,O00O00000O00OO00O ):#line:843
    OOO00O0OO00OO0O0O =[]#line:844
    for O00000OO00OO0O000 in OO0OOO0O0O0O0O000 :#line:845
        OOOOO00O0O0OOOOO0 ={"Authorization":O00000OO00OO0O000 ,"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}#line:846
        OOOOO0OO00O0000O0 =session .get (f"https://canary.discord.com/api/v9/guilds/{O000O0OOOOOOOOOO0}",headers =OOOOO00O0O0OOOOO0 )#line:847
        if OOOOO0OO00O0000O0 .status_code ==200 :#line:848
            OOO00O0OO00OO0O0O .append (O00000OO00OO0O000 )#line:849
            break #line:850
    if not OOO00O0OO00OO0O0O :#line:851
        print ("missing access")#line:852
    O00000OO00OO0O000 =random .choice (OOO00O0OO00OO0O0O )#line:854
    OOOOOO0OOO0O00000 =scrape (O00000OO00OO0O000 ,O000O0OOOOOOOOOO0 ,O00O00000O00OO00O )#line:855
    O0OOO0OOOO00OOOOO =[f"<@{OO00000OOO0O0O000}>"for OO00000OOO0O0O000 in [int (O000OOOOO0O0O00O0 )for O000OOOOO0O0O00O0 in OOOOOO0OOO0O00000 .keys ()]]#line:856
    print (f"[SUCCESS] {len(O0OOO0OOOO00OOOOO)} scraped members")#line:857
    return O0OOO0OOOO00OOOOO #line:858
def spammer_menu ():#line:860
    try :#line:861
        with open ("token.txt")as O0000OOO0O0O00OO0 :#line:862
            O000O0OO0OOO0OOO0 =[O0O0OO0OO0OOO0O00 .strip ()for O0O0OO0OO0OOO0O00 in O0000OOO0O0O00OO0 .readlines ()if O0O0OO0OO0OOO0O00 .strip ()]#line:863
    except (FileNotFoundError ,KeyError ):#line:864
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:865
        return #line:866
    OOO00O0O00O00O0O0 =input ("Server ID?: ").strip ()#line:868
    OO000O0OO0000O0O0 =input ("Message?: ").strip ()#line:869
    OO00000O0000OOO00 =input ("Random mention (True/False)?: ").strip ().lower ()=='true'#line:870
    OOOOO000OO0OOOOO0 =input ("Delay between messages (in seconds)?: ").strip ()#line:871
    OO000O0O0OOOOO0OO =input ("Number of messages to send?: ").strip ()#line:872
    OOOO00000O0OO0O00 =input ("Blacklist User IDs (comma-separated) (Leave blank to skip)?: ").strip ().split (',')#line:873
    OOOO00000O0OO0O00 =[f"<@{O0OO00OOO0OOOO000.strip()}>"for O0OO00OOO0OOOO000 in OOOO00000O0OO0O00 if O0OO00OOO0OOOO000 .strip ()]#line:874
    try :#line:876
        OOOOO000OO0OOOOO0 =float (OOOOO000OO0OOOOO0 )#line:877
        if OOOOO000OO0OOOOO0 <0 :#line:878
            raise ValueError #line:879
    except ValueError :#line:880
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:881
        OOOOO000OO0OOOOO0 =1.0 #line:882
    try :#line:884
        OO000O0O0OOOOO0OO =int (OO000O0O0OOOOO0OO )#line:885
        if OO000O0O0OOOOO0OO <=0 :#line:886
            raise ValueError #line:887
    except ValueError :#line:888
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:889
        OO000O0O0OOOOO0OO =1 #line:890
    O0000OOO0OOOOOO0O =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:892
    if O0000OOO0OOOOOO0O =='2':#line:893
        OO0O00OOO000O0OOO =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:894
        OO0O00OOO000O0OOO =[O0O0O00OO0O000000 .strip ()for O0O0O00OO0O000000 in OO0O00OOO000O0OOO if O0O0O00OO0O000000 .strip ()]#line:895
    else :#line:896
        OO0O00OOO000O0OOO =fetch_channels (O000O0OO0OOO0OOO0 [0 ],OOO00O0O00O00O0O0 )#line:897
    O000000OOO0OOO00O =None #line:899
    spammer (O000O0OO0OOO0OOO0 ,OOO00O0O00O00O0O0 ,OO0O00OOO000O0OOO ,OO000O0OO0000O0O0 ,OO00000O0000OOO00 ,OOOO00000O0OO0O00 ,O000000OOO0OOO00O ,OO000O0O0OOOOO0OO )#line:901
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:903
def spammer (O0OOO00O0000OOOO0 ,OO00O0000OO00O000 ,OO00OOOOOOOO00O00 ,OO000OOO0O0000O0O ,OOOOOO0000O00O0OO ,OOO0O0O000O0O0O0O ,O00O0000OO0OOO0OO ,O00O000O000O00000 ):#line:905
    O0O0O00OOOOOOO000 =get_session (O00O0000OO0OOO0OO )#line:906
    OO0OOOOO0O0000OO0 =0 #line:907
    O00OOO0O0O000O0O0 =member_scrape (O0OOO00O0000OOOO0 ,OO00O0000OO00O000 ,OO00OOOOOOOO00O00 [0 ])#line:909
    O00OOO0O0O000O0O0 =[O0O00OOO00OOO0O0O for O0O00OOO00OOO0O0O in O00OOO0O0O000O0O0 if O0O00OOO00OOO0O0O not in OOO0O0O000O0O0O0O ]#line:910
    for _OO0O0000000OOOO00 in range (O00O000O000O00000 ):#line:912
        OO0O0OOO00O000OO0 =O0OOO00O0000OOOO0 [OO0OOOOO0O0000OO0 ]#line:913
        O00O0O00O0OOOOO0O =get_headers (OO0O0OOO00O000OO0 )#line:914
        for OO00O0OOO000O0O00 in OO00OOOOOOOO00O00 :#line:915
            O0O00O00OO0O00O0O =OO000OOO0O0000O0O #line:916
            if OOOOOO0000O00O0OO and O00OOO0O0O000O0O0 :#line:917
                OO0O0OOOOOOOOOOOO =random .choice (O00OOO0O0O000O0O0 )#line:918
                O0O00O00OO0O00O0O +=f" {OO0O0OOOOOOOOOOOO}"#line:919
            OO0OO00O00OO000O0 =O0O0O00OOOOOOO000 .post (f"https://discord.com/api/v9/channels/{OO00O0OOO000O0O00}/messages",json ={"content":O0O00O00OO0O00O0O },headers =O00O0O00O0OOOOO0O )#line:921
            if OO0OO00O00OO000O0 .status_code ==200 :#line:922
                print (f"200 message sent: {OO0O0OOO00O000OO0}")#line:923
            elif OO0OO00O00OO000O0 .status_code ==429 :#line:924
                print (f"429 rate limit: {OO0O0OOO00O000OO0}")#line:925
                OOO00OOO00O00O000 =OO0OO00O00OO000O0 .json ().get ("retry_after",1 )#line:926
                time .sleep (OOO00OOO00O00O000 )#line:927
            elif OO0OO00O00OO000O0 .status_code ==401 :#line:928
                print (f"401 unknown token: {OO0O0OOO00O000OO0}")#line:929
            else :#line:930
                print (f"error: {OO0O0OOO00O000OO0}")#line:931
        OO0OOOOO0O0000OO0 =(OO0OOOOO0O0000OO0 +1 )%len (O0OOO00O0000OOOO0 )#line:933
        time .sleep (1 )#line:934
import requests #line:938
import base64 #line:939
import colorama #line:940
import time #line:941
def add_emojis_from_files ():#line:943
    try :#line:944
        with open ("emojiname.txt")as O0OOO00O00OO00OOO ,open ("emojiurl.txt")as OO0O0O0O0O0O0O000 :#line:945
            O0OOOOOOOO0OO00OO =[OO0O00O0O00OOO0OO .strip ()for OO0O00O0O00OOO0OO in O0OOO00O00OO00OOO .read ().split (',')if OO0O00O0O00OOO0OO .strip ()]#line:946
            OO00OO0O0O00OO00O =[O0O0OO0OOOOO000OO .strip ()for O0O0OO0OOOOO000OO in OO0O0O0O0O0O0O000 .read ().split (',')if O0O0OO0OOOOO000OO .strip ()]#line:947
    except FileNotFoundError as OOOO0O000O000000O :#line:948
        print (f"{colorama.Fore.RED}    [!] Error: {str(OOOO0O000O000000O)}{colorama.Fore.RESET}")#line:949
        return #line:950
    if len (O0OOOOOOOO0OO00OO )!=len (OO00OO0O0O00OO00O ):#line:952
        print (f"{colorama.Fore.RED}    [!] Error: The number of emoji names and URLs do not match!{colorama.Fore.RESET}")#line:953
        return #line:954
    try :#line:956
        with open ("token.txt")as OO0OOOO0OO0OOO0O0 :#line:957
            OO0O0O0O0OOO00OO0 =[O00OO0OOOO000OO00 .strip ()for O00OO0OOOO000OO00 in OO0OOOO0OO0OOO0O0 .readlines ()if O00OO0OOOO000OO00 .strip ()]#line:958
    except FileNotFoundError as OOOO0O000O000000O :#line:959
        print (f"{colorama.Fore.RED}    [!] Error: {str(OOOO0O000O000000O)}{colorama.Fore.RESET}")#line:960
        return #line:961
    OO0O0OO00OOOO0O0O =input ("Enter the Guild ID: ").strip ()#line:963
    OOOOOOO000000O0OO =input ("Enter the rate limit between requests (in seconds): ").strip ()#line:964
    try :#line:966
        OOOOOOO000000O0OO =float (OOOOOOO000000O0OO )#line:967
        if OOOOOOO000000O0OO <0 :#line:968
            raise ValueError #line:969
    except ValueError :#line:970
        print (f"{colorama.Fore.RED}    [!] Invalid rate limit. Using default rate limit of 5 seconds.{colorama.Fore.RESET}")#line:971
        OOOOOOO000000O0OO =5.0 #line:972
    OO00OOOOO00000O00 =set ()#line:974
    for O00O000OOOO00O00O in OO0O0O0O0OOO00OO0 :#line:976
        OO00O0O0OOO0000OO ={'Authorization':O00O000OOOO00O00O ,'Content-Type':'application/json'}#line:980
        O00000O0OO000OO0O =requests .get (f"https://discord.com/api/v9/guilds/{OO0O0OO00OOOO0O0O}/emojis",headers =OO00O0O0OOO0000OO )#line:983
        if O00000O0OO000OO0O .status_code ==200 :#line:984
            O0OOOO0OO0O0O00OO =O00000O0OO000OO0O .json ()#line:985
            for O0OO0OOO0O0OO0OOO in O0OOOO0OO0O0O00OO :#line:986
                OO00OOOOO00000O00 .add (O0OO0OOO0O0OO0OOO ['name'])#line:987
        else :#line:988
            print (f"{colorama.Fore.RED}    [!] Error fetching existing emojis: {O00000O0OO000OO0O.status_code} - {O00000O0OO000OO0O.text}{colorama.Fore.RESET}")#line:989
            continue #line:990
    for O0O0OOOO00OO0O0OO ,OOO000O000OO0OOO0 in zip (O0OOOOOOOO0OO00OO ,OO00OO0O0O00OO00O ):#line:992
        if O0O0OOOO00OO0O0OO in OO00OOOOO00000O00 :#line:993
            print (f"{colorama.Fore.YELLOW}    [*] Emoji '{O0O0OOOO00OO0O0OO}' already exists. Skipping...{colorama.Fore.RESET}")#line:994
            continue #line:995
        for O00O000OOOO00O00O in OO0O0O0O0OOO00OO0 :#line:997
            try :#line:998
                O00000O0OO000OO0O =requests .get (OOO000O000OO0OOO0 )#line:999
                O00000O0OO000OO0O .raise_for_status ()#line:1000
                OO000OOOOOOOO000O =O00000O0OO000OO0O .content #line:1001
                OO00O0O0O0OOO0O0O =base64 .b64encode (OO000OOOOOOOO000O ).decode ('utf-8')#line:1002
                OO0000000O000OOO0 ={'name':O0O0OOOO00OO0O0OO ,'image':f"data:image/png;base64,{OO00O0O0O0OOO0O0O}"}#line:1007
                OO00O0O0OOO0000OO ={'Authorization':O00O000OOOO00O00O ,'Content-Type':'application/json'}#line:1012
                OOO00OOO0O000O0O0 =requests .post (f"https://discord.com/api/v9/guilds/{OO0O0OO00OOOO0O0O}/emojis",headers =OO00O0O0OOO0000OO ,json =OO0000000O000OOO0 )#line:1014
                if OOO00OOO0O000O0O0 .status_code ==201 :#line:1015
                    print (f"{colorama.Fore.GREEN}    [+] Successfully added emoji '{O0O0OOOO00OO0O0OO}' with token {O00O000OOOO00O00O}{colorama.Fore.RESET}")#line:1016
                    OO00OOOOO00000O00 .add (O0O0OOOO00OO0O0OO )#line:1017
                    break #line:1018
                else :#line:1019
                    print (f"{colorama.Fore.RED}    [!] Failed to add emoji '{O0O0OOOO00OO0O0OO}' with token {O00O000OOOO00O00O}: {OOO00OOO0O000O0O0.status_code} - {OOO00OOO0O000O0O0.text}{colorama.Fore.RESET}")#line:1020
                time .sleep (OOOOOOO000000O0OO )#line:1022
            except Exception as OOOO0O000O000000O :#line:1023
                print (f"{colorama.Fore.RED}    [!] Error adding emoji '{O0O0OOOO00OO0O0OO}' with token {O00O000OOOO00O00O}: {str(OOOO0O000O000000O)}{colorama.Fore.RESET}")#line:1024
def main ():#line:1026
    colorama .init ()#line:1027
    while True :#line:1028
        logo ()#line:1029
        O0O0OO0OO0OO000O0 =input (f"{colorama.Fore.LIGHTMAGENTA_EX}    [Final] Select an option from above: ")#line:1030
        if O0O0OO0OO0OO000O0 =="0":#line:1032
            update_group_ids ()#line:1033
        elif O0O0OO0OO0OO000O0 =="1":#line:1034
            join_discord_invite ()#line:1035
        elif O0O0OO0OO0OO000O0 =="2":#line:1036
            reaction_spammer ()#line:1037
        elif O0O0OO0OO0OO000O0 =="3":#line:1038
            send_messages_with_mentions ()#line:1039
        elif O0O0OO0OO0OO000O0 =="4":#line:1040
            spammer_menu ()#line:1041
        elif O0O0OO0OO0OO000O0 =="5":#line:1042
            nickchanger ()#line:1043
        elif O0O0OO0OO0OO000O0 =="6":#line:1044
            add_emojis_from_files ()#line:1045
        elif O0O0OO0OO0OO000O0 =="7":#line:1046
            reaction_art ()#line:1047
        elif O0O0OO0OO0OO000O0 =="0":#line:1048
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [*] Exiting the application. Goodbye!{colorama.Fore.RESET}")#line:1049
            break #line:1050
        else :#line:1051
            print (f"{colorama.Fore.RED}    [!] Invalid option selected!{colorama.Fore.RESET}")#line:1052
        input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:1054
if __name__ =="__main__":#line:1056
    main ()#line:1057

