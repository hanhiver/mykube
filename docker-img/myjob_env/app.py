from time import sleep
import os

def main():
    sleep_time = 10
    
    if 'INTERVAL' in os.environ:
        sleep_time = int(os.environ['INTERVAL'])

    for i in range(sleep_time):
        print('Sleep {} second, {} seconds left.'.format(sleep_time, sleep_time - i))
        sleep(1)

    print('Job Done!')

if __name__ == '__main__':
    main()


