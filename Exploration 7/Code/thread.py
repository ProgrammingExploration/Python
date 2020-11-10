import threading


def init_thread():
    print("Om")


for i in range(5):
    t = threading.Thread(target=init_thread)
    t.start()

# Not Much Different
for i in range(5):
    print("Om")
