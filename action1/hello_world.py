import os
# import pandas

def main():
    my_input = os.environ['INPUT_WHO-TO-GREET']
    my_output = f'Hello world'
    print(f'::set-output name=myprint::{my_output}')

if __name__ == '__main__':
    main()