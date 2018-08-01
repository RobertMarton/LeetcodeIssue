import requests
import json

class Solution(object):
    def GetSummarizebyUrl(self,url):
        Api = r'http://bing-blink.azurewebsites.net/api/blink/summary?url='
        tar = Api+url
        print tar
        source = requests.get(tar)
        print 'source:',source
        print 'data:',source.text
        tmp = source.text
        index = tmp.find(',"Data":')
        endex = tmp.find(',"TimeStamp"')
        data = tmp[index+8:endex]
        print 'data--0:',data
        data = json.loads(data)
        print 'dataByjson:',data
        return data[0]['Text']

tmp = Solution()
url = r'http://techcrunch.com/2015/08/13/the-galaxy-s6-edge-is-samsungs-answer-to-the-iphone-6-plus/'
res = tmp.GetSummarizebyUrl(url)
print 'FinalExtractSummary:',res
