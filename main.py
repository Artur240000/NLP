import argparse


def main():
    parser = argparse.ArgumentParser(description='NLPGenration')

    parser.add_argument('--input-dir', type=str, help='Название файла')
    parser.add_argument('--length', type=int, default=1000, help='Длина генерируемой последовательности.')

    args = parser.parse_args()


if __name__ == '__main__':
    main()