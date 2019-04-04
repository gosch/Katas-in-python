import pycurl

# curl "http://localhost:8080/npss/mapping" -X POST -H "Content-Type: multipart/form-data" -F "mapping=@mapping.json"
# -F "file0=@input0.csv" -F "file1=@input1.csv" -F file3=@input2.csv
c = pycurl.Curl()
c.setopt(pycurl.URL, 'http://localhost:8080/npss/mapping')
c.setopt(pycurl.HTTPHEADER, ['Content-Type: multipart/form-data'])
c.setopt(c.POST, 1)

files = [('file0', (c.FORM_FILE, 'input0.csv')), ('file1', (c.FORM_FILE, 'input1.csv')),
         ('file3', (c.FORM_FILE, 'input2.csv')), ('mapping', (c.FORM_FILE, 'mapping.json'))]


c.setopt(c.HTTPPOST, files)
c.perform()
print("\nStatus code: " + str(c.getinfo(pycurl.HTTP_CODE)))
c.close()
