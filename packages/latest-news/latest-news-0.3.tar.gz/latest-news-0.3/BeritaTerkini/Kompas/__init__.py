import requests as requests
from bs4 import BeautifulSoup


def isi():

    try:
        link = requests.get('https://www.kompas.com/')



    except Exception:
        return Exception

    if link.status_code == 200:
        package = BeautifulSoup(link.text,'html.parser')
        DataPackage = package.find('div',{'class':'ga--latest'})

        DataPackage = DataPackage.findChildren('h3')

        i=0;
        data1 = None
        data2 = None
        data3 = None
        data4 = None

        for dataS in DataPackage:

            if i == 1:
                data1 = dataS.text
            elif i == 2:
                data2 = dataS.text
            elif i == 3:
                data3 = dataS.text
            elif i == 4:
                data4 = dataS.text
            i = i +1





        data = dict()
        data['data1'] = data1
        data['data2'] = data2
        data['data3'] = data3
        data['data4'] = data4
        return data



def wadah(data):
    print(f'Berita bahwa {data["data1"]}')
    print(f'Dan mengenai peristiwa bahwa {data["data2"]}')
    print(f'Adapun juga  berita tentang {data["data3"]}')
    print(f'Dan dilanjutkan dengan  {data["data4"]}')


if __name__ == '__main__':
    data = isi()
    wadah(data)
