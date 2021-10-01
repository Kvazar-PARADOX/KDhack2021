sl = [{
    'name': 'Мопс',
    'height': '27-36',
    "ves" : "6-8",
    "naznachenie" : "Дом",
    "Sherst" : "Глад",
},
{
    'name': 'Ретривер',
    'height': '52-61',
    "ves" : "26-40",
    "naznachenie" : "Охот",
    "Sherst" : "Плот Вод" ,  
},
{
    'name': 'Рассер терьер',
    'height': '22-30',
    "ves" : "5-6",
    "naznachenie" : "Охот",
    "Sherst" : "Глад",
},
{
    
    'name': 'Немецкая овчарка',
    'height': '55-65',
    "ves" : "22-40",
    "naznachenie" : "Служ",
    "Sherst" : "Плот",
},
{
    'name': 'Английский бульдог',
    'height': '50-55',
    "ves" : "24-25",
    "naznachenie" : "Дом",
    "Sherst" : "Глад",
},
{
    'name': 'Акита-ину',
    'height': '60-70',
    "ves" : "20-40",
    "naznachenie" : "Охот",
    "Sherst" : "Плот",
},
{
    'name': 'Сербернар',
    'height': '65-85',
    "ves" : "70-85",
    "naznachenie" : "Служ",
    "Sherst" : "Плот",
},
{
    'name': 'Хаски',
    'height': '50-60',
    "ves" : "15-28",
    "naznachenie" : "Служ",
    "Sherst" : "Плот",
},
{
    'name': 'Бигль',
    'height': '33-40',
    "ves" : "9-14",
    "naznachenie" : "Охот",
    "Sherst" : "Глад",
},
{
    'name': 'Шпиц',
    'height': '40-50',
    "ves" : "17-22",
    "naznachenie" : "Дом",
    "Sherst" : "Плот",
},
{
    'name': 'Доберман',
    'height': '63-72',
    "ves" : "32-45",
    "naznachenie" : "Служ",
    "Sherst" : "Корот",
},
{
    'name': 'Бультерьер',
    'height': '47-56',
    "ves" : "23-38",
    "naznachenie" : "Дом",
    "Sherst" : "Глад",
},
{
    'name': 'Далматин',
    'height': '54-62',
    "ves" : "24-32",
    "naznachenie" : "Дом",
    "Sherst" : "Корот",
},
{
    'name': 'Ротвейлер',
    'height': '56-68',
    "ves" : "38-53",
    "naznachenie" : "Служ",
    "Sherst" : "Глад",
},
{
    'name': 'Cиба-ину',
    'height': '35-41', 
    "ves" : "7-13",
    "naznachenie" : "Охот",
    "Sherst" : "Плот",
},
{
    'name': 'Ньюфаундленд',
    'height': '61-76', 
    "ves" : "49-53",
    "naznachenie" : "Служ",
    "Sherst" : "Плот вод",
}
]

def find_nearbest(in_dic:dict, sl_dic:dict):
    nearbest = []
    prom = []

    for i in sl_dic:
        for j in sl_dic:
            prom.append([i['name'] + '+' + j['name'], 0])

            if round((sr(i['height']) + sr(j['height'])) / 2) >= int(in_dic['height']) - 5 and round((sr(i['height']) + sr(j['height'])) / 2) <= int(in_dic['height']) + 5:
                prom[-1][1] += 3

            if round((sr(i['ves']) + sr(j['ves'])) / 2) >= int(in_dic['ves']) - 3 and round((sr(i['ves']) + sr(j['ves'])) / 2) <= int(in_dic['ves']) + 3:
                prom[-1][1] += 1

            if i['naznachenie'] == j['naznachenie'] == in_dic['naznachenie']:
                prom[-1][1] += 3
            elif i['naznachenie'] == in_dic['naznachenie'] or j['naznachenie'] == in_dic['naznachenie']:
                prom[-1][1] += 2
        
        inp = prom[0]
        for k in range(len(prom)):
            if inp[1] < prom[k][1]:
                inp = prom[k]
        nearbest.append(inp)
        prom = []
    inp2 = nearbest[0]
    for k in range(len(nearbest)):
            if inp2[1] < nearbest[k][1]:
                inp2 = nearbest[k]
    return inp2

def sr(st):
    lst = st.split('-')
    ret = (int(lst[0]) + int(lst[1]))/2
    return ret

in_sl = {
    'name': 'Ньюфаундленд',
    'height': '150', 
    "ves" : "10",
    "naznachenie" : "Охот",
    "Sherst" : "Плот вод",
}

print(find_nearbest(in_sl, sl))