{\rtf1\ansi\ansicpg936\cocoartf1561\cocoasubrtf200
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Ch27 End Of Chapter\
##S3C3 Dennis\
\
### **1** a\
###	          Bank Account\
	    	            |\
	           /                     \\\
                  /                        \\\
###PersonalAccount       SavingAccount\
\
###b\
class bankaccount:\
	def _init_(self, iban)\
		  self.__AccountHolderName = ''\
     		  self.__IBAN = ban\
\
   	def SetAccountHolderName(self, name):\
     		  self.__AccountHolderName = name\
\
        def GetAccountHolderName(self):\
                    return(self.__AccountHolderName)\
\
        def GetIBAN(self):\
                    return(self.__IBAN)\
\
### c **i**\
### attributes : the monthly fee, whether overdraw the account up to an agreed overdraft limit\
\
### **ii**\
### attributes : balance of payment, interest rate, interest paid\
\
### **iii**\
###  encapsulation\
\
### **2** a\
SeasonTicketHolder\
EmailAddress: STRING\
\
GetName()\
GetEmail()\
\
Pay-As-You-Go-TocketHolder\
Private\
MoneyPaid: NUMBER\
\
Constructor(Holder: STRING, Email: STRING)\
GetPaid()\
\
ContractTicketHolder\
Private\
Fee: NUMBER\
\
GetFee()\
\
### b\
i  Because these attributes are attached together and cannot be be changed separately.\
ii  Because they are used to all different private sectors.\
\
### c\
NewCustomer=ContractTicketHolder("A. Smith", "xyz@abc.xx", 10)\
\
### **3** a\
contain\
\
### b\
class NodeClass :\
\
	def __init__(self):\
		self.__Data = ' '\
      		self.__Pointer = 0\
\
   	def SetData(self, data):\
      		self.__Data = data\
\
   	def GetData(self):\
      		return(self.__Data)\
\
   	def SetPointer(self, pointer):\
      		self.__Data = pointer\
\
   	def GetPointer(self):\
      		return(self.__Pointer)\
\
### c\
class QueueClass :\
\
   	def __init__(self):\
      		self.__Queue = [NodeClass() for i in range(100)]\
      		self.__Head = -1\
      		self.__Tail = -1}