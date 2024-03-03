import multiprocessing

def spawn():
    print('Spawned')

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=spawn)
        p.start()
        p.join()