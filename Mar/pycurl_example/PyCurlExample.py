import pycurl
from io import BytesIO

# curl "http://localhost:8080/npss/mapping" -X POST -H "Content-Type: multipart/form-data" -F "mapping=@mapping.json"  -F "file0=@input0.csv" -F "file1=@input1.csv" -F file3=@input2.csv
c = pycurl.Curl()
c.setopt(pycurl.URL, 'http://localhost:8092/npss/execute')
c.setopt(pycurl.HTTPHEADER, ['Content-Type: multipart/form-data'])
c.setopt(c.POST, 1)

# Get response in buffer
buffer = BytesIO()
c.setopt(c.WRITEDATA, buffer)

files = [('input1', (c.FORM_FILE, 'GP_in.csv')), ('mapping', (c.FORM_FILE, 'contract.json'))]

c.setopt(c.HTTPPOST, files)
c.perform()
body = buffer.getvalue()
f = open("output.zip", "wb")
f.write(body)
print("\nStatus code: " + str(c.getinfo(pycurl.HTTP_CODE)))
c.close()

