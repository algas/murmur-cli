import sys
import mmh3

def get_hash(data, seed=None):
    if seed is None:
        return mmh3.hash(data)
    return mmh3.hash(data, seed, signed=False)

def main(args):
    if len(args) > 1:
        return get_hash(args[0], int(args[1]))
    return get_hash(args[0])


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 0:
        print('Usage: docker run algas/murmur-cli <target_string> [seed (option)]')
    print(main(args[1:]))
