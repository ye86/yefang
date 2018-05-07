import urllib.request

import os

def url_open(url):
	
	req = urllib.request.Request(url)
	
	req.add_header('User-Agent',"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36")

	response = urllib.request.urlopen(req)
	html = response.read()
	return html

#def get_page(url):
#	html = url_open(url).decode('utf-8')
#	a = html.find('current-comment-page')+23
#	b = html.find(']',a)
#	print(url)
#	return html[a:b]




def save_imgs(folder,img_addrs):
	
	filename = img_addrs.split('/')[-1]
	with open(filename,'wb') as f:
		img = url_open(img_addrs)
		f.write(img)

def download_mm(folder='cat',url="http://ww3.sinaimg.cn/mw600/0073ob6Pgy1fpehyyct3yj30ho0qowgh.jpg"):
	try:
		os.mkdir(folder)
	except(SyntaxError,FileExistsError):
		print("目录已存在！")
	os.chdir(folder)
	



	img_adds = url

	save_imgs(folder,img_adds)


if __name__ == '__main__':
	download_mm("xxoo","http://ww3.sinaimg.cn/mw600/0073ob6Pgy1fpehyyct3yj30ho0qowgh.jpg")


