from PIL import Image
import os
import random
import string
import json



#After importing the necessary packages,
## This is where I will be storing the finished product on my computer

finished_path = r"C:\Users\mikep\PycharmProjects\pythonProject1\finished"

#  This is where I have all the image pieces stored.

back_path =  r"C:\Users\mikep\PycharmProjects\pythonProject1\1 Backgrounds"
weapon_path = r"C:\Users\mikep\PycharmProjects\pythonProject1\2 Weapons"
shirt_path = r"C:\Users\mikep\PycharmProjects\pythonProject1\3 Shirt"
acc_path = r"C:\Users\mikep\PycharmProjects\pythonProject1\4 Accessories 1"
face_path = r"C:\Users\mikep\PycharmProjects\pythonProject1\5 Face"
mouth_path = r"C:\Users\mikep\PycharmProjects\pythonProject1\6 Mouth"
eye_path = r"C:\Users\mikep\PycharmProjects\pythonProject1\7 Eyes"
ear_path = r"C:\Users\mikep\PycharmProjects\pythonProject1\8 Earring"
mark_path = r"C:\Users\mikep\PycharmProjects\pythonProject1\9 Face Marking"
hat_path = r"C:\Users\mikep\PycharmProjects\pythonProject1\10 Hat"
spec_one_path = r"C:\Users\mikep\PycharmProjects\pythonProject1\Special 1"
spec_two_path = r"C:\Users\mikep\PycharmProjects\pythonProject1\Special 2"


#Now I create the data storing variables


list_of_substrings = []
backgrounds = []
weapons = []
shirts = []
accessories = []
faces = []
mouths = []
eyes = []
earrings = []
face_markings = []
hats = []
specials_one = []
specials_two = []




chosenback = ''
chosenwep = ''
chosenshirt = ''
chosenacc = ''
chosenface = ''
chosenmouth = ''
choseneyes = ''
chosenears = ''
chosenmark = ''
chosenhat = ''
chosenone = ''
chosentwo = ''



baseback = []
basewep = []
baseshirt = []
baseacc = []
baseface = []
basemouth = []
baseeyes = []
baseear = []
basemark = []
basehats = []
baseone = []
basetwo = []



names = []
maulist = []



#Here, I define the functions I will be using.
#random_char creates a random string of characters for a range to be determined later on.


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

#validate file contents will check if two files are the same.


def validate_file_contents(file1, file2):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        contents1 = f1.read()
        contents2 = f2.read()
    return contents1 == contents2


#This will show what items are in a file and append the filenames to a list.
def list_dir(dir, list, list_of_substrings):
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        list.append(os.path.abspath(os.path.join(dir, fileName)))
        list_of_substrings.append(fileName)


#This does the same for the location the program is being run in.
def list_dirs(dir, list):
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        list.append(os.path.abspath(os.path.join(dir, fileName)))


#Here, I use the list_dir function to load all of the image file names into a list of strings.

list_dir(back_path, backgrounds, baseback)
list_dir(weapon_path, weapons, basewep)
list_dir(shirt_path, shirts, baseshirt)
list_dir(acc_path, accessories, baseacc)
list_dir(face_path, faces, baseface)
list_dir(mouth_path, mouths, basemouth)
list_dir(eye_path, eyes, baseeyes)
list_dir(ear_path, earrings, baseear)
list_dir(mark_path, face_markings, basemark)
list_dir(hat_path, hats, basehats)
list_dir(spec_one_path, specials_one, baseone)
list_dir(spec_two_path, specials_two, basetwo)

#Here I initiate an index for a while loop to increment.  I have chosen 10 for the purposes
# of saving time.  But this generator with these image files has the capacity to
# create well over 10,000 unique images.

i = 1
while i <= 10:

    breaker = False


#Determining rarity
    one = (random.choices(backgrounds, weights=(20, 3, .4, .6, 20, 20, 7, 15, 13, 9, 1, 8, 4, 3, 5))[0])
    two = (random.choices(weapons, weights=(10, 60, 3, 15, 12, 7, 10, 10))[0])
    three = (random.choices(shirts, weights=(
    12, 12, 12, 12, 12, 12, 50, 39, 32, 60, 25, 25, 25, 25, 25, 25, 39, 35, 25, 25, 25, 25, 25, 25, 35, 33, 26, 20, 20,
    20, 20, 20, 20))[0])
    four = (random.choices(accessories, weights=(4, 90, 1, 12))[0])
    five = (random.choices(faces, weights=(3, 75, 80, 65, 38, 14))[0])
    six = (random.choices(mouths, weights=(0.00001, 2, 6.66, 28, 55, 69, 50, 25, 20))[0])
    seven = (random.choices(eyes, weights=(0.00001, 8, 8, 55, 6, 4, 3, 12))[0])
    eight = (random.choices(earrings, weights=(60, 3, 9, 7, 8, 15, 17, 20))[0])
    nine = (random.choices(face_markings, weights=(33, 26, 88, 40, 28, 26, 40))[0])
    ten = (random.choices(hats, weights=(
    15, 15, 40, 10, 19, 20, 3, 11, 8, 8, 6, 23, 20, 3, 15, 1, 2, 8, 8, 3, 17, 1, 4, 7))[0])
    eleven = (random.choices(specials_one, weights=(93, 6, 4, 5))[0])
    twelve = (random.choices(specials_two, weights=(80, 6, 8, 7, 5, 17, 2, 6, 22, 18, 6))[0])

#making sure that certain combinations where the images would overlap does not happen
    if twelve == r'{}\{}'.format(spec_two_path, 'Knight Helmet.png'):
        six = r'{}\{}'.format(mouth_path, 'Blank.png')
        seven = r'{}\{}'.format(eye_path, 'Blank.png')
        five = r'{}\{}'.format(face_path, 'Blank.png')


    if ten == r'{}\{}'.format(hat_path, 'Pumpins Evil Mask.png'):
        six = r'{}\{}'.format(mouth_path, 'Blank.png')
        seven = r'{}\{}'.format(eye_path, 'Blank.png')
        nine = r'{}\{}'.format(mark_path, 'Blank.png')

    if ten == r'{}\{}'.format(hat_path, 'Pumpins Happy Mask.png'):
        six = r'{}\{}'.format(mouth_path, 'Blank.png')
        seven = r'{}\{}'.format(eye_path, 'Blank.png')
        nine = r'{}\{}'.format(mark_path, 'Blank.png')



    if seven == r'{}\{}'.format(eye_path, 'Cyclops Eye.png') and ten == r'{}\{}'.format(hat_path, 'Mom Tattoo Special.png'):
        continue
    elif seven == r'{}\{}'.format(eye_path, 'Cyclops Eye.png') and ten == r'{}\{}'.format(hat_path, 'Heart Tattoo.png'):
        continue
    if twelve == r'{}\{}'.format(spec_two_path, 'Knight Helmet.png') and nine != r'{}\{}'.format(mark_path, 'Blank.png'):
        continue
    if twelve == r'{}\{}'.format(spec_two_path, 'Knight Helmet.png') and ten != r'{}\{}'.format(hat_path, 'Blank.png'):
        continue
    if twelve == r'{}\{}'.format(spec_two_path, 'Knight Helmet.png') and eight != r'{}\{}'.format(ear_path, 'Blank.png'):
        continue
    if two == r'{}\{}'.format(weapon_path, 'Guitar.png') and four == r'{}\{}'.format(acc_path, 'Balloon.png'):
        continue
    if ten == r'{}\{}'.format(hat_path, 'Crown.png') and twelve == r'{}\{}'.format(spec_two_path, 'Halo.png'):
        continue
    if ten == r'{}\{}'.format(hat_path, 'Crown.png') and twelve == r'{}\{}'.format(spec_two_path, 'Knight Helmet.png'):
        continue
    if ten == r'{}\{}'.format(hat_path, 'Crown.png') and twelve == r'{}\{}'.format(spec_two_path, 'Red Potion.png'):
        continue
    if ten == r'{}\{}'.format(hat_path, 'Crown.png') and twelve == r'{}\{}'.format(spec_two_path, 'Blue Potion.png'):
        continue
    if ten == r'{}\{}'.format(hat_path, 'Crown.png') and twelve == r'{}\{}'.format(spec_two_path, 'Fairy.png'):
        continue
    if ten == r'{}\{}'.format(hat_path, 'Pumpins Evil Mask.png') and nine != r'{}\{}'.format(mark_path, 'Blank.png'):
        continue
    if ten == r'{}\{}'.format(hat_path, 'Pumpins Happy Mask.png') and nine != r'{}\{}'.format(mark_path, 'Blank.png'):
        continue
    if seven == r'{}\{}'.format(eye_path, 'Hypnotized Eyes.png') and ten == r'{}\{}'.format(hat_path, 'Heart Tattoo.png'):
        continue
    if seven == r'{}\{}'.format(eye_path, 'Hypnotized Eyes.png') and ten == r'{}\{}'.format(hat_path, 'Mom Tattoo Special.png'):
        continue
    if seven == r'{}\{}'.format(eye_path, 'Hypnotized Eyes.png') and nine == r'{}\{}'.format(mark_path, 'Scar.png'):
        continue
    if seven == r'{}\{}'.format(eye_path, 'Possessed Eyes.png') and nine == r'{}\{}'.format(mark_path, 'Scar.png'):
        continue
    if seven == r'{}\{}'.format(eye_path, 'Red Circle Eyes.png') and nine == r'{}\{}'.format(mark_path, 'Scar.png'):
        continue
    if ten == r'{}\{}'.format(hat_path, 'UFO.png') and twelve == r'{}\{}'.format(spec_two_path, 'Halo.png'):
        continue
    if seven == r'{}\{}'.format(eye_path, 'Cyclops Eye.png') and ten == r'{}\{}'.format(hat_path, 'Horn.png'):
        continue




    ##populate the base attributes for the json file

    for c in baseback:
        if c in one:
            chosenback = c.rsplit(' 3', 1)[0]
            break

    for c in basewep:
        if c in two:
            chosenwep = c.rsplit('.', 1)[0]
            break


    for c in baseshirt:
        if c in three:
            chosenshirt = c.rsplit('.', 1)[0]
            break


    for c in baseacc:
        if c in four:
            chosenacc = c.rsplit('.', 1)[0]
            break


    for c in baseface:
        if c in five:
            chosenface = c.rsplit('.', 1)[0]
            break


    for c in basemouth:
        if c in six:
            chosenmouth = c.rsplit('.', 1)[0]
            break


    for c in baseeyes:
        if c in seven:
            choseneyes = c.rsplit('.', 1)[0]
            break


    for c in baseear:
        if c in eight:
            chosenears = c.rsplit('.', 1)[0]
            break


    for c in basemark:
        if c in nine:
            chosenmark = c.rsplit('.', 1)[0]
            break


    for c in basehats:
        if c in ten:
            chosenhat = c.rsplit('.', 1)[0]
            break


    for c in baseone:
        if c in eleven:
            chosenone = c.rsplit('.', 1)[0]
            break


    for c in basetwo:
        if c in twelve:
            chosentwo = c.rsplit('.', 1)[0]
            break



    attributes = {'background': chosenback, 'weapon': chosenwep, 'shirt': chosenshirt, 'accessories': chosenacc,
                  'faces': chosenface, 'mouths': chosenmouth, 'eyes': choseneyes, 'earrings': chosenears, 'faces markings': chosenmark,
                  'hats': chosenhat, 'specials one': chosenone, 'specials two': chosentwo}


#Here I use the textual attributes data to ensure that no duplicates are created.

    if attributes in maulist:
        breaker = True
        print('The program found a duplicate, but will continue without saving the duplicate.')
    else:
        maulist.append(attributes)

    if breaker == True:
        continue


#Now I put the images together, and name them with a unique filename.
    one = Image.open(one)
    two = Image.open(two)
    three = Image.open(three)
    four = Image.open(four)
    five = Image.open(five)
    six = Image.open(six)
    seven = Image.open(seven)
    eight = Image.open(eight)
    nine = Image.open(nine)
    ten = Image.open(ten)
    eleven = Image.open(eleven)
    twelve = Image.open(twelve)

    one = Image.alpha_composite(one, two)
    three = Image.alpha_composite(three, four)
    five = Image.alpha_composite(five, six)
    seven = Image.alpha_composite(seven, eight)
    nine = Image.alpha_composite(nine, ten)
    eleven = Image.alpha_composite(eleven, twelve)

    game = Image.alpha_composite(one, three)
    set = Image.alpha_composite(five, seven)
    match = Image.alpha_composite(nine, eleven)

    almost = Image.alpha_composite(game, set)
    there = Image.alpha_composite(almost, match)
    name = random_char(10) + str(random.randint(1, 9))
    while name in names:
        name = random_char(10) + str(random.randint(1, 9))
    name_file = name + '.png'
    name_path = '{}\{}'.format(finished_path, name_file)

    there = there.save(name_file)
    names.append(name_file)


#Now that I have saved the unique image with a unique name into a png file, I save the attributes into a json file.

    with open(name + '.json', 'w') as outfile:
        json.dump(attributes, outfile)


    print(i)
    i += 1













