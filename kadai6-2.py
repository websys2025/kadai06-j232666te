import requests
import json

# -----------------------------------------------------------------------------
# 取得するデータの種類
#   「人口動態調査 人口動態統計 確定数 出生」
#   日本における年間の出生数について、都道府県や出生場所（病院、診療所など）
#   ごとに集計した統計データです。少子化の動向や地域ごとの特徴を
#   分析するために利用されます。
#   ・統計表ID: 0003411627
#
# エンドポイントと機能
#   ・エンドポイント: https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData
#   ・機能: 統計データ取得 (getStatsData)
#     指定した統計表IDのデータをJSON形式で取得します。
#
# 使い方 (主要なAPIパラメータ)
#   ・appId:e-Statで取得したアプリケーションID。
#   ・statsDataId:取得したい統計データのID。
#   ・metaGetFlg:'Y'にすると、コードに対応する名称などのメタデータを取得できる。
#   ・limit:取得するデータ件数を制限。
# -----------------------------------------------------------------------------

APP_ID = "0418cef46892296c1554462f207ed34e020dab2b"

API_URL = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "statsDataId": "0003411627",
    "lang": "J",
    "metaGetFlg": "Y",
    "limit": 10
}

print("人口動態調査（出生数）のデータを取得します...")

response = requests.get(API_URL, params=params)
data = response.json()

statistical_data = data["GET_STATS_DATA"]["STATISTICAL_DATA"]

class_info = statistical_data["CLASS_INF"]["CLASS_OBJ"]

area_map = {}
area_obj = next((obj for obj in class_info if obj.get('@id') == 'area'), None)
if area_obj:
    area_map = {item['@code']: item['@name'] for item in area_obj['CLASS']}

cat01_map = {}
cat01_obj = next((obj for obj in class_info if obj.get('@id') == 'cat01'), None)
if cat01_obj:
    cat01_map = {item['@code']: item['@name'] for item in cat01_obj['CLASS']}

values = statistical_data["DATA_INF"]["VALUE"]

print("\n--- 人口動態調査 出生数データ（抜粋） ---")
for item in values:
    year = item.get('@time', 'N/A')
    area_name = area_map.get(item.get('@area', ''), 'N/A')
    cat01_name = cat01_map.get(item.get('@cat01', ''), 'N/A')
    births = item.get('$', 'N/A')

    print(f"調査年: {year[:4]}年, 都道府県: {area_name}, 場所: {cat01_name}, 出生数: {births}人")
