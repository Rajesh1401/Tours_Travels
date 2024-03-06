from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from result.models import *

def homepage(request):
    return render(request,'welcome.html')
def homepage(request):
    return render(request,'list.html')

def localvariable(request):
    my_variable="Hello local variable"
    return render(request,'local1.html',{'my_variable':my_variable})

my_variable="Hello global variable"
def globalvariable(request):
    return render(request,'global1.html',{'my_variable':my_variable})

def view1(request):
    if request.method=='GET':
     return render(request,'getto.html')
    
def view2(request):
    if request.method=='POST':
     username=request.POST.get('username')
     password=request.POST.get('password')
     return render(request, 'success.html',{'username':username})
    return render(request,'postto.html')

def sum(request):
   if request.method=='POST':
      num1=int(request.POST.get('num1'))
      num2=int(request.POST.get('num2'))
      result=num1+num2
      return render(request,'result.html',{'result':result})
   return render(request,'add.html')

def calculator(request):
   if request.method=='POST':
      num1=request.POST['num1']
      num2=request.POST['num2']
      operator=request.POST['operator']
      if operator=='+':
         result=int(num1)+int(num2)
      elif operator=='-':
         result=int(num1)-int(num2)
      elif operator=='*':
         result=int(num1)*int(num2)
      elif operator=='/':
         result=int(num1)//int(num2)
      return render(request,'calculator.html',{'result':result})
   else:
      return render(request,'calculator.html')
   
def find_biggest(request):
      if request.method=='POST':
         num1=int(request.POST['num1'])
         num2=int(request.POST['num2'])
         if num1>num2:
            result=num1
         else:
            result=num2

         return render(request,'biggest.html',{'result':result})
      else:
         return render(request,'biggest.html')

def atm(request):
   balance=1000
   if request.method=='POST':
      transaction_type=request.POST.get('transaction_type')
      amount=int(request.POST.get('amount'))
      if transaction_type=='check_balance':
         message=balance
      elif transaction_type=='deposit':
         message = balance + amount
      elif transaction_type=='withdraw':
       if amount%100==0:
         if amount>balance:
            message="overdraft"
         else:
            message  = balance - amount
       else:
         message="multiple of 100"
      return render(request,'atm_transaction.html',{'message': message}) 
   else:
       return render(request,'atm_transaction.html') 
   
def square(request):
   if request.method=='POST':
      num1=int(request.POST.get('num1'))
      result=num1*num1
      return render(request,'result.html',{'result':result})
   return render(request,'square.html')

def swap_accounts(request):
      if request.method=='POST':
         bank_account1=int(request.POST.get('bank_account1'))
         bank_account2=int(request.POST.get('bank_account2'))
         bank_account1,bank_account2=bank_account2,bank_account1
         return render(request,'result.html',{'bank_account1':bank_account1,'bank_account2':bank_account2})
      return render(request,'swap_bank_accounts.html')
      

def biggest_number(request):
   if request.method=='POST':
      num1=int(request.POST['num1'])
      num2=int(request.POST['num2'])
      num3=int(request.POST['num3'])
      result=max(num1,num2,num3)
      return render(request,'biggest_number.html',{'result':result})
   return render(request,'biggest_number.html')

def login(request):
    if request.method == 'POST':
        # Check if the user entered the correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'password':
            return render(request, 'success.html', {'username': username})
        else:
            error = 'Invalid username or password. Please try again.'
            return render(request, 'login.html', {'error': error})
    else:
        return render(request,'login.html')
      
def student(request):
   if request.method=='POST':
      name=request.POST.get('name')
      marks1=int(request.POST.get('marks1'))
      marks2=int(request.POST.get('marks2'))
      marks3=int(request.POST.get('marks3'))
      total=marks1+marks2+marks3
      avg=total/3
      if avg>=95 and avg<=100:
         grade='A+'
      elif avg>=75 and avg<=94:
         grade='A'
      elif avg>=65 and avg<=74:
         grade='B'
      elif avg>=50 and avg<=64:
         grade='B+'
      elif avg>=35 and avg<=49:
         grade='C'
      elif avg>=0 and avg<=34:
         grade='fail'
      else:
         grade='invalid'
      return render(request, 'result.html', {'name': name, 'total': total, 'avg': avg, 'grade': grade})
   else: 
        return render(request,'student_details.html')
   
def table(request):
      data = [
         {'name':'apt','age':30},
         {'name':'bangalore','age':28},
           ]
      return render(request,'table.html',{'data':data})

def student_results(request):
   students=[
      {'name':'vikaas','maths':90,'science':85,'english':95},
      {'name':'mohan','maths':80,'science':75,'english':85},
      {'name':'vijay','maths':70,'science':65,'english':75},
   ]
   return render(request,'results.html',{'students':students})

def even(request):
   numbers=[i for i in range(1,11) if i % 2 ==0]
   return render(request,'even.html',{'numbers':numbers})

def testone(request):
    if request.method=='POST':
      firstname=request.POST.get('firstname')
      lastname=request.POST.get('lastname')
      mail=request.POST.get('mail')
      password=request.POST.get('password')
      return render(request, 'result.html', {'firstname': firstname, 'lastname': lastname, 'mail': mail, 'password': password})
    else: 
        return render(request,'test1.html')
    
def testtwo(request):
    if request.method == 'POST':
        # Check if the user entered the correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        return render(request, 'result.html',{'username':username,'password':password})
    else:
        return render(request,'test2.html')
    
def images(request):
   return render(request,'image1.html')

def logo(request):
   return render(request,'logo.html') 

def table1(request):
   return render(request,'table1.html')

def home(request):
   return render(request,'project_page1.html') 

def book(request):
   return render(request,'project_page2.html') 

def services(request):
   return render(request,'project_page3.html') 

def login1(request):
   return render(request,'project_page4.html') 

def register(request):
   return render(request,'project_page5.html') 

def programming_language(request): 
   users=[
      {'name':'vikaas','language':'Python','os':'Windows'},
      {'name':'APT','language':'Java','os':'Linux'},
      {'name':'vijay','language':'C','os':'macOS'},
      {'name':'ajay','language':'Javascript','os':'Windows'},
   ]
   return render(request,'checkandradio.html',{'users':users}) 

def table2(request): 
   return render(request,'csstable.html') 

def food(request):
   return render(request,'food.html') 

def foodcontact(request):
   return render(request,'foodcontact.html') 

def foodlogin(request):
   return render(request,'foodlogin.html') 

def foodorder(request):
   return render(request,'foodorder.html') 

def index(request):
   if request.method=="POST":  
        x= request.POST.get('suname')     
        y= request.POST.get('suemail')
        z= request.POST.get('supassword')
        en=Signin(suname=x,suemail=y,supassword=z)
        en.save()
   return render(request,'index.html')
   

def famousplaces(request):
   return render(request,'famousplaces.html')

def restaurants(request):
   return render(request,'restaurants.html')

def booking(request):
   if request.method=="POST":       
        g= request.POST.get('location')
        h= request.POST.get('destination')
        en=Booking(location=g,destination=h)
        en.save()
   return render(request,'booking.html')

def contactus(request):
    if request.method=="POST":       
        c= request.POST.get('customer_name')
        d= request.POST.get('mobile_number')
        e= request.POST.get('email_id')
        f= request.POST.get('query_text')
        en=Contactus(customer_name=c,mobile_number=d,email_id=e,query_text=f)
        en.save()
    return render(request,'contactus.html')

def payment(request):
   if request.method=="POST":     
         i= request.POST.get('name')
         j= request.POST.get('card')
         k= request.POST.get('number')
         l= request.POST.get('expiry')
         m= request.POST.get('ccv')
         en=Payment(name=i,card=j,number=k,expiry=l,ccv=m)
         en.save()
   return render(request,'payment.html')

def my_form(request):
   if request.method=="POST":
    name=request.POST.get('name')
    email=request.POST.get('email')
    message=request.POST.get('message')
    return HttpResponse('form is valid')
   return render(request,'my_form.html')

def drop(request):
   return render(request,'dropdown.html')

def login1(request):
   if request.method=="POST":  
        x= request.POST.get('suname')     
        y= request.POST.get('suemail')
        z= request.POST.get('supassword')
        en=Signin(suname=x,suemail=y,supassword=z)
        en.save()
   return render(request,'index.html')

def contact(request):
   if request.method=="POST":       
        c= request.POST.get('customer_name')
        d= request.POST.get('mobile_number')
        e= request.POST.get('email_id')
        f= request.POST.get('query_text')
        en=Contactus(customer_name=c,mobile_number=d,email_id=e,query_text=f)
        en.save()
   return render(request,'contactus.html')

def book1(request):
   if request.method=="POST":       
        g= request.POST.get('location')
        h= request.POST.get('destination')
        en=Booking(location=g,destination=h)
        en.save()
   return render(request,'booking.html')

def pay(request):
   if request.method=="POST":     
         i= request.POST.get('name')
         j= request.POST.get('card')
         k= request.POST.get('number')
         l= request.POST.get('expiry')
         m= request.POST.get('ccv')
         en=Payment(name=i,card=j,number=k,expiry=l,ccv=m)
         en.save()
   return render(request,'payment.html')

def handle_arithmetic_exception(request):
      try:
         result=10/0
      except ZeroDivisionError as e:
         return render(request,'exceptionarithmetic.html',{'error':str(e)})

def signin(request):
   if request.method=="POST":       
        u= request.POST.get('lemail')
        v= request.POST.get('lpassword')
        en=Login(lemail=u,lpassword=v)
        en.save()
   return render(request,'signin.html')

def my_view(request):
   my_var=None
   try:
      result=my_var.upper()
   except AttributeError:
      return render(request,'errors.html',{'message':'invalid input.Please  enter a non empty string'})
   return render(request,'my_template.html',{'result':result})

def my_view1(request):
   try:
      result=10/0
      my_var=None
      my_var.upper()
   except ZeroDivisionError:
      error_message="cant divide by zero"
   except AttributeError:
      error_message="Invalid input .Please enter a non-empty string"
   return render(request,'my_template.html',{'error_message':error_message})

def result_view(request):
   
    student_name = 'apt'
    subject1 = 85
    subject2 = 90
    subject3 = 80
    subject4 = 95
    total = subject1 + subject2 + subject3 + subject4
    percentage = total / 4 
    context = {
        'student_name': student_name,
        'subject1': subject1,
        'subject2': subject2,
        'subject3': subject3,
        'subject4': subject4,
        'total': total,
        'percentage': percentage,
    }
    return render(request, 'lcm.html', context)

def add_number(request):

    if request.method=="POST":       
        num1=int(request.POST['num1'])
        num2=int(request.POST['num2'])
        result=num1+num2
    else:
         result=None
    return render(request, 'child1.html',{'result':result})

def inher(request):
   return render(request,'child5.html')