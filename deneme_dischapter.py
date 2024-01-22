message_mappings = {
    "hys": ["hys", "hayata yatırım", "hayata yatirim", "hayata yatır","hayat"],
    "his": ["his", "her ihtimal"],
    "iis": ["iis", "iyi ihtimaller", "iyi ihtimal", "iyi", "iss"],
    "18bes":["18 yaş altı","-18", "- 18", "çocuk", "küçük", "çocuk", "18", "on sekiz", "yaş"],
    "bes": ["bes","bireysel emeklilik","bireysel"],
    "ok" : ["ok", "otomatik","otomatik katılım", "otomatik katilim"]

}

def MainFonksiyon(user_message,attribute,dict):
    def func(urun):
            
            
        if dict.get(urun) == None:
            text=f"İlgili ürün için {attribute} şartları bulunmamaktadır."
            dispatcher.utter_message(text =text)
        else:
            dispatcher.utter_message(text =f"{(attribute).title()}")
            dispatcher.utter_message(text =dict.get(urun))
             
        
    matched_key = None
    #user_message=tracker.latest_message['text']
    
    for key, keywords in message_mappings.items():
        for keyword in keywords:
            if keyword in user_message:
                matched_key = key
                break

    if matched_key is not None:
        func(matched_key)
    else:
        dispatcher.utter_message(text =f"{(attribute).title()}")

        for i in dict.values():
            dispatcher.utter_message(text =i)  
    return []       





def PoliceSuresi():
    dict_police_suresi={"hys":"<font color='blue'><b>HYS (Hayata Yatırım Sigortası):</b></font> Sabit **10 (on)** yıldır.", 
                        "iis":"<font color='blue'><b>İİS (İyi İhtimallerin Sigortası):</b></font> **12** ile **20 yıl** arasında değişebilir.",
                        "his": "<font color='blue'><b>HİS (Her İhtimalin Sigortası):</b></font> **12 yıl** ya da **6 yıl** olabilir"}
    user_message=input("poliçe süresi için message : ")
    MainFonksiyon(user_message,'poliçe süresi',dict_police_suresi)
    
           
    return []


PoliceSuresi()


def PoliceIptali():
    dict_police_iptali={"hys":"<font color='blue'><b>HYS (Hayata Yatırım Sigortası):</b></font> Poliçe ilk yıl içinde iptal edilemez. Poliçe süresi 1 yıl dolduktan ve 1 yıllık primini ödedikten sonra yapabilir. İptal statüsündeki bir poliçe hiçbir türlü yeniden yürürlüğe alınamaz.", 
          "iis":"<font color='blue'><b>İİS (İyi İhtimallerin Sigortası):</b></font> İptal statüsündeki bir poliçe Operasyon onayı ile 12 aydan önce evraksız , 12 aydan sonra evraklı (yeniden yürürlük talep formu ya da süre sonuna ekleme talep formu) yeniden yürürlüğe alınabilir.", 
          "his":"<font color='blue'><b>HİS (Her İhtimalin Sigortası):</b></font> Poliçe ilk yıl içinde iptal edilemez. <br>Poliçe süresi 1 yıl dolduktan ve 12 aylık primini ödedikten sonra iptal işlemi yapabilir. <br>İptal statüsündeki bir poliçe Operasyon onayı ile 12 aydan önce evraksız, 12 aydan sonra evraklı (yeniden yürürlük talep formu ya da süre sonuna ekleme talep formu) yeniden yürürlüğe alınabilir."
                            }
    user_message2=input("poliçe iptali için ürün : ")
    attribute="poliçe iptali"
    MainFonksiyon(user_message2,attribute,dict_police_iptali)

    return []

PoliceIptali()
