from suds.client import Client
# The service URL
soap_url = 'http://myapp.example.notreal/path/to/soap'
# The WSDL URL, we wont' use this but just illustrating for example. This 
# would be the file you download to your system and save as wsdl_file
wsdl_url = 'http://myapp.example.notreal/path/to/soap?wsdl' 
# The full path to the downloaded WSDL file on your local system
wsdl_file = '/path/to/myapp.wsdl'
wsdl_url = 'file://' + wsdl_file # Override original wsdl_url

client = Client(url=wsdl_url, location=soap_url)
#client = Client(wsdl_url)

# shows the details of this service
print client

result = client.service.GetWeatherInformation() 
print result
