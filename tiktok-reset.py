import requests

def reset_tiktok_password(email):
    url = 'https://api16-normal-c-alisg.tiktokv.com/passport/email/send_code/?residence=JO&device_id=7002851779940271622&os_version=14.6&app_id=1233&iid=7090067468483643138&app_name=musical_ly&vendor_id=A0E47A34-1BAE-4407-AB86-219468E804C5&locale=ar&ac=WIFI&sys_region=JO&ssmix=a&version_code=17.6.1&vid=A0E47A34-1BAE-4407-AB86-219468E804C5&channel=App%20Store&op_region=JO&os_api=18&idfa=00000000-0000-0000-0000-000000000000&install_id=7090067468483643138&idfv=A0E47A34-1BAE-4407-AB86-219468E804C5&device_platform=iphone&device_type=iPhone11%2C2&openudid=62b064ef098f5d1c5817b2bf68f0ce3be9a52dcf&account_region=&tz_name=Asia%2FAmman&tz_offset=10800&app_language=ar&carrier_region=JO&current_region=JO&aid=1233&mcc_mnc=41601&screen_width=1125&uoo=1&content_language=&language=ar&cdid=C3303766-D942-4770-B538-DADCC78137C4&build_number=176111&app_version=17.6.1&resolution=1125%2A2436'

    headers = {
        "Host": "api16-normal-c-alisg.tiktokv.com",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "TikTok 17.6.1 rv:176111 (iPhone; iOS 14.6; ar_JO@numbers=latn) Cronet",
    }

    data = f"account_sdk_source=app&email={email}&mix_mode=1&type=31"

    response = requests.post(url, headers=headers, data=data)
    return response.text


print("Enter Tiktok Email :")
email = input("> ")

print("\nSending reset code request...")
result = reset_tiktok_password(email)

print("\n--- Response ---")
print(result)
