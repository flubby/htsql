#    Copyright 2013 Frank Jackson


#    BSIQ Quer maker is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

#    BSIQ Quer maker is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License along with BSIQ Quer maker. If not, see http://www.gnu.org/licenses/.




import linecache
import re
template=open('./temp.csv','r')
tmplst=[]
match=open('./org.csv','r')
mtch=[]
tempis=open('./is.csv','r')
tmpis=[]
writen=open('./bsiq.quer','w')
twrt=[]
twrtis=[]
query="/individual{(family)  ,(code)  ,(sex)  ,(mother)  ,(father),(ethnicity)  ,(race)  ,(guid),(latest_measure.bsi.measure.eval_age_months),round((latest_measure.bsi.measure.eval_age_months) * .083333) title 'eval_age_years',(vip_individual_details.asd_affected),(vip_individual_details.status_16p)  "
#adds Age Bins
query+=",if((latest_measure.bsi.measure.eval_age_months<60),1,(latest_measure.bsi.measure.eval_age_months>60)&(latest_measure.bsi.measure.eval_age_months<216),2,(latest_measure.bsi.measure.eval_age_months>216),3) title 'age_bin'"
subset='''}?!is_null(latest_measure.bsi.sum_ever)'''
def lister(filey):
	i=1
	listing=[]
	while(1):
		listing.append(re.sub('"','',re.sub('\n','',linecache.getline(filey,i))))
		i+=1
		if (linecache.getline(filey,i)==''):
			break
	return listing
def matcher(match,template):
	matched=[]
	for i in match:
		for j in template:
			if (re.search(j,i) ):
				matched.append(i)
	return matched

def freqquer(title,status,listin):
	query=",(0"
	for i in listin:
		if (re.search(status,i)):
			query+="+if("+i+">'0'&"+i+"<'4',1,"+i+"=='0' |"+i+">='4'| is_null("+i+"),0)" 
	query+=') title"' +title+'"'
	return query
def summer(title,status,listin):
	query=",(0"
	for i in listin:
		if (re.search(status,i)):
			query+="+if("+i+">'0'&"+i+"<'4',"+i+",'0')" 			
	query+=') title"' +title+'"'
	return query
tmplst=lister("./temp.csv")
mtch=lister("./org.csv")
tmpis=lister("./is.csv")
tmpnagrs=lister("./nonaggress.csv")

twrt=matcher(mtch,tmplst)
twrtis=matcher(mtch,tmpis)
twrtnarg=matcher(mtch,tmpnagrs)
i=0


#adds all items to BSIQ
for i in mtch:
	query+=","+i

#adds all RSM evers
query+=freqquer("bsiq_freq_rsm_ever","ever",twrt)
query+=summer("bsiq_sum_rsm_ever","ever",twrt)

#adds all RSM current
query+=freqquer("bsiq_freq_rsm_current","current",twrt)
query+=summer("bsiq_sum_rsm_current","current",twrt)
#adds all IS evers
query+=freqquer("bsiq_freq_is_ever","ever",twrtis)
query+=summer("bsiq_sum_is_ever","ever",twrtis)

#adds all IS current
query+=freqquer("bsiq_freq_is_current","current",twrtis)
query+=summer("bsiq_sum_is_current","current",twrtis)

#adds all non aggresive current
query+=freqquer("bsiq_freq_nonagr_current","current",twrt)
query+=summer("bsiq_sum_nonagr_current","current",twrt)

#adds all non aggresive evers
query+=freqquer("bsiq_freq_nonagr_current","ever",twrt)
query+=summer("bsiq_sum_nonagr_current","ever",twrt)

query+=subset
writen.write(query)
writen.close()
template.close()
match.close()
print query

