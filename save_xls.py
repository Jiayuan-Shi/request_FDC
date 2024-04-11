import json
import xlwt

def write_data(worksheet, json_data):
    all_nutrients = set()
    for item in json_data:
        for nutrient in item['foodNutrients']:
            #print(nutrient['name'])
            all_nutrients.add(nutrient['name'])

    all_nutrients = list(all_nutrients)

    base_columns = ['FDC ID', 'Description', 'Data Type', 'Publication Date', 'NDB Number']
    columns = base_columns + all_nutrients
    for i, column in enumerate(columns):
        worksheet.write(0, i, column)
    row = 1

    for item in json_data:
        col = 0
        # 写入食物的基本信息
        worksheet.write(row, col, item['fdcId']);
        col += 1
        worksheet.write(row, col, item['description']);
        col += 1
        worksheet.write(row, col, item['dataType']);
        col += 1
        worksheet.write(row, col, item['publicationDate']);
        col += 1
        worksheet.write(row, col, item['ndbNumber']);
        col += 1

        # 为每种营养成分创建一个列值映射
        nutrient_map = {nutrient['name']: nutrient.get('amount', 'N/A') for nutrient in item['foodNutrients']}

        # 根据all_nutrients列表填充每个营养成分的值
        for nutrient in all_nutrients:
            worksheet.write(row, col, nutrient_map.get(nutrient, ''))  # 如果食物不含该营养成分，则写入'N/A'
            col += 1

        row += 1  # 移动到下一行
    return worksheet

def main():
    files = ['test1.json','test2.json']
    all_jsondata = []
    for filename in files:
        with open(filename, 'r', encoding='utf-8') as file:
            # 加载JSON数据
            json_data = json.load(file)
            all_jsondata.extend(json_data)

    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('nutrition')

    worksheet = write_data(worksheet, all_jsondata)
    workbook.save('nutrients_Foundation.xls')

# 保存工作簿
if __name__ == '__main__':
    main()
