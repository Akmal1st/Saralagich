# Muallif: Otaboboyev Akmal
# https://t.me/akmal1st

import os, sys, configparser
config = configparser.ConfigParser()
config.read("types.ini")

def Saralash(katalog,sara):
     if katalog!='1':
          way = os.path.abspath(katalog)
     elif katalog=='1':
          way = os.getcwd()
     if os.path.isdir(way)==True:
          if os.path.exists(os.getcwd()+"/types.ini")==True:
               os.chdir(way)
               files = os.listdir(way)
               selfFile = os.path.basename(sys.argv[0])
               if selfFile in files:
                    files.remove(selfFile)
                    files.remove("types.ini")
                    if selfFile=="windowed.py":
                         files.remove("console.py")
                    elif selfFile=="console.py":
                         files.remove("windowed.py")
               natija=0
               types = config["types"]
               natija+=sarala(types,files,natija,sara)
               if natija>0:
                    print("Saralandi")
               else:
                    if os.path.isdir("Saralangan")==True:
                         try:
                              os.rmdir("Saralangan")
                         except:
                              print()
                    print('Kerakli tipdagi fayllar topilmadi')
          else:
               print("types.ini topilmadi")
     else:
         print("KATALOG TOPILMADI")
######################################
##  Fayllarni saralash
######################################
def sarala(types,files,natija,sara):
     if sara=="1":
          katalog = "Saralangan"+pl
          if os.path.isdir(os.path.dirname(katalog))==False:
               os.mkdir(os.path.dirname(katalog))
     else:
          katalog=""
     for x in files:
          rep = x[:x.rfind(".")] + x[x.rfind("."):].lower()
          if os.path.exists(rep)==False:
               os.rename(os.getcwd()+pl+x, os.getcwd()+pl+rep)
          for y in types:
               strs="."+y
               if strs==x[x.rfind("."):].lower():
                    if os.path.isfile(rep)==True:
                         way_dir=katalog+types[y]+pl+y
                         if os.path.isdir(os.path.dirname(way_dir))==False:
                             os.mkdir(os.path.dirname(way_dir))
                         elif os.path.isdir(os.path.abspath(way_dir))==False:
                             os.mkdir(way_dir)
                         if os.path.isfile(os.getcwd()+pl+way_dir+pl+rep)==False:
                              os.renames(os.getcwd()+pl+rep, os.getcwd()+pl+way_dir+pl+rep)
                         natija+=1
     return natija
######################################
##  Asosiy qism
######################################
if sys.platform=='linux':
     pl = "/"
elif (sys.platform=='win32') or (sys.platform=='win64'):
     pl = "\\"
print("""Menyu:
1 = joriy katalog
""")
katalog=input("Katalogni kiriting: ")
sara = input("Saralash katalogini qo`shish [1-ha / 0-yo`q] : ")
Saralash(katalog,sara)
