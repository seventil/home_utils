import argparse
import os
from PIL import Image

MAX_VALUE_OF_LESSER_SIDE = 1200
IMAGE_FILE_FORMATS = ['jpg', 'jpeg', 'png']


def process_images(directory, files: list, convert: bool):

    for file in files:
        input_file = os.path.join(directory, file)
        file_extention = file.split('.')[-1]

        print(f'processing {input_file}')

        if file_extention != 'jpg' and not convert:
            continue

        try:
            with Image.open(input_file).convert('RGB') as img:
                height = img.size[0]
                width = img.size[1]
                max_size = 1600
                wpercent = (max_size / float(max(img.size)))

                if wpercent >= 1:
                    continue

                print(f'resizing {file} from height {height}'
                      f' and width {width}')
                hsize = int((height * float(wpercent)))
                wsize = int((width * float(wpercent)))

                img = img.resize((hsize, wsize), Image.ANTIALIAS)
                img.save(input_file)
        except OSError:
            print('failed smt')


def filter_image_files(files: list):
    filtered_files = []
    for file in files:
        if file.split(".")[-1].lower() in IMAGE_FILE_FORMATS:
            filtered_files.append(file)

    return filtered_files


def get_dirs_and_files(first_dir, recursive):
    '''Returns dict, where key is directory full path and values is the list
    of files (images) that are to be processed'''
    content = {}

    for root, _, files in os.walk(first_dir):
        content[root] = filter_image_files(files)

    if not recursive:
        return {first_dir: content.get(first_dir)}
    return content


def parse_args(args):
    parser = argparse.ArgumentParser(
        description='Process input dir and formats')
    parser.add_argument(
        '--input_dir',
        '-id',
        help='full path to the directory which requeres change')
    parser.add_argument('--recursive', '-r', action='store_true',
                        help='if images search needs to be recursive')
    parser.add_argument('--convert', '-c', action='store_true',
                        help='sum the integers (default: find the max)')

    return parser.parse_args(args)


def main():
    # args = parse_args(sys.argv[1:])
    args = parse_args(['-id',
                       'D:\\Images\\60. Dopaminetrash\\',
                       '-r',
                       '-c'])

    dirs_to_process = get_dirs_and_files(args.input_dir, args.recursive)

    for directory, files in dirs_to_process.items():
        process_images(directory, files, args.convert)


if __name__ == "__main__":
    main()
