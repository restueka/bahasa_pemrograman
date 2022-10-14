#variabel
a = "Restu Eka Putri"
def func():
    a = "datang"
    print ("selamat "+ a)
func()
print (a)

#definisi
def tambah():
    a = 10
    b= 5
    c= a+b
    print (c)

tambah()

#parameter
def data(nama,nim):
    print(f"nama saya {nama} dan nim {nim}")
data ("Restu Eka Putri","20210801042")

#contoh
def total(sisi):
    return sisi*sisi


def segitiga(alas,tinggi):
    return 0.5*alas*tinggi