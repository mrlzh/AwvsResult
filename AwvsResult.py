# coding: utf-8
import csv,re,os,cgi

resultpath='./aaaa'
dirlist=os.listdir(resultpath)
allresultfile=open('vulresult.html','w+')
htmlhear='''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="en">
<head>
	<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
	<title>VulResult</title>
</head>
<body>
'''
allresultfile.writelines(htmlhear)
for dirname in dirlist:
	if os.path.isdir(resultpath+'/'+dirname):
		filelist=os.listdir(resultpath+'/'+dirname)
		for filename in filelist:
			if '.csv' in filename:

				csvfile = file(resultpath+'/'+dirname+'/'+filename, 'rb')
				reader = csv.reader(csvfile)
				allresultfile.writelines('<ul>\n<h3>'+dirname+'<h3>\n')
				for line in reader:
					try:
						line[3]
					except:
						continue
					if  re.match('\[.*', line[3]) and not re.match('\[TCrawler.*', line[3]):
						print line[3]
						allresultfile.writelines('<li style=" font-size: 13px;">'+cgi.escape(line[3])+'</li>\n')
				allresultfile.writelines('</ul>\n')
				csvfile.close()
allresultfile.writelines('</body>\n</html>')
allresultfile.close()