import math
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.modalview import ModalView
from kivy.core.window import Window
import re
import numpy as np
import pandas as pd


class MainWindow(BoxLayout):

	#--------simple---------#
	def calculate(self,calculation):
		if calculation:
			try:
				self.display.text=str(eval(calculation))
			except:
				self.display.text="Syntex Error"
	def click(self,input):
		if(self.display.text=="Syntex Error" or self.display.text=="0" or self.display.text=="0.0"):
			self.display.text=""
			self.display.text+=input
		else:
			self.display.text+=input
	def delete(self,s):
		lenth=len(s)
		self.display.text=s[:-1]

	#-------Scientific------------#
	def fact(self,n):
		val=math.factorial(n)
		self.display.text=str(val)

	def squrt(self,num):
		val=math.sqrt(float(num))
		return str(val)


	def scientific(self,exp):
		if(self.display.text==""):
			self.display.text=""
		else:
			try:
				#value matching
				print("Raw Exp= "+exp+"\n")
				exp=exp.replace("e","2.7182818284590452353")
				exp=exp.replace("π","3.14159265358979323846264338327950288419716939937510582097494459231")
				exp=exp.replace("^","**")

				###finding square root
				pattern=re.compile("√")
				matches=pattern.finditer(exp)
				i=0
				y={}
				for match in matches:
					y[i]=match.span()
					i=i+1

				if(i!=0):	
					index=-5
					for k in range(i-1,-1,-1):
						#print("y["+str(k)+"]=")
						#print(y[k])
						start1=y[k][0]
						end1=y[k][1]
						index=len(exp)
						#print("start="+str(start1))
						#print("End="+str(end1))
						func_name=exp[y[k][0]:y[k][1]]
						#print(func_name)

						for l in range(end1,len(exp)):

							#print(exp[l:l+1])
							if((exp[l:l+1]=="(") or (exp[l:l+1]==")") or (exp[l:l+1]=="*") or (exp[l:l+1]=="-") 
								or (exp[l:l+1]=="/") or (exp[l:l+1]=="+") or (exp[l:l+1]=="\n")):
								print(exp[l:l+1])
								index=l
								break
						#print(exp[start1:index])
						#print("index="+str(index)+"\n")
						exp=exp.replace(exp[start1:index],self.squrt(exp[start1+1:index]))
						#print(exp)





				fns={0:"log2",1:"log10",2:"ln",3:"sin",4:"cos",5:"tan"}
				for j in fns:
					#print("\n\n")
					pattern=re.compile(fns[j]+"[(](.*?)[)]")
					matches=pattern.finditer(exp)
					i=0
					x={}
					for match in matches:
						x[i]=match.span()
						i=i+1


					if(i!=0):	
						for k in range(i-1,-1,-1):
							#print(x[k])
							start=x[k][0]
							end=x[k][1]
							#print("End="+str(end))
							func_name=exp[x[k][0]:x[k][1]]
							if(j==0):
								var=float(func_name[5:(end-start-1)])     #find no under the fn
								#print(func_name+"="+str(math.log(var,2)))
								exp=exp.replace(func_name,str(math.log(var,2)))
								#print(exp)
							if(j==1):
								var=float(func_name[6:(end-start-1)])
								#print(func_name+"="+str(math.log(var,10)))
								exp=exp.replace(func_name,str(math.log(var,10)))
								#print(exp)
							if(j==2):
								var=float(func_name[3:(end-start-1)])
								#print(func_name+"="+str(math.log(var,2.7182818284590452353)))
								exp=exp.replace(func_name,str(math.log(var,2.7182818284590452353)))
								#print(exp)
							if(j==3):
								var=float(eval(func_name[4:(end-start-1)]))
								#print(func_name+"="+str(math.sin(var)))
								exp=exp.replace(func_name,str("{0:.2f}".format(round(math.sin(var)))))
								#print(exp)
							if(j==4):
								var=float(eval(func_name[4:(end-start-1)]))
								#print(func_name+"="+str(math.cos(var)))
								exp=exp.replace(func_name,str("{0:.2f}".format(round(math.cos(var)))))
								#print(exp)
							if(j==5):
								var=float(eval(func_name[4:(end-start-1)]))
								#print(func_name+"="+str(math.tan(var)))
								exp=exp.replace(func_name,str("{0:.5f}".format(round(math.tan(var)))))
								#print(exp)


					#print("\n\n")

				print("Modified exp= "+exp)		
			#basic calculation
			
				self.display.text=str(eval(exp))
			except:
				self.display.text="Syntex Error"


gui=Builder.load_file("gui.kv")
class Calculator(App):
	def build(self):
		#Window.size = (480,800)
		return gui

Calculator().run()
