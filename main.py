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
    OO0OOO0O0OOO0O0O0 =requests .Session ()#line:57
    if proxy :#line:58
        OO0OOO0O0OOO0O0O0 .proxies ={"http":proxy ,"https":proxy }#line:59
    return OO0OOO0O0OOO0O0O0 #line:60
def get_headers (OOO0O0O0O0OO00OO0 ):#line:62
    return {"Authorization":OOO0O0O0O0OO00OO0 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:67
def send_message_with_mention (O00000000000OO000 ,O0O0O0OOO0OOO0OO0 ,OOOO0O0000O0OOOO0 ,O0O0OOO000O0O0OOO ):#line:70
    O00O0OO0O0O00OOO0 =get_session ()#line:71
    O0O00O0O0O0OO0OO0 =get_headers (O00000000000OO000 )#line:72
    if O0O0OOO000O0O0OOO :#line:74
        O00OO0000000O0000 =random .choice (O0O0OOO000O0O0OOO )#line:75
        OOOO0O0000O0OOOO0 +=f" <@{O00OO0000000O0000}>"#line:76
    OO000O0O000OOOOO0 =O00O0OO0O0O00OOO0 .post (f"https://discord.com/api/v9/channels/{O0O0O0OOO0OOO0OO0}/messages",headers =O0O00O0O0O0OO0OO0 ,json ={"content":OOOO0O0000O0OOOO0 })#line:82
    if OO000O0O000OOOOO0 .status_code in [200 ,201 ]:#line:83
        print (f"[+] Message sent to channel {O0O0O0OOO0OOO0OO0}")#line:84
    elif OO000O0O000OOOOO0 .status_code ==429 :#line:85
        print ("[-] Rate limited. Please wait before retrying.")#line:86
        OOO0O0O00OO00O00O =OO000O0O000OOOOO0 .json ().get ("retry_after",1 )#line:87
        time .sleep (OOO0O0O00OO00O00O )#line:88
    else :#line:89
        print (f"[!] Error occurred: {OO000O0O000OOOOO0.status_code}")#line:90
def fetch_messages (O000000O00OO0OOOO ,O00000OOO0000OO00 ,limit =100 ):#line:93
    OOOO0OOO00000O0O0 ={"Authorization":O000000O00OO0OOOO ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:98
    OOO00O00000000O0O =requests .get (f"https://discord.com/api/v9/channels/{O00000OOO0000OO00}/messages?limit={limit}",headers =OOOO0OOO00000O0O0 )#line:102
    if OOO00O00000000O0O .status_code ==200 :#line:103
        return OOO00O00000000O0O .json ()#line:104
    else :#line:105
        print (f"[!] Failed to fetch messages. HTTP Status Code: {OOO00O00000000O0O.status_code}")#line:106
        return []#line:107
import concurrent .futures #line:108
def reaction_spammer ():#line:110
    try :#line:111
        with open ("token.txt")as O0O000O0OOO0O00O0 :#line:112
            OOOOOO00O00O0OO00 =[OOO000O0O000OO0OO .strip ()for OOO000O0O000OO0OO in O0O000O0OOO0O00O0 .readlines ()if OOO000O0O000OO0OO .strip ()]#line:113
    except (FileNotFoundError ,KeyError ):#line:114
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:115
        return #line:116
    O0OO00OO0OOO00OO0 =input ("Server ID?: ").strip ()#line:118
    OO0OO0OOO0OO0OO0O =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:120
    if OO0OO0OOO0OO0OO0O =='2':#line:121
        OOOO0OOO0O0O00OOO =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:122
        O0O00O0OOOOOO0OO0 =[O00000OOOOOOOO0OO .strip ()for O00000OOOOOOOO0OO in OOOO0OOO0O0O00OOO if O00000OOOOOOOO0OO .strip ()]#line:123
    else :#line:124
        O0O00O0OOOOOO0OO0 =[]#line:125
        for OO0O0OO0OO00000O0 in OOOOOO00O00O0OO00 :#line:126
            try :#line:127
                O0O00O0OOOOOO0OO0 .extend (fetch_channels (OO0O0OO0OO00000O0 ,O0OO00OO0OOO00OO0 ))#line:128
            except Exception as O00OO00OOOO00O0O0 :#line:129
                print (f"[!] Failed to fetch channels for token. Error: {O00OO00OOOO00O0O0}")#line:130
                continue #line:131
    O0O00O000O00OOO00 =input ("Select your emoji (a, b, c, ... or custom emojis): ").strip ()#line:133
    OO0OOOOO00OOOO000 =input ("Delay between reactions (in seconds)?: ").strip ()#line:134
    try :#line:136
        OO0OOOOO00OOOO000 =float (OO0OOOOO00OOOO000 )#line:137
        if OO0OOOOO00OOOO000 <0 :#line:138
            raise ValueError #line:139
    except ValueError :#line:140
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:141
        OO0OOOOO00OOOO000 =1.0 #line:142
    O0OOOOO0OO0O0OOOO =[]#line:144
    for O0OO0OOO0O000000O in O0O00O000O00OOO00 .split (","):#line:145
        O0OO0OOO0O000000O =O0OO0OOO0O000000O .strip ().lower ()#line:146
        if O0OO0OOO0O000000O in alphabet_to_flag :#line:147
            O0OOOOO0OO0O0OOOO .append (alphabet_to_flag [O0OO0OOO0O000000O ])#line:148
        else :#line:149
            O0OOOOO0OO0O0OOOO .append (O0OO0OOO0O000000O )#line:150
    if not O0OOOOO0OO0O0OOOO :#line:152
        print (f"{colorama.Fore.RED}    [!] No valid emojis provided!{colorama.Fore.RESET}")#line:153
        return #line:154
import requests #line:156
import json #line:157
import time #line:158
import colorama #line:159
alphabet_to_flag ={'a':'🇦','b':'🇧','c':'🇨','d':'🇩','e':'🇪','f':'🇫','g':'🇬','h':'🇭','i':'🇮','j':'🇯','k':'🇰','l':'🇱','m':'🇲','n':'🇳','o':'🇴','p':'🇵','q':'🇶','r':'🇷','s':'🇸','t':'🇹','u':'🇺','v':'🇻','w':'🇼','x':'🇽','y':'🇾','z':'🇿'}#line:167
def fetch_channels (O0O000O00O000O0OO ,OOO0OOOOO0OO0O00O ):#line:169
    O0OOO0000OO00000O =f"https://discord.com/api/v9/guilds/{OOO0OOOOO0OO0O00O}/channels"#line:170
    OO0O0000O00O0O0OO ={"Authorization":O0O000O00O000O0OO }#line:171
    OOO00O0O0O000O0OO =requests .get (O0OOO0000OO00000O ,headers =OO0O0000O00O0O0OO )#line:172
    if OOO00O0O0O000O0OO .status_code ==200 :#line:173
        return [O0O0O00O0O0O0O0O0 ['id']for O0O0O00O0O0O0O0O0 in OOO00O0O0O000O0OO .json ()if O0O0O00O0O0O0O0O0 ['type']==0 ]#line:174
    else :#line:175
        raise Exception (f"Failed to fetch channels: {OOO00O0O0O000O0OO.status_code} - {OOO00O0O0O000O0OO.text}")#line:176
def fetch_messages (O000O0OOO000OOO0O ,O000OOO0OO00OOO00 ,limit =100 ):#line:178
    OOOO000OOOOOO0O0O =f"https://discord.com/api/v9/channels/{O000OOO0OO00OOO00}/messages?limit={limit}"#line:179
    O00O000OO00O000O0 ={"Authorization":O000O0OOO000OOO0O }#line:180
    OO0OO00000O0O0OOO =requests .get (OOOO000OOOOOO0O0O ,headers =O00O000OO00O000O0 )#line:181
    if OO0OO00000O0O0OOO .status_code ==200 :#line:182
        return OO0OO00000O0O0OOO .json ()#line:183
    else :#line:184
        print (f"[!] Failed to fetch messages: {OO0OO00000O0O0OOO.status_code} - {OO0OO00000O0O0OOO.text}")#line:185
        return []#line:186
def reactionput (OOO0O0OOOOOO00O0O ,OOO00O0O0OOOO000O ,OO0O0OOOOOO00OO00 ,O00OO0O00O0000000 ):#line:188
    OOO0000OO00OOOOOO =f"https://discord.com/api/v9/channels/{OOO00O0O0OOOO000O}/messages/{OO0O0OOOOOO00OO00}/reactions/{O00OO0O00O0000000}/@me"#line:189
    OO00OOO00OO0OOOO0 ={"Authorization":OOO0O0OOOOOO00O0O ,"Content-Type":"application/json"}#line:190
    O0OOOOOO00000OO00 =requests .put (OOO0000OO00OOOOOO ,headers =OO00OOO00OO0OOOO0 )#line:191
    if O0OOOOOO00000OO00 .status_code not in [204 ,200 ]:#line:192
        print (f"{colorama.Fore.RED}    [!] Failed to add reaction: {O0OOOOOO00000OO00.status_code} - {O0OOOOOO00000OO00.text}{colorama.Fore.RESET}")#line:193
def reaction_art ():#line:195
    try :#line:196
        with open ("token.txt",encoding ="utf-8")as O000000O00OOO0000 :#line:197
            OOO00O00000OOO00O =[OO000O000O0000O00 .strip ()for OO000O000O0000O00 in O000000O00OOO0000 .readlines ()if OO000O000O0000O00 .strip ()]#line:198
    except (FileNotFoundError ,KeyError ):#line:199
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:200
        return #line:201
    OOO0OO000O00O0OO0 =input ("Server ID?: ").strip ()#line:203
    O0O0O00O00OO00000 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:205
    if O0O0O00O00OO00000 =='2':#line:206
        O00OO0OOOOOO0OOO0 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:207
        O000000O0O0OOOO00 =[O0OO00O000000O0O0 .strip ()for O0OO00O000000O0O0 in O00OO0OOOOOO0OOO0 if O0OO00O000000O0O0 .strip ()]#line:208
    else :#line:209
        O000000O0O0OOOO00 =[]#line:210
        for O0OO0000O00O0OOOO in OOO00O00000OOO00O :#line:211
            try :#line:212
                O000000O0O0OOOO00 .extend (fetch_channels (O0OO0000O00O0OOOO ,OOO0OO000O00O0OO0 ))#line:213
            except Exception as O0O0O0OO0OO0000O0 :#line:214
                print (f"[!] Failed to fetch channels for token. Error: {O0O0O0OO0OO0000O0}")#line:215
                continue #line:216
    O0000O0O00000OO0O =input ("Delay between reactions (in seconds)?: ").strip ()#line:218
    try :#line:220
        O0000O0O00000OO0O =float (O0000O0O00000OO0O )#line:221
        if O0000O0O00000OO0O <0 :#line:222
            raise ValueError #line:223
    except ValueError :#line:224
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:225
        O0000O0O00000OO0O =1.0 #line:226
    try :#line:228
        with open ("art.txt",encoding ="utf-8")as O000O00O0O00O0O0O :#line:229
            OO0OOO0O0OO000000 =[O00OOO00OO0O000OO .strip ()for O00OOO00OO0O000OO in O000O00O0O00O0O0O .readlines ()if O00OOO00OO0O000OO .strip ()]#line:230
    except (FileNotFoundError ,KeyError ):#line:231
        print (f"{colorama.Fore.RED}    [!] Error: art.txt file not found or empty!{colorama.Fore.RESET}")#line:232
        return #line:233
    except UnicodeDecodeError as O0O0O0OO0OO0000O0 :#line:234
        print (f"{colorama.Fore.RED}    [!] Error decoding art.txt: {str(O0O0O0OO0OO0000O0)}{colorama.Fore.RESET}")#line:235
        return #line:236
    if not OO0OOO0O0OO000000 :#line:238
        print (f"{colorama.Fore.RED}    [!] No valid art provided in art.txt!{colorama.Fore.RESET}")#line:239
        return #line:240
    OO0OOO0O0OO000000 .reverse ()#line:243
    for O0OO0000O00O0OOOO in OOO00O00000OOO00O :#line:245
        for O0O0OO0O00OO0O0OO in O000000O0O0OOOO00 :#line:246
            try :#line:247
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {O0O0OO0O00OO0O0OO}...{colorama.Fore.RESET}")#line:248
                OOOO00OOO000OO0OO =fetch_messages (O0OO0000O00O0OOOO ,O0O0OO0O00OO0O0OO ,limit =len (OO0OOO0O0OO000000 ))#line:249
                if not OOOO00OOO000OO0OO :#line:250
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:251
                    continue #line:252
                for O0OOOO0O0O0O0000O ,OOO0OO0O0O0OOOO0O in enumerate (OOOO00OOO000OO0OO ):#line:255
                    OOOO0O0000O00OOOO =OO0OOO0O0OO000000 [O0OOOO0O0O0O0000O %len (OO0OOO0O0OO000000 )].split (',')#line:256
                    for O0OOOOO0O0OOO00OO in OOOO0O0000O00OOOO :#line:257
                        reactionput (O0OO0000O00O0OOOO ,O0O0OO0O00OO0O0OO ,OOO0OO0O0O0OOOO0O ['id'],O0OOOOO0O0OOO00OO .strip ())#line:258
                        print (f"Adding reaction '{O0OOOOO0O0OOO00OO.strip()}' to message {OOO0OO0O0O0OOOO0O['id']} in channel {O0O0OO0O00OO0O0OO}")#line:259
                        time .sleep (O0000O0O00000OO0O )#line:260
            except Exception as O0O0O0OO0OO0000O0 :#line:261
                print (f"[!] Error processing channel {O0O0OO0O00OO0O0OO}. Error: {O0O0O0OO0OO0000O0}")#line:262
                continue #line:263
    def OOOO000OOOOOOO000 (O0OO0O000OOOO00O0 ):#line:267
        for O00O000O0OO0O0OO0 in O000000O0O0OOOO00 :#line:268
            try :#line:269
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {O00O000O0OO0O0OO0}...{colorama.Fore.RESET}")#line:270
                OOOO000OO0O00OOO0 =fetch_messages (O0OO0O000OOOO00O0 ,O00O000O0OO0O0OO0 ,limit =100 )#line:271
                if not OOOO000OO0O00OOO0 :#line:272
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:273
                    continue #line:274
                for OOOO0O0000O0OO0OO in OOOO000OO0O00OOO0 :#line:276
                    for OO00O0OOOO0O0O0OO in OOOO0O0000O00OOOO :#line:277
                        reactionput (O0OO0O000OOOO00O0 ,O00O000O0OO0O0OO0 ,OOOO0O0000O0OO0OO ['id'],OO00O0OOOO0O0O0OO )#line:278
                        time .sleep (O0000O0O00000OO0O )#line:279
            except Exception as O0OOO000OO0OO0O00 :#line:280
                print (f"[!] Error processing channel {O00O000O0OO0O0OO0}. Error: {O0OOO000OO0OO0O00}")#line:281
                continue #line:282
    with concurrent .futures .ThreadPoolExecutor ()as OO0OO0O0O000OO0OO :#line:284
        O0OOO0OO00O00OO0O =[OO0OO0O0O000OO0OO .submit (OOOO000OOOOOOO000 ,O000O0OOOOO0O0000 )for O000O0OOOOO0O0000 in OOO00O00000OOO00O ]#line:285
        concurrent .futures .wait (O0OOO0OO00O00OO0O )#line:286
def update_group_ids ():#line:289
    try :#line:290
        with open ("token.txt")as O0O0OO0OO00O0OOO0 :#line:291
            OO00O0O0O00O0OOOO =[OO00OO0000OO0O00O .strip ()for OO00OO0000OO0O00O in O0O0OO0OO00O0OOO0 .readlines ()if OO00OO0000OO0O00O .strip ()]#line:292
        O0O0OO0OOOOOOO0O0 =OO00O0O0O00O0OOOO [0 ]#line:293
    except (FileNotFoundError ,KeyError ):#line:294
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:295
        return #line:296
    O000O0OOOO0OOO0O0 ={"Authorization":O0O0OO0OOOOOOO0O0 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:302
    O0O0OO00OO00O00O0 =requests .get ('https://discord.com/api/v9/users/@me/channels',headers =O000O0OOOO0OOO0O0 )#line:304
    if O0O0OO00OO00O00O0 .status_code ==200 :#line:305
        OO0000OOO0OOO0O00 =O0O0OO00OO00O00O0 .json ()#line:306
        with open ("group_id.txt","w")as O0O0OO0O00OO0000O :#line:307
            for OOOO0O0OO00OO0O00 in OO0000OOO0OOO0O00 :#line:308
                if OOOO0O0OO00OO0O00 ['type']==3 :#line:309
                    O0O0OO0O00OO0000O .write (OOOO0O0OO00OO0O00 ['id']+'\n')#line:310
        print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Group IDs updated successfully.{colorama.Fore.RESET}")#line:311
    else :#line:312
        print (f"{colorama.Fore.LIGHTRED_EX}    [!] Failed to retrieve group IDs. HTTP Status Code: {O0O0OO00OO00O00O0.status_code}{colorama.Fore.RESET}")#line:313
import requests #line:315
import requests #line:317
def fetch_channels (OO0O0O0OOOO0OO0O0 ,O000OOO0OOOOOO0OO ):#line:319
    try :#line:320
        OOOOO000000O0O0OO =requests .Session ()#line:321
        O00O000000O00OOO0 =get_headers (OO0O0O0OOOO0OO0O0 )#line:322
        O000OOO0O0O00O000 =OOOOO000000O0O0OO .get (f"https://discord.com/api/v9/guilds/{O000OOO0OOOOOO0OO}/channels",headers =O00O000000O00OOO0 ,timeout =10 )#line:329
        if O000OOO0O0O00O000 .status_code ==200 :#line:332
            try :#line:333
                O00O0O0000O00O0O0 =O000OOO0O0O00O000 .json ()#line:334
                return [OO00000O000OOO0O0 ['id']for OO00000O000OOO0O0 in O00O0O0000O00O0O0 if OO00000O000OOO0O0 .get ('type')==0 ]#line:335
            except ValueError :#line:336
                print ("[!] Error: Response was not valid JSON.")#line:337
                return []#line:338
        elif O000OOO0O0O00O000 .status_code ==401 :#line:339
            print ("[!] Error: Unauthorized - check your token.")#line:340
        elif O000OOO0O0O00O000 .status_code ==403 :#line:341
            print ("[!] Error: Forbidden - you lack permissions.")#line:342
        elif O000OOO0O0O00O000 .status_code ==404 :#line:343
            print ("[!] Error: Server not found - check the server ID.")#line:344
        else :#line:345
            print (f"[!] Error: Unexpected status code {O000OOO0O0O00O000.status_code}.")#line:346
        return []#line:349
    except requests .exceptions .Timeout :#line:351
        print ("[!] Error: Request timed out. Check your connection or try again later.")#line:352
        return []#line:353
    except requests .exceptions .RequestException as O0O0O0OOO0OOOOOO0 :#line:354
        print (f"[!] Error: An error occurred while fetching channels: {O0O0O0OOO0OOOOOO0}")#line:355
        return []#line:356
def extract_uids_from_messages (O00O0OOOOOO00OOOO ):#line:362
    OOOOOOOOOO0000OOO =set ()#line:363
    for OO0O0OOOOOO00OO0O in O00O0OOOOOO00OOOO :#line:364
        OOOOOOOOOO0000OOO .add (OO0O0OOOOOO00OO0O ['author']['id'])#line:365
    return list (OOOOOOOOOO0000OOO )#line:366
def send_message_with_mention (O0OOOO0OO00OO0O0O ,O0O0O0O000O0O0OOO ,O0OO00O000OOO000O ,OOOO0O00O0000O000 ):#line:368
    OO00000OO0OOOOO00 =get_session ()#line:369
    O0O0000O000O0OOOO =get_headers (O0OOOO0OO00OO0O0O )#line:370
    if OOOO0O00O0000O000 :#line:372
        O0O000000OOO00O00 =random .choice (OOOO0O00O0000O000 )#line:373
        O0OO00O000OOO000O +=f" <@{O0O000000OOO00O00}>"#line:374
    OOOOO0O0O0OO00OO0 =OO00000OO0OOOOO00 .post (f"https://discord.com/api/v9/channels/{O0O0O0O000O0O0OOO}/messages",headers =O0O0000O000O0OOOO ,json ={"content":O0OO00O000OOO000O })#line:380
    if OOOOO0O0O0OO00OO0 .status_code in [200 ,201 ]:#line:381
        print (f"[+] Message sent to channel {O0O0O0O000O0O0OOO}")#line:382
    elif OOOOO0O0O0OO00OO0 .status_code ==429 :#line:383
        print ("[-] Rate limited. Please wait before retrying.")#line:384
        OOOO00O00O00000O0 =OOOOO0O0O0OO00OO0 .json ().get ("retry_after",1 )#line:385
        time .sleep (OOOO00O00O00000O0 )#line:386
    else :#line:387
        print (f"[!] Error occurred: {OOOOO0O0O0OO00OO0.status_code}")#line:388
def send_messages_with_mentions ():#line:389
    try :#line:390
        with open ("token.txt")as OOOO0O0OOOOO0OO0O :#line:391
            OO00O00OO0OOOO0O0 =[O00O00OOOO000O000 .strip ()for O00O00OOOO000O000 in OOOO0O0OOOOO0OO0O .readlines ()if O00O00OOOO000O000 .strip ()]#line:392
    except (FileNotFoundError ,KeyError ):#line:393
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:394
        return #line:395
    OO000OO00O00O0OO0 =input ("Server ID?: ").strip ()#line:397
    OO0OOO0000OOO0OOO =input ("Delay between messages (in seconds)?: ").strip ()#line:398
    OOO0OOO0OOO000OO0 =input ("Number of messages to send?: ").strip ()#line:399
    OO00OOOOO0OOOO0OO =input ("Message content?: ").strip ()#line:400
    OO0OO00O0O0O00OOO =input ("Blacklist User IDs (comma-separated)?: ").strip ().split (',')#line:401
    OO0OO00O0O0O00OOO =[OO00OOO0OOO0OO000 .strip ()for OO00OOO0OOO0OO000 in OO0OO00O0O0O00OOO if OO00OOO0OOO0OO000 .strip ()]#line:402
    try :#line:404
        OO0OOO0000OOO0OOO =float (OO0OOO0000OOO0OOO )#line:405
        if OO0OOO0000OOO0OOO <0 :#line:406
            raise ValueError #line:407
    except ValueError :#line:408
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:409
        OO0OOO0000OOO0OOO =1.0 #line:410
    try :#line:412
        OOO0OOO0OOO000OO0 =int (OOO0OOO0OOO000OO0 )#line:413
        if OOO0OOO0OOO000OO0 <=0 :#line:414
            raise ValueError #line:415
    except ValueError :#line:416
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:417
        OOO0OOO0OOO000OO0 =1 #line:418
    OO00OOO0OOOO0OOO0 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:420
    if OO00OOO0OOOO0OOO0 =='2':#line:421
        OOO00OO00O00OO0OO =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:422
        OOO00OO00O00OO0OO =[O000OOOO0O0OOO00O .strip ()for O000OOOO0O0OOO00O in OOO00OO00O00OO0OO if O000OOOO0O0OOO00O .strip ()]#line:423
    else :#line:424
        OOO00OO00O00OO0OO =[]#line:425
    O0O0O0O00O0000OOO =set ()#line:427
    for O000OO0O0O000O00O in OO00O00OO0OOOO0O0 :#line:428
        O00OOO0OO0OO00O00 =fetch_channels (O000OO0O0O000O00O ,OO000OO00O00O0OO0 )#line:429
        for OOO00O0OO000OO0OO in O00OOO0OO0OO00O00 :#line:430
            O0OO0O0OOO0OOOO0O =fetch_messages (O000OO0O0O000O00O ,OOO00O0OO000OO0OO ,limit =100 )#line:431
            OOO00O0OO0OOOOOOO =extract_uids_from_messages (O0OO0O0OOO0OOOO0O )#line:432
            O0O0O0O00O0000OOO .update (OOO00O0OO0OOOOOOO )#line:433
    O0O0O0O00O0000OOO =list (set (O0O0O0O00O0000OOO )-set (OO0OO00O0O0O00OOO ))#line:436
    for _O0OOOOO00OOO0O00O in range (OOO0OOO0OOO000OO0 ):#line:438
        for O000OO0O0O000O00O in OO00O00OO0OOOO0O0 :#line:439
            if OOO00OO00O00OO0OO :#line:440
                O00OOO0OO0OO00O00 =OOO00OO00O00OO0OO #line:441
            for OOO00O0OO000OO0OO in O00OOO0OO0OO00O00 :#line:442
                send_message_with_mention (O000OO0O0O000O00O ,OOO00O0OO000OO0OO ,OO00OOOOO0OOOO0OO ,O0O0O0O00O0000OOO )#line:443
                time .sleep (OO0OOO0000OOO0OOO )#line:444
def join_discord_invite ():#line:449
    try :#line:450
        with open ("token.txt")as OO0O000O000OOO0OO :#line:451
            OOOO00OO0O0O000OO =[O0O00O0O00OOOO0OO .strip ()for O0O00O0O00OOOO0OO in OO0O000O000OOO0OO .readlines ()if O0O00O0O00OOOO0OO .strip ()]#line:452
    except (FileNotFoundError ,KeyError ):#line:453
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:454
        return #line:455
    OOOO0OO000O000O00 =input ("Invite Code?: discord.gg/").strip ()#line:457
    for OOO0OOOOOO0O0O00O in OOOO00OO0O0O000OO :#line:460
        joiner (OOO0OOOOOO0O0O00O ,OOOO0OO000O000O00 )#line:461
import json ,time ,base64 ,random ,requests #line:463
def cookieset (OOO00OO00OO00O0OO ):#line:465
    OOOOO00OO0OO00OO0 =OOO00OO00OO00O0OO .get ("https://discord.com/app")#line:466
    return OOOOO00OO0OO00OO0 .cookies .get_dict ()#line:467
def generatexspandua (OOOO00O0O0O0O0OOO ):#line:469
    OOO0000OOO0OOOO00 =["Android","Windows","Macintosh"]#line:470
    O000O0O0OO0O00OO0 =random .choice (OOO0000OOO0OOOO00 )#line:471
    if O000O0O0OO0O00OO0 =="Macintosh":#line:472
        O0O0O00O0O0OOO000 =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:473
        OO00OOO0OOOO0OO00 ="Macintosh; Intel Mac OS X "+O0O0O00O0O0OOO000 #line:474
        O0OOOOOOO0OO00000 ="x86_64"#line:475
    elif O000O0O0OO0O00OO0 =="Windows":#line:476
        O0O0O00O0O0OOO000 =f'{random.choice([6.0, 10.0, 11.0])}'#line:477
        OO00OOO0OOOO0OO00 ="Windows NT "+O0O0O00O0O0OOO000 +" Win64; x64"#line:478
        O0OOOOOOO0OO00000 ="x86_64"#line:479
    else :#line:480
        O0O0O00O0O0OOO000 ="13"#line:481
        OO00OOO0OOOO0OO00 =f"Linux; Android 13; Pixel 6a"#line:482
        O0OOOOOOO0OO00000 ="aarch64"#line:483
    OOOOO00OOO00OO000 ={"os":O000O0O0OO0O00OO0 ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":O0O0O00O0O0OOO000 ,"os_arch":O0OOOOOOO0OO00000 ,"system_locale":"ja-JP","client_build_number":OOOO00O0O0O0O0OOO ,"client_event_source":None ,"design_id":0 }#line:496
    OO00OOO00OO0OOO0O =f"Mozilla/5.0 ({OO00OOO0OOOO0OO00}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:497
    return base64 .b64encode (json .dumps (OOOOO00OOO00OO000 ,separators =(',',':')).encode ()).decode (),OO00OOO00OO0OOO0O #line:498
def joiner (OOOOOOO00000O0OO0 ,O0000O0OO0O000OO0 ,OO0000OO00OO0O0O0 ):#line:500
    OO0OO00OO0O00000O =cookieset (OO0000OO00OO0O0O0 )#line:501
    OO0OO00OO0O00000O ["locale"]="ja-JP"#line:502
    O0OOO0OOOOO00O0O0 =201211 #line:503
    OO00OOO000O00OO0O ,O00O00OO0OOOOOO00 =generatexspandua (O0OOO0OOOOO00O0O0 )#line:504
    O0OOOO0O0OO000OOO ={"Authorization":OOOOOOO00000O0OO0 ,"accept":"*/*","accept-language":"ja-JP","connection":"keep-alive","DNT":"1","origin":"https://discord.com","sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","referer":"https://discord.com/channels/@me","TE":"Trailers","user-agent":O00O00OO0OOOOOO00 ,"X-Super-Properties":OO00OOO000O00OO0O ,}#line:519
    OO00O00O00000OOO0 =OO0000OO00OO0O0O0 .post ("https://discord.com/api/v9/invites/"+O0000O0OO0O000OO0 ,headers =O0OOOO0O0OO000OOO ,json ={},cookies =OO0OO00OO0O00000O )#line:520
    if OO00O00O00000OOO0 .status_code ==200 :#line:521
        print ("[+] join this server "+OOOOOOO00000O0OO0 )#line:522
        if "show_verification_form"in OO00O00O00000OOO0 .json ():#line:523
            bypass (OOOOOOO00000O0OO0 ,OO00O00O00000OOO0 .json ()["guild"]["id"],OO0000OO00OO0O0O0 ,O0OOOO0O0OO000OOO )#line:524
        return #line:525
    elif "captcha_key"in OO00O00O00000OOO0 .text and OO00O00O00000OOO0 .status_code ==400 :#line:526
        print ("[!] Hcaptcha protect"+OOOOOOO00000O0OO0 )#line:527
        return #line:528
    elif OO00O00O00000OOO0 .status_code ==401 :#line:529
        print ("[×] token is dead"+OOOOOOO00000O0OO0 )#line:530
        return #line:531
    elif OO00O00O00000OOO0 .status_code ==403 :#line:532
        print ("[!] 403 banned "+OOOOOOO00000O0OO0 )#line:533
        return #line:534
    elif OO00O00O00000OOO0 .status_code ==429 :#line:535
        O0O000OOO0O0OO0O0 =OO00O00O00000OOO0 .json ().get ("retry_after",1 )#line:536
        print (f"[!] 429 rate limit. Retrying after {O0O000OOO0O0OO0O0} seconds.")#line:537
        time .sleep (O0O000OOO0O0OO0O0 )#line:538
        return #line:539
    else :#line:540
        print ("[!] error "+OOOOOOO00000O0OO0 )#line:541
        return #line:542
def update_group_ids ():#line:544
    O0OO0OOO000000O00 =input ("Invite Code?: ").strip ()#line:545
    try :#line:546
        with open ("token.txt")as OO0OO00OOOO000000 :#line:547
            OOOOOO0O0000O0OOO =[O0OOOO0OOOO0OOOOO .strip ()for O0OOOO0OOOO0OOOOO in OO0OO00OOOO000000 .readlines ()if O0OOOO0OOOO0OOOOO .strip ()]#line:548
    except (FileNotFoundError ,KeyError ):#line:549
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:550
        return #line:551
    O0OO0OO0OOOOO0000 =requests .Session ()#line:553
    for OO0O0OOOOO000OO00 in OOOOOO0O0000O0OOO :#line:554
        joiner (OO0O0OOOOO000OO00 ,O0OO0OOO000000O00 ,O0OO0OO0OOOOO0000 )#line:555
        time .sleep (2 )#line:556
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:558
def bypass (OO00000OO0OOO0000 ,O0O00000O000000OO ,O00OOOOOOO00O0O0O ,OO00O00O0OO0O00OO ):#line:561
    try :#line:562
        O0OO0O0O0O0OOOO00 =O00OOOOOOO00O0O0O .get (f"https://discord.com/api/v9/guilds/{O0O00000O000000OO}/member-verification?with_guild=false",headers =OO00O00O0OO0O00OO ).json ()#line:563
        O0OOO0OOOOOOOOO00 =O00OOOOOOO00O0O0O .put (f"https://discord.com/api/v9/guilds/{O0O00000O000000OO}/requests/@me",headers =OO00O00O0OO0O00OO ,json =O0OO0O0O0O0OOOO00 )#line:564
        if O0OOO0OOOOOOOOO00 .status_code ==201 :#line:565
            print (f"[+] MemberscreeningBypassed {OO00000OO0OOO0000}")#line:566
            return #line:567
        else :#line:568
            print (f"[!] Bypassが出来ませんでした {OO00000OO0OOO0000}")#line:569
            return #line:570
    except Exception as O0000O0OOOO0OOO0O :#line:571
        print (f"[!] エラーが発生しました。{O0000O0OOOO0OOO0O}")#line:572
session =requests .Session ()#line:574
def reactionput (O00OOOO0OO0OOO0OO ,OO0OOOOOOOOO0O0O0 ,O0000O0O0OOOO0O00 ,O000OOOO0000000O0 ,proxy =None ):#line:577
    O0O00O000O00OOOOO =get_session (proxy )#line:578
    O00O00OOOO0O0000O =get_headers (O0O00O000O00OOOOO )#line:579
    O00O00OOOO0O0000O ["Authorization"]=O00OOOO0OO0OOO0OO #line:580
    O000OOOO0000000O0 =requests .utils .quote (O000OOOO0000000O0 )#line:582
    O0OOO0000O00O0O00 =O0O00O000O00OOOOO .put (f"https://discord.com/api/v9/channels/{OO0OOOOOOOOO0O0O0}/messages/{O0000O0O0OOOO0O00}/reactions/{O000OOOO0000000O0}/%40me?location=Message&type=0",headers =O00O00OOOO0O0000O )#line:586
    if O0OOO0000O00O0O00 .status_code in [200 ,204 ]:#line:587
        print (f"[+] Reaction '{O000OOOO0000000O0}' added successfully to message {O0000O0O0OOOO0O00}")#line:588
    elif O0OOO0000O00O0O00 .status_code ==429 :#line:589
        print ("[-] Rate limited. Please wait before retrying.")#line:590
        OOOOOO00OOO00O0OO =O0OOO0000O00O0O00 .json ().get ("retry_after",1 )#line:591
        time .sleep (OOOOOO00OOO00O0OO )#line:592
    elif O0OOO0000O00O0O00 .status_code ==401 :#line:593
        print ("[-] Invalid or expired token.")#line:594
    else :#line:595
        print (f"[!] Error occurred: {O0OOO0000O00O0O00.status_code}")#line:596
def generatexspandua (OO00OOOOOOOOO0OOO ):#line:599
  O00O00O0OOOO000O0 =["Android","Windows","Macintosh"]#line:600
  OOO00O00O0O000O00 =random .choice (O00O00O0OOOO000O0 )#line:601
  if OOO00O00O0O000O00 =="Macintosh":#line:602
    O0000OOOOO0000OO0 =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:603
    O0O000O0OO0O00O00 ="Macintosh; Intel Mac OS X "+O0000OOOOO0000OO0 #line:604
    OOO0O000O0000OO00 ="x86_64"#line:605
  if OOO00O00O0O000O00 =="Windows":#line:606
    O0000OOOOO0000OO0 =f'{random.choice([6.0,10.0,11.0])}'#line:607
    O0O000O0OO0O00O00 ="Windows NT "+O0000OOOOO0000OO0 +" Win64; x64"#line:608
    OOO0O000O0000OO00 ="x86_64"#line:609
  if OOO00O00O0O000O00 =="Android":#line:610
    O0000OOOOO0000OO0 ="13"#line:611
    O0O000O0OO0O00O00 =f"Linux; Android 13; Pixel 6a"#line:612
    OOO0O000O0000OO00 ="aarch64"#line:613
  O0OOO0OOO000O0OOO ={"os":OOO00O00O0O000O00 ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":O0000OOOOO0000OO0 ,"os_arch":OOO0O000O0000OO00 ,"system_locale":"ja-JP","client_build_number":OO00OOOOOOOOO0OOO ,"client_event_source":None ,"design_id":0 }#line:614
  O0OOOO0000O000000 =f"Mozilla/5.0 ({O0O000O0OO0O00O00}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:615
  return base64 .b64encode (json .dumps (O0OOO0OOO000O0OOO ,separators =(',',':')).encode ()).decode (),O0OOOO0000O000000 #line:616
import base64 #line:618
def nickchanger ():#line:621
    try :#line:622
        with open ("token.txt")as O0OO00OOOO00O0O00 :#line:623
            O0O00OO000000OO00 =[O0OOOOO000OOO0O00 .strip ()for O0OOOOO000OOO0O00 in O0OO00OOOO00O0O00 .readlines ()if O0OOOOO000OOO0O00 .strip ()]#line:624
    except (FileNotFoundError ,KeyError ):#line:625
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:626
        return #line:627
    OOO0O000OO0OO00O0 =input ("Server ID?: ").strip ()#line:629
    OOOOOOO000O000OOO =input ("Nickname?: ").strip ()#line:630
    O0O000OO00O000OO0 =input ("Delay (in seconds)?: ").strip ()#line:631
    try :#line:633
        O0O000OO00O000OO0 =float (O0O000OO00O000OO0 )#line:634
        if O0O000OO00O000OO0 <0 :#line:635
            raise ValueError #line:636
    except ValueError :#line:637
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:638
        O0O000OO00O000OO0 =1.0 #line:639
    for O0O00OOO000OOOOOO in O0O00OO000000OO00 :#line:641
        O0O0O0OO0OOO0OO00 ={"Authorization":O0O00OOO000OOOOOO ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:646
        OO000OO0OOOO000OO ={"nick":OOOOOOO000O000OOO }#line:647
        O0O00O0OOOOO0OO0O =requests .patch (f"https://discord.com/api/v9/guilds/{OOO0O000OO0OO00O0}/members/@me",headers =O0O0O0OO0OOO0OO00 ,json =OO000OO0OOOO000OO )#line:648
        if O0O00O0OOOOO0OO0O .status_code ==200 :#line:650
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Nickname changed to '{OOOOOOO000O000OOO}' successfully for token {O0O00OOO000OOOOOO}.{colorama.Fore.RESET}")#line:651
        elif O0O00O0OOOOO0OO0O .status_code ==429 :#line:652
            print (f"{colorama.Fore.RED}    [!] Rate limited. Please wait before retrying for token {O0O00OOO000OOOOOO}.{colorama.Fore.RESET}")#line:653
            OO0OOOO0O0O00O0O0 =O0O00O0OOOOO0OO0O .json ().get ("retry_after",1 )#line:654
            time .sleep (OO0OOOO0O0O00O0O0 )#line:655
        else :#line:656
            print (f"{colorama.Fore.RED}    [!] Error occurred: {O0O00O0OOOOO0OO0O.status_code} for token {O0O00OOO000OOOOOO}.{colorama.Fore.RESET}")#line:657
        time .sleep (O0O000OO00O000OO0 )#line:659
import json ,websocket ,threading ,tls_client ,random ,time #line:663
session =tls_client .Session (client_identifier ="chrome112",random_tls_extension_order =True )#line:665
class Utils :#line:667
    @staticmethod #line:668
    def rangeCorrector (OO0OO00O0OOOOOOO0 ):#line:669
        if [0 ,99 ]not in OO0OO00O0OOOOOOO0 :#line:670
            OO0OO00O0OOOOOOO0 .insert (0 ,[0 ,99 ])#line:671
        return OO0OO00O0OOOOOOO0 #line:672
    @staticmethod #line:674
    def getRanges (O0O0O000OO0O0OOOO ,OOOOOO0O0O0OOO0OO ,OOO0OOO000OOO0O0O ):#line:675
        OO0O0OOOO0OOO0O0O =int (O0O0O000OO0O0OOOO *OOOOOO0O0O0OOO0OO )#line:676
        OOOO00O00000OO00O =[[OO0O0OOOO0OOO0O0O ,OO0O0OOOO0OOO0O0O +99 ]]#line:677
        if OOO0OOO000OOO0O0O >OO0O0OOOO0OOO0O0O +99 :#line:678
            OOOO00O00000OO00O .append ([OO0O0OOOO0OOO0O0O +100 ,OO0O0OOOO0OOO0O0O +199 ])#line:679
        return Utils .rangeCorrector (OOOO00O00000OO00O )#line:680
    @staticmethod #line:682
    def parseGuildMemberListUpdate (OO0000000OO0OOOOO ):#line:683
        O00OOO0O0O0OOOOO0 ={"online_count":OO0000000OO0OOOOO ["d"]["online_count"],"member_count":OO0000000OO0OOOOO ["d"]["member_count"],"id":OO0000000OO0OOOOO ["d"]["id"],"guild_id":OO0000000OO0OOOOO ["d"]["guild_id"],"hoisted_roles":OO0000000OO0OOOOO ["d"]["groups"],"types":[],"locations":[],"updates":[],}#line:693
        for O0O0OOO0000OO0OO0 in OO0000000OO0OOOOO ["d"]["ops"]:#line:695
            O00OOO0O0O0OOOOO0 ["types"].append (O0O0OOO0000OO0OO0 ["op"])#line:696
            if O0O0OOO0000OO0OO0 ["op"]in ("SYNC","INVALIDATE"):#line:697
                O00OOO0O0O0OOOOO0 ["locations"].append (O0O0OOO0000OO0OO0 ["range"])#line:698
                if O0O0OOO0000OO0OO0 ["op"]=="SYNC":#line:699
                    O00OOO0O0O0OOOOO0 ["updates"].append (O0O0OOO0000OO0OO0 ["items"])#line:700
                else :#line:701
                    O00OOO0O0O0OOOOO0 ["updates"].append ([])#line:702
            elif O0O0OOO0000OO0OO0 ["op"]in ("INSERT","UPDATE","DELETE"):#line:703
                O00OOO0O0O0OOOOO0 ["locations"].append (O0O0OOO0000OO0OO0 ["index"])#line:704
                if O0O0OOO0000OO0OO0 ["op"]=="DELETE":#line:705
                    O00OOO0O0O0OOOOO0 ["updates"].append ([])#line:706
                else :#line:707
                    O00OOO0O0O0OOOOO0 ["updates"].append (O0O0OOO0000OO0OO0 ["item"])#line:708
        return O00OOO0O0O0OOOOO0 #line:709
class DiscordSocket (websocket .WebSocketApp ):#line:711
    def __init__ (O00OOO0OO0000OO00 ,O0OOO00OO0OOOO0OO ,OO0OO0O00OOOO000O ,OO00O0OOO0O0O0OO0 ):#line:712
        O00OOO0OO0000OO00 .token =O0OOO00OO0OOOO0OO #line:713
        O00OOO0OO0000OO00 .guild_id =OO0OO0O00OOOO000O #line:714
        O00OOO0OO0000OO00 .channel_id =OO00O0OOO0O0O0OO0 #line:715
        O00OOO0OO0000OO00 .socket_headers ={"Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","Cache-Control":"no-cache","Pragma":"no-cache","Sec-WebSocket-Extensions":"permessage-deflate; client_max_window_bits","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",}#line:723
        super ().__init__ ("wss://gateway.discord.gg/?encoding=json&v=9",header =O00OOO0OO0000OO00 .socket_headers ,on_open =lambda OOOOOO0O000O00OOO :O00OOO0OO0000OO00 .sock_open (OOOOOO0O000O00OOO ),on_message =lambda OOO000OO0O000OO0O ,O0000O0O00OOOO000 :O00OOO0OO0000OO00 .sock_message (OOO000OO0O000OO0O ,O0000O0O00OOOO000 ),on_close =lambda O0000OOOOOO0OO0OO ,O0000O0OOOO000000 ,OO0OO00O0OOO0O0OO :O00OOO0OO0000OO00 .sock_close (O0000OOOOOO0OO0OO ,O0000O0OOOO000000 ,OO0OO00O0OOO0O0OO ),)#line:732
        O00OOO0OO0000OO00 .endScraping =False #line:734
        O00OOO0OO0000OO00 .guilds ={}#line:735
        O00OOO0OO0000OO00 .members ={}#line:736
        O00OOO0OO0000OO00 .ranges =[[0 ,0 ]]#line:737
        O00OOO0OO0000OO00 .lastRange =0 #line:738
        O00OOO0OO0000OO00 .packets_recv =0 #line:739
    def run (O000000O00000OO00 ):#line:741
        O000000O00000OO00 .run_forever ()#line:742
        return O000000O00000OO00 .members #line:743
    def scrapeUsers (O0OO0O00OO0O0O00O ):#line:745
        if not O0OO0O00OO0O0O00O .endScraping :#line:746
            O0OO0O00OO0O0O00O .send ('{"op":14,"d":{"guild_id":"'+O0OO0O00OO0O0O00O .guild_id +'","typing":true,"activities":true,"threads":true,"channels":{"'+O0OO0O00OO0O0O00O .channel_id +'":'+json .dumps (O0OO0O00OO0O0O00O .ranges )+"}}}")#line:755
    def sock_open (OO0O00000OOOO0OO0 ,OO0000OOOO0OO00OO ):#line:757
        OO0O00000OOOO0OO0 .send ('{"op":2,"d":{"token":"'+OO0O00000OOOO0OO0 .token +'","capabilities":125,"properties":{"os":"Windows NT","browser":"Chrome","device":"","system_locale":"it-IT","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36","browser_version":"119.0","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":103981,"client_event_source":null},"presence":{"status":"online","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}')#line:762
    def heartbeatThread (OOOOOO000O000O0OO ,OOO00OO0OOO00000O ):#line:764
        try :#line:765
            while True :#line:766
                OOOOOO000O000O0OO .send ('{"op":1,"d":'+str (OOOOOO000O000O0OO .packets_recv )+"}")#line:767
                time .sleep (OOO00OO0OOO00000O )#line:768
        except Exception as O00O0000OO000O000 :#line:769
            pass #line:770
    def sock_message (O0O000OO0OO0OO00O ,O0O0OOOO00OO00OO0 ,O00O000OOOO0O00OO ):#line:772
        O00OO0O000O0O000O =json .loads (O00O000OOOO0O00OO )#line:773
        if O00OO0O000O0O000O is None :#line:774
            return #line:775
        if O00OO0O000O0O000O ["op"]!=11 :#line:776
            O0O000OO0OO0OO00O .packets_recv +=1 #line:777
        if O00OO0O000O0O000O ["op"]==10 :#line:778
            threading .Thread (target =O0O000OO0OO0OO00O .heartbeatThread ,args =(O00OO0O000O0O000O ["d"]["heartbeat_interval"]/1000 ,),daemon =True ,).start ()#line:783
        if O00OO0O000O0O000O ["t"]=="READY":#line:784
            for OOO00OO0OOO00O00O in O00OO0O000O0O000O ["d"]["guilds"]:#line:785
                O0O000OO0OO0OO00O .guilds [OOO00OO0OOO00O00O ["id"]]={"member_count":OOO00OO0OOO00O00O ["member_count"]}#line:786
        if O00OO0O000O0O000O ["t"]=="READY_SUPPLEMENTAL":#line:787
            O0O000OO0OO0OO00O .ranges =Utils .getRanges (0 ,100 ,O0O000OO0OO0OO00O .guilds [O0O000OO0OO0OO00O .guild_id ]["member_count"])#line:790
            O0O000OO0OO0OO00O .scrapeUsers ()#line:791
        elif O00OO0O000O0O000O ["t"]=="GUILD_MEMBER_LIST_UPDATE":#line:792
            OO000O00O0O0OO0OO =Utils .parseGuildMemberListUpdate (O00OO0O000O0O000O )#line:793
            if OO000O00O0O0OO0OO ["guild_id"]==O0O000OO0OO0OO00O .guild_id and ("SYNC"in OO000O00O0O0OO0OO ["types"]or "UPDATE"in OO000O00O0O0OO0OO ["types"]):#line:797
                for OO00000OO00OO0O00 ,O000O0000O0O00OO0 in enumerate (OO000O00O0O0OO0OO ["types"]):#line:798
                    if O000O0000O0O00OO0 =="SYNC":#line:799
                        if len (OO000O00O0O0OO0OO ["updates"][OO00000OO00OO0O00 ])==0 :#line:800
                            O0O000OO0OO0OO00O .endScraping =True #line:801
                            break #line:802
                        for O0O000OO0OOOO00OO in OO000O00O0O0OO0OO ["updates"][OO00000OO00OO0O00 ]:#line:804
                            if "member"in O0O000OO0OOOO00OO :#line:805
                                O00OO000OO0O0O00O =O0O000OO0OOOO00OO ["member"]#line:806
                                OO00O0O0O0OOOO00O ={"tag":O00OO000OO0O0O00O ["user"]["username"]+"#"+O00OO000OO0O0O00O ["user"]["discriminator"],"id":O00OO000OO0O0O00O ["user"]["id"],}#line:812
                                if not O00OO000OO0O0O00O ["user"].get ("bot"):#line:813
                                    O0O000OO0OO0OO00O .members [O00OO000OO0O0O00O ["user"]["id"]]=OO00O0O0O0OOOO00O #line:814
                    elif O000O0000O0O00OO0 =="UPDATE":#line:816
                        for O0O000OO0OOOO00OO in OO000O00O0O0OO0OO ["updates"][OO00000OO00OO0O00 ]:#line:817
                            if "member"in O0O000OO0OOOO00OO :#line:818
                                O00OO000OO0O0O00O =O0O000OO0OOOO00OO ["member"]#line:819
                                OO00O0O0O0OOOO00O ={"tag":O00OO000OO0O0O00O ["user"]["username"]+"#"+O00OO000OO0O0O00O ["user"]["discriminator"],"id":O00OO000OO0O0O00O ["user"]["id"],}#line:825
                                if not O00OO000OO0O0O00O ["user"].get ("bot"):#line:826
                                    O0O000OO0OO0OO00O .members [O00OO000OO0O0O00O ["user"]["id"]]=OO00O0O0O0OOOO00O #line:827
                    O0O000OO0OO0OO00O .lastRange +=1 #line:829
                    O0O000OO0OO0OO00O .ranges =Utils .getRanges (O0O000OO0OO0OO00O .lastRange ,100 ,O0O000OO0OO0OO00O .guilds [O0O000OO0OO0OO00O .guild_id ]["member_count"])#line:832
                    time .sleep (0.45 )#line:833
                    O0O000OO0OO0OO00O .scrapeUsers ()#line:834
            if O0O000OO0OO0OO00O .endScraping :#line:836
                O0O000OO0OO0OO00O .close ()#line:837
    def sock_close (O00O0O0OO0O000000 ,O0O000OO0O0O0O00O ,O0OO0000OO00O0OOO ,OOOO0OO0O0OOO00O0 ):#line:839
        pass #line:840
def scrape (O00O00OOOO0O000O0 ,OOOOO0O000O0000O0 ,O0000OO0O0O000O00 ):#line:842
    OO0OOO0OOOO0000OO =DiscordSocket (O00O00OOOO0O000O0 ,OOOOO0O000O0000O0 ,O0000OO0O0O000O00 )#line:843
    return OO0OOO0OOOO0000OO .run ()#line:844
def member_scrape (O000O0OO000000000 ,O0O00OO00OO000OO0 ,O000O0OOOO00OO0O0 ):#line:846
    O00O00OO000000O00 =[]#line:847
    for OO0O000OO0O0000O0 in O000O0OO000000000 :#line:848
        OOOOOOOOO0000O00O ={"Authorization":OO0O000OO0O0000O0 ,"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}#line:849
        OOOOOO0OO0OOO0O0O =session .get (f"https://canary.discord.com/api/v9/guilds/{O0O00OO00OO000OO0}",headers =OOOOOOOOO0000O00O )#line:850
        if OOOOOO0OO0OOO0O0O .status_code ==200 :#line:851
            O00O00OO000000O00 .append (OO0O000OO0O0000O0 )#line:852
            break #line:853
    if not O00O00OO000000O00 :#line:854
        print ("missing access")#line:855
    OO0O000OO0O0000O0 =random .choice (O00O00OO000000O00 )#line:857
    O00OOO0O000000O0O =scrape (OO0O000OO0O0000O0 ,O0O00OO00OO000OO0 ,O000O0OOOO00OO0O0 )#line:858
    OOOO0OOO00O0OOOO0 =[f"<@{OO000O000O00OO0O0}>"for OO000O000O00OO0O0 in [int (OOO0O00OO0000O0O0 )for OOO0O00OO0000O0O0 in O00OOO0O000000O0O .keys ()]]#line:859
    print (f"[SUCCESS] {len(OOOO0OOO00O0OOOO0)} scraped members")#line:860
    return OOOO0OOO00O0OOOO0 #line:861
def spammer_menu ():#line:863
    try :#line:864
        with open ("token.txt")as O0000OO0OO0000000 :#line:865
            OOOO0OOO000OOOO0O =[O0O0OO0OOO0OOO000 .strip ()for O0O0OO0OOO0OOO000 in O0000OO0OO0000000 .readlines ()if O0O0OO0OOO0OOO000 .strip ()]#line:866
    except (FileNotFoundError ,KeyError ):#line:867
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:868
        return #line:869
    O00OO0OO000O00O00 =input ("Server ID?: ").strip ()#line:871
    O0O00OO0OOO000O00 =input ("Message?: ").strip ()#line:872
    O00O0OO0OO00000O0 =input ("Random mention (True/False)?: ").strip ().lower ()=='true'#line:873
    O0OO00O0O000000OO =input ("Delay between messages (in seconds)?: ").strip ()#line:874
    O000O000O000OOO0O =input ("Number of messages to send?: ").strip ()#line:875
    O00OOOOO0O00OO00O =input ("Blacklist User IDs (comma-separated) (Leave blank to skip)?: ").strip ().split (',')#line:876
    O00OOOOO0O00OO00O =[f"<@{O000OO0OO00O00O0O.strip()}>"for O000OO0OO00O00O0O in O00OOOOO0O00OO00O if O000OO0OO00O00O0O .strip ()]#line:877
    try :#line:879
        O0OO00O0O000000OO =float (O0OO00O0O000000OO )#line:880
        if O0OO00O0O000000OO <0 :#line:881
            raise ValueError #line:882
    except ValueError :#line:883
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:884
        O0OO00O0O000000OO =1.0 #line:885
    try :#line:887
        O000O000O000OOO0O =int (O000O000O000OOO0O )#line:888
        if O000O000O000OOO0O <=0 :#line:889
            raise ValueError #line:890
    except ValueError :#line:891
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:892
        O000O000O000OOO0O =1 #line:893
    OOO0O0OOOO0OOOOO0 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:895
    if OOO0O0OOOO0OOOOO0 =='2':#line:896
        OOO00O0OO00OO00O0 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:897
        OOO00O0OO00OO00O0 =[O0OO0OO00OOO0OO00 .strip ()for O0OO0OO00OOO0OO00 in OOO00O0OO00OO00O0 if O0OO0OO00OOO0OO00 .strip ()]#line:898
    else :#line:899
        OOO00O0OO00OO00O0 =fetch_channels (OOOO0OOO000OOOO0O [0 ],O00OO0OO000O00O00 )#line:900
    OOO000O00O0O000O0 =None #line:902
    spammer (OOOO0OOO000OOOO0O ,O00OO0OO000O00O00 ,OOO00O0OO00OO00O0 ,O0O00OO0OOO000O00 ,O00O0OO0OO00000O0 ,O00OOOOO0O00OO00O ,OOO000O00O0O000O0 ,O000O000O000OOO0O )#line:904
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:906
def spammer (OOOOOOOOOOOO0OO00 ,OO0000O0OO00OO000 ,OO0O0O0OO00O00OO0 ,O0O0OO0OO00OOO0OO ,OO0O0000OOO00OOO0 ,O0O0O0O0000000O0O ,OOOO00OO00OO0OO0O ,OOOO0O00O0OO0O0O0 ):#line:908
    OO000000OO000O00O =get_session (OOOO00OO00OO0OO0O )#line:909
    OOOO0O0O000OOO0OO =0 #line:910
    OOO000O00OO0OOO00 =member_scrape (OOOOOOOOOOOO0OO00 ,OO0000O0OO00OO000 ,OO0O0O0OO00O00OO0 [0 ])#line:912
    OOO000O00OO0OOO00 =[OO0OOOO00OO00OO00 for OO0OOOO00OO00OO00 in OOO000O00OO0OOO00 if OO0OOOO00OO00OO00 not in O0O0O0O0000000O0O ]#line:913
    for _OOOOO0O00O0OOO00O in range (OOOO0O00O0OO0O0O0 ):#line:915
        OO0OOO0O0OO0000OO =OOOOOOOOOOOO0OO00 [OOOO0O0O000OOO0OO ]#line:916
        OO0000O0O0O000O0O =get_headers (OO0OOO0O0OO0000OO )#line:917
        for OO0OOOO00O0O0OO0O in OO0O0O0OO00O00OO0 :#line:918
            O0O0O0O0O0O0000OO =O0O0OO0OO00OOO0OO #line:919
            if OO0O0000OOO00OOO0 and OOO000O00OO0OOO00 :#line:920
                OOO00OOOO0O0OOOOO =random .choice (OOO000O00OO0OOO00 )#line:921
                O0O0O0O0O0O0000OO +=f" {OOO00OOOO0O0OOOOO}"#line:922
            O00O000OOOO0O0000 =OO000000OO000O00O .post (f"https://discord.com/api/v9/channels/{OO0OOOO00O0O0OO0O}/messages",json ={"content":O0O0O0O0O0O0000OO },headers =OO0000O0O0O000O0O )#line:924
            if O00O000OOOO0O0000 .status_code ==200 :#line:925
                print (f"200 message sent: {OO0OOO0O0OO0000OO}")#line:926
            elif O00O000OOOO0O0000 .status_code ==429 :#line:927
                print (f"429 rate limit: {OO0OOO0O0OO0000OO}")#line:928
                O0O00OO00OOO0O000 =O00O000OOOO0O0000 .json ().get ("retry_after",1 )#line:929
                time .sleep (O0O00OO00OOO0O000 )#line:930
            elif O00O000OOOO0O0000 .status_code ==401 :#line:931
                print (f"401 unknown token: {OO0OOO0O0OO0000OO}")#line:932
            else :#line:933
                print (f"error: {OO0OOO0O0OO0000OO}")#line:934
        OOOO0O0O000OOO0OO =(OOOO0O0O000OOO0OO +1 )%len (OOOOOOOOOOOO0OO00 )#line:936
        time .sleep (1 )#line:937
import requests #line:941
import base64 #line:942
import colorama #line:943
import time #line:944
def add_emojis_from_files ():#line:946
    try :#line:947
        with open ("emojiname.txt")as OO0OOOO0000O0OO00 ,open ("emojiurl.txt")as OO0000000O00000OO :#line:948
            O0000000OO000O00O =[O0O0O0O0O000000O0 .strip ()for O0O0O0O0O000000O0 in OO0OOOO0000O0OO00 .read ().split (',')if O0O0O0O0O000000O0 .strip ()]#line:949
            O00O0OOOOO0O000O0 =[O000OO0OOO0O0OOO0 .strip ()for O000OO0OOO0O0OOO0 in OO0000000O00000OO .read ().split (',')if O000OO0OOO0O0OOO0 .strip ()]#line:950
    except FileNotFoundError as OOOOOOOOO0000OOO0 :#line:951
        print (f"{colorama.Fore.RED}    [!] Error: {str(OOOOOOOOO0000OOO0)}{colorama.Fore.RESET}")#line:952
        return #line:953
    if len (O0000000OO000O00O )!=len (O00O0OOOOO0O000O0 ):#line:955
        print (f"{colorama.Fore.RED}    [!] Error: The number of emoji names and URLs do not match!{colorama.Fore.RESET}")#line:956
        return #line:957
    try :#line:959
        with open ("token.txt")as O00OO000OOOO00000 :#line:960
            OO0OO0OO0O0OOOOO0 =[O00OO0O0O00000000 .strip ()for O00OO0O0O00000000 in O00OO000OOOO00000 .readlines ()if O00OO0O0O00000000 .strip ()]#line:961
    except FileNotFoundError as OOOOOOOOO0000OOO0 :#line:962
        print (f"{colorama.Fore.RED}    [!] Error: {str(OOOOOOOOO0000OOO0)}{colorama.Fore.RESET}")#line:963
        return #line:964
    OO0OOO00O00O0O000 =input ("Enter the Guild ID: ").strip ()#line:966
    O00O0O0O00O0OO000 =input ("Enter the rate limit between requests (in seconds): ").strip ()#line:967
    try :#line:969
        O00O0O0O00O0OO000 =float (O00O0O0O00O0OO000 )#line:970
        if O00O0O0O00O0OO000 <0 :#line:971
            raise ValueError #line:972
    except ValueError :#line:973
        print (f"{colorama.Fore.RED}    [!] Invalid rate limit. Using default rate limit of 5 seconds.{colorama.Fore.RESET}")#line:974
        O00O0O0O00O0OO000 =5.0 #line:975
    O0000O0O00OOO0O00 =set ()#line:977
    for OO000OO00OOO0O0OO in OO0OO0OO0O0OOOOO0 :#line:979
        O0OOOOO0OOO0OO0OO ={'Authorization':OO000OO00OOO0O0OO ,'Content-Type':'application/json'}#line:983
        O0OOO00O00O0000O0 =requests .get (f"https://discord.com/api/v9/guilds/{OO0OOO00O00O0O000}/emojis",headers =O0OOOOO0OOO0OO0OO )#line:986
        if O0OOO00O00O0000O0 .status_code ==200 :#line:987
            O0O0OO00OOO0OOOO0 =O0OOO00O00O0000O0 .json ()#line:988
            for OOO0OO00OOO00000O in O0O0OO00OOO0OOOO0 :#line:989
                O0000O0O00OOO0O00 .add (OOO0OO00OOO00000O ['name'])#line:990
        else :#line:991
            print (f"{colorama.Fore.RED}    [!] Error fetching existing emojis: {O0OOO00O00O0000O0.status_code} - {O0OOO00O00O0000O0.text}{colorama.Fore.RESET}")#line:992
            continue #line:993
    for OO000OOO0O00OO00O ,OO0O0000O0O00O0OO in zip (O0000000OO000O00O ,O00O0OOOOO0O000O0 ):#line:995
        if OO000OOO0O00OO00O in O0000O0O00OOO0O00 :#line:996
            print (f"{colorama.Fore.YELLOW}    [*] Emoji '{OO000OOO0O00OO00O}' already exists. Skipping...{colorama.Fore.RESET}")#line:997
            continue #line:998
        for OO000OO00OOO0O0OO in OO0OO0OO0O0OOOOO0 :#line:1000
            try :#line:1001
                O0OOO00O00O0000O0 =requests .get (OO0O0000O0O00O0OO )#line:1002
                O0OOO00O00O0000O0 .raise_for_status ()#line:1003
                O0OOO0O00OO00O0OO =O0OOO00O00O0000O0 .content #line:1004
                OO00O0OO0O0OOOOO0 =base64 .b64encode (O0OOO0O00OO00O0OO ).decode ('utf-8')#line:1005
                O00O0O0OO00OOOO00 ={'name':OO000OOO0O00OO00O ,'image':f"data:image/png;base64,{OO00O0OO0O0OOOOO0}"}#line:1010
                O0OOOOO0OOO0OO0OO ={'Authorization':OO000OO00OOO0O0OO ,'Content-Type':'application/json'}#line:1015
                OO0OOO00OO0OOO00O =requests .post (f"https://discord.com/api/v9/guilds/{OO0OOO00O00O0O000}/emojis",headers =O0OOOOO0OOO0OO0OO ,json =O00O0O0OO00OOOO00 )#line:1017
                if OO0OOO00OO0OOO00O .status_code ==201 :#line:1018
                    print (f"{colorama.Fore.GREEN}    [+] Successfully added emoji '{OO000OOO0O00OO00O}' with token {OO000OO00OOO0O0OO}{colorama.Fore.RESET}")#line:1019
                    O0000O0O00OOO0O00 .add (OO000OOO0O00OO00O )#line:1020
                    break #line:1021
                else :#line:1022
                    print (f"{colorama.Fore.RED}    [!] Failed to add emoji '{OO000OOO0O00OO00O}' with token {OO000OO00OOO0O0OO}: {OO0OOO00OO0OOO00O.status_code} - {OO0OOO00OO0OOO00O.text}{colorama.Fore.RESET}")#line:1023
                time .sleep (O00O0O0O00O0OO000 )#line:1025
            except Exception as OOOOOOOOO0000OOO0 :#line:1026
                print (f"{colorama.Fore.RED}    [!] Error adding emoji '{OO000OOO0O00OO00O}' with token {OO000OO00OOO0O0OO}: {str(OOOOOOOOO0000OOO0)}{colorama.Fore.RESET}")#line:1027
def main ():#line:1029
    colorama .init ()#line:1030
    while True :#line:1031
        logo ()#line:1032
        O0OO00O00O0OOOOO0 =input (f"{colorama.Fore.LIGHTMAGENTA_EX}    [Final] Select an option from above: ")#line:1033
        if O0OO00O00O0OOOOO0 =="0":#line:1035
            update_group_ids ()#line:1036
        elif O0OO00O00O0OOOOO0 =="1":#line:1037
            join_discord_invite ()#line:1038
        elif O0OO00O00O0OOOOO0 =="2":#line:1039
            reaction_spammer ()#line:1040
        elif O0OO00O00O0OOOOO0 =="3":#line:1041
            send_messages_with_mentions ()#line:1042
        elif O0OO00O00O0OOOOO0 =="4":#line:1043
            spammer_menu ()#line:1044
        elif O0OO00O00O0OOOOO0 =="5":#line:1045
            nickchanger ()#line:1046
        elif O0OO00O00O0OOOOO0 =="6":#line:1047
            add_emojis_from_files ()#line:1048
        elif O0OO00O00O0OOOOO0 =="7":#line:1049
            reaction_art ()#line:1050
        elif O0OO00O00O0OOOOO0 =="0":#line:1051
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [*] Exiting the application. Goodbye!{colorama.Fore.RESET}")#line:1052
            break #line:1053
        else :#line:1054
            print (f"{colorama.Fore.RED}    [!] Invalid option selected!{colorama.Fore.RESET}")#line:1055
        input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:1057
if __name__ =="__main__":#line:1059
    main ()#line:1060
