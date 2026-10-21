"""English 101 — গল্পে গল্পে ইংরেজি. Twenty days; each day = one short story about Sanjoy, 10 words, 20 sentences,
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
Hello! My name is Sanjoy Dev Shuvo. | হ্যালো! আমার নাম সঞ্জয় দেব শুভ।
I work at Medicine Corner in Hajiganj Bazar. | আমি হাজীগঞ্জ বাজারের মেডিসিন কর্নারে কাজ করি।
I live in Hajiganj, Chandpur. | আমি চাঁদপুরের হাজীগঞ্জে থাকি।
I am a graduate. | আমি একজন গ্র্যাজুয়েট।
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
My name is Sanjoy Dev Shuvo. | আমার নাম সঞ্জয় দেব শুভ।
What is your name? | আপনার নাম কী?
I am from Bangladesh. | আমি বাংলাদেশ থেকে।
Where are you from? | আপনি কোথা থেকে এসেছেন?
I live in Hajiganj, Chandpur. | আমি চাঁদপুরের হাজীগঞ্জে থাকি।
I am a graduate. | আমি একজন গ্র্যাজুয়েট।
Are you a graduate? | আপনি কি গ্র্যাজুয়েট?
Yes, I am. | হ্যাঁ, আমি।
No, I am not. | না, আমি না।
This is my friend. | ইনি আমার বন্ধু।
Nice to meet you. | আপনার সাথে দেখা হয়ে ভালো লাগল।
Nice to meet you, too. | আপনার সাথেও দেখা হয়ে ভালো লাগল।
I work at Medicine Corner. | আমি মেডিসিন কর্নারে কাজ করি।
You can call me Shuvo. | আপনি আমাকে শুভ বলে ডাকতে পারেন।
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
I have a small family of four. | আমার চার সদস্যের একটি ছোট পরিবার আছে।
This is my father, Sukumar Poddar. He is a businessman. | ইনি আমার বাবা, সুকুমার পোদ্দার। তিনি একজন ব্যবসায়ী।
This is my mother, Nupur Poddar. She is a homemaker. | ইনি আমার মা, নুপুর পোদ্দার। তিনি একজন গৃহিণী।
I have one younger brother, Rajib Poddar. | আমার একটি ছোট ভাই আছে, রাজীব পোদ্দার।
Our father works hard in his business. | আমাদের বাবা তার ব্যবসায় কঠোর পরিশ্রম করেন।
Our mother takes care of our home. | আমাদের মা আমাদের ঘরের যত্ন নেন।
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
businessman | বিজনেসম্যান | ব্যবসায়ী
homemaker | হোমমেইকার | গৃহিণী
love | লাভ | ভালোবাসা
""",
"""
This is my father. | ইনি আমার বাবা।
This is my mother. | ইনি আমার মা।
I have a brother. | আমার একটি ভাই আছে।
I have one younger brother. | আমার একটি ছোট ভাই আছে।
Do you have a brother? | আপনার কি ভাই আছে?
Yes, I have one younger brother. | হ্যাঁ, আমার একটি ছোট ভাই আছে।
No, I don't have a sister. | না, আমার কোনো বোন নেই।
My father is a businessman. | আমার বাবা একজন ব্যবসায়ী।
My mother is a homemaker. | আমার মা একজন গৃহিণী।
How many people are in your family? | আপনার পরিবারে কতজন মানুষ?
There are four people in my family. | আমার পরিবারে চারজন মানুষ।
My grandfather is old. | আমার দাদা বয়স্ক।
My grandmother makes tea. | আমার দাদি চা বানান।
His name is Rajib. | তার নাম রাজীব।
He is my younger brother. | সে আমার ছোট ভাই।
I love my mother. | আমি আমার মাকে ভালোবাসি।
We eat dinner together. | আমরা একসাথে রাতের খাবার খাই।
My brother and I are friends. | আমার ভাই আর আমি বন্ধু।
My mother is very kind. | আমার মা খুব দয়ালু।
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
I open Medicine Corner at nine. | আমি নয়টায় মেডিসিন কর্নার খুলি।
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
I open the shop at nine. | আমি নয়টায় দোকান খুলি।
I leave home at eight. | আমি আটটায় বাড়ি থেকে বের হই।
My mother wakes up early. | আমার মা সকালে আগে ওঠেন।
I don't want to sleep late. | আমি দেরিতে ঘুমাতে চাই না।
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
People buy medicine at my shop. | মানুষ আমার দোকান থেকে ওষুধ কেনে।
This medicine is not expensive. | এই ওষুধটা দামি না।
Thank you, see you again. | ধন্যবাদ, আবার দেখা হবে।
""",
dict(title="How much? বনাম How many?",
     points=["<b>How much</b> — যা গোনা যায় না বা দাম: how much water, how much is this?", "<b>How many</b> — যা গোনা যায়: how many mangoes, how many people?"],
     table=[("How much", "দাম / পরিমাণ", "How much is this?"), ("How many", "সংখ্যা", "How many kilos?")],
     quiz=("___ mangoes do you want?", ["How much", "How many", "How"], 1, "আম গোনা যায়, তাই How many।")))

# ======================================================================= Day 5
day(5, "Food and Tea", "খাবার আর চা", "আজ রেস্টুরেন্টে খাবার অর্ডার করতে আর খাবারের কথা বলতে শিখব।",
"""
It is lunch time at Medicine Corner. | মেডিসিন কর্নারে এখন দুপুরের খাবারের সময়।
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
I eat lunch at my shop. | আমি আমার দোকানে দুপুরের খাবার খাই।
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
Sanjoy goes to Hajiganj Bazar by bus. | সঞ্জয় বাসে করে হাজীগঞ্জ বাজারে যায়।
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
I am going to the shop. | আমি দোকানে যাচ্ছি।
I go by bus. | আমি বাসে যাই।
Excuse me, where is the bus stop? | মাফ করবেন, বাস স্টপ কোথায়?
It is near here. | এটা এখানেই কাছে।
It is far from here. | এটা এখান থেকে দূরে।
Go straight. | সোজা যান।
Turn left. | বাঁয়ে ঘুরুন।
Turn right. | ডানে ঘুরুন।
Stop here, please. | এখানে থামুন, প্লিজ।
How much to Hajiganj Bazar? | হাজীগঞ্জ বাজার পর্যন্ত কত?
Please hurry. | দয়া করে তাড়াতাড়ি করুন।
There is a lot of traffic. | অনেক যানজট।
I am stuck in traffic. | আমি যানজটে আটকে আছি।
I walk to the shop. | আমি দোকান পর্যন্ত হেঁটে যাই।
Is this the right bus? | এটা কি ঠিক বাস?
This bus goes to Chandpur. | এই বাসটা চাঁদপুর যায়।
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
I live in a house with my family. | আমি পরিবারের সাথে একটি বাড়িতে থাকি।
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
It is a hot day in Hajiganj. | হাজীগঞ্জে আজ গরমের দিন।
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
I am busy at the shop now. | আমি এখন দোকানে ব্যস্ত।
I am free in the evening. | আমি সন্ধ্যায় ফ্রি।
Let's meet at five. | চলো পাঁচটায় দেখা করি।
Where shall we meet? | আমরা কোথায় দেখা করব?
Let's play cricket. | চলো ক্রিকেট খেলি।
Can I help you? | আমি কি আপনাকে সাহায্য করতে পারি?
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
On Friday, he will visit Rahim. | শুক্রবার সে রহিমের সাথে দেখা করতে যাবে।
He will take some mangoes with him. | সে সাথে কিছু আম নেবে।
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
I will visit my friend. | আমি আমার বন্ধুর সাথে দেখা করতে যাব।
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

# ======================================================================= Day 11
day(11, "Body and Health", "শরীর ও স্বাস্থ্য", "আজ শরীরের অংশ, অসুস্থতার কথা আর ডাক্তারের কাছে যেতে শিখব।",
"""
Sanjoy wakes up with a headache. | সঞ্জয় মাথাব্যথা নিয়ে ঘুম থেকে ওঠে।
He also has a fever. | তার জ্বরও আছে।
His mother says, "You should see a doctor." | তার মা বলেন, "তোমার ডাক্তার দেখানো উচিত।"
At the hospital, the doctor checks his eyes and throat. | হাসপাতালে ডাক্তার তার চোখ আর গলা পরীক্ষা করেন।
"You have a small fever. Take this medicine." | "তোমার সামান্য জ্বর। এই ওষুধটা খাও।"
"Drink a lot of water and rest." | "প্রচুর পানি খাও আর বিশ্রাম নাও।"
Two days later, Sanjoy feels much better and goes back to Medicine Corner. | দুই দিন পরে সঞ্জয় অনেক ভালো বোধ করে আর মেডিসিন কর্নারে ফিরে যায়।
"Health is more important than work," he says. | "কাজের চেয়ে স্বাস্থ্য বেশি জরুরি," সে বলে।
""",
"""
head | হেড | মাথা
eye | আই | চোখ
hand | হ্যান্ড | হাত
stomach | স্টমাক | পেট
fever | ফিভার | জ্বর
pain | পেইন | ব্যথা
doctor | ডক্টর | ডাক্তার
medicine | মেডিসিন | ওষুধ
hospital | হসপিটাল | হাসপাতাল
healthy | হেলদি | সুস্থ, স্বাস্থ্যবান
""",
"""
I have a headache. | আমার মাথাব্যথা করছে।
My stomach hurts. | আমার পেট ব্যথা করছে।
I have a fever. | আমার জ্বর আছে।
I don't feel well. | আমি ভালো বোধ করছি না।
How do you feel today? | আজ আপনি কেমন বোধ করছেন?
I feel much better. | আমি অনেক ভালো বোধ করছি।
You should see a doctor. | আপনার ডাক্তার দেখানো উচিত।
You should take some rest. | আপনার কিছুটা বিশ্রাম নেওয়া উচিত।
You should drink more water. | আপনার আরও পানি খাওয়া উচিত।
You shouldn't eat too much oily food. | আপনার বেশি তেলে ভাজা খাবার খাওয়া উচিত না।
Take this medicine twice a day. | এই ওষুধ দিনে দুইবার খান।
Where is the nearest hospital? | সবচেয়ে কাছের হাসপাতাল কোথায়?
I need to see a doctor. | আমার ডাক্তার দেখাতে হবে।
Do you have any pain? | আপনার কি কোথাও ব্যথা আছে?
Open your mouth, please. | দয়া করে মুখ খুলুন।
My hand is hurting. | আমার হাতে ব্যথা করছে।
Please close your eyes. | দয়া করে চোখ বন্ধ করুন।
Do you need any medicine? | আপনার কি কোনো ওষুধ লাগবে?
Stay healthy and happy. | সুস্থ আর খুশি থাকুন।
Get well soon! | শিগগিরই সুস্থ হয়ে উঠুন!
""",
dict(title="should / shouldn't — পরামর্শ",
     points=["<b>should + verb</b> — করা উচিত: You should rest.", "<b>shouldn't</b> — করা উচিত না: You shouldn't worry.", "প্রশ্ন: <b>Should I</b> see a doctor? (আমার কি ডাক্তার দেখানো উচিত?)"],
     table=[("You", "should rest", "আপনার বিশ্রাম নেওয়া উচিত"), ("He", "should see a doctor", "তার ডাক্তার দেখানো উচিত"), ("You", "shouldn't worry", "আপনার চিন্তা করা উচিত না")],
     quiz=("You ___ drink more water. (পরামর্শ)", ["should", "shouldn't", "are"], 0, "পরামর্শ দিতে should + verb।")))

# ======================================================================= Day 12
day(12, "Clothes and Shopping", "পোশাক ও কেনাকাটা", "আজ ঈদের কেনাকাটায় পোশাক পছন্দ করতে, মাপ বলতে আর দাম দিতে শিখব।",
"""
Eid is coming, so Sanjoy goes shopping. | ঈদ আসছে, তাই সঞ্জয় কেনাকাটায় যায়।
He wants a new shirt. | সে একটি নতুন শার্ট চায়।
"Do you have this shirt in blue?" he asks. | "এই শার্টটা কি নীল রঙে আছে?" সে জিজ্ঞেস করে।
"Yes, what size do you wear?" | "হ্যাঁ, আপনি কোন সাইজ পরেন?"
"Medium." He tries on the shirt. | "মিডিয়াম।" সে শার্টটা পরে দেখে।
"It fits well, but it is a little expensive." | "ঠিকমতো লেগেছে, কিন্তু একটু দামি।"
The shopkeeper gives a small discount. | দোকানদার একটু ছাড় দেন।
Sanjoy pays and takes the receipt. | সঞ্জয় টাকা দেয় আর রসিদ নেয়।
""",
"""
shirt | শার্ট | শার্ট
trousers | ট্রাউজারস | প্যান্ট
shoes | শুজ | জুতা
size | সাইজ | মাপ
colour | কালার | রং
wear | ওয়্যার | পরা
try on | ট্রাই অন | পরে দেখা
fit | ফিট | ঠিকমতো লাগা
pay | পে | টাকা দেওয়া
receipt | রিসিট | রসিদ
""",
"""
I want to buy a shirt. | আমি একটি শার্ট কিনতে চাই।
Do you have this in blue? | আপনার কাছে কি এটা নীল রঙে আছে?
What colour do you like? | আপনি কোন রং পছন্দ করেন?
I like the black one. | আমি কালোটা পছন্দ করি।
What size do you wear? | আপনি কোন সাইজ পরেন?
I wear size medium. | আমি মিডিয়াম সাইজ পরি।
Can I try this on? | আমি কি এটা পরে দেখতে পারি?
The fitting room is over there. | ট্রায়াল রুম ওখানে।
It fits me well. | এটা আমার ঠিকমতো লাগছে।
It is too big. | এটা অনেক বড়।
It is too small. | এটা অনেক ছোট।
Do you have a bigger size? | আপনার কাছে কি আরও বড় সাইজ আছে?
These shoes are comfortable. | এই জুতাগুলো আরামদায়ক।
Those trousers are too long. | ওই প্যান্টটা অনেক লম্বা।
How much is this shirt? | এই শার্টের দাম কত?
Is there any discount? | কোনো ছাড় আছে কি?
I will take this one. | আমি এটা নেব।
Can I pay by card? | আমি কি কার্ডে টাকা দিতে পারি?
Please give me the receipt. | দয়া করে আমাকে রসিদটা দিন।
Happy Eid shopping! | ঈদের কেনাকাটা শুভ হোক!
""",
dict(title="this / that / these / those",
     points=["<b>this</b> — কাছের একটি জিনিস: this shirt", "<b>these</b> — কাছের অনেকগুলো: these shoes", "<b>that</b> — দূরের একটি: that bag", "<b>those</b> — দূরের অনেকগুলো: those trousers"],
     table=[("this", "কাছে, একটি", "This shirt is nice."), ("these", "কাছে, একাধিক", "These shoes are new."), ("that", "দূরে, একটি", "That bag is big."), ("those", "দূরে, একাধিক", "Those books are old.")],
     quiz=("(হাতের কাছের অনেক জুতা) ___ shoes are comfortable.", ["This", "These", "That"], 1, "কাছে + একাধিক = these।")))

# ======================================================================= Day 13
day(13, "Numbers and Dates", "সংখ্যা ও তারিখ", "আজ সংখ্যা, মাস, তারিখ আর জন্মদিনের কথা বলতে শিখব।",
"""
Today is Sanjoy's birthday. | আজ সঞ্জয়ের জন্মদিন।
It is the twenty-first of October. | আজ একুশে অক্টোবর।
He is one year older today. | সে আজ এক বছর বড় হলো।
His friends call him in the morning. | তার বন্ধুরা সকালে তাকে ফোন করে।
"Happy birthday, Sanjoy!" they say. | "শুভ জন্মদিন, সঞ্জয়!" তারা বলে।
In the evening, he cuts a cake with his family. | সন্ধ্যায় সে পরিবারের সাথে কেক কাটে।
The cake costs one thousand two hundred taka. | কেকটার দাম এক হাজার দুইশো টাকা।
"This is my best birthday!" he says. | "এটা আমার সেরা জন্মদিন!" সে বলে।
""",
"""
number | নাম্বার | সংখ্যা, নম্বর
hundred | হান্ড্রেড | একশো
thousand | থাউজেন্ড | হাজার
month | মান্থ | মাস
year | ইয়ার | বছর
date | ডেইট | তারিখ
birthday | বার্থডে | জন্মদিন
first | ফার্স্ট | প্রথম
second | সেকেন্ড | দ্বিতীয়
third | থার্ড | তৃতীয়
""",
"""
What is today's date? | আজকের তারিখ কত?
Today is the twenty-first of October. | আজ একুশে অক্টোবর।
My birthday is in March. | আমার জন্মদিন মার্চ মাসে।
When is your birthday? | আপনার জন্মদিন কবে?
It is on the fifth of May. | এটা পাঁচই মে।
Happy birthday! | শুভ জন্মদিন!
Many happy returns of the day. | জন্মদিনের অনেক শুভেচ্ছা।
One, two, three, four, five. | এক, দুই, তিন, চার, পাঁচ।
Ten, twenty, thirty, forty, fifty. | দশ, বিশ, ত্রিশ, চল্লিশ, পঞ্চাশ।
This medicine is one hundred taka. | এই ওষুধটা একশো টাকা।
This box is two hundred and fifty taka. | এই বাক্সটা আড়াইশো টাকা।
One thousand taka. | এক হাজার টাকা।
What is your phone number? | আপনার ফোন নম্বর কত?
Please write down your number. | দয়া করে আপনার নম্বরটা লিখে দিন।
This is my first job. | এটা আমার প্রথম চাকরি।
He is the second son. | সে দ্বিতীয় ছেলে।
She is in the third class. | সে তৃতীয় শ্রেণিতে পড়ে।
There are twelve months in a year. | এক বছরে বারো মাস।
There are seven days in a week. | এক সপ্তাহে সাত দিন।
Happy New Year! | শুভ নববর্ষ!
""",
dict(title="in / on / at — সময়ের সাথে",
     points=["<b>in</b> — মাস, বছর, ঋতু: in March, in 2026, in winter", "<b>on</b> — নির্দিষ্ট দিন ও তারিখ: on Friday, on the fifth of May", "<b>at</b> — ঘড়ির সময়: at five o'clock, at night"],
     table=[("in", "মাস / বছর", "in March"), ("on", "দিন / তারিখ", "on Friday"), ("at", "ঘড়ির সময়", "at ten")],
     quiz=("My birthday is ___ March.", ["in", "on", "at"], 0, "মাসের আগে in বসে।")))

# ======================================================================= Day 14
day(14, "Study Life", "পড়াশোনার জীবন", "আজ ক্লাস, শিক্ষক, পরীক্ষা আর হোমওয়ার্কের কথা বলতে শিখব।",
"""
Sanjoy has an English class at ten o'clock. | সঞ্জয়ের দশটায় ইংরেজি ক্লাস আছে।
The teacher asks a question. | শিক্ষক একটি প্রশ্ন করেন।
Sanjoy raises his hand and gives the answer. | সঞ্জয় হাত তোলে আর উত্তর দেয়।
"Very good!" says the teacher. | "খুব ভালো!" বলেন শিক্ষক।
After class, he goes to Medicine Corner. | ক্লাসের পরে সে মেডিসিন কর্নারে যায়।
He reads a book and writes notes in his notebook. | সে একটি বই পড়ে আর খাতায় নোট লেখে।
The teacher gives homework for tomorrow. | শিক্ষক আগামীকালের জন্য হোমওয়ার্ক দেন।
Next week there is an exam, so he studies hard. | আগামী সপ্তাহে পরীক্ষা, তাই সে কঠোর পরিশ্রম করে পড়ে।
""",
"""
class | ক্লাস | ক্লাস, শ্রেণি
teacher | টিচার | শিক্ষক
exam | এগজাম | পরীক্ষা
homework | হোমওয়ার্ক | বাড়ির কাজ
subject | সাবজেক্ট | বিষয়
question | কোয়েশ্চেন | প্রশ্ন
answer | আন্সার | উত্তর
library | লাইব্রেরি | গ্রন্থাগার
notebook | নোটবুক | খাতা
read | রিড | পড়া
""",
"""
I have an English class today. | আজ আমার ইংরেজি ক্লাস আছে।
What time does the class start? | ক্লাস কয়টায় শুরু হয়?
The class starts at ten. | ক্লাস দশটায় শুরু হয়।
Who is your teacher? | আপনার শিক্ষক কে?
My favourite subject is English. | আমার প্রিয় বিষয় ইংরেজি।
What is your favourite subject? | আপনার প্রিয় বিষয় কী?
May I ask a question? | আমি কি একটি প্রশ্ন করতে পারি?
Can you repeat the question? | আপনি কি প্রশ্নটা আবার বলবেন?
I know the answer. | আমি উত্তরটা জানি।
I don't know the answer. | আমি উত্তরটা জানি না।
Please open your notebook. | দয়া করে আপনার খাতা খুলুন।
Write your name here. | এখানে আপনার নাম লিখুন।
Read this page aloud. | এই পৃষ্ঠাটি জোরে পড়ুন।
Do you have homework today? | আজ কি আপনার হোমওয়ার্ক আছে?
I must finish my homework. | আমাকে হোমওয়ার্ক শেষ করতে হবে।
Let's go to the library. | চলো লাইব্রেরিতে যাই।
Please be quiet in the library. | দয়া করে লাইব্রেরিতে চুপ থাকুন।
The exam is next week. | পরীক্ষা আগামী সপ্তাহে।
I am studying for the exam. | আমি পরীক্ষার জন্য পড়ছি।
Good luck with your exam! | পরীক্ষায় শুভকামনা!
""",
dict(title="must / have to — বাধ্যবাধকতা",
     points=["<b>must + verb</b> — করতেই হবে: I must finish my homework.", "<b>have to / has to</b> — একই অর্থ: She has to study.", "<b>must not (mustn't)</b> — করা নিষেধ: You mustn't talk in the exam."],
     table=[("I", "must study", "আমাকে পড়তেই হবে"), ("She", "has to go", "তাকে যেতে হবে"), ("You", "mustn't cheat", "নকল করা নিষেধ")],
     quiz=("You ___ be quiet in the library. (নিয়ম)", ["must", "mustn't", "can"], 0, "নিয়ম/বাধ্যবাধকতা বোঝাতে must।")))

# ======================================================================= Day 15
day(15, "Yesterday", "গতকাল (অতীত কাল)", "আজ গতকাল কী করেছি তা বলতে শিখব — অতীত কালের ক্রিয়া।",
"""
Yesterday was a busy day for Sanjoy. | গতকাল সঞ্জয়ের জন্য ব্যস্ত একটি দিন ছিল।
He woke up early and went to Medicine Corner. | সে সকালে ঘুম থেকে উঠে মেডিসিন কর্নারে গেল।
He sold medicine to many people. | সে অনেক মানুষের কাছে ওষুধ বিক্রি করল।
On the way, he met his old friend Rahim. | পথে সে তার পুরনো বন্ধু রহিমের সাথে দেখা করল।
They ate lunch together. | তারা একসাথে দুপুরের খাবার খেলো।
In the afternoon, he saw a movie with his brother. | বিকেলে সে তার ভাইয়ের সাথে একটি সিনেমা দেখল।
He came home late at night. | সে অনেক রাতে বাড়ি ফিরল।
"I didn't sleep early, but I had a great day!" | "আমি তাড়াতাড়ি ঘুমাইনি, কিন্তু দিনটা দারুণ ছিল!"
""",
"""
yesterday | ইয়েস্টারডে | গতকাল
ago | অ্যাগো | আগে
went | ওয়েন্ট | গেল (go-র অতীত)
saw | সো | দেখল (see-র অতীত)
ate | এইট | খেল (eat-এর অতীত)
came | কেইম | এল (come-এর অতীত)
bought | বট | কিনল (buy-র অতীত)
met | মেট | দেখা করল (meet-এর অতীত)
gave | গেইভ | দিল (give-এর অতীত)
took | টুক | নিল (take-এর অতীত)
""",
"""
What did you do yesterday? | গতকাল আপনি কী করেছিলেন?
I went to the market yesterday. | আমি গতকাল বাজারে গিয়েছিলাম।
I bought some fruits. | আমি কিছু ফল কিনেছিলাম।
I met my friend there. | আমি সেখানে আমার বন্ধুর সাথে দেখা করেছিলাম।
We ate lunch together. | আমরা একসাথে দুপুরের খাবার খেয়েছিলাম।
We played cricket in the evening. | আমরা সন্ধ্যায় ক্রিকেট খেলেছিলাম।
I watched a movie last night. | আমি গত রাতে একটি সিনেমা দেখেছিলাম।
She came home early. | সে তাড়াতাড়ি বাড়ি এসেছিল।
He gave me a gift. | সে আমাকে একটি উপহার দিয়েছিল।
I took a rickshaw to the station. | আমি স্টেশন পর্যন্ত রিকশা নিয়েছিলাম।
I saw a beautiful bird. | আমি একটি সুন্দর পাখি দেখেছিলাম।
I didn't close the shop early. | আমি দোকান তাড়াতাড়ি বন্ধ করিনি।
She didn't call me. | সে আমাকে ফোন করেনি।
Did you sleep well? | আপনি কি ভালো ঘুমিয়েছিলেন?
Yes, I did. | হ্যাঁ, ঘুমিয়েছিলাম।
No, I didn't. | না, ঘুমাইনি।
I visited my friend two days ago. | আমি দুই দিন আগে আমার বন্ধুর সাথে দেখা করেছিলাম।
It rained all day. | সারাদিন বৃষ্টি হয়েছিল।
We were very tired. | আমরা খুব ক্লান্ত ছিলাম।
It was a wonderful day. | দিনটা চমৎকার ছিল।
""",
dict(title="Past Simple — অতীত কাল",
     points=["সাধারণ নিয়ম: verb + <b>-ed</b> — played, visited, watched", "অনিয়মিত (মুখস্থ): go → <b>went</b>, see → <b>saw</b>, eat → <b>ate</b>, buy → <b>bought</b>", "না/প্রশ্ন: <b>did / didn't + verb-এর আসল রূপ</b> — I didn't go. · Did you sleep?"],
     table=[("play", "played", "খেলেছিলাম"), ("go", "went", "গিয়েছিলাম"), ("didn't", "+ go", "যাইনি")],
     quiz=("Yesterday I ___ to the market.", ["go", "went", "going"], 1, "গতকাল = অতীত; go-র অতীত went।")))

# ======================================================================= Day 16
day(16, "Cooking at Home", "রান্নাঘরে", "আজ রান্নার ধাপ বলতে আর কাউকে নির্দেশ দিতে শিখব।",
"""
Today Sanjoy's mother teaches him to cook khichuri. | আজ সঞ্জয়ের মা তাকে খিচুড়ি রান্না শেখান।
"First, wash the rice and the dal," she says. | "প্রথমে চাল আর ডাল ধুয়ে নাও," তিনি বলেন।
"Then cut the onion into small pieces." | "তারপর পেঁয়াজ ছোট ছোট টুকরো করে কাটো।"
Sanjoy fries the onion in hot oil. | সঞ্জয় গরম তেলে পেঁয়াজ ভাজে।
"Now add salt and spices." | "এবার লবণ আর মসলা দাও।"
"Add water and boil it for twenty minutes." | "পানি দাও আর বিশ মিনিট সেদ্ধ করো।"
Finally, Sanjoy tastes the khichuri. | অবশেষে সঞ্জয় খিচুড়ির স্বাদ নেয়।
"It's delicious, Mom!" | "দারুণ হয়েছে, মা!"
""",
"""
cook | কুক | রান্না করা
boil | বয়েল | সেদ্ধ করা
fry | ফ্রাই | ভাজা
cut | কাট | কাটা
salt | সল্ট | লবণ
spice | স্পাইস | মসলা
oil | অয়েল | তেল
onion | অনিয়ন | পেঁয়াজ
recipe | রেসিপি | রান্নার প্রণালী
taste | টেইস্ট | স্বাদ নেওয়া; স্বাদ
""",
"""
Can you cook? | আপনি কি রান্না করতে পারেন?
I can cook rice and curry. | আমি ভাত আর তরকারি রান্না করতে পারি।
What is the recipe? | রান্নার প্রণালী কী?
First, wash the rice. | প্রথমে চাল ধুয়ে নিন।
Then cut the onions. | তারপর পেঁয়াজ কাটুন।
Heat the oil in a pan. | কড়াইতে তেল গরম করুন।
Fry the onions until they are brown. | পেঁয়াজ বাদামি হওয়া পর্যন্ত ভাজুন।
Add salt and spices. | লবণ আর মসলা দিন।
Add two cups of water. | দুই কাপ পানি দিন।
Boil it for twenty minutes. | বিশ মিনিট সেদ্ধ করুন।
Stir it slowly. | ধীরে ধীরে নাড়ুন।
Turn off the stove. | চুলা বন্ধ করুন।
Finally, taste it. | অবশেষে স্বাদ দেখুন।
It needs more salt. | এতে আরও লবণ লাগবে।
It is too spicy. | এটা খুব ঝাল।
It tastes great. | খেতে দারুণ হয়েছে।
Be careful, the pan is hot. | সাবধান, কড়াই গরম।
Do you like to cook? | আপনি কি রান্না করতে পছন্দ করেন?
My mother is a great cook. | আমার মা দারুণ রাঁধুনি।
Dinner is ready! | রাতের খাবার তৈরি!
""",
dict(title="নির্দেশ ও ধাপ: First, Then, Finally",
     points=["নির্দেশ দিতে <b>verb-এর আসল রূপ দিয়ে শুরু</b>: Wash the rice. Add salt.", "ধাপ বোঝাতে: <b>First</b> (প্রথমে), <b>Then / Next</b> (তারপর), <b>Finally</b> (অবশেষে)", "নিষেধ: <b>Don't + verb</b> — Don't touch the pan."],
     table=[("First", "wash the rice", "প্রথমে চাল ধোও"), ("Then", "cut the onion", "তারপর পেঁয়াজ কাটো"), ("Finally", "taste it", "অবশেষে স্বাদ দেখো")],
     quiz=("___, wash the rice. (প্রথম ধাপ)", ["First", "Finally", "Then"], 0, "প্রথম ধাপে First।")))

# ======================================================================= Day 17
day(17, "A Trip to Cox's Bazar", "কক্সবাজার ভ্রমণ", "আজ ভ্রমণের পরিকল্পনা, টিকেট, হোটেল আর সমুদ্রসৈকতের কথা বলতে শিখব।",
"""
Sanjoy and his friends are going to visit Cox's Bazar. | সঞ্জয় আর তার বন্ধুরা কক্সবাজার ঘুরতে যাচ্ছে।
They book their train tickets two weeks before. | তারা দুই সপ্তাহ আগে ট্রেনের টিকেট বুক করে।
On Friday night, they arrive at the station with their luggage. | শুক্রবার রাতে তারা মালপত্র নিয়ে স্টেশনে পৌঁছায়।
The train leaves at ten o'clock. | ট্রেন দশটায় ছাড়ে।
After a long journey, they reach Cox's Bazar. | দীর্ঘ যাত্রার পরে তারা কক্সবাজারে পৌঁছায়।
Their hotel is near the beach. | তাদের হোটেল সমুদ্রসৈকতের কাছে।
"Look at the waves!" says Sanjoy. | "ঢেউগুলো দেখো!" বলে সঞ্জয়।
"We are going to stay here for three days." | "আমরা এখানে তিন দিন থাকব।"
""",
"""
ticket | টিকেট | টিকেট
train | ট্রেইন | ট্রেন
station | স্টেশন | স্টেশন
journey | জার্নি | যাত্রা
luggage | লাগেজ | মালপত্র
hotel | হোটেল | হোটেল
beach | বিচ | সমুদ্রসৈকত
book | বুক | আগে থেকে নেওয়া (বুক করা)
arrive | অ্যারাইভ | পৌঁছানো
leave | লিভ | ছাড়া, ছেড়ে যাওয়া
""",
"""
Where are you going for the holiday? | ছুটিতে আপনি কোথায় যাচ্ছেন?
I am going to visit Cox's Bazar. | আমি কক্সবাজার ঘুরতে যাচ্ছি।
How are you going there? | আপনি সেখানে কীভাবে যাচ্ছেন?
We are going by train. | আমরা ট্রেনে যাচ্ছি।
I want to book two tickets. | আমি দুইটি টিকেট বুক করতে চাই।
What time does the train leave? | ট্রেন কয়টায় ছাড়ে?
It leaves at ten at night. | এটা রাত দশটায় ছাড়ে।
What time does it arrive? | এটা কয়টায় পৌঁছায়?
Which platform is it? | ওটা কোন প্ল্যাটফর্ম?
Where is the ticket counter? | টিকেট কাউন্টার কোথায়?
This is my luggage. | এটা আমার মালপত্র।
The journey is very long. | যাত্রাটা অনেক দীর্ঘ।
We have a hotel booking. | আমাদের হোটেল বুকিং আছে।
I would like a room with a sea view. | আমি সমুদ্র দেখা যায় এমন একটি ঘর চাই।
How much is the room per night? | ঘরের এক রাতের ভাড়া কত?
The beach is very beautiful. | সমুদ্রসৈকতটা খুব সুন্দর।
Let's take some photos. | চলো কিছু ছবি তুলি।
We are going to swim in the sea. | আমরা সমুদ্রে সাঁতার কাটব।
We are going to stay for three days. | আমরা তিন দিন থাকব।
Have a safe trip! | আপনার যাত্রা নিরাপদ হোক!
""",
dict(title="be going to — পরিকল্পনা",
     points=["ঠিক করা পরিকল্পনা: <b>am / is / are + going to + verb</b>", "I <b>am going to</b> visit Cox's Bazar.", "না: We <b>aren't going to</b> stay long. · প্রশ্ন: <b>Are you going to</b> swim?"],
     table=[("I", "am going to visit", "আমি ঘুরতে যাব"), ("She", "is going to book", "সে বুক করবে"), ("We", "are going to swim", "আমরা সাঁতার কাটব")],
     quiz=("We ___ going to visit the beach tomorrow.", ["are", "is", "am"], 0, "We-এর সাথে are going to।")))

# ======================================================================= Day 18
day(18, "Feelings and Opinions", "অনুভূতি ও মতামত", "আজ নিজের অনুভূতি, মতামত আর কারণ বলতে শিখব।",
"""
Sanjoy has an important English test today. | আজ সঞ্জয়ের একটি গুরুত্বপূর্ণ ইংরেজি পরীক্ষা।
In the morning, he feels afraid. | সকালে সে ভয় পায়।
"I think I will forget everything," he says. | "আমার মনে হয় আমি সব ভুলে যাব," সে বলে।
Rahim says, "I don't agree. You study every day." | রহিম বলে, "আমি একমত না। তুমি রোজ পড়ো।"
The test starts, and Sanjoy feels calmer. | পরীক্ষা শুরু হয়, আর সঞ্জয় আরও শান্ত বোধ করে।
He answers every question. | সে সব প্রশ্নের উত্তর দেয়।
The result comes: he passed! | ফল আসে: সে পাস করেছে!
He is surprised, excited and very happy. | সে অবাক, উত্তেজিত আর খুব খুশি।
""",
"""
sad | স্যাড | দুঃখিত, মন খারাপ
angry | অ্যাংগ্রি | রাগান্বিত
tired | টায়ার্ড | ক্লান্ত
excited | এক্সাইটেড | উত্তেজিত
afraid | আফ্রেইড | ভীত
surprised | সারপ্রাইজড | অবাক
think | থিংক | মনে করা, ভাবা
agree | অ্যাগ্রি | একমত হওয়া
opinion | ওপিনিয়ন | মতামত
because | বিকজ | কারণ, কেননা
""",
"""
How do you feel? | আপনি কেমন বোধ করছেন?
I feel happy today. | আমি আজ খুশি বোধ করছি।
I feel sad. | আমার মন খারাপ।
Why are you angry? | আপনি রাগ করেছেন কেন?
I am not angry. | আমি রাগ করিনি।
I am tired because I worked at the shop all day. | আমি ক্লান্ত কারণ সারাদিন দোকানে কাজ করেছি।
I am excited about the trip. | আমি ভ্রমণ নিয়ে উত্তেজিত।
Don't be afraid. | ভয় পেয়ো না।
I was surprised to see him. | তাকে দেখে আমি অবাক হয়েছিলাম।
What do you think? | আপনি কী মনে করেন?
I think it is a good idea. | আমি মনে করি এটা ভালো আইডিয়া।
In my opinion, it is too expensive. | আমার মতে এটা অনেক দামি।
I agree with you. | আমি আপনার সাথে একমত।
I don't agree. | আমি একমত নই।
I like it because it is simple. | আমার এটা ভালো লাগে কারণ এটা সহজ।
It is cheap, so I will buy it. | এটা সস্তা, তাই আমি কিনব।
It is nice, but it is far. | এটা সুন্দর, কিন্তু অনেক দূরে।
I am sorry to hear that. | এটা শুনে আমি দুঃখিত।
Don't worry, everything will be fine. | চিন্তা কোরো না, সব ঠিক হয়ে যাবে।
I am proud of you. | আমি তোমাকে নিয়ে গর্বিত।
""",
dict(title="because / so / but — কারণ, ফল, বিপরীত",
     points=["<b>because</b> — কারণ বলে: I am tired <b>because</b> I worked all day.", "<b>so</b> — ফল বলে: I am tired, <b>so</b> I will sleep early.", "<b>but</b> — বিপরীত বলে: It is nice, <b>but</b> it is far."],
     table=[("because", "কারণ", "I stayed home because it rained."), ("so", "তাই", "It rained, so I stayed home."), ("but", "কিন্তু", "I like tea, but I prefer coffee.")],
     quiz=("I am tired, ___ I will sleep early.", ["because", "so", "but"], 1, "ক্লান্ত → তাই ঘুমাব: ফল বোঝাতে so।")))

# ======================================================================= Day 19
day(19, "Comparing Places and People", "তুলনা: মানুষ ও জায়গা", "আজ দুটো জিনিসের তুলনা করতে আর সেরাটা বলতে শিখব।",
"""
Sanjoy lives in Hajiganj, a small town in Chandpur. | সঞ্জয় চাঁদপুরের ছোট শহর হাজীগঞ্জে থাকে।
Dhaka is bigger and more crowded than Hajiganj. | ঢাকা হাজীগঞ্জের চেয়ে বড় আর বেশি ভিড়ের।
Hajiganj is quieter and calmer. | হাজীগঞ্জ বেশি শান্ত আর নীরব।
He works at Medicine Corner in Hajiganj Bazar. | সে হাজীগঞ্জ বাজারের মেডিসিন কর্নারে কাজ করে।
Medicine Corner is the biggest medicine shop in Hajiganj Bazar. | মেডিসিন কর্নার হাজীগঞ্জ বাজারের সবচেয়ে বড় ওষুধের দোকান।
His mother is the kindest person he knows. | তার মা তার চেনা সবচেয়ে দয়ালু মানুষ।
"Dhaka is exciting, but Hajiganj is my favourite place," he says. | "ঢাকা রোমাঞ্চকর, কিন্তু হাজীগঞ্জই আমার সবচেয়ে প্রিয় জায়গা," সে বলে।
"I feel calm there." | "সেখানে আমি শান্তি অনুভব করি।"
""",
"""
big | বিগ | বড়
small | স্মল | ছোট
new | নিউ | নতুন
crowded | ক্রাউডেড | ভিড়ে ভরা
quiet | কোয়াইট | শান্ত, নীরব
famous | ফেইমাস | বিখ্যাত
beautiful | বিউটিফুল | সুন্দর
strong | স্ট্রং | শক্তিশালী
young | ইয়াং | তরুণ, কম বয়সী
rich | রিচ | ধনী
""",
"""
Dhaka is a big city. | ঢাকা একটি বড় শহর।
Hajiganj is small. | হাজীগঞ্জ ছোট।
Dhaka is bigger than Hajiganj. | ঢাকা হাজীগঞ্জের চেয়ে বড়।
Hajiganj is quieter than the city. | হাজীগঞ্জ শহরের চেয়ে শান্ত।
This bus is more crowded than that one. | এই বাসটা ওটার চেয়ে বেশি ভিড়ের।
My brother is taller than me. | আমার ভাই আমার চেয়ে লম্বা।
She is the youngest in the family. | সে পরিবারের সবচেয়ে ছোট।
He is the strongest boy in the class. | সে ক্লাসের সবচেয়ে শক্তিশালী ছেলে।
Medicine Corner is the biggest medicine shop in Hajiganj Bazar. | মেডিসিন কর্নার হাজীগঞ্জ বাজারের সবচেয়ে বড় ওষুধের দোকান।
It is a famous park. | এটি একটি বিখ্যাত পার্ক।
Cox's Bazar is more famous than my town. | কক্সবাজার আমার শহরের চেয়ে বেশি বিখ্যাত।
My phone is new. | আমার ফোনটা নতুন।
Your phone is newer than mine. | আপনার ফোন আমারটার চেয়ে নতুন।
This room is as big as that one. | এই ঘরটা ওটার মতোই বড়।
Who is the richest man in the world? | পৃথিবীর সবচেয়ে ধনী মানুষ কে?
What is the longest river in Bangladesh? | বাংলাদেশের সবচেয়ে দীর্ঘ নদী কোনটা?
Tea is cheaper than coffee. | চা কফির চেয়ে সস্তা।
English is easier than I thought. | ইংরেজি আমার ভাবনার চেয়ে সহজ।
This is the best day of my life. | এটা আমার জীবনের সেরা দিন।
Dhaka is exciting, but I love Hajiganj. | ঢাকা রোমাঞ্চকর, কিন্তু আমি হাজীগঞ্জকে ভালোবাসি।
""",
dict(title="তুলনা: -er than, the -est",
     points=["ছোট শব্দে: <b>-er than</b> — big → <b>bigger than</b>, quiet → <b>quieter than</b>", "ছোট শব্দে সেরা: <b>the -est</b> — the strongest, the youngest", "লম্বা শব্দে: <b>more … than</b>, <b>the most …</b> — more beautiful, the most famous", "অনিয়মিত: good → better → <b>the best</b>"],
     table=[("big", "bigger / the biggest", "বড় — আরও বড় — সবচেয়ে বড়"), ("beautiful", "more / the most beautiful", "সুন্দর — আরও সুন্দর — সবচেয়ে সুন্দর"), ("good", "better / the best", "ভালো — আরও ভালো — সেরা")],
     quiz=("Dhaka is ___ than Hajiganj.", ["big", "bigger", "the biggest"], 1, "দুটোর তুলনায় -er than: bigger than।")))

# ======================================================================= Day 20
day(20, "My Story", "আমার গল্প ও স্বপ্ন", "আজ ২০ দিনে যা শিখেছেন তা দিয়ে নিজের গল্প বলুন — আর স্বপ্নের কথা।",
"""
My name is Sanjoy Dev Shuvo, and I am from Bangladesh. | আমার নাম সঞ্জয় দেব শুভ, আর আমি বাংলাদেশের।
I live in Hajiganj, Chandpur, with my family. | আমি চাঁদপুরের হাজীগঞ্জে আমার পরিবারের সাথে থাকি।
Twenty days ago, I could speak only a little English. | বিশ দিন আগে আমি খুব অল্প ইংরেজি বলতে পারতাম।
Every day I read a story and learned ten new words. | প্রতিদিন আমি একটি গল্প পড়তাম আর দশটি নতুন শব্দ শিখতাম।
Now I can talk to the customers at Medicine Corner in English. | এখন আমি মেডিসিন কর্নারের ক্রেতাদের সাথে ইংরেজিতে কথা বলতে পারি।
My dream is to speak English with confidence. | আমার স্বপ্ন আত্মবিশ্বাসের সাথে ইংরেজি বলা।
My goal is to get a good job in the future. | আমার লক্ষ্য ভবিষ্যতে একটি ভালো চাকরি পাওয়া।
I am proud of my progress, and I will never stop learning. | আমি আমার অগ্রগতিতে গর্বিত, আর আমি কখনো শেখা থামাব না।
""",
"""
dream | ড্রিম | স্বপ্ন
goal | গোল | লক্ষ্য
job | জব | চাকরি
future | ফিউচার | ভবিষ্যৎ
confident | কনফিডেন্ট | আত্মবিশ্বাসী
proud | প্রাউড | গর্বিত
success | সাকসেস | সাফল্য
improve | ইমপ্রুভ | উন্নতি করা
together | টুগেদার | একসাথে
progress | প্রোগ্রেস | অগ্রগতি
""",
"""
Please introduce yourself. | দয়া করে নিজের পরিচয় দিন।
My name is Sanjoy and I am a graduate. | আমার নাম সঞ্জয় আর আমি একজন গ্র্যাজুয়েট।
I live in Hajiganj, Chandpur. | আমি চাঁদপুরের হাজীগঞ্জে থাকি।
I have a small and happy family. | আমার একটি ছোট আর সুখী পরিবার আছে।
I wake up at six every morning. | আমি প্রতিদিন সকালে ছয়টায় উঠি।
Yesterday I studied English for one hour. | গতকাল আমি এক ঘণ্টা ইংরেজি পড়েছি।
I work at Medicine Corner in Hajiganj Bazar. | আমি হাজীগঞ্জ বাজারের মেডিসিন কর্নারে কাজ করি।
I am going to visit my grandmother soon. | আমি শিগগিরই আমার দাদির সাথে দেখা করতে যাব।
I can speak English better now. | আমি এখন আগের চেয়ে ভালো ইংরেজি বলতে পারি।
My English is improving every day. | আমার ইংরেজি প্রতিদিন উন্নতি করছে।
What is your dream? | আপনার স্বপ্ন কী?
My dream is to travel the world. | আমার স্বপ্ন পৃথিবী ঘুরে দেখা।
My goal is to get a good job. | আমার লক্ষ্য একটি ভালো চাকরি পাওয়া।
I want to be confident when I speak. | আমি কথা বলার সময় আত্মবিশ্বাসী হতে চাই।
Success needs practice and patience. | সাফল্যের জন্য অনুশীলন আর ধৈর্য দরকার।
We learn better together. | আমরা একসাথে ভালো শিখি।
Thank you for teaching me. | আমাকে শেখানোর জন্য ধন্যবাদ।
I am proud of myself. | আমি নিজের জন্য গর্বিত।
I will never stop learning. | আমি কখনো শেখা থামাব না।
See you in English 102! | English 102-তে দেখা হবে!
""",
dict(title="চার সময় এক নজরে",
     points=["<b>Present</b> — রোজকার কাজ: I study every day.", "<b>Past</b> — যা শেষ হয়েছে: I studied yesterday.", "<b>Future</b> — যা হবে: I will study tomorrow. · I am going to study.", "<b>Continuous</b> — এখন হচ্ছে: I am studying now."],
     table=[("Present", "I study", "আমি পড়ি"), ("Past", "I studied", "আমি পড়েছিলাম"), ("Future", "I will study", "আমি পড়ব"), ("Continuous", "I am studying", "আমি পড়ছি")],
     quiz=("Yesterday I ___ English for one hour.", ["study", "studied", "will study"], 1, "গতকাল = অতীত: studied।")))

assert len(DAYS) == 20
for d in DAYS:
    assert len(d["story"]) == 8, (d["n"], "story", len(d["story"]))
    assert len(d["words"]) == 10, (d["n"], "words", len(d["words"]))
    assert len(d["sentences"]) == 20, (d["n"], "sentences", len(d["sentences"]))
# every taught word is new: no word repeats across the whole course
_seen = {}
for d in DAYS:
    for w, _, _ in d["words"]:
        k = w.lower()
        assert k not in _seen, f"word '{w}' on day {d['n']} was already taught on day {_seen[k]}"
        _seen[k] = d["n"]
