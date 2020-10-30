import os, sys, random, time, json
from dhooks import Webhook, File

with open('config.json', 'r') as handle:
    config = json.load(handle)

interval = (config["interval"])
hook = Webhook((config["webhook"]))
loop = (config["loop"])
path = "./images"

if not os.path.exists('./images'):
    try:
        os.mkdir('./images')
    except OSError:
        print ('Creation of the directory {} failed').format(path))
    else:
        print('Successfully created the directory {}'.format(path))
    
def forever():
    print ("Sending images every " + str(interval) + " seconds.")
    while True:
        try:
            file = random.choice(os.listdir("./images"))
        except Exception:
            print ("There are no files in the images folder. Please add some.")
            time.sleep(5)
            sys.exit()
        print (file)
        file = File("./images/" + str(file))
        hook.send(file=file)
        time.sleep(int(interval))

def notforever():
    print ("Sending " + str(loop) + " images every " + str(interval) + " seconds.")
    for x in range(int(loop)):
        try:
            file = random.choice(os.listdir(".\\images\\"))
        except Exception:
            print ("There are no files in the images folder. Please add some.")
            time.sleep(5)
            sys.exit()
        print (file)
        file = File(".\\images\\" + str(file))
        hook.send(file=file)
        time.sleep(int(interval))

if loop == "forever":
    forever()
else:
    notforever()
