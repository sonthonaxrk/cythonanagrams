import click
from anagrams_finder import PyAnagramFinder

@click.command()
@click.argument('filename', type=click.Path(exists=True))
def main(filename):
    with open(filename) as f:
        finder = PyAnagramFinder()
        for line in f:
            for word in line.split():
               finder.add_word(word)


    results = finder.search()

    if not results:
        print('no anagrams found')
    else:
        for r in results:
            print(r)


if __name__ == '__main__':
    main()
