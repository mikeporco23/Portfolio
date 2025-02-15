from PIL import Image
import os
import random
import string
import json

# Paths
finished_path = r"C:\Users\mikep\PycharmProjects\pythonProject1\finished"
back_path = r"C:\Users\mikep\PycharmProjects\pythonProject1\1 Backgrounds"
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

# Data storing variables
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

# Functions
def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

def list_dir(dir, list, list_of_substrings):
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        list.append(os.path.abspath(os.path.join(dir, fileName)))
        list_of_substrings.append(fileName)

# Load image file names
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

# Generate unique images
i = 1
while i <= 10:
    breaker = False

    try:
        # Randomly choose images with weights
        one = random.choices(backgrounds, weights=(20, 3, 0.4, 0.6, 20, 20, 7, 15, 13, 9, 1, 8, 4, 3, 5))[0]
        two = random.choices(weapons, weights=(10, 60, 3, 15, 12, 7, 10, 10))[0]
        three = random.choices(shirts, weights=(12, 12, 12, 12, 12, 12, 50, 39, 32, 60, 25, 25, 25, 25, 25, 25, 39, 35, 25, 25, 25, 25, 25, 25, 35, 33, 26, 20, 20, 20, 20, 20, 20))[0]
        four = random.choices(accessories, weights=(4, 90, 1, 12))[0]
        five = random.choices(faces, weights=(3, 75, 80, 65, 38, 14))[0]
        six = random.choices(mouths, weights=(0.00001, 2, 6.66, 28, 55, 69, 50, 25, 20))[0]
        seven = random.choices(eyes, weights=(0.00001, 8, 8, 55, 6, 4, 3, 12))[0]
        eight = random.choices(earrings, weights=(60, 3, 9, 7, 8, 15, 17, 20))[0]
        nine = random.choices(face_markings, weights=(33, 26, 88, 40, 28, 26, 40))[0]
        ten = random.choices(hats, weights=(15, 15, 40, 10, 19, 20, 3, 11, 8, 8, 6, 23, 20, 3, 15, 1, 2, 8, 8, 3, 17, 1, 4, 7))[0]
        eleven = random.choices(specials_one, weights=(93, 6, 4, 5))[0]
        twelve = random.choices(specials_two, weights=(80, 6, 8, 7, 5, 17, 2, 6, 22, 18, 6))[0]

        # Ensure no overlapping images
        if twelve == os.path.join(spec_two_path, 'Knight Helmet.png'):
            six = os.path.join(mouth_path, 'Blank.png')
            seven = os.path.join(eye_path, 'Blank.png')
            five = os.path.join(face_path, 'Blank.png')

        if ten in [os.path.join(hat_path, 'Pumpins Evil Mask.png'), os.path.join(hat_path, 'Pumpins Happy Mask.png')]:
            six = os.path.join(mouth_path, 'Blank.png')
            seven = os.path.join(eye_path, 'Blank.png')
            nine = os.path.join(mark_path, 'Blank.png')

        if (seven == os.path.join(eye_path, 'Cyclops Eye.png') and
           ten in [os.path.join(hat_path, 'Mom Tattoo Special.png'), os.path.join(hat_path, 'Heart Tattoo.png')]):
            continue

        if twelve == os.path.join(spec_two_path, 'Knight Helmet.png') and nine != os.path.join(mark_path, 'Blank.png'):
            continue
        if twelve == os.path.join(spec_two_path, 'Knight Helmet.png') and ten != os.path.join(hat_path, 'Blank.png'):
            continue
        if twelve == os.path.join(spec_two_path, 'Knight Helmet.png') and eight != os.path.join(ear_path, 'Blank.png'):
            continue
        if two == os.path.join(weapon_path, 'Guitar.png') and four == os.path.join(acc_path, 'Balloon.png'):
            continue
        if ten == os.path.join(hat_path, 'Crown.png') and twelve in [os.path.join(spec_two_path, 'Halo.png'),
                                                                     os.path.join(spec_two_path, 'Knight Helmet.png'),
                                                                     os.path.join(spec_two_path, 'Red Potion.png'),
                                                                     os.path.join(spec_two_path, 'Blue Potion.png'),
                                                                     os.path.join(spec_two_path, 'Fairy.png')]:
            continue

        if ten in [os.path.join(hat_path, 'Pumpins Evil Mask.png'), os.path.join(hat_path, 'Pumpins Happy Mask.png')] and nine != os.path.join(mark_path, 'Blank.png'):
            continue

        if (seven in [os.path.join(eye_path, 'Hypnotized Eyes.png'), os.path.join(eye_path, 'Possessed Eyes.png'), os.path.join(eye_path, 'Red Circle Eyes.png')]
           and nine == os.path.join(mark_path, 'Scar.png')):
            continue

        if ten == os.path.join(hat_path, 'UFO.png') and twelve == os.path.join(spec_two_path, 'Halo.png'):
            continue

        if seven == os.path.join(eye_path, 'Cyclops Eye.png') and ten == os.path.join(hat_path, 'Horn.png'):
            continue

        # Populate attributes for JSON
        chosenback = next((c.rsplit(' 3', 1)[0] for c in baseback if c in one), '')
        chosenwep = next((c.rsplit('.', 1)[0] for c in basewep if c in two), '')
        chosenshirt = next((c.rsplit('.', 1)[0] for c in baseshirt if c in three), '')
        chosenacc = next((c.rsplit('.', 1)[0] for c in baseacc if c in four), '')
        chosenface = next((c.rsplit('.', 1)[0] for c in baseface if c in five), '')
        chosenmouth = next((c.rsplit('.', 1)[0] for c in basemouth if c in six), '')
        choseneyes = next((c.rsplit('.', 1)[0] for c in baseeyes if c in seven), '')
        chosenears = next((c.rsplit('.', 1)[0] for c in baseear if c in eight), '')
        chosenmark = next((c.rsplit('.', 1)[0] for c in basemark if c in nine), '')
        chosenhat = next((c.rsplit('.', 1)[0] for c in basehats if c in ten), '')
        chosenone = next((c.rsplit('.', 1)[0] for c in baseone if c in eleven), '')
        chosentwo = next((c.rsplit('.', 1)[0] for c in basetwo if c in twelve), '')

        attributes = {
            'background': chosenback, 'weapon': chosenwep, 'shirt': chosenshirt, 'accessories': chosenacc,
            'faces': chosenface, 'mouths': chosenmouth, 'eyes': choseneyes, 'earrings': chosenears, 'face markings': chosenmark,
            'hats': chosenhat, 'specials one': chosenone, 'specials two': chosentwo
        }

        # Check for duplicates
        if attributes in maulist:
            print('The program found a duplicate, but will continue without saving the duplicate.')
            continue
        else:
            maulist.append(attributes)

        # Composite images
        images = [Image.open(img) for img in [one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve]]
        composite = images[0]
        for img in images[1:]:
            composite = Image.alpha_composite(composite, img)

        # Save image
        name = random_char(10) + str(random.randint(1, 9))
        while name in names:
            name = random_char(10) + str(random.randint(1, 9))
        name_file = name + '.png'
        name_path = os.path.join(finished_path, name_file)

        composite.save(name_path)
        names.append(name_file)

        # Save attributes to JSON
        with open(os.path.join(finished_path, name + '.json'), 'w') as outfile:
            json.dump(attributes, outfile)

        print(i)
        i += 1

    except Exception as e:
        print(f"Error occurred: {e}")
        continue
