{\rtf1\ansi\ansicpg936\cocoartf1561\cocoasubrtf200
{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fmodern\fcharset0 CourierNewPSMT;\f2\fnil\fcharset134 PingFangSC-Regular;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 #Chapter26 ECQ\
##S3C3 Dennis Zhang\
\
### **1** \
### **a** **i**\
class CustomRecord:\
	def _init_(self):\
		self.CustomerID=0\
		self.CustomerName=\'91 \'92\
		self.TelephoneNumber=\'91 \'92\
		self.TotalValueOfOrder= 0\
\
### **ii**\
\pard\pardeftab720\sl340\partightenfactor0
\cf2 \expnd0\expndtw0\kerning0
CustomerData = [CustomerRecord() for I in range(1,999)]
\f1\fs29\fsmilli14667 \
\

\f0\fs24 ### **b** **i**\
def Hash(CustomerID):\
	Address=CustomerID%100\
	return Address\
\
### **ii**\
FUNCTION AddRecord(File,Customer
\f2 \'a3\'a9\
	Address <- Hash(Customer.CustomerID)\
	IF NOT File(Address).CustomerID = 0:\
		Address <- Address+1\
	ENDIF\
	File[Address] <- Customer\
ENDFUNCTION\
\
### **iii**\

\f0 def FindRecord(File, CustomerID)\
	Address = Hash(ID)\
	while not File[Address].CustomerID==CustomerID :\
		Address=Address + 1\
	return Address\
\
### **c**\
import pickle\
def Save(File) :\
	CustomerFile = open(\'91File.Dat','wb') \
	for i in range(1000) :\
		pickle.dump(CustomerData[i], CustomerFile)\
	CustomerFile.close()\
\
### **2**\
def OpenFile() :\
	input(FileName=\'91Which file you want to use\'92) \
	try:\
		Channel = open(FileName, 'rb+')\
	except :\
		print(\'93Not Found\'94)}