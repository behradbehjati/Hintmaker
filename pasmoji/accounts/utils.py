import requests
import json
def get_url_image(my_url):


    url = "https://www.klazify.com/api/domain_logo?url="+my_url

    payload = {}
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNWY5ZTRlNDMyMmI5ODMxMDE4ZTJjMDAzMmU0NGY5ZTMxZWE1YmRiNmQzZjA5MDdmNDVmZWM4ZjY3ZTc1MTBjOGU2NzA4MmMzNGNiMWZmYjUiLCJpYXQiOjE2NzY1NTI1NTUsIm5iZiI6MTY3NjU1MjU1NSwiZXhwIjoxNzA4MDg4NTU1LCJzdWIiOiIxMDA5MyIsInNjb3BlcyI6W119.FqrpC0N2ykS_uBeKIQP3YIjQEZoGn62z2sLBq-zdgq3vLWGykCVFNfPKkarrF_D_JeSr9gXV7mQ5L8NetbhwLQ',
        'Cookie': 'XSRF-TOKEN=eyJpdiI6Imo1aGtSdnYyc1hrekREQjdBeWozbWc9PSIsInZhbHVlIjoiWGc4S24xRTBSRDgvT0tqTG5hNlg2UFJKbk1rWGI3cVNCTWRsZm9nQnRwQWFSbitMVkJHZkdCUlNmTjh5YWppeTdPcGZENVV3RlA2M0FSaW1ZNmxHSldiSGt2cWtYb3JIR1BjWlllS0RvVTV5dUNabzkya0JTMWh3QzNhSUErU2oiLCJtYWMiOiI2Mjk4MDNlNzZlZTA2NmJmNjRiZTg5MzdlMjllNDM5N2ZmZTU0Y2VkMTE2ZmMwYmJjMDBhYTVmNjA3MzE3YzcyIn0%3D; klazify_session=eyJpdiI6ImMraFJidE5VRFRCNFBOVk9kbW1uYXc9PSIsInZhbHVlIjoiWG9BQkE5SUJEQ0dlTzRYb1NXRzVUUC9lTlRHQ0I1YmF6WHZvWGNpZ1ZmbmF2YVVSeUI4KzE5b3RORXVhRXQ0NUtkQVpkT1RtN2hhbU5YdXI4RGFKYmN6QjNLb01oQzZrNEFDL1RZc2MzR28xNlVXUmdOYTkreFVzcDRSYi9XR3UiLCJtYWMiOiJiNTg2ZDM4NTcxZGM4NTIxNTM2ODllYjI5NGFjZDA3ZmU5Mjg2OGY3N2JkYTZiYjNiZWE0ZmZhODM0MjEzMDgwIn0%3D'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    text=json.loads(response.text)
    print(text)