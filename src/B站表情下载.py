# -*- coding: utf-8 -*-
import requests
import os
import winreg

true = True
false = False
null = None

def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return winreg.QueryValueEx(key, "Desktop")[0]
桌面路径 = get_desktop().replace("\\","/").replace('"','')

SESSDATA = input("请输入SESSDATA：")
bili_jct = input("请输入bili_jct：")

while True: # 一直循环
    choose = input("1、保存到桌面 2、自定义保存路径 [1/2] ")
    if choose == "1" or choose == "2": # 用户的选择有效
        break # 跳出循环
    print ("请输入数字：1或2！")

if choose == "1": # 保存到桌面
    保存路径 = 桌面路径
if choose == "2": # 自定义保存路径
    保存路径 = input("请输入保存路径：").replace("\\","/").replace('"','')
print()

try:
    os.makedirs(保存路径 + "/表情下载") # 新建表情下载目录
except FileExistsError: # 如果文件夹已存在则跳过
    pass
    
headers = {"Cookie": "SESSDATA=" + SESSDATA + "; bili_jct=" + bili_jct, "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}

result = eval(requests.get('https://api.bilibili.com/x/emote/user/panel?&build=6371100&business=reply&c_locale=zh_CN&channel=ss_baidusem_014&mobi_app=android&platform=android&s_locale=zh_CN&statistics={"appId":1,"platform":3,"version":"6.37.1","abtest":""}',headers=headers).text)["data"]["packages"]
for 表情集循环 in range(0,len(result)):
    if result[表情集循环]["id"] == 0 or result[表情集循环]["id"] == 4: # 如果表情集是“最近使用”或“颜文字”
        continue # 跳过本循环
    表情集名称=result[表情集循环]["text"]
    print("正在下载表情集“" + 表情集名称 + "”...")
    try:
        os.makedirs(保存路径 + "/表情下载/" + 表情集名称)
    except FileExistsError: # 如果文件夹已存在则跳过
        pass
    for 表情循环 in range(0,len(result[表情集循环]["emote"])):
        表情名称=result[表情集循环]["emote"][表情循环]["text"].replace("?","？")
        表情链接=result[表情集循环]["emote"][表情循环]["url"]
        if result[表情集循环]["emote"][表情循环].get("gif_url") != None: # 如果该表情有gif动图
            表情链接=result[表情集循环]["emote"][表情循环]["gif_url"] # 替换表情链接为gif动图表情链接
        表情文件=requests.get(表情链接).content
        with open(保存路径 + "/表情下载/" + 表情集名称 + "/" + 表情名称 + os.path.splitext(os.path.split(表情链接)[1])[1],mode="wb") as file:
            file.write(表情文件)
        file.close()
        
print()
print("已下载完毕！")