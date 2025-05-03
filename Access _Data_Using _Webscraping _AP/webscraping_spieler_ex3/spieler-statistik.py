'''
Dieses Python-Projekt verwendet Web Scraping, um die wertvollsten Fußballspieler von [transfermarkt.de](https://www.transfermarkt.de/) zu extrahieren.  
Es werden Name, Marktwert, Verein und Alter gesammelt und in einer CSV-Datei gespeichert.

'''

import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

# URL المصحح (مع تحديد صفحة أكثر ثباتاً)
url = "https://www.transfermarkt.de/spieler-statistik/wertvollstespieler/marktwertetop"

# تحسين رؤوس HTTP للتمويه بشكل أفضل كمتصفح حقيقي
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
    "Referer": "https://www.transfermarkt.de/",
    "Connection": "keep-alive"
}

try:
    # إضافة مهلة للطلب لتجنب الفشل
    response = requests.get(url, headers=headers, timeout=10)
    
    # طباعة حالة الاستجابة للتصحيح
    print(f"حالة الاستجابة: {response.status_code}")
    
    # تحقق من نجاح الطلب
    if response.status_code == 200:
        # تخزين HTML للفحص (مفيد للتصحيح)
        html_content = response.text
        with open("transfermarkt_debug.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        print("تم حفظ HTML في ملف 'transfermarkt_debug.html' للفحص")
        
        soup = BeautifulSoup(html_content, "html.parser")
        
        # العثور على صفوف اللاعبين بطريقة مختلفة 
        # البحث عن جميع عناصر tr في جدول البيانات الرئيسي
        players = []
        
        # نحاول عدة طرق مختلفة للعثور على بيانات اللاعبين
        
        # الطريقة 1: البحث عن جميع صفوف الجدول
        #استخدام محدد CSS للعثور على جميع صفوف الجدول
        all_rows = soup.select("table.items tbody tr")
        print(f"عدد الصفوف التي تم العثور عليها (الطريقة 1): {len(all_rows)}")
        
        if all_rows:
            for row in all_rows:
                # نتخطى صفوف العناوين أو الفارغة
                if 'class' in row.attrs and ('bg_Platz' in row['class'] or 'extrarow' in row['class']):
                    continue
                    
                # استخراج اسم اللاعب
                name_cell = row.select_one("td.hauptlink a")
                if not name_cell:
                    continue
                    
                name = name_cell.text.strip()
                
                # استخراج القيمة السوقية
                market_value_cells = row.select("td.rechts")
                # market_value_cells[-1] يتم استخراج آخر قيمة سوقية موجودة في الصف.
                market_value = market_value_cells[-1].text.strip() if market_value_cells else "N/A"
                
                # استخراج النادي
                club_cell = row.select_one("td img.flaggenrahmen")
                club = club_cell['title'] if club_cell and 'title' in club_cell.attrs else "N/A"
                
                # استخراج العمر
                age_cell = row.select("td")
                age = age_cell[3].text.strip() if len(age_cell) > 3 else "N/A"
                
                players.append({
                    "Name": name,
                    "Marktwert": market_value,
                    "Verein": club,
                    "Alter": age
                })
        
       
    
        
        # طباعة النتائج
        if players:
            print(f"\nتم العثور على {len(players)} لاعباً. فيما يلي أعلى 10 لاعبين:")
            for i, player in enumerate(players[:10], 1):
                print(f"{i}. Spieler: {player['Name']}, Marktwert: {player['Marktwert']}, Verein: {player.get('Verein', 'N/A')}")
                
                # Speichern der Daten in einer CSV-Datei
                df = pd.DataFrame(players)
                df.to_csv("top_players.csv", index=False, encoding="utf-8-sig")
                print("Daten wurden erfolgreich in 'top_players.csv' gespeichert.")
        else:
            print("لم يتم العثور على أي لاعبين. يرجى فحص ملف HTML المحفوظ لفهم بنية الصفحة.")
            
            # طباعة بعض المعلومات التشخيصية
            print("\nمعلومات تشخيصية:")
            print(f"عنوان الصفحة: {soup.title.text if soup.title else 'غير متوفر'}")
            print(f"هل الصفحة تحتوي على كلمة 'Transfermarkt': {'Transfermarkt' in html_content}")
            print(f"هل الصفحة تحتوي على كلمة 'spieler-statistik': {'spieler-statistik' in html_content}")
            print(f"عدد عناصر الجداول في الصفحة: {len(soup.find_all('table'))}")
            
    else:
        print(f"فشل في الوصول إلى الصفحة. كود الحالة: {response.status_code}")
        
except Exception as e:
    print(f"حدث خطأ: {str(e)}")
    print("\nنصائح للتصحيح:")
    print("1. تأكد من أن لديك اتصال بالإنترنت")
    print("2. تأكد من تثبيت المكتبات المطلوبة: pip install requests beautifulsoup4")
    print("3. موقع Transfermarkt قد يكون يحظر استخراج البيانات. جرب إضافة تأخير أو استخدام وكيل (proxy)")