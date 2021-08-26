import requests
import json
import os
from Crypto.Cipher import AES
import base64
import codecs
import pynlpir

def aesEncrypt(text, secKey):
	pad = 16 - len(text) % 16
	# print(type(text))
	# print(type(pad))
	# print(type(pad * chr(pad)))
	# text = text + str(pad * chr(pad))
	if isinstance(text, bytes):
		# print("type(text)=='bytes'")
		text = text.decode('utf-8')
	# print(type(text))
	text = text + str(pad * chr(pad))
	if not isinstance(secKey, bytes):
		#print('secKey ={0}'.format(type(secKey)))
		secKey = secKey.encode(encoding = "utf-8")
		#print('secKey ={0}'.format(type(secKey)))
	iv = b'0102030405060708'
	encryptor = AES.new(secKey, 2, iv)
	if not isinstance(text, bytes):
		#print('text ={0}'.format(type(text)))
		text = text.encode(encoding = "utf-8")
		#print('text ={0}'.format(type(text)))
	ciphertext = encryptor.encrypt(text)
	ciphertext = base64.b64encode(ciphertext)
	return ciphertext

def rsaEncrypt(text, pubKey, modulus):
	text = text[::-1]
	#	rs = int(text.encode('hex'), 16)**int(pubKey, 16)%int(modulus, 16)
	rs = int(codecs.encode(text.encode('utf-8'), 'hex_codec'), 16) ** int(pubKey, 16) % int(modulus, 16)
	return format(rs, 'x').zfill(256)

modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
nonce = '0CoJUm6Qyw8W8jud'
pubKey = '010001'

def createSecretKey(size):
	return (''.join(map(lambda xx: (hex(ord(xx))[2:]), str(os.urandom(size)))))[0:16]

#通过输入信息，返回字典
def get_it_comments(Querysong):
	url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
	headers = {
		'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
		'referer' : 'https://music.163.com/'
		}

	comment_list = []
	count = 0
	text = {
			'hlpretag':'',
			'hlposttag':'',
			's':Querysong,
			'type':'1',
			'offset':'0',
			'total':'true',
			'limit':'30',
			'csrf_token':''
		}
	text = json.dumps(text)
	secKey = createSecretKey(16)
	encText = aesEncrypt(aesEncrypt(text, nonce), secKey)
	encSecKey = rsaEncrypt(secKey, pubKey, modulus)
	payload = {
		'params': encText,
		'encSecKey': encSecKey
		}

	r = requests.post(url, headers=headers, data=payload)
	r.raise_for_status()
	#转成字典
	r_dic = json.loads(r.text)
	r_song = r_dic["result"]["songs"]
	return r_song

	
songs_Id=[]
music_name=[]

#通过字典显示列表参数
def Show_List(r_dic):
	songs_Id.clear
	music_name.clear
	for i in range(len(r_dic)):
		music_name.append(r_dic[i]['name'] + '_' + r_dic[i]['ar'][0]["name"])
		print('{}.{}'.format(i + 1,music_name[i]))
		songs_Id.append((r_dic[i]['id']))


if __name__ == '__main__':
	#w=input('输入歌名\歌手:')
	w = "明年今日"
	Show_List(get_it_comments(w))
