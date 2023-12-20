import os #line:1
import tkinter as tk #line:4
from tkinter import messagebox #line:5
from tkinter import ttk #line:6
from datetime import datetime ,timedelta #line:7
def clear_files ():#line:8
    O00000O000O00O000 =entry_directory .get ()#line:9
    O0OO00O00OO0O00O0 =entry_extensions .get ().split (',')#line:10
    OO0O000OOO0OO0O00 =entry_date .get ()#line:11
    if not os .path .exists (O00000O000O00O000 ):#line:12
        messagebox .showerror ("Error","Directory does not exist.")#line:13
        return #line:14
    def O0O00000O0O000O0O (OOOO0OO0000OO000O ):#line:15
        return any (OOOO0OO0000OO000O .lower ().endswith (OO0OO0OOOOO0O0OO0 .strip ())for OO0OO0OOOOO0O0OO0 in O0OO00O00OO0O00O0 )#line:16
    try :#line:17
        OOO0O00OOOOO0OOO0 =datetime .strptime (OO0O000OOO0OO0O00 ,'%d/%m/%Y')#line:18
        OOO000O00O000O0OO =OOO0O00OOOOO0OOO0 +timedelta (days =1 )#line:19
    except ValueError :#line:20
        messagebox .showerror ("Error","Invalid date format. Use DD/MM/YYYY.")#line:21
        return #line:22
    for O00OOOO0000O000O0 in os .listdir (O00000O000O00O000 ):#line:23
        O0O000000OOO0O000 =os .path .join (O00000O000O00O000 ,O00OOOO0000O000O0 )#line:24
        if not os .path .isdir (O0O000000OOO0O000 )and not O0O00000O0O000O0O (O0O000000OOO0O000 ):#line:25
            O0O0O00O0O0OO0O0O =datetime .fromtimestamp (os .path .getctime (O0O000000OOO0O000 ))#line:26
            if O0O0O00O0O0OO0O0O <OOO000O00O000O0OO :#line:27
                try :#line:28
                    os .remove (O0O000000OOO0O000 )#line:29
                    text .insert (tk .END ,f"Deleted: {O0O000000OOO0O000}\n")#line:30
                except Exception as O0000OO0000O0O00O :#line:31
                    text .insert (tk .END ,f"Error deleting {O0O000000OOO0O000}: {O0000OO0000O0O00O}\n")#line:32
                    text .see (tk .END )#line:33
root =tk .Tk ()#line:34
root .title ("File Clearer")#line:35
label_directory =tk .Label (root ,text ="Enter the directory path:")#line:36
label_directory .pack ()#line:37
entry_directory =tk .Entry (root )#line:38
entry_directory .pack ()#line:39
label_extensions =tk .Label (root ,text ="Enter safe file extensions and seperate file extentions with a comma (,):")#line:40
label_extensions .pack ()#line:41
entry_extensions =tk .Entry (root )#line:42
entry_extensions .insert (0 ,'.safe')#line:43
entry_extensions .pack ()#line:44
label_date =tk .Label (root ,text ="Enter date (MM/DD/YYYY) to delete files created before:")#line:45
label_date .pack ()#line:46
default_date =datetime .now ().strftime ('%m/%d/%Y')#line:47
entry_date =tk .Entry (root )#line:48
entry_date .insert (0 ,default_date )#line:49
entry_date .pack ()#line:50
button =tk .Button (root ,text ="Clear Files",command =clear_files )#line:51
button .pack ()#line:52
text =tk .Text (root ,height =10 ,width =40 )#line:53
text .pack ()#line:54
root .mainloop ()
