# Yönergeler
# Kullanıcıdan 1-100 arası bir sayı girmesini isteyip,
# Sayının verilen aralık dışında olması durumunda uyarmasını sağlayan,
# Sayının devamını 100’e kadar olan çift sayıları listeleyen
# x ‘ e basınca çıkılan
# Bir program yazınız..

###########

print("Programımıza hoşgeldiniz...")
print("Programımız 0-100 aralığında gireceğiniz sayıdan 100'e kadar olan çift sayıları yazdırmaktadır.")
print("*Programdan çıkış yapmak istiyorsanız 'x' tuşuna basınız!")

while True:

    sayi = input("Lütfen 1 ile 100 arasında bir sayı giriniz: ")

    if sayi == 'x':
        print("Program sonlandırıldı. Hoşçakalın...")
        break

    sayi = int(sayi)    

    if sayi >= 0 and sayi <= 100:

        # if sayi >= 100:
        #     print("Hatalı! Lütfen tekrar deneyin.")
        # Bu iki satır yerine if bloğunda tanımladığımız 'and' kalıbıyla programın kodunu kısaltmış olduk.

        print("Girdiğiniz sayıdan 100'e kadar olan çift sayılar aşağıda sıralanmıştır: ")    
        while sayi <= 100:
            if sayi % 2 == 0:
                print(sayi)
            sayi+=1       

    else:
        print("Hatalı! Lütfen tekrar deneyin.")

    

    

        
          
