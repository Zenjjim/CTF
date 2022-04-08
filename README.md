# CTF 

## Requirements
- Python 3.9 or above

## Setup
```
mkdir CTF
cd CTF
python3 -m venv venv
git clone git@github.com:Zenjjim/CTF.git
venv/bin/pip install -e ./CTF
```

Start enviorment
```
source venv/bin/activate
```

To update database with new config
```
r8 sql file r8/config.sql
```

We have now created a db with some example Challenges and temporary user/password: `user1|test`


To run system
```
r8 run
```
The system is run on [http://localhost:8000/](http://localhost:8000/). 
Login with `user1|test`



## Credit
System built on [R8](https://github.com/mhils/r8)