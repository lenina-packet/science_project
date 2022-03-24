from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"input.html")

def addition(request):

    count_office = request.POST['count_office']
    count_level = request.POST['count_level']
    count_humans = request.POST['count_humans']
    cars = request.POST['cars']
    count_kw =  request.POST['count_kw']
    count_gas = request.POST['count_gas']
    weather = request.POST['weather']
    rek = ['Установка теплоотражающих щитов из пенофола с фольгой: ', \
    'Установка контейнеров для раздельного сбора мусора: ',\
    'Утепление окон и дверей, герметизация плинтусов и других мест утечек тепла: ',\
    'Использование энергоэффективных систем освещения: ', \
    'Необходимо высадить деревья в количестве: ']

    val = ['Улучшение теплоизоляции. Стоимость материала в один кабинет: 3.6 тыс. рублей. ', \
    'Раздельный сбор мусора. Стоимость одного контейнера: 20 тыс. рублей.  ', \
    'Улучшение энергоэффективности здания. Стоимость одной солнечной батареи: 20 тыс. рублей. (1 панель = 2.5 кв. м).', \
    'Общая стоимость всех затрат для проведения мероприятий: ']

    if  count_office.isdigit() and count_level.isdigit() and count_humans.isdigit() \
    and cars.isdigit() and count_kw.isdigit() and count_gas.isdigit():
        count_office = int(count_office)
        count_level = int(count_level)
        count_humans = int(count_humans)
        cars = int(cars)
        count_kw = int(count_kw)
        count_gas = int(count_gas)
        result_office =  0.7 * 0.035 * count_office * count_humans * 8 * 20 * 1.05 * count_level
        if weather == "Лето":
            result_car = cars * 0.217 * 5 * 20 * 0.001
        if weather == "Зима":
            result_car = cars * 0.217 * 30 * 20 * 0.001
        result_kw = count_kw * 0.396
        result_gas = 154 * count_gas
        result = result_office + result_car + result_kw + result_gas 
        print('result', result, result_office, result_car, result_kw, result_gas)
        # render(request,"result.html",{"result":result}) 
        
        rek[0] += "Позволяет уменьшить концентрацию C02 на " + str(round(result_gas * 0.15)) + " кг."
        rek[1] += "Позволяет уменьшить концентрацию C02 на " + str(round(result_office * 0.10)) + " кг."
        rek[2] += "Позволяет уменьшить концентрацию C02 на " + str(round(result_gas * 0.15)) + " кг."  
        rek[3] += "Позволяет уменьшить концентрацию C02 на " + str(round(result_kw* 0.15)) + " кг."
        for count_drevo in range (10**8):
            if count_drevo * 6.5 >= result:
                break
        rek[4] += str(count_drevo) + " штук. Стоимость посадки всех деревьев: " + str(round(count_drevo * 150 / 1000)) + " тыс. рублей."
        val[0] += "Примерная стоимость для вашего здания: " + str(round(3600 * count_office * count_level / 1000)) + " тыс. рублей."
        val[1] += "Примерная стоимость для вашего здания: " + str(round(20000* count_office / 1000)) + " тыс. рублей."
        val[3] += str(round((count_drevo * 150 + 3600 * count_office * count_level + 20000* count_office + count_drevo * 150)/1000)) + " тыс. рублей."
        print(rek[4])
        return render(request,"result.html",{"result":round(result), "result_office":round(result_office), "result_car":round(result_car), \
            "result_kw":round(result_kw), "result_gas":round(result_gas), "rec1": rek[0], "rec2":rek[1], \
            "rec3": rek[2], "rec4": rek[3], "val1": val[0], "val2": val[1], "val3": val[2], "val4": val[3], "rek5": rek[4]})
        
    else:
        result= "Введите коректные значения!"
        return render(request,"result.html",{"result":result})

def subtration(request):
    pass

def multiplication(request):
    pass



def division(request):
    pass