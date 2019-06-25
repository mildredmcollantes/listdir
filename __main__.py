import os, sys
import argparse
import csv


def main(options):
    output = options.name
    # print(output)
    for roots, dirs, files in os.walk(options.dir):
        for file in files:
            with open(output, 'a') as f:
                filepath = os.path.join(roots, file)
                filesize = _get_fileSize(filepath)
                csv_writer(f, roots, file, filesize)


def _get_fileSize(file):
    return os.path.getsize(file)


def csv_writer(csvfile, filepath, sha1, filesize):
    try:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([filepath] + [sha1] + [filesize])
    except Exception as ex:
        print(ex)


def _get_args():
    parser = None
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("dir", help="input directory")
        parser.add_argument("name",  help="filename of output file")
    except Exception as ex:
        print("[ERROR] Problem in getting options: {}".format(ex))
    finally:
        return parser


if __name__ == "__main__":
    options = (_get_args()).parse_args()
    if options:
        main(options)