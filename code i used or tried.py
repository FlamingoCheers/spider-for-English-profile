#A_Z word list url aquire
import requests
import bs4
from requests import get as reqGet
from bs4 import BeautifulSoup as soup
headers = {'Authorization': 'Basic ZW5nbGlzaHByb2ZpbGU6dm9jYWJ1bGFyeQ=='}
wordList = 'http://vocabulary.englishprofile.org/dictionary//word-list/uk/c2/A'
responWL = reqGet (wordList, headers=headers)
page_html_WL = responWL.content
#parse the html
page_soup_WL = soup (page_html_WL,'html.parser')
#get the urls in tags as :<span><a href="/dictionary/word-list/uk/c2/A" title="A">A</a></span>
urlA_Z = page_soup_WL.find('div',{'id':'letters'})
urlA_Zurl = urlA_Z.find_all('a') 
print (urlA_Zurl)
UrlSet = list()
for index in range(len(urlA_Zurl)):
	aLineEle = urlA_Zurl[index]
	UrlEle = aLineEle['href']
	list.append(UrlSet,UrlEle)
print (UrlSet)
#write the urls into a file
import pickle
pkF = open(r'C:\myfirstgrab\picUrlSet.pk','wb')
pickle.dump(UrlSet, pkF)
pkF.close()
#good for now



#urls of ranges of initial letters 
import requests
import bs4
from requests import get as reqGet
from bs4 import BeautifulSoup as soup

import pickle
UrlSetIn = open(r'C:\myfirstgrab\picUrlSet.txt','rb')
UrlSet_in = pickle.load(UrlSetIn)
#replace every element as itself with a prefix of 'http://'
prefix = 'http://vocabulary.englishprofile.org'
prf_UrlSet_in = list()
for index in range(len(UrlSet_in)):
	preEle = str(UrlSet_in[index])
	newEle = prefix + preEle
	list.append(prf_UrlSet_in, newEle)
print ('url adjasted')
#good for now

#range_urlSet = list()

rangeLiSet = list()
#prf_UrlSet_in is the list of urls of letter pages
for index in range(len(prf_UrlSet_in)):
	#get letter page 
	headers = {'Authorization': 'Basic ZW5nbGlzaHByb2ZpbGU6dm9jYWJ1bGFyeQ=='}
	range_ind = reqGet (prf_UrlSet_in[index], headers=headers)
	page_html_range = range_ind.content
	#parse letter page 
	page_soup_range = soup (page_html_range, 'html.parser')
	#find all node li (all word ranges)
	range_url_li = page_soup_range.find_all('li')
	list.append (rangeLiSet, range_url_li)
print (rangeLiSet)
import pickle
pkF_rangeLiSet = open(r'C:\myfirstgrab\rangeLiSet.pk','wb')
pickle.dump(range_url_li, pkF_rangeLiSet)
pkF_rangeLiSet.close()

import pickle
rangeLiSet_in = open(r'C:\myfirstgrab\rangeLiSet.pk','rb')
rangeLiSetIn = pickle.load(rangeLiSet_in)
rangeHrefSet = list()
for index in range(len(rangeLiSetIn)):
	range_url_li = rangeLiSetIn[index]
	range_url_href = range_url_li.a['href']
	list.append (rangeHrefSet, range_url_href)
print (rangeHrefSet)
#good

prefix = 'http://vocabulary.englishprofile.org'
prf_rangeHrefSet = list()
for index in range(len(rangeHrefSet)):
	preEle = str(rangeHrefSet[index])
	newEle = prefix + preEle
	list.append(prf_rangeHrefSet, newEle)
print ('url adjasted')
#good

#open range page, find li, find a, modify url, output
entryLiSet = list()
for index in range(len(prf_rangeHrefSet)):
	#get letter page 
	headers = {'Authorization': 'Basic ZW5nbGlzaHByb2ZpbGU6dm9jYWJ1bGFyeQ=='}
	entry_ind = reqGet (prf_rangeHrefSet[index], headers=headers)
	page_html_entry = entry_ind.content
	#parse letter page 
	page_soup_entry = soup (page_html_entry, 'html.parser')
	#find all node li (all word ranges)
	entry_url_li = page_soup_entry.find_all('li')
	for index in range(len(entry_url_li)):
		list.append(entryLiSet, entry_url_li[index])
	print ('entryLiSet'+str(index))
#good
import pickle
pkF_entryLiSet = open(r'C:\myfirstgrab\entryLiSet.pk','wb')
pickle.dump(entryLiSet, pkF_entryLiSet)
pkF_entryLiSet.close()
#good

import pickle
entryLiSet_in = open(r'C:\myfirstgrab\entryLiSet.pk','rb')
entryLiSetIn = pickle.load(entryLiSet_in)
entryAset = list()
for index in range(len(entryLiSetIn)):
	entry_url_li = entryLiSetIn[index]
	entry_url_a = entry_url_li.a
	list.append(entryAset, entry_url_a)
	print ('entryAset'+str(index))
for index in range(len(entryAset)):
	entryHref = entryAset[index]['href']
	list.append(entryHrefSet, entryHref)
	print ('href '+str(index))
#good

prefix = 'http://vocabulary.englishprofile.org'
prf_entryHrefSet = list()
for index in range(len(entryHrefSet)):
	preEle = str(entryHrefSet[index])
	newEle = prefix + preEle
	list.append(prf_entryHrefSet, newEle)
print ('url adjasted')

import pickle
pkF_entryUrlSet = open(r'C:\myfirstgrab\entryUrlSet.pk','wb')
pickle.dump(prf_entryHrefSet, pkF_entryUrlSet)
pkF_entryUrlSet.close()
#all entry url aquired


****************************

#get morphs and senses 
#question: how do i send them to mysql?	
import pickle
entryUrl = open(r'C:\myfirstgrab\entryUrlSet.pk','rb')
entryUrl_in = pickle.load(entryUrl)
#good
#open each entry url
gwblocklist = list()
gwblockAllSet = list()
for index in range(len(entryUrl_in)):
		headers = {'Authorization': 'Basic ZW5nbGlzaHByb2ZpbGU6dm9jYWJ1bGFyeQ=='}
		responEntry = reqGet (entryUrl_in[index], headers=headers)
		page_html_entry = responEntry.content
	    #parse page entry-index
		page_soup_entry = soup (page_html_entry, 'html.parser')
		#page_soup.find_all('h3')
		gwblockSet=page_soup_entry.find_all('div',{'class':'gwblock'})
		for index in range(len(gwblockSet)):
			list.append(gwblockAllSet, gwblockSet[index])
		print ('gwblock ' + str(entryUrl_in[index]))
		#havent finished grabing

import pickle
pkF_gwblockAllSet = open(r'C:\myfirstgrab\gwblockAllSet.pk','wb')
pickle.dump(gwblockAllSet, pkF_gwblockAllSet)
pkF_gwblockAllSet.close()
		
import pickle
gwblockAllSet_in = open(r'C:\myfirstgrab\gwblockAllSet.pk','rb')
gwblockAllSetIn = pickle.load(gwblockAllSet_in)
_______________________________________________________
		#morphs and sense aquired in entry page
usageH = list()
for index in range(len(gwblockAllSetIn)):
	h3Ele = gwblockAllSetIn[index]
	h3EleH = h3Ele.find('h3')
	list.append(usageH,h3EleH)
	print ('morphs'+str(index))
********************

#placeboTag = soup('<div> nothing fouond here </div>',"html5")
#list.append(usageH,placeboTag)



usage_NN = list()
for index in range(len(usageH)):
	usageVa = usageH[index]
	if usageVa == (None) :
		placeboTag = soup('<div> nothing found here </div>',"html5")
		usageVa = placeboTag
	else:
	    pass
	list.append(usage_NN, usageVa)





usa_h = list()
for index in range(len(usage_NN)):
	#print (index)
	usageEle = usage_NN[index].text
	#usage_text = usageEle.text
	list.append(usa_h,usageEle)

import pickle
pkF_usa_h = open(r'C:\myfirstgrab\usa_h.pk','wb')
pickle.dump(usa_h, pkF_usa_h)
pkF_usa_h.close()

defs = list()		
for index in range(len(gwblockAllSetIn)):
	defEle = gwblockAllSetIn[index].find('span',{'class':'def'})
	defText = defEle.text
	list.append(defs,defText)
import pickle
pkF_defs = open(r'C:\myfirstgrab\defs.pk','wb')
pickle.dump(defs, pkF_defs)
pkF_defs.close()


import pickle
pkF_defs = open(r'C:\myfirstgrab\defs.pk','rb')
pkF_defs_in = pickle.load(pkF_defs)
len(pkF_defs_in)

________________________________
examp_blocks_NN = list()
for index in range(len(gwblockAllSetIn)):
	examp_blocksVa = gwblockAllSetIn[index]
	if examp_blocksVa == (None) :
		print ('a')
		#placeboTag = soup('<div class="examp-block" show_less="yes"><b class="examp-title" show_less="yes">Dictionary examples:</b><blockquote class="examp" id="3270331" query="yes" resource="uk" show_less="yes"> nothing <b class="b" query="yes" resource="uk">found here </b></blockquote><blockquote class="examp" id="3270332" query="yes" resource="uk" show_less="yes"> sorry <b class="b" query="yes" resource="uk">results</b>.</blockquote></div>',"html5")
		examp_blocksVa = placeboTag
	else:
	    pass
	list.append(examp_blocks_NN, examp_blocksVa)




examp_blocksNP = list()		
for index in range(len(gwblockAllSetIn)):
	examp_blockEle = gwblockAllSetIn[index]
	examp_block_div = examp_blockEle.find('div',{'class':'examp-block'})
	if examp_block_div == None:
		exampNP = soup( '<div class="examp-block" show_less="yes"><b class="examp-title" show_less="yes">Dictionary examples:</b><blockquote class="examp" id="3270331" query="yes" resource="uk" show_less="yes"> nothing found here <b class="b" query="yes" resource="uk">sorry</b></blockquote><blockquote class="examp" id="3270332" query="yes" resource="uk" show_less="yes"> make an example yourself  <b class="b" query="yes" resource="uk">results</b>.</blockquote></div>', "html5")
		examp_block_div = exampNP
	else:
		pass
	list.append(examp_blocksNP, examp_block_div)
examp_blocks = list()
for index in range(len(examp_blocksNP)):
	examp_in = examp_blocksNP[index]
	examp_blockText = examp_in.text
	list.append(examp_blocks,examp_blockText)

import pickle
pkF_examp_blocks = open(r'C:\myfirstgrab\examp_blocks.pk','wb')
pickle.dump(examp_blocks, pkF_examp_blocks)
pkF_examp_blocks.close()




lcNN = list()
for index in range(len(gwblockAllSetIn)):
	learnerCEle = gwblockAllSetIn[index].find('blockquote',{'class':'clc'})
	if learnerCEle == None :
		lcEplacebo = soup('<blockquote class="clc" query="yes" resource="uk" show_less="yes"><div class="clc_before"><img alt="Cambridge Learner Corpus" src="/external/images/clc.png"/> Learner example: </div>Sorry, nothing is found here. Make up your own example maybe. <div class="src"> Best wishes</div></blockquote>',"html5")
		learnerCEle = lcEplacebo
	else:
		pass
	list.append(lcNN, learnerCEle)

learnerCs = list()
for index in range(len(lcNN)):
	lCind = lcNN[index]
	learnerCText = lCind.text
	list.append(learnerCs,learnerCText)
import pickle
pkF_learnerCs = open(r'C:\myfirstgrab\learnerCs.pk','wb')
pickle.dump(learnerCs, pkF_learnerCs)
pkF_learnerCs.close()






valueFor = list()
for index in range(len(usagelist)):
	list.append(valueFor,  str('Usage: '+usagelist[index]+'ahahahahahahaha'+'Definition: '+defslist[index]+'ahahahahahahaha'+dictexamplist[index]+'ahahahahahahaha'+learnerexamplist[index]+'ahahahahahahaha'+'ahahahahahahaha'))
pkF_valueFor = open(r'C:\myfirstgrab\c2tableForB.txt','wb')
pickle.dump(valueFor, pkF_valueFor)
pkF_valueFor.close()	

#尾递归优化

import pickle
pkF_usage = open(r'C:\myfirstgrab\usa_h.pk','rb')
usagelist = pickle.load(pkF_usage)

pkF_def = open(r'C:\myfirstgrab\defs.pk','rb')
defslist = pickle.load(pkF_def)

pkF_dictexamp = open(r'C:\myfirstgrab\examp_blocks.pk','rb')
dictexamplist = pickle.load(pkF_dictexamp)

pkF_learnerexamp = open(r'C:\myfirstgrab\learnerCs.pk','rb')
learnerexamplist = pickle.load(pkF_learnerexamp)

c2 = [[] for i in range(4)]
c2[0].append(usagelist)
c2[1].append(defslist)
c2[2].append(dictexamplist)
c2[3].append(learnerexamplist)



pkF_valueOne = open(r'C:\myfirstgrab\c2table.txt','wb')
pickle.dump(valueOne, pkF_valueOne)
pkF_valueOne.close()		




valueOne = list()
for index in range(len(usagelist)):
	valuelist =list.append(valueOne, str(usagelist[index]+'/t'+defslist[index]+'/t'+dictexamplist[index]+'/t'+learnerexamplist[index]+'/n'))
	print ('row '+ str(index)