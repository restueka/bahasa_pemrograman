# Rangkuman Modul Sesi 4
Penyeleksian if adalah pernyataan penyeleksian yang mencari kebenaran dari conditional
expression yang disebutkan. conditional expression harus berupa bilangan Boolean atau operasi yang menghasilkan bilangan Boolean dan menyatakan benar atau salah atas expression tersebut. Ketika mesin eksekusi bertemu dengan penyeleksian if maka CPU akan memeriksa kebenaran
dari conditional expression yang disebutkan, jika benar (true) maka perintah yang ada di dalamnya akan dijalankan, jika salah (false) maka akan memeriksa pernyataan else if (jika ada), hal itu dilakukan berulang satu demi satu hingga menemukan kondisi yang bernilai benar (true). Jika tidak ditemukan maka akan melakukan perintah pernyataan else. 
Nested IF merupakan hal yang dimungkinkan dalam bahasa pemrograman C++ yaitu membuat
pernyataan IF di dalam pernyataan IF. hal ini dapat memungkinkan anda untuk membuat
tahapan penyeleksian yang berlipat-lipat. Contoh Program :
Pengantar Operasi Penyeleksian 
* Pernyataan percabangan digunakan untuk memecahkan persoalan untuk mengambil suatu keputusan diantara sekian pernyataan yang ada. 
* Dalam bahasa C++ terdapat beberapa perintah, diantaranya adalah :
* Pernyataan IF 
* Pernyataan IF – ELSE
* Pernyataan NESTED IF 
* Pernyataan IF – ELSE Majemuk 
* Pernyataan SWITCH - CASE 
Pernyataan IF (lanjutan) 
Cara Pendeklarasian : 
* Penulisan kondisi harus dalam tanda kurung dan berupa ekspresi relasi dan penulisan pernyataan dapat berupa sebuah pernyataan tunggal, pernyataan majemuk atau pernyataan kosong.
* Jika pernyataan IF diikuti dengan pernyataan majemuk, bentuk penulisan sebagai berikut.
Pernyataan IF – ELSE Majemuk (lanjutan)
* PerSwitch – case merupakan pernyataan yang dirancang khusus untuk menangani pengambilan keputusan yang melibatkan sejumlah atau banyak alternative. 
* Pernyataan switch – case memiliki kegunaan yang sama seperti if-else bertingkat, tetapi penggunaannya untuk memeriksa data yang bertipe karakter atau integer
* PERBEDAAN IF DAN SWITCH
Flow control (struktur kendali) dapat dibagi menjadi dua jenis yaitu , Struktur percabangan dan pengulangan (looping). Namun kali ini akan membahas struktus percabangan. Percabangan adalah perintah yang memungkinkan pemilihan atas perintah yang akan dijalankan sesuai dengan kondisi tertentu yang menentukan alur perjalanan program.
Ada tiga macam perintah percabangan, yaitu if, if … else, dan switch :
 1. IF If digunakan untuk satu kondisi saja. Jika pernyataan benar (terpenuhi) maka akan dijalankan, jika salah (tidak terpenuhi) maka diabaikan. 
2. IF … ELSE Perintah ini digunakan untuk lebih dari satu kondisi. Seperti biasa, perintah1 dan perintah2 bisa berbentuk blok yang terdiri dari beberapa perintah. Pernyataan if merupakan bentuk percabangan 2 arah, jika kondisi yang diuji tersebut terpenuhi, maka program akan menjalankan pernyataan-pernyataan tertentu.
3. SWITCH Perintah ini digunakan sebagai alternatif pengganti dari sintaks if … else dengan else lebih dari satu. Switch, kondisi hanya dinyatakan dengan bilangan bulat atau karakter/string. Dengan perintah ini program percabangan akan semakin mudah dibuat dan dipelajari. Perintah switch akan menyeleksi kondisi yang diberikan dan kemudian membandingkan hasilnya dengan konstanta-konstanta yang berada di case.
i IF ELSE IF adalah sebuah struktur logika program yang di dapat dengan cara menyambung beberapa kondisi IF ELSE menjadi sebuah kesatuan. Jika kondisi pertama tidak terpenuhi atau bernilai false, maka kode program akan lanjut ke kondisi IF di bawahnya. Jika ternyata tidak juga terpenuhi, akan lanjut lagi ke kondisi IF di bawahnya, dst hingga blok ELSE terakhir atau terdapat kondisi IF yang bernilai true.