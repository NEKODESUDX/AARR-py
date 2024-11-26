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
    OOO00OO0OOOOO0O00 =requests .Session ()#line:57
    if proxy :#line:58
        OOO00OO0OOOOO0O00 .proxies ={"http":proxy ,"https":proxy }#line:59
    return OOO00OO0OOOOO0O00 #line:60
def get_headers (O00O000000OOO000O ):#line:62
    return {"Authorization":O00O000000OOO000O ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:67
def send_message_with_mention (OOO00OOO00OO0O000 ,OOOO0O0OO00O0O0O0 ,OO0O0OO0OO0OOO0OO ,O0000OOOO0000OOO0 ):#line:70
    OO0O000OOO00O00O0 =get_session ()#line:71
    O0OOOO000OOOOO00O =get_headers (OOO00OOO00OO0O000 )#line:72
    if O0000OOOO0000OOO0 :#line:74
        O00OOO0O0O00O000O =random .choice (O0000OOOO0000OOO0 )#line:75
        OO0O0OO0OO0OOO0OO +=f" <@{O00OOO0O0O00O000O}>"#line:76
    OO00O00O0OO0000OO =OO0O000OOO00O00O0 .post (f"https://discord.com/api/v9/channels/{OOOO0O0OO00O0O0O0}/messages",headers =O0OOOO000OOOOO00O ,json ={"content":OO0O0OO0OO0OOO0OO })#line:82
    if OO00O00O0OO0000OO .status_code in [200 ,201 ]:#line:83
        print (f"[+] Message sent to channel {OOOO0O0OO00O0O0O0}")#line:84
    elif OO00O00O0OO0000OO .status_code ==429 :#line:85
        print ("[-] Rate limited. Please wait before retrying.")#line:86
        O00O000O00OO000OO =OO00O00O0OO0000OO .json ().get ("retry_after",1 )#line:87
        time .sleep (O00O000O00OO000OO )#line:88
    else :#line:89
        print (f"[!] Error occurred: {OO00O00O0OO0000OO.status_code}")#line:90
def fetch_messages (O00O0O0O000OOOO0O ,O000000O0O00OO0O0 ,limit =100 ):#line:93
    O00000000OO00000O ={"Authorization":O00O0O0O000OOOO0O ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:98
    OO0O0OO0O00OOOO0O =requests .get (f"https://discord.com/api/v9/channels/{O000000O0O00OO0O0}/messages?limit={limit}",headers =O00000000OO00000O )#line:102
    if OO0O0OO0O00OOOO0O .status_code ==200 :#line:103
        return OO0O0OO0O00OOOO0O .json ()#line:104
    else :#line:105
        print (f"[!] Failed to fetch messages. HTTP Status Code: {OO0O0OO0O00OOOO0O.status_code}")#line:106
        return []#line:107
import concurrent .futures #line:108
def reaction_spammer ():#line:110
    try :#line:111
        with open ("token.txt")as OO0OO0O00O0OO0OOO :#line:112
            O0OO00O0OOO0O0O00 =[OOOOO00OO0000000O .strip ()for OOOOO00OO0000000O in OO0OO0O00O0OO0OOO .readlines ()if OOOOO00OO0000000O .strip ()]#line:113
    except (FileNotFoundError ,KeyError ):#line:114
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:115
        return #line:116
    O00OO00OOO0O0O00O =input ("Server ID?: ").strip ()#line:118
    OOOO0OOOO00OOOOO0 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:120
    if OOOO0OOOO00OOOOO0 =='2':#line:121
        OO0000O000O00000O =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:122
        OO0O0O0O0O00O000O =[OO0OO0OOOO0OO0OOO .strip ()for OO0OO0OOOO0OO0OOO in OO0000O000O00000O if OO0OO0OOOO0OO0OOO .strip ()]#line:123
    else :#line:124
        OO0O0O0O0O00O000O =[]#line:125
        for OOO0OOOOOO00OO0OO in O0OO00O0OOO0O0O00 :#line:126
            try :#line:127
                OO0O0O0O0O00O000O .extend (fetch_channels (OOO0OOOOOO00OO0OO ,O00OO00OOO0O0O00O ))#line:128
            except Exception as O000O000000O0000O :#line:129
                print (f"[!] Failed to fetch channels for token. Error: {O000O000000O0000O}")#line:130
                continue #line:131
    O0OO00OOO0OO0O000 =input ("Select your emoji (a, b, c, ... or custom emojis): ").strip ()#line:133
    O00O0O000O00000OO =input ("Delay between reactions (in seconds)?: ").strip ()#line:134
    try :#line:136
        O00O0O000O00000OO =float (O00O0O000O00000OO )#line:137
        if O00O0O000O00000OO <0 :#line:138
            raise ValueError #line:139
    except ValueError :#line:140
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:141
        O00O0O000O00000OO =1.0 #line:142
    O00OOOOOOO00O000O =[]#line:144
    for OO0OOO0000O0O000O in O0OO00OOO0OO0O000 .split (","):#line:145
        OO0OOO0000O0O000O =OO0OOO0000O0O000O .strip ().lower ()#line:146
        if OO0OOO0000O0O000O in alphabet_to_flag :#line:147
            O00OOOOOOO00O000O .append (alphabet_to_flag [OO0OOO0000O0O000O ])#line:148
        else :#line:149
            O00OOOOOOO00O000O .append (OO0OOO0000O0O000O )#line:150
    if not O00OOOOOOO00O000O :#line:152
        print (f"{colorama.Fore.RED}    [!] No valid emojis provided!{colorama.Fore.RESET}")#line:153
        return #line:154
import requests #line:156
import json #line:157
import time #line:158
import colorama #line:159
alphabet_to_flag ={'a':'🇦','b':'🇧','c':'🇨','d':'🇩','e':'🇪','f':'🇫','g':'🇬','h':'🇭','i':'🇮','j':'🇯','k':'🇰','l':'🇱','m':'🇲','n':'🇳','o':'🇴','p':'🇵','q':'🇶','r':'🇷','s':'🇸','t':'🇹','u':'🇺','v':'🇻','w':'🇼','x':'🇽','y':'🇾','z':'🇿'}#line:167
def fetch_channels (O0OO0OOOOO0OOOO00 ,OOO0O0O0O00O00OOO ):#line:169
    OOO000O00OO00000O =f"https://discord.com/api/v9/guilds/{OOO0O0O0O00O00OOO}/channels"#line:170
    OOO00OO00OOO0OOOO ={"Authorization":O0OO0OOOOO0OOOO00 }#line:171
    O0OO00O0OOO0OOOO0 =requests .get (OOO000O00OO00000O ,headers =OOO00OO00OOO0OOOO )#line:172
    if O0OO00O0OOO0OOOO0 .status_code ==200 :#line:173
        return [OO000O0O00O0O0000 ['id']for OO000O0O00O0O0000 in O0OO00O0OOO0OOOO0 .json ()if OO000O0O00O0O0000 ['type']==0 ]#line:174
    else :#line:175
        raise Exception (f"Failed to fetch channels: {O0OO00O0OOO0OOOO0.status_code} - {O0OO00O0OOO0OOOO0.text}")#line:176
def fetch_messages (O00O0OO00O000OOO0 ,OO0OOOO00OOO000O0 ,limit =100 ):#line:178
    OOOOOO0O0OOO00000 =f"https://discord.com/api/v9/channels/{OO0OOOO00OOO000O0}/messages?limit={limit}"#line:179
    O0O000000O0O0O000 ={"Authorization":O00O0OO00O000OOO0 }#line:180
    O000O0O00OOO0OOO0 =requests .get (OOOOOO0O0OOO00000 ,headers =O0O000000O0O0O000 )#line:181
    if O000O0O00OOO0OOO0 .status_code ==200 :#line:182
        return O000O0O00OOO0OOO0 .json ()#line:183
    else :#line:184
        print (f"[!] Failed to fetch messages: {O000O0O00OOO0OOO0.status_code} - {O000O0O00OOO0OOO0.text}")#line:185
        return []#line:186
def reactionput (OOO00O00000OOO0OO ,O0O0000OO00OO0O0O ,OO0000OOO0O0O000O ,O00OOOO000O00O0OO ):#line:188
    O0O000O0000OOOO0O =f"https://discord.com/api/v9/channels/{O0O0000OO00OO0O0O}/messages/{OO0000OOO0O0O000O}/reactions/{O00OOOO000O00O0OO}/@me"#line:189
    OOOO0OOO00O0OOO00 ={"Authorization":OOO00O00000OOO0OO ,"Content-Type":"application/json"}#line:190
    O00OOOO0OOOOO0O0O =requests .put (O0O000O0000OOOO0O ,headers =OOOO0OOO00O0OOO00 )#line:191
    if O00OOOO0OOOOO0O0O .status_code not in [204 ,200 ]:#line:192
        print (f"{colorama.Fore.RED}    [!] Failed to add reaction: {O00OOOO0OOOOO0O0O.status_code} - {O00OOOO0OOOOO0O0O.text}{colorama.Fore.RESET}")#line:193
def reaction_art ():#line:195
    try :#line:196
        with open ("token.txt",encoding ="utf-8")as O00OO0O000O0O00O0 :#line:197
            O0OO00OO0OOOOOO00 =[O0O000O0O00OOO0O0 .strip ()for O0O000O0O00OOO0O0 in O00OO0O000O0O00O0 .readlines ()if O0O000O0O00OOO0O0 .strip ()]#line:198
    except (FileNotFoundError ,KeyError ):#line:199
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:200
        return #line:201
    O000O0OO00O00O00O =input ("Server ID?: ").strip ()#line:203
    O00OO0OOO000O0O00 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:205
    if O00OO0OOO000O0O00 =='2':#line:206
        O00O0OOOO00000O00 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:207
        O0OO0O0OOOO00000O =[OOOOOOO0OO0O0O000 .strip ()for OOOOOOO0OO0O0O000 in O00O0OOOO00000O00 if OOOOOOO0OO0O0O000 .strip ()]#line:208
    else :#line:209
        O0OO0O0OOOO00000O =[]#line:210
        for OO00O0OO00O0O0OO0 in O0OO00OO0OOOOOO00 :#line:211
            try :#line:212
                O0OO0O0OOOO00000O .extend (fetch_channels (OO00O0OO00O0O0OO0 ,O000O0OO00O00O00O ))#line:213
            except Exception as OOOO000O00O0000O0 :#line:214
                print (f"[!] Failed to fetch channels for token. Error: {OOOO000O00O0000O0}")#line:215
                continue #line:216
    OOO0OOOO00OO00O0O =input ("Delay between reactions (in seconds)?: ").strip ()#line:218
    try :#line:220
        OOO0OOOO00OO00O0O =float (OOO0OOOO00OO00O0O )#line:221
        if OOO0OOOO00OO00O0O <0 :#line:222
            raise ValueError #line:223
    except ValueError :#line:224
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:225
        OOO0OOOO00OO00O0O =1.0 #line:226
    try :#line:228
        with open ("art.txt",encoding ="utf-8")as OOO00OOO00O0O00O0 :#line:229
            O00O0OO0O000O0OO0 =[OOO0OO000O0O0O000 .strip ()for OOO0OO000O0O0O000 in OOO00OOO00O0O00O0 .readlines ()if OOO0OO000O0O0O000 .strip ()]#line:230
    except (FileNotFoundError ,KeyError ):#line:231
        print (f"{colorama.Fore.RED}    [!] Error: art.txt file not found or empty!{colorama.Fore.RESET}")#line:232
        return #line:233
    except UnicodeDecodeError as OOOO000O00O0000O0 :#line:234
        print (f"{colorama.Fore.RED}    [!] Error decoding art.txt: {str(OOOO000O00O0000O0)}{colorama.Fore.RESET}")#line:235
        return #line:236
    if not O00O0OO0O000O0OO0 :#line:238
        print (f"{colorama.Fore.RED}    [!] No valid art provided in art.txt!{colorama.Fore.RESET}")#line:239
        return #line:240
    for OO00O0OO00O0O0OO0 in O0OO00OO0OOOOOO00 :#line:242
        for OOOO0O000O000O0OO in O0OO0O0OOOO00000O :#line:243
            try :#line:244
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {OOOO0O000O000O0OO}...{colorama.Fore.RESET}")#line:245
                O0OO0O0000O000O00 =fetch_messages (OO00O0OO00O0O0OO0 ,OOOO0O000O000O0OO ,limit =len (O00O0OO0O000O0OO0 ))#line:246
                if not O0OO0O0000O000O00 :#line:247
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:248
                    continue #line:249
                O0OOO00O0OOO0OO0O =O0OO0O0000O000O00 [:]#line:252
                for O0OOOO0O0OOOOOOOO ,OOO0OO0OO000OOO00 in enumerate (reversed (O0OOO00O0OOO0OO0O )):#line:253
                    O0OO000OOO0OO0000 =O00O0OO0O000O0OO0 [O0OOOO0O0OOOOOOOO %len (O00O0OO0O000O0OO0 )].split (',')#line:254
                    for OOO0O0O0OO0OOO0OO in O0OO000OOO0OO0000 :#line:255
                        reactionput (OO00O0OO00O0O0OO0 ,OOOO0O000O000O0OO ,OOO0OO0OO000OOO00 ['id'],OOO0O0O0OO0OOO0OO .strip ())#line:256
                        print (f"Adding reaction '{OOO0O0O0OO0OOO0OO.strip()}' to message {OOO0OO0OO000OOO00['id']} in channel {OOOO0O000O000O0OO}")#line:257
                        time .sleep (OOO0OOOO00OO00O0O )#line:258
            except Exception as OOOO000O00O0000O0 :#line:259
                print (f"[!] Error processing channel {OOOO0O000O000O0OO}. Error: {OOOO000O00O0000O0}")#line:260
                continue #line:261
    def O0OO000O0O0O0O000 (OO00O0O000000OO0O ):#line:265
        for OO0O0O0OOOO0OO0OO in O0OO0O0OOOO00000O :#line:266
            try :#line:267
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {OO0O0O0OOOO0OO0OO}...{colorama.Fore.RESET}")#line:268
                O0O0OOOO0000OOOO0 =fetch_messages (OO00O0O000000OO0O ,OO0O0O0OOOO0OO0OO ,limit =100 )#line:269
                if not O0O0OOOO0000OOOO0 :#line:270
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:271
                    continue #line:272
                for O0OOOOO0OO0O000OO in O0O0OOOO0000OOOO0 :#line:274
                    for O00O0OO0OOOO0OOOO in O0OO000OOO0OO0000 :#line:275
                        reactionput (OO00O0O000000OO0O ,OO0O0O0OOOO0OO0OO ,O0OOOOO0OO0O000OO ['id'],O00O0OO0OOOO0OOOO )#line:276
                        time .sleep (OOO0OOOO00OO00O0O )#line:277
            except Exception as OOO00OO0OOOOO0000 :#line:278
                print (f"[!] Error processing channel {OO0O0O0OOOO0OO0OO}. Error: {OOO00OO0OOOOO0000}")#line:279
                continue #line:280
    with concurrent .futures .ThreadPoolExecutor ()as O0O0O0O0000O0O000 :#line:282
        O0O000O00OO00OOO0 =[O0O0O0O0000O0O000 .submit (O0OO000O0O0O0O000 ,O000000OOO0O00OOO )for O000000OOO0O00OOO in O0OO00OO0OOOOOO00 ]#line:283
        concurrent .futures .wait (O0O000O00OO00OOO0 )#line:284
def update_group_ids ():#line:287
    try :#line:288
        with open ("token.txt")as OO0OOOOOO00OOO0OO :#line:289
            OO00OOOOOOOOOO00O =[O0OOO000O0O000O00 .strip ()for O0OOO000O0O000O00 in OO0OOOOOO00OOO0OO .readlines ()if O0OOO000O0O000O00 .strip ()]#line:290
        OO00O000O000OO0O0 =OO00OOOOOOOOOO00O [0 ]#line:291
    except (FileNotFoundError ,KeyError ):#line:292
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:293
        return #line:294
    OOO00OOOO0OO0OO00 ={"Authorization":OO00O000O000OO0O0 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:300
    OO000O0O00OOOOO00 =requests .get ('https://discord.com/api/v9/users/@me/channels',headers =OOO00OOOO0OO0OO00 )#line:302
    if OO000O0O00OOOOO00 .status_code ==200 :#line:303
        O000O0OO00O00000O =OO000O0O00OOOOO00 .json ()#line:304
        with open ("group_id.txt","w")as OO0000OO0O0OOO000 :#line:305
            for O0O0OOOO0OOO0O00O in O000O0OO00O00000O :#line:306
                if O0O0OOOO0OOO0O00O ['type']==3 :#line:307
                    OO0000OO0O0OOO000 .write (O0O0OOOO0OOO0O00O ['id']+'\n')#line:308
        print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Group IDs updated successfully.{colorama.Fore.RESET}")#line:309
    else :#line:310
        print (f"{colorama.Fore.LIGHTRED_EX}    [!] Failed to retrieve group IDs. HTTP Status Code: {OO000O0O00OOOOO00.status_code}{colorama.Fore.RESET}")#line:311
import requests #line:313
import requests #line:315
def fetch_channels (OOOO0OOO0OO0OO0O0 ,O0O0OOOOO0000OOOO ):#line:317
    try :#line:318
        O000OOOOOOOO0OO00 =requests .Session ()#line:319
        OO0O00O00OOO0OO0O =get_headers (OOOO0OOO0OO0OO0O0 )#line:320
        OOOOOOO00OOOOO0OO =O000OOOOOOOO0OO00 .get (f"https://discord.com/api/v9/guilds/{O0O0OOOOO0000OOOO}/channels",headers =OO0O00O00OOO0OO0O ,timeout =10 )#line:327
        if OOOOOOO00OOOOO0OO .status_code ==200 :#line:330
            try :#line:331
                O000OOO0O00O0OO00 =OOOOOOO00OOOOO0OO .json ()#line:332
                return [O0000OOOO00O0OO0O ['id']for O0000OOOO00O0OO0O in O000OOO0O00O0OO00 if O0000OOOO00O0OO0O .get ('type')==0 ]#line:333
            except ValueError :#line:334
                print ("[!] Error: Response was not valid JSON.")#line:335
                return []#line:336
        elif OOOOOOO00OOOOO0OO .status_code ==401 :#line:337
            print ("[!] Error: Unauthorized - check your token.")#line:338
        elif OOOOOOO00OOOOO0OO .status_code ==403 :#line:339
            print ("[!] Error: Forbidden - you lack permissions.")#line:340
        elif OOOOOOO00OOOOO0OO .status_code ==404 :#line:341
            print ("[!] Error: Server not found - check the server ID.")#line:342
        else :#line:343
            print (f"[!] Error: Unexpected status code {OOOOOOO00OOOOO0OO.status_code}.")#line:344
        return []#line:347
    except requests .exceptions .Timeout :#line:349
        print ("[!] Error: Request timed out. Check your connection or try again later.")#line:350
        return []#line:351
    except requests .exceptions .RequestException as O0O0O00OOO0OO000O :#line:352
        print (f"[!] Error: An error occurred while fetching channels: {O0O0O00OOO0OO000O}")#line:353
        return []#line:354
def extract_uids_from_messages (OO00O00O0O00O0O0O ):#line:360
    OO0000O0O00000000 =set ()#line:361
    for O0OOO0O0OO0O0000O in OO00O00O0O00O0O0O :#line:362
        OO0000O0O00000000 .add (O0OOO0O0OO0O0000O ['author']['id'])#line:363
    return list (OO0000O0O00000000 )#line:364
def send_message_with_mention (OOOOOOOOOO000O00O ,O0O00OO0OO0OOOO0O ,OO000OO0OO000O00O ,OO0O000OOOOO000O0 ):#line:366
    O0O0O0OOOOOO00000 =get_session ()#line:367
    O00O0O0OO0000OOOO =get_headers (OOOOOOOOOO000O00O )#line:368
    if OO0O000OOOOO000O0 :#line:370
        O0OO0000O00OO00O0 =random .choice (OO0O000OOOOO000O0 )#line:371
        OO000OO0OO000O00O +=f" <@{O0OO0000O00OO00O0}>"#line:372
    O00O0O0O0O00OOO00 =O0O0O0OOOOOO00000 .post (f"https://discord.com/api/v9/channels/{O0O00OO0OO0OOOO0O}/messages",headers =O00O0O0OO0000OOOO ,json ={"content":OO000OO0OO000O00O })#line:378
    if O00O0O0O0O00OOO00 .status_code in [200 ,201 ]:#line:379
        print (f"[+] Message sent to channel {O0O00OO0OO0OOOO0O}")#line:380
    elif O00O0O0O0O00OOO00 .status_code ==429 :#line:381
        print ("[-] Rate limited. Please wait before retrying.")#line:382
        O00O0000O000O0O0O =O00O0O0O0O00OOO00 .json ().get ("retry_after",1 )#line:383
        time .sleep (O00O0000O000O0O0O )#line:384
    else :#line:385
        print (f"[!] Error occurred: {O00O0O0O0O00OOO00.status_code}")#line:386
def send_messages_with_mentions ():#line:387
    try :#line:388
        with open ("token.txt")as OOOOOOO000O0OO00O :#line:389
            O0O0O000O0OOOOOO0 =[OOO00OOOO0O000000 .strip ()for OOO00OOOO0O000000 in OOOOOOO000O0OO00O .readlines ()if OOO00OOOO0O000000 .strip ()]#line:390
    except (FileNotFoundError ,KeyError ):#line:391
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:392
        return #line:393
    O00O00OO00O00O0O0 =input ("Server ID?: ").strip ()#line:395
    O0OOO0OO0O000OOOO =input ("Delay between messages (in seconds)?: ").strip ()#line:396
    OOOOOOOOOO000O0O0 =input ("Number of messages to send?: ").strip ()#line:397
    OO0000O00OOO0O000 =input ("Message content?: ").strip ()#line:398
    OOOO0OO0OO000000O =input ("Blacklist User IDs (comma-separated)?: ").strip ().split (',')#line:399
    OOOO0OO0OO000000O =[O00OOO0O0O00000O0 .strip ()for O00OOO0O0O00000O0 in OOOO0OO0OO000000O if O00OOO0O0O00000O0 .strip ()]#line:400
    try :#line:402
        O0OOO0OO0O000OOOO =float (O0OOO0OO0O000OOOO )#line:403
        if O0OOO0OO0O000OOOO <0 :#line:404
            raise ValueError #line:405
    except ValueError :#line:406
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:407
        O0OOO0OO0O000OOOO =1.0 #line:408
    try :#line:410
        OOOOOOOOOO000O0O0 =int (OOOOOOOOOO000O0O0 )#line:411
        if OOOOOOOOOO000O0O0 <=0 :#line:412
            raise ValueError #line:413
    except ValueError :#line:414
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:415
        OOOOOOOOOO000O0O0 =1 #line:416
    OO000OO0OO0OOO000 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:418
    if OO000OO0OO0OOO000 =='2':#line:419
        OOOOO0OO00O0O0OOO =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:420
        OOOOO0OO00O0O0OOO =[OO0O000O00OOOOO0O .strip ()for OO0O000O00OOOOO0O in OOOOO0OO00O0O0OOO if OO0O000O00OOOOO0O .strip ()]#line:421
    else :#line:422
        OOOOO0OO00O0O0OOO =[]#line:423
    OO00OO00OOO00OOO0 =set ()#line:425
    for O0OOOOOO0OO00OOOO in O0O0O000O0OOOOOO0 :#line:426
        O000O00O000000OOO =fetch_channels (O0OOOOOO0OO00OOOO ,O00O00OO00O00O0O0 )#line:427
        for OO00OO000OOOO00O0 in O000O00O000000OOO :#line:428
            OOOO0O0OO00O0OOO0 =fetch_messages (O0OOOOOO0OO00OOOO ,OO00OO000OOOO00O0 ,limit =100 )#line:429
            OO00O0OOO000O0000 =extract_uids_from_messages (OOOO0O0OO00O0OOO0 )#line:430
            OO00OO00OOO00OOO0 .update (OO00O0OOO000O0000 )#line:431
    OO00OO00OOO00OOO0 =list (set (OO00OO00OOO00OOO0 )-set (OOOO0OO0OO000000O ))#line:434
    for _O0O000OOOOOO0OO00 in range (OOOOOOOOOO000O0O0 ):#line:436
        for O0OOOOOO0OO00OOOO in O0O0O000O0OOOOOO0 :#line:437
            if OOOOO0OO00O0O0OOO :#line:438
                O000O00O000000OOO =OOOOO0OO00O0O0OOO #line:439
            for OO00OO000OOOO00O0 in O000O00O000000OOO :#line:440
                send_message_with_mention (O0OOOOOO0OO00OOOO ,OO00OO000OOOO00O0 ,OO0000O00OOO0O000 ,OO00OO00OOO00OOO0 )#line:441
                time .sleep (O0OOO0OO0O000OOOO )#line:442
def join_discord_invite ():#line:447
    try :#line:448
        with open ("token.txt")as O0O0O0000000O0OOO :#line:449
            O0OO0OO0O0O0OOO0O =[O00O00OOOO000OOO0 .strip ()for O00O00OOOO000OOO0 in O0O0O0000000O0OOO .readlines ()if O00O00OOOO000OOO0 .strip ()]#line:450
    except (FileNotFoundError ,KeyError ):#line:451
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:452
        return #line:453
    O0O0O0O0O0O00OOOO =input ("Invite Code?: discord.gg/").strip ()#line:455
    for O0OO0000000OOO0O0 in O0OO0OO0O0O0OOO0O :#line:458
        joiner (O0OO0000000OOO0O0 ,O0O0O0O0O0O00OOOO )#line:459
import json ,time ,base64 ,random ,requests #line:461
def cookieset (O00O0O0OOO0OOO0O0 ):#line:463
    OOO0OO00O0OO000OO =O00O0O0OOO0OOO0O0 .get ("https://discord.com/app")#line:464
    return OOO0OO00O0OO000OO .cookies .get_dict ()#line:465
def generatexspandua (OOOO0O0O000O0OOO0 ):#line:467
    OOOOOOOOOO0O0OO0O =["Android","Windows","Macintosh"]#line:468
    OOOO000O0000OOOO0 =random .choice (OOOOOOOOOO0O0OO0O )#line:469
    if OOOO000O0000OOOO0 =="Macintosh":#line:470
        O0000O0O0OOO0OO0O =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:471
        OOOO0OOOOO0O0000O ="Macintosh; Intel Mac OS X "+O0000O0O0OOO0OO0O #line:472
        OOOOOOOOOO00OO0O0 ="x86_64"#line:473
    elif OOOO000O0000OOOO0 =="Windows":#line:474
        O0000O0O0OOO0OO0O =f'{random.choice([6.0, 10.0, 11.0])}'#line:475
        OOOO0OOOOO0O0000O ="Windows NT "+O0000O0O0OOO0OO0O +" Win64; x64"#line:476
        OOOOOOOOOO00OO0O0 ="x86_64"#line:477
    else :#line:478
        O0000O0O0OOO0OO0O ="13"#line:479
        OOOO0OOOOO0O0000O =f"Linux; Android 13; Pixel 6a"#line:480
        OOOOOOOOOO00OO0O0 ="aarch64"#line:481
    OOO0O00000OOOO0O0 ={"os":OOOO000O0000OOOO0 ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":O0000O0O0OOO0OO0O ,"os_arch":OOOOOOOOOO00OO0O0 ,"system_locale":"ja-JP","client_build_number":OOOO0O0O000O0OOO0 ,"client_event_source":None ,"design_id":0 }#line:494
    O0O000OO00O0O0OOO =f"Mozilla/5.0 ({OOOO0OOOOO0O0000O}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:495
    return base64 .b64encode (json .dumps (OOO0O00000OOOO0O0 ,separators =(',',':')).encode ()).decode (),O0O000OO00O0O0OOO #line:496
def joiner (OOOO0O0O0OOOO0O0O ,OO0O00OO0O000O0O0 ,OOO0O0O000OO0O00O ):#line:498
    OO0O00OOO00000000 =cookieset (OOO0O0O000OO0O00O )#line:499
    OO0O00OOO00000000 ["locale"]="ja-JP"#line:500
    OO0OOOOO00O00OO00 =201211 #line:501
    O0O0O00OOOO0O00O0 ,O000OO0OOO00OO0OO =generatexspandua (OO0OOOOO00O00OO00 )#line:502
    OO00O000OO0OO0000 ={"Authorization":OOOO0O0O0OOOO0O0O ,"accept":"*/*","accept-language":"ja-JP","connection":"keep-alive","DNT":"1","origin":"https://discord.com","sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","referer":"https://discord.com/channels/@me","TE":"Trailers","user-agent":O000OO0OOO00OO0OO ,"X-Super-Properties":O0O0O00OOOO0O00O0 ,}#line:517
    O00OO00O0O00O0O0O =OOO0O0O000OO0O00O .post ("https://discord.com/api/v9/invites/"+OO0O00OO0O000O0O0 ,headers =OO00O000OO0OO0000 ,json ={},cookies =OO0O00OOO00000000 )#line:518
    if O00OO00O0O00O0O0O .status_code ==200 :#line:519
        print ("[+] join this server "+OOOO0O0O0OOOO0O0O )#line:520
        if "show_verification_form"in O00OO00O0O00O0O0O .json ():#line:521
            bypass (OOOO0O0O0OOOO0O0O ,O00OO00O0O00O0O0O .json ()["guild"]["id"],OOO0O0O000OO0O00O ,OO00O000OO0OO0000 )#line:522
        return #line:523
    elif "captcha_key"in O00OO00O0O00O0O0O .text and O00OO00O0O00O0O0O .status_code ==400 :#line:524
        print ("[!] Hcaptcha protect"+OOOO0O0O0OOOO0O0O )#line:525
        return #line:526
    elif O00OO00O0O00O0O0O .status_code ==401 :#line:527
        print ("[×] token is dead"+OOOO0O0O0OOOO0O0O )#line:528
        return #line:529
    elif O00OO00O0O00O0O0O .status_code ==403 :#line:530
        print ("[!] 403 banned "+OOOO0O0O0OOOO0O0O )#line:531
        return #line:532
    elif O00OO00O0O00O0O0O .status_code ==429 :#line:533
        O0O000OOOOOOOOO00 =O00OO00O0O00O0O0O .json ().get ("retry_after",1 )#line:534
        print (f"[!] 429 rate limit. Retrying after {O0O000OOOOOOOOO00} seconds.")#line:535
        time .sleep (O0O000OOOOOOOOO00 )#line:536
        return #line:537
    else :#line:538
        print ("[!] error "+OOOO0O0O0OOOO0O0O )#line:539
        return #line:540
def update_group_ids ():#line:542
    OO000OO00O00O00OO =input ("Invite Code?: ").strip ()#line:543
    try :#line:544
        with open ("token.txt")as O00OOOO0O00O0OOOO :#line:545
            OOOOO0OOOOO0O0O00 =[OOO0OOO0OO00OOOO0 .strip ()for OOO0OOO0OO00OOOO0 in O00OOOO0O00O0OOOO .readlines ()if OOO0OOO0OO00OOOO0 .strip ()]#line:546
    except (FileNotFoundError ,KeyError ):#line:547
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:548
        return #line:549
    OO000OO0OOO0OOO00 =requests .Session ()#line:551
    for OOOOOOO000OOO00O0 in OOOOO0OOOOO0O0O00 :#line:552
        joiner (OOOOOOO000OOO00O0 ,OO000OO00O00O00OO ,OO000OO0OOO0OOO00 )#line:553
        time .sleep (2 )#line:554
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:556
def bypass (O0OO00O0O00OO0O0O ,O00O000O0OOO00OO0 ,O0OO00O000O0O0O0O ,O0O0OO0OOO00OO0O0 ):#line:559
    try :#line:560
        O0O00OO0OO0OO0OOO =O0OO00O000O0O0O0O .get (f"https://discord.com/api/v9/guilds/{O00O000O0OOO00OO0}/member-verification?with_guild=false",headers =O0O0OO0OOO00OO0O0 ).json ()#line:561
        O0O000O00O0000O0O =O0OO00O000O0O0O0O .put (f"https://discord.com/api/v9/guilds/{O00O000O0OOO00OO0}/requests/@me",headers =O0O0OO0OOO00OO0O0 ,json =O0O00OO0OO0OO0OOO )#line:562
        if O0O000O00O0000O0O .status_code ==201 :#line:563
            print (f"[+] MemberscreeningBypassed {O0OO00O0O00OO0O0O}")#line:564
            return #line:565
        else :#line:566
            print (f"[!] Bypassが出来ませんでした {O0OO00O0O00OO0O0O}")#line:567
            return #line:568
    except Exception as OOOO00OO00000OOOO :#line:569
        print (f"[!] エラーが発生しました。{OOOO00OO00000OOOO}")#line:570
session =requests .Session ()#line:572
def reactionput (OO00OO0000OO00O00 ,OOO00O0O00OOOO00O ,OOOOO00O0O00O000O ,OO00OO000O0O0OO0O ,proxy =None ):#line:575
    O000O00OOO0O0O000 =get_session (proxy )#line:576
    OOOO0O00OOOO0OOO0 =get_headers (O000O00OOO0O0O000 )#line:577
    OOOO0O00OOOO0OOO0 ["Authorization"]=OO00OO0000OO00O00 #line:578
    OO00OO000O0O0OO0O =requests .utils .quote (OO00OO000O0O0OO0O )#line:580
    OOO0OO00O0O00OOOO =O000O00OOO0O0O000 .put (f"https://discord.com/api/v9/channels/{OOO00O0O00OOOO00O}/messages/{OOOOO00O0O00O000O}/reactions/{OO00OO000O0O0OO0O}/%40me?location=Message&type=0",headers =OOOO0O00OOOO0OOO0 )#line:584
    if OOO0OO00O0O00OOOO .status_code in [200 ,204 ]:#line:585
        print (f"[+] Reaction '{OO00OO000O0O0OO0O}' added successfully to message {OOOOO00O0O00O000O}")#line:586
    elif OOO0OO00O0O00OOOO .status_code ==429 :#line:587
        print ("[-] Rate limited. Please wait before retrying.")#line:588
        O00OOOO000O0O0OO0 =OOO0OO00O0O00OOOO .json ().get ("retry_after",1 )#line:589
        time .sleep (O00OOOO000O0O0OO0 )#line:590
    elif OOO0OO00O0O00OOOO .status_code ==401 :#line:591
        print ("[-] Invalid or expired token.")#line:592
    else :#line:593
        print (f"[!] Error occurred: {OOO0OO00O0O00OOOO.status_code}")#line:594
def generatexspandua (OOO0OO0O000OO00O0 ):#line:597
  O0O000OOO0OOOOO0O =["Android","Windows","Macintosh"]#line:598
  O0O0O0OOOOOO0O0O0 =random .choice (O0O000OOO0OOOOO0O )#line:599
  if O0O0O0OOOOOO0O0O0 =="Macintosh":#line:600
    OOO000O0OO000OO0O =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:601
    OOOOO00O0000O00O0 ="Macintosh; Intel Mac OS X "+OOO000O0OO000OO0O #line:602
    OO0000O0OOO0OOO00 ="x86_64"#line:603
  if O0O0O0OOOOOO0O0O0 =="Windows":#line:604
    OOO000O0OO000OO0O =f'{random.choice([6.0,10.0,11.0])}'#line:605
    OOOOO00O0000O00O0 ="Windows NT "+OOO000O0OO000OO0O +" Win64; x64"#line:606
    OO0000O0OOO0OOO00 ="x86_64"#line:607
  if O0O0O0OOOOOO0O0O0 =="Android":#line:608
    OOO000O0OO000OO0O ="13"#line:609
    OOOOO00O0000O00O0 =f"Linux; Android 13; Pixel 6a"#line:610
    OO0000O0OOO0OOO00 ="aarch64"#line:611
  OO0O000O0OO000O00 ={"os":O0O0O0OOOOOO0O0O0 ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":OOO000O0OO000OO0O ,"os_arch":OO0000O0OOO0OOO00 ,"system_locale":"ja-JP","client_build_number":OOO0OO0O000OO00O0 ,"client_event_source":None ,"design_id":0 }#line:612
  O000O00O0000O0000 =f"Mozilla/5.0 ({OOOOO00O0000O00O0}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:613
  return base64 .b64encode (json .dumps (OO0O000O0OO000O00 ,separators =(',',':')).encode ()).decode (),O000O00O0000O0000 #line:614
import base64 #line:616
def nickchanger ():#line:619
    try :#line:620
        with open ("token.txt")as OOO0O00O0OO0000O0 :#line:621
            O0O00000000OOO000 =[OOO0O00OOOO0O00OO .strip ()for OOO0O00OOOO0O00OO in OOO0O00O0OO0000O0 .readlines ()if OOO0O00OOOO0O00OO .strip ()]#line:622
    except (FileNotFoundError ,KeyError ):#line:623
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:624
        return #line:625
    OOO0O000OO00OOO00 =input ("Server ID?: ").strip ()#line:627
    O00O0O00O000O0OOO =input ("Nickname?: ").strip ()#line:628
    OOO0OOO0OOOO00000 =input ("Delay (in seconds)?: ").strip ()#line:629
    try :#line:631
        OOO0OOO0OOOO00000 =float (OOO0OOO0OOOO00000 )#line:632
        if OOO0OOO0OOOO00000 <0 :#line:633
            raise ValueError #line:634
    except ValueError :#line:635
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:636
        OOO0OOO0OOOO00000 =1.0 #line:637
    for OOO0000OO000OOO0O in O0O00000000OOO000 :#line:639
        O00OOOOO0O000O00O ={"Authorization":OOO0000OO000OOO0O ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:644
        OO0O00OOOO00O0OOO ={"nick":O00O0O00O000O0OOO }#line:645
        O00OO0OO00O00000O =requests .patch (f"https://discord.com/api/v9/guilds/{OOO0O000OO00OOO00}/members/@me",headers =O00OOOOO0O000O00O ,json =OO0O00OOOO00O0OOO )#line:646
        if O00OO0OO00O00000O .status_code ==200 :#line:648
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Nickname changed to '{O00O0O00O000O0OOO}' successfully for token {OOO0000OO000OOO0O}.{colorama.Fore.RESET}")#line:649
        elif O00OO0OO00O00000O .status_code ==429 :#line:650
            print (f"{colorama.Fore.RED}    [!] Rate limited. Please wait before retrying for token {OOO0000OO000OOO0O}.{colorama.Fore.RESET}")#line:651
            O0000000O00O000OO =O00OO0OO00O00000O .json ().get ("retry_after",1 )#line:652
            time .sleep (O0000000O00O000OO )#line:653
        else :#line:654
            print (f"{colorama.Fore.RED}    [!] Error occurred: {O00OO0OO00O00000O.status_code} for token {OOO0000OO000OOO0O}.{colorama.Fore.RESET}")#line:655
        time .sleep (OOO0OOO0OOOO00000 )#line:657
import json ,websocket ,threading ,tls_client ,random ,time #line:661
session =tls_client .Session (client_identifier ="chrome112",random_tls_extension_order =True )#line:663
class Utils :#line:665
    @staticmethod #line:666
    def rangeCorrector (OO000OOO00OO0OO00 ):#line:667
        if [0 ,99 ]not in OO000OOO00OO0OO00 :#line:668
            OO000OOO00OO0OO00 .insert (0 ,[0 ,99 ])#line:669
        return OO000OOO00OO0OO00 #line:670
    @staticmethod #line:672
    def getRanges (OO0O0O000O000O00O ,O0OO0O00OO0O00000 ,O00OOOO0O0OO0OOO0 ):#line:673
        OO0O0000O0OO0O0OO =int (OO0O0O000O000O00O *O0OO0O00OO0O00000 )#line:674
        OO00O000000O0O0O0 =[[OO0O0000O0OO0O0OO ,OO0O0000O0OO0O0OO +99 ]]#line:675
        if O00OOOO0O0OO0OOO0 >OO0O0000O0OO0O0OO +99 :#line:676
            OO00O000000O0O0O0 .append ([OO0O0000O0OO0O0OO +100 ,OO0O0000O0OO0O0OO +199 ])#line:677
        return Utils .rangeCorrector (OO00O000000O0O0O0 )#line:678
    @staticmethod #line:680
    def parseGuildMemberListUpdate (OO00000000O0O0000 ):#line:681
        O0O0O00O0OO00O0O0 ={"online_count":OO00000000O0O0000 ["d"]["online_count"],"member_count":OO00000000O0O0000 ["d"]["member_count"],"id":OO00000000O0O0000 ["d"]["id"],"guild_id":OO00000000O0O0000 ["d"]["guild_id"],"hoisted_roles":OO00000000O0O0000 ["d"]["groups"],"types":[],"locations":[],"updates":[],}#line:691
        for O0OOO000OO000O0O0 in OO00000000O0O0000 ["d"]["ops"]:#line:693
            O0O0O00O0OO00O0O0 ["types"].append (O0OOO000OO000O0O0 ["op"])#line:694
            if O0OOO000OO000O0O0 ["op"]in ("SYNC","INVALIDATE"):#line:695
                O0O0O00O0OO00O0O0 ["locations"].append (O0OOO000OO000O0O0 ["range"])#line:696
                if O0OOO000OO000O0O0 ["op"]=="SYNC":#line:697
                    O0O0O00O0OO00O0O0 ["updates"].append (O0OOO000OO000O0O0 ["items"])#line:698
                else :#line:699
                    O0O0O00O0OO00O0O0 ["updates"].append ([])#line:700
            elif O0OOO000OO000O0O0 ["op"]in ("INSERT","UPDATE","DELETE"):#line:701
                O0O0O00O0OO00O0O0 ["locations"].append (O0OOO000OO000O0O0 ["index"])#line:702
                if O0OOO000OO000O0O0 ["op"]=="DELETE":#line:703
                    O0O0O00O0OO00O0O0 ["updates"].append ([])#line:704
                else :#line:705
                    O0O0O00O0OO00O0O0 ["updates"].append (O0OOO000OO000O0O0 ["item"])#line:706
        return O0O0O00O0OO00O0O0 #line:707
class DiscordSocket (websocket .WebSocketApp ):#line:709
    def __init__ (O000O0OOO0OOO000O ,OOO00000OO00000O0 ,OOO000O0O0000O0O0 ,O0OOO00OOO0O0O00O ):#line:710
        O000O0OOO0OOO000O .token =OOO00000OO00000O0 #line:711
        O000O0OOO0OOO000O .guild_id =OOO000O0O0000O0O0 #line:712
        O000O0OOO0OOO000O .channel_id =O0OOO00OOO0O0O00O #line:713
        O000O0OOO0OOO000O .socket_headers ={"Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","Cache-Control":"no-cache","Pragma":"no-cache","Sec-WebSocket-Extensions":"permessage-deflate; client_max_window_bits","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",}#line:721
        super ().__init__ ("wss://gateway.discord.gg/?encoding=json&v=9",header =O000O0OOO0OOO000O .socket_headers ,on_open =lambda O0OOOO0OOOOOO0OO0 :O000O0OOO0OOO000O .sock_open (O0OOOO0OOOOOO0OO0 ),on_message =lambda O0OOO00O0000O0O00 ,O000OO0O0OOOOOOOO :O000O0OOO0OOO000O .sock_message (O0OOO00O0000O0O00 ,O000OO0O0OOOOOOOO ),on_close =lambda O0OOOO0OOO00O0OO0 ,O0O0O000000000OOO ,OOO00OOOOOO0OO000 :O000O0OOO0OOO000O .sock_close (O0OOOO0OOO00O0OO0 ,O0O0O000000000OOO ,OOO00OOOOOO0OO000 ),)#line:730
        O000O0OOO0OOO000O .endScraping =False #line:732
        O000O0OOO0OOO000O .guilds ={}#line:733
        O000O0OOO0OOO000O .members ={}#line:734
        O000O0OOO0OOO000O .ranges =[[0 ,0 ]]#line:735
        O000O0OOO0OOO000O .lastRange =0 #line:736
        O000O0OOO0OOO000O .packets_recv =0 #line:737
    def run (OO00OO000O0000OOO ):#line:739
        OO00OO000O0000OOO .run_forever ()#line:740
        return OO00OO000O0000OOO .members #line:741
    def scrapeUsers (O0OO000O00O0O00OO ):#line:743
        if not O0OO000O00O0O00OO .endScraping :#line:744
            O0OO000O00O0O00OO .send ('{"op":14,"d":{"guild_id":"'+O0OO000O00O0O00OO .guild_id +'","typing":true,"activities":true,"threads":true,"channels":{"'+O0OO000O00O0O00OO .channel_id +'":'+json .dumps (O0OO000O00O0O00OO .ranges )+"}}}")#line:753
    def sock_open (O00O0O00OO0O0OO0O ,OO00OO0OOOOO0O0OO ):#line:755
        O00O0O00OO0O0OO0O .send ('{"op":2,"d":{"token":"'+O00O0O00OO0O0OO0O .token +'","capabilities":125,"properties":{"os":"Windows NT","browser":"Chrome","device":"","system_locale":"it-IT","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36","browser_version":"119.0","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":103981,"client_event_source":null},"presence":{"status":"online","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}')#line:760
    def heartbeatThread (O000OOO0O0OO0OO0O ,OO0OO0O0OO0O0000O ):#line:762
        try :#line:763
            while True :#line:764
                O000OOO0O0OO0OO0O .send ('{"op":1,"d":'+str (O000OOO0O0OO0OO0O .packets_recv )+"}")#line:765
                time .sleep (OO0OO0O0OO0O0000O )#line:766
        except Exception as OOO0O0OO0000OO00O :#line:767
            pass #line:768
    def sock_message (O00OO0OOO0O00OO0O ,OOO000O0OOO00OOOO ,O0000O0O0OO0O0OOO ):#line:770
        OOO0OO000O0O0OO00 =json .loads (O0000O0O0OO0O0OOO )#line:771
        if OOO0OO000O0O0OO00 is None :#line:772
            return #line:773
        if OOO0OO000O0O0OO00 ["op"]!=11 :#line:774
            O00OO0OOO0O00OO0O .packets_recv +=1 #line:775
        if OOO0OO000O0O0OO00 ["op"]==10 :#line:776
            threading .Thread (target =O00OO0OOO0O00OO0O .heartbeatThread ,args =(OOO0OO000O0O0OO00 ["d"]["heartbeat_interval"]/1000 ,),daemon =True ,).start ()#line:781
        if OOO0OO000O0O0OO00 ["t"]=="READY":#line:782
            for OOO00O000O00O0O00 in OOO0OO000O0O0OO00 ["d"]["guilds"]:#line:783
                O00OO0OOO0O00OO0O .guilds [OOO00O000O00O0O00 ["id"]]={"member_count":OOO00O000O00O0O00 ["member_count"]}#line:784
        if OOO0OO000O0O0OO00 ["t"]=="READY_SUPPLEMENTAL":#line:785
            O00OO0OOO0O00OO0O .ranges =Utils .getRanges (0 ,100 ,O00OO0OOO0O00OO0O .guilds [O00OO0OOO0O00OO0O .guild_id ]["member_count"])#line:788
            O00OO0OOO0O00OO0O .scrapeUsers ()#line:789
        elif OOO0OO000O0O0OO00 ["t"]=="GUILD_MEMBER_LIST_UPDATE":#line:790
            OO0000000OO00OOOO =Utils .parseGuildMemberListUpdate (OOO0OO000O0O0OO00 )#line:791
            if OO0000000OO00OOOO ["guild_id"]==O00OO0OOO0O00OO0O .guild_id and ("SYNC"in OO0000000OO00OOOO ["types"]or "UPDATE"in OO0000000OO00OOOO ["types"]):#line:795
                for O0OO00000O0OOO0OO ,O00OO00O000OO0O00 in enumerate (OO0000000OO00OOOO ["types"]):#line:796
                    if O00OO00O000OO0O00 =="SYNC":#line:797
                        if len (OO0000000OO00OOOO ["updates"][O0OO00000O0OOO0OO ])==0 :#line:798
                            O00OO0OOO0O00OO0O .endScraping =True #line:799
                            break #line:800
                        for O00OOO00OO00OOO0O in OO0000000OO00OOOO ["updates"][O0OO00000O0OOO0OO ]:#line:802
                            if "member"in O00OOO00OO00OOO0O :#line:803
                                OOOOOOO0O000O00OO =O00OOO00OO00OOO0O ["member"]#line:804
                                O00OO000OO0O0OOOO ={"tag":OOOOOOO0O000O00OO ["user"]["username"]+"#"+OOOOOOO0O000O00OO ["user"]["discriminator"],"id":OOOOOOO0O000O00OO ["user"]["id"],}#line:810
                                if not OOOOOOO0O000O00OO ["user"].get ("bot"):#line:811
                                    O00OO0OOO0O00OO0O .members [OOOOOOO0O000O00OO ["user"]["id"]]=O00OO000OO0O0OOOO #line:812
                    elif O00OO00O000OO0O00 =="UPDATE":#line:814
                        for O00OOO00OO00OOO0O in OO0000000OO00OOOO ["updates"][O0OO00000O0OOO0OO ]:#line:815
                            if "member"in O00OOO00OO00OOO0O :#line:816
                                OOOOOOO0O000O00OO =O00OOO00OO00OOO0O ["member"]#line:817
                                O00OO000OO0O0OOOO ={"tag":OOOOOOO0O000O00OO ["user"]["username"]+"#"+OOOOOOO0O000O00OO ["user"]["discriminator"],"id":OOOOOOO0O000O00OO ["user"]["id"],}#line:823
                                if not OOOOOOO0O000O00OO ["user"].get ("bot"):#line:824
                                    O00OO0OOO0O00OO0O .members [OOOOOOO0O000O00OO ["user"]["id"]]=O00OO000OO0O0OOOO #line:825
                    O00OO0OOO0O00OO0O .lastRange +=1 #line:827
                    O00OO0OOO0O00OO0O .ranges =Utils .getRanges (O00OO0OOO0O00OO0O .lastRange ,100 ,O00OO0OOO0O00OO0O .guilds [O00OO0OOO0O00OO0O .guild_id ]["member_count"])#line:830
                    time .sleep (0.45 )#line:831
                    O00OO0OOO0O00OO0O .scrapeUsers ()#line:832
            if O00OO0OOO0O00OO0O .endScraping :#line:834
                O00OO0OOO0O00OO0O .close ()#line:835
    def sock_close (OO0000OOOO0O0O000 ,O00OO0OOOOO00O0OO ,O00O00OOO00O0O000 ,O000O000O0OOOOO00 ):#line:837
        pass #line:838
def scrape (O0O000OOO0OOOO0OO ,O0000000O00O0000O ,O000O0OO000O0OOOO ):#line:840
    OOO00OO0O0O00O0O0 =DiscordSocket (O0O000OOO0OOOO0OO ,O0000000O00O0000O ,O000O0OO000O0OOOO )#line:841
    return OOO00OO0O0O00O0O0 .run ()#line:842
def member_scrape (O000OO0000O00OO0O ,O0O00O0O0O0OOOO0O ,O000000O0OO0O0O0O ):#line:844
    OO000O0O000O00OO0 =[]#line:845
    for OO00O0O0OO000O00O in O000OO0000O00OO0O :#line:846
        OO0000OOOOOO00O00 ={"Authorization":OO00O0O0OO000O00O ,"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}#line:847
        OO0OOOO00OO0O0OOO =session .get (f"https://canary.discord.com/api/v9/guilds/{O0O00O0O0O0OOOO0O}",headers =OO0000OOOOOO00O00 )#line:848
        if OO0OOOO00OO0O0OOO .status_code ==200 :#line:849
            OO000O0O000O00OO0 .append (OO00O0O0OO000O00O )#line:850
            break #line:851
    if not OO000O0O000O00OO0 :#line:852
        print ("missing access")#line:853
    OO00O0O0OO000O00O =random .choice (OO000O0O000O00OO0 )#line:855
    OOO0O00OO0OO0OO00 =scrape (OO00O0O0OO000O00O ,O0O00O0O0O0OOOO0O ,O000000O0OO0O0O0O )#line:856
    OO0OOO00OO00OOOOO =[f"<@{O000O0000O0O0000O}>"for O000O0000O0O0000O in [int (O0O0OOOOOOOO0OOO0 )for O0O0OOOOOOOO0OOO0 in OOO0O00OO0OO0OO00 .keys ()]]#line:857
    print (f"[SUCCESS] {len(OO0OOO00OO00OOOOO)} scraped members")#line:858
    return OO0OOO00OO00OOOOO #line:859
def spammer_menu ():#line:861
    try :#line:862
        with open ("token.txt")as O0000000O0O000OO0 :#line:863
            O000OOO0OO0OO0OO0 =[O0OOOOOOOO0O0OOOO .strip ()for O0OOOOOOOO0O0OOOO in O0000000O0O000OO0 .readlines ()if O0OOOOOOOO0O0OOOO .strip ()]#line:864
    except (FileNotFoundError ,KeyError ):#line:865
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:866
        return #line:867
    OOO0OOO0O0O00O000 =input ("Server ID?: ").strip ()#line:869
    OO0000O00OO0OO00O =input ("Message?: ").strip ()#line:870
    OO0O0O000OO0O0O0O =input ("Random mention (True/False)?: ").strip ().lower ()=='true'#line:871
    O0OOO0O0OOOOOO000 =input ("Delay between messages (in seconds)?: ").strip ()#line:872
    OOOOOOO0O000OOOOO =input ("Number of messages to send?: ").strip ()#line:873
    OO00000O00O000000 =input ("Blacklist User IDs (comma-separated) (Leave blank to skip)?: ").strip ().split (',')#line:874
    OO00000O00O000000 =[f"<@{O0000O000O00OO000.strip()}>"for O0000O000O00OO000 in OO00000O00O000000 if O0000O000O00OO000 .strip ()]#line:875
    try :#line:877
        O0OOO0O0OOOOOO000 =float (O0OOO0O0OOOOOO000 )#line:878
        if O0OOO0O0OOOOOO000 <0 :#line:879
            raise ValueError #line:880
    except ValueError :#line:881
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:882
        O0OOO0O0OOOOOO000 =1.0 #line:883
    try :#line:885
        OOOOOOO0O000OOOOO =int (OOOOOOO0O000OOOOO )#line:886
        if OOOOOOO0O000OOOOO <=0 :#line:887
            raise ValueError #line:888
    except ValueError :#line:889
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:890
        OOOOOOO0O000OOOOO =1 #line:891
    O00O0000OOOOO0OOO =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:893
    if O00O0000OOOOO0OOO =='2':#line:894
        O0OO00O0OO00O000O =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:895
        O0OO00O0OO00O000O =[OO0O000OO0O000000 .strip ()for OO0O000OO0O000000 in O0OO00O0OO00O000O if OO0O000OO0O000000 .strip ()]#line:896
    else :#line:897
        O0OO00O0OO00O000O =fetch_channels (O000OOO0OO0OO0OO0 [0 ],OOO0OOO0O0O00O000 )#line:898
    O0OOO00OO00000OO0 =None #line:900
    spammer (O000OOO0OO0OO0OO0 ,OOO0OOO0O0O00O000 ,O0OO00O0OO00O000O ,OO0000O00OO0OO00O ,OO0O0O000OO0O0O0O ,OO00000O00O000000 ,O0OOO00OO00000OO0 ,OOOOOOO0O000OOOOO )#line:902
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:904
def spammer (OOO0O00OO00OOOOOO ,OOOOOO0OOOOO00OO0 ,O0OO00000OO0OOO00 ,OOO0OOOOO00OO0O0O ,O0O0OOOO000OO00O0 ,OO0000O00O00OO00O ,O00OOOO000OO00O00 ,OO000O0000OOOO0O0 ):#line:906
    O0OO00OOO0O00OOOO =get_session (O00OOOO000OO00O00 )#line:907
    O0O0OOO0O0000000O =0 #line:908
    O00O0O0000000OOOO =member_scrape (OOO0O00OO00OOOOOO ,OOOOOO0OOOOO00OO0 ,O0OO00000OO0OOO00 [0 ])#line:910
    O00O0O0000000OOOO =[O00OO0OO0O0OOO0OO for O00OO0OO0O0OOO0OO in O00O0O0000000OOOO if O00OO0OO0O0OOO0OO not in OO0000O00O00OO00O ]#line:911
    for _O0OO0000OOO00000O in range (OO000O0000OOOO0O0 ):#line:913
        OOO000O0O0OOO00O0 =OOO0O00OO00OOOOOO [O0O0OOO0O0000000O ]#line:914
        OO00O0O000OOO0OO0 =get_headers (OOO000O0O0OOO00O0 )#line:915
        for O00000OO0OOOOO0O0 in O0OO00000OO0OOO00 :#line:916
            OOOO0OO0O00OOOO0O =OOO0OOOOO00OO0O0O #line:917
            if O0O0OOOO000OO00O0 and O00O0O0000000OOOO :#line:918
                O0000OOOO0O0O000O =random .choice (O00O0O0000000OOOO )#line:919
                OOOO0OO0O00OOOO0O +=f" {O0000OOOO0O0O000O}"#line:920
            O0O00000O00OOOO00 =O0OO00OOO0O00OOOO .post (f"https://discord.com/api/v9/channels/{O00000OO0OOOOO0O0}/messages",json ={"content":OOOO0OO0O00OOOO0O },headers =OO00O0O000OOO0OO0 )#line:922
            if O0O00000O00OOOO00 .status_code ==200 :#line:923
                print (f"200 message sent: {OOO000O0O0OOO00O0}")#line:924
            elif O0O00000O00OOOO00 .status_code ==429 :#line:925
                print (f"429 rate limit: {OOO000O0O0OOO00O0}")#line:926
                O0O0OO0O0O0O0OO00 =O0O00000O00OOOO00 .json ().get ("retry_after",1 )#line:927
                time .sleep (O0O0OO0O0O0O0OO00 )#line:928
            elif O0O00000O00OOOO00 .status_code ==401 :#line:929
                print (f"401 unknown token: {OOO000O0O0OOO00O0}")#line:930
            else :#line:931
                print (f"error: {OOO000O0O0OOO00O0}")#line:932
        O0O0OOO0O0000000O =(O0O0OOO0O0000000O +1 )%len (OOO0O00OO00OOOOOO )#line:934
        time .sleep (1 )#line:935
import requests #line:939
import base64 #line:940
import colorama #line:941
import time #line:942
def add_emojis_from_files ():#line:944
    try :#line:945
        with open ("emojiname.txt")as O0OO00O0O00OO0000 ,open ("emojiurl.txt")as O0OO0O0O0O00O0OO0 :#line:946
            OO0OOO0O000OOO0O0 =[O00OOOO0O000O000O .strip ()for O00OOOO0O000O000O in O0OO00O0O00OO0000 .read ().split (',')if O00OOOO0O000O000O .strip ()]#line:947
            O00O0OOO0O00O000O =[OO00O0O00O0OOOO0O .strip ()for OO00O0O00O0OOOO0O in O0OO0O0O0O00O0OO0 .read ().split (',')if OO00O0O00O0OOOO0O .strip ()]#line:948
    except FileNotFoundError as O000OO0OOOOOOO0OO :#line:949
        print (f"{colorama.Fore.RED}    [!] Error: {str(O000OO0OOOOOOO0OO)}{colorama.Fore.RESET}")#line:950
        return #line:951
    if len (OO0OOO0O000OOO0O0 )!=len (O00O0OOO0O00O000O ):#line:953
        print (f"{colorama.Fore.RED}    [!] Error: The number of emoji names and URLs do not match!{colorama.Fore.RESET}")#line:954
        return #line:955
    try :#line:957
        with open ("token.txt")as O0OOO0OO0O00O0OOO :#line:958
            O000000O0O00OOO0O =[OOOOOOO00OOO0000O .strip ()for OOOOOOO00OOO0000O in O0OOO0OO0O00O0OOO .readlines ()if OOOOOOO00OOO0000O .strip ()]#line:959
    except FileNotFoundError as O000OO0OOOOOOO0OO :#line:960
        print (f"{colorama.Fore.RED}    [!] Error: {str(O000OO0OOOOOOO0OO)}{colorama.Fore.RESET}")#line:961
        return #line:962
    O00O0OOOO0000OO0O =input ("Enter the Guild ID: ").strip ()#line:964
    O00OO0O00O0OOO0OO =input ("Enter the rate limit between requests (in seconds): ").strip ()#line:965
    try :#line:967
        O00OO0O00O0OOO0OO =float (O00OO0O00O0OOO0OO )#line:968
        if O00OO0O00O0OOO0OO <0 :#line:969
            raise ValueError #line:970
    except ValueError :#line:971
        print (f"{colorama.Fore.RED}    [!] Invalid rate limit. Using default rate limit of 5 seconds.{colorama.Fore.RESET}")#line:972
        O00OO0O00O0OOO0OO =5.0 #line:973
    O0000O0O00O0OOO0O =set ()#line:975
    for OOO0OO0O0000OO00O in O000000O0O00OOO0O :#line:977
        OO000OOO0OO0O0O0O ={'Authorization':OOO0OO0O0000OO00O ,'Content-Type':'application/json'}#line:981
        O000OO000O000OO0O =requests .get (f"https://discord.com/api/v9/guilds/{O00O0OOOO0000OO0O}/emojis",headers =OO000OOO0OO0O0O0O )#line:984
        if O000OO000O000OO0O .status_code ==200 :#line:985
            OOO0000O0O0000O00 =O000OO000O000OO0O .json ()#line:986
            for OO0OO0O00O00OO000 in OOO0000O0O0000O00 :#line:987
                O0000O0O00O0OOO0O .add (OO0OO0O00O00OO000 ['name'])#line:988
        else :#line:989
            print (f"{colorama.Fore.RED}    [!] Error fetching existing emojis: {O000OO000O000OO0O.status_code} - {O000OO000O000OO0O.text}{colorama.Fore.RESET}")#line:990
            continue #line:991
    for OO0O0O000O0OOO0OO ,OO0O00OO0OO0OOOOO in zip (OO0OOO0O000OOO0O0 ,O00O0OOO0O00O000O ):#line:993
        if OO0O0O000O0OOO0OO in O0000O0O00O0OOO0O :#line:994
            print (f"{colorama.Fore.YELLOW}    [*] Emoji '{OO0O0O000O0OOO0OO}' already exists. Skipping...{colorama.Fore.RESET}")#line:995
            continue #line:996
        for OOO0OO0O0000OO00O in O000000O0O00OOO0O :#line:998
            try :#line:999
                O000OO000O000OO0O =requests .get (OO0O00OO0OO0OOOOO )#line:1000
                O000OO000O000OO0O .raise_for_status ()#line:1001
                OOOO000OO000OOO00 =O000OO000O000OO0O .content #line:1002
                OOO00OOOO00OO0000 =base64 .b64encode (OOOO000OO000OOO00 ).decode ('utf-8')#line:1003
                OO00OO0000000OOOO ={'name':OO0O0O000O0OOO0OO ,'image':f"data:image/png;base64,{OOO00OOOO00OO0000}"}#line:1008
                OO000OOO0OO0O0O0O ={'Authorization':OOO0OO0O0000OO00O ,'Content-Type':'application/json'}#line:1013
                OOOOO00OOOOO0O0O0 =requests .post (f"https://discord.com/api/v9/guilds/{O00O0OOOO0000OO0O}/emojis",headers =OO000OOO0OO0O0O0O ,json =OO00OO0000000OOOO )#line:1015
                if OOOOO00OOOOO0O0O0 .status_code ==201 :#line:1016
                    print (f"{colorama.Fore.GREEN}    [+] Successfully added emoji '{OO0O0O000O0OOO0OO}' with token {OOO0OO0O0000OO00O}{colorama.Fore.RESET}")#line:1017
                    O0000O0O00O0OOO0O .add (OO0O0O000O0OOO0OO )#line:1018
                    break #line:1019
                else :#line:1020
                    print (f"{colorama.Fore.RED}    [!] Failed to add emoji '{OO0O0O000O0OOO0OO}' with token {OOO0OO0O0000OO00O}: {OOOOO00OOOOO0O0O0.status_code} - {OOOOO00OOOOO0O0O0.text}{colorama.Fore.RESET}")#line:1021
                time .sleep (O00OO0O00O0OOO0OO )#line:1023
            except Exception as O000OO0OOOOOOO0OO :#line:1024
                print (f"{colorama.Fore.RED}    [!] Error adding emoji '{OO0O0O000O0OOO0OO}' with token {OOO0OO0O0000OO00O}: {str(O000OO0OOOOOOO0OO)}{colorama.Fore.RESET}")#line:1025
def main ():#line:1027
    colorama .init ()#line:1028
    while True :#line:1029
        logo ()#line:1030
        OOOOOOO0OO0O00OO0 =input (f"{colorama.Fore.LIGHTMAGENTA_EX}    [Final] Select an option from above: ")#line:1031
        if OOOOOOO0OO0O00OO0 =="0":#line:1033
            update_group_ids ()#line:1034
        elif OOOOOOO0OO0O00OO0 =="1":#line:1035
            join_discord_invite ()#line:1036
        elif OOOOOOO0OO0O00OO0 =="2":#line:1037
            reaction_spammer ()#line:1038
        elif OOOOOOO0OO0O00OO0 =="3":#line:1039
            send_messages_with_mentions ()#line:1040
        elif OOOOOOO0OO0O00OO0 =="4":#line:1041
            spammer_menu ()#line:1042
        elif OOOOOOO0OO0O00OO0 =="5":#line:1043
            nickchanger ()#line:1044
        elif OOOOOOO0OO0O00OO0 =="6":#line:1045
            add_emojis_from_files ()#line:1046
        elif OOOOOOO0OO0O00OO0 =="7":#line:1047
            reaction_art ()#line:1048
        elif OOOOOOO0OO0O00OO0 =="0":#line:1049
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [*] Exiting the application. Goodbye!{colorama.Fore.RESET}")#line:1050
            break #line:1051
        else :#line:1052
            print (f"{colorama.Fore.RED}    [!] Invalid option selected!{colorama.Fore.RESET}")#line:1053
        input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:1055
if __name__ =="__main__":#line:1057
    main ()#line:1058
