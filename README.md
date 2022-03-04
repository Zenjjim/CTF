# CTF 

## Requirements
- Python 3.9 or above
- GNU Make

## Setup
```
git clone git@github.com:Zenjjim/CTF.git
cd CTF
make env
```

Copy and run command to access env, then run
```
make init
```
We have now created a db with some example Challenges and temporary user/password: `user1|test`

To run system
```
make run
```
The system is run on [http://localhost:8000/](http://localhost:8000/). 
Login with `user1|test`



## Credit
System built on [R8](https://github.com/mhils/r8)