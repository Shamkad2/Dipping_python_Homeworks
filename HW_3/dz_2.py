# 3. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.



text = "'Война и мир', 1863 год"\
        "На краю дороги стоял дуб. Вероятно, в десять раз старше берёз, составлявших лес, он был в десять раз толще и в два раза выше каждой берёзы. " \
       "Это был огромный в два обхвата дуб с обломанными, давно видно, суками и с обломанной корой, заросшей старыми болячками. " \
       "С огромными своими неуклюжими, несимметрично - растопыренными, корявыми руками и пальцами, он старым, сердитым и презрительным уродом стоял между " \
       "улыбающимися берёзами. Только он один не хотел подчиняться обаянию весны и не хотел видеть ни весны, ни солнца.«Весна, и любовь, и счастие!» – " \
       "как будто говорил этот дуб, – «и как не надоест вам всё один и тот же глупый и бессмысленный обман. Всё одно и то же, и всё обман! Нет ни весны, " \
       "ни солнца, ни счастия. Вон смотрите, сидят задавленные мёртвые ели, всегда одинакие, и вон и я растопырил свои обломанные, ободранные пальцы, где " \
       "ни выросли они – из спины, из боков; как выросли – так и стою, и не верю вашим надеждам и обманам».Князь Андрей несколько раз оглянулся на этот дуб, " \
       "проезжая по лесу, как будто он чего-то ждал от него. Цветы и трава были и под дубом, но он всё так же, хмурясь, неподвижно, уродливо и упорно, стоял " \
       "посреди их. «Да, он прав, тысячу раз прав этот дуб, думал князь Андрей, пускай другие, молодые, вновь поддаются на этот обман, а мы знаем жизнь, – " \
       "наша жизнь кончена!» Целый новый ряд мыслей безнадёжных, но грустно-приятных в связи с этим дубом, возник в душе князя Андрея." \
       "Во время этого путешествия он как будто вновь обдумал всю свою жизнь, и пришёл к тому же прежнему успокоительному и безнадёжному заключению, что " \
       "ему начинать ничего было не надо, что он должен доживать свою жизнь, не делая зла, не тревожась и ничего не желая. "

my_dict = {}
text_list = text.lower().split()
text_list_new = [''.join(filter(str.isalpha, a)) for a in text_list]    # убираем все ненужное: символы, цифры, оставляя только слова

while '' in text_list_new:
    text_list_new.remove('')

for word in text_list_new:
    my_dict.setdefault(word, text_list_new.count(word))

num_words = 1
while num_words <= 10:
    num_words += 1
    max_key = max(my_dict,  key=my_dict.get)
    print(f'{max_key:>5}  =  {my_dict[max_key]}')
    my_dict.pop(max_key)