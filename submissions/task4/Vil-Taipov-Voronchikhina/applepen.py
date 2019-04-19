import csv
import pandas as pd

def csv_dict_reader(file, c):
    
    reader = csv.DictReader(file)
    
    DF_inventory = pd.read_csv("input/MS-" + c + "-inventory.csv")
    DF_supply = pd.read_csv("input/MS-" + c + "-supply.csv")
    
    current_apple = 0
    current_pen = 0
    sold_apple = 0
    sold_pen = 0
    supply_apple = 0
    supply_pen = 0
    stolen_apple = 0
    stolen_pen = 0
    DF_daily = pd.DataFrame(columns = ["date", "apple", "pen"])
    DF_stolen = pd.DataFrame(columns = ["date", "apple", "pen"])
    daily_index = 0
    stolen_index = 0
    supply_index = 0  
    inventory_index = 0
    prev_date = "0000-00-00"
    
    for row in reader:
        if (prev_date == "0000-00-00"):
            prev_date = row["date"]
        if (row["date"] == prev_date):
            if (row["sku_num"][6] == 'a'): 
                sold_apple += 1
            if (row["sku_num"][6] == 'p'):
                sold_pen +=1
            prev_date = row["date"]
        else:
            if (prev_date[8:] == "01") or (prev_date[8:] == "15"): 
                supply_apple += DF_supply["apple"][supply_index]
                supply_pen += DF_supply["pen"][supply_index]
                supply_index +=1
            current_apple = current_apple + supply_apple - sold_apple
            current_pen = current_pen + supply_pen - sold_pen
            if (row["date"][8:] == "01") and (row["date"] != "2006-01-01"):
                stolen_apple = current_apple - DF_inventory["apple"][inventory_index]
                stolen_pen = current_pen - DF_inventory["pen"][inventory_index]
                current_apple = DF_inventory["apple"][inventory_index]
                current_pen =  DF_inventory["pen"][inventory_index]
                inventory_index += 1
                DF_stolen.loc[stolen_index] = [prev_date, stolen_apple, stolen_pen]
                stolen_index += 1
            DF_daily.loc[daily_index] = [prev_date, current_apple, current_pen]
            daily_index += 1
            prev_date = row["date"]
            sold_apple = 0
            sold_pen = 0
            if (row["sku_num"][6] == 'a'): 
                sold_apple += 1
            if (row["sku_num"][6] == 'p'):
                sold_pen +=1
            supply_apple = 0
            supply_pen = 0
    
    current_apple = current_apple - sold_apple
    current_pen = current_pen - sold_pen 
    stolen_apple = current_apple - DF_inventory["apple"][inventory_index]
    stolen_pen = current_pen - DF_inventory["pen"][inventory_index]
    current_apple = DF_inventory["apple"][inventory_index]
    current_pen =  DF_inventory["pen"][inventory_index]
    DF_stolen.loc[stolen_index] = [prev_date, stolen_apple, stolen_pen]
    DF_daily.loc[daily_index] = [prev_date, current_apple, current_pen]
        
    DF_daily.to_csv("output/MS-" + c + "-daily.csv", index = False)
    DF_stolen.to_csv("output/MS-" + c + "-stolen.csv", index = False)
    
    DF_daily.iloc[0]
            
with open("input/MS-b1-sell.csv") as file_obj:
    csv_dict_reader(file_obj, "b1")
with open("input/MS-b2-sell.csv") as file_obj:
    csv_dict_reader(file_obj, "b2")
with open("input/MS-m1-sell.csv") as file_obj:
    csv_dict_reader(file_obj, "m1")
with open("input/MS-m2-sell.csv") as file_obj:
    csv_dict_reader(file_obj, "m2")
with open("input/MS-s1-sell.csv") as file_obj:
    csv_dict_reader(file_obj, "s1")
with open("input/MS-s2-sell.csv") as file_obj:
    csv_dict_reader(file_obj, "s2")
with open("input/MS-s3-sell.csv") as file_obj:
    csv_dict_reader(file_obj, "s3")
with open("input/MS-s4-sell.csv") as file_obj:
    csv_dict_reader(file_obj, "s4")
with open("input/MS-s5-sell.csv") as file_obj:
    csv_dict_reader(file_obj, "s5")
    