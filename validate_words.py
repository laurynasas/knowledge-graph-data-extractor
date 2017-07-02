file = open("related_words_2.txt", "r")
file_new = open("related_words_2_sifted.txt", "w")
content = file.readlines()

words = ["actor", "actress", "film", "leader", "team", "comedian", "painter", "photographer", "writer", "novelist", "president",
         "company", "song", "album", "university", "king", "princess", "novel", "businessman", "author", "engineer", "philosopher",
         "preacher", "president"]
for line in content:
    passed = True
    for word in words:
        if word in line.replace("\n","").lower():
            print word, line.replace("\n", "")
            passed = False
            break
    if passed:
        file_new.write(line)



