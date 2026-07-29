import json
data = [{"name": "张三", "age": 10}, {"name": "李四", "age": 11}, {"name": "王五", "age": 12}]
json_str = json.dumps(data, ensure_ascii=False)
print(json_str)
print(type(json_str))

data2 = {"name": "张三", "age": 10}
json_str2 = json.dumps(data2, ensure_ascii=False)
print(json_str2)

s = '[{"name": "张三", "age": 10}, {"name": "李四", "age": 11}, {"name": "王五", "age": 12}]'
py_str1 = json.loads(s)
print(py_str1, type(py_str1))

s2 = '{"name": "张三", "age": 10}'
py_str2 = json.loads(s2)
print(py_str2, type(py_str2))
