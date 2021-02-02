# config:utf-8
import random
def randomName():
    name = ["itou", "watanabe", "yamamoto", "nakamura", "kobayashi", "yoshida", "sasaki", "matumoto", "inoue", "kimura", "hayashi", "saitou", "simizu", "yamazaki", "mori", "ikeda", "hashimoto", "okada", "fujita", "gotou"]
    return random.choice(name)
def randomGender():
    return random.choice(["man", "woman"])
def randomHobby():
    hobby = ["music", "karaoke", "anime", "kabuki", "yoga", "onsen", "tera", "ba-", "powerspot", "zoo", "animal", "caffe", "running", "shopping", "soccer", "sea", "igo", "diy", "cooking", "osero", "interia", "eat", "tv"]
    return random.choice(hobby)
OUTPUT_FILE = "TestData.sql"
RECORD_COUNT = 1000000
sqlCommands = ""
for _ in range(RECORD_COUNT):
    name = randomName()
    gender = randomGender()
    hobby = randomHobby()
    sqlCommands += "insert into people " \
                   "(name, gender, hobby)" \
                   "values ('{}', '{}', '{}');\n" \
                   .format(name, gender, hobby)
f = open(OUTPUT_FILE, 'w')
f.write(sqlCommands)
f.close()
