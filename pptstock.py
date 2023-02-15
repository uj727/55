from distutils.filelist import findall
import requests
from bs4 import BeautifulSoup  
import random
import time
 
user_agent_lis = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"]
my_user_agent = random.choice(user_agent_lis)
url="https://www.ptt.cc/bbs/Stock/index5020.html"
my_headers = {'User-Agent': my_user_agent}
count=0

while count < 1000:    
    r = requests.get(url, headers=my_headers)
    soup = BeautifulSoup(r.text,"html.parser")    
    btn = soup.select('div.btn-group a')#下一頁按鈕
    #在bottunGroup第4個位置
    up_page_href = btn[3]['href']
    # print(up_page_href)
    next_page_url = 'https://www.ptt.cc' + up_page_href
    url= next_page_url
    print(url)
    # target = soup.find_all("div",class_="title")
    target = soup.select('div.title')
    for tt in target:
            if tt.a !=None:
                href = tt.select_one('a').get('href')
                print(tt.a.text)
                print(href)
                            #爬文章內容 先替換url
                url='https://www.ptt.cc'+href
                r = requests.get(url, headers=my_headers)
                soup = BeautifulSoup(r.text,"html.parser")
                    
                        # 查找所有html 元素 抓出內容         
                main_container = soup.find(id='main-container')
                context = main_container.text
                            #  以"-- " 切割成2個陣列 把評論切掉
                context = context.split('※ 發信站')[0]                            
                            # 把每段文字 '\n' 去除
                context = context.split('\n')           
                            # 去頭留內容 
                contents = context[2:]
                            # 內容轉string
                content = '\n'.join(contents)
                print('內容'+content) 
                a=str(count)+'.txt'  
                
                with open(a, 'w',encoding='UTF-8') as f:
                        f.write(str(count))
                        f.write(content)
                        count=count+1
            url = next_page_url
            print(url)   
    time.sleep(2)
        

        
                
                
        







   






