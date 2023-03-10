# user text is talk about A P J kalam

text = input("Enter a text\n").lower()
find_text = text.find("abdul")
find_text2 = text.find("kalam")
find_text3 = text.find("apj")
find_text4 = text.find("a.p.j.")

if find_text != -1 or find_text2 != -1 or find_text3 != -1 or find_text4 != -1:
    print("Title is A.P.J. Abdul Kalam")
else:
    print("Title not found")