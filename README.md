# Pyord
A cipher that is hard to bruteforce   


## Benefits
- Cannot be bruteforced because it randomly chooses between + and - shift   
- Default is 64 shifts (you can change the shift), so bruteforcers would have a hard time finding the shift (if they bruteforce from 0 to infinity)   

## How to use
To encrypt, use the `encrypt(text, shift)` function in [main.py](https://github.com/Falcn8/Pyord/blob/main/main.py)   
To decrypt, use the `decrypt(encrypted_text, shift)` function in [main.py](https://github.com/Falcn8/Pyord/blob/main/main.py)   


## To Do
- [X] Support custom shifts   
- [ ] Make a Python library
