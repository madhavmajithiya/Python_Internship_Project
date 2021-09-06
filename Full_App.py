import json
import csv
import datetime
today_date = datetime.date.today()
dicb = dict()
item_dic = dict()
dicc = dict()
lst = list()
dicitem = list()
diccus = list()


#inventory_data = 100001:{'item':'pen', 'stock':'20', 'price':'5', 'category':'stationary', 'expiry_date':'NA'}}

def write_inventory_file(data_file):
    json_inventory_data = json.dumps(data_file)
    inventory_json_file = open("inventory.json", "w")
    inventory_json_file.write(json_inventory_data)
    inventory_json_file.close()
def read_inventory_file():
    inventory_json_file = open("inventory.json", 'r')
    inventory_data = inventory_json_file.read()
    inventory_data = json.loads(inventory_data)
    inventory_json_file.close()
    return inventory_data
def readcustomerfile():
    with open('customer.csv', 'r') as cusfile:
        cus_file = csv.DictReader(cusfile)
        for cus in cus_file:
            dicc[cus['customer']] = cus['payment']
def writecustomerfile():
    diccus = []
    for cus,pay in dicc.items():
        diccus.append({'customer':cus,'payment':dicc[cus]})
    with open('customer.csv','w') as cusfile:
        cusfield = ['customer','payment']
        cuswriter = csv.DictWriter(cusfile, fieldnames = cusfield)
        cuswriter.writeheader()
        for pay in diccus:
            cuswriter.writerow(pay)
inventory_data = {}
print('Welcome To MADBILL SOFTWARE\n\nHear Is The List Of All Function\n\nITEM - To List All Item Available In Inventory\nADD - To Add Item And Its Price And Stock\nBILL - To Create Bill\nPRICE - To Check Price Of Item\nCUSTOMER - To Check Customer Due Payments\nPAY - To Enter Entry Of Customer Payment\nSTOCK - To Check Stock Of Item\nDELETE - To Delete Item From Inventory\n\n')
while True:
    try:
        inventory_data = read_inventory_file()
        readcustomerfile()
    except:
        write_inventory_file(inventory_data)
        writecustomerfile()
    inp = input('What Function You Want To Do(Item, Add, Bill, Pay, Price, Customer, Stock Or Type Exit To Exit Program):-')
    inpl = inp.lower()
    inpl = inpl.rstrip()
    inpl = inpl.lstrip()
    while True:
        if inpl == 'item':
            while True:
                print("How You Want To List Item? \n\n1)By Product Id\n2)List All Items")
                item = input("\nEnter Your Choice(1,2 or Exit To Exit This Function):-")
                item = item.lower()
                item = item.strip()
                if item == 'exit':
                    break
                try:
                    item = int(item)
                except:
                    print("Enter Valid Numeric Choice")
                    continue
                if item == 1:
                    while True:
                        if len(inventory_data) == 0:
                            print("\n***************\n\nNo Item Available\n\n***************")
                            break
                        pid = input("Enter Product Id:-")
                        pid = pid.lower()
                        pid = pid.strip()
                        try:
                            pid = int(pid)
                        except:
                            print("Enter Valid Numeric Product ID")
                            continue
                        found = 0
                        for item in inventory_data:
                            if int(item) == int(pid):
                                print("\n")
                                print("Product ID:-",item)
                                print("Item Name:-",inventory_data[item]['item'].capitalize())
                                print("Price Of Item:-",inventory_data[item]['price'])
                                print("Available Stock:-",inventory_data[item]['stock'])
                                print("Category:-",inventory_data[item]['category'])
                                print("Item Entry Date:-",inventory_data[item]['invent_date'])
                                print("\n***********************")
                                found = 1
                        if found == 0:
                            print("No Item Found")
                            continue
                        break
                elif item == 2:
                    if len(inventory_data) == 0:
                        print("\n***************\n\nNo Item Available\n\n***************")
                        break
                    else:
                        for items in inventory_data:
                            print("\n")
                            print("Product ID:-",items)
                            print("Item Name:-",inventory_data[items]['item'])
                            print("Price Of Item:-",inventory_data[items]['price'])
                            print("Available Stock:-",inventory_data[items]['stock'])
                            print("Category:-",inventory_data[items]['category'])
                            print("Item Entry Date:-",inventory_data[items]['invent_date'])
                            print("\n***********************")
                        break
                else:
                    print('Enter Valid Choice')

        if inpl == 'add':
            while True:
                product_id = input('Enter Product ID (Or Press Exit To Exit This Function):-')
                product_id = product_id.strip()
                if product_id == '':
                    print('Enter Valid Name')
                    continue
                elif product_id == 'no':
                    write_inventory_file(inventory_data)
                    break
                elif product_id == 'quit':
                    write_inventory_file(inventory_data)
                    break
                elif product_id == 'exit':
                    write_inventory_file(inventory_data)
                    break
                elif product_id == 'over':
                    write_inventory_file(inventory_data)
                    break
                try:
                    product_id = int(product_id)
                except:
                    print("Enter Valid Numeric Value")
                    continue
                if str(product_id) in inventory_data:
                    print("************\n\nItem Already Found\n\n************")
                    print("\n")
                    print("Product ID:-",str(product_id))
                    print("Item Name:-",inventory_data[str(product_id)]['item'])
                    print("Price Of Item:-",inventory_data[str(product_id)]['price'])
                    print("Available Stock:-",inventory_data[str(product_id)]['stock'])
                    print("Category:-",inventory_data[str(product_id)]['category'])
                    print("Item Entry Date:-",inventory_data[str(product_id)]['invent_date'])
                    print("\n***********************")
                    while True:
                        price = input("Enter New Price:-")
                        price = price.lower()
                        price = price.strip()
                        try:
                            price = int(price)
                            break
                        except:
                            print("Enter Valid Numeric Input")
                            continue
                    while True:
                        stock = input("Enter Quantity:-")
                        stock = stock.lower()
                        stock = stock.strip()
                        try:
                            stock = int(stock)
                            break
                        except:
                            print("Enter Valid Numeric Input")
                            continue
                    inventory_data[str(product_id)]['price'] = price
                    inventory_data[str(product_id)]['stock'] = int(inventory_data[str(product_id)]['stock']) + int(stock)
                    #print(inventory_data)
                    write_inventory_file(inventory_data)
                    print("***********\n\nItem Updated Successfull\n\n***********")
                    break

                while True:
                    ke = input('Enter Item Name(Or Press EXIT To Exit This Function):-')
                    key = ke.lower()
                    key = key.rstrip()
                    key = key.lstrip()
                    if key == '':
                        print('Enter Valid Name')
                        continue
                    elif key == 'no':
                        write_inventory_file(inventory_data)
                        break
                    elif key == 'quit':
                        write_inventory_file(inventory_data)
                        break
                    elif key == 'exit':
                        write_inventory_file(inventory_data)
                        break
                    elif key == 'over':
                        write_inventory_file(inventory_data)
                        break
                    try:
                        float(key)
                        print('Enter Valid Item Name(Letter)')
                        continue
                    except:
                        None
                    while True:
                        value = input('Enter Price Of Item:-')
                        value = value.rstrip()
                        value = value.lstrip()
                        try:
                            float(value)
                            break
                        except:
                            print('Enter Valid Price(Numeric)')
                            continue
                    while True:
                        stock = input('Enter Stock:-')
                        stock = stock.rstrip()
                        stock = stock.lstrip()
                        try:
                            float(stock)
                            break
                        except:
                            print('Enter Valid Stock(Numeric)')
                            continue
                    try:
                        float(dic_stock[key])
                        #dic_stock[key] = float(dic_stock[key]) + float(stock)
                    except:
                        None
                        #dic_stock[key] = stock
                    while True:
                        print("Select Category\n\n1)Stationary\n2)Cosmetic\n3)Snacks And Foods\n4)Cloathes\n5)Others")
                        s_category = input("Enter Choice:-")
                        s_category = s_category.strip()
                        try:
                            s_category = int(s_category)
                        except:
                            print("Enter Valid Numeric Value")
                            continue
                        if s_category == 1:
                            category = "Stationary"
                            break
                        elif s_category == 2:
                            category = "Cosmetic"
                            break
                        elif s_category == 3:
                            category = "Snacks And Foods"
                            break
                        elif s_category == 4:
                            category = "Cloathes"
                            break
                        elif s_category == 5:
                            category = "Others"
                            break
                    item_dic["item"] = key
                    item_dic["price"] = value
                    item_dic["stock"] = stock
                    item_dic["category"] = category
                    item_dic["invent_date"] = str(today_date)
                    #print(item_dic)
                    inventory_data[product_id] = item_dic
                    #print(inventory_data)
                    item_dic = {}
                    print("****************\n\nItem Added Successfull\n\n****************")
                    break
        if inpl == 'price':
            item = input('Enter Product ID(Or Press EXIT To Exit This Function):-')
            iteml = item.lower()
            iteml = iteml.rstrip()
            iteml = iteml.lstrip()
            if iteml in inventory_data:
                print('Price Of',inventory_data[iteml]['item'].capitalize() + ':-', inventory_data[iteml]['price'])
                continue
            elif iteml == '':
                print('Enter Valid Name')
                continue
            elif iteml == 'no':
                break
            elif iteml == 'quit':
                break
            elif iteml == 'exit':
                break
            elif iteml == 'over':
                break
            else :
                print('No Item Found')
                continue
        if inpl == 'stock':
            item = input('Enter Product ID(Or Press EXIT To Exit This Function):-')
            iteml = item.lower()
            iteml = iteml.rstrip()
            iteml = iteml.lstrip()
            if iteml in inventory_data:
                print('Total Available',inventory_data[iteml]['item'].capitalize() + ':-', inventory_data[iteml]['stock'])
                continue
            elif iteml == '':
                print('Enter Valid Name')
                continue
            elif iteml == 'no':
                break
            elif iteml == 'quit':
                break
            elif iteml == 'exit':
                break
            elif iteml == 'over':
                break
            else :
                print('No Item Found')
                continue
        if inpl == 'delete':
            item = input('Enter Product ID(Or Press EXIT To Exit This Function):-')
            iteml = item.lower()
            iteml = iteml.rstrip()
            iteml = iteml.lstrip()
            if iteml in inventory_data:
                print('Total Available',inventory_data[iteml]['item'].capitalize() + ':-', inventory_data[iteml]['stock'])
                que = input('Do You Want To Delete Item(YES Or NO)')
                quel = que.lower()
                quel = que.rstrip()
                quel = que.lstrip()
                if quel == 'yes':
                    del inventory_data[iteml]
                    print('Item Deleted Successfull')
                    continue
                elif quel == 'no':
                    print('Ok')
                    continue
                else:
                    print('Print Enter Valid Input(Yes Or No')
                    continue
            elif iteml == '':
                print('Enter Valid Name')
                continue
            elif iteml == 'no':
                write_inventory_file(inventory_data)
                break
            elif iteml == 'quit':
                write_inventory_file(inventory_data)
                break
            elif iteml == 'exit':
                write_inventory_file(inventory_data)
                break
            elif iteml == 'over':
                write_inventory_file(inventory_data)
                break
            else :
                print('No Item Found')
                continue
        if inpl == 'customer':
            cuc = input('Enter Customer Name(Or Press EXIT To Exit This Function):-')
            cucl = cuc.lower()
            cucl = cucl.rstrip()
            cucl = cucl.lstrip()
            if cucl in dicc:
                print('Total Due Payment Of',cucl.capitalize() + ':-', dicc[cucl])
                continue
            elif cucl == '':
                print('Enter Valid Name')
                continue
            elif cucl == 'no':
                break
            elif cucl == 'quit':
                break
            elif cucl == 'exit':
                break
            elif cucl == 'over':
                break
            else :
                print('No Customer Found')
                continue
        if inpl == 'pay':
            p = input('Enter Customer Name(Or Press EXIT To Exit This Function):-')
            pl = p.lower()
            pl = pl.rstrip()
            pl = pl.lstrip()
            if pl in dicc:
                print('Total Due Payment Of',pl.capitalize() + ':-', dicc[pl])
                while True:
                    q = input('How Much You Want To Pay Now?')
                    q = q.rstrip()
                    q = q.lstrip()
                    try:
                        float(q)
                        break
                    except:
                        print('Enter Valid Numeric Input.')
                        continue
                dicc[pl] = float(dicc[pl]) - float(q)
                print('****************\n\nPayment Accepted...Your Clear Balance Is',dicc[pl],"\n\n****************")
                writecustomerfile()
                continue
            elif pl == '':
                print('Enter Valid Name.')
                continue
            elif pl == 'no':
                write_inventory_file(inventory_data)
                break
            elif pl == 'quit':
                write_inventory_file(inventory_data)
                break
            elif pl == 'exit':
                write_inventory_file(inventory_data)
                break
            elif pl == 'over':
                write_inventory_file(inventory_data)
                break
            else :
                print('No Customer Found.')
                continue
        if inpl == 'bill':

            if len(inventory_data) < 1:
                print('Please Add Item First.')
                break
            if len(dicb) < 1:
                print('****************\n\nType CHECK When Your Bill Is Ready To Calulate Bill.\n\n****************')
                cu = input('Enter Customer Name(Or Press EXIT To Exit This Function):-')
                cus = cu.lower()
                cus = cus.rstrip()
                cus = cus.lstrip()
                if cus == '':
                    print('Enter Valid Name.')
                    continue
                elif cus == 'no':
                    break
                elif cus == 'quit':
                    break
                elif cus == 'exit':
                    break
                elif cus == 'over':
                    break
            try:
                float(cus)
                print('Enter Valid Name(In Letter)')
            except:
                None
            thing = input('Enter Product ID(Or Press EXIT To Exit This Function):-')
            thingl = thing.lower()
            thingl = thingl.rstrip()
            thingl = thingl.lstrip()
            if thingl == 'check':
                if len(dicb) < 1:
                    print('Blank Bill......Please Enter Item In Bill')
                    continue
                else:
                    for x in dicb:
                        print('Item Name:-',x.capitalize(), ' ' ' ' ' ' 'Quantity:-',dicb[x])
                while True:
                    pb = input('Do You Want To Calculate And Print Bill(YES Or NO):-')
                    pbl = pb.lower()
                    pbl = pbl.rstrip()
                    pbl = pbl.lstrip()
                    if pbl == 'yes':
                        for x in dicb:
                            if len(x) < 1:
                                print('There Is Nothing To Calculate.')
                            else:
                                amount = float(inventory_data[x]['price']) * float(dicb[x])
                                lst.append(amount)
                                inventory_data[x]['stock'] = float(inventory_data[x]['stock']) - float(dicb[x])
                                print('Item Name:-',x.capitalize(), ' ' ' ' ' ' 'Quantity:-',dicb[x], ' ' ' ' ' ' ' ' 'Item Price:-', inventory_data[x]['price'],' ' ' ' ' ' ' ' 'Total Price:-', amount, 'Rs')
                        print('****************\n\nTOTAL AMOUNT:-', sum(lst),"\n\n****************")
                        try:
                            float(dicc[cus])
                            #if float(dicc[cus]) < 0:
                            dicc[cus] = float(dicc[cus]) + sum(lst)
                            half = float(dicc[cus]) / 2
                            halfs = str(half)
                        except:
                            dicc[cus] = sum(lst)
                            half = float(dicc[cus]) / 2
                            halfs = str(half)
                        print('Your Due Amount Is', dicc[cus])
                        print('50%('+ halfs,'Rs)','Payment You Have To Pay.')

                        while True:
                            if half <= float(0):
                                print('Payment Successfull Remaining Balance is',dicc[cus],'Rs')
                                break
                            pay = input('How Much Amount You Want To Pay(Or Press NO To Cancel Bill):-')
                            payl = pay.lower()
                            payl = payl.rstrip()
                            payl = payl.lstrip()
                            if payl == 'no':
                                print('Your Bill Was Cancelled....')
                                break
                            try:
                                float(pay)
                            except:
                                print('Enter Valid Numeric Input')
                                continue
                            if float(pay) >= half:
                                dicc[cus] = float(dicc[cus]) - float(pay)
                                print('***********\n\nPayment Successfull Remaining Balance is',dicc[cus],'Rs\n\n***********')
                                break
                            elif float(pay) < half:
                                print('***********\n\nPlease Pay Atleast Half To Continue\n\n***********')
                                continue
                        writecustomerfile()
                        write_inventory_file(inventory_data)
                        dicb = { }
                        lst = [ ]
                        break
                    elif pbl == 'no':
                        break
                    else:
                        print('Enter Valid Input (Yes Or No)')
                        continue
            try:
                float(thingl)
            except:
                print('Enter Valid Product ID(Numeric)')
                continue
            if thingl in inventory_data:
                print("Item", inventory_data[thingl]['item'].capitalize())
                while thingl in inventory_data:
                    qty = input('Enter Quantity:-')
                    qtyl = qty.lower()
                    qtyl = qtyl.rstrip()
                    qtyl = qtyl.lstrip()
                    try:
                        float(qtyl)
                    except:
                        print('Enter Valid Quantity(Numeric)')
                        continue
                    if float(inventory_data[thingl]['stock']) >= float(qtyl):
                        dicb[thingl] = qtyl
                        print('Item Name:-',inventory_data[thingl]['item'].capitalize(), ' ' ' ' 'Quantity:-', qtyl)
                        break
                    elif float(inventory_data[thingl]['stock']) == 0:
                        print('***********\n\nThere Are 0',inventory_data[thingl]['item'].capitalize(),'Available In Stock.\n\n***********')
                        break
                    else:
                        print('There Are',inventory_data[thingl]['stock'],inventory_data[thingl]['item'].capitalize(),'Available In Stock.')
                        continue

            elif thingl == '':
                print('Enter Valid Name')
                continue
            elif thingl == 'no':
                writecustomerfile()
                write_inventory_file(inventory_data)
                break
            elif thingl == 'quit':
                writecustomerfile()
                write_inventory_file(inventory_data)
                break
            elif thingl == 'exit':
                writecustomerfile()
                write_inventory_file(inventory_data)
                break
            elif thingl == 'over':
                writecustomerfile()
                write_inventory_file(inventory_data)
                break


            else :
                print('No Item Found')
                continue
        elif inpl == 'no':
            writecustomerfile()
            write_inventory_file(inventory_data)
            print('Thank You')
            quit()
        elif inpl == 'quit':
            writecustomerfile()
            write_inventory_file(inventory_data)
            print('Thank You')
            quit()
        elif inpl == 'exit':
            writecustomerfile()
            write_inventory_file(inventory_data)
            print('Thank You')
            quit()
        elif inpl == 'over':
            writecustomerfile()
            write_inventory_file(inventory_data)
            print('Thank You')
            quit()
        else:
            #print('Enter Valid Input(Add, Price, Bill)')
            break
