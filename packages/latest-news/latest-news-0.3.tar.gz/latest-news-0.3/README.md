# Latest News Indonesia
This package contains the latest news from various official Indonesian websites

## HOW IT WORK?
This package will be taken from the [Official Indonesian Website] (https://www.cnnindonesia.com/) and (https://www.kompas.com) to find out the latest news happening in Indonesia.

This package will use BeautifulSoup4 and Request, to produce output in the form of JSON ready for use in web or mobile applications
## HOW TO USE
```
import BeritaTerkini.CNN
import BeritaTerkini.Kompas


if __name__ == '__main__':
    print('Sumber Berita : https://www.kompas.com/')
    data = BeritaTerkini.CNN.isi()
    BeritaTerkini.CNN.wadah(data)
    print('Sumber Berita : https://www.cnnindonesia.com/')
    data = BeritaTerkini.Kompas.isi()
    BeritaTerkini.Kompas.wadah(data)

```

# Author
Rafi Ramdhani