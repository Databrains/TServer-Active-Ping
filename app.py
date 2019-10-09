import requests
from xml.etree import ElementTree
from pprint import  pprint as pp
from datetime import datetime

def getServerName(ip):
    if ip == '172-31-43-129':
        serverName = 'DBI-APP01'
    elif ip == '172-31-24-246':
        serverName = 'DBI-DEM01'
    elif ip =='172-31-29-204':
        serverName = 'HMS-APP01'
    elif ip == '172-31-70-76':
        serverName = 'HMS-APP02'
    elif ip == '172-31-53-122':
        serverName = 'PDR-APP01'
    elif ip == '10-57-1-6':
        serverName = 'Touro APP'
    elif ip =='172-31-8-43':
        serverName = 'DBI-APP03'
    return serverName

servers = ['http://52.7.220.189/admin/systeminfo.xml']



for server in servers:

    r = requests.get(server)
    print(r.status_code)
    if r.status_code == 200:
        timeStamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        tree = ElementTree.fromstring(r.content)

        for leaf in tree.iter('machine'):
            # print(leaf.attrib)
            for x in leaf.iter():
                # print(x.tag, x.attrib)
                tag = x.tag
                attr = x.attrib
                # print(attr)
                try:
                    time = timeStamp
                    ip = attr['worker']
                    serverName = getServerName(str(ip).split(':')[0].replace('ip-',''))
                    status = attr['status']
                    print([{'server': serverName, 'ip': ip, 'time': time, 'process': tag, 'status': status}])
                except KeyError:
                    continue

