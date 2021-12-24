# Pyord
A cipher that is hard to bruteforce   


## Benefits
- Cannot be bruteforced because it randomly chooses between + and - shift   
- Default is ±64 shifts (you can change the shift), so bruteforcers would have a hard time finding the shift (if they bruteforce from 0 to infinity)   

## How to use
To encrypt, use the `encrypt(text, shift)` function in [main.py](https://github.com/Falcn8/Pyord/blob/main/main.py)   
To decrypt, use the `decrypt(encrypted_text, shift)` function in [main.py](https://github.com/Falcn8/Pyord/blob/main/main.py)   


## To Do
- [X] Support custom shifts   
- [ ] Make a Python library


## License
Apache License 2.0   
A permissive license whose main conditions require preservation of copyright and license notices. Contributors provide an express grant of patent rights. Licensed works, modifications, and larger works may be distributed under different terms and without source code.   
https://github.com/Falcn8/Pyord/blob/main/LICENSE   

