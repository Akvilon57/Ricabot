from data.config import JBASK, JRASS, JRU, JUA, JZAK
from aiogram.utils.markdown import hbold
import json

def del_basket(user_id):
    with open(JRASS, 'r+',encoding='utf-8') as fe:
        f = json.load(fe)
        import datetime
        today = datetime.datetime.today()
        today_data=today.strftime("%Y-%m-%d-%H-%M")

        if 'del_basket' not in f.keys():
            f['del_basket']={}
        datau=f['del_basket']
        use=str(user_id)
        if use in datau:
            print('est')
            user=datau[use]
            user.append(today_data)
        else:
            print('net')
            datau[use]=[]
            user=datau[use]
            user.append(today_data)


        fe.seek(0)
        fe.truncate(0)
        json.dump(f, fe)
        fe.close()  


def lang_bot(lang):
    d=''
    import json
    if lang=='Русский язык':
        with open(JRU, 'r', encoding='utf-8') as file:
            infa = json.load(file)
            d=infa
            file.close()
    elif lang=='Українська мова':
        with open(JUA, 'r', encoding='utf-8') as file:
            infa = json.load(file)
            d=infa
            file.close()
    return d    



def zakaz_list(user_id, articul_id, size_id, price, d_w='del_all'):
    price_id="".join(c for c in price if  c.isdecimal())
    import json
    with open(JBASK, 'r+',encoding='utf-8') as file:
        data = json.load(file)
        if 'w'==d_w:
            if user_id in data:
                articul=data[user_id]
                d_art=len(data[user_id])
                if d_art<10:
                    if articul_id in articul:
                        size=articul[articul_id]
                        if size_id in size:
                            if size[size_id]<10:
                                size[size_id]+=1
                            else:
                                return True
                        else:
                            size[size_id]=1
                    else:
                        articul[articul_id]={'price': price_id, size_id: 1}
                else:
                    return True
            else:
                data[user_id]={articul_id: {'price': price_id, size_id: 1}}

            print(data)
            file.seek(0)
            file.truncate(0)
            json.dump(data, file)
            file.close()

        elif 'del'==d_w:
            if user_id in data:
                articul=data[user_id]
                d_art=len(data[user_id])
                if articul_id in articul:
                    size=articul[articul_id]
                    d_size=len(size)
                    if size_id in size:
                        if size[size_id]==1:
                            if d_size>2:
                                size.pop(size_id)
                                del_basket(user_id)

                            else:
                                if d_art>1:
                                    articul.pop(articul_id)
                                    del_basket(user_id)
                                else:
                                    

                                    data.pop(user_id)
                                    del_basket(user_id)
                                    pass
                                    
                        else:
                            size[size_id]-=1
                            del_basket(user_id)
                    else:
                        return True
                else:
                    return True       
            else:
                return True



            # Ну очень противное место для сохранения JSON(из-за него вылазят скобки)
            file.seek(0)
            file.truncate(0)
            json.dump(data, file)
            file.close()

        elif d_w == 'del_all':
            if user_id in data:
                data.pop(user_id)
                file.seek(0)
                file.truncate(0)
                json.dump(data, file)
                file.close()

                del_basket(user_id)        
                print(data)



def basket(lang,user_id,condition,tel=''):
    basket_all=[]
    price_all=0
    with open(JBASK, 'r+',encoding='utf-8') as file:
        data = json.load(file)
        if condition == 'read':
            if lang=='Русский язык':
                if user_id in data:
                    articuls=data[user_id]
                    basket_all.append(f"🛒 {hbold('Корзина покупок:')}\n\n")
                    for articul in articuls:
                        tov=articuls[articul]
                        for poz in tov:
                            if poz != 'price':
                                kolvo=tov[poz]
                                price_poz=kolvo*int(tov['price'])
                                price_all+=price_poz
                                basket_all.append(f'▫ {articul}  {poz.title()}\nКоличество: {kolvo}шт. Цена: {price_poz} грн.\n\n')
                    basket_all.append(
                        f"{hbold(f'На сумму: {price_all} грн.')}\n")

                    return basket_all

                else:
                    return False


            elif lang == 'Українська мова':
                if user_id in data:
                    articuls=data[user_id]
                    basket_all.append(f"🛒 {hbold('Корзина покупок:')}\n\n")
                    for articul in articuls:
                        tov=articuls[articul]
                        for poz in tov:
                            if poz != 'price':
                                kolvo=tov[poz]
                                price_poz=kolvo*int(tov['price'])
                                price_all+=price_poz
                                basket_all.append(f'▫ {articul}  {poz.title()}\nКількість: {kolvo}шт. Ціна: {price_poz} грн.\n\n')
                    basket_all.append(
                        f"{hbold(f'Загальна вартість: {price_all} грн.')}\n")

                    return basket_all

                else:
                    return False

        elif condition == 'del':
            if lang=='Русский язык':
                print(user_id)
                if user_id in data:
                    articuls=data[user_id]
                    
                    ind=1
                    for articul in articuls:
                        tov=articuls[articul]
                        for poz in tov:
                            if poz != 'price':
                                kolvo=tov[poz]
                                price_poz=kolvo*int(tov['price'])
                                price_all+=price_poz
                                basket_all.append(f"{ind}) {articul}  {poz.title()}\nКоличество: {kolvo}шт. Цена: {price_poz} грн.\n\n")
                                ind +=1
                    basket_all.append(f"\n{hbold(f'На сумму: {price_all} грн.')}\n")


                    data.pop(user_id)
                    file.seek(0)
                    file.truncate(0)
                    json.dump(data, file)
                    file.close()
                    import datetime


                    with open(JZAK, 'r+',encoding='utf-8') as fi:
                        datas = json.load(fi)
                        zakaz=basket_all.copy()
                        zakaz.append(tel)
                        today = datetime.datetime.today()
                        zakaz.append(today.strftime("%Y-%m-%d-%H.%M.%S"))
                        if user_id in datas:
                            spis=datas[user_id]
                            spis.append(zakaz)
                        else:    
                            datas[user_id]=[]
                            spis=datas[user_id]
                            spis.append(zakaz)
                        fi.seek(0)
                        fi.truncate(0)
                        json.dump(datas, fi)
                        fi.close()

                    return basket_all

                else:
                    return False


            elif lang == 'Українська мова':
                if user_id in data:
                    articuls=data[user_id]
                    
                    for articul in articuls:
                        tov=articuls[articul]
                        ind = 1
                        for poz in tov:
                            if poz != 'price':
                                kolvo=tov[poz]
                                price_poz=kolvo*int(tov['price'])
                                price_all+=price_poz
                                basket_all.append(f"{ind}) {articul}  {poz.title()}\nКількість: {kolvo}шт. Ціна: {price_poz} грн.\n\n")
                                ind +=1
                    basket_all.append(f"\n{hbold(f'Загальна вартість: {price_all} грн.')}\n")

                    data.pop(user_id)
                    file.seek(0)
                    file.truncate(0)
                    json.dump(data, file)
                    file.close()
                    import datetime


                    with open(JZAK, 'r+',encoding='utf-8') as fi:
                        datas = json.load(fi)
                        zakaz=basket_all.copy()
                        zakaz.append(tel)
                        today = datetime.datetime.today()
                        zakaz.append(today.strftime("%Y-%m-%d-%H.%M.%S"))
                        if user_id in datas:
                            spis=datas[user_id]
                            spis.append(zakaz)
                        else:    
                            datas[user_id]=[]
                            spis=datas[user_id]
                            spis.append(zakaz)
                        fi.seek(0)
                        fi.truncate(0)
                        json.dump(datas, fi)
                        fi.close()

                    return basket_all

                else:
                    return False





