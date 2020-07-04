import requests
from bs4 import BeautifulSoup
import execjs, json, time, datetime

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}
submitHeaders = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8'
}
config = json.load(open('config.json'))  # 密码账号配置
submitData = json.load(open('submit.json', encoding='utf8'))  # 上报资料设置
# 网址
url = 'https://sso.scut.edu.cn/cas/login?service=https%3A%2F%2Fiamok.scut.edu.cn%2Fcas%2Flogin'
loginPostUrl = 'https://sso.scut.edu.cn/cas/login?service=https://iamok.scut.edu.cn/cas/login'
submitPostUrl = 'https://iamok.scut.edu.cn/mobile/recordPerDay/submitRecordPerDay'

session = requests.Session()
# 登录
req = session.get(url, headers=headers)
soup = BeautifulSoup(req.text, features='lxml')

# 获取验证登录的各个参数值
u = config['account']
p = config['password']
lt = soup.find(id='lt').attrs['value']
with open('./des.js') as f:
    ctx = execjs.compile(f.read())
    rsa = ctx.call('strEnc', u + p + lt, '1', '2', '3')
postData = {
    'rsa': rsa,
    'ul': len(u),
    'pl': len(p),
    'lt': lt,
    'execution': 'e1s1',
    '_eventId': 'submit',
}
loginReq = session.post(loginPostUrl, postData, headers=headers)

# 报平安
today = str(datetime.date.today())
# 设置时间为今日0时
submitData["recordDate"] = submitData[
    "visitingRelativesOrTravelToWenzhouDate"] = submitData[
        "recordShowDate"] = round(time.mktime(time.strptime(today,
                                                            '%Y-%m-%d')))
# 设置时间为现在
submitData["createTime"] = submitData["updateTime"] = round(time.time())
submitReq = session.post(submitPostUrl,
                         json.dumps(submitData),
                         headers=submitHeaders)
