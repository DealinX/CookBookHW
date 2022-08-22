def creating_result():
    all_texts = [len(list(open(f'{i}.txt', encoding='utf-8').readlines())) for i in range(1, 4)]
    texts_dict = {'1.txt': all_texts[0], '2.txt': all_texts[1], '3.txt': all_texts[2]}
    key_list = list(texts_dict.keys())
    value_list = list(texts_dict.values())

    with open('result.txt','a', encoding='utf-8')as result:
        for text in range(len(all_texts)):
            pos = value_list.index(sorted(all_texts)[text])
            result.write(key_list[pos]+'\n')
            result.write(str(sorted(all_texts)[text])+'\n')
            result.write(''.join(line for line in open(key_list[pos], encoding='utf-8'))+'\n')


creating_result()
