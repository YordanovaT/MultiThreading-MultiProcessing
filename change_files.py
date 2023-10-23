""" Using threads to change text files """

from threading import Thread
from time import perf_counter


def replace_str(filename, substr, new_substr):
    print(f'Processing the file {filename}')
    # get the contents of the file
    with open(filename, 'r') as f:
        content = f.read()

    # replace the substr by new_substr
    content = content.replace(substr, new_substr)

    # write data into the file
    with open(filename, 'w') as f:
        f.write(content)


def main():
    filenames = [
        'Path-to-your-text-file/test1.txt',
        'Path-to-your-text-file/test2.txt',
        'Path-to-your-text-file/test3.txt',
    ]  # you can create and use as many .txt files as you want

    # create threads and use them to change the text files
    threads = [Thread(target=replace_str, args=(filename, 'IDs', 'ID')) for filename in filenames]

    # start the threads
    for thread in threads:
        thread.start()

    # wait for the threads to complete
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    start_time = perf_counter()

    main()

    end_time = perf_counter()
    print(f'It took {end_time- start_time :0.3f} second(s) to complete.')
