{\rtf1\ansi\ansicpg936\cocoartf1561\cocoasubrtf200
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 #Ch29 End of Chapter Questions\
##S3C3 Dennis\
\
### **1** a i  cityIn(London,uk).\
\
### ii iVisited(Strasbourg).\
\
### b \
Country = chile;\
Country = argentina.\
\
### c\
countriesIVisited(Country) :-\
	iVisited(X),\
	cityIn(X,Country).\
\
### **2** a i Emma is aged 22.\
\
### ii If a man has age larger than 18 and has license, then this man is allowed to drive a car.\
\
### b i Who = jack.	ii false	iii false\
\
###c i \
qualifiedCarDrivers(X) :-\
	qualifiedDriver(X, car).\
\
### ii\
partQualified(X) :- \
	passedTheoryTest(X);\
	not(passedDrivingTest(X, _)).\
\
\
\
\
\
}