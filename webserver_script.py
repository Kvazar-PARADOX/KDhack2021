sl = [{
    'name': 'Мопс',
    'height': '27-36',
    "ves" : "6.3-8.1",
    "naznachenie" : "Дом",
    "Sherst" : "Глад",
    "Agrassive" : "2",
},
{
    'name': 'Ретривер',
    'height': '52-61',
    "ves" : "26-40",
    "naznachenie" : "Охота",
    "Sherst" : "Плот Вод" , 
    "Agrassive" : "1" ,
},
{
    'name': 'Рассер терьер',
    'height': '22-30',
    "ves" : "5-6",
    "naznachenie" : "Охота",
    "Sherst" : "Глад",
    "Agrassive" : "4",
},
{

    'name': 'Немецкая овчарка',
    'height': '55-65',
    "ves" : "22-40",
    "naznachenie" : "Служ",
    "Sherst" : "Плот",
    "Agrassive" : "3",
},
{
    'name': 'Английский бульдог',
    'height': '50-55',
    "ves" : "24",
    "naznachenie" : "Дом",
    "Sherst" : "Глад",
    "Agrassive" : "2",
},
{
    'name': 'Акита-ину',
    'height': '60-70',
    "ves" : "20-40",
    "naznachenie" : "Охот",
    "Sherst" : "Плот",
    "Agrassive" : "2",
},
{
    'name': 'Сербернар',
    'height': '65-85',
    "ves" : "70-85",
    "naznachenie" : "Служ",
    "Sherst" : "Плот",
    "Agrassive" : "2",
},
{
    'name': 'Хаски',
    'height': '50-60',
    "ves" : "15-28",
    "naznachenie" : "Служ",
    "Sherst" : "Плот",
    "Agrassive" : "5",
},
{
    'name': 'Бигль',
    'height': '33-40',
    "ves" : "9-14",
    "naznachenie" : "Охота",
    "Sherst" : "Глад",
    "Agrassive" : "1",
},
{
    'name': 'Шпиц',
    'height': '40-50',
    "ves" : "17-22",
    "naznachenie" : "Дом",
    "Sherst" : "Плот",
    "Agrassive" : "3",
},
{
    'name': 'Доберман',
    'height': '63-72',
    "ves" : "32-45",
    "naznachenie" : "Служ",
    "Sherst" : "Корот",
    "Agrassive" : "3",
},
{
    'name': 'Бультерьер',
    'height': '47-56',
    "ves" : "23-38",
    "naznachenie" : "Дом",
    "Sherst" : "Глад",
    "Agrassive" : "5",
},
{
    'name': 'Далматинец',
    'height': '54-62',
    "ves" : "24-32",
    "naznachenie" : "Охот дом",
    "Sherst" : "Корот",
    "Agrassive" : "4",
},
{
    'name': 'Ротвейлер',
    'height': '56-68',
    "ves" : "38-53",
    "naznachenie" : "Служ",
    "Sherst" : "Глад",
    "Agrassive" : "5",
},
{
    'name': 'Cиба-ину',
    'height': '35-41', 
    "ves" : "7-13",
    "naznachenie" : "Охот",
    "Sherst" : "Плот",
    "Agrassive" : "6",
},
{
    'name': 'Ньюфаундленд',
    'height': '61-76', 
    "ves" : "49-53",
    "naznachenie" : "Служ",
    "Sherst" : "Плот вод",
    "Agrassive" : "2",
}
]
shake_y = 5
shake_xz = 3
height_dog = int(input('Высота собаки: ')) #изменить на входные данные с qt
weight_dog = int(input('Вес собаки: ')) #изменить на входные данные с qt
nazn_dog = str(input('Назначение собаки: ')) #изменить на входные данные с qt
sherst_dog = str(input('Шерсть собаки: ')) #изменить на входные данные с qt

def find_nearbest(in_dic:dict, sl_dic:dict):
    nearbest = []
    prom = []

    for i in sl_dic:
        for j in sl_dic:
            prom.append([i['name'] + '+' + j['name'], 0])

            if round((sr(i['height']) + sr(j['height'])) / 2) >= int(in_dic['height']) - 5 and round((sr(i['height']) + sr(j['height'])) / 2) <= int(in_dic['height']) + shake_y:
                prom[-1][1] += 3

            if round((sr(i['ves']) + sr(j['ves'])) / 2) >= int(in_dic['ves']) - 3 and round((sr(i['ves']) + sr(j['ves'])) / 2) <= int(in_dic['ves']) + shake_y:
                prom[-1][1] += 1

            if i['naznachenie'] == j['naznachenie'] == in_dic['naznachenie']:
                prom[-1][1] += 3
            elif i['naznachenie'] == in_dic['naznachenie'] or j['naznachenie'] == in_dic['naznachenie']:
                prom[-1][1] += 2

            if i['Sherst'] == j['Sherst'] == in_dic['Sherst']:
                prom[-1][1] += 2
            elif i['Sherst'] == in_dic['Sherst'] or j['Sherst'] == in_dic['Sherst']:
                prom[-1][1] += 1
        
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
    'height': height_dog, 
    "ves" : weight_dog,
    "naznachenie" : nazn_dog,
    "Sherst" :  sherst_dog,
}

print(find_nearbest(in_sl, sl))
