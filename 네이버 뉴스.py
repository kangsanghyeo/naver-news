import requests

headers = \
{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}


url = 'https://news.naver.com/'
site = requests.get(url, headers=headers)
source_data = site.text

count = source_data.count('"cjs_t">')

for i in range(count):
      position1 = source_data.find('"cjs_t">')+ len('"cjs_t">')
      source_data = source_data[pos1:]
      
      pos2 = source_data.find('</div>')
      extract_data = source_data[: pos2]

      source_data = source_data[pos2+1:]

      pos3 = source_data.find('"cjs_d">')+ len('"cjs_d">')
      source_data = source_data[pos3:]

      pos4 = source_data.find('</p>')
      a_data = source_data[: pos4]

      source_data = source_data[pos4+1:]
      print(i+1, extract_data,'||', a_data)
