from sys import argv, exit
import os

try:
    import lz4.block as lz4
except ImportError:
    print("Please install lz4 via   'pip install lz4'.")


EXTENSIONS = {"1": ".lz4", "2": ".mozlz4", "3": ".jsonlz4", "4": ".baklz4"}



def check_overwrite(path):
    if os.path.exists(path):
        i = input(f"File {path} already exists. Overwrite? y/n\n")
        if i.lower() == "y":
            print("Overwriting file.")
            return True
        else:
            print("Exiting.")
            exit(1)
    else:
        return True


def print_info():
    print(f"Usage: {argv[0]} <infile>")
    print("Decompress Mozilla-LZ4 encoded <infile> or compress <infile> to Mozilla-LZ4.")
    print("Output file will be put in same folder as input file.")
    exit(1)


def choose_ext():
    print(f"Please choose file extension:")
    for k, v in EXTENSIONS.items():
        print(f"{k}: {v}")
    if (i := input()) in EXTENSIONS.keys():
        return EXTENSIONS[i]
    else:
        print("Invalid extension.\nExiting")
        exit(1)


def main():
    if len(argv) != 2:
        print_info()

    else:
        if not os.path.exists(argv[1]):
            print_info()
        else:
            in_full_name = os.path.basename(argv[1])
            in_folder_path = os.path.dirname(argv[1])
            in_name, in_ext = os.path.splitext(argv[1])  # "search.json", ".mozlz4"
            in_file_handle = open(argv[1], "rb")

            if in_ext.lower() in EXTENSIONS.values():
                ''' Decompress '''
                print(f"Trying to decompress {in_full_name}")
                out_file = os.path.join(in_folder_path, f"{in_name}")
                if check_overwrite(out_file):
                    with open(out_file, "wb") as f:
                        assert in_file_handle.read(8) == b"mozLz40\0"
                        f.write(lz4.decompress(in_file_handle.read()))

            else:
                ''' Compress '''
                print(f"Trying to compress {in_full_name}")
                ext = choose_ext()
                out_file = os.path.join(in_folder_path, f"{in_full_name}{ext}")
                if check_overwrite(out_file):
                    with open(out_file, "wb") as f:
                        f.write(b"mozLz40\0" + lz4.compress(in_file_handle.read()))


if __name__ == '__main__':
    main()
