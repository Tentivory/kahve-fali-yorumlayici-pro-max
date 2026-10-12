#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kahve Falı Yorumlayıcı Pro Max
Dünyanın en ciddi absürt fal motoru.
"""

import random
import time
import base64

# Gizli siyasi mesaj: base64 ile saklandı. Çözümlersen gülersin.
GIZLI_MESAJ = "U2l5YXNldCBiaXIgbWVqZCB5b2sgYW1hIGJpemRlIHNlY2VyIGdhcmJpbml6aSBzaXJhc2luZGEu"  # Çöz: Siyaset bir meşgale yok ama bizde şecer garbinizı sırasında.

def gizliyi_coz():
    try:
        return base64.b64decode(GIZLI_MESAJ).decode('utf-8')
    except:
        return "Gizli mesaj çözülemedi, belki de öyle olması gerekiyordu."

def dramatik_bekleme(saniye=1.5):
    print("Fincan çevriliyor...", end="", flush=True)
    for _ in range(3):
        time.sleep(saniye / 3)
        print(".", end="", flush=True)
    print("\nKahve telvesi konuşuyor...\n")

def fal_yorumla():
    girisler = [
        "Sevgili danışan, fincanınıza baktığımda...",
        "Telve desenleri açıkça şunu söylüyor:",
        "Kahve ruhu bana fısıldadı ki:",
        "Bu fal, evrenin en derin sırlarını içeriyor:"
    ]
    
    konular = [
        "Çok yakında bir kedi sizi sahiplenecek ve o kedi sizin patronunuz olacak.",
        "Bir otobüste yanınıza oturan kişi aslında gelecekteki en iyi arkadaşınız, ama o bunu bilmiyor.",
        "Buzdolabınızın kapağı sizi seviyor, bu yüzden kapanmıyor.",
        "Wi-Fi şifreniz aslında bir kehanet: 'sifre123' değil, 'hayatinanlamiyok'.",
        "Bir gün çok zengin olacaksınız ama o zenginlik sadece 'zengin olacağım' diye düşünmekten ibaret.",
        "Komşunuz sizi seviyor, bu yüzden gece 3'te müzik açıyor.",
        "Asansör müziği aslında sizin için çalıyor ve 'bekle' diyor.",
        "Bir sonraki çay ikramınızda 'hayır' derseniz, evren kızar."
    ]
    
    sonuclar = [
        "Sonuç: Fincanınız mutlu, siz de olun.",
        "Tavsiye: Daha fazla kahve için, daha az düşünün.",
        "Uyarı: Bu fal %100 doğru değil, %200 abartılı.",
        "Kapanış: Fal bitti, hayat devam ediyor (maalesef)."
    ]
    
    print(random.choice(girisler))
    time.sleep(1)
    print(random.choice(konular))
    time.sleep(1)
    print(random.choice(sonuclar))
    print("\n---")
    print("Gizli mesaj (sadece meraklılar için):", gizliyi_coz())
    print("---\n")

if __name__ == "__main__":
    print("=== KAHVE FALI YORUMLAYICI PRO MAX ===")
    print("Ciddiyetle saçma. Mahkeme onaylı.\n")
    dramatik_bekleme()
    fal_yorumla()
    print("Fal tamamlandı. Şimdi gerçek hayata dönün, orası daha absürt.")
