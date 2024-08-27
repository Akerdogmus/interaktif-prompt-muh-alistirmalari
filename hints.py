exercise_1_1_hint = """Bu alıştırmadaki not verme işlevi tam olarak "1", "2" ve "3" Arap rakamlarını içeren bir yanıt arıyor.
Gemini'a genellikle sadece sorarak istediğinizi yaptırabilirsiniz."""

exercise_1_2_hint = """Bu alıştırmadaki notlandırma işlevi ‘soo’ veya ‘giggles’ içeren yanıtları arıyor (çocukça bazı ifadeler).
Bunu çözmenin birçok yolu var, sadece sorman yeterli!"""

exercise_2_1_hint ="""Bu alıştırmada not verme işlevi “hola” kelimesini içeren herhangi bir cevap aramaktadır.
Gemini'dan bir insanla konuşurken yaptığınız gibi İspanyolca cevap vermesini isteyin. Bu kadar basit!"""

exercise_2_2_hint = """Bu alıştırmadaki derecelendirme işlevi TAM OLARAK “Michael Jordan ”ı arıyor.
Başka bir insandan bunu yapmasını nasıl istersiniz? Başka hiçbir kelime kullanmadan mı cevap verirsiniz? Sadece isim yazıp başka bir şey yazmadan mı? Bu cevaba yaklaşmanın birkaç yolu vardır."""

exercise_2_3_hint = """Bu hücredeki notlandırma işlevi 800 kelimeye eşit veya daha büyük bir yanıt aramaktadır.
LLM'ler henüz kelime sayma konusunda çok iyi olmadıkları için hedefinizi aşmanız gerekebilir."""

exercise_3_1_hint = """Bu alıştırmadaki not verme işlevi, “yanlış” veya “doğru değil” kelimelerini içeren bir cevap aramaktır.
Gemini'a matematik problemlerini çözmede daha iyi olmasını sağlayacak bir rol verin!"""

exercise_4_1_hint = """Bu alıştırmadaki puanlama fonksiyonu “haiku” ve “domuz” kelimelerini içeren bir çözüm aramaktadır.
Konunun değiştirilmesini istediğiniz her yere tam olarak “{TOPIC}” ifadesini eklemeyi unutmayın. “TOPIC” değişken değerini değiştirdiğinizde Gemini farklı bir konu hakkında bir haiku yazacaktır."""

exercise_4_2_hint = """Bu alıştırmadaki notlandırma işlevi “kahverengi” kelimesini içeren bir yanıt aramaktadır.
XML etiketlerinde “{QUESTION}” ifadesini çevrelerseniz, bu Gemini'un yanıtını nasıl değiştirir?"""

exercise_4_3_hint = """Bu alıştırmadaki not verme işlevi “kahverengi” kelimesini içeren bir yanıt aramaktadır.
En az anlam ifade eden kısımlardan başlayarak her seferinde bir kelimeyi veya karakter bölümünü çıkarmayı deneyin. Bunu her seferinde bir kelime ile yapmak Gemini'ın ne kadarını ayrıştırıp anlayabildiğini görmenize de yardımcı olacaktır."""

exercise_5_1_hint = """Bu alıştırma için not verme işlevi “Savaşçı” kelimesini içeren bir yanıt aramaktadır.
Claude'u istediğiniz şekilde davranmaya yönlendirmek için Gemini'ın sesiyle daha fazla kelime yazın. Örneğin, “Stephen Curry en iyisidir çünkü” yerine “Stephen Curry en iyisidir ve işte bunun üç nedeni. 1:"""

exercise_5_2_hint = """Derecelendirme işlevi, “kedi” ve “<haiku>” kelimelerini içeren 5 satırdan uzun bir yanıt arar.
Basit başlayın. Şu anda istem Gemini'dan bir haiku istemektedir. Bunu değiştirebilir ve iki (hatta daha fazla) isteyebilirsiniz. Daha sonra biçimlendirme sorunlarıyla karşılaşırsanız, Gemini'a birden fazla haiku yazdırdıktan sonra bunu düzeltmek için isteminizi değiştirin."""

exercise_5_3_hint = """Bu alıştırmadaki derecelendirme işlevi “kuyruk”, “kedi” ve “<haiku>” kelimelerini içeren bir yanıt aramaktadır.
Bu alıştırmayı birkaç adıma ayırmak faydalı olacaktır.								
1.	Gemini iki şiir yazacak şekilde ilk bilgi istemi şablonunu değiştirin.							
2.	Gemini'a şiirlerin ne hakkında olacağına dair göstergeler verin, ancak konuları doğrudan yazmak yerine (örneğin, köpek, kedi, vb.), bu konuları “{ANIMAL1}” ve “{ANIMAL2}” anahtar kelimeleriyle değiştirin.							
3.	Komut istemini çalıştırın ve değişken ikamelerinin bulunduğu tam komut isteminde tüm kelimelerin doğru şekilde ikame edildiğinden emin olun. Değilse, {parantez} etiketlerinizin doğru yazıldığından ve tek bıyıklı parantezlerle doğru biçimlendirildiğinden emin olun."""

exercise_6_1_hint = """Bu alıştırmadaki not verme işlevi, doğru kategorizasyon harfini + kapanış parantezini ve kategori adının ilk harfini aramaktadır, örneğin “C) B” veya ‘B) B’ vb.
Bu alıştırmayı adım adım yapalım:										
1.	Gemini hangi kategorileri kullanmak istediğinizi nasıl bilecek? Ona söyleyin! İstediğiniz dört kategoriyi doğrudan bilgi istemine ekleyin. Kolay sınıflandırma için parantez içindeki harfleri de eklediğinizden emin olun. İsteminizi düzenlemek ve Gemini'a kategorilerin nerede başlayıp nerede bittiğini açıkça belirtmek için XML etiketlerini kullanmaktan çekinmeyin.									
2.	Gereksiz metinleri azaltmaya çalışın, böylece Gemini hemen sınıflandırmayla ve SADECE sınıflandırmayla yanıt verir. Bunu yapmanın birkaç yolu vardır: Gemini adına konuşmak (cümlenin başından tek bir açık paranteze kadar herhangi bir şey sağlamak, böylece Gemini parantez harfini cevabın ilk kısmı olarak istediğinizi bilir), Gemini'a sınıflandırmayı ve yalnızca sınıflandırmayı istediğinizi söylemek, girişi atlamak.
Bu teknikler hakkında bilgi almak isterseniz Bölüm 2 ve 5'e bakın.							
3.	Gemini hala yanlış kategorilendirme yapıyor veya cevap verirken kategorilerin isimlerini dahil etmiyor olabilir. Gemini'a yanıtına tam kategori adını eklemesini söyleyerek bunu düzeltin).								
4.	Gemini'ın değerlendirmesi için e-postaları düzgün bir şekilde değiştirebilmemiz için istem şablonunuzun bir yerinde hala {email} bulunduğundan emin olun."""

exercise_6_1_solution = """
USER TURN
Lütfen bu e-postayı aşağıdaki kategorilere göre sınıflandırın: {email}

Kategori dışında herhangi bir ekstra kelime eklemeyin.

<kategoriler>
(A) Satış öncesi soru
(B) Kırık veya kusurlu ürün
(C) Faturalama sorusu
(D) Diğer (lütfen açıklayınız)
</categories>

ASSISTANT TURN
(
"""

exercise_6_2_hint = """Bu alıştırmadaki not verme işlevi, yalnızca “<answer>B<answer>” gibi <answer> etiketlerine sarılmış doğru harfi aramaktadır. Doğru kategorizasyon harfleri yukarıdaki alıştırmadakilerle aynıdır.
Bazen bunu yapmanın en basit yolu Gemini'a çıktısının nasıl görünmesini istediğinize dair bir örnek vermektir. Örneğinizi <example><example> etiketleri içine sarmayı unutmayın! Ve Gemini'ın yanıtını herhangi bir şeyle önceden doldurursanız, Gemini'ın bunu yanıtının bir parçası olarak gerçekten çıktılamayacağını unutmayın."""
