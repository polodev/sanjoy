"""English 101 — গল্পে গল্পে ইংরেজি. Ten days; each day = one short story about Sanjoy, 10 words, 20 sentences,
one grammar tip and a quiz. Data only: engine.py turns it into slides.

Format of the text blocks: one item per line, cells separated by ' | '.
story / sentences: English | Bangla          words: English | Bangla pronunciation | Bangla meaning
"""
from engine import parse_pairs

COURSE = dict(slug="101", lang="english", title="English 101", tag="গল্পে গল্পে ইংরেজি",
              sub="প্রতিটি Day-তে একটা ছোট গল্প, ১০টি শব্দ আর ২০টি বাক্য",
              lead="সঞ্জয়ের জীবনের গল্প পড়তে পড়তে ইংরেজি শিখুন — সহজ শব্দ, রোজকার বাক্য, শুনে শুনে।")

DAYS = []


def day(n, en_title, bn_title, intro, story, words, sentences, grammar):
    DAYS.append(dict(
        n=n, en=en_title, bn=bn_title, intro=intro,
        story=parse_pairs(story), words=parse_pairs(words, 3), sentences=parse_pairs(sentences), grammar=grammar))


# ======================================================================= Day 1
day(1, "Hello, I am Sanjoy", "পরিচয়", "আজ সঞ্জয়ের সাথে পরিচয় হবে — নিজের পরিচয় দিতে আর অন্যের পরিচয় জানতে শিখব।",
"""
Hello! My name is Sanjoy. | হ্যালো! আমার নাম সঞ্জয়।
I am from Bangladesh. | আমি বাংলাদেশ থেকে এসেছি।
I live in Dhaka. | আমি ঢাকায় থাকি।
I am a student. | আমি একজন ছাত্র।
This is my friend, Rahim. | ইনি আমার বন্ধু, রহিম।
Rahim, this is Nusrat. | রহিম, ইনি নুসরাত।
Nice to meet you! | আপনার সাথে দেখা হয়ে ভালো লাগল!
How are you? I am fine, thank you. | আপনি কেমন আছেন? আমি ভালো আছি, ধন্যবাদ।
""",
"""
hello | হ্যালো | হ্যালো, নমস্কার
name | নেইম | নাম
friend | ফ্রেন্ড | বন্ধু
student | স্টুডেন্ট | ছাত্র
fine | ফাইন | ভালো, সুস্থ
thank you | থ্যাংক ইউ | ধন্যবাদ
please | প্লিজ | দয়া করে
sorry | সরি | দুঃখিত
yes | ইয়েস | হ্যাঁ
no | নো | না
""",
"""
Hello, how are you? | হ্যালো, আপনি কেমন আছেন?
I am fine, thank you. | আমি ভালো আছি, ধন্যবাদ।
And you? | আর আপনি?
My name is Sanjoy. | আমার নাম সঞ্জয়।
What is your name? | আপনার নাম কী?
I am from Bangladesh. | আমি বাংলাদেশ থেকে।
Where are you from? | আপনি কোথা থেকে এসেছেন?
I live in Dhaka. | আমি ঢাকায় থাকি।
I am a student. | আমি একজন ছাত্র।
Are you a student? | আপনি কি ছাত্র?
Yes, I am. | হ্যাঁ, আমি।
No, I am not. | না, আমি না।
This is my friend. | ইনি আমার বন্ধু।
Nice to meet you. | আপনার সাথে দেখা হয়ে ভালো লাগল।
Nice to meet you, too. | আপনার সাথেও দেখা হয়ে ভালো লাগল।
Good morning. | শুভ সকাল।
Good night. | শুভ রাত্রি।
Thank you very much. | অনেক ধন্যবাদ।
Sorry, I am late. | দুঃখিত, আমার দেরি হয়েছে।
Please sit down. | দয়া করে বসুন।
""",
dict(title="am, is, are — “হওয়া” ক্রিয়া",
     points=["<b>I am</b> — আমি (<b>I'm</b> সংক্ষেপে)", "<b>You are</b> — তুমি/আপনি/তোমরা", "<b>He / She / It is</b> — সে, এটা",
             "<b>We / They are</b> — আমরা, তারা"],
     table=[("I", "am", "I am a student."), ("You", "are", "You are my friend."), ("She", "is", "She is Nusrat.")],
     quiz=("She ___ a student.", ["am", "is", "are"], 1, "She-এর সাথে is বসে।")))

# ======================================================================= Day 2
day(2, "My Family", "আমার পরিবার", "আজ নিজের পরিবারের কথা বলতে শিখব — বাবা, মা, ভাই, বোন।",
"""
I have a small family. | আমার একটি ছোট পরিবার আছে।
This is my father. He is a teacher. | ইনি আমার বাবা। তিনি একজন শিক্ষক।
This is my mother. She cooks very well. | ইনি আমার মা। তিনি খুব ভালো রান্না করেন।
I have one brother and one sister. | আমার এক ভাই আর এক বোন আছে।
My brother is tall. | আমার ভাই লম্বা।
My sister is young. | আমার বোন ছোট।
We live together. | আমরা একসাথে থাকি।
I love my family. | আমি আমার পরিবারকে ভালোবাসি।
""",
"""
family | ফ্যামিলি | পরিবার
father | ফাদার | বাবা
mother | মাদার | মা
brother | ব্রাদার | ভাই
sister | সিস্টার | বোন
grandfather | গ্র্যান্ডফাদার | দাদা, নানা
grandmother | গ্র্যান্ডমাদার | দাদি, নানি
son | সান | ছেলে
daughter | ডটার | মেয়ে
love | লাভ | ভালোবাসা
""",
"""
This is my father. | ইনি আমার বাবা।
This is my mother. | ইনি আমার মা।
I have a brother. | আমার একটি ভাই আছে।
I have two sisters. | আমার দুইটি বোন আছে।
Do you have a brother? | আপনার কি ভাই আছে?
Yes, I have one brother. | হ্যাঁ, আমার একটি ভাই আছে।
No, I don't have a sister. | না, আমার কোনো বোন নেই।
My father is a teacher. | আমার বাবা একজন শিক্ষক।
My mother is at home. | আমার মা বাড়িতে আছেন।
How many people are in your family? | আপনার পরিবারে কতজন মানুষ?
There are five people in my family. | আমার পরিবারে পাঁচজন মানুষ।
My grandfather is old. | আমার দাদা বয়স্ক।
My grandmother makes tea. | আমার দাদি চা বানান।
He is my son. | সে আমার ছেলে।
She is my daughter. | সে আমার মেয়ে।
I love my mother. | আমি আমার মাকে ভালোবাসি।
We eat dinner together. | আমরা একসাথে রাতের খাবার খাই।
My brother is tall. | আমার ভাই লম্বা।
My sister is very kind. | আমার বোন খুব দয়ালু।
Our family is happy. | আমাদের পরিবার সুখী।
""",
dict(title="have / has — “আছে”",
     points=["<b>I / You / We / They have</b>", "<b>He / She / It has</b> — তৃতীয় ব্যক্তিতে has", "না বোঝাতে: <b>don't have</b> (সে হলে <b>doesn't have</b>)"],
     table=[("I", "have", "I have a brother."), ("She", "has", "She has a sister."), ("They", "have", "They have a car.")],
     quiz=("My sister ___ a pen.", ["have", "has", "having"], 1, "My sister = She, তাই has।")))

# ======================================================================= Day 3
day(3, "My Morning", "আমার সকাল", "আজ সকালের রুটিন বলতে শিখব — ঘুম থেকে ওঠা, নাস্তা, বের হওয়া।",
"""
I wake up at six o'clock. | আমি ছয়টায় ঘুম থেকে উঠি।
I brush my teeth and wash my face. | আমি দাঁত মাজি আর মুখ ধুই।
Then I take a shower. | তারপর আমি গোসল করি।
I have breakfast at seven. | আমি সাতটায় সকালের নাস্তা খাই।
I eat paratha and egg. | আমি পরোটা আর ডিম খাই।
I drink a cup of tea. | আমি এক কাপ চা খাই।
I leave home at eight. | আমি আটটায় বাড়ি থেকে বের হই।
It is a busy morning! | এটা একটা ব্যস্ত সকাল!
""",
"""
morning | মর্নিং | সকাল
wake up | ওয়েক আপ | ঘুম থেকে ওঠা
breakfast | ব্রেকফাস্ট | সকালের নাস্তা
eat | ঈট | খাওয়া
drink | ড্রিংক | পান করা
tea | টি | চা
water | ওয়াটার | পানি
shower | শাওয়ার | গোসল
sleep | স্লিপ | ঘুমানো
time | টাইম | সময়
""",
"""
I wake up at six. | আমি ছয়টায় ঘুম থেকে উঠি।
What time do you wake up? | আপনি কয়টায় ঘুম থেকে ওঠেন?
I take a shower every morning. | আমি প্রতিদিন সকালে গোসল করি।
I brush my teeth. | আমি দাঁত মাজি।
I have breakfast at seven. | আমি সাতটায় নাস্তা করি।
What do you eat for breakfast? | আপনি নাস্তায় কী খান?
I eat bread and eggs. | আমি রুটি আর ডিম খাই।
I drink tea every day. | আমি প্রতিদিন চা খাই।
Do you drink tea or coffee? | আপনি চা খান নাকি কফি?
I drink a glass of water. | আমি এক গ্লাস পানি খাই।
The time is seven o'clock. | এখন সাতটা বাজে।
What time is it? | কয়টা বাজে?
It is half past seven. | সাড়ে সাতটা বাজে।
I am late. | আমার দেরি হয়েছে।
I am not late. | আমার দেরি হয়নি।
I leave home at eight. | আমি আটটায় বাড়ি থেকে বের হই।
My mother wakes up early. | আমার মা সকালে আগে ওঠেন।
He sleeps late. | সে দেরিতে ঘুমায়।
Good morning, Mom! | শুভ সকাল, মা!
Have a nice day! | আপনার দিনটি ভালো কাটুক!
""",
dict(title="Simple Present — রোজকার কাজ",
     points=["নিয়মিত কাজ বোঝাতে verb-এর সাধারণ রূপ: <b>I wake up</b>", "<b>He / She / It</b>-এর সাথে verb-এর শেষে <b>-s</b>: <b>He wakes up</b>",
             "প্রশ্ন: <b>Do you</b> wake up early? (সে হলে <b>Does she</b> ...?)"],
     table=[("I", "eat", "I eat rice."), ("She", "eats", "She eats rice."), ("They", "drink", "They drink tea.")],
     quiz=("She ___ tea every day.", ["drink", "drinks", "drinking"], 1, "She-এর সাথে verb-এ -s যোগ হয়: drinks।")))

# ======================================================================= Day 4
day(4, "At the Market", "বাজারে", "আজ বাজারে গিয়ে দাম জিজ্ঞেস করতে, দরদাম করতে আর কিনতে শিখব।",
"""
Today is Friday. I go to the market. | আজ শুক্রবার। আমি বাজারে যাই।
I want some fruits. | আমি কিছু ফল চাই।
"How much is this mango?" | "এই আমের দাম কত?"
"It is eighty taka per kilo." | "কেজি প্রতি আশি টাকা।"
"That is too expensive!" | "এটা অনেক দামি!"
"Okay, seventy taka." | "ঠিক আছে, সত্তর টাকা।"
I buy two kilos of mangoes. | আমি দুই কেজি আম কিনি।
"Thank you. Here is your money." | "ধন্যবাদ। এই নিন আপনার টাকা।"
""",
"""
market | মার্কেট | বাজার
buy | বাই | কেনা
sell | সেল | বিক্রি করা
money | মানি | টাকা-পয়সা
price | প্রাইস | দাম
cheap | চিপ | সস্তা
expensive | এক্সপেনসিভ | দামি
fruit | ফ্রুট | ফল
mango | ম্যাঙ্গো | আম
kilo | কিলো | কেজি
""",
"""
I go to the market. | আমি বাজারে যাই।
What do you want? | আপনি কী চান?
I want some mangoes. | আমি কিছু আম চাই।
How much is this? | এটার দাম কত?
How much are these bananas? | এই কলাগুলোর দাম কত?
It is fifty taka. | এটা পঞ্চাশ টাকা।
That is too expensive. | এটা অনেক দামি।
This one is cheap. | এটা সস্তা।
Can you give me a discount? | আপনি কি একটু ছাড় দেবেন?
Okay, I will take it. | ঠিক আছে, আমি এটা নেব।
Give me one kilo, please. | আমাকে এক কেজি দিন, প্লিজ।
Two kilos of rice, please. | দুই কেজি চাল দিন, প্লিজ।
Do you have fresh fish? | আপনার কাছে কি তাজা মাছ আছে?
Yes, we have. | হ্যাঁ, আছে।
No, we don't have. | না, নেই।
Here is the money. | এই নিন টাকা।
Do you have change? | আপনার কাছে কি খুচরা আছে?
I buy vegetables every week. | আমি প্রতি সপ্তাহে সবজি কিনি।
The mangoes are sweet. | আমগুলো মিষ্টি।
Thank you, see you again. | ধন্যবাদ, আবার দেখা হবে।
""",
dict(title="How much? বনাম How many?",
     points=["<b>How much</b> — যা গোনা যায় না বা দাম: how much water, how much is this?", "<b>How many</b> — যা গোনা যায়: how many mangoes, how many people?"],
     table=[("How much", "দাম / পরিমাণ", "How much is this?"), ("How many", "সংখ্যা", "How many kilos?")],
     quiz=("___ mangoes do you want?", ["How much", "How many", "How"], 1, "আম গোনা যায়, তাই How many।")))

# ======================================================================= Day 5
day(5, "Food and Tea", "খাবার আর চা", "আজ রেস্টুরেন্টে খাবার অর্ডার করতে আর খাবারের কথা বলতে শিখব।",
"""
It is lunch time. | এখন দুপুরের খাবারের সময়।
Sanjoy and Rahim are hungry. | সঞ্জয় আর রহিম ক্ষুধার্ত।
They go to a small restaurant. | তারা একটি ছোট রেস্টুরেন্টে যায়।
"What would you like?" asks the waiter. | "আপনারা কী নেবেন?" ওয়েটার জিজ্ঞেস করে।
"I would like rice and chicken curry." | "আমি ভাত আর মুরগির তরকারি নেব।"
"I would like fish and dal." | "আমি মাছ আর ডাল নেব।"
After lunch they drink tea. | দুপুরের খাবারের পরে তারা চা খায়।
"The food was delicious!" | "খাবারটা খুব মজার ছিল!"
""",
"""
rice | রাইস | ভাত
fish | ফিশ | মাছ
chicken | চিকেন | মুরগি
vegetable | ভেজিটেবল | সবজি
hungry | হাংগ্রি | ক্ষুধার্ত
delicious | ডেলিশাস | সুস্বাদু
bill | বিল | বিল (খাবারের হিসাব)
lunch | লাঞ্চ | দুপুরের খাবার
dinner | ডিনার | রাতের খাবার
sugar | শুগার | চিনি
""",
"""
I am hungry. | আমি ক্ষুধার্ত।
Are you hungry? | তুমি কি ক্ষুধার্ত?
Let's have lunch. | চলো দুপুরের খাবার খাই।
I would like some rice. | আমি একটু ভাত নেব।
Can I have fish curry, please? | আমি কি মাছের তরকারি পেতে পারি, প্লিজ?
What do you recommend? | আপনি কী সুপারিশ করেন?
I don't like spicy food. | আমি ঝাল খাবার পছন্দ করি না।
The food is delicious. | খাবারটা সুস্বাদু।
It is very spicy. | এটা খুব ঝাল।
A glass of water, please. | এক গ্লাস পানি দিন, প্লিজ।
Tea with milk, please. | দুধ চা দিন, প্লিজ।
One sugar, please. | এক চামচ চিনি দিন, প্লিজ।
I like tea very much. | আমি চা খুব পছন্দ করি।
Do you like coffee? | আপনি কি কফি পছন্দ করেন?
No, I prefer tea. | না, আমি চা বেশি পছন্দ করি।
We eat dinner at nine. | আমরা নয়টায় রাতের খাবার খাই।
The bill, please. | বিলটা দিন, প্লিজ।
How much is the bill? | বিল কত হয়েছে?
This is for you. | এটা আপনার জন্য।
Thank you, it was delicious. | ধন্যবাদ, খুব সুস্বাদু ছিল।
""",
dict(title="I like বনাম I would like",
     points=["<b>I like</b> — আমি পছন্দ করি (সাধারণ কথা): I like tea.", "<b>I would like</b> — আমি চাই/নিতে চাই (ভদ্র অনুরোধ, অর্ডারের সময়): I would like some tea."],
     table=[("I like tea.", "আমি চা পছন্দ করি", "স্বভাব/পছন্দ"), ("I would like tea.", "আমি চা নিতে চাই", "ভদ্রভাবে চাওয়া")],
     quiz=("Waiter: What would you like? You: I ___ like some rice.", ["will", "would", "am"], 1, "ভদ্রভাবে চাইতে would like।")))

# ======================================================================= Day 6
day(6, "On the Road", "রাস্তায়", "আজ রাস্তা জিজ্ঞেস করতে, রিকশা-বাসে যেতে আর দিক বলতে শিখব।",
"""
Sanjoy goes to university by bus. | সঞ্জয় বাসে করে বিশ্ববিদ্যালয়ে যায়।
Today the road is very busy. | আজ রাস্তায় অনেক ভিড়।
There is a lot of traffic. | অনেক যানজট।
"Excuse me, where is the bus stop?" | "মাফ করবেন, বাস স্টপ কোথায়?"
"Go straight, then turn left." | "সোজা যান, তারপর বাঁয়ে ঘুরুন।"
He takes a rickshaw instead. | সে বরং একটা রিকশা নেয়।
"How much to Dhanmondi?" | "ধানমন্ডি পর্যন্ত কত?"
"Fifty taka." "Okay, let's go!" | "পঞ্চাশ টাকা।" "ঠিক আছে, চলুন!"
""",
"""
bus | বাস | বাস
rickshaw | রিকশা | রিকশা
road | রোড | রাস্তা
traffic | ট্রাফিক | যানজট
left | লেফট | বাঁ
right | রাইট | ডান
straight | স্ট্রেইট | সোজা
stop | স্টপ | থামা
walk | ওয়াক | হাঁটা
far | ফার | দূরে
""",
"""
Where are you going? | আপনি কোথায় যাচ্ছেন?
I am going to the university. | আমি বিশ্ববিদ্যালয়ে যাচ্ছি।
I go by bus. | আমি বাসে যাই।
Excuse me, where is the bus stop? | মাফ করবেন, বাস স্টপ কোথায়?
It is near here. | এটা এখানেই কাছে।
It is far from here. | এটা এখান থেকে দূরে।
Go straight. | সোজা যান।
Turn left. | বাঁয়ে ঘুরুন।
Turn right. | ডানে ঘুরুন।
Stop here, please. | এখানে থামুন, প্লিজ।
How much to Dhanmondi? | ধানমন্ডি পর্যন্ত কত?
Please hurry. | দয়া করে তাড়াতাড়ি করুন।
There is a lot of traffic. | অনেক যানজট।
I am stuck in traffic. | আমি যানজটে আটকে আছি।
I walk to the shop. | আমি দোকান পর্যন্ত হেঁটে যাই।
Is this the right bus? | এটা কি ঠিক বাস?
This bus goes to Mirpur. | এই বাস মিরপুর যায়।
Where do I get off? | আমি কোথায় নামব?
I take a rickshaw. | আমি রিকশা নিই।
Be careful! | সাবধান!
""",
dict(title="by, in, at, to — ছোট শব্দ, বড় কাজ",
     points=["<b>by</b> — বাহন: by bus, by rickshaw", "<b>to</b> — গন্তব্যের দিকে: go to school", "<b>at</b> — নির্দিষ্ট সময়/জায়গা: at eight, at the bus stop",
             "<b>in</b> — ভিতরে/শহরে: in Dhaka, in the bus"],
     table=[("by", "বাহন", "by bus"), ("to", "দিকে", "to Mirpur"), ("at", "সময়", "at eight"), ("in", "ভিতরে", "in Dhaka")],
     quiz=("I go ___ bus.", ["on", "by", "at"], 1, "বাহন বোঝাতে by।")))

# ======================================================================= Day 7
day(7, "My Home", "আমার বাড়ি", "আজ ঘরের জিনিসপত্র আর কোনটা কোথায় আছে বলতে শিখব।",
"""
I live in a small flat. | আমি একটা ছোট ফ্ল্যাটে থাকি।
It has two rooms. | এতে দুইটি ঘর আছে।
There is a bed and a table in my room. | আমার ঘরে একটি খাট আর একটি টেবিল আছে।
There is a fan on the ceiling. | ছাদে একটি পাখা আছে।
Books are on the table. | বইগুলো টেবিলের উপর আছে।
My bag is under the bed. | আমার ব্যাগ খাটের নিচে।
The kitchen is next to my room. | রান্নাঘর আমার ঘরের পাশে।
I love my home. | আমি আমার বাড়ি ভালোবাসি।
""",
"""
home | হোম | বাড়ি
room | রুম | ঘর
door | ডোর | দরজা
window | উইন্ডো | জানালা
bed | বেড | খাট, বিছানা
table | টেবিল | টেবিল
chair | চেয়ার | চেয়ার
kitchen | কিচেন | রান্নাঘর
light | লাইট | আলো
fan | ফ্যান | পাখা
""",
"""
This is my house. | এটা আমার বাড়ি।
How many rooms are there? | কয়টি ঘর আছে?
There are two rooms. | দুইটি ঘর আছে।
This is my room. | এটা আমার ঘর।
There is a bed in the room. | ঘরে একটি খাট আছে।
There is a fan on the ceiling. | ছাদে একটি পাখা আছে।
The book is on the table. | বইটি টেবিলের উপর।
The bag is under the bed. | ব্যাগটি খাটের নিচে।
The chair is next to the table. | চেয়ারটি টেবিলের পাশে।
Open the door, please. | দরজা খুলুন, প্লিজ।
Close the window. | জানালা বন্ধ করুন।
Turn on the light. | আলো জ্বালান।
Turn off the fan. | পাখা বন্ধ করুন।
The kitchen is clean. | রান্নাঘর পরিষ্কার।
My mother cooks in the kitchen. | আমার মা রান্নাঘরে রান্না করেন।
Where is my phone? | আমার ফোন কোথায়?
It is on the bed. | ওটা খাটের উপর।
Is there a fan in your room? | আপনার ঘরে কি পাখা আছে?
Yes, there is. | হ্যাঁ, আছে।
Welcome to my home. | আমার বাড়িতে স্বাগতম।
""",
dict(title="There is / There are — “আছে”",
     points=["<b>There is</b> + একটি জিনিস: There is a fan.", "<b>There are</b> + একাধিক: There are two rooms.", "কোথায়: <b>on</b> (উপর), <b>under</b> (নিচে), <b>in</b> (ভিতরে), <b>next to</b> (পাশে)"],
     table=[("There is", "একটি", "There is a bed."), ("There are", "একাধিক", "There are three chairs.")],
     quiz=("There ___ three chairs in the room.", ["is", "are", "am"], 1, "three chairs একাধিক, তাই There are।")))

# ======================================================================= Day 8
day(8, "The Weather", "আবহাওয়া", "আজ আবহাওয়া, বৃষ্টি, আজ-কাল-গতকালের কথা বলতে শিখব।",
"""
It is a hot day in Dhaka. | ঢাকায় আজ গরমের দিন।
The sun is bright. | সূর্য উজ্জ্বল।
Sanjoy drinks a lot of water. | সঞ্জয় অনেক পানি খায়।
In the afternoon, the sky becomes dark. | বিকেলে আকাশ কালো হয়ে যায়।
It starts to rain. | বৃষ্টি শুরু হয়।
"I love the rain," says Sanjoy. | "আমি বৃষ্টি ভালোবাসি," বলে সঞ্জয়।
The weather is cool now. | এখন আবহাওয়া ঠান্ডা।
"What a beautiful evening!" | "কী সুন্দর সন্ধ্যা!"
""",
"""
weather | ওয়েদার | আবহাওয়া
hot | হট | গরম
cold | কোল্ড | ঠান্ডা
rain | রেইন | বৃষ্টি
sun | সান | সূর্য
sky | স্কাই | আকাশ
cloud | ক্লাউড | মেঘ
wind | উইন্ড | বাতাস
today | টুডে | আজ
tomorrow | টুমরো | আগামীকাল
""",
"""
How is the weather today? | আজ আবহাওয়া কেমন?
It is hot today. | আজ গরম।
It is very cold. | অনেক ঠান্ডা।
It is raining. | বৃষ্টি হচ্ছে।
It is not raining. | বৃষ্টি হচ্ছে না।
The sun is bright. | সূর্য উজ্জ্বল।
The sky is cloudy. | আকাশ মেঘলা।
There is a strong wind. | জোরে বাতাস বইছে।
I like the rain. | আমি বৃষ্টি পছন্দ করি।
Take an umbrella. | ছাতা নাও।
What day is it today? | আজ কী বার?
Today is Friday. | আজ শুক্রবার।
Tomorrow is Saturday. | আগামীকাল শনিবার।
Yesterday was Thursday. | গতকাল বৃহস্পতিবার ছিল।
It will rain tomorrow. | আগামীকাল বৃষ্টি হবে।
Summer is hot. | গ্রীষ্ম গরম।
Winter is cold. | শীত ঠান্ডা।
I like winter. | আমি শীত পছন্দ করি।
The evening is beautiful. | সন্ধ্যাটা সুন্দর।
What a lovely day! | কী চমৎকার দিন!
""",
dict(title="Present Continuous — এখন যা হচ্ছে",
     points=["এই মুহূর্তে যা ঘটছে: <b>is / am / are + verb-ing</b>", "<b>It is raining.</b> (বৃষ্টি হচ্ছে)", "<b>I am drinking</b> water. · <b>They are playing</b> cricket."],
     table=[("It", "is raining", "বৃষ্টি হচ্ছে"), ("I", "am reading", "আমি পড়ছি"), ("They", "are playing", "তারা খেলছে")],
     quiz=("Look! It ___ raining now.", ["is", "are", "do"], 0, "It-এর সাথে is + raining।")))

# ======================================================================= Day 9
day(9, "Phone and Friends", "ফোন ও বন্ধু", "আজ ফোনে কথা বলতে, দেখা করার সময় ঠিক করতে আর খেলার প্রস্তাব দিতে শিখব।",
"""
Sanjoy's phone rings. | সঞ্জয়ের ফোন বাজে।
"Hello? Who is this?" | "হ্যালো? কে বলছেন?"
"It's me, Rahim." | "আমি রহিম।"
"Hi Rahim! How are you?" | "হাই রহিম! কেমন আছো?"
"I am good. Are you free this evening?" | "আমি ভালো। আজ সন্ধ্যায় কি তুমি ফ্রি?"
"Yes! Why?" | "হ্যাঁ! কেন?"
"Let's play cricket!" | "চলো ক্রিকেট খেলি!"
"Great idea! See you at five." | "দারুণ আইডিয়া! পাঁচটায় দেখা হবে।"
""",
"""
phone | ফোন | ফোন
call | কল | ফোন করা
message | মেসেজ | বার্তা
free | ফ্রি | অবসর, ফাঁকা
busy | বিজি | ব্যস্ত
play | প্লে | খেলা
cricket | ক্রিকেট | ক্রিকেট
idea | আইডিয়া | ধারণা, পরিকল্পনা
meet | মিট | দেখা করা
wait | ওয়েট | অপেক্ষা করা
""",
"""
Hello, who is this? | হ্যালো, কে বলছেন?
This is Sanjoy speaking. | আমি সঞ্জয় বলছি।
Can I speak to Rahim? | আমি কি রহিমের সাথে কথা বলতে পারি?
Please wait a moment. | দয়া করে একটু অপেক্ষা করুন।
I will call you later. | আমি পরে আপনাকে ফোন করব।
Call me tomorrow. | আমাকে আগামীকাল ফোন করো।
I will send you a message. | আমি তোমাকে একটা মেসেজ পাঠাব।
Are you free today? | তুমি কি আজ ফ্রি?
I am busy now. | আমি এখন ব্যস্ত।
I am free in the evening. | আমি সন্ধ্যায় ফ্রি।
Let's meet at five. | চলো পাঁচটায় দেখা করি।
Where shall we meet? | আমরা কোথায় দেখা করব?
Let's play cricket. | চলো ক্রিকেট খেলি।
Do you play football? | তুমি কি ফুটবল খেলো?
That is a great idea. | এটা দারুণ আইডিয়া।
I can't come today. | আমি আজ আসতে পারব না।
I am on my way. | আমি আসছি, রওনা দিয়েছি।
Can you hear me? | তুমি কি আমার কথা শুনতে পাচ্ছ?
The network is bad. | নেটওয়ার্ক খারাপ।
Talk to you soon! | শিগগিরই কথা হবে!
""",
dict(title="can / can't — পারা, না পারা",
     points=["<b>can</b> + verb — পারি: I can play cricket.", "<b>can't</b> (cannot) — পারি না: I can't come today.", "প্রশ্ন/অনুমতি: <b>Can I</b> speak to Rahim? · <b>Can you</b> hear me?"],
     table=[("I", "can swim", "আমি সাঁতার জানি"), ("She", "can't drive", "সে গাড়ি চালাতে পারে না"), ("Can you", "help me?", "আমাকে সাহায্য করবেন?")],
     quiz=("Sorry, I ___ come today. I am busy.", ["can", "can't", "am"], 1, "ব্যস্ত, তাই আসতে পারছি না = can't।")))

# ======================================================================= Day 10
day(10, "Weekend Plan", "সপ্তাহান্তের পরিকল্পনা", "আজ ভবিষ্যতের পরিকল্পনা বলতে আর ইংরেজি শেখার কথা বলতে শিখব।",
"""
This weekend, Sanjoy has a plan. | এই সপ্তাহান্তে সঞ্জয়ের একটি পরিকল্পনা আছে।
On Friday, he will visit his grandmother. | শুক্রবার সে তার দাদির সাথে দেখা করতে যাবে।
He will take some mangoes for her. | সে তার জন্য কিছু আম নেবে।
On Saturday, he will study English. | শনিবার সে ইংরেজি পড়বে।
In the evening, he will play cricket with Rahim. | সন্ধ্যায় সে রহিমের সাথে ক্রিকেট খেলবে।
On Sunday, he will clean his room. | রবিবার সে তার ঘর পরিষ্কার করবে।
"I will speak English every day!" | "আমি প্রতিদিন ইংরেজিতে কথা বলব!"
"I am learning, and I am happy." | "আমি শিখছি, আর আমি খুশি।"
""",
"""
weekend | উইকএন্ড | সপ্তাহান্ত
plan | প্ল্যান | পরিকল্পনা
visit | ভিজিট | দেখা করতে যাওয়া
study | স্টাডি | পড়াশোনা করা
clean | ক্লিন | পরিষ্কার করা
learn | লার্ন | শেখা
speak | স্পিক | কথা বলা
happy | হ্যাপি | খুশি
every day | এভরি ডে | প্রতিদিন
week | উইক | সপ্তাহ
""",
"""
What is your plan for the weekend? | সপ্তাহান্তের জন্য আপনার পরিকল্পনা কী?
I will visit my grandmother. | আমি আমার দাদির সাথে দেখা করতে যাব।
I will study English. | আমি ইংরেজি পড়ব।
I will clean my room. | আমি আমার ঘর পরিষ্কার করব।
I will not go out. | আমি বাইরে যাব না।
Will you come with me? | তুমি কি আমার সাথে আসবে?
Yes, I will. | হ্যাঁ, আসব।
No, I won't. | না, আসব না।
I am learning English. | আমি ইংরেজি শিখছি।
I can speak a little English. | আমি একটু ইংরেজি বলতে পারি।
Please speak slowly. | দয়া করে ধীরে বলুন।
Can you say it again? | আপনি কি আবার বলতে পারেন?
I don't understand. | আমি বুঝতে পারছি না।
I understand now. | আমি এখন বুঝেছি।
What does this mean? | এটার মানে কী?
How do you say this in English? | এটা ইংরেজিতে কীভাবে বলে?
Practice every day. | প্রতিদিন অনুশীলন করুন।
I am happy to learn. | আমি শিখতে পেরে খুশি।
See you next week. | আগামী সপ্তাহে দেখা হবে।
Have a great weekend! | আপনার সপ্তাহান্ত দারুণ কাটুক!
""",
dict(title="will — ভবিষ্যতের কথা",
     points=["<b>will + verb</b> — করব/করবে: I will study.", "না: <b>will not = won't</b>: I won't go out.", "প্রশ্ন: <b>Will you</b> come with me?"],
     table=[("I", "will visit", "আমি যাব"), ("She", "will study", "সে পড়বে"), ("We", "won't go", "আমরা যাব না")],
     quiz=("Tomorrow I ___ study English.", ["will", "am", "does"], 0, "আগামীকালের পরিকল্পনা = will + verb।")))

assert len(DAYS) == 10
for d in DAYS:
    assert len(d["story"]) == 8, (d["n"], "story", len(d["story"]))
    assert len(d["words"]) == 10, (d["n"], "words", len(d["words"]))
    assert len(d["sentences"]) == 20, (d["n"], "sentences", len(d["sentences"]))
