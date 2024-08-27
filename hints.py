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

exercise_7_1_hint = """You're going to have to write some example emails and classify them for Claude (with the exact formatting you want). There are multiple ways to do this. Here are some guidelines below.										
1.	Try to have at least two example emails. Claude doesn't need an example for all categories, and the examples don't have to be long. It's more helpful to have examples for whatever you think the trickier categories are (which you were asked to think about at the bottom of Chapter 6 Exercise 1). XML tags will help you separate out your examples from the rest of your prompt, although it's unnecessary.									
2.	Make sure your example answer formatting is exactly the format you want Claude to use, so Claude can emulate the format as well. This format should make it so that Claude's answer ends in the letter of the category. Wherever you put the {email} placeholder, make sure that it's formatted exactly like your example emails.									
3.	Make sure you still have the categories listed within the prompt itself, otherwise Claude won't know what categories to reference, as well as {email} as a placeholder for substitution."""

exercise_7_1_solution = """
USER TURN
Please classify emails into the following categories, and do not include explanations: 
<categories>
(A) Pre-sale question
(B) Broken or defective item
(C) Billing question
(D) Other (please explain)
</categories>

Here are a few examples of correct answer formatting:
<examples>
Q: How much does it cost to buy a Mixmaster4000?
A: The correct category is: A

Q: My Mixmaster won't turn on.
A: The correct category is: B

Q: Please remove me from your mailing list.
A: The correct category is: D
</examples>

Here is the email for you to categorize: {email}

ASSISTANT TURN
The correct category is:
"""
exercise_8_1_hint = """The grading function in this exercise is looking for a response that contains the phrase "I do not", "I don't", or "Unfortunately".
What should Claude do if it doesn't know the answer?"""

exercise_8_2_hint = """The grading function in this exercise is looking for a response that contains the phrase "49-fold".
Make Claude show its work and thought process first by extracting relevant quotes and seeing whether or not the quotes provide sufficient evidence. Refer back to the Chapter 8 Lesson if you want a refresher."""

exercise_9_1_solution = """
You are a master tax acountant. Your task is to answer user questions using any provided reference documentation.

Here is the material you should use to answer the user's question:
<docs>
{TAX_CODE}
</docs>

Here is an example of how to respond:
<example>
<question>
What defines a "qualified" employee?
</question>
<answer>
<quotes>For purposes of this subsection—
(A)In general
The term "qualified employee" means any individual who—
(i)is not an excluded employee, and
(ii)agrees in the election made under this subsection to meet such requirements as are determined by the Secretary to be necessary to ensure that the withholding requirements of the corporation under chapter 24 with respect to the qualified stock are met.</quotes>

<answer>According to the provided documentation, a "qualified employee" is defined as an individual who:

1. Is not an "excluded employee" as defined in the documentation.
2. Agrees to meet the requirements determined by the Secretary to ensure the corporation's withholding requirements under Chapter 24 are met with respect to the qualified stock.</answer>
</example>

First, gather quotes in <quotes></quotes> tags that are relevant to answering the user's question. If there are no quotes, write "no relevant quotes found".

Then insert two paragraph breaks before answering the user question within <answer></answer> tags. Only answer the user's question if you are confident that the quotes in <quotes></quotes> tags support your answer. If not, tell the user that you unfortunately do not have enough information to answer the user's question.

Here is the user question: {QUESTION}
"""

exercise_9_2_solution = """
You are Codebot, a helpful AI assistant who finds issues with code and suggests possible improvements.

Act as a Socratic tutor who helps the user learn.

You will be given some code from a user. Please do the following:
1. Identify any issues in the code. Put each issue inside separate <issues> tags.
2. Invite the user to write a revised version of the code to fix the issue.

Here's an example:

<example>
<code>
def calculate_circle_area(radius):
    return (3.14 * radius) ** 2
</code>
<issues>
<issue>
3.14 is being squared when it's actually only the radius that should be squared>
</issue>
<response>
That's almost right, but there's an issue related to order of operations. It may help to write out the formula for a circle and then look closely at the parentheses in your code.
</response>
</example>

Here is the code you are to analyze:

<code>
{CODE}
</code>

Find the relevant issues and write the Socratic tutor-style response. Do not give the user too much help! Instead, just give them guidance so they can find the correct solution themselves.

Put each issue in <issue> tags and put your final response in <response> tags.
"""

exercise_10_2_1_solution = """system_prompt = system_prompt_tools_general_explanation + \"""Here are the functions available in JSONSchema format:

<tools>

<tool_description>
<tool_name>get_user</tool_name>
<description>
Retrieves a user from the database by their user ID.
</description>
<parameters>
<parameter>
<name>user_id</name>
<type>int</type>
<description>The ID of the user to retrieve.</description>
</parameter>
</parameters>
</tool_description>

<tool_description>
<tool_name>get_product</tool_name>
<description>
Retrieves a product from the database by its product ID.
</description>
<parameters>
<parameter>
<name>product_id</name>
<type>int</type>
<description>The ID of the product to retrieve.</description>
</parameter>
</parameters>
</tool_description>

<tool_description>
<tool_name>add_user</tool_name>
<description>
Adds a new user to the database.
</description>
<parameters>
<parameter>
<name>name</name>
<type>str</type>
<description>The name of the user.</description>
</parameter>
<parameter>
<name>email</name>
<type>str</type>
<description>The email address of the user.</description>
</parameter>
</parameters>
</tool_description>

<tool_description>
<tool_name>add_product</tool_name>
<description>
Adds a new product to the database.
</description>
<parameters>
<parameter>
<name>name</name>
<type>str</type>
<description>The name of the product.</description>
</parameter>
<parameter>
<name>price</name>
<type>float</type>
<description>The price of the product.</description>
</parameter>
</parameters>
</tool_description>

</tools>
"""