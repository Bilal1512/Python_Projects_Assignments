import re
import os
import csv

def rename_FIR(folder_name):
	    # rename Logic 
	path = 'Subtitles'+'\\'+folder_name
	for filename in os.listdir(path):
		try:
			extension = (re.split(r'\.',filename)[-1]).strip()
			all_num = re.findall(r'\d+',filename)
			episode_number = all_num[0]
			if(int(episode_number_padding)>len(episode_number)):
				episode_number = '0'*(int(episode_number_padding)-len(episode_number))+ episode_number
			path =os.path.join(os.getcwd(),path)        
			os.chdir(path)
			os.rename(filename,'FIR -' + ' Episode ' + episode_number+ '.' + extension) 
		except:
			os.remove(filename)  

def rename_Game_of_Thrones(folder_name):
	    # rename Logic  
	path = 'Subtitles'+'\\'+folder_name
	for filename in os.listdir(path):
		try:
			info = filename.split('-')
			season_number=re.findall(r'\d+',info[1])[0]
			episode_number=re.findall(r'\d+',info[1])[1]
			extension = (re.split(r'\.',filename)[-1]).strip()
			name = (re.split(r'\.',info[2])[0]).strip()
			if(len(season_number) < int(season_number_padding)):
				season_number = '0'*(int(season_number_padding)-len(season_number)) + season_number
			if(len(episode_number) < int(episode_number_padding)):
				episode_number = '0'*(int(episode_number_padding)-len(episode_number)) + episode_number
			path=os.path.join(os.getcwd(),path)      
			os.chdir(path)
			os.rename(filename,'Game of Thrones - Season '+ season_number +' Episode ' + episode_number + ' - ' + name + '.' + extension)  
		except:
			os.remove(filename)  

def rename_How_I_Met_Your_Mother(folder_name):
        # rename Logic  
	path = 'Subtitles'+'\\'+folder_name
	for filename in os.listdir(path):
		try:
			info = filename.split('-')
			season_number=re.findall(r'\d+',info[1])[0]
			episode_number=re.findall(r'\d+',info[1])[1]
			extension = (re.split(r'\.',filename)[-1]).strip()
			name = (re.split(r'\.',info[2])[0]).strip()
			if(len(season_number) < int(season_number_padding)):
				season_number = '0'*(int(season_number_padding)-len(season_number)) + season_number
			if(len(episode_number) < int(episode_number_padding)):
				episode_number = '0'*(int(episode_number_padding)-len(episode_number)) + episode_number
			path=os.path.join(os.getcwd(),path)      
			os.chdir(path)
			os.rename(filename,'How I Met Your Mother - Season '+ season_number + ' Episode ' + episode_number + ' - ' + name + '.' + extension) 
		except:
			os.remove(filename)