import uuid
import string
import requests
import random
import time
class Instagram:
    def Login(User,Password):
        g1=requests.get('https://i.instagram.com/api/v1/accounts/login/').cookies
        mid=g1['mid']
        ts=round(time.time())
        PigeonSession=f'UFS-{str(uuid.uuid4())}-0'
        IgDeviceId=uuid.uuid4()
        IgFamilyDeviceId=uuid.uuid4()
        a1=''.join(random.choices(string.ascii_letters+string.digits,k=16))
        AndroidID=f'android-{a1}'
        a2=''.join(random.choices(string.digits,k=3))
        useragent=f'Instagram 262.0.0.24.327 Android (28/9; 240dpi; 720x1280; google; G{a2}A; G{a2}A; intel; en_US; 426482113)'
        headers = {
            'Host': 'i.instagram.com',
            'X-Ig-App-Locale': 'en_US',
            'X-Ig-Device-Locale': 'en_US',
            'X-Ig-Mapped-Locale': 'en_US',
            'X-Pigeon-Session-Id': str(PigeonSession),
            'X-Pigeon-Rawclienttime': str(time.time()),
            'X-Ig-Bandwidth-Speed-Kbps': '-1.000',
            'X-Ig-Bandwidth-Totalbytes-B': '0',
            'X-Ig-Bandwidth-Totaltime-Ms': '0',
            'X-Bloks-Version-Id': 'bcc515ffbd24010cd9d89d4856ae93562377ebc5ff84a57335ea2756265f5e70',
            'X-Ig-Www-Claim': '0',
            'X-Bloks-Is-Layout-Rtl': 'false',
            'X-Ig-Device-Id':str(IgDeviceId),
            'X-Ig-Family-Device-Id': str(IgFamilyDeviceId),
            'X-Ig-Android-Id': str(AndroidID),
            'X-Ig-Timezone-Offset': '28800',
            'X-Fb-Connection-Type': 'WIFI',
            'X-Ig-Connection-Type': 'WIFI',
            'X-Ig-Capabilities': '3brTv10=',
            'X-Ig-App-Id': '567067343352427',
            'Priority': 'u=3',
            'User-Agent': str(useragent),
            'Accept-Language': 'en-US',
            'X-Mid': str(mid),
            'Ig-Intended-User-Id': '0',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Fb-Http-Engine': 'Liger',
            'X-Fb-Client-Ip': 'True',
            'X-Fb-Server-Cluster': 'True',
        }
        data = {
            'signed_body': 'SIGNATURE.{"jazoest":"22385","country_codes":"[{\\"country_code\\":\\"1\\",\\"source\\":[\\"default\\"]},{\\"country_code\\":\\"91\\",\\"source\\":[\\"sim\\"]}]","phone_id":"'+str(IgFamilyDeviceId)+'","enc_password":"#PWD_INSTAGRAM:0:'+str(round(time.time()))+':'+str(Password)+'","username":"'+str(User)+'","adid":"'+str(uuid.uuid4())+'","guid":"'+str(IgDeviceId)+'","device_id":"'+str(AndroidID)+'","google_tokens":"[]","login_attempt_count":"0"}',
        }
        response = requests.post('https://i.instagram.com/api/v1/accounts/login/', headers=headers, data=data)
        value = {
            "Response": response,
            "Mid": mid,
            'PigeonSession': PigeonSession,
            "IgDeviceId": IgDeviceId,
            "IgFamilyDeviceId": IgFamilyDeviceId,
            "AndroidID": AndroidID,
            'UserAgent': useragent
        }
        return value


