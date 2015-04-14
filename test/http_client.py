from poster.encode import *
from poster.streaminghttp import register_openers
import urllib2

url="http://localhost:80/upload_image"

res ='this is content of a file'
parmLst =[('field1','value1'), ('field2','value2')]
register_openers()
parmLst.append(MultipartParam("file", value=res, filename=None, filetype='application/octet-stream'))
datagen, headers = multipart_encode(parmLst)
request = urllib2.Request(url, datagen, headers)
print urllib2.urlopen(request).read()

