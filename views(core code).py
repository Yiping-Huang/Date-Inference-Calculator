from django.shortcuts import render, redirect

def datecalculate(request):
	""" Infer the date after or between certain days. """
	check_1 = 0
	check_2 = 0
	leap_year = [ 0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
	common_year = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

	if request.POST.get('year_1') and request.POST.get('month_1') and request.POST.get('day_1') and request.POST.get('interval_1'):
		check_1 = 1
		year_1 = int(request.POST.get('year_1'))
		month_1 = int(request.POST.get('month_1'))
		day_1 = int(request.POST.get('day_1'))
		interval_1 = int(request.POST.get('interval_1'))
		ini_interval_1 = interval_1
		ini_result_1 = str(year_1) + "/" + str(month_1) + "/" + str(day_1)
		year_3 = year_1
		month_3 = month_1
		day_3 = day_1 + interval_1

		if month_1 > 12  or month_1 <= 0  or year_1 <= 0 or day_1 <= 0:
			result_1 = "您输入了不合适的数据！You have submitted improper data!"
	
		elif year_1 % 4 == 0 and day_1 > leap_year[month_1] or year_1 % 4 != 0 and day_1 > common_year[month_1]:
			result_1 = "您输入了不合适的数据！You have submitted improper data!"
		
		else:
			while interval_1 > 0:    
				if month_3 < 12 and year_3 % 4 != 0 and day_3 > common_year[month_3]:
					day_3 = day_3 - common_year[month_3]
					month_3 = month_3 + 1
					interval_1 = day_3
					continue
    
				if month_3 < 12 and year_3 % 4 == 0 and day_3 > leap_year[month_3]:
					day_3 = day_3 - leap_year[month_3]
					month_3 = month_3 + 1
					interval_1 = day_3
					continue
    
				if month_3 == 12 and year_3 % 4 != 0 and day_3 > common_year[month_3]:
					day_3 = day_3 - common_year[month_3]
					month_3 = 1
					year_3 = year_3 + 1
					interval_1 = day_3
					continue
    
				if month_3 == 12 and year_3 % 4 == 0 and day_3 > leap_year[month_3]:
					day_3 = day_3 - leap_year[month_3]
					month_3 = 1
					year_3 = year_3 + 1
					interval_1 = day_3
					continue

				else:
					interval_1 = 0
					break

			result_1 = ini_result_1 + " 之后 " + str(ini_interval_1) + " 天的日期是 " +  str(year_3) + "/" + str(month_3) + "/" + str(day_3) +"。" + str(ini_interval_1) + " days after " + ini_result_1 + " is " + str(year_3) + "/" + str(month_3) + "/" + str(day_3) +"."

	if request.POST.get('year_2') and request.POST.get('month_2') and request.POST.get('day_2') and request.POST.get('interval_2'):
		check_2 = 1
		year_2 = int(request.POST.get('year_2'))
		month_2 = int(request.POST.get('month_2'))
		day_2 = int(request.POST.get('day_2'))
		interval_2 = int(request.POST.get('interval_2'))
		ini_interval_2 = interval_2
		ini_result_2 = str(year_2) + "/" + str(month_2) + "/" + str(day_2)
		year_4 = year_2
		month_4 = month_2
		day_4 = day_2 - interval_2

		if month_2 > 12 or month_2 <= 0 or year_2 <= 0 or day_2 <=0:
			result_2 = "您输入了不合适的数据！You have submitted improper data!"

		elif year_2 % 4 == 0 and day_2 > leap_year[month_2] or year_2 % 4 != 0 and day_2 > common_year[month_2]:
			result_2 = "您输入了不合适的数据！You have submitted improper data!"
		
		else:
			while interval_2 > 0:    
				if month_4 > 1 and year_4 % 4 != 0 and day_4 < 0:
					month_4 = month_4 - 1
					day_4 = day_4 + common_year[month_4]
					interval_2 = abs(day_4)
					continue
    
				if month_4 > 1 and year_4 % 4 == 0 and day_4 < 0:
					month_4 = month_4 - 1
					day_4 = day_4 + leap_year[month_4]
					interval_2 = abs(day_4)
					continue
    
				if month_4 == 1 and year_4 % 4 != 0 and day_4 < 0:
					month_4 = 12
					day_4 = day_4 + common_year[month_4]
					year_4 = year_4 - 1
					interval_2 = abs(day_4)
					continue
    
				if month_4 == 1 and year_4 % 4 == 0 and day_4 < 0:
					month_4 = 12
					day_4 = day_4 + leap_year[month_4]
					year_4 = year_4 - 1
					interval_2 = abs(day_4)
					continue

				else:
					interval_2 = 0
					break

			result_2 = ini_result_2 + " 之前 " + str(ini_interval_2) + " 天的日期是 " +  str(year_4) + "/" + str(month_4) + "/" + str(day_4) +"。" + str(ini_interval_2) + " days before " + ini_result_2 + " is " + str(year_4) + "/" + str(month_4) + "/" + str(day_4) +"."

	if check_1 + check_2 == 0:
		result_1 = "您尚未输入完整数据！You have not submitted complete data yet!"
		result_2 = ""	

	if check_1 == 1 and check_2 == 0:
		result_2 = ""	
	
	if check_1 == 0 and check_2 == 1:
		result_1 = ""	


	context = {'result_1': result_1, 'result_2': result_2}
	return render(request, 'ect_cal/datecalculate.html', context)
