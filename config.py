import requests
import sys
from requests_toolbelt.multipart.encoder import MultipartEncoder
path = './/test//'

def login(host):
    burp0_url = "http://"+host+"/index.php/admin/authentication/sa/login"
    burp0_cookies = {"PHPSESSID": "d1f05cefe8bec342c61a93cc722b75e1", "YII_CSRF_TOKEN": "Q1h-QUJKZ2x4a09hR3JmdWQ3eVFFNWxHTmtXX0ZqMHZGaRXh68Lir7Dx9LLsALqnWMWyzp6sbmucRtDTeYVf8w=="}
    burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://192.168.1.237:8082", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://192.168.1.237:8082/index.php/admin/authentication/sa/login", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    burp0_data = {"YII_CSRF_TOKEN": "Q1h-QUJKZ2x4a09hR3JmdWQ3eVFFNWxHTmtXX0ZqMHZGaRXh68Lir7Dx9LLsALqnWMWyzp6sbmucRtDTeYVf8w==", "authMethod": "Authdb", "user": "admin", "password": "password", "loginlang": "default", "action": "login", "width": "1536", "login_submit": "login"}
    session = requests.session()
    res=session.post(burp0_url, headers=burp0_headers,data=burp0_data,verify=False,cookies=burp0_cookies,allow_redirects=False)
    #print(res.text)
    location=res.headers
    phin = requests.utils.dict_from_cookiejar(session.cookies)
    r2=str(phin)
    r1=r2[15:47]
    return r1

def setting(r1,host):
# language  user  email
    burp0_url = "http://"+host+"/index.php/admin/globalsettings"
    burp0_cookies = {"PHPSESSID": r1, "YII_CSRF_TOKEN": "Q1h-QUJKZ2x4a09hR3JmdWQ3eVFFNWxHTmtXX0ZqMHZGaRXh68Lir7Dx9LLsALqnWMWyzp6sbmucRtDTeYVf8w=="}
    burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://"+host+"", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://"+host+"/index.php/admin/globalsettings", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    burp0_data = {"YII_CSRF_TOKEN": "Q1h-QUJKZ2x4a09hR3JmdWQ3eVFFNWxHTmtXX0ZqMHZGaRXh68Lir7Dx9LLsALqnWMWyzp6sbmucRtDTeYVf8w==", "sitename": "ChinaMobile", "defaulttheme": "fruity", "admintheme": "Sea_Green", "timeadjust": "0", "ipInfoDbAPIKey": '', "googleMapsAPIKey": '', "googleanalyticsapikey": '', "googletranslateapikey": '', "characterset": "auto", "maintenancemode": "off", "sideMenuBehaviour": "adaptive", "defaultquestionselectormode": "default", "defaultthemeteeditormode": "default", "javascriptdebugbcknd": "0", "javascriptdebugfrntnd": "0", "allow_unstable_extension_update": "0", "siteadminemail": "ChinaMobile@163.com", "siteadminname": "ChinaMobile", "emailmethod": "mail", "emailsmtpssl": '', "emailsmtpdebug": "0", "maxemails": "50", "siteadminbounce": "ChinaMobile@163.com", "bounceaccounttype": "off", "bounceencryption": "off", "surveyPreview_require_Auth": "0", "surveyPreview_require_Auth": "1", "filterxsshtml": "0", "filterxsshtml": "1", "filterxsshtml": "0", "filterxsshtml": "1", "usercontrolSameGroupPolicy": "0", "usercontrolSameGroupPolicy": "1", "x_frame_options": "sameorigin", "force_ssl": "off", "repeatheadings": "25", "pdffontsize": "9", "pdflogowidth": "50", "pdfheadertitle": '', "pdfheaderstring": '', "pdfshowsurveytitle": "0", "pdfshowsurveytitle": "1", "pdfshowheader": "0", "bPdfQuestionFill": "0", "bPdfQuestionFill": "1", "bPdfQuestionBold": "0", "bPdfQuestionBorder": "0", "bPdfQuestionBorder": "1", "bPdfResponseBorder": "0", "bPdfResponseBorder": "1", "defaultlang": "zh-Hans", "RPCInterface": "off", "rpc_publish_api": "0", "add_access_control_header": "0", "add_access_control_header": "1", "global-settings-storage-url": "/index.php/admin/globalsettings?sa=getStorageData", "overwritefiles": "0", "restrictToLanguages": "fil run kmr so es-CO tl tg ug zh-Hant-TW zh-Hant-HK da uk ur hy ru bg si hr lv cnr is gl ca-valencia hu hi af lb id gu ky tr rw sr-Latn sr oc cy bn ful eu he el pap-CW ckb de de-informal it ca it-informal ko nn nb cs cs-informal sl sk swh pa ja ps ka fr pl fa ta th pl-informal ie sv be zu lt zh-Hans mya ml ro et bs fi en nl nl-informal pt pt-BR mn es es-MX es-CL es-AR es-AR-informal vi prs am sq ar mk mt mr ms", "action": "globalsettingssave"}
    r=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)

def adduser(r1,host):
    burp0_url = "http://"+host+"/index.php/admin/usermanagement?sa=applyedit"
    burp0_cookies = {"PHPSESSID": r1, "YII_CSRF_TOKEN": "Q1h-QUJKZ2x4a09hR3JmdWQ3eVFFNWxHTmtXX0ZqMHZGaRXh68Lir7Dx9LLsALqnWMWyzp6sbmucRtDTeYVf8w=="}
    burp0_headers = {"Accept": "application/json, text/javascript, */*; q=0.01", "X-Requested-With": "XMLHttpRequest", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Origin": "http://"+host+"", "Referer": "http://"+host+"/index.php/admin/usermanagement/sa/view", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    burp0_data = {"YII_CSRF_TOKEN": "Q1h-QUJKZ2x4a09hR3JmdWQ3eVFFNWxHTmtXX0ZqMHZGaRXh68Lir7Dx9LLsALqnWMWyzp6sbmucRtDTeYVf8w==", "User[uid]": '', "User[users_name]": "cuc", "User[full_name]": "cucedu", "User[email]": "cuc@cuc.com", "preset_password": "1", "User[password]": "12345678", "password_repeat": "12345678", "random_example_password": "pjozsaux"}
    requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)


def power(r1,host):
    burp0_url = "http://"+host+"/index.php/admin/usermanagement?sa=saveuserpermissions"
    burp0_cookies = {"YII_CSRF_TOKEN": "Q1h-QUJKZ2x4a09hR3JmdWQ3eVFFNWxHTmtXX0ZqMHZGaRXh68Lir7Dx9LLsALqnWMWyzp6sbmucRtDTeYVf8w==", "PHPSESSID": r1}
    burp0_headers = {"Accept": "application/json, text/javascript, */*; q=0.01", "X-Requested-With": "XMLHttpRequest", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Origin": "http://"+host+"", "Referer": "http://"+host+"/index.php/admin/usermanagement/sa/view", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    burp0_data = {"YII_CSRF_TOKEN": "Q1h-sQUJKZ2x4a09hR3JmdWQ3eVFFNWxHTmtXX0ZqMHZGaRXh68Lir7Dx9LLsALqnWMWyzp6sbmucRtDTeYVf8w==", "userid": "2", "PermissionAll[surveys]": "on", "Permission[surveys][read]": "on", "PermissionAll[auth_db]": "on", "Permission[auth_db][read]": "on"}
    requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
    

def addfile(r1,host):
    filename='limesurvey_survey_113688.lss'
    filepath=path+'//limesurvey_survey_113688.lss'
    multipart_encoder = MultipartEncoder(
        fields={
            "YII_CSRF_TOKEN": "Q1h-QUJKZ2x4a09hR3JmdWQ3eVFFNWxHTmtXX0ZqMHZGaRXh68Lir7Dx9LLsALqnWMWyzp6sbmucRtDTeYVf8w==",
            "Content-Type": "application/octet-stream",
            "the_file": (
            "limesurvey_survey_113688.lss", open(filepath,'rb'), 'application/octet-stream'),
            "translinksfields":"0",
            "translinksfields":"1",
            "sid":"0",
            "action":"importsurvey"
        },
        boundary="------WebKitFormBoundarywhDbqnsYUfLX8XYI"
    )

    burp0_data=multipart_encoder 
    burp0_url = "http://"+host+"/index.php/admin/survey/sa/copy"
    burp0_cookies = {"YII_CSRF_TOKEN": "Q1h-QUJKZ2x4a09hR3JmdWQ3eVFFNWxHTmtXX0ZqMHZGaRXh68Lir7Dx9LLsALqnWMWyzp6sbmucRtDTeYVf8w==", "PHPSESSID": r1}
    burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://"+host+"", "Content-Type": "multipart/form-data; boundary=------WebKitFormBoundarywhDbqnsYUfLX8XYI", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://"+host+"/index.php/admin/survey/sa/newsurvey", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    r=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
    #print(r.text)

def addfile2(r1,host):
    filename='limesurvey_survey_447419.lss'
    filepath=path+'//limesurvey_survey_447419.lss'
    multipart_encoder = MultipartEncoder(
        fields={
            "YII_CSRF_TOKEN": "Q1h-QUJKZ2x4a09hR3JmdWQ3eVFFNWxHTmtXX0ZqMHZGaRXh68Lir7Dx9LLsALqnWMWyzp6sbmucRtDTeYVf8w==",
            "Content-Type": "application/octet-stream",
            "the_file": (
            "limesurvey_survey_447419.lss", open(filepath,'rb'), 'application/octet-stream'),
            "translinksfields":"0",
            "translinksfields":"1",
            "sid":"0",
            "action":"importsurvey"
        },
        boundary="------WebKitFormBoundarywhDbqnsYUfLX8XYI"
    )

    burp0_data=multipart_encoder 
    burp0_url = "http://"+host+"/index.php/admin/survey/sa/copy"
    burp0_cookies = {"YII_CSRF_TOKEN": "Q1h-QUJKZ2x4a09hR3JmdWQ3eVFFNWxHTmtXX0ZqMHZGaRXh68Lir7Dx9LLsALqnWMWyzp6sbmucRtDTeYVf8w==", "PHPSESSID": r1}
    burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://"+host+"", "Content-Type": "multipart/form-data; boundary=------WebKitFormBoundarywhDbqnsYUfLX8XYI", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://"+host+"/index.php/admin/survey/sa/newsurvey", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    r=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
    #print(r.text)


def addfile3(r1,host):        
    filename='limesurvey_survey_449682.lss'
    filepath=path+'//limesurvey_survey_449682.lss'
    multipart_encoder = MultipartEncoder(
        fields={
            "YII_CSRF_TOKEN": "Q1h-QUJKZ2x4a09hR3JmdWQ3eVFFNWxHTmtXX0ZqMHZGaRXh68Lir7Dx9LLsALqnWMWyzp6sbmucRtDTeYVf8w==",
            "Content-Type": "application/octet-stream",
            "the_file": (
            "limesurvey_survey_449682.lss", open(filepath,'rb'), 'application/octet-stream'),
            "translinksfields":"0",
            "translinksfields":"1",
            "sid":"0",
            "action":"importsurvey"
        },
        boundary="------WebKitFormBoundarywhDbqnsYUfLX8XYI"
    )

    burp0_data=multipart_encoder 
    burp0_url = "http://"+host+"/index.php/admin/survey/sa/copy"
    burp0_cookies = {"YII_CSRF_TOKEN": "Q1h-QUJKZ2x4a09hR3JmdWQ3eVFFNWxHTmtXX0ZqMHZGaRXh68Lir7Dx9LLsALqnWMWyzp6sbmucRtDTeYVf8w==", "PHPSESSID": r1}
    burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://"+host+"", "Content-Type": "multipart/form-data; boundary=------WebKitFormBoundarywhDbqnsYUfLX8XYI", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://"+host+"/index.php/admin/survey/sa/newsurvey", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    r=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
    #print(r.text)

def addfile4(r1,host):
    filename='limesurvey_survey_761995.lss'
    filepath=path+'//limesurvey_survey_761995.lss'
    multipart_encoder = MultipartEncoder(
        fields={
            "YII_CSRF_TOKEN": "Q1h-QUJKZ2x4a09hR3JmdWQ3eVFFNWxHTmtXX0ZqMHZGaRXh68Lir7Dx9LLsALqnWMWyzp6sbmucRtDTeYVf8w==",
            "Content-Type": "application/octet-stream",
            "the_file": (
            "limesurvey_survey_761995.lss", open(filepath,'rb'), 'application/octet-stream'),
            "translinksfields":"0",
            "translinksfields":"1",
            "sid":"0",
            "action":"importsurvey"
        },
        boundary="------WebKitFormBoundarywhDbqnsYUfLX8XYI"
    )

    burp0_data=multipart_encoder 
    burp0_url = "http://"+host+"/index.php/admin/survey/sa/copy"
    burp0_cookies = {"YII_CSRF_TOKEN": "Q1h-QUJKZ2x4a09hR3JmdWQ3eVFFNWxHTmtXX0ZqMHZGaRXh68Lir7Dx9LLsALqnWMWyzp6sbmucRtDTeYVf8w==", "PHPSESSID": r1}
    burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://"+host+"", "Content-Type": "multipart/form-data; boundary=------WebKitFormBoundarywhDbqnsYUfLX8XYI", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://"+host+"/index.php/admin/survey/sa/newsurvey", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    r=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
    #print(r.text)

def check_config(r1,host):
    burp0_url = "http://"+host+"/index.php/admin/survey/sa/listsurveys"
    burp0_cookies = {"PHPSESSID": r1, "YII_CSRF_TOKEN": "Q1h-QUJKZ2x4a09hR3JmdWQ3eVFFNWxHTmtXX0ZqMHZGaRXh68Lir7Dx9LLsALqnWMWyzp6sbmucRtDTeYVf8w=="}
    burp0_headers = {"Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://"+host+"/index.php/admin", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    #print(r.text)    
    return r

if __name__ == "__main__":
   host = sys.argv[1]
   #host="web"
   #host="192.168.1.100"
   r1=login(host)
   result1=check_config(r1,host)
   setting(r1,host)
   adduser(r1,host) 
   power(r1,host)   
   addfile(r1,host)
   addfile2(r1,host)
   addfile3(r1,host)
   addfile4(r1,host)
   result2 = check_config(r1,host)
   target_info = '中国移动套餐满意度'
   if (target_info not in result1.text and target_info in result2.text):
        print('Config success!')
        exit(0)
   else:
        print('Config failed!')
        exit(-1)
