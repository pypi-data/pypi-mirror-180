import hello
import argparse

def main():
    parser = argparse.ArgumentParser(prog='meu_pacote_aa', description='Meu pacote python aa')
    parser.add_argument('name', type=str, help='O seu nome')

    args = parser.parse_args()

    hello.hello_word(args.name)
    
if __name__ == '__main__':
    main()
