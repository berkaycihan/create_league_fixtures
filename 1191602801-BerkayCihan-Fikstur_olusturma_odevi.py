import random    #rastgele index üretebilmek için random modulünü dahil ediyoruz

""" 
ADI: BERKAY SOYADI:CİHAN NUMARA:1191602801
TRAKYA ÜNİVERSİTESİ BİLGİSAYAR MÜHENDİSLİĞİ
PROGRAMLAMA DİLLERİNE GİRİŞ ARASINAV ÖDEVİ
"""


def takimlari_karistir(liste):        #her bir satırdaki takim isimlerini alıp islem yapacak fonksiyon

    temp_liste = []
    yeni_index_liste=[]
    while True:  #tüm takimların indexlerini rastgele dizip listeye atan döngü
        if(len(yeni_index_liste)==18): #liste uzunluğu 18 olunca duruyor
            break
        rastgele_index=random.randint(0,17)   #sıfırdan 17 ye kadar rastgele integer deger üretiyor
        if (rastgele_index in yeni_index_liste):  #rastgele üretilen index listede varsa kabul etmeden döngü başına dönüyor
            continue

        else:
            yeni_index_liste.append(rastgele_index)  #listeye ekliyor

    print(yeni_index_liste)
    for i in yeni_index_liste:

        temp_liste.append(liste[i])


    return temp_liste      #fonksiyonumuz liste değer dönüyor


with open('Takimlar.txt','r',encoding="utf-8") as file:  #takımlar dosyasını okuyoruz encoding için ISO-8859-1 kullandım utf-8 sorun çıkardı
    takim_liste=[]
    for i in file:


        #her bir satiri alacağız
        i = i[:-1]  # satir aralarında bosluk olmaması icin

        takim_liste.append(i) # her satirdaki takim ismini döngüyle listeye ekletiyoruz

    raslistem = []
    raslistem = takimlari_karistir(takim_liste)  #fonksiyonu çalıştırıyoruz dönen listeyi yeni listeye atıyoruz
    print(raslistem)








with open('Fikstur.txt','w',encoding="utf-8") as file2:  #fikstur.txt dosyasına yazma islemi burada
    #pass
    """
    SIFIR İNDEXİNDEKİ TAKIM SABİT KALIYOR DİĞER
    TAKIMLAR SAATİN TERSİ YÖNÜNDE KAYARAK İLERLİYOR 
    VE SONRASINDA DEPLASMAN DÜZENLEMESİ YAPILIYOR
    """
    file2.write(    #txt dosyasına uygun düzende fikstürü yazdırıyoruz

    "           1.Hafta           \n"+"  "+ raslistem[0] +"  -  "+raslistem[1]+"\n"
                    +"  " + raslistem[2] + "  -  " +  raslistem[3]+"\n"
                    + "  " + raslistem[4] + "  -  " + raslistem[5] + "\n"
                    + "  "           + raslistem[6] + "  -  " + raslistem[7] + "\n"
                    + "  "           + raslistem[8] + "  -  " + raslistem[9] + "\n"
                    + "  "           + raslistem[10] + "  -  " + raslistem[11] + "\n"
                    + "  "           + raslistem[12] + "  -  " + raslistem[13] + "\n"
                    + "  "           + raslistem[14] + "  -  " + raslistem[15] + "\n"
                    + "  "           + raslistem[16] + "  -  " + raslistem[17] + "\n\n"
    
    
    "           2.Hafta           \n" + "  " +
    raslistem[2] + "  -  " + raslistem[0] + "\n"
    + "  " + raslistem[1] + "  -  " + raslistem[4] + "\n"
    + "  " + raslistem[3] + "  -  " + raslistem[6] + "\n"
    + "  " + raslistem[5] + "  -  " + raslistem[8] + "\n"
    + "  " + raslistem[7] + "  -  " + raslistem[10] + "\n"
    + "  " + raslistem[9] + "  -  " + raslistem[12] + "\n"
    + "  " + raslistem[11] + "  -  " + raslistem[14] + "\n"
    + "  " + raslistem[13] + "  -  " + raslistem[16] + "\n"
    + "  " + raslistem[15] + "  -  " + raslistem[17] + "\n\n"


     "           3.Hafta           \n" + "  " +
    raslistem[0] + "  -  " + raslistem[4] + "\n"
    + "  " + raslistem[6] + "  -  " + raslistem[2] + "\n"
    + "  " + raslistem[8] + "  -  " + raslistem[1] + "\n"
    + "  " + raslistem[10] + "  -  " + raslistem[3] + "\n"
    + "  " + raslistem[8] + "  -  " + raslistem[5] + "\n"
    + "  " + raslistem[12] + "  -  " + raslistem[7] + "\n"
    + "  " + raslistem[14] + "  -  " + raslistem[9] + "\n"
    + "  " + raslistem[16] + "  -  " + raslistem[11] + "\n"
    + "  " + raslistem[17] + "  -  " + raslistem[13] + "\n\n"


    "           4.Hafta           \n" + "  " +
    raslistem[6] + "  -  " + raslistem[0] + "\n"
    + "  " + raslistem[4] + "  -  " + raslistem[8] + "\n"
    + "  " + raslistem[2] + "  -  " + raslistem[10] + "\n"
    + "  " + raslistem[1] + "  -  " + raslistem[12] + "\n"
    + "  " + raslistem[3] + "  -  " + raslistem[14] + "\n"
    + "  " + raslistem[5] + "  -  " + raslistem[16] + "\n"
    + "  " + raslistem[7] + "  -  " + raslistem[17] + "\n"
    + "  " + raslistem[9] + "  -  " + raslistem[15] + "\n"
    + "  " + raslistem[11] + "  -  " + raslistem[13] + "\n\n"


    "           5.Hafta           \n" + "  " +
    raslistem[0] + "  -  " + raslistem[8] + "\n"
    + "  " + raslistem[10] + "  -  " + raslistem[6] + "\n"
    + "  " + raslistem[12] + "  -  " + raslistem[4] + "\n"
    + "  " + raslistem[14] + "  -  " + raslistem[2] + "\n"
    + "  " + raslistem[16] + "  -  " + raslistem[1] + "\n"
    + "  " + raslistem[17] + "  -  " + raslistem[3] + "\n"
    + "  " + raslistem[15] + "  -  " + raslistem[5] + "\n"
    + "  " + raslistem[13] + "  -  " + raslistem[7] + "\n"
    + "  " + raslistem[11] + "  -  " + raslistem[9] + "\n\n"

     "           6.Hafta           \n" + "  " +
    raslistem[10] + "  -  " + raslistem[0] + "\n"
    + "  " + raslistem[8] + "  -  " + raslistem[12] + "\n"
    + "  " + raslistem[6] + "  -  " + raslistem[14] + "\n"
    + "  " + raslistem[4] + "  -  " + raslistem[16] + "\n"
    + "  " + raslistem[2] + "  -  " + raslistem[17] + "\n"
    + "  " + raslistem[1] + "  -  " + raslistem[15] + "\n"
    + "  " + raslistem[3] + "  -  " + raslistem[13] + "\n"
    + "  " + raslistem[5] + "  -  " + raslistem[11] + "\n"
    + "  " + raslistem[7] + "  -  " + raslistem[9] + "\n\n"

    "           7.Hafta           \n" + "  " +
    raslistem[0] + "  -  " + raslistem[12] + "\n"
    + "  " + raslistem[14] + "  -  " + raslistem[10] + "\n"
    + "  " + raslistem[16] + "  -  " + raslistem[8] + "\n"
    + "  " + raslistem[17] + "  -  " + raslistem[6] + "\n"
    + "  " + raslistem[15] + "  -  " + raslistem[4] + "\n"
    + "  " + raslistem[13] + "  -  " + raslistem[2] + "\n"
    + "  " + raslistem[11] + "  -  " + raslistem[1] + "\n"
    + "  " + raslistem[9] + "  -  " + raslistem[3] + "\n"
    + "  " + raslistem[7] + "  -  " + raslistem[5] + "\n\n"


    "           8.Hafta           \n" + "  " +
    raslistem[15] + "  -  " + raslistem[0] + "\n"
    + "  " + raslistem[17] + "  -  " + raslistem[13] + "\n"
    + "  " + raslistem[16] + "  -  " + raslistem[11] + "\n"
    + "  " + raslistem[14] + "  -  " + raslistem[9] + "\n"
    + "  " + raslistem[12] + "  -  " + raslistem[7] + "\n"
    + "  " + raslistem[10] + "  -  " + raslistem[5] + "\n"
    + "  " + raslistem[8] + "  -  " + raslistem[3] + "\n"
    + "  " + raslistem[6] + "  -  " + raslistem[1] + "\n"
    + "  " + raslistem[4] + "  -  " + raslistem[2] + "\n\n"


    "           9.Hafta           \n" + "  " +
    raslistem[0] + "  -  " + raslistem[16] + "\n"
    + "  " + raslistem[17] + "  -  " + raslistem[14] + "\n"
    + "  " + raslistem[15] + "  -  " + raslistem[12] + "\n"
    + "  " + raslistem[13] + "  -  " + raslistem[10] + "\n"
    + "  " + raslistem[11] + "  -  " + raslistem[8] + "\n"
    + "  " + raslistem[9] + "  -  " + raslistem[6] + "\n"
    + "  " + raslistem[7] + "  -  " + raslistem[4] + "\n"
    + "  " + raslistem[5] + "  -  " + raslistem[2] + "\n"
    + "  " + raslistem[3] + "  -  " + raslistem[1] + "\n\n"


    "           10.Hafta           \n" + "  " +
    raslistem[17] + "  -  " + raslistem[0] + "\n"
    + "  " + raslistem[16] + "  -  " + raslistem[15] + "\n"
    + "  " + raslistem[14] + "  -  " + raslistem[13] + "\n"
    + "  " + raslistem[12] + "  -  " + raslistem[11] + "\n"
    + "  " + raslistem[10] + "  -  " + raslistem[9] + "\n"
    + "  " + raslistem[8] + "  -  " + raslistem[7] + "\n"
    + "  " + raslistem[6] + "  -  " + raslistem[5] + "\n"
    + "  " + raslistem[4] + "  -  " + raslistem[3] + "\n"
    + "  " + raslistem[2] + "  -  " + raslistem[1] + "\n\n"

    "           11.Hafta           \n" + "  " +
    raslistem[0] + "  -  " + raslistem[15] + "\n"
    + "  " + raslistem[13] + "  -  " + raslistem[17] + "\n"
    + "  " + raslistem[11] + "  -  " + raslistem[16] + "\n"
    + "  " + raslistem[9] + "  -  " + raslistem[14] + "\n"
    + "  " + raslistem[7] + "  -  " + raslistem[12] + "\n"
    + "  " + raslistem[5] + "  -  " + raslistem[10] + "\n"
    + "  " + raslistem[3] + "  -  " + raslistem[8] + "\n"
    + "  " + raslistem[1] + "  -  " + raslistem[6] + "\n"
    + "  " + raslistem[2] + "  -  " + raslistem[4] + "\n\n"


    "           12.Hafta           \n" + "  " +
    raslistem[13] + "  -  " + raslistem[0] + "\n"
    + "  " + raslistem[15] + "  -  " + raslistem[11] + "\n"
    + "  " + raslistem[17] + "  -  " + raslistem[9] + "\n"
    + "  " + raslistem[16] + "  -  " + raslistem[7] + "\n"
    + "  " + raslistem[14] + "  -  " + raslistem[5] + "\n"
    + "  " + raslistem[12] + "  -  " + raslistem[3] + "\n"
    + "  " + raslistem[10] + "  -  " + raslistem[1] + "\n"
    + "  " + raslistem[8] + "  -  " + raslistem[2] + "\n"
    + "  " + raslistem[6] + "  -  " + raslistem[4] + "\n\n"


    "           13.Hafta           \n" + "  " +
    raslistem[0] + "  -  " + raslistem[11] + "\n"
    + "  " + raslistem[9] + "  -  " + raslistem[13] + "\n"
    + "  " + raslistem[7] + "  -  " + raslistem[15] + "\n"
    + "  " + raslistem[5] + "  -  " + raslistem[17] + "\n"
    + "  " + raslistem[3] + "  -  " + raslistem[16] + "\n"
    + "  " + raslistem[1] + "  -  " + raslistem[14] + "\n"
    + "  " + raslistem[2] + "  -  " + raslistem[12] + "\n"
    + "  " + raslistem[4] + "  -  " + raslistem[10] + "\n"
    + "  " + raslistem[6] + "  -  " + raslistem[8] + "\n\n"


    "           14.Hafta           \n" + "  " +
    raslistem[9] + "  -  " + raslistem[0] + "\n"
    + "  " + raslistem[11] + "  -  " + raslistem[7] + "\n"
    + "  " + raslistem[13] + "  -  " + raslistem[5] + "\n"
    + "  " + raslistem[15] + "  -  " + raslistem[3] + "\n"
    + "  " + raslistem[17] + "  -  " + raslistem[1] + "\n"
    + "  " + raslistem[16] + "  -  " + raslistem[2] + "\n"
    + "  " + raslistem[14] + "  -  " + raslistem[4] + "\n"
    + "  " + raslistem[12] + "  -  " + raslistem[6] + "\n"
    + "  " + raslistem[10] + "  -  " + raslistem[8] + "\n\n"


    "           15.Hafta           \n" + "  " +
    raslistem[0] + "  -  " + raslistem[7] + "\n"
    + "  " + raslistem[5] + "  -  " + raslistem[9] + "\n"
    + "  " + raslistem[3] + "  -  " + raslistem[11] + "\n"
    + "  " + raslistem[1] + "  -  " + raslistem[13] + "\n"
    + "  " + raslistem[2] + "  -  " + raslistem[15] + "\n"
    + "  " + raslistem[4] + "  -  " + raslistem[17] + "\n"
    + "  " + raslistem[6] + "  -  " + raslistem[16] + "\n"
    + "  " + raslistem[8] + "  -  " + raslistem[14] + "\n"
    + "  " + raslistem[10] + "  -  " + raslistem[12] + "\n\n"


    "           16.Hafta           \n" + "  " +
    raslistem[5] + "  -  " + raslistem[0] + "\n"
    + "  " + raslistem[7] + "  -  " + raslistem[3] + "\n"
    + "  " + raslistem[9] + "  -  " + raslistem[1] + "\n"
    + "  " + raslistem[11] + "  -  " + raslistem[2] + "\n"
    + "  " + raslistem[13] + "  -  " + raslistem[4] + "\n"
    + "  " + raslistem[15] + "  -  " + raslistem[6] + "\n"
    + "  " + raslistem[17] + "  -  " + raslistem[8] + "\n"
    + "  " + raslistem[16] + "  -  " + raslistem[10] + "\n"
    + "  " + raslistem[14] + "  -  " + raslistem[12] + "\n\n"


    "           17.Hafta           \n" + "  " +
    raslistem[0] + "  -  " + raslistem[3] + "\n"
    + "  " + raslistem[1] + "  -  " + raslistem[5] + "\n"
    + "  " + raslistem[2] + "  -  " + raslistem[7] + "\n"
    + "  " + raslistem[4] + "  -  " + raslistem[9] + "\n"
    + "  " + raslistem[6] + "  -  " + raslistem[11] + "\n"
    + "  " + raslistem[8] + "  -  " + raslistem[13] + "\n"
    + "  " + raslistem[10] + "  -  " + raslistem[15] + "\n"
    + "  " + raslistem[12] + "  -  " + raslistem[17] + "\n"
    + "  " + raslistem[14] + "  -  " + raslistem[16] + "\n\n"


    "           18.Hafta           \n" + "  " +
    raslistem[1] + "  -  " + raslistem[0] + "\n"
    + "  " + raslistem[3] + "  -  " + raslistem[2] + "\n"
    + "  " + raslistem[5] + "  -  " + raslistem[4] + "\n"
    + "  " + raslistem[7] + "  -  " + raslistem[6] + "\n"
    + "  " + raslistem[9] + "  -  " + raslistem[8] + "\n"
    + "  " + raslistem[11] + "  -  " + raslistem[10] + "\n"
    + "  " + raslistem[13] + "  -  " + raslistem[12] + "\n"
    + "  " + raslistem[15] + "  -  " + raslistem[14] + "\n"
    + "  " + raslistem[17] + "  -  " + raslistem[16] + "\n\n"


    "           19.Hafta           \n" + "  " +
    raslistem[0] + "  -  " + raslistem[2] + "\n"
    + "  " + raslistem[4] + "  -  " + raslistem[1] + "\n"
    + "  " + raslistem[6] + "  -  " + raslistem[3] + "\n"
    + "  " + raslistem[8] + "  -  " + raslistem[5] + "\n"
    + "  " + raslistem[10] + "  -  " + raslistem[7] + "\n"
    + "  " + raslistem[12] + "  -  " + raslistem[9] + "\n"
    + "  " + raslistem[14] + "  -  " + raslistem[11] + "\n"
    + "  " + raslistem[16] + "  -  " + raslistem[13] + "\n"
    + "  " + raslistem[17] + "  -  " + raslistem[15] + "\n\n"


    "           20.Hafta           \n" + "  " +
    raslistem[4] + "  -  " + raslistem[0] + "\n"
    + "  " + raslistem[2] + "  -  " + raslistem[6] + "\n"
    + "  " + raslistem[1] + "  -  " + raslistem[8] + "\n"
    + "  " + raslistem[3] + "  -  " + raslistem[10] + "\n"
    + "  " + raslistem[5] + "  -  " + raslistem[12] + "\n"
    + "  " + raslistem[7] + "  -  " + raslistem[14] + "\n"
    + "  " + raslistem[9] + "  -  " + raslistem[16] + "\n"
    + "  " + raslistem[11] + "  -  " + raslistem[17] + "\n"
    + "  " + raslistem[13] + "  -  " + raslistem[15] + "\n\n"


    "           21.Hafta           \n" + "  " +
    raslistem[0] + "  -  " + raslistem[6] + "\n"
    + "  " + raslistem[8] + "  -  " + raslistem[4] + "\n"
    + "  " + raslistem[10] + "  -  " + raslistem[2] + "\n"
    + "  " + raslistem[12] + "  -  " + raslistem[1] + "\n"
    + "  " + raslistem[14] + "  -  " + raslistem[3] + "\n"
    + "  " + raslistem[16] + "  -  " + raslistem[5] + "\n"
    + "  " + raslistem[17] + "  -  " + raslistem[7] + "\n"
    + "  " + raslistem[15] + "  -  " + raslistem[9] + "\n"
    + "  " + raslistem[13] + "  -  " + raslistem[11] + "\n\n"


    "           22.Hafta           \n" + "  " +
    raslistem[8] + "  -  " + raslistem[0] + "\n"
    + "  " + raslistem[6] + "  -  " + raslistem[10] + "\n"
    + "  " + raslistem[4] + "  -  " + raslistem[12] + "\n"
    + "  " + raslistem[2] + "  -  " + raslistem[14] + "\n"
    + "  " + raslistem[1] + "  -  " + raslistem[16] + "\n"
    + "  " + raslistem[3] + "  -  " + raslistem[17] + "\n"
    + "  " + raslistem[5] + "  -  " + raslistem[15] + "\n"
    + "  " + raslistem[7] + "  -  " + raslistem[13] + "\n"
    + "  " + raslistem[9] + "  -  " + raslistem[11] + "\n\n"


    "           23.Hafta           \n" + "  " +
    raslistem[0] + "  -  " + raslistem[10] + "\n"
    + "  " + raslistem[12] + "  -  " + raslistem[8] + "\n"
    + "  " + raslistem[14] + "  -  " + raslistem[6] + "\n"
    + "  " + raslistem[16] + "  -  " + raslistem[4] + "\n"
    + "  " + raslistem[17] + "  -  " + raslistem[2] + "\n"
    + "  " + raslistem[15] + "  -  " + raslistem[1] + "\n"
    + "  " + raslistem[13] + "  -  " + raslistem[3] + "\n"
    + "  " + raslistem[11] + "  -  " + raslistem[5] + "\n"
    + "  " + raslistem[9] + "  -  " + raslistem[7] + "\n\n"


    "           24.Hafta           \n" + "  " +
    raslistem[12] + "  -  " + raslistem[0] + "\n"
    + "  " + raslistem[10] + "  -  " + raslistem[14] + "\n"
    + "  " + raslistem[8] + "  -  " + raslistem[16] + "\n"
    + "  " + raslistem[6] + "  -  " + raslistem[17] + "\n"
    + "  " + raslistem[4] + "  -  " + raslistem[15] + "\n"
    + "  " + raslistem[2] + "  -  " + raslistem[13] + "\n"
    + "  " + raslistem[1] + "  -  " + raslistem[11] + "\n"
    + "  " + raslistem[3] + "  -  " + raslistem[9] + "\n"
    + "  " + raslistem[5] + "  -  " + raslistem[7] + "\n\n"


    "           25.Hafta           \n" + "  " +
    raslistem[0] + "  -  " + raslistem[14] + "\n"
    + "  " + raslistem[16] + "  -  " + raslistem[12] + "\n"
    + "  " + raslistem[17] + "  -  " + raslistem[10] + "\n"
    + "  " + raslistem[15] + "  -  " + raslistem[8] + "\n"
    + "  " + raslistem[13] + "  -  " + raslistem[6] + "\n"
    + "  " + raslistem[11] + "  -  " + raslistem[4] + "\n"
    + "  " + raslistem[9] + "  -  " + raslistem[2] + "\n"
    + "  " + raslistem[7] + "  -  " + raslistem[1] + "\n"
    + "  " + raslistem[5] + "  -  " + raslistem[3] + "\n\n"


    "           26.Hafta           \n" + "  " +
    raslistem[16] + "  -  " + raslistem[0] + "\n"
    + "  " + raslistem[14] + "  -  " + raslistem[17] + "\n"
    + "  " + raslistem[12] + "  -  " + raslistem[15] + "\n"
    + "  " + raslistem[10] + "  -  " + raslistem[13] + "\n"
    + "  " + raslistem[8] + "  -  " + raslistem[11] + "\n"
    + "  " + raslistem[6] + "  -  " + raslistem[9] + "\n"
    + "  " + raslistem[4] + "  -  " + raslistem[7] + "\n"
    + "  " + raslistem[2] + "  -  " + raslistem[5] + "\n"
    + "  " + raslistem[1] + "  -  " + raslistem[3] + "\n\n"


    "           27.Hafta           \n" + "  " +
    raslistem[0] + "  -  " + raslistem[17] + "\n"
    + "  " + raslistem[15] + "  -  " + raslistem[16] + "\n"
    + "  " + raslistem[13] + "  -  " + raslistem[14] + "\n"
    + "  " + raslistem[11] + "  -  " + raslistem[12] + "\n"
    + "  " + raslistem[9] + "  -  " + raslistem[10] + "\n"
    + "  " + raslistem[7] + "  -  " + raslistem[8] + "\n"
    + "  " + raslistem[5] + "  -  " + raslistem[6] + "\n"
    + "  " + raslistem[3] + "  -  " + raslistem[4] + "\n"
    + "  " + raslistem[1] + "  -  " + raslistem[2] + "\n\n"


    "           28.Hafta           \n" + "  " +
    raslistem[15] + "  -  " + raslistem[0] + "\n"
    + "  " + raslistem[17] + "  -  " + raslistem[13] + "\n"
    + "  " + raslistem[16] + "  -  " + raslistem[11] + "\n"
    + "  " + raslistem[14] + "  -  " + raslistem[9] + "\n"
    + "  " + raslistem[12] + "  -  " + raslistem[7] + "\n"
    + "  " + raslistem[10] + "  -  " + raslistem[5] + "\n"
    + "  " + raslistem[8] + "  -  " + raslistem[3] + "\n"
    + "  " + raslistem[6] + "  -  " + raslistem[1] + "\n"
    + "  " + raslistem[4] + "  -  " + raslistem[2] + "\n\n"


    "           29.Hafta           \n" + "  " +
    raslistem[0] + "  -  " + raslistem[13] + "\n"
    + "  " + raslistem[11] + "  -  " + raslistem[15] + "\n"
    + "  " + raslistem[9] + "  -  " + raslistem[17] + "\n"
    + "  " + raslistem[7] + "  -  " + raslistem[16] + "\n"
    + "  " + raslistem[5] + "  -  " + raslistem[14] + "\n"
    + "  " + raslistem[3] + "  -  " + raslistem[12] + "\n"
    + "  " + raslistem[1] + "  -  " + raslistem[10] + "\n"
    + "  " + raslistem[2] + "  -  " + raslistem[8] + "\n"
    + "  " + raslistem[4] + "  -  " + raslistem[6] + "\n\n"


    "           30.Hafta           \n" + "  " +
    raslistem[11] + "  -  " + raslistem[0] + "\n"
    + "  " + raslistem[13] + "  -  " + raslistem[9] + "\n"
    + "  " + raslistem[15] + "  -  " + raslistem[7] + "\n"
    + "  " + raslistem[17] + "  -  " + raslistem[5] + "\n"
    + "  " + raslistem[16] + "  -  " + raslistem[3] + "\n"
    + "  " + raslistem[14] + "  -  " + raslistem[1] + "\n"
    + "  " + raslistem[12] + "  -  " + raslistem[2] + "\n"
    + "  " + raslistem[10] + "  -  " + raslistem[4] + "\n"
    + "  " + raslistem[8] + "  -  " + raslistem[6] + "\n\n"


    "           31.Hafta           \n" + "  " +
    raslistem[0] + "  -  " + raslistem[9] + "\n"
    + "  " + raslistem[7] + "  -  " + raslistem[11] + "\n"
    + "  " + raslistem[5] + "  -  " + raslistem[13] + "\n"
    + "  " + raslistem[3] + "  -  " + raslistem[15] + "\n"
    + "  " + raslistem[1] + "  -  " + raslistem[17] + "\n"
    + "  " + raslistem[2] + "  -  " + raslistem[16] + "\n"
    + "  " + raslistem[4] + "  -  " + raslistem[14] + "\n"
    + "  " + raslistem[6] + "  -  " + raslistem[12] + "\n"
    + "  " + raslistem[8] + "  -  " + raslistem[10] + "\n\n"


    "           32.Hafta           \n" + "  " +
    raslistem[7] + "  -  " + raslistem[0] + "\n"
    + "  " + raslistem[9] + "  -  " + raslistem[5] + "\n"
    + "  " + raslistem[11] + "  -  " + raslistem[3] + "\n"
    + "  " + raslistem[13] + "  -  " + raslistem[1] + "\n"
    + "  " + raslistem[15] + "  -  " + raslistem[2] + "\n"
    + "  " + raslistem[17] + "  -  " + raslistem[4] + "\n"
    + "  " + raslistem[16] + "  -  " + raslistem[6] + "\n"
    + "  " + raslistem[14] + "  -  " + raslistem[8] + "\n"
    + "  " + raslistem[12] + "  -  " + raslistem[10] + "\n\n"


    "           33.Hafta           \n" + "  " +
    raslistem[0] + "  -  " + raslistem[3] + "\n"
    + "  " + raslistem[3] + "  -  " + raslistem[5] + "\n"
    + "  " + raslistem[1] + "  -  " + raslistem[7] + "\n"
    + "  " + raslistem[2] + "  -  " + raslistem[9] + "\n"
    + "  " + raslistem[4] + "  -  " + raslistem[11] + "\n"
    + "  " + raslistem[6] + "  -  " + raslistem[13] + "\n"
    + "  " + raslistem[8] + "  -  " + raslistem[15] + "\n"
    + "  " + raslistem[10] + "  -  " + raslistem[17] + "\n"
    + "  " + raslistem[12] + "  -  " + raslistem[16] + "\n\n"


    "           34.Hafta           \n" + "  " +
    raslistem[3] + "  -  " + raslistem[0] + "\n"
    + "  " + raslistem[5] + "  -  " + raslistem[1] + "\n"
    + "  " + raslistem[7] + "  -  " + raslistem[2] + "\n"
    + "  " + raslistem[9] + "  -  " + raslistem[4] + "\n"
    + "  " + raslistem[11] + "  -  " + raslistem[6] + "\n"
    + "  " + raslistem[13] + "  -  " + raslistem[8] + "\n"
    + "  " + raslistem[15] + "  -  " + raslistem[10] + "\n"
    + "  " + raslistem[17] + "  -  " + raslistem[12] + "\n"
    + "  " + raslistem[16] + "  -  " + raslistem[14] + "\n\n"

               )

