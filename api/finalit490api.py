import requests
import json
from difflib import SequenceMatcher
import time

calgoal = 0
favrcipe = []
foodhistory = []
currentcal = 0
perstats = {}
budget = 0

def price_cal(ingre=[]):

    url = "https://walmart-search.p.rapidapi.com/search.php"
    holder = []
    total = 0.00
    #print(ingre)
    for i in ingre:
        bestname = ""
        oldperc = 0
        bestprice = 3.00
        x = i
        querystring = {"query": x, "page": "1"}
        headers = {
            'x-rapidapi-key': "b380c9703emsh4735d7f5311ebdep132f4ejsn6294dd54e04a",
            'x-rapidapi-host': "walmart-search.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        pricedata = response.text
        #print(pricedata)
        priceholder = json.loads(pricedata)
        #info = price_finder(pricedata, x)
        #print(info)

        for runner in priceholder['items']:
            name = runner['title']
            #print(name)
            newprice = runner['price']
            #print(newprice)
            comp = SequenceMatcher(None, x, name)
            perc = comp.ratio()

            if(perc > oldperc and newprice < bestprice):
                bestname = name
                oldperc = perc
                bestprice = newprice

        holder.append([bestname,bestprice])
    #print(holder)
    for x in holder:
        gprice = x[1]
        total += int(gprice)
    #print("THIS IS PRICE TOTAL FOR RECIPE " + str(total))
    return(total)


def budgetmeal():
    global budget
    budget = int(input("What is your budget per meal?: $"))
    name = input("What is the recipe name or ingredient?: ")
    params = (
        ('q', name),
        ('app_id', 'e4e162ee'),
        ('app_key', 'cc1c56d90b0a698d3fbd6b42d2c4dda3'),
        ('from', '0'),
        ('to', '10'),
    )
    response = requests.get('https://api.edamam.com/search', params=params)
    data = response.text
    datarunner = json.loads(data)
    counter = 0
    budgetmeal = []
    for it in datarunner['hits']:
        counter += 1
        name = (it['recipe']['label'])
        print("\n")
        #print(str(counter) + ")" + name)
        calo = (it['recipe']['calories'])
        incal = int(calo)
        serves = (it['recipe']['yield'])
        calpserv = incal / serves
        calperserv = str(int(calpserv))
        #print("Calories per serving: " + calperserv)
        ingredients = (it['recipe']['ingredientLines'])
        readableI = ', '.join(ingredients)
        price = price_cal(ingredients)
        print(price)
        if(price < budget):
            budgetmeal.append([name, calperserv, readableI])
        #print(budgetmeal)
        # print(type(ingredients))
        # print("THIS IS INGREDIENT LIST BELOW")
        #print(readableI)
        #instruct = (it['recipe']['shareAs'])
        #print(instruct)
        #reciplelist.append([name, calperserv, readableI])
        # return(reciplelist)
        # print("\n")
    return(budgetmeal)


def historyholder():
    print(perstats)
    leftcal = float(calgoal) - float(currentcal)
    print("\nThis user has " + str(int(leftcal)) + " calories remaining")
    print("\nThis is user's eating log for today:")
    for y in foodhistory:
        print(y)
    print("\nThis is user's favorite recipe list: ")
    for x in favrcipe:
        print(x)

#Will get details for ingredients or recipe
def ingredientP(option):
    holderlist = []
    if (option == 1):
        #This is to get details per ingredient
        url = "https://trackapi.nutritionix.com/v2/search/instant/"

        # querystring = {"fields":"item_name,item_id,brand_name,nf_calories,nf_total_fat"}
        # querystring = {"query":"cheese", "detailed": "1"}

        item = input("What item?: ")
        querystring = {"query": item, "detailed": "0", "claims": "1"}

        headers = {
            'x-app-id': "ec49ed00",
            'x-app-key': "fbaaed8f8bb4905778fdfb64c7d66bd2"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        #print(response.text)
        namelist = []
        queryans = response.text
        dataint = json.loads(queryans)
        for it in dataint['common']:
            name = (it['food_name'])
            namelist.append(name)
            print(name)

        url2 = "https://trackapi.nutritionix.com/v2/natural/nutrients"
        headers2 = {"Content-Type": "application/x-www-form-urlencoded", 'x-app-id': 'ec49ed00',
                    "x-app-key": 'fbaaed8f8bb4905778fdfb64c7d66bd2'}
        calList = []
        y = 0
        #tester = "hold"
        for x in namelist:
            newitem = x
            print(newitem)
            data = {"query": newitem}
            response = requests.post(url2, data=data, headers=headers2)
            #print(response.text)
            queryans = response.text
            dataint2 = json.loads(queryans)
            foods = dataint2['foods']
            calamount = foods[0]['nf_calories']
            print(calamount)
            holderlist.append([newitem, calamount])
            y+=1
        return(holderlist)

    elif (option == 2):
        #this is to get details of the recipe
        name = input("What is the recipe name or ingredient?: ")
        params = (
            ('q', name),
            ('app_id', 'e4e162ee'),
            ('app_key', 'cc1c56d90b0a698d3fbd6b42d2c4dda3'),
            ('from', '0'),
            ('to', '5'),
            # ('calories', '591-722'),
            # ('health', 'alcohol-free'),
        )
        response = requests.get('https://api.edamam.com/search', params=params)
        # print(type(response))
        data = response.text
        #print(response.text)
        datarunner = json.loads(data)
        counter = 0
        reciplelist = []
        for it in datarunner['hits']:
            counter +=1
            name = (it['recipe']['label'])
            print("\n")
            print(str(counter) + ")" +name)
            calo = (it['recipe']['calories'])
            incal = int(calo)
            #print(incal)
            serves = (it['recipe']['yield'])
            calpserv = incal / serves
            calperserv = str(int(calpserv))
            print("Calories per serving: " + calperserv)
            ingredients = (it['recipe']['ingredientLines'])
            readableI = ', '.join(ingredients)
            #price_cal(ingredients)
            # print(type(ingredients))
            #print("THIS IS INGREDIENT LIST BELOW")
            print(readableI)
            instruct = (it['recipe']['shareAs'])
            print(instruct)
            reciplelist.append([name,calperserv,readableI])
            #return(reciplelist)
            #print("\n")
        return(reciplelist)

    '''
        sql = "INSERT INTO fooddata (name, details) VALUES (%s,%s)"
        val = (name, calo)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted")
    '''
#will calculate basic metabolic rate for customer
def calBMR(pW, pH, pA, pG):
    if(pG == "m"):
        maleBMR = (10* pW) + (6.25*pH) - (5*pA) + 5
        return maleBMR
    else:
        femaleBMR = (10*pW) + (6.25*pH) - (5*pA) - 161
        return femaleBMR

#will contains questions to build the customer their profile and give them their calorie goal
def profilebuilder():
    global perstats
    name = input("What is your name: ")
    height = input("What is your height(inches): ")
    weight = input("What is your weight(lbs): ")
    gender = input("What is your gender(m/f): ")
    age = int(input("How old are you?: "))

    heightCM = float(height) * 2.54
    weightKG = float(weight) * .45359237

    answer = input("What is your goal? Gain weight, Lose Weight or Maintain Weight(Gain, Lose, Maintain): ")

    if (answer.upper() == "GAIN" or answer == "LOSE"):
        rate = float(input("At what weekly rate: \n .5 lb  \n 1 lb  \n 1.5 lb  \n 2 lb \n:"))

    elif (answer.upper() == "MAINTAIN"):
        print("ok")

    result = (calBMR(weightKG, heightCM, age, gender))
    # print(calBMR(weightKG, heightCM, age, gender))
    print("Your BMR is: " + str(result))

    if (answer.upper() == "GAIN"):
        CalGoal = result + (rate * 500)
    elif (answer.upper() == "LOSE"):
        CalGoal = result - (rate * 500)
    else:
        CalGoal = result

    perstats = {name: [height, weight, gender, age]}
    #historyholder(perstats)

    print("Based on your profile, your new calorie goal is: " + str(CalGoal))
    return(CalGoal)



#this will ask for user email and send an reminder to track breakfast, lunch, and dinner
def emailsender():
    addy = input("email: ")

    while True:
        time.sleep(31)
        t = time.localtime()
        current_time = time.strftime("%H:%M", t)
        print(current_time)

        if (current_time == '09:40'):
            body = "HEY! Don't forget to have your breakfast and to log it"
            break
        elif (current_time == '12:00'):
            body = "LUNCH TIME. Take a break and eat...."
            break
        elif (current_time == '22:08'):
            body = "It is time for dinner, make sure to log your meals to stay on track"
            break

    #addy = input("email: ")
    response = requests.post(
        "https://api.mailgun.net/v3/sandboxe7f75336315147b0b3974223573a8e9e.mailgun.org/messages",
        auth=("api", "a4c79013cd1c5d5078beb59a6a5686b6-e49cc42c-090f7e45"),
        data={"from": "Excited User <mailgun@sandboxe7f75336315147b0b3974223573a8e9e.mailgun.org>",
                "to": addy,  # ["thetriadsit490@gmail.com"],
                "subject": "Hello",
                "text": body})  # "Testing some Mailgun awesomness!"})
    print(response.text)



while True:
    task = int(input("\nWhat would you like to do? \n1)Set profile\n2)Log Food\n3)Meal Suggestion:\n4)Recipe Search\n5)Personal Stats and History\n6)Push Notification\n7)End Program\nYour Answer: "))
    if(task == 1):
        #global calgoal
        calgoal = profilebuilder()
        #print(calgoal)
    elif(task == 2):
        #globals currentcal
        choice = int(input("1)Ingredient\n2)Recipe\nYour Answer: "))
        resp = ingredientP(choice)
        counter = 0
        for x in resp:
            counter += 1
            print(str(counter) + ")")
            print(x)
        logchoice = int(input("\nWhat item would you like to log?: "))
        foodhistory.append(resp[logchoice-1])
        #print(foodhistory)
        if(choice == 1):
            cal = resp[1]
            realcal = cal[1]
            # print(cal)
            currentcal += int(realcal)
            print("You have just logged " + str(cal))
            print("You have just logged " + str(realcal) + " calories")
            print("You have eaten " + str(currentcal) + " calories so far")
            leftcal = float(calgoal) - float(currentcal)
            print("You have " + str(leftcal) + " calories left for today")
        elif(choice == 2):
            #print(resp)
            rename = resp[logchoice -1]
            seccal = resp[logchoice-1][1]
            currentcal += int(seccal)
            #print(seccal)
            print("You have just logged " + str(rename))
            print("You have just logged " + str(seccal) + " calories")
            print("You have eaten " + str(currentcal) + " calories so far")
            leftcal = float(calgoal) - float(currentcal)
            print("You have " + str(leftcal) + " calories left for today")

    elif(task == 3):
        #global budget
        print("Budget friendly meal suggestion\n")
        #budget = int(input("What is your budget per meal?: $"))
        bmeals = budgetmeal()
        counter = 0
        for x in bmeals:
            counter += 1
            print(str(counter) + ")")
            print(x)
        favchoice = int(input("\nWhat recipe would you like to favorite?: "))
        favrcipe.append(bmeals[favchoice - 1])

    elif(task == 4):
        currlist = []
        holder = ingredientP(2)
        currlist.append(holder)
        #print("This is holder:\n")
        counter = 0
        for x in holder:
            counter += 1
            print(str(counter) + ")")
            print(x)
        favchoice = int(input("\nWhat recipe would you like to favorite?: "))
        favrcipe.append(holder[favchoice-1])
        #print(favrcipe)

    elif(task == 5):
        historyholder()

    elif(task == 6):
        emailsender()

    elif(task == 7):
        quit()
