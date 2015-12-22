#!/bin/python3

import urllib.request, re, urllib.parse

mode = "vi_en"
word = ""

while word != " ":
    word = input("Tu tieng viet: ")
    word = urllib.parse.quote(str(word))

    url = "http://vndic.net/m.php?word=%s&dict=%s" % (word, mode)
    htmltag = ("<TABLE.*?>", "</TABLE>", "<TR.*?>", "</TR>", "<TD.*?>", "</TD>", "<IMG.*?>", "</IMG>", "<FONT.*?>", "</FONT>", "<B.*?>", "</B>", "<SPAN.*?>", "</SPAN>")

    try:
        with urllib.request.urlopen(url) as f:
            read_data = f.read().decode("utf-8")

            m = re.search("<span class=thisword>(.*?)*</span>", read_data)
            if m:
                thisword = m.group(0)
                for tag in htmltag:
                    thisword = re.sub(tag.lower(), '', thisword)
                print('\n', thisword)

            m = re.search("<span class=maincontent>(.*?)*</span>", read_data)
            if m:
                maincontent = m.group(0).replace("<br>", "\n").replace("<br />", "\n").replace("</TR>", "\n")
                
                # remove html tag
                for tag in htmltag:
                    maincontent = re.sub(tag, '', maincontent)
                # remove html tag lower case
                for tag in htmltag:
                    maincontent = re.sub(tag.lower(), '', maincontent)
                    
                print(maincontent)
                      
    except urllib.request.URLError as err:
        msg = "url error"


