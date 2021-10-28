import sys
import os
import hashlib


def remove_duplicates(dir):
    count = 0
    dup_count = 0
    unique = set()
    for filename in os.listdir(dir):
        if os.path.isfile(dir + filename):
            filehash = hashlib.md5(open(dir + filename, 'rb').read()).hexdigest()
            count += 1
            if filehash not in unique:
                unique.add(filehash)
            else:
                # os.remove(dir + filename)
                print(f'Duplicate found and removed: {dir + filename}')
                dup_count += 1
    print(f'Scan complete. {dup_count}/{count} duplicates found...')


# enter path to folder containing possible duplicate photos:
photos_path = ""
remove_duplicates(photos_path)
