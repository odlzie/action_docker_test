import os
# import pandas

def main():
    my_input = os.environ['INPUT_WHO-TO-GREET']
    my_output = f'Hello {my_input}'
    # print(f'::set-output name=myprint::{my_output}')

    output_name = 'myprint'
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'{output_name}={my_output}', file=fh)

if __name__ == '__main__':
    main()