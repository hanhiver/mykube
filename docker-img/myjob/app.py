from time import sleep
import sys

def main():
    sleep_time = 10
    
    if len(sys.argv) > 1:
        sleep_time = int(sys.argv[1])

    for i in range(sleep_time):
        print('Sleep {} second, {} seconds left.'.format(sleep_time, sleep_time - i))
        sleep(1)

    print('Job Done!')

if __name__ == '__main__':
    main()


