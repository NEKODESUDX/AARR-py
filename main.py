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
    O0OOOOO0O0OOOO00O =requests .Session ()#line:58
    if proxy :#line:59
        O0OOOOO0O0OOOO00O .proxies ={"http":proxy ,"https":proxy }#line:60
    return O0OOOOO0O0OOOO00O #line:61
def get_headers (O00O0OOO0OO000OOO ):#line:63
    return {"Authorization":O00O0OOO0OO000OOO ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:68
def send_message_with_mention (O00O000O0O00O0000 ,OO000OO0OO00O0OO0 ,OO0O0OOOO0OOOO000 ,OO0O0O00OOOOOOOO0 ):#line:71
    O000000O0O00O0OO0 =get_session ()#line:72
    O000OOOO0OO00O000 =get_headers (O00O000O0O00O0000 )#line:73
    if OO0O0O00OOOOOOOO0 :#line:75
        O0OOOO0OOOO0O00O0 =random .choice (OO0O0O00OOOOOOOO0 )#line:76
        OO0O0OOOO0OOOO000 +=f" <@{O0OOOO0OOOO0O00O0}>"#line:77
    O000O00000000O0O0 =O000000O0O00O0OO0 .post (f"https://discord.com/api/v9/channels/{OO000OO0OO00O0OO0}/messages",headers =O000OOOO0OO00O000 ,json ={"content":OO0O0OOOO0OOOO000 })#line:83
    if O000O00000000O0O0 .status_code in [200 ,201 ]:#line:84
        print (f"[+] Message sent to channel {OO000OO0OO00O0OO0}")#line:85
    elif O000O00000000O0O0 .status_code ==429 :#line:86
        print ("[-] Rate limited. Please wait before retrying.")#line:87
        O0OOOOO0OOOOOOO0O =O000O00000000O0O0 .json ().get ("retry_after",1 )#line:88
        time .sleep (O0OOOOO0OOOOOOO0O )#line:89
    else :#line:90
        print (f"[!] Error occurred: {O000O00000000O0O0.status_code}")#line:91
def fetch_messages (OOOO0000O0OOO0OOO ,O0O00OOOO00O00OOO ,limit =100 ):#line:94
    OO000O00000OO0O0O ={"Authorization":OOOO0000O0OOO0OOO ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:99
    O0O000O0000000000 =requests .get (f"https://discord.com/api/v9/channels/{O0O00OOOO00O00OOO}/messages?limit={limit}",headers =OO000O00000OO0O0O )#line:103
    if O0O000O0000000000 .status_code ==200 :#line:104
        return O0O000O0000000000 .json ()#line:105
    else :#line:106
        print (f"[!] Failed to fetch messages. HTTP Status Code: {O0O000O0000000000.status_code}")#line:107
        return []#line:108
import concurrent .futures #line:110
import time #line:112
import urllib .parse #line:113
import requests #line:114
import concurrent .futures #line:115
def reaction_spammer ():#line:117
    try :#line:118
        with open ("token.txt")as O0O000OOO00OOOO0O :#line:119
            OO0OOOOO000OOOOO0 =[O0OOO0O0OO0OO000O .strip ()for O0OOO0O0OO0OO000O in O0O000OOO00OOOO0O .readlines ()if O0OOO0O0OO0OO000O .strip ()]#line:120
    except (FileNotFoundError ,KeyError ):#line:121
        print ("Error: token.txt file not found or no valid tokens!")#line:122
        return #line:123
    if not OO0OOOOO000OOOOO0 :#line:125
        print ("No tokens found in token.txt!")#line:126
        return #line:127
    OO0OO0O000000OO00 =input ("Server ID?: ").strip ()#line:129
    O0OOO0OOOO00O000O =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:131
    if O0OOO0OOOO00O000O =='2':#line:132
        O00O00OO000O00OO0 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:133
        O00O0OOOO00O0OOO0 =[O0OO0O0O0OO00O0OO .strip ()for O0OO0O0O0OO00O0OO in O00O00OO000O00OO0 if O0OO0O0O0OO00O0OO .strip ()]#line:134
    else :#line:135
        O00O0OOOO00O0OOO0 =[]#line:136
        for OOOOOO00000OO0000 in OO0OOOOO000OOOOO0 :#line:137
            try :#line:138
                O00O0OOOO00O0OOO0 .extend (fetch_channels (OOOOOO00000OO0000 ,OO0OO0O000000OO00 ))#line:139
            except Exception as O0O00OOO0O0O0OOOO :#line:140
                print (f"Failed to fetch channels for token. Error: {O0O00OOO0O0O0OOOO}")#line:141
                continue #line:142
    OOOOOOO00O0O000OO =input ("Select your emoji (custom emojis should be in 'emoji_name:emoji_id' format): ").strip ()#line:144
    O0OO00OO00OOO0O00 =input ("Delay between reactions (in seconds)?: ").strip ()#line:145
    try :#line:147
        O0OO00OO00OOO0O00 =float (O0OO00OO00OOO0O00 )#line:148
        if O0OO00OO00OOO0O00 <0 :#line:149
            raise ValueError #line:150
    except ValueError :#line:151
        print ("Invalid delay. Using default delay of 1 second.")#line:152
        O0OO00OO00OOO0O00 =1.0 #line:153
    O0O000O0O00OOOOOO =[]#line:155
    for OO0000O0OO0O0O00O in OOOOOOO00O0O000OO .split (","):#line:156
        OO0000O0OO0O0O00O =OO0000O0OO0O0O00O .strip ()#line:157
        O0O000O0O00OOOOOO .append (OO0000O0OO0O0O00O )#line:158
    if not O0O000O0O00OOOOOO :#line:160
        print ("No valid emojis provided!")#line:161
        return #line:162
    def O0O00O0O0O00O00OO (OO0OOO0OO0O0OOOOO ):#line:164
        for OOOO0000OO0000OOO in O00O0OOOO00O0OOO0 :#line:165
            try :#line:166
                print (f"Processing channel {OOOO0000OO0000OOO}...")#line:167
                OO00O0OO0OOOOO00O =fetch_messages (OO0OOO0OO0O0OOOOO ,OOOO0000OO0000OOO ,limit =100 )#line:168
                if not OO00O0OO0OOOOO00O :#line:169
                    print (f"No messages found in the channel {OOOO0000OO0000OOO} or an error occurred.")#line:170
                    continue #line:171
                for O0OOO00OOO00O0OO0 in OO00O0OO0OOOOO00O :#line:173
                    for O000O000O00OOOO0O in O0O000O0O00OOOOOO :#line:174
                        reactionput (OO0OOO0OO0O0OOOOO ,OOOO0000OO0000OOO ,O0OOO00OOO00O0OO0 ['id'],O000O000O00OOOO0O )#line:175
                        time .sleep (O0OO00OO00OOO0O00 )#line:176
            except Exception as O0O00OOOO0000O00O :#line:177
                print (f"Error processing channel {OOOO0000OO0000OOO}. Error: {O0O00OOOO0000O00O}")#line:178
                continue #line:179
    with concurrent .futures .ThreadPoolExecutor ()as OOO0OO0OO00000O00 :#line:181
        OO0OO000OOOOOOO00 =[OOO0OO0OO00000O00 .submit (O0O00O0O0O00O00OO ,OOO0OO0OOOOO0000O )for OOO0OO0OOOOO0000O in OO0OOOOO000OOOOO0 ]#line:182
        concurrent .futures .wait (OO0OO000OOOOOOO00 )#line:183
def reactionput (O0OOOO00O0OOOO00O ,OOOO00O0OO000O0OO ,OO0O000OO000OO000 ,O0O0O0OO00OO0O0OO ):#line:185
    if ':'in O0O0O0OO00OO0O0OO :#line:187
        O0000O0O000O0000O ,OO000000O0OO0O00O =O0O0O0OO00OO0O0OO .split (':')#line:188
        OOOO0000O0OO0O0OO =f"{O0000O0O000O0000O}%3A{OO000000O0OO0O00O}"#line:189
    else :#line:190
        OOOO0000O0OO0O0OO =urllib .parse .quote (O0O0O0OO00OO0O0OO )#line:191
    OO0000OOOOOO00OOO =f"https://discord.com/api/v9/channels/{OOOO00O0OO000O0OO}/messages/{OO0O000OO000OO000}/reactions/{OOOO0000O0OO0O0OO}/%40me?location=Message%20Inline%20Button&type=0"#line:193
    O00000OOOOOOO0000 ={"Authorization":O0OOOO00O0OOOO00O ,"Content-Type":"application/json"}#line:198
    OO000O00O000OO00O ={"http":None ,"https":None }#line:204
    print (f"Request URL: {OO0000OOOOOO00OOO}")#line:207
    print (f"Request Headers: {O00000OOOOOOO0000}")#line:208
    try :#line:210
        O0OOO000O0000OO00 =requests .put (OO0000OOOOOO00OOO ,headers =O00000OOOOOOO0000 ,proxies =OO000O00O000OO00O )#line:211
        if O0OOO000O0000OO00 .status_code ==204 :#line:212
            print ("Successfully reacted with emoji")#line:213
        else :#line:214
            print (f"Failed to react with emoji: {O0OOO000O0000OO00.status_code} - {O0OOO000O0000OO00.text}")#line:215
    except requests .exceptions .RequestException as O0000O0OO0O0000O0 :#line:216
        print (f"Request failed: {O0000O0OO0O0000O0}")#line:217
def fetch_channels (OO0O0OOOOOOOOOO0O ,O00O0O0000000O0OO ):#line:220
    OO0OO00O00O00O000 =f"https://discord.com/api/v9/guilds/{O00O0O0000000O0OO}/channels"#line:221
    O0O0OOO0OO0O000OO ={"Authorization":OO0O0OOOOOOOOOO0O }#line:222
    OO00O0000O0O0OOOO =requests .get (OO0OO00O00O00O000 ,headers =O0O0OOO0OO0O000OO )#line:223
    if OO00O0000O0O0OOOO .status_code ==200 :#line:224
        return [O000O0O00OO00O000 ['id']for O000O0O00OO00O000 in OO00O0000O0O0OOOO .json ()if O000O0O00OO00O000 ['type']==0 ]#line:225
    else :#line:226
        print (f"Failed to fetch channels: {OO00O0000O0O0OOOO.status_code} - {OO00O0000O0O0OOOO.text}")#line:227
        return []#line:228
def fetch_messages (O0O0O00OO00OO00OO ,O000O000O0000000O ,limit =100 ):#line:231
    O00000O0O000O0OO0 =f"https://discord.com/api/v9/channels/{O000O000O0000000O}/messages?limit={limit}"#line:232
    OOO0OO00OOO0O000O ={"Authorization":O0O0O00OO00OO00OO }#line:233
    O000O0000OO0OOO0O =requests .get (O00000O0O000O0OO0 ,headers =OOO0OO00OOO0O000O )#line:234
    if O000O0000OO0OOO0O .status_code ==200 :#line:235
        return O000O0000OO0OOO0O .json ()#line:236
    else :#line:237
        print (f"Failed to fetch messages: {O000O0000OO0OOO0O.status_code} - {O000O0000OO0OOO0O.text}")#line:238
        return []#line:239
import requests #line:242
import json #line:243
import time #line:244
import colorama #line:245
alphabet_to_flag ={'a':'🇦','b':'🇧','c':'🇨','d':'🇩','e':'🇪','f':'🇫','g':'🇬','h':'🇭','i':'🇮','j':'🇯','k':'🇰','l':'🇱','m':'🇲','n':'🇳','o':'🇴','p':'🇵','q':'🇶','r':'🇷','s':'🇸','t':'🇹','u':'🇺','v':'🇻','w':'🇼','x':'🇽','y':'🇾','z':'🇿'}#line:253
def fetch_channels (OO00OO0O0O00O0O0O ,OOOOO0OO00OO0OOOO ):#line:255
    O0OO000O0OO00O000 =f"https://discord.com/api/v9/guilds/{OOOOO0OO00OO0OOOO}/channels"#line:256
    OOO0O00OOOO0000OO ={"Authorization":OO00OO0O0O00O0O0O }#line:257
    OOO00OO0OOO0O00OO =requests .get (O0OO000O0OO00O000 ,headers =OOO0O00OOOO0000OO )#line:258
    if OOO00OO0OOO0O00OO .status_code ==200 :#line:259
        return [OO0O0OO00O0O0O000 ['id']for OO0O0OO00O0O0O000 in OOO00OO0OOO0O00OO .json ()if OO0O0OO00O0O0O000 ['type']==0 ]#line:260
    else :#line:261
        raise Exception (f"Failed to fetch channels: {OOO00OO0OOO0O00OO.status_code} - {OOO00OO0OOO0O00OO.text}")#line:262
def fetch_messages (OO0O00O000OO00O00 ,OOOOOOOOOOO0OOO0O ,limit =100 ):#line:264
    O00O000O00000O0O0 =f"https://discord.com/api/v9/channels/{OOOOOOOOOOO0OOO0O}/messages?limit={limit}"#line:265
    O000000O0O0000O00 ={"Authorization":OO0O00O000OO00O00 }#line:266
    OOO00O0OOOO000O00 =requests .get (O00O000O00000O0O0 ,headers =O000000O0O0000O00 )#line:267
    if OOO00O0OOOO000O00 .status_code ==200 :#line:268
        return OOO00O0OOOO000O00 .json ()#line:269
    else :#line:270
        print (f"[!] Failed to fetch messages: {OOO00O0OOOO000O00.status_code} - {OOO00O0OOOO000O00.text}")#line:271
        return []#line:272
def reactionput (OO0O0O0O0OO00O0O0 ,O0OO0000000OO000O ,O000OOOOO0OO00OO0 ,OO00OO0OOOOO0OOOO ):#line:274
    OO00OOO0OOOO00OOO =f"https://discord.com/api/v9/channels/{O0OO0000000OO000O}/messages/{O000OOOOO0OO00OO0}/reactions/{OO00OO0OOOOO0OOOO}/@me"#line:275
    OOO0OO000O0O0O0OO ={"Authorization":OO0O0O0O0OO00O0O0 ,"Content-Type":"application/json"}#line:276
    O0O0000O00O00O0O0 =requests .put (OO00OOO0OOOO00OOO ,headers =OOO0OO000O0O0O0OO )#line:277
    if O0O0000O00O00O0O0 .status_code not in [204 ,200 ]:#line:278
        print (f"{colorama.Fore.RED}    [!] Failed to add reaction: {O0O0000O00O00O0O0.status_code} - {O0O0000O00O00O0O0.text}{colorama.Fore.RESET}")#line:279
import random #line:281
def reaction_art ():#line:283
    try :#line:284
        with open ("token.txt",encoding ="utf-8")as O000O0O0O0OO00OO0 :#line:285
            O0OOO0000OO0OOOOO =[O0O000O0OOO000OO0 .strip ()for O0O000O0OOO000OO0 in O000O0O0O0OO00OO0 .readlines ()if O0O000O0OOO000OO0 .strip ()]#line:286
    except (FileNotFoundError ,KeyError ):#line:287
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:288
        return #line:289
    OO00000000OOO00OO =input ("Server ID?: ").strip ()#line:291
    O0OOOO0OOOO00O000 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:293
    if O0OOOO0OOOO00O000 =='2':#line:294
        O00OO0O00OO0O0O0O =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:295
        OO0OOO0OO0000O0OO =[O00OOOO00O00OO0OO .strip ()for O00OOOO00O00OO0OO in O00OO0O00OO0O0O0O if O00OOOO00O00OO0OO .strip ()]#line:296
    else :#line:297
        OO0OOO0OO0000O0OO =[]#line:298
        for OOO000OO00000000O in O0OOO0000OO0OOOOO :#line:299
            try :#line:300
                OO0OOO0OO0000O0OO .extend (fetch_channels (OOO000OO00000000O ,OO00000000OOO00OO ))#line:301
            except Exception as OO000O000000OOO0O :#line:302
                print (f"[!] Failed to fetch channels for token. Error: {OO000O000000OOO0O}")#line:303
                continue #line:304
        random .shuffle (OO0OOO0OO0000O0OO )#line:305
    OO0O0000O0OOOO00O =input ("Delay between reactions (in seconds)?: ").strip ()#line:307
    try :#line:309
        OO0O0000O0OOOO00O =float (OO0O0000O0OOOO00O )#line:310
        if OO0O0000O0OOOO00O <0 :#line:311
            raise ValueError #line:312
    except ValueError :#line:313
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:314
        OO0O0000O0OOOO00O =1.0 #line:315
    try :#line:317
        with open ("art.txt",encoding ="utf-8")as OO0O0000O0OOOO0OO :#line:318
            OOO000OOOOO00O000 =[OOO0OO000O0OOO000 .strip ()for OOO0OO000O0OOO000 in OO0O0000O0OOOO0OO .readlines ()if OOO0OO000O0OOO000 .strip ()]#line:319
    except (FileNotFoundError ,KeyError ):#line:320
        print (f"{colorama.Fore.RED}    [!] Error: art.txt file not found or empty!{colorama.Fore.RESET}")#line:321
        return #line:322
    except UnicodeDecodeError as OO000O000000OOO0O :#line:323
        print (f"{colorama.Fore.RED}    [!] Error decoding art.txt: {str(OO000O000000OOO0O)}{colorama.Fore.RESET}")#line:324
        return #line:325
    if not OOO000OOOOO00O000 :#line:327
        print (f"{colorama.Fore.RED}    [!] No valid art provided in art.txt!{colorama.Fore.RESET}")#line:328
        return #line:329
    OOO000OOOOO00O000 .reverse ()#line:332
    for OOO000OO00000000O in O0OOO0000OO0OOOOO :#line:334
        for O0O000OO00O0OOOOO in OO0OOO0OO0000O0OO :#line:335
            try :#line:336
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {O0O000OO00O0OOOOO}...{colorama.Fore.RESET}")#line:337
                O00O00OO00O000O0O =fetch_messages (OOO000OO00000000O ,O0O000OO00O0OOOOO ,limit =100 )#line:340
                if not O00O00OO00O000O0O :#line:341
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:342
                    continue #line:343
                for OOO00OOO000O0O00O ,OO0OO0OOO000O0000 in enumerate (O00O00OO00O000O0O ):#line:346
                    O0000O0O0OOOO0O0O =OOO000OOOOO00O000 [OOO00OOO000O0O00O %len (OOO000OOOOO00O000 )].split (',')#line:347
                    for OOOOO0000O000OOO0 in O0000O0O0OOOO0O0O :#line:348
                        reactionput (OOO000OO00000000O ,O0O000OO00O0OOOOO ,OO0OO0OOO000O0000 ['id'],OOOOO0000O000OOO0 .strip ())#line:349
                        print (f"Adding reaction '{OOOOO0000O000OOO0.strip()}' to message {OO0OO0OOO000O0000['id']} in channel {O0O000OO00O0OOOOO}")#line:350
                        time .sleep (OO0O0000O0OOOO00O )#line:351
            except Exception as OO000O000000OOO0O :#line:352
                print (f"[!] Error processing channel {O0O000OO00O0OOOOO}. Error: {OO000O000000OOO0O}")#line:353
                continue #line:354
    def OO0O00OO0OOO0O0O0 (OOO00O0OO0O0000OO ):#line:359
        for OOO0OOO00OO0O0OO0 in OO0OOO0OO0000O0OO :#line:360
            try :#line:361
                print (f"{colorama.Fore.LIGHTCYAN_EX}Processing channel {OOO0OOO00OO0O0OO0}...{colorama.Fore.RESET}")#line:362
                OO00000O0OO0O0O0O =fetch_messages (OOO00O0OO0O0000OO ,OOO0OOO00OO0O0OO0 ,limit =100 )#line:363
                if not OO00000O0OO0O0O0O :#line:364
                    print (f"{colorama.Fore.RED}    [!] No messages found in the channel or an error occurred.{colorama.Fore.RESET}")#line:365
                    continue #line:366
                for OO00OOO0000O0O0OO in OO00000O0OO0O0O0O :#line:368
                    for OO000OO0OOO0000OO in O0000O0O0OOOO0O0O :#line:369
                        reactionput (OOO00O0OO0O0000OO ,OOO0OOO00OO0O0OO0 ,OO00OOO0000O0O0OO ['id'],OO000OO0OOO0000OO )#line:370
                        time .sleep (OO0O0000O0OOOO00O )#line:371
            except Exception as OO00OOO0OO0O00O0O :#line:372
                print (f"[!] Error processing channel {OOO0OOO00OO0O0OO0}. Error: {OO00OOO0OO0O00O0O}")#line:373
                continue #line:374
    with concurrent .futures .ThreadPoolExecutor ()as O000O0O0O0O0000O0 :#line:376
        O0O000OOO0O000000 =[O000O0O0O0O0000O0 .submit (OO0O00OO0OOO0O0O0 ,OOOO00O000OO0OOOO )for OOOO00O000OO0OOOO in O0OOO0000OO0OOOOO ]#line:377
        concurrent .futures .wait (O0O000OOO0O000000 )#line:378
def update_group_ids ():#line:381
    try :#line:382
        with open ("token.txt")as O0OO000O0OOO000OO :#line:383
            OOO0O00OO0O0OO00O =[OOOO0OOO0O0O000OO .strip ()for OOOO0OOO0O0O000OO in O0OO000O0OOO000OO .readlines ()if OOOO0OOO0O0O000OO .strip ()]#line:384
        OOO000000O0OOOO00 =OOO0O00OO0O0OO00O [0 ]#line:385
    except (FileNotFoundError ,KeyError ):#line:386
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:387
        return #line:388
    OOO0O0O0000OO0O0O ={"Authorization":OOO000000O0OOOO00 ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:394
    OOOO0O000OOOOOOO0 =requests .get ('https://discord.com/api/v9/users/@me/channels',headers =OOO0O0O0000OO0O0O )#line:396
    if OOOO0O000OOOOOOO0 .status_code ==200 :#line:397
        OO00O000OOO0O0O0O =OOOO0O000OOOOOOO0 .json ()#line:398
        with open ("group_id.txt","w")as OOOO0000OO000OOOO :#line:399
            for O0000O000O0O00O0O in OO00O000OOO0O0O0O :#line:400
                if O0000O000O0O00O0O ['type']==3 :#line:401
                    OOOO0000OO000OOOO .write (O0000O000O0O00O0O ['id']+'\n')#line:402
        print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Group IDs updated successfully.{colorama.Fore.RESET}")#line:403
    else :#line:404
        print (f"{colorama.Fore.LIGHTRED_EX}    [!] Failed to retrieve group IDs. HTTP Status Code: {OOOO0O000OOOOOOO0.status_code}{colorama.Fore.RESET}")#line:405
import requests #line:407
import requests #line:409
def fetch_channels (OOOO0000OOO000000 ,O00O000OO0O0OO0O0 ):#line:411
    try :#line:412
        OOOOOOOOO0O000OO0 =requests .Session ()#line:413
        O0OO00O0O0O00000O =get_headers (OOOO0000OOO000000 )#line:414
        OOO00OOOO0OO0O0OO =OOOOOOOOO0O000OO0 .get (f"https://discord.com/api/v9/guilds/{O00O000OO0O0OO0O0}/channels",headers =O0OO00O0O0O00000O ,timeout =10 )#line:421
        if OOO00OOOO0OO0O0OO .status_code ==200 :#line:424
            try :#line:425
                OOO000000O0OO000O =OOO00OOOO0OO0O0OO .json ()#line:426
                return [O0O00OOO0OO0OO000 ['id']for O0O00OOO0OO0OO000 in OOO000000O0OO000O if O0O00OOO0OO0OO000 .get ('type')==0 ]#line:427
            except ValueError :#line:428
                print ("[!] Error: Response was not valid JSON.")#line:429
                return []#line:430
        elif OOO00OOOO0OO0O0OO .status_code ==401 :#line:431
            print ("[!] Error: Unauthorized - check your token.")#line:432
        elif OOO00OOOO0OO0O0OO .status_code ==403 :#line:433
            print ("[!] Error: Forbidden - you lack permissions.")#line:434
        elif OOO00OOOO0OO0O0OO .status_code ==404 :#line:435
            print ("[!] Error: Server not found - check the server ID.")#line:436
        else :#line:437
            print (f"[!] Error: Unexpected status code {OOO00OOOO0OO0O0OO.status_code}.")#line:438
        return []#line:441
    except requests .exceptions .Timeout :#line:443
        print ("[!] Error: Request timed out. Check your connection or try again later.")#line:444
        return []#line:445
    except requests .exceptions .RequestException as O0OO0OO0O0OO000OO :#line:446
        print (f"[!] Error: An error occurred while fetching channels: {O0OO0OO0O0OO000OO}")#line:447
        return []#line:448
def extract_uids_from_messages (OO00OOOOOOO00O00O ):#line:454
    O0O0O0000OO000O00 =set ()#line:455
    for OO0O0O0OO000OOO00 in OO00OOOOOOO00O00O :#line:456
        O0O0O0000OO000O00 .add (OO0O0O0OO000OOO00 ['author']['id'])#line:457
    return list (O0O0O0000OO000O00 )#line:458
def send_message_with_mention (O0OOO0O0OO00000OO ,OOO0OOO0O0O0O0000 ,O00O0O000O000O0O0 ,OOO00OO000000O0OO ):#line:460
    OO0OOO0O0OOO0OO0O =get_session ()#line:461
    OO0O0OOO0O0OO0O00 =get_headers (O0OOO0O0OO00000OO )#line:462
    if OOO00OO000000O0OO :#line:464
        OO0O0O0OOOO00O00O =random .choice (OOO00OO000000O0OO )#line:465
        O00O0O000O000O0O0 +=f" <@{OO0O0O0OOOO00O00O}>"#line:466
    O0O000O0O0O0000O0 =OO0OOO0O0OOO0OO0O .post (f"https://discord.com/api/v9/channels/{OOO0OOO0O0O0O0000}/messages",headers =OO0O0OOO0O0OO0O00 ,json ={"content":O00O0O000O000O0O0 })#line:472
    if O0O000O0O0O0000O0 .status_code in [200 ,201 ]:#line:473
        print (f"[+] Message sent to channel {OOO0OOO0O0O0O0000}")#line:474
    elif O0O000O0O0O0000O0 .status_code ==429 :#line:475
        print ("[-] Rate limited. Please wait before retrying.")#line:476
        OO00O00OOO000OOOO =O0O000O0O0O0000O0 .json ().get ("retry_after",1 )#line:477
        time .sleep (OO00O00OOO000OOOO )#line:478
    else :#line:479
        print (f"[!] Error occurred: {O0O000O0O0O0000O0.status_code}")#line:480
def send_messages_with_mentions ():#line:481
    try :#line:482
        with open ("token.txt")as O0O0000OO0O0OOO00 :#line:483
            OOO000O0O0O0O0000 =[O000OO0O0O0O0O0OO .strip ()for O000OO0O0O0O0O0OO in O0O0000OO0O0OOO00 .readlines ()if O000OO0O0O0O0O0OO .strip ()]#line:484
    except (FileNotFoundError ,KeyError ):#line:485
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:486
        return #line:487
    O0O0000O0O000OOOO =input ("Server ID?: ").strip ()#line:489
    OOO0OO00OOOOOO0OO =input ("Delay between messages (in seconds)?: ").strip ()#line:490
    OO0OO0O000O0OOO00 =input ("Number of messages to send?: ").strip ()#line:491
    O00O0OOOO000O00OO =input ("Message content?: ").strip ()#line:492
    OOOO00O0O0OO00OOO =input ("Blacklist User IDs (comma-separated)?: ").strip ().split (',')#line:493
    OOOO00O0O0OO00OOO =[OOOO0O0O0OO0OOO00 .strip ()for OOOO0O0O0OO0OOO00 in OOOO00O0O0OO00OOO if OOOO0O0O0OO0OOO00 .strip ()]#line:494
    try :#line:496
        OOO0OO00OOOOOO0OO =float (OOO0OO00OOOOOO0OO )#line:497
        if OOO0OO00OOOOOO0OO <0 :#line:498
            raise ValueError #line:499
    except ValueError :#line:500
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:501
        OOO0OO00OOOOOO0OO =1.0 #line:502
    try :#line:504
        OO0OO0O000O0OOO00 =int (OO0OO0O000O0OOO00 )#line:505
        if OO0OO0O000O0OOO00 <=0 :#line:506
            raise ValueError #line:507
    except ValueError :#line:508
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:509
        OO0OO0O000O0OOO00 =1 #line:510
    OOO00OOOOOO000OO0 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:512
    if OOO00OOOOOO000OO0 =='2':#line:513
        O00O0OOOO000000O0 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:514
        O00O0OOOO000000O0 =[O00O000O0OO0O0OOO .strip ()for O00O000O0OO0O0OOO in O00O0OOOO000000O0 if O00O000O0OO0O0OOO .strip ()]#line:515
    else :#line:516
        O00O0OOOO000000O0 =[]#line:517
    O0OOO00O0000OOO0O =set ()#line:519
    for OO0O00O0O0OO0O00O in OOO000O0O0O0O0000 :#line:520
        OOOO0O00000O00O0O =fetch_channels (OO0O00O0O0OO0O00O ,O0O0000O0O000OOOO )#line:521
        for OOOO00O00O00O00O0 in OOOO0O00000O00O0O :#line:522
            OOOO0OO0OO0OO0000 =fetch_messages (OO0O00O0O0OO0O00O ,OOOO00O00O00O00O0 ,limit =100 )#line:523
            O000OOOO000000O0O =extract_uids_from_messages (OOOO0OO0OO0OO0000 )#line:524
            O0OOO00O0000OOO0O .update (O000OOOO000000O0O )#line:525
    O0OOO00O0000OOO0O =list (set (O0OOO00O0000OOO0O )-set (OOOO00O0O0OO00OOO ))#line:528
    for _O0OOOO000OOOOO00O in range (OO0OO0O000O0OOO00 ):#line:530
        for OO0O00O0O0OO0O00O in OOO000O0O0O0O0000 :#line:531
            if O00O0OOOO000000O0 :#line:532
                OOOO0O00000O00O0O =O00O0OOOO000000O0 #line:533
            for OOOO00O00O00O00O0 in OOOO0O00000O00O0O :#line:534
                send_message_with_mention (OO0O00O0O0OO0O00O ,OOOO00O00O00O00O0 ,O00O0OOOO000O00OO ,O0OOO00O0000OOO0O )#line:535
                time .sleep (OOO0OO00OOOOOO0OO )#line:536
def join_discord_invite ():#line:541
    try :#line:542
        with open ("token.txt")as OO0O0000000OOO000 :#line:543
            OOOO0OOO0O00OOOOO =[OO00OO0OO00O0O0OO .strip ()for OO00OO0OO00O0O0OO in OO0O0000000OOO000 .readlines ()if OO00OO0OO00O0O0OO .strip ()]#line:544
    except (FileNotFoundError ,KeyError ):#line:545
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:546
        return #line:547
    O0OOO000OO0O0O0O0 =input ("Invite Code?: discord.gg/").strip ()#line:549
    for O00OOO0OO0O000OOO in OOOO0OOO0O00OOOOO :#line:552
        joiner (O00OOO0OO0O000OOO ,O0OOO000OO0O0O0O0 )#line:553
import json ,time ,base64 ,random ,requests #line:555
def cookieset (O0O0000O00000O000 ):#line:557
    OOOOOOO0OO0OOOOO0 =O0O0000O00000O000 .get ("https://discord.com/app")#line:558
    return OOOOOOO0OO0OOOOO0 .cookies .get_dict ()#line:559
def generatexspandua (O0O00O00O0O00OO0O ):#line:561
    O00OOO0OOO0O00OOO =["Android","Windows","Macintosh"]#line:562
    O000OOOOOOOOO0O0O =random .choice (O00OOO0OOO0O00OOO )#line:563
    if O000OOOOOOOOO0O0O =="Macintosh":#line:564
        O00OO00O0O000O0OO =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:565
        OO00OOOOO0000O0OO ="Macintosh; Intel Mac OS X "+O00OO00O0O000O0OO #line:566
        O00O00O00OOOOOO00 ="x86_64"#line:567
    elif O000OOOOOOOOO0O0O =="Windows":#line:568
        O00OO00O0O000O0OO =f'{random.choice([6.0, 10.0, 11.0])}'#line:569
        OO00OOOOO0000O0OO ="Windows NT "+O00OO00O0O000O0OO +" Win64; x64"#line:570
        O00O00O00OOOOOO00 ="x86_64"#line:571
    else :#line:572
        O00OO00O0O000O0OO ="13"#line:573
        OO00OOOOO0000O0OO =f"Linux; Android 13; Pixel 6a"#line:574
        O00O00O00OOOOOO00 ="aarch64"#line:575
    O000O00O0OOOOOO0O ={"os":O000OOOOOOOOO0O0O ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":O00OO00O0O000O0OO ,"os_arch":O00O00O00OOOOOO00 ,"system_locale":"ja-JP","client_build_number":O0O00O00O0O00OO0O ,"client_event_source":None ,"design_id":0 }#line:588
    OOO0OOO0O00OOOOO0 =f"Mozilla/5.0 ({OO00OOOOO0000O0OO}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:589
    return base64 .b64encode (json .dumps (O000O00O0OOOOOO0O ,separators =(',',':')).encode ()).decode (),OOO0OOO0O00OOOOO0 #line:590
def joiner (OO000O00000OOO0OO ,OO0O0O00O0OOO000O ,O0OO0OOOO0OOO0O0O ,O00O0OO00OOOO0O0O ):#line:592
  OO00OOO0O0OOO0O00 =get_session (O0OO0OOOO0OOO0O0O )#line:593
  OO00000OO00O0OO00 =cookieset (OO00OOO0O0OOO0O00 )#line:594
  OO00000OO00O0OO00 ["locale"]="ja-JP"#line:595
  O00OO0OOO00O00OOO =201211 #line:596
  O00OO0OO0O000O000 ,OO000OO0OO0O00OOO =generatexspandua (O00OO0OOO00O00OOO )#line:597
  O000OO0OOOOO0OOOO ={"Authorization":OO000O00000OOO0OO ,"accept":"*/*","accept-language":"ja-JP","connection":"keep-alive","DNT":"1","origin":"https://discord.com","sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","referer":"https://discord.com/channels/@me","TE":"Trailers","user-agent":OO000OO0OO0O00OOO ,"X-Super-Properties":O00OO0OO0O000O000 ,}#line:612
  OO0O000O00000O00O =OO00OOO0O0OOO0O00 .post ("https://discord.com/api/v9/invites/"+OO0O0O00O0OOO000O ,headers =O000OO0OOOOO0OOOO ,json ={},cookies =OO00000OO00O0OO00 )#line:614
  if OO0O000O00000O00O .status_code ==200 :#line:615
    print ("[+] Probably joined "+OO000O00000OOO0OO )#line:616
    if "show_verification_form"in OO0O000O00000O00O .json ():#line:617
      bypass (OO000O00000OOO0OO ,OO0O000O00000O00O .json ()["guild"]["id"],OO00OOO0O0OOO0O00 ,O000OO0OOOOO0OOOO )#line:618
    return #line:619
  elif "captcha_key"in OO0O000O00000O00O .text and OO0O000O00000O00O .status_code ==400 :#line:620
    print ("[!] Hcaptcha interference "+OO000O00000OOO0OO )#line:621
    return #line:622
  elif OO0O000O00000O00O .status_code ==401 :#line:623
    print ("[!] Token is dead "+OO000O00000OOO0OO )#line:624
    return #line:625
  elif OO0O000O00000O00O .status_code ==403 :#line:626
    if "message"in OO0O000O00000O00O .json ():#line:627
      if OO0O000O00000O00O .json ()["message"]=="Unknown Message":#line:628
        print ("[!] Unknown error "+OO000O00000OOO0OO )#line:629
        return #line:630
      else :#line:631
        print ("[!] Verification required "+OO000O00000OOO0OO )#line:632
        return #line:633
    else :#line:634
      print ("[!] Error occurred "+OO000O00000OOO0OO )#line:635
      return #line:636
  elif OO0O000O00000O00O .status_code ==429 :#line:637
    print ("[!] Token rate-limited "+OO000O00000OOO0OO )#line:638
    return #line:639
  elif OO0O000O00000O00O .status_code ==400 :#line:640
    if "captcha_key"in OO0O000O00000O00O .json ():#line:641
      print ("[!] Hcaptcha interference "+OO000O00000OOO0OO )#line:642
      return #line:643
    else :#line:644
      print ("[!] Error occurred "+OO000O00000OOO0OO )#line:645
      return #line:646
  elif OO0O000O00000O00O .status_code ==401 :#line:647
    print ("[!] Token is dead "+OO000O00000OOO0OO )#line:648
    return #line:649
  elif OO0O000O00000O00O .status_code ==403 :#line:650
    if "message"in OO0O000O00000O00O .json ():#line:651
      if OO0O000O00000O00O .json ()["message"]=="Unknown Message":#line:652
        print ("[!] Unknown error "+OO000O00000OOO0OO )#line:653
        return #line:654
      else :#line:655
        print ("[!] Verification required "+OO000O00000OOO0OO )#line:656
        return #line:657
    else :#line:658
      print ("[!] Error occurred "+OO000O00000OOO0OO )#line:659
  elif OO0O000O00000O00O .status_code ==429 :#line:660
    print ("[!] Token rate-limited "+OO000O00000OOO0OO )#line:661
    return #line:662
  else :#line:663
    print ("[!] Error occurred "+OO000O00000OOO0OO )#line:664
    return #line:665
def update_group_ids ():#line:668
    OOO00OOO00O0OOOO0 =input ("Invite Code?: ").strip ()#line:669
    try :#line:670
        with open ("token.txt")as OOO00OO0000000O0O :#line:671
            O00OO0OO0OO00OO00 =[O00OOO000O0OOOO0O .strip ()for O00OOO000O0OOOO0O in OOO00OO0000000O0O .readlines ()if O00OOO000O0OOOO0O .strip ()]#line:672
    except (FileNotFoundError ,KeyError ):#line:673
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:674
        return #line:675
    OOOOO0OOOOOO00O0O =requests .Session ()#line:677
    for O0OO000O00O0OOO00 in O00OO0OO0OO00OO00 :#line:678
        joiner (O0OO000O00O0OOO00 ,OOO00OOO00O0OOOO0 ,OOOOO0OOOOOO00O0O )#line:679
        time .sleep (2 )#line:680
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:682
def bypass (O000000O0O0OOOO00 ,O0O0OOOOOO0000000 ,OOOOO000OO000O0OO ,O0O0O0OO0O0O00OOO ):#line:685
    try :#line:686
        O00O00OOOOOOO00O0 =OOOOO000OO000O0OO .get (f"https://discord.com/api/v9/guilds/{O0O0OOOOOO0000000}/member-verification?with_guild=false",headers =O0O0O0OO0O0O00OOO ).json ()#line:687
        O00O0O00O0O0OOO00 =OOOOO000OO000O0OO .put (f"https://discord.com/api/v9/guilds/{O0O0OOOOOO0000000}/requests/@me",headers =O0O0O0OO0O0O00OOO ,json =O00O00OOOOOOO00O0 )#line:688
        if O00O0O00O0O0OOO00 .status_code ==201 :#line:689
            print (f"[+] MemberscreeningBypassed {O000000O0O0OOOO00}")#line:690
            return #line:691
        else :#line:692
            print (f"[!] Bypassが出来ませんでした {O000000O0O0OOOO00}")#line:693
            return #line:694
    except Exception as O0O0OO00OOO0OOOO0 :#line:695
        print (f"[!] エラーが発生しました。{O0O0OO00OOO0OOOO0}")#line:696
session =requests .Session ()#line:698
def reactionput (OO0O0OOO0OOO0O0O0 ,O000OOOO00OOOO00O ,OO0O000OOOO00O0O0 ,OO0000O0OOOOO0000 ,proxy =None ):#line:701
    OO000OOO0OO00OOOO =get_session (proxy )#line:702
    OOOO00O0000OO0OO0 =get_headers (OO000OOO0OO00OOOO )#line:703
    OOOO00O0000OO0OO0 ["Authorization"]=OO0O0OOO0OOO0O0O0 #line:704
    OO0000O0OOOOO0000 =requests .utils .quote (OO0000O0OOOOO0000 )#line:706
    O00OO0000000OOOO0 =OO000OOO0OO00OOOO .put (f"https://discord.com/api/v9/channels/{O000OOOO00OOOO00O}/messages/{OO0O000OOOO00O0O0}/reactions/{OO0000O0OOOOO0000}/%40me?location=Message&type=0",headers =OOOO00O0000OO0OO0 )#line:710
    if O00OO0000000OOOO0 .status_code in [200 ,204 ]:#line:711
        print (f"[+] Reaction '{OO0000O0OOOOO0000}' added successfully to message {OO0O000OOOO00O0O0}")#line:712
    elif O00OO0000000OOOO0 .status_code ==429 :#line:713
        print ("[-] Rate limited. Please wait before retrying.")#line:714
        O0OOO0000OO0O0OO0 =O00OO0000000OOOO0 .json ().get ("retry_after",1 )#line:715
        time .sleep (O0OOO0000OO0O0OO0 )#line:716
    elif O00OO0000000OOOO0 .status_code ==401 :#line:717
        print ("[-] Invalid or expired token.")#line:718
    else :#line:719
        print (f"[!] Error occurred: {O00OO0000000OOOO0.status_code}")#line:720
def generatexspandua (OO00OO00OO00O00O0 ):#line:723
  O00O0OO00000O0O0O =["Android","Windows","Macintosh"]#line:724
  OOOOO0OO0000O0O0O =random .choice (O00O0OO00000O0O0O )#line:725
  if OOOOO0OO0000O0O0O =="Macintosh":#line:726
    OO0OOO00000OOO0O0 =f"Intel Mac OS X 10_15_"+str (random .randint (5 ,7 ))#line:727
    O0000000O0OO0OOOO ="Macintosh; Intel Mac OS X "+OO0OOO00000OOO0O0 #line:728
    O0OO00OOOOO0O0O0O ="x86_64"#line:729
  if OOOOO0OO0000O0O0O =="Windows":#line:730
    OO0OOO00000OOO0O0 =f'{random.choice([6.0,10.0,11.0])}'#line:731
    O0000000O0OO0OOOO ="Windows NT "+OO0OOO00000OOO0O0 +" Win64; x64"#line:732
    O0OO00OOOOO0O0O0O ="x86_64"#line:733
  if OOOOO0OO0000O0O0O =="Android":#line:734
    OO0OOO00000OOO0O0 ="13"#line:735
    O0000000O0OO0OOOO =f"Linux; Android 13; Pixel 6a"#line:736
    O0OO00OOOOO0O0O0O ="aarch64"#line:737
  OO000O000O000000O ={"os":OOOOO0OO0000O0O0O ,"browser":"Discord Client","release_channel":"stable","client_version":"1.0.9001","os_version":OO0OOO00000OOO0O0 ,"os_arch":O0OO00OOOOO0O0O0O ,"system_locale":"ja-JP","client_build_number":OO00OO00OO00O00O0 ,"client_event_source":None ,"design_id":0 }#line:738
  OOO0000000000O000 =f"Mozilla/5.0 ({O0000000O0OO0OOOO}) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/112.0.0.0 Electron/9.3.5 Safari/537.36"#line:739
  return base64 .b64encode (json .dumps (OO000O000O000000O ,separators =(',',':')).encode ()).decode (),OOO0000000000O000 #line:740
import base64 #line:742
def nickchanger ():#line:745
    try :#line:746
        with open ("token.txt")as O0O0000O0O0000O0O :#line:747
            OOO0000OO00OO0O00 =[OOOOOOOO0OO000OO0 .strip ()for OOOOOOOO0OO000OO0 in O0O0000O0O0000O0O .readlines ()if OOOOOOOO0OO000OO0 .strip ()]#line:748
    except (FileNotFoundError ,KeyError ):#line:749
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:750
        return #line:751
    OOOOOO0O0O0O00000 =input ("Server ID?: ").strip ()#line:753
    O00O000O00O000OOO =input ("Nickname?: ").strip ()#line:754
    OO0O000OO0O0O0O00 =input ("Delay (in seconds)?: ").strip ()#line:755
    try :#line:757
        OO0O000OO0O0O0O00 =float (OO0O000OO0O0O0O00 )#line:758
        if OO0O000OO0O0O0O00 <0 :#line:759
            raise ValueError #line:760
    except ValueError :#line:761
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:762
        OO0O000OO0O0O0O00 =1.0 #line:763
    for OOO0OOOOOO0O0OOOO in OOO0000OO00OO0O00 :#line:765
        OO0000OOO0OOOO0O0 ={"Authorization":OOO0OOOOOO0O0OOOO ,"accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"}#line:770
        OO0000OOOOOOO0O0O ={"nick":O00O000O00O000OOO }#line:771
        OOOOOOO0OO0O0OOO0 =requests .patch (f"https://discord.com/api/v9/guilds/{OOOOOO0O0O0O00000}/members/@me",headers =OO0000OOO0OOOO0O0 ,json =OO0000OOOOOOO0O0O )#line:772
        if OOOOOOO0OO0O0OOO0 .status_code ==200 :#line:774
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [+] Nickname changed to '{O00O000O00O000OOO}' successfully for token {OOO0OOOOOO0O0OOOO}.{colorama.Fore.RESET}")#line:775
        elif OOOOOOO0OO0O0OOO0 .status_code ==429 :#line:776
            print (f"{colorama.Fore.RED}    [!] Rate limited. Please wait before retrying for token {OOO0OOOOOO0O0OOOO}.{colorama.Fore.RESET}")#line:777
            OO0O0000000000000 =OOOOOOO0OO0O0OOO0 .json ().get ("retry_after",1 )#line:778
            time .sleep (OO0O0000000000000 )#line:779
        else :#line:780
            print (f"{colorama.Fore.RED}    [!] Error occurred: {OOOOOOO0OO0O0OOO0.status_code} for token {OOO0OOOOOO0O0OOOO}.{colorama.Fore.RESET}")#line:781
        time .sleep (OO0O000OO0O0O0O00 )#line:783
import json ,websocket ,threading ,tls_client ,random ,time #line:787
session =tls_client .Session (client_identifier ="chrome112",random_tls_extension_order =True )#line:789
class Utils :#line:791
    @staticmethod #line:792
    def rangeCorrector (OOO0O000000000000 ):#line:793
        if [0 ,99 ]not in OOO0O000000000000 :#line:794
            OOO0O000000000000 .insert (0 ,[0 ,99 ])#line:795
        return OOO0O000000000000 #line:796
    @staticmethod #line:798
    def getRanges (O00O00OOOOO0OOOO0 ,O0O00O000OO000OO0 ,OOOOO000000O00000 ):#line:799
        OOO000OOO0000OO0O =int (O00O00OOOOO0OOOO0 *O0O00O000OO000OO0 )#line:800
        OOOO0OOO0OOO000OO =[[OOO000OOO0000OO0O ,OOO000OOO0000OO0O +99 ]]#line:801
        if OOOOO000000O00000 >OOO000OOO0000OO0O +99 :#line:802
            OOOO0OOO0OOO000OO .append ([OOO000OOO0000OO0O +100 ,OOO000OOO0000OO0O +199 ])#line:803
        return Utils .rangeCorrector (OOOO0OOO0OOO000OO )#line:804
    @staticmethod #line:806
    def parseGuildMemberListUpdate (OO0OO0OOOOO0000O0 ):#line:807
        O0OOO0OO0OO00OOOO ={"online_count":OO0OO0OOOOO0000O0 ["d"]["online_count"],"member_count":OO0OO0OOOOO0000O0 ["d"]["member_count"],"id":OO0OO0OOOOO0000O0 ["d"]["id"],"guild_id":OO0OO0OOOOO0000O0 ["d"]["guild_id"],"hoisted_roles":OO0OO0OOOOO0000O0 ["d"]["groups"],"types":[],"locations":[],"updates":[],}#line:817
        for O0OOOO0O0000000OO in OO0OO0OOOOO0000O0 ["d"]["ops"]:#line:819
            O0OOO0OO0OO00OOOO ["types"].append (O0OOOO0O0000000OO ["op"])#line:820
            if O0OOOO0O0000000OO ["op"]in ("SYNC","INVALIDATE"):#line:821
                O0OOO0OO0OO00OOOO ["locations"].append (O0OOOO0O0000000OO ["range"])#line:822
                if O0OOOO0O0000000OO ["op"]=="SYNC":#line:823
                    O0OOO0OO0OO00OOOO ["updates"].append (O0OOOO0O0000000OO ["items"])#line:824
                else :#line:825
                    O0OOO0OO0OO00OOOO ["updates"].append ([])#line:826
            elif O0OOOO0O0000000OO ["op"]in ("INSERT","UPDATE","DELETE"):#line:827
                O0OOO0OO0OO00OOOO ["locations"].append (O0OOOO0O0000000OO ["index"])#line:828
                if O0OOOO0O0000000OO ["op"]=="DELETE":#line:829
                    O0OOO0OO0OO00OOOO ["updates"].append ([])#line:830
                else :#line:831
                    O0OOO0OO0OO00OOOO ["updates"].append (O0OOOO0O0000000OO ["item"])#line:832
        return O0OOO0OO0OO00OOOO #line:833
class DiscordSocket (websocket .WebSocketApp ):#line:835
    def __init__ (O00O0OO0O0O0OOOOO ,OOO0OO0OOOOO0O0OO ,O0OOOOOO00OOOOOO0 ,OOO0O00OO00O00OO0 ):#line:836
        O00O0OO0O0O0OOOOO .token =OOO0OO0OOOOO0O0OO #line:837
        O00O0OO0O0O0OOOOO .guild_id =O0OOOOOO00OOOOOO0 #line:838
        O00O0OO0O0O0OOOOO .channel_id =OOO0O00OO00O00OO0 #line:839
        O00O0OO0O0O0OOOOO .socket_headers ={"Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","Cache-Control":"no-cache","Pragma":"no-cache","Sec-WebSocket-Extensions":"permessage-deflate; client_max_window_bits","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",}#line:847
        super ().__init__ ("wss://gateway.discord.gg/?encoding=json&v=9",header =O00O0OO0O0O0OOOOO .socket_headers ,on_open =lambda OO000OO0OOOOO000O :O00O0OO0O0O0OOOOO .sock_open (OO000OO0OOOOO000O ),on_message =lambda O0OO000O0O00O0OO0 ,OO0O0OOO0OO00O0OO :O00O0OO0O0O0OOOOO .sock_message (O0OO000O0O00O0OO0 ,OO0O0OOO0OO00O0OO ),on_close =lambda O0OOOOO00OO000000 ,OOO0O0OOOO0OO0O00 ,OO0OOOOO00OO0000O :O00O0OO0O0O0OOOOO .sock_close (O0OOOOO00OO000000 ,OOO0O0OOOO0OO0O00 ,OO0OOOOO00OO0000O ),)#line:856
        O00O0OO0O0O0OOOOO .endScraping =False #line:858
        O00O0OO0O0O0OOOOO .guilds ={}#line:859
        O00O0OO0O0O0OOOOO .members ={}#line:860
        O00O0OO0O0O0OOOOO .ranges =[[0 ,0 ]]#line:861
        O00O0OO0O0O0OOOOO .lastRange =0 #line:862
        O00O0OO0O0O0OOOOO .packets_recv =0 #line:863
    def run (O0O00O0OO0O000OO0 ):#line:865
        O0O00O0OO0O000OO0 .run_forever ()#line:866
        return O0O00O0OO0O000OO0 .members #line:867
    def scrapeUsers (O000O0O00000OOO00 ):#line:869
        if not O000O0O00000OOO00 .endScraping :#line:870
            O000O0O00000OOO00 .send ('{"op":14,"d":{"guild_id":"'+O000O0O00000OOO00 .guild_id +'","typing":true,"activities":true,"threads":true,"channels":{"'+O000O0O00000OOO00 .channel_id +'":'+json .dumps (O000O0O00000OOO00 .ranges )+"}}}")#line:879
    def sock_open (OOO00000O0OOO0OO0 ,O0OOOO00OO0000OO0 ):#line:881
        OOO00000O0OOO0OO0 .send ('{"op":2,"d":{"token":"'+OOO00000O0OOO0OO0 .token +'","capabilities":125,"properties":{"os":"Windows NT","browser":"Chrome","device":"","system_locale":"it-IT","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36","browser_version":"119.0","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":103981,"client_event_source":null},"presence":{"status":"online","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}')#line:886
    def heartbeatThread (OOOO0OOOO0O0000O0 ,OOO0O00O00000OOO0 ):#line:888
        try :#line:889
            while True :#line:890
                OOOO0OOOO0O0000O0 .send ('{"op":1,"d":'+str (OOOO0OOOO0O0000O0 .packets_recv )+"}")#line:891
                time .sleep (OOO0O00O00000OOO0 )#line:892
        except Exception as OOOO0OO0O00OO0O0O :#line:893
            pass #line:894
    def sock_message (OOO00OOO0OOOOO00O ,O000O00OOOOOO0O0O ,O0000O0OOO0OOOOO0 ):#line:896
        O0000O000O0000000 =json .loads (O0000O0OOO0OOOOO0 )#line:897
        if O0000O000O0000000 is None :#line:898
            return #line:899
        if O0000O000O0000000 ["op"]!=11 :#line:900
            OOO00OOO0OOOOO00O .packets_recv +=1 #line:901
        if O0000O000O0000000 ["op"]==10 :#line:902
            threading .Thread (target =OOO00OOO0OOOOO00O .heartbeatThread ,args =(O0000O000O0000000 ["d"]["heartbeat_interval"]/1000 ,),daemon =True ,).start ()#line:907
        if O0000O000O0000000 ["t"]=="READY":#line:908
            for OOOO0OOO00OO0O000 in O0000O000O0000000 ["d"]["guilds"]:#line:909
                OOO00OOO0OOOOO00O .guilds [OOOO0OOO00OO0O000 ["id"]]={"member_count":OOOO0OOO00OO0O000 ["member_count"]}#line:910
        if O0000O000O0000000 ["t"]=="READY_SUPPLEMENTAL":#line:911
            OOO00OOO0OOOOO00O .ranges =Utils .getRanges (0 ,100 ,OOO00OOO0OOOOO00O .guilds [OOO00OOO0OOOOO00O .guild_id ]["member_count"])#line:914
            OOO00OOO0OOOOO00O .scrapeUsers ()#line:915
        elif O0000O000O0000000 ["t"]=="GUILD_MEMBER_LIST_UPDATE":#line:916
            O00OOOO00OO0O00OO =Utils .parseGuildMemberListUpdate (O0000O000O0000000 )#line:917
            if O00OOOO00OO0O00OO ["guild_id"]==OOO00OOO0OOOOO00O .guild_id and ("SYNC"in O00OOOO00OO0O00OO ["types"]or "UPDATE"in O00OOOO00OO0O00OO ["types"]):#line:921
                for O0OO0O0O000O000O0 ,O00O000OOOO000OO0 in enumerate (O00OOOO00OO0O00OO ["types"]):#line:922
                    if O00O000OOOO000OO0 =="SYNC":#line:923
                        if len (O00OOOO00OO0O00OO ["updates"][O0OO0O0O000O000O0 ])==0 :#line:924
                            OOO00OOO0OOOOO00O .endScraping =True #line:925
                            break #line:926
                        for O000OO0O000OO000O in O00OOOO00OO0O00OO ["updates"][O0OO0O0O000O000O0 ]:#line:928
                            if "member"in O000OO0O000OO000O :#line:929
                                O000OO00O0O000O0O =O000OO0O000OO000O ["member"]#line:930
                                OO0OO0OOOOOOO00OO ={"tag":O000OO00O0O000O0O ["user"]["username"]+"#"+O000OO00O0O000O0O ["user"]["discriminator"],"id":O000OO00O0O000O0O ["user"]["id"],}#line:936
                                if not O000OO00O0O000O0O ["user"].get ("bot"):#line:937
                                    OOO00OOO0OOOOO00O .members [O000OO00O0O000O0O ["user"]["id"]]=OO0OO0OOOOOOO00OO #line:938
                    elif O00O000OOOO000OO0 =="UPDATE":#line:940
                        for O000OO0O000OO000O in O00OOOO00OO0O00OO ["updates"][O0OO0O0O000O000O0 ]:#line:941
                            if "member"in O000OO0O000OO000O :#line:942
                                O000OO00O0O000O0O =O000OO0O000OO000O ["member"]#line:943
                                OO0OO0OOOOOOO00OO ={"tag":O000OO00O0O000O0O ["user"]["username"]+"#"+O000OO00O0O000O0O ["user"]["discriminator"],"id":O000OO00O0O000O0O ["user"]["id"],}#line:949
                                if not O000OO00O0O000O0O ["user"].get ("bot"):#line:950
                                    OOO00OOO0OOOOO00O .members [O000OO00O0O000O0O ["user"]["id"]]=OO0OO0OOOOOOO00OO #line:951
                    OOO00OOO0OOOOO00O .lastRange +=1 #line:953
                    OOO00OOO0OOOOO00O .ranges =Utils .getRanges (OOO00OOO0OOOOO00O .lastRange ,100 ,OOO00OOO0OOOOO00O .guilds [OOO00OOO0OOOOO00O .guild_id ]["member_count"])#line:956
                    time .sleep (0.45 )#line:957
                    OOO00OOO0OOOOO00O .scrapeUsers ()#line:958
            if OOO00OOO0OOOOO00O .endScraping :#line:960
                OOO00OOO0OOOOO00O .close ()#line:961
    def sock_close (OOOOO00OOO0O000O0 ,OO0OOOO0OOO00O00O ,O000OO00OOOOOOO0O ,O0O00O000000O0OOO ):#line:963
        pass #line:964
def scrape (O0O00O0OOOO0OOOOO ,OO000OOO0O00O0000 ,O0OO00O0OOOO0O00O ):#line:966
    OO00000O00O0OOO00 =DiscordSocket (O0O00O0OOOO0OOOOO ,OO000OOO0O00O0000 ,O0OO00O0OOOO0O00O )#line:967
    return OO00000O00O0OOO00 .run ()#line:968
def member_scrape (OO0OOO00O0OO00OOO ,OOOO00O00O000O0O0 ,O000OO0OOO0O0OO00 ):#line:970
    OOO00O0000OOOO00O =[]#line:971
    for OOOOO0O0000O00OO0 in OO0OOO00O0OO00OOO :#line:972
        OOO0O0OOO0OO000O0 ={"Authorization":OOOOO0O0000O00OO0 ,"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}#line:973
        O000000OOOOOO0O0O =session .get (f"https://canary.discord.com/api/v9/guilds/{OOOO00O00O000O0O0}",headers =OOO0O0OOO0OO000O0 )#line:974
        if O000000OOOOOO0O0O .status_code ==200 :#line:975
            OOO00O0000OOOO00O .append (OOOOO0O0000O00OO0 )#line:976
            break #line:977
    if not OOO00O0000OOOO00O :#line:978
        print ("missing access")#line:979
    OOOOO0O0000O00OO0 =random .choice (OOO00O0000OOOO00O )#line:981
    O00O0O00O0000O0O0 =scrape (OOOOO0O0000O00OO0 ,OOOO00O00O000O0O0 ,O000OO0OOO0O0OO00 )#line:982
    O00OOO0O00OO0000O =[f"<@{O0000O0O00000O0O0}>"for O0000O0O00000O0O0 in [int (O00O0O000OOO0O0OO )for O00O0O000OOO0O0OO in O00O0O00O0000O0O0 .keys ()]]#line:983
    print (f"[SUCCESS] {len(O00OOO0O00OO0000O)} scraped members")#line:984
    return O00OOO0O00OO0000O #line:985
def spammer_menu ():#line:987
    try :#line:988
        with open ("token.txt")as O0000OOO0O00000O0 :#line:989
            OO0O000O000000O00 =[OO0O00O0O000OO0O0 .strip ()for OO0O00O0O000OO0O0 in O0000OOO0O00000O0 .readlines ()if OO0O00O0O000OO0O0 .strip ()]#line:990
    except (FileNotFoundError ,KeyError ):#line:991
        print (f"{colorama.Fore.RED}    [!] Error: token.txt file not found or no valid tokens!{colorama.Fore.RESET}")#line:992
        return #line:993
    OOOO0OOOO0OOO00O0 =input ("Server ID?: ").strip ()#line:995
    OOO0OOOOO0O000OOO =input ("Message?: ").strip ()#line:996
    O0O000OOOO0OOO00O =input ("Random mention (True/False)?: ").strip ().lower ()=='true'#line:997
    OOOO0000000O00000 =input ("Delay between messages (in seconds)?: ").strip ()#line:998
    O000000OO000O0O00 =input ("Number of messages to send?: ").strip ()#line:999
    O0O0O0OO0OOOO0O0O =input ("Blacklist User IDs (comma-separated) (Leave blank to skip)?: ").strip ().split (',')#line:1000
    O0O0O0OO0OOOO0O0O =[f"<@{OO0OOOO00000O0O0O.strip()}>"for OO0OOOO00000O0O0O in O0O0O0OO0OOOO0O0O if OO0OOOO00000O0O0O .strip ()]#line:1001
    try :#line:1003
        OOOO0000000O00000 =float (OOOO0000000O00000 )#line:1004
        if OOOO0000000O00000 <0 :#line:1005
            raise ValueError #line:1006
    except ValueError :#line:1007
        print (f"{colorama.Fore.RED}    [!] Invalid delay. Using default delay of 1 second.{colorama.Fore.RESET}")#line:1008
        OOOO0000000O00000 =1.0 #line:1009
    try :#line:1011
        O000000OO000O0O00 =int (O000000OO000O0O00 )#line:1012
        if O000000OO000O0O00 <=0 :#line:1013
            raise ValueError #line:1014
    except ValueError :#line:1015
        print (f"{colorama.Fore.RED}    [!] Invalid send count. Using default count of 1.{colorama.Fore.RESET}")#line:1016
        O000000OO000O0O00 =1 #line:1017
    OO000O0OOOO0OOOO0 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:1019
    if OO000O0OOOO0OOOO0 =='2':#line:1020
        OO0O000O000O00OO0 =input ("Enter Channel IDs (comma-separated)?: ").strip ().split (',')#line:1021
        OO0O000O000O00OO0 =[O00000OO0OO0O0OO0 .strip ()for O00000OO0OO0O0OO0 in OO0O000O000O00OO0 if O00000OO0OO0O0OO0 .strip ()]#line:1022
    else :#line:1023
        OO0O000O000O00OO0 =fetch_channels (OO0O000O000000O00 [0 ],OOOO0OOOO0OOO00O0 )#line:1024
    O00OOOOO000O00O0O =None #line:1026
    spammer (OO0O000O000000O00 ,OOOO0OOOO0OOO00O0 ,OO0O000O000O00OO0 ,OOO0OOOOO0O000OOO ,O0O000OOOO0OOO00O ,O0O0O0OO0OOOO0O0O ,O00OOOOO000O00O0O ,O000000OO000O0O00 )#line:1028
    input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:1031
def buildnumget (OOOOOO0O000O0OO00 ):#line:1033
  O000OO00OOO0OOO0O =OOOOOO0O000O0OO00 .get ('https://discord.com/login',headers ={'Accept-Encoding':'gzip, deflate'},timeout =7 )#line:1034
  O000OO0000000OO00 =O000OO00OOO0OOO0O .text #line:1035
import discum #line:1037
import random #line:1038
import time #line:1039
def userget (O0O00O0OO0000OO0O ,OOOO000OO00O000OO ,OOO00000O00000O00 ):#line:1041
    OO0O0O0O0OO0000OO =[]#line:1042
    O0OOOO000O00OO00O =discum .Client (token =O0O00O0OO0000OO0O ,log =False )#line:1043
    def O0OO0O0000000OO0O (O0OOO000OO00000O0 ):#line:1045
        if O0OOOO000O00OO00O .gateway .finishedMemberFetching (OOOO000OO00O000OO ):#line:1046
            O000O00O0OOO00O0O =len (O0OOOO000O00OO00O .gateway .session .guild (OOOO000OO00O000OO ).members )#line:1047
            print (str (O000O00O0OOO00O0O )+' members fetched')#line:1048
            O0OOOO000O00OO00O .gateway .removeCommand ({'function':O0OO0O0000000OO0O ,'params':{}})#line:1049
            O0OOOO000O00OO00O .gateway .close ()#line:1050
    def O0OOO0OO0O0O0O0O0 (O00O0O00O0OO00OOO ,OO0OO00O000O00OOO ):#line:1052
        O0OOOO000O00OO00O .gateway .fetchMembers (O00O0O00O0OO00OOO ,OO0OO00O000O00OOO ,keep ='all',wait =1 )#line:1053
        O0OOOO000O00OO00O .gateway .command ({'function':O0OO0O0000000OO0O ,'params':{}})#line:1054
        O0OOOO000O00OO00O .gateway .run ()#line:1055
        O0OOOO000O00OO00O .gateway .resetSession ()#line:1056
        return O0OOOO000O00OO00O .gateway .session .guild (O00O0O00O0OO00OOO ).members #line:1057
    O0O0000OOOOO00O00 =O0OOO0OO0O0O0O0O0 (OOOO000OO00O000OO ,OOO00000O00000O00 )#line:1059
    for OOO000OO0OO0O00O0 in O0O0000OOOOO00O00 :#line:1060
        if OOO000OO0OO0O00O0 not in OO0O0O0O0OO0000OO :#line:1061
            OO0O0O0O0OO0000OO .append (f"<@{OOO000OO0OO0O00O0}>")#line:1062
    return OO0O0O0O0OO0000OO #line:1063
def spammer (O0OO00O00OO000OOO ,OOO0O00000O0O0O00 ,O0O0OO0O0OOO0OO00 ,OOO0OOO0000O0O000 ,O00O0O00O00O0OOO0 ,OOO00OOO0OOO0OO0O ,OO00OOO0O0O00OOO0 ,OOO0O00O0OO0OO0OO ):#line:1068
    O0OO000OOO0OOOOOO =get_session (OO00OOO0O0O00OOO0 )#line:1069
    O000000O0O0O0OO00 =0 #line:1070
    OOOO00OO0OO00000O =userget (O0OO00O00OO000OOO [0 ],OOO0O00000O0O0O00 ,O0O0OO0O0OOO0OO00 [0 ])#line:1072
    OOOO00OO0OO00000O =[O00O00OOOOOO0OO0O for O00O00OOOOOO0OO0O in OOOO00OO0OO00000O if O00O00OOOOOO0OO0O not in OOO00OOO0OOO0OO0O ]#line:1075
    for _O00OOO0O0000OO0O0 in range (OOO0O00O0OO0OO0OO ):#line:1077
        OO0O000000OOOOO00 =O0OO00O00OO000OOO [O000000O0O0O0OO00 ]#line:1078
        OO0OO0O0O00O000O0 =get_headers (OO0O000000OOOOO00 )#line:1079
        for OO0000O00OOO00O00 in O0O0OO0O0OOO0OO00 :#line:1080
            O00OOO0O0O00O0O00 =OOO0OOO0000O0O000 #line:1081
            if O00O0O00O00O0OOO0 and OOOO00OO0OO00000O :#line:1082
                OOOO0000OO00OO00O =random .choice (OOOO00OO0OO00000O )#line:1083
                O00OOO0O0O00O0O00 +=f" {OOOO0000OO00OO00O}"#line:1084
            OO00O0OO00000OO0O =O0OO000OOO0OOOOOO .post (f"https://discord.com/api/v9/channels/{OO0000O00OOO00O00}/messages",json ={"content":O00OOO0O0O00O0O00 },headers =OO0OO0O0O00O000O0 )#line:1086
            if OO00O0OO00000OO0O .status_code ==200 :#line:1087
                print (f"200 message sent: {OO0O000000OOOOO00}")#line:1088
            elif OO00O0OO00000OO0O .status_code ==429 :#line:1089
                print (f"429 rate limit: {OO0O000000OOOOO00}")#line:1090
                O0O00OO000O0O0000 =OO00O0OO00000OO0O .json ().get ("retry_after",1 )#line:1091
                time .sleep (O0O00OO000O0O0000 )#line:1092
            elif OO00O0OO00000OO0O .status_code ==401 :#line:1093
                print (f"401 unknown token: {OO0O000000OOOOO00}")#line:1094
            else :#line:1095
                print (f"error: {OO0O000000OOOOO00}")#line:1096
        O000000O0O0O0OO00 =(O000000O0O0O0OO00 +1 )%len (O0OO00O00OO000OOO )#line:1098
        time .sleep (1 )#line:1099
import requests #line:1103
import base64 #line:1104
import colorama #line:1105
import time #line:1106
def add_emojis_from_files ():#line:1108
    try :#line:1109
        with open ("emojiname.txt")as O00O0OOOO000OOOO0 ,open ("emojiurl.txt")as O00OO0OO00O0OO000 :#line:1110
            OO0OO000O00O0OOO0 =[O00O0O0O0OOOOO00O .strip ()for O00O0O0O0OOOOO00O in O00O0OOOO000OOOO0 .read ().split (',')if O00O0O0O0OOOOO00O .strip ()]#line:1111
            OOOO00000000OOO00 =[OOO00O0O0OO0OO0O0 .strip ()for OOO00O0O0OO0OO0O0 in O00OO0OO00O0OO000 .read ().split (',')if OOO00O0O0OO0OO0O0 .strip ()]#line:1112
    except FileNotFoundError as O00OOOOO0OO0OO0OO :#line:1113
        print (f"{colorama.Fore.RED}    [!] Error: {str(O00OOOOO0OO0OO0OO)}{colorama.Fore.RESET}")#line:1114
        return #line:1115
    if len (OO0OO000O00O0OOO0 )!=len (OOOO00000000OOO00 ):#line:1117
        print (f"{colorama.Fore.RED}    [!] Error: The number of emoji names and URLs do not match!{colorama.Fore.RESET}")#line:1118
        return #line:1119
    try :#line:1121
        with open ("token.txt")as OOOO0000O00OO0O00 :#line:1122
            O0000O00O0000OO0O =[O0O00O0OOO0OOO0OO .strip ()for O0O00O0OOO0OOO0OO in OOOO0000O00OO0O00 .readlines ()if O0O00O0OOO0OOO0OO .strip ()]#line:1123
    except FileNotFoundError as O00OOOOO0OO0OO0OO :#line:1124
        print (f"{colorama.Fore.RED}    [!] Error: {str(O00OOOOO0OO0OO0OO)}{colorama.Fore.RESET}")#line:1125
        return #line:1126
    O0O000O0O0OO0OOOO =input ("Enter the Guild ID: ").strip ()#line:1128
    O0OOOO0OOOOOO0OO0 =input ("Enter the rate limit between requests (in seconds): ").strip ()#line:1129
    try :#line:1131
        O0OOOO0OOOOOO0OO0 =float (O0OOOO0OOOOOO0OO0 )#line:1132
        if O0OOOO0OOOOOO0OO0 <0 :#line:1133
            raise ValueError #line:1134
    except ValueError :#line:1135
        print (f"{colorama.Fore.RED}    [!] Invalid rate limit. Using default rate limit of 5 seconds.{colorama.Fore.RESET}")#line:1136
        O0OOOO0OOOOOO0OO0 =5.0 #line:1137
    OO00O000O0O0O0OO0 =set ()#line:1139
    for O0OOO000O000O0000 in O0000O00O0000OO0O :#line:1141
        OOOOO0O0000000OOO ={'Authorization':O0OOO000O000O0000 ,'Content-Type':'application/json'}#line:1145
        O0OOO0O0OOOOO0OO0 =requests .get (f"https://discord.com/api/v9/guilds/{O0O000O0O0OO0OOOO}/emojis",headers =OOOOO0O0000000OOO )#line:1148
        if O0OOO0O0OOOOO0OO0 .status_code ==200 :#line:1149
            O0000OOO00O0OOOOO =O0OOO0O0OOOOO0OO0 .json ()#line:1150
            for O00O0OO0OOO000OOO in O0000OOO00O0OOOOO :#line:1151
                OO00O000O0O0O0OO0 .add (O00O0OO0OOO000OOO ['name'])#line:1152
        else :#line:1153
            print (f"{colorama.Fore.RED}    [!] Error fetching existing emojis: {O0OOO0O0OOOOO0OO0.status_code} - {O0OOO0O0OOOOO0OO0.text}{colorama.Fore.RESET}")#line:1154
            continue #line:1155
    for OO000O000OOOO0O0O ,O000O0OOOO00O000O in zip (OO0OO000O00O0OOO0 ,OOOO00000000OOO00 ):#line:1157
        if OO000O000OOOO0O0O in OO00O000O0O0O0OO0 :#line:1158
            print (f"{colorama.Fore.YELLOW}    [*] Emoji '{OO000O000OOOO0O0O}' already exists. Skipping...{colorama.Fore.RESET}")#line:1159
            continue #line:1160
        for O0OOO000O000O0000 in O0000O00O0000OO0O :#line:1162
            try :#line:1163
                O0OOO0O0OOOOO0OO0 =requests .get (O000O0OOOO00O000O )#line:1164
                O0OOO0O0OOOOO0OO0 .raise_for_status ()#line:1165
                OO00000OOO00O00O0 =O0OOO0O0OOOOO0OO0 .content #line:1166
                OO000O0OOO0OO000O =base64 .b64encode (OO00000OOO00O00O0 ).decode ('utf-8')#line:1167
                O0000OOOO00OO00O0 ={'name':OO000O000OOOO0O0O ,'image':f"data:image/png;base64,{OO000O0OOO0OO000O}"}#line:1172
                OOOOO0O0000000OOO ={'Authorization':O0OOO000O000O0000 ,'Content-Type':'application/json'}#line:1177
                O0000OOOO000O0OO0 =requests .post (f"https://discord.com/api/v9/guilds/{O0O000O0O0OO0OOOO}/emojis",headers =OOOOO0O0000000OOO ,json =O0000OOOO00OO00O0 )#line:1179
                if O0000OOOO000O0OO0 .status_code ==201 :#line:1180
                    print (f"{colorama.Fore.GREEN}    [+] Successfully added emoji '{OO000O000OOOO0O0O}' with token {O0OOO000O000O0000}{colorama.Fore.RESET}")#line:1181
                    OO00O000O0O0O0OO0 .add (OO000O000OOOO0O0O )#line:1182
                    break #line:1183
                else :#line:1184
                    print (f"{colorama.Fore.RED}    [!] Failed to add emoji '{OO000O000OOOO0O0O}' with token {O0OOO000O000O0000}: {O0000OOOO000O0OO0.status_code} - {O0000OOOO000O0OO0.text}{colorama.Fore.RESET}")#line:1185
                time .sleep (O0OOOO0OOOOOO0OO0 )#line:1187
            except Exception as O00OOOOO0OO0OO0OO :#line:1188
                print (f"{colorama.Fore.RED}    [!] Error adding emoji '{OO000O000OOOO0O0O}' with token {O0OOO000O000O0000}: {str(O00OOOOO0OO0OO0OO)}{colorama.Fore.RESET}")#line:1189
import random #line:1191
import requests #line:1192
import time #line:1193
def pollspammer (O0O00O0O0OOOO0OOO ,O00O0OOOOOOO0O000 ,OO00OOOOO00O00O00 ,OO0O0O0OOO0O0O00O ,O00O0000O00O0O0OO ,O0O00OO0O00O0000O ,OOOOO00O0OO0O000O ,OO000O000O000O00O ,OOOOO000O000O00OO ,O0OO00OO0000OO0O0 ,O00OOO0OOOOO00O00 ):#line:1197
    OO00OOOOOO0OO0O00 =get_session ()#line:1198
    O0OO00O0O0O0000O0 =0 #line:1199
    OO00OOO0OOOOO0OOO =userget (O0O00O0O0OOOO0OOO [0 ],O00O0OOOOOOO0O000 ,OO00OOOOO00O00O00 [0 ])#line:1201
    OO00OOO0OOOOO0OOO =[O000O00000000O0OO for O000O00000000O0OO in OO00OOO0OOOOO0OOO if O000O00000000O0OO not in OOOOO000O000O00OO ]#line:1204
    for _OOOO0O0OO00OOOO0O in range (O0OO00OO0000OO0O0 ):#line:1206
        for OOOO00OO000OO00OO in OO00OOOOO00O00O00 :#line:1207
            OOO0O0OOO0O0O0000 =O0O00O0O0OOOO0OOO [O0OO00O0O0O0000O0 ]#line:1208
            O00OO0OOO0OOOOOO0 =get_headers (OOO0O0OOO0O0O0000 )#line:1209
            if OOOOO00O0OO0O000O and OO00OOO0OOOOO0OOO :#line:1212
                O000O00O0000OOO0O =random .choice (OO00OOO0OOOOO0OOO )#line:1213
                O0O0O0OOOO0O0OO0O ={"content":f"{OO000O000O000O00O} {O000O00O0000OOO0O}","tts":False ,"nonce":str (random .randint (10 **17 ,10 **18 -1 ))}#line:1218
                OO0O0OO00OO0O0O0O =OO00OOOOOO0OO0O00 .post (f"https://discord.com/api/v9/channels/{OOOO00OO000OO00OO}/messages",json =O0O0O0OOOO0O0OO0O ,headers =O00OO0OOO0OOOOOO0 )#line:1219
                if OO0O0OO00OO0O0O0O .status_code !=200 :#line:1220
                    print (f"Failed to send mention: {OO0O0OO00OO0O0O0O.status_code} - {OO0O0OO00OO0O0O0O.text}")#line:1221
            else :#line:1222
                OOOOOO0OO00O00O0O ={"content":f"{OO000O000O000O00O}","tts":False ,"nonce":str (random .randint (10 **17 ,10 **18 -1 ))}#line:1228
                OOOOOO00OOO0OOO00 =OO00OOOOOO0OO0O00 .post (f"https://discord.com/api/v9/channels/{OOOO00OO000OO00OO}/messages",json =OOOOOO0OO00O00O0O ,headers =O00OO0OOO0OOOOOO0 )#line:1229
                if OOOOOO00OOO0OOO00 .status_code !=200 :#line:1230
                    print (f"Failed to send message: {OOOOOO00OOO0OOO00.status_code} - {OOOOOO00OOO0OOO00.text}")#line:1231
            time .sleep (O00OOO0OOOOO00O00 )#line:1233
            OO0O000O0000OO00O =[{"poll_media":{"text":O0O0OOOO00O000O00 .strip ()}}for O0O0OOOO00O000O00 in O00O0000O00O0O0OO .split (',')]#line:1236
            O00O0OO0000OOO000 ={"mobile_network_type":"unknown","content":"","nonce":str (random .randint (10 **17 ,10 **18 -1 )),"tts":False ,"flags":0 ,"poll":{"question":{"text":OO0O0O0OOO0O0O00O },"answers":OO0O000O0000OO00O ,"allow_multiselect":False ,"duration":O0O00OO0O00O0000O ,"layout_type":1 }}#line:1250
            O0OOOO0O00O00O000 =OO00OOOOOO0OO0O00 .post (f"https://discord.com/api/v9/channels/{OOOO00OO000OO00OO}/messages",json =O00O0OO0000OOO000 ,headers =O00OO0OOO0OOOOOO0 )#line:1252
            if O0OOOO0O00O00O000 .status_code ==200 :#line:1253
                print (f"200 poll message sent: {OOO0O0OOO0O0O0000}")#line:1254
            elif O0OOOO0O00O00O000 .status_code ==429 :#line:1255
                print (f"429 rate limit: {OOO0O0OOO0O0O0000}")#line:1256
                O0O0OOO0O0O000OOO =O0OOOO0O00O00O000 .json ().get ("retry_after",1 )#line:1257
                time .sleep (O0O0OOO0O0O000OOO )#line:1258
            elif O0OOOO0O00O00O000 .status_code ==401 :#line:1259
                print (f"401 unknown token: {OOO0O0OOO0O0O0000}")#line:1260
            else :#line:1261
                print (f"error: {OOO0O0OOO0O0O0000} - {O0OOOO0O00O00O000.status_code}: {O0OOOO0O00O00O000.text}")#line:1262
            O0OO00O0O0O0000O0 =(O0OO00O0O0O0000O0 +1 )%len (O0O00O0O0OOOO0OOO )#line:1264
            time .sleep (O00OOO0OOOOO00O00 )#line:1265
def pollspammermenu ():#line:1268
    with open ("token.txt")as O00OOOOOO0O0OO000 :#line:1269
        O0OO0000OOOOOOOOO =[O00OOO00OOOOOO00O .strip ()for O00OOO00OOOOOO00O in O00OOOOOO0O0OO000 .readlines ()if O00OOO00OOOOOO00O .strip ()]#line:1270
    OOO00OO0OOOOOO00O =input ("Enter Server ID: ").strip ()#line:1272
    OOOOOO000O0000000 =input ("Send to (1) all channels or (2) specific channel(s)?: ").strip ()#line:1273
    if OOOOOO000O0000000 =='2':#line:1274
        OOOOO0O0O0OOOO000 =input ("Enter Channel IDs (comma-separated): ").strip ().split (',')#line:1275
    else :#line:1276
        OOOOO0O0O0OOOO000 =[]#line:1277
        for O00O000OO0OOOO000 in O0OO0000OOOOOOOOO :#line:1278
            try :#line:1279
                OOOOO0O0O0OOOO000 .extend (fetch_channels (O00O000OO0OOOO000 ,OOO00OO0OOOOOO00O ))#line:1280
            except Exception as O00000OO0OO000O0O :#line:1281
                print (f"[!] Failed to fetch channels for token. Error: {O00000OO0OO000O0O}")#line:1282
                continue #line:1283
        random .shuffle (OOOOO0O0O0OOOO000 )#line:1284
    O0OOO0O0O00OO0OOO =input ("Enter poll title: ").strip ()#line:1286
    OO0OOO00000OOOOOO =input ("Enter poll answers (comma-separated): ").strip ()#line:1287
    OO00O0O0OO0OOOO00 =int (input ("Enter poll duration (in hours 1/4/8/24/72/168/336 ): ").strip ())#line:1288
    O0O000OO0000OOOO0 =input ("Do you want to mention random users? (true/false): ").strip ().lower ()=='true'#line:1289
    OOO0OO0O0O0O000O0 =""#line:1290
    if O0O000OO0000OOOO0 :#line:1291
        OOO0OO0O0O0O000O0 =input ("Enter the message to prepend to the mention: ").strip ()#line:1292
    O000O000000O00000 =input ("Enter blacklist user IDs (comma-separated): ").strip ().split (',')#line:1293
    O000O0000O00000OO =int (input ("Enter number of send poll: ").strip ())#line:1294
    OO0O00OOOO00O00OO =float (input ("Enter delay between posts (in seconds): ").strip ())#line:1295
    pollspammer (O0OO0000OOOOOOOOO ,OOO00OO0OOOOOO00O ,OOOOO0O0O0OOOO000 ,O0OOO0O0O00OO0OOO ,OO0OOO00000OOOOOO ,OO00O0O0OO0OOOO00 ,O0O000OO0000OOOO0 ,OOO0OO0O0O0O000O0 ,O000O000000O00000 ,O000O0000O00000OO ,OO0O00OOOO00O00OO )#line:1297
def main ():#line:1300
    colorama .init ()#line:1301
    while True :#line:1302
        logo ()#line:1303
        O00O000O0OO0OO00O =input (f"{colorama.Fore.LIGHTMAGENTA_EX}    [Final] Select an option from above: ")#line:1304
        if O00O000O0OO0OO00O =="0":#line:1306
            update_group_ids ()#line:1307
        elif O00O000O0OO0OO00O =="1":#line:1308
            join_discord_invite ()#line:1309
        elif O00O000O0OO0OO00O =="2":#line:1310
            reaction_spammer ()#line:1311
        elif O00O000O0OO0OO00O =="3":#line:1312
            send_messages_with_mentions ()#line:1313
        elif O00O000O0OO0OO00O =="4":#line:1314
            spammer_menu ()#line:1315
        elif O00O000O0OO0OO00O =="5":#line:1316
            nickchanger ()#line:1317
        elif O00O000O0OO0OO00O =="6":#line:1318
            add_emojis_from_files ()#line:1319
        elif O00O000O0OO0OO00O =="7":#line:1320
            reaction_art ()#line:1321
        elif O00O000O0OO0OO00O =="8":#line:1322
            pollspammermenu ()#line:1323
        elif O00O000O0OO0OO00O =="0":#line:1324
            print (f"{colorama.Fore.LIGHTGREEN_EX}    [*] Exiting the application. Goodbye!{colorama.Fore.RESET}")#line:1325
            break #line:1326
        else :#line:1327
            print (f"{colorama.Fore.RED}    [!] Invalid option selected!{colorama.Fore.RESET}")#line:1328
        input (f"{colorama.Fore.LIGHTCYAN_EX}Press Enter to return to the main menu...{colorama.Fore.RESET}")#line:1330
if __name__ =="__main__":#line:1332
    main ()#line:1333
