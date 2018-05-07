import urllib.request

import os

def url_open(url):
	
	req = urllib.request.Request(url)
	
	req.add_header('User-Agent',"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36")

	response = urllib.request.urlopen(req)
	html = response.read()
	return html

def get_page(url):
	html = url_open(url).decode('utf-8')
	a = html.find('current-comment-page')+23
	b = html.find(']',a)
#	print(url)
	return html[a:b]


def find_imgs(url):
	html = url_open(url).decode('utf-8')
	print(html)
#	with open("html.txt","w") as f:
#		f.write(html)
	img_addrs = []
	a = html.find('img src=')
	while a != -1:
		b = html.find('.jpg',a,a+255)
		if b != -1:
			img_addrs.append(html[a+9,b+4])
		else:
			b = a+9
		a = html.find('img src=',b)
	print(img_addrs)
	return img_addrs

def save_imgs(folder,img_addrs):
	for each in img_addrs:
		filename = each.split('/')[-1]
		with open(filename,'wb') as f:
			img = url_open(each)
			f.write(img)

def download_mm(folder='ooxx',pages=10):
	try:
		os.mkdir(folder)
	except(SyntaxError,FileExistsError):
		print("目录已存在！")
	os.chdir(folder)
	
	url = "http://jandan.net/ooxx/"
#	print(url)
	page_num = int(get_page(url))
	print(str(page_num))
	for i in range(pages):
		page_num -= 1
		page_url = url + 'page-' + str(page_num) + '#comments'
#		print(page_url)
		img_adds = find_imgs(page_url)
		save_imgs(folder,img_adds)


if __name__ == '__main__':
	download_mm()


