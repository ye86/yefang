from aip import AipSpeech

APP_ID = '10910493'
API_KEY = 'KPCD0hVpRPyif2spWktxojwf'
SECRET_KEY = '3sqTae1NF200d2YKitSPbCplcptPnmtt'

client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)
txt = '你好'

result = client.synthesis(txt,'zh',1,{
		'vol':5,
})

if not isinstance(result,dict):
	with open(txt + '.mp3','wb') as f:
		f.write(result)
		f.close()
		print('语音输出成功')
	
