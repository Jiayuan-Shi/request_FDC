import json
import xlwt
import requests

with open('test.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('nutrition')

def req(pageNum):
    api_key = "EnUueKJPEf4nbwogkZZ8bV1k0Ec7UW6fLNlBMjdc"
    params = {
        'api_key': api_key,
        'dataType': ['SR Legacy'],  # Foundation, Branded, Survey (FNDDS), SR Legacy
        'pageSize': 200,  # 指定每页的最大结果数
        'pageNumber': pageNum,  # 指定要检索的页码
        'sortBy': 'dataType.keyword',  # 指定按描述字段排序
        'sortOrder': 'asc'  # 指定排序顺序
    }

    # 构建API请求的URL
    url = 'https://api.nal.usda.gov/fdc/v1/foods/list'

    response = requests.get(url, params=params)

    # 检查响应的状态码
    if response.status_code == 200:
        # 解析响应内容（JSON格式）
        foods = response.json()
        #print(foods)
        if foods == {}:
            return False
        return foods
    else:
        #print(response.status_code)
        return False

def main():
    json_foods = []
    for pageNum in range(1, 40):
        res = req(pageNum)
        if res != False :
            json_foods.extend(req(pageNum))

    f = open(r"SR_Legacy.json", "w")
    f.write(json.dumps(json_foods))
    f.close()

if __name__ == '__main__':
    main()