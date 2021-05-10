import csv
import matplotlib.pyplot as plt

foodlist = []
date_month = []
with open('Food price.txt', newline = '') as foodprice:
	food_reader = csv.DictReader(foodprice, delimiter='\t')
	for i in food_reader:
		foodlist.append(i)
		if i['date'] not in date_month:
			date_month.append(i['date'])
	foodprice.close()

counter_trial = 0
kondisi = True
while kondisi:
	print()
	ask = int(input(" 1. Statistik \n 2. Grafik \n 3. Keluar \n Masukkan angka :"))
	if ask == 1:
		def desk(list_or_dict,value,key):
			data = []
			for x in list_or_dict:
				if x[key] == value:
					data.append(x)
			return data

		def desk2(list_or_dict, barang):
			data = []
			for y in list_or_dict:
				data.append(y[barang])
			return data

		def stats(input):
			count = len(input)
			price = [int(x) for x in sorted(desk2(input, "price"))]
			mean = sum(price)/len(price)
			if len(price) % 2 == 0:
				median = ((price[int(len(price) / 2)] + price[int(len(price) / 2) - 1]) / 2)
			else:
				median = (price[int(len(price)/2)])
			if len(price) % 2 == 0:
				bawah = price[:int(len(price) / 2)]
				atas = price[int(len(price) / 2):]
			else:
				price.pop(price.index(median))
				bawah = price[:int(len(price) / 2)]
				atas = price[int(len(price) / 2):]

			if len(price) % 2 == 0:
				quartil_bawah = (bawah[int(len(bawah) / 2)] + bawah[int(len(bawah) / 2) - 1]) / 2
				quartil_atas = (atas[int(len(atas) / 2) - 1] + atas[int(len(atas) / 2)]) / 2
			else:
				quartil_bawah = bawah[int((len(bawah) - 1) / 2)]
				quartil_atas = atas[int((len(atas) - 1) / 2)]
			input = {"count": count, "mean": mean, "median": median, "quartile 1" : quartil_bawah, "quartile 2" : median, "quartile 3": quartil_atas}
			return input

		cereals_tubers = stats(desk(foodlist, "cereals and tubers", "category"))
		meat_fish_egg = stats(desk(foodlist, "meat, fish and eggs", "category"))
		vegetables_fruits = stats(desk(foodlist, "vegetables and fruits", "category"))
		milk_dairy = stats(desk(foodlist, "milk and dairy", "category"))
		oil_fats = stats(desk(foodlist, "oil and fats", "category"))
		miscellaneous_food = stats(desk(foodlist, "miscellaneous food", "category"))
		non_food = stats(desk(foodlist, "non-food", "category"))

		ask = int(input(" 1. cereals and tubers \n 2. meat, fish and eggs \n 3. vegetables and fruits \n 4. milk and dairy \n 5. oil and fats \n 6. miscellaneous food \n 7. non-food \n kategori apa yang mau kamu tampilkan?(input angka) :"))
		if ask == 1:
			print(" Banyak data : {} \n Mean data : {} \n Median data : {} \n Kuartil-1 Data : {} \n Kuartil-3 Data : {}".format(cereals_tubers['count'], cereals_tubers['mean'], cereals_tubers['median'], cereals_tubers['quartile 1'], cereals_tubers['quartile 3']))
		elif ask == 2:
			print(" Banyak data : {} \n Mean data : {} \n Median data : {} \n Kuartil-1 Data : {} \n Kuartil-3 Data : {}".format(meat_fish_egg['count'], meat_fish_egg['mean'], meat_fish_egg['median'], meat_fish_egg['quartile 1'], meat_fish_egg['quartile 3']))
		elif ask == 3:
			print(" Banyak data : {} \n Mean data : {} \n Median data : {} \n Kuartil-1 Data : {} \n Kuartil-3 Data : {}".format(vegetables_fruits['count'], vegetables_fruits['mean'], vegetables_fruits['median'], vegetables_fruits['quartile 1'], vegetables_fruits['quartile 3']))
		elif ask == 4:
			print(" Banyak data : {} \n Mean data : {} \n Median data : {} \n Kuartil-1 Data : {} \n Kuartil-3 Data : {}".format(milk_dairy['count'], milk_dairy['mean'], milk_dairy['median'], milk_dairy['quartile 1'], milk_dairy['quartile 3']))
		elif ask == 5:
			print(" Banyak data : {} \n Mean data : {} \n Median data : {} \n Kuartil-1 Data : {} \n Kuartil-3 Data : {}".format(oil_fats['count'], oil_fats['mean'], oil_fats['median'], oil_fats['quartile 1'], oil_fats['quartile 3']))
		elif ask == 6:
			print(" Banyak data : {} \n Mean data : {} \n Median data : {} \n Kuartil-1 Data : {} \n Kuartil-3 Data : {}".format(miscellaneous_food['count'], miscellaneous_food['mean'], miscellaneous_food['median'], miscellaneous_food['quartile 1'], miscellaneous_food['quartile 3']))
		elif ask == 7:
			print(" Banyak data : {} \n Mean data : {} \n Median data : {} \n Kuartil-1 Data : {} \n Kuartil-3 Data : {}".format(non_food['count'], non_food['mean'], non_food['median'], non_food['quartile 1'], non_food['quartile 3']))

	elif ask == 2:
		def key_values_binding(foodlist, column):
			list_kategori = []
			for i in foodlist:
				list_kategori.append(i[column])
			return list_kategori

		def graf(comodity):
			dataname_percomodity = []
			for x in foodlist:
				if x["cmname"] == comodity:
					dataname_percomodity.append(x)
			price = [int(x) for x in key_values_binding(dataname_percomodity, "price")]
			date = key_values_binding(dataname_percomodity, "date")
			# kerosin adalah komoditi yang hanya ada ditahun 2013
			if comodity == "Fuel (kerosene) - Retail":
				price_2013 = [price[date.index(x)] for x in date if '2013' in x]
				mean_2013 = sum(price_2013) / len(price_2013)
				mean_total = [mean_2013]
			else:
				price_2013 = [price[date.index(x)] for x in date if '2013' in x]
				price_2014 = [price[date.index(x)] for x in date if '2014' in x]			
				price_2015 = [price[date.index(x)] for x in date if '2015' in x]			
				price_2016 = [price[date.index(x)] for x in date if '2016' in x]			
				price_2017 = [price[date.index(x)] for x in date if '2017' in x]
				# menghitung rata-rata untuk data tahunan
				mean_2013 = sum(price_2013) / len(price_2013)
				mean_2014 = sum(price_2014) / len(price_2014)
				mean_2015 = sum(price_2015) / len(price_2015)
				mean_2016 = sum(price_2016) / len(price_2016)
				mean_2017 = sum(price_2017) / len(price_2017)
				mean_total = [mean_2013, mean_2014, mean_2015, mean_2016, mean_2017]
			return {'price': price, "date": date, "mean_total": mean_total}

		graf_rice = graf("Rice - Retail")
		graf_wheat = graf("Wheat - Retail")
		graf_chicken = graf("Meat (chicken, broiler) - Retail")
		graf_greenchili = graf("Chili (green) - Retail")
		graf_redchili = graf("Chili (red) - Retail")
		graf_egg = graf("Eggs - Retail")
		graf_milk = graf("Milk (condensed) - Retail")
		graf_oil = graf("Oil (vegetable) - Retail")
		graf_sugar = graf("Sugar - Retail")
		graf_beef = graf("Meat (beef) - Retail")
		graf_fuel = graf("Fuel (kerosene) - Retail")

		all_food_graf = [graf_rice, graf_wheat, graf_chicken, graf_greenchili, graf_redchili, graf_egg, graf_milk, graf_oil, graf_sugar, graf_beef, graf_fuel]
		all_linecolor = ["orange", "red", "blue", "green", "yellow", "black", "purple", "silver", "pink", "brown", "cyan"]
		all_comodity = ['Rice', 'Wheat', 'Chicken', 'Chili (Green)', 'Chili (Red)', 'Eggs', 'Milk', 'Oil', 'Sugar', '(Beef)', 'Fuel']

		ask = int(input("\n 1. data perbulan \n 2. data pertahun \n Masukkan angka :"))
		if ask == 1:
			#plotting into visual data
			plt.figure(figsize=(12, 15))
			ax = plt.subplot(1, 1, 1)
			ax.set_xticklabels(date_month)
			for i in range(11):
				plt.plot(all_food_graf[i]['date'], all_food_graf[i]['price'], color = all_linecolor[i], label = all_comodity[i])
			plt.legend()
			plt.title("Comodity Price Comparison Per-Month")
			plt.xticks(rotation = 45)
			plt.show()
		if ask == 2:
			plt.figure(figsize=(12, 15))
			years = ["2013", "2014", "2015", "2016", "2017"]
			for i in range(10):
				plt.plot(years, all_food_graf[i]['mean_total'], color = all_linecolor[i], label = all_comodity[i])
			plt.plot("2013", all_food_graf[10]['mean_total'], color = all_linecolor[10], label = all_comodity[10])
			plt.legend()
			plt.title("Comodity Price Comparison Per-Year")
			plt.show()

	elif ask == 3:
		print(" terimakasih, anda akan keluar dalam beberapa milisecond!")
		exit()
	else:
		counter_trial += 1
		print(f" pilih salah satu dari opsi! gagal {counter_trial} kali \n")
		if counter_trial == 3:
			print("anda akan keluar dalam beberapa milisecond!")
			exit()