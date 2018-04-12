<<<<<<< Updated upstream
=======
import urllib
print (' #########   C0D3404   ######### \n\n')

pastebin_vars = {'api_dev_key':raw_input('Your API KEY ==>>'),'api_option':'paste','api_paste_code':raw_input("Paste what you want to paste ===>>\n")}
response = urllib.urlopen('http://pastebin.com/api/api_post.php', urllib.urlencode(pastebin_vars))
url = response.read()
print url

