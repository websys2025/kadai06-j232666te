import requests
import json

# -----------------------------------------------------------------------------
# 取得するデータの種類
#   「家計調査 家計収支編 二人以上の世帯」
#   二人以上の世帯が、ひと月にどれくらいの収入を得て、何にどれくらい
#   お金を使っているか（支出）を示す統計です。個人の消費動向や景気を
#   判断するための重要な資料として利用されます。
#   ・統計表ID: 0003427113
#
# エンドポイントと機能
#   ・エンドポイント: https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData
#   ・機能: 統計データ取得 (getStatsData)
#     指定した統計表IDのデータをJSON形式で取得します。
#
# 使い方 (主要なAPIパラメータ)
#   ・appId:e-Statで取得したアプリケーションID。
#   ・statsDataId:取得したい統計データのID。
#   ・cdTime:調査年月をYYYYMM形式で指定。例: '202004'
#   ・limit:取得するデータ件数を制限。
# -----------------------------------------------------------------------------


APP_ID = "746059d951bae69b35011fbfa80cd7d5e544f534"

API_URL = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "statsDataId": "0003427113",
    "cdTime": "202004",
    "limit": 5
}

if "" in APP_ID:
    print("エラー: プログラム内の `APP_ID` をご自身のe-StatアプリケーションIDに書き換えてください。")
else:
    print("家計調査（2020年4月分）のデータを取得します...")

    response = requests.get(API_URL, params=params)

    data = response.json()
    print("\n--- 取得したデータ (JSON形式) ---")
    print(json.dumps(data, indent=2, ensure_ascii=False))
