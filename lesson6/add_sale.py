import click

@click.command()
# @click.option('--count', default = 1, help = "Number of sale's sums")
@click.option('--sum', prompt = 'Sale Sum', help = "The sum of sales to be written in the file")
def sale_sum_to_file(sum):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(sum)
        f.write('\n')

if __name__ == '__main__':
    sale_sum_to_file()

# def main(argv):
#     with open('bakery.csv', 'a', encoding='utf-8') as f:
#         f.writelines(argv)
#         f.writelines('/n')
#     return 0
#
# if __name__ == '__main__':
#     import sys
#     num = input('Enter the sale sum: ')
#     main(num)
#
#     exit(main(sys.argv))

