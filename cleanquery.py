#This program cleans up HTSQL queries pulled from RexDB. 
    #Copyright (C) 2013 Frank Jackson

    #This program is free software: you can redistribute it and/or modify
    #it under the terms of the GNU General Public License as published by
    #the Free Software Foundation, either version 3 of the License

    #This program is distributed in the hope that it will be useful,
    #but WITHOUT ANY WARRANTY; without even the implied warranty of
    #MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    #GNU General Public License for more details.

    #You should have received a copy of the GNU General Public License
    #along with this program.  If not, see <http://www.gnu.org/licenses/>.
import re

readen=open('./query','r')
partial=''
quoted=False
writen=open('./built.quer','w')
finished=''

for c in readen.readline():
	if c!='''"''' and quoted==False:
		partial+=c
	elif c=='''"''' and quoted==False:
		quoted=True
	elif c=='''"''' and quoted==True:
		quoted=False

finished=re.sub(r'title','',partial)
writen.write(finished)
readen.close()
writen.close()








