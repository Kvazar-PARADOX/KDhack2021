#!C:\Users\Ученик\AppData\Local\Programs\Python\Python39\python.exe
import cgi
import cgitb
cgitb.enable()
sl = [{
    'name': 'Mops',
    'height': '27-36',
    "ves": "6-8",
    "naznachenie": "Дом",
    "Sherst": "Глад",
},
    {
        'name': 'Retryver',
        'height': '52-61',
        "ves": "26-40",
        "naznachenie": "Охот",
        "Sherst": "Вод",
    },
    {
        'name': 'Rasser Teryer',
        'height': '22-30',
        "ves": "5-6",
        "naznachenie": "Охот",
        "Sherst": "Глад",
    },
    {

        'name': 'Nemeckaya Ovcharka',
        'height': '55-65',
        "ves": "22-40",
        "naznachenie": "Служ",
        "Sherst": "Плот",
    },
    {
        'name': 'Angliyskii Buldog',
        'height': '50-55',
        "ves": "24-25",
        "naznachenie": "Дом",
        "Sherst": "Глад",
    },
    {
        'name': 'Akyta-Inu',
        'height': '60-70',
        "ves": "20-40",
        "naznachenie": "Охот",
        "Sherst": "Плот",
    },
    {
        'name': 'Serbynar',
        'height': '65-85',
        "ves": "70-85",
        "naznachenie": "Служ",
        "Sherst": "Плот",
    },
    {
        'name': 'Hasky',
        'height': '50-60',
        "ves": "15-28",
        "naznachenie": "Служ",
        "Sherst": "Плот",
    },
    {
        'name': 'Bygl',
        'height': '33-40',
        "ves": "9-14",
        "naznachenie": "Охот",
        "Sherst": "Глад",
    },
    {
        'name': 'Shpyc',
        'height': '40-50',
        "ves": "17-22",
        "naznachenie": "Дом",
        "Sherst": "Плот",
    },
    {
        'name': 'Doberman',
        'height': '63-72',
        "ves": "32-45",
        "naznachenie": "Служ",
        "Sherst": "Корот",
    },
    {
        'name': 'Bulteryer',
        'height': '47-56',
        "ves": "23-38",
        "naznachenie": "Дом",
        "Sherst": "Глад",
    },
    {
        'name': 'Dalmatyn',
        'height': '54-62',
        "ves": "24-32",
        "naznachenie": "Дом",
        "Sherst": "Корот",
    },
    {
        'name': 'Rotveyler',
        'height': '56-68',
        "ves": "38-53",
        "naznachenie": "Служ",
        "Sherst": "Глад",
    },
    {
        'name': 'Syba-Inu',
        'height': '35-41',
        "ves": "7-13",
        "naznachenie": "Охот",
        "Sherst": "Плот",
    },
    {
        'name': 'Newfundland',
        'height': '61-76',
        "ves": "49-53",
        "naznachenie": "Служ",
        "Sherst": "Вод",
    }
]
form = cgi.FieldStorage()
height_dog = form.getfirst("INT_1", "int")
weight_dog = form.getfirst("INT_2", "int")
nazn_dog = form.getfirst("TEXT_1", "не задано")
sherst_dog = form.getfirst("TEXT_2", "не задано")
shake_y = 5
shake_xz = 4


def find_nearbest(in_dic: dict, sl_dic: dict):
    nearbest = []
    prom = []

    for i in sl_dic:
        for j in sl_dic:
            prom.append([i['name'] + ' + ' + j['name'], 0])

            if round((sr(i['height']) + sr(j['height'])) / 2) >= int(in_dic['height']) - 5 and round(
                    (sr(i['height']) + sr(j['height'])) / 2) <= int(in_dic['height']) + shake_y:
                prom[-1][1] += 3

            if round((sr(i['ves']) + sr(j['ves'])) / 2) >= int(in_dic['ves']) - 3 and round(
                    (sr(i['ves']) + sr(j['ves'])) / 2) <= int(in_dic['ves']) + shake_y:
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
    ret = (int(lst[0]) + int(lst[1])) / 2
    return ret


in_sl = {
    'height': height_dog,
    "ves": weight_dog,
    "naznachenie": nazn_dog,
    "Sherst": sherst_dog,
}

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html lang="ru">
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
            <link rel="icon" type="image/png" href="images/icons/favicon.ico"/>
	        <link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
	        <link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
	        <link rel="stylesheet" type="text/css" href="fonts/Linearicons-Free-v1.0.0/icon-font.min.css">
	        <link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
	        <link rel="stylesheet" type="text/css" href="vendor/css-hamburgers/hamburgers.min.css">
	        <link rel="stylesheet" type="text/css" href="vendor/animsition/css/animsition.min.css">
	        <link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
	        <link rel="stylesheet" type="text/css" href="vendor/daterangepicker/daterangepicker.css">
	        <link rel="stylesheet" type="text/css" href="css/util.css">
	        <link rel="stylesheet" type="text/css" href="css/main.css">
	        <script src ="vendor/jquery/jquery-3.2.1.min.js"></script>
            <script src ="vendor/animsition/js/animsition.min.js"></script>
            <script src ="vendor/bootstrap/js/popper.js"></script>
            <script src ="vendor/bootstrap/js/bootstrap.min.js"></script>
            <script src ="vendor/select2/select2.min.js"></script>
            <script src ="vendor/daterangepicker/moment.min.js"></script>
            <script src ="vendor/daterangepicker/daterangepicker.js"></script>
            <script src ="vendor/countdowntime/countdowntime.js"></script>
            <script src ="js/main.js"></script>
        </head>
        <body>""")
pre_result = find_nearbest(in_sl, sl)
result = pre_result[0].split("+")
resul_1 = result[0]
resul_2 = result[1]
sovmes = pre_result[1]
print("""<div class="limiter">
		<div class="container-login100">
			<div class="wrap-login100 p-t-1500 p-b-1200">
				<form action="webserver_script.py" class="login100-form validate-form flex-sb flex-w">
					<span class="login100-form-title p-b-51">
						<h1>Genetic Code Manipulator</h1>
					</span>""")
print("<h1>{}<h1>".format(pre_result))
print("""	</div>
		</div>
	</div>""")

print("""</body>
        </html>""")
