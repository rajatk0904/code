import sys
import codecs
import operator
import csv
import plotly.plotly as py
import math
from plotly.graph_objs import *
def is_vowel(ch):
	if(ch>=u"\u0904" and ch<=u"\u0914"):
		return 1
	else:
		return 0
def is_consonat(ch):
	if(ch>u"\u0914" and ch<=u"\u0939"):
		return 1
	else:
		return 0
def is_vowel_matra(ch):
	if(ch>=u'\u093A' and ch<=u'\u094F' and ch!=u"\u094D"):
		return 1
	else:
		return 0
def is_character(ch):
	if(is_vowel(ch)==1 or is_consonat(ch)==1):
		return 1
	else:
		return 0
def rule1(word,marker_list):
	for i in range(0,len(word)):
		if(is_vowel(word[i])==1):
			marker_list[i]='F'
		if (is_consonat(word[i])==1 and i!=len(word)-1):
			if(is_vowel(word[i+1])==1 or is_vowel_matra(word[i+1])==1):
				marker_list[i]='F'
			if(word[i+1]==u"\u094D"):
				marker_list[i]='H'
	return marker_list

def rule2(word,marker_list):
	for i in range(0,len(word)):
		if(word[i]==u'\u092F' and i!=0):
			if(word[i-1]>=u'\u093F' and word[i-1]<=u'\u0943'):
				marker_list[i]='F'
	return marker_list

def rule3(word,marker_list):
	for i in range(0,len(word)):
		if(word[i] in [u'\u092D',u'\u092F',u'\u0932',u'\u0930'] and marker_list[i]=='U'):
			j=i
			while(j>0):
				j=j-1
				if(is_character(word[j])==1):
					if(is_consonat(word[j])==1 and marker_list[j]=='H'):
						marker_list[i]='F'
					break
	return marker_list
def rule4(word,marker_list):
	for i in range(0,len(word)):
		if(is_consonat(word[i])==1 and marker_list[i]=='U'):
			j=i
			while(j<len(word)-1):
				j=j+1
				if(is_character(word[j])==1):
					if(is_vowel(word[j])==1):
						marker_list[i]='F'
					break
	return marker_list
def rule5(word,marker_list):
	for i in range(0,len(word)):
		if(marker_list[i]=='F'):
			break
		if(is_consonat(word[i])==1 and marker_list[i]=='U'):
			marker_list[i]='F'
			break
	return marker_list
def rule6(word,marker_list):
	for i in range(0,len(word)):
		if(is_consonat(word[len(word)-1-i])==1):
			if(marker_list[len(word)-1-i]=='U'):
				marker_list[len(word)-1-i]='H'
			break
	return marker_list
def rule7(word,marker_list):
	for i in range(0,len(word)):
		if(is_consonat(word[i])==1 and marker_list[i]=='U' and i < len(word)-1):
			if(is_consonat(word[i+1])==1 and marker_list[i+1]=='H'):
				marker_list[i]='F'
	return marker_list
def rule8(word,marker_list):
	for i in range(0,len(word)):
		if(is_consonat(word[i])==1 and marker_list[i]=='U'):
			j=i
			while (j>0):
				j=j-1
				if(is_character(word[j])==1):
					break
				if(j==0):
					j=-1
			k=i
			while (k<len(word)-1):
				k=k-1
				if(is_character(word[k])==1):
					break
				if(k==len(word)-1):
					k=-1
			if(j!=-1 and k!=-1):
				if(marker_list[j]=='F' and marker_list[k] in ['F','U']):
					marker_list[i]='H'
				else:
					marker_list[i]='F'
			else:
				marker_list[i]='F'
	return marker_list
def rule9(word,marker_list):
	for i in range(0,len(word)):
		if(word[i]>=u'\u0900' and word[i]<=u'\u0902'):
			marker_list[i]='H'
	return marker_list
def next_char(word,i,marker_list):
	j=i
	while (j<len(word)-1):
		j=j+1
		if(marker_list[j]!='n'):
			return j
	return -1
def prev_char(word,i,marker_list):
	j=i
	while (j>0):
		j=j-1
		if(marker_list[j]!='n'):
			return j
	return -1
def find_syllable_breaks(word,marker_list):
	lis_=[0]
	for i in range(0,len(word)):

		if(marker_list[i]=='F' and is_vowel(word[i])==0):
			prev_mark=prev_char(word,i,marker_list)
			if(prev_mark!=-1):
				if (marker_list[prev_mark]=='F'):
					lis_.append(i)
	print lis_
	for i in range(0,len(word)):
		if(marker_list[i]=='H'):
			next_mark=next_char(word,i,marker_list)
			if(next_mark!=-1):
				if(marker_list[i]!=marker_list[next_mark]):
					if (marker_list[i]=='H' and i in lis_):
						pass
					else:
						lis_.append(next_mark)
	for i in range(0,len(word)):
		if(i+5<len(word)):
			if (is_consonat(word[i])==1 and word[i+1]==u'\u094D' and is_consonat(word[i+2])==1 and word[i+3]==u'\u094D' and is_consonat(word[i+4])==1):
				if(i in lis_):
					lis_.remove(i)
				if(i+4 in lis_):
					lis_.remove(i+4)
				lis_.append(i+2)
	return lis_
def modify(word,marker_list):
	marker_list=rule1(word,marker_list)
	marker_list=rule2(word,marker_list)
	marker_list=rule3(word,marker_list)
	marker_list=rule4(word,marker_list)
	marker_list=rule5(word,marker_list)
	marker_list=rule6(word,marker_list)
	marker_list=rule7(word,marker_list)
	marker_list=rule8(word,marker_list)
	marker_list=rule9(word,marker_list)
	syllable_breaks=find_syllable_breaks(word,marker_list)
	return marker_list,syllable_breaks
big_dict={}
def func1(word):
	marker_list=['n']*len(word)
	for i in range(0,len(word)):
		if(word[i]>=u'\u0904' and word[i] <=u'\u0939'):
			marker_list[i]='U'
	valid=1
	for ch in word:
		if(ch < u"\u0900" or ch > u"\u0963"):
			valid=0
			break
	if(valid==1):
		marker_list,syllable_breaks=modify(word,marker_list)
		syllable_breaks.sort()
		print word
		for i in range(0,len(syllable_breaks)):
			start=int(syllable_breaks[i])
			if(i<len(syllable_breaks)-1):
				end=int(syllable_breaks[i+1])
			else:
				end=len(word)
			syl=""
			for j in range(start,end):
				syl=syl+word[j]
			if(syl in big_dict):
				big_dict[syl]=big_dict[syl]+1
			else:
				big_dict[syl]=1
	return big_dict
def func2(word):
	valid=1
	for ch in word:
		if(ch < u'\u0B00' or ch > u'\u0B63'):
			valid=0
			break
	if(valid==1):
		syl=""
		for i in range(0,len(word)):
			if((word[i]>=u'\u0B05' and word[i]<=u'\u0B39')):
				if((i==0 or word[i-1]!=u'\u0B4D') and (i!=len(word)-2 or word[i+1]!=u'\u0B4D')):
					if(syl!=""):
						if(syl in big_dict):
							big_dict[syl]=big_dict[syl]+1
						else:
							big_dict[syl]=1
					syl=word[i]
				else:
					syl=syl+word[i]
			else:
				syl=syl+word[i]
		if(syl!=""):
			if(syl in big_dict):
				big_dict[syl]=big_dict[syl]+1
			else:
				big_dict[syl]=1		
f1 = codecs.open(sys.argv[2], "r", "utf-8")
text = f1.read()
words=[s.split() for s in text.splitlines()]
for word in words:
	for demi in word:
		if(sys.argv[1]=="-hindi"):
			func1(demi)
		if(sys.argv[1]=="-odia"):
			func2(demi)
writer = csv.writer(open('dict.csv', 'wb'))
for key, value in big_dict.items():
   writer.writerow([key.encode("utf-8"), value])
sorted_dict = sorted(big_dict.items(), key=operator.itemgetter(1),reverse=True)
x=[]
y=[]
for i in range(0,100):
	x.append(sorted_dict[i][0])
	y.append(math.log10(sorted_dict[i][1]))
	print sorted_dict[i][0].encode("utf-8"),":",sorted_dict[i][1]
data = Data([Bar(x=x,y=(y))])
plot_url = py.plot(data, filename='basic-bar')