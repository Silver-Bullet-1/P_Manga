import os 
os.system('clear')
import urllib.request

ColorYellow="\033[0;33m"
ColorRed="\033[0;31m"
ColorGreen="\033[0;32m"
ColorPurple="\033[0;35m"

print (ColorYellow+"Silver Bullet")
#os.mkdir('/storage/emulated/0/manga/')
link = "https://3asq.org/wp-content/uploads/WP-manga/data/manga_5ea11671db1b9/5cbed2808e5f2e718af28c3913a5e27d/"
ext="png"
numPhoto=20
for a in range(numPhoto):
    a = a + 1
    if a >= 10:
        urllib.request.urlretrieve(link+str(a)+"."+ext,"/storage/emulated/0/manga/img"+str(a)+".jpg")
    else:
        urllib.request.urlretrieve(link+"0"+str(a)+"."+ext,"/storage/emulated/0/manga/img"+str(a)+".jpg")
    print(ColorGreen+"Photo "+ColorRed+str(a)+ColorGreen+" is Added.")
print (ColorPurple+"photo download suc. . .       Enter Any Key To Exit . . .")
input()
          
