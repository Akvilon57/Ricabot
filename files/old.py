import json
from urllib.error import HTTPError
from urllib.request import urlopen
#from jazik import spisru, spisua
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

spisua={'casual':'Одяг',
'blouse':'Сорочки та блузи',
'bodi':'Боді',
'skirt':'Спідниці',
'pants':'Брюки',
'suits':'Костюми',
'jackets':'Піджаки',
'vests':'Жилети',
'overalls':'Комбінезони',
'suitshot':'Світшоти та светри',
't-shirts':'Футболки та майки',
'shorts':'Шорти',
'outwear':'Верхній одяг',
'sport_wellness':'Sport&Wellness',

'dress':'Сукні',
'evening':'Вечірні сукні',
'cocktail':'Коктейльні сукні',
'summer':'Літні сукні',
'autumn':'Демісезонні сукні',

'xl':'Великі розміри',
'evening-dress':'Вечірні сукні',
'cocktail-dress':'Коктейльні сукні',
'spring-summer-dress':'Літні сукні',
'autumn-winter-dress':'Демісезонні сукні',
'blouses':'Блузки та сорочки',
'skirts':'Спідниці',
'pants-xl':'Брюки',
'suits-xl':'Костюми',
'zhakety':'Піджаки',
'cardigans':'Жилети',
'overalls-xl':'Комбінезони',
'pullover':'Світшоти і светри',
'futbolki':'Футболки',
'outwear':'Верхній одяг',

'accessories':'Аксесуари',
'avtorskie_aksessuary':'Авторські аксесуари',
'zashchitnaya_maska_dlya_litsa':'Маски для обличчя',
'braslety':'Браслети',
'sergi':'Сережки',
'ozherelya':'Підвіски',
'sumki':'Сумки',
'poyasa':'Ремені',
'kolgoty':'Колготи, панчохи',
'shapki':'Шапки, рукавички',
'sharfy':'Шарфи, хустки',
'overalls':'Комбінезони',

'sale':'Знижки'
}

spisru={'casual':'Одежда',
'blouse':'Рубашки и блузы',
'overalls':'Комбинизоны',
'bodi':'Боди',
'skirt':'Юбки',
'pants':'Брюки',
'suits':'Костюмы',
'jackets':'Пиджаки',
'vests':'Жилеты',
'overalls':'Комбинезоны',
'suitshot':'Свитшоты и свитера',
't-shirts':'Футболки и майки',
'shorts':'Шорты',
'outwear':'Верхняя одежда',
'sport_wellness':'Sport&Wellness',

'dress':'Платья',
'evening':'Вечерние платья',
'cocktail':'Коктейльные платья',
'summer':'Летние платья',
'autumn':'Демисезонные платья',

'xl':'Большие размеры',
'evening-dress':'Вечерние',
'cocktail-dress':'Коктейльные',
'spring-summer-dress':'Летние платья',
'autumn-winter-dress':'Демисезонные',
'blouses':'Рубашки и блузы',
'skirts':'Юбки',
'pants-xl':'Брюки',
'suits-xl':'Костюмы',
'zhakety':'Пиджаки',
'cardigans':'Жилеты',
'overalls-xl':'Комбинезоны',
'pullover':'Свитера и свитшоты',
'futbolki':'Футболки',
'outwear':'Верхняя одежда',

'accessories':'Аксессуары',
'avtorskie_aksessuary':'Авторские аксессуары',
'zashchitnaya_maska_dlya_litsa':'Маски для лица',
'braslety':'Браслеты',
'sergi':'Серьги',
'ozherelya':'Подвески',
'sumki':'Сумки',
'poyasa':'Ремни',
'kolgoty':'Колготы, чулки',
'shapki':'Шапки, перчатки',
'sharfy':'Шарфы, платки',

'sale':'Скидки'
}


def translite(size):
    from googletrans import Translator
    translator = Translator()

    result = translator.translate(size, dest='uk')
    res=result.text
    return res
        
    





def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        # title = bs.body.h1
    except AttributeError as e:
        return None
    return bs


def url_cat(jazik):
    global scanz
    url = []
    urls_cat = []
    scan_stranic = []
    # Подсчет количества страниц в категориях
    cefra = str(list(range(1, 30)))
    url_categ=''
    if jazik=='ua':
        url_categ = ['https://ricamare.com.ua/ua/catalog/casual/','https://ricamare.com.ua/ua/catalog/dress/', 'https://ricamare.com.ua/ua/catalog/xl/', 'https://ricamare.com.ua/ua/catalog/accessories/']
    if jazik=='ru':
        url_categ = ['https://ricamare.com.ua/catalog/casual/', 'https://ricamare.com.ua/catalog/dress/', 'https://ricamare.com.ua/catalog/xl/', 'https://ricamare.com.ua/catalog/accessories/']
    for url_scan in url_categ:
        ti = getTitle(url_scan)
        name_scan = ti.find_all('div', class_='bx-pagination-container')
        for scan in name_scan:
            a = scan.find_all('a')
            for b in a:
                z = b.get_text()
                if z in cefra:
                    scanz = z.strip().lstrip()
        scan_stranic.append(scanz)
    print(scan_stranic)
    colvo_cat = len(url_categ)
    d = 1
    while True:
        if colvo_cat >= d:
            s = d - 1
            scann = int(scan_stranic[s])
            for stranic in range(1,scann+1):
                urls_cat.append(f'{url_categ[s]}?PAGEN_1={stranic}')
                #print(f'{url_categ[s]}?PAGEN_1={stranic}')
            d += 1
        else:
            break

    # for i in range(1,9):
    #    urls_cat.append(f'https://ricamare.com.ua/catalog/casual/?PAGEN_1={i}')
    # for i in range(1,8):
    #    urls_cat.append(f'https://ricamare.com.ua/catalog/dress/?PAGEN_1={i}')
    # for i in range(1,4):
    #    urls_cat.append(f'https://ricamare.com.ua/catalog/xl/?PAGEN_1={i}')
    # for i in range(1,6):
    #    urls_cat.append(f'https://ricamare.com.ua/catalog/accessories/?PAGEN_1={i}')

    # Создание ссылок на товар
    for urls in urls_cat:
        ti = getTitle(urls)
        name_p = ti.find_all('div', {'class': 'desc-name-fix'})
        for name in name_p:
            urls = name.find('a').get('href')
            url.append(f'https://ricamare.com.ua{urls}')
    #print(url)
    return url


def kartochka(soup,jaz):
    global articul_s, names, sostav, sostavs, opisanie
    ti = soup
    name_p = ti.find_all(['h1'])
    for name in name_p:
        names = name.get_text()
    articuls = ti.find_all('span', itemprop='sku')
    for articul in articuls:
        articul_s = articul.get_text()

    price_old = ti.find('span', {'class': 'rozn-price-old'})
    if price_old:
        price_old = price_old.get_text()
    else:
        price_old = None

    price_new = ti.find('span', {'class': 'rozn-price-new'})
    if price_new:
        price_new = price_new.get_text()
    else:
        try:
            price_roz = ti.find('p', {'class': 'rozn-price'})
            if price_roz.span:
                price_new = price_roz.span.get_text()
            else:
                price_new = None
        except AttributeError:
            spis=False
            return spis
    sostavi = ti.find_all('p', class_="mat")
    for sostav in sostavi:
        sos = sostav.get_text()
        l = len(sos)
        sostavs=''
        if jaz =='ua':
            sostavs = sos[7:l - 1]
        else:
            sostavs = sos[8:l - 1]
    opisaniu = ti.find_all('span', itemprop="description")
    for opisanie in opisaniu:
        opisanie = opisanie.get_text()
        opisanie = opisanie.replace('\xa0', '')
        if '\xbe' in opisanie:
            opisanie = None

        if opisanie == ':' or '':
            opisanie = None
        # очистить контент от тегов
    foto = []
    color = []
    for child in ti.find_all('img', alt="Выберите цвет"):
        fs = child['src']
        foto.append(f'https://ricamare.com.ua{fs}')
        color.append(child.div.get_text())

    size = []
    for sod in ti.find_all('script'):
        a = sod.get_text()
        x = a.lstrip()
        d = x[20:]
        filename = 'username.txt'
        with open(filename, 'w', encoding='utf-8') as file_object:
            file_object.write(d)
        file_object.close()

        with open(filename, 'r') as file_object:
            try:
                for line in file_object:
                    line = line.strip()
                    try:
                        if 'variant' in line:
                            
                            #print(line)
                            line = line[12:-2]
                            line=str(line)
                            line.replace(',','')
                            line.replace(',','')
                            line.replace('&quot','')
                        
                            if line != '':
                                if line !=',':
                                    #print(f'ok  {line}')
                                    line = line.encode('cp1251').decode('utf-8')
                                    size.append(line)
                    except UnicodeDecodeError:
                        if 'variant' in line:
                            if line != '':
                                if line !=',':
                                    line=line[12:-2]
                                    line=str(line)
                                    line.replace(',','')
                                    line.replace('&quot','')
                                    size.append(line)

                                    

                    try:
                        if "'category':" in line:
                            category = line[13:-2]
                            category = category.encode('cp1251').decode('utf-8')

                    except UnicodeDecodeError:
                        category = line[13:-2]
            except UnicodeDecodeError:
                category = None

    spis = {'articul': articul_s, 'name': names, 'price_old': price_old, 'price_new': price_new, 'foto': foto,
            'color': color, 'size': size, 'category': category, 'sostav': sostavs, 'opisanie': opisanie}
    for key, value in spis.items():
        if value!=None:
            if '\xbe' in value:
                #spis.replace('\xbe','3/4')
                print(key)
    return spis


def catedory(urls,cuntry):
    from urllib.parse import urlparse
    spisok=[]
    parsed = urlparse(urls)
    path = parsed[2] #this is the path element
    pathlist = path.strip('/').split("/")
    dlin=len(pathlist)
    spisok.append(cuntry[pathlist[dlin-3]])
    spisok.append(cuntry[pathlist[dlin-2]])
    return spisok

def stoki_stolbec(d):
    stok=len(d)//3
    ost=len(d)%3
    mas=[]
    if stok>0:
        for i in range(stok):
            if i==0:
                mas.append([d[i],d[i+1],d[i+2]])
            elif i>0:
                mas.append([d[3*i],d[3*i+1],d[3*i+2]])  
        if ost>0:
            if ost==1:
                mas.append([d[3*(i+1)]])
            elif ost==2:
                a=3*(i+1)
                mas.append([d[a],d[a+1]])
    elif stok==0:
        if ost>0:
            if ost==1:
                mas.append([d[0]])
            elif ost==2:
                mas.append([d[0],d[1]])
    return mas

def spisok_telegram(book,cuntry,ru,ua,categoriga,catalog):
    if cuntry == 'ua':
        s=ua[catalog]
        if categoriga in s.keys():#проверка если ключ в словаре
            d=s[categoriga]
            d.append(book)
        else:
            s[categoriga]=[]
            d=s[categoriga]
            d.append(book)
    else:
        s=ru[catalog]
        if categoriga in s.keys():#проверка если ключ в словаре
            d=s[categoriga]
            d.append(book)
        else:
            s[categoriga]=[]
            d=s[categoriga]
            d.append(book)
            uas={}

def ends():
    s=datetime.now()
    print(s)
    uas = {'Одяг': {}, 'Сукні': {}, 'Великі розміри': {}, 'Аксесуари': {}}
    rus = {'Одежда': {}, 'Платья': {}, 'Большие размеры': {}, 'Аксессуары': {}}
    locashion=['ua','ru']
    for jaz in locashion:
        for urls in url_cat(jaz):
            print(f'Скачиваю : {urls} ')
            s=0
            try:
                ti = getTitle(urls)
                kart = kartochka(ti,jaz)
            except Exception:   
                while True:
                    if s<7: 
                        s+=1
                        try:
                            ti = getTitle(urls)
                            kart = kartochka(ti,jaz)
                        except Exception:
                            s+=1
                    else:
                        kart=Fa
                        break   
            if kart==False:
                print(f'!!!Проблемы : {urls} ')
            else:
                kart['urls'] = urls
                tele=[]
                if jaz=='ua':
                    tele=catedory(urls,spisua)
                elif jaz=='ru':
                    tele=catedory(urls,spisru)


                spisok_telegram(kart,jaz,rus,uas,tele[1],tele[0])
        if jaz=='ua':
            with open(f'ricamare_ua.json', 'w', encoding='utf-8') as f:
                json.dump(uas, f)
            print('Базы успешно обновлены в ricamare_ua.json')
        if jaz=='ru':
            with open(f'ricamare_ru.json', 'w', encoding='utf-8') as f:
                json.dump(rus, f)
            print('Базы успешно обновлены в ricamare_ru.json')


def ua():
    perevod={}
    import time
    with open(f'ricamare_ua.json', 'r+') as fil:
        data = json.load(fil)
        for k,v in data.items():
            for vu in v:
                print(vu)
                for to in v[vu]:
                    print('new',to['size'])
                    d=[]
                    for i in to['size']:

                        if i!=',':
                            pass
                        if i!='[':
                            pass
                        if i!=']':
                            pass
                        if i!=', ':
                            with open(f'perevod.json', 'r') as file:
                                ta = json.load(file)
                                if i in ta.keys():
                                    d.append(ta[i])
                                    file.close()

                                else:
                                    time.sleep(5)
                                    tr=translite(i)
                                    d.append(tr)
                                    perevod[i]=tr
                                    with open(f'perevod.json', 'r+') as file:
                                        datas = json.load(file)
                                        datas[i]=tr
                                        file.seek(0)
                                        file.truncate(0)
                                        json.dump(datas, file)
                                        file.close()




                        to['size']=d
                    #print(f'!!! {d}\n')

                    

        fil.seek(0)
        fil.truncate(0)
        json.dump(data, fil)
        fil.close()

def leto_zima():
    spis={'leto':[], 'zima':[]}
    with open('ricamare_ua.json', 'r', encoding='utf-8') as file:
        infa = json.load(file)
        for catl in infa.values():
            for cat in catl.values():
                for cart in cat:
                    if 'лето' in str(cart['category']):
                        spis['leto'].append(cart)
                    elif 'весна' in str(cart['category']):
                        spis['leto'].append(cart)
                    elif 'зима' in str(cart['category']):
                        spis['zima'].append(cart)
                    elif 'осень' in str(cart['category']):
                        spis['zima'].append(cart)
                    elif str(cart['category'])=='/':
                        if 'accessories' not in cart['urls']:
                            spis['zima'].append(cart)
        file.close()
    with open('leto_zima.json', 'w', encoding='utf-8') as fil:
        json.dump(spis, fil)
        fil.close()





def cvs():
    with open('ricamare.json') as f:
        file = json.load(f)
    df = pd.DataFrame(file)
    df.to_csv('ricamare.csv', index=False)
    print('Файл ricamare.csv создан')


def rload():
    try:
        ends()
        ua()
        leto_zima()
    except Exception as es:
        print(f'{es}')





def timer(func):
    import schedule
    import time
    
    #schedule.every(0.1).minutes.do(func)
    #schedule.every().hour.do(job)
    #schedule.every('2').day.do(func)
    #schedule.every().monday.do(func)
    #schedule.every().wednesday.at("13:15").do(job)
    #schedule.every().minute.at(":17").do(job)
    schedule.every(4).days.at("02:00").do(func)
    #schedule.every("3").days.at("1:00:00").do(func)
    while True:
        schedule.run_pending()
        time.sleep(1)


def main():
    try:
        rload()
    except Exception as e:
        print(f'{e}')
    while True:
        try:
            timer(rload)
        except Exception as e:
            print(f'{e}')


if __name__ == '__main__':      
    main()    

