from django.shortcuts import render
from busapp import form
from busapp import models
import datetime
from django.db import connection
import requests
from django.core.mail import send_mail
import json
my_cursor=connection.cursor()
def sendPostRequest(reqUrl,apiKey,secretKey,useType,phoneNo,senderId,textMessage):
	req_params={
		'apiKey':apiKey,
		'secret':secretKey,
		'useType':useType,
		'phone':phoneNo,
		'message':textMessage,
		'senderId':senderId
	}
	return requests.post(reqUrl,req_params)
def Booking_details(request):
	date=datetime.datetime.now()
	msg="Book your tickets!!!"
	Book_lst=form.Bus_booking

	if request.method=='POST':
		book_data=form.Bus_booking(request.POST)
		if book_data.is_valid():
			E_MAIL=book_data.cleaned_data['EMAIL']
			sql='select * from bus.busapp_busbooking where `EMAIL`=%s'
			e_data=(E_MAIL,)
			my_cursor.execute(sql,e_data)
			record=my_cursor.fetchone()
			print(record)
			if record !=None:
				if E_MAIL==record[2]:
					return render(request,'busapp/mailExists.html')

			else:
			    book_data.save(commit=True)
			    P=book_data.cleaned_data['PH_NO']
			    Phnum=int(P)
			    sendPostRequest('https://www.sms4india.com/api/v1/sendCampaign','4VCQPOYTK7USW3BN2G0522FTCCJFS348','9UF6MP9RNBK4L5DH','stage',Phnum,'nishvikaabcbtm@gmail.com',f"hello,{book_data.cleaned_data['NAME']},You have successfully registered!!")
			    send_mail('hello','from Busbooking','nishvikaabcbtm@gmail.com',[f'{E_MAIL}'])	
	my_dict={'Book_lst':Book_lst,'msg':msg,'date':date}
	return render(request,'busapp/display.html',context=my_dict)

def result(request):
	sq_query='select * from bus.busapp_welcome_form'
	my_cursor.execute(sq_query)
	recr=my_cursor.fetchone()
	BNAME=recr[3]
	BTIME=recr[4]
	dict3={'Ob1':BNAME,'Ob2':BTIME}
	return render(request,'busapp/result.html',context=dict3)


def failure(request):
	return render(request,'busapp/Nobus.html')

def Welcome(request):
	sd=form.Welcome_F
	if request.method=='POST':
		data=form.Welcome_F(request.POST)

		if data.is_valid():
			FROM_H=data.cleaned_data['FROM']
			TO_H=data.cleaned_data['TO']
			
			sql_query='select * from bus.busapp_welcome_form where `FROM`=%s and `TO`=%s'
			data1=(FROM_H,TO_H)
			my_cursor.execute(sql_query,data1)
			rec=my_cursor.fetchone()
			print(rec)
			if rec !=None:
				if FROM_H==rec[1] and TO_H==rec[2]:
					result(request)
				
				else:
					failure(request)
	dict1={'sd':sd}
	return render(request,'busapp/Welcome.html',context=dict1)
