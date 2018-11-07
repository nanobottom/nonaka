# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup 

print("Password>>", end = "")
password = input()
login_info = {
        "SsLogonUser":"01159503",
        "SsLogonPassword":password,
        "CookieOn":"1",
        "SsLogonHost":"100",
        "SsLoginPage":"/Members/Personal/KBSSettei/KBSRule.asp",
        }

# ログイン
session = requests.session()
session.post("https://s10.kabu.co.jp/_mem_bin/Members/verifpwd.asp", data = login_info)

# 資産管理>現物株式>残高照会のページへアクセスする
res = session.get("https://s20.si1.kabu.co.jp/ap/PC/Stocks/Stock/Position/List?actType=TOKUTEI")
# 文字化けを直す
#res.encoding = res.apparent_encoding
# エラーならここで例外発生
res.raise_for_status()
# ログインページパース
soup = BeautifulSoup(res.content, "html.parser")
print(soup)