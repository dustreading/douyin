import json
import requests

def crawl(url):
    lua = '''
            function main(splash)
                splash:set_user_agent('Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36')
                splash:go('{}')
                splash:wait(0.5)
                return splash:html()
            end
            '''.format(url)
    splash_url = 'http://47.106.120.64:8050/execute?proxy=http://H5S5EP77ISZGR1DC:78DADE9861B2BD42@http-cla.abuyun.com:9030'
    headers = {'content-type': 'application/json'}
    data = json.dumps({'lua_source': lua})
    response = requests.post(splash_url, headers=headers, data=data)
    return response

if __name__ == '__main__':
    print(crawl('https://www.iesdouyin.com/share/user/2613650662'))