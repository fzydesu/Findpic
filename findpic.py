import webbrowser as w
web = 0 # 0unsure 1JM 2Pixiv
jmurl = 'https://18comic.vip/album/'
pixivurl = 'https://www.pixiv.net/artworks/'
num = input('请输入车号：')
if (num[0]=='J' and num[1]=='M') or (num[0]=='j' and num[1]=='m'):
    web = 1
    num = num[2:]
numi = int(num)
if 0 < numi < 500000:
    web = 1
elif 500000 < numi < 150000000:
    web = 2
if web == 1:
    print('判断为禁漫号，正在打开……\n网址：',jmurl+num)
    w.open(jmurl+num)
elif web == 2:
    print('判断为P站号，正在打开……\n网址：',pixivurl+num)
    w.open(pixivurl+num)
else:
    print('未知的车号\n')
input('\n回车退出……')
# key = url.split('&')[1]
# md5 = key.split('=')[1]
# pdf_left = 'https://r2-ndr.ykt.cbern.com.cn/edu_product/esp/assets_document/'
# pdf_right = '.pkg/pdf.pdf'
# pdf_url = pdf_left + md5 + pdf_right
# print('获取链接:',pdf_url,sep='\n')
# w.open(pdf_url)
# input('按下Enter退出:')
