from html.parser import HTMLParser
from html.entities import name2codepoint
import os

max_size = 4096
read_size = 0
read_buffer = ""
dest_file = open("ODE_Trimed.txt", "w", encoding="utf-8")

def get_attr(attrs, key):
    for attr in attrs:
        if attr[0] == key:
            return attr[1]
    return None


class MyHTMLParser(HTMLParser): 

    def __init__(self, convert_charrefs=True):
        super().__init__(convert_charrefs=convert_charrefs)
        self.in_tag_em = False
        self.in_tag_h2 = False

    def handle_data(self, data):
        if self.in_tag_em or self.in_tag_h2:
            dest_file.write(data)

    def handle_starttag(self, tag, attrs):
        if tag == "em":
            self.in_tag_em = True
        else:
            if tag == "h2" and get_attr(attrs, "class") == "z2h":
                dest_file.write("----------word\n")
                self.in_tag_h2 = True

    def handle_endtag(self, tag):
        if tag == "em":
            self.in_tag_em = False
            dest_file.write("\n")
        else:
            if tag == "h2":
                self.in_tag_h2 = False
                dest_file.write("\n")
                dest_file.write("----------example\n")


if __name__ == "__main__":
    parser = MyHTMLParser()
    file_size = os.path.getsize("ODE.txt")
    with open("ODE.txt", "r", encoding="utf-8") as f:
        while (True):
            read_buffer = f.read(max_size)
            if read_buffer == "":
                print("\r处理进度:100.00%\n")
                print("Done.")
                break
            parser.feed(read_buffer)
            read_size += len(read_buffer)
            print("\r处理进度:%.2f%%" % (read_size / file_size * 100), end='', flush=True)
    dest_file.close()
