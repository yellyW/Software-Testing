import sys
import time


def normalPulse(x):
	global error
	if x.isdigit():
		pulse = int(x)
		if  pulse > 200:
			error = error + " * pulse is outside the range [0...200] * "
		else: 
			if (pulse >= 60 and pulse <= 100):
				return True 
			else:
				global pulseStatus
				if pulse > 100:
					pulseStatus = "Pulse is high"
				else:
					pulseStatus = "Pulse is low"
				return False
	else:
		error = error + " * Please fix the error in pulse input *"

def normalBloodPressure(x):
	global error
	if x[0].isdigit() and x[1].isdigit():
		systolic = int(x[0])
		diastolic = int(x[1])
		if ( systolic > 250 or  diastolic > 140) :
			error = error + " * make sure systolic values is in the range [0...250] and diastolic is in the range [0...140] * "
		else:
			if systolic <= diastolic:
				error = error + " * please fix your systolic and diastolic input. diastolic value should be less than the systolic value * "
			else:
				global bloodPressureStatus
				if (diastolic < 60 and systolic >= 90 and systolic <= 120) or (diastolic >= 60 and diastolic <= 80 and systolic <= 120):
					return True 
				elif (systolic < 90 and diastolic < 60):
					bloodPressureStatus = "Low blood pressure"
					return False
				elif (systolic > 120 or diastolic > 80):
					bloodPressureStatus = "High blood pressure"
					return False
				else:
					return False
	else:
		error = error + " * Please fix your blood pressure input *"

def normalOxygen(x):
	global error
	if x.isdigit():
		oxygenlvl = int(x)
		if  oxygenlvl > 100:
			error = error + " * oxygen level is outside the range [0...100] * "
		else:
			if (oxygenlvl >= 95 and oxygenlvl <= 100):
				return True 
			else:
				return False
	else:
		
		error = error + " * Please fix the error in oxygen level input *"

def condition(vitals,bloodPressureVal):
	# severity // oxygen: 4 - pulse: 3 - blood pressure: 2
	#2 , 3 , 4 , 6 , 8 , 12 , 24
	global error
	sum = 1
	condition = ""
	# 0 -> false , 1 -> true , 2 -> error 
	if not normalOxygen(vitals[2]):
		sum = sum*4
		condition = condition + " - Oxygen level is low"
	if not normalPulse(vitals[0]):
		sum = sum*3
		condition = condition + " - "+pulseStatus
	if not normalBloodPressure(bloodPressureVal) :
		sum = sum*2
		condition = condition + " - "+bloodPressureStatus
		

	severity = {1:"Normal",2:"Careful I",3:"Careful II",4:"Careful III",6:"Intermediate risk I",8:"Intermediate risk II",12:"Intermediate risk III",24:"Maximum risk"}
	#print(sum)
	result = ""
	if not error == "":
		result = error
		print(error)
	else:
		print(severity[sum]+ " "+ condition)
		result = severity[sum]+ " "+ condition
	error = ""
	return result

def splitLine(line):
	if "\t" in line:
		vitals = line.split("\t")
		if len(vitals) == 3 :
			if ":" in vitals[1]:
				bloodPressureValues = vitals[1].split(":")
				#print(bloodPressureValues)
			#print(bloodPressureValues[0])
				if len(bloodPressureValues) == 2:
					condition(vitals,bloodPressureValues)
					time.sleep(1)
				else:
					print(" * Please fix your blood pressure input *")	
			else:
				print(" * Please fix your blood pressure input * ")
		else:
			print(" * Please fix your input row *")
	else:
		print(" * Please fix your input row *")

if not len(sys.argv) == 1:
	filename = sys.argv[1]
	file = None 
	try:
		file = open(filename, "r") 
	except:
		print(" * file could not be open. Make sure you entered the correct name * ")
	if not file == None: 
		allfile = file.read()
		pulseStatus = ""
		bloodPressureStatus = ""
		error = ""
		if "\n" in allfile:
			allLines = allfile.split("\n")
			for line in allLines:
				splitLine(line)
		elif allfile == "":
			print(" * caution: your file is empty * ")
		else:
			splitLine(allfile)
else:
	print(" * please enter a filename as an argument * ")
