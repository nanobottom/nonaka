# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
#url = "https://s10.kabu.co.jp/_mem_bin/members/login.asp?/Members/Personal/KBSSettei/KBSRule.asp"
login_info = {
        "SsLogonUser":"01159503",
        "SsLogonPassword":"nano8088",
        "CookieOn":"1",
        "SsLogonHost":"100",
        "SsLoginPage":"/Members/Personal/KBSSettei/KBSRule.asp",
        }

#response = requests.get(url)
#soup = BeautifulSoup(response.content, 'html.parser')
#print(soup)


# ログイン
session = requests.session()
session.post("https://s10.kabu.co.jp/_mem_bin/Members/verifpwd.asp", data = login_info)

# 資産管理>現物株式のページへアクセスする
res = session.get("https://s20.si1.kabu.co.jp/ap/PC/Stocks/Stock/History/List")
# 文字化けを直す
response.encoding = response.apparent_encoding
# エラーならここで例外発生
res.raise_for_status()
# ログインページパース
soup = BeautifulSoup(res.content, "html.parser")
print(soup)