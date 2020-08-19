

cs_list=[['I','CS110' ,'Computer Programming Lab'],['I' ,'CS101',' Computer Programming'],['II' ,'CS103',' Data Structures'],['II' ,'CS111' ,'Data Structures Lab'],['II' ,'CS104', 'Computer Organization'],['III', 'CS201', 'Algorithms'],['III', 'CS210' ,'Algorithm Lab'],['III', 'CS221' ,'Data Communication'],
['IV', 'CS210' ,'Formal Languages and Automata'],['IV' ,'CS231' ,'Operating Systems'],['IV', 'CS232', 'Operating Systems Lab'],['IV', 'CS235' ,'Artificial Intelligence'],['IV', 'CS240', 'Database Management Systems'],
['IV', 'CS241' ,'DBMS Lab'],['V', 'CS351', 'IT Workshop III: Cloud Computing'],['V' ,'CS306', 'Machine Learning'],['V', 'CS316' ,'Machine Learning Lab'],['VI', 'CS330', 'Software Engineering'],['VI' ,'CS331', 'Software Engineering Lab'],
['VI', 'CS320', 'Compilers'],['V' ,'CS321' ,'Compilers Lab'],['VI', 'CS361' ,'Computer Security'],['VII', 'CS401', 'Data Analytics'],['VII' ,'CS400' ,'Project II']]



ec_list=[['I'	,'EC101'	,'Digital Design'],['I','EC110',	'Digital Design Lab'],['I'	,'EC102'	,'Electrical Circuit Analysis'],['II','EC103'	,'Basic Electronic Circuits'],['II'	,'EC111'	,'Basic Electronics Lab'],['III',	'EC201'	,'Analog Circuits'],
['III',	'EC260'	,'Semiconductor Devices'],['III',	'EC241',	'Signals and Systems'],['III',	'EC281'	,'Measurement and Instrumentation'],['IV'	,'EC251'	,'Principles of Communication'],['IV',	'EC252',	'Communications Lab'],
['IV'	,'EC243',	'Digital Signal Processing'],['IV'	,'EC244'	,'Digital Signal Processing Lab'],['V'	,'EC351'	,'Digital Communication'],['V',	'EC352'	,'Digital Communication Lab'],['V',	'EC301'	,'Analog Integrated Circuits'],
['V'	,'EC302'	,'Analog Integrated Circuit Lab'],['V',	'EC370'	,'Electromagnetics'],['V'	,'EC380'	,'Control Systems'],['VI'	,'EC353'	,'Information Theory and Coding'],['VI'	,'EC361'	,'VLSI Design'],['VI',	'EC362'	,'VLSI Design Lab'],
['VI',	'EC371'	,'Microwave Engineering'],['VII'	,'EC456'	,'Communication Network'],['VII'	,'EC382',	'Embedded Systems Lab'],['VII'	,'EC381',	'Embedded Systems'],['VIII' ,'EC452'	,'Detection and Estimation Theory'],['VIII' ,'EC455'	,'Wireless Sensor Networks'],['VIII' ,'EC471'	,'Antennas and Wave Propagation']]
#print(cs_list)

#print(ec_list)


res=[]

while True:

	temp=[]

	print('enter student name')
	name=input()
	temp.append(name)
	print('enter student roll no')
	roll=input()
	temp.append(roll)

	print('enter student semester')
	sem=input()
	temp.append(sem)

	if sem=='I' or sem=='II':

		if roll[2] !='1':

			continue
	  
	if sem=='III' or sem == "IV":
		if roll[2] !='2':
			continue
	if sem=='V' or sem=='VI':
		if roll[2] !='3':
			continue

	if sem=='VII' or sem=='VIII':
		if roll[2] !='4':
			continue
	if roll[0].lower()=='c' and roll[1].lower()=='s':
		for i in cs_list:
			if i[0]==sem:
				temp.append(i[2])

	if roll[0].lower()=='e' and roll[1].lower()=='c':
		for i in ec_list:
			if i[0]==sem:
				temp.append(i[2])

	res.append(temp)

	print('Do you want to register new student[yes/no]')

	temp2=input()
	if temp2.lower()=='no':
		break


f=open('student course information','w')
for i in res:
	for j in i:
		f.write(j+'\t')

	f.write('\n')




