import sys
import codecs
sys.stdout = codecs.getwriter("iso-8859-1")(sys.stdout, 'xmlcharrefreplace')

from pyquery import PyQuery as pq
import urllib2

distritos = ('porto', 'braga', 'lisboa')

site = "https://www.idealista.pt/comprar-casas/portalegre-distrito/pagina-2"

class idealistaPage:

    def __init__(self, link):
        self.link = link

    def getData(self):
        self.d = pq(url=self.link)
        print(self.link)

class idealistaAdList:

    #plataforma  # imovirtual, ...
    #id = # id na plataforma (se aplicavel)
    #link # para o anuncio

    #tipo    # apartamento, moradia, ...

    #preco

    #distrito
    #conselho
    #freguesia

    #topologia   # T1, T1+1
    #area-contrucao
    #area-terreno
    #casas-de-banho

    #fotos[]

    #descricao


    #def __init__(self):
        #self.plataforma = plataforma

    def getData(self, n):
        self.id = d('article:nth-of-type(' +str(n) + ') div').attr('data-adid')
        self.link = 'https://www.idealista.pt' + d('article:nth-of-type(' + str(n) + ') a.item-link').attr('href')

        title = d('article:nth-of-type(' + str(n) + ') a.item-link').text()
        if(title.find(' em ') != -1):
            self.tipo = (title.split(' em ', 1))[0]
            localidade = (title.split(' em ', 1))[1]

            if(localidade.count(",") > 0):
                self.freguesia = (((localidade.split(','))[0]).strip()).lower()
                self.concelho  = (((localidade.split(','))[1]).strip()).lower()
            else:
                self.concelho = localidade

        else:
            self.tipo = (title.split(',', 1))[0]
            morada = (title.split(',', 1))[1]
            self.concelho = ((morada.split(','))[-1].strip()).lower()
            self.freguesia = ((morada.split(','))[-2].strip()).lower()
            self.morada = morada.rsplit(',', 2)[0].strip()


        self.topologia = d('article:nth-of-type(' + str(n) + ') span.item-detail:nth-of-type(1)').text()
        self.area = d('article:nth-of-type(' + str(n) + ') span.item-detail:nth-of-type(2)').text()
        self.telefone = d('article:nth-of-type(' + str(n) + ') span.icon-phone').text()

for distrito in distritos:
    print distrito
    page = 1
    site = "https://www.idealista.pt/comprar-casas/" + distrito + "-distrito/pagina-" + str(page)
    d = pq(url=site)
    print site

    still_ads = True



    while(d('article:nth-of-type(1)').text() != ''):
        site = "https://www.idealista.pt/comprar-casas/" + distrito + "-distrito/pagina-" + str(page)
        print "Page:" + str(page)
        d = pq(url=site)

        nth = 1

        while(d('article:nth-of-type(' + str(nth) + ')').text() != ''):

            if(d('article:nth-of-type(' + str(nth) + ') div').attr('data-adid') == None):
                nth = nth + 1
                print "jump"
                continue

            ad1 = idealistaAdList()
            ad1.getData(nth)

            print(str(nth) + ":")

            print ad1.id
            print ad1.tipo
            #print ad1.freguesia
            print ad1.concelho
            print ad1.topologia
            print ad1.link
            #print ad1.morada
            print '\n\n'
            nth = nth + 1

        page = page + 1

#    page1 = idealistaPage('https://www.google.com')
#    page1.getData()
