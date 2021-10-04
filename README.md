# eVisa

### Setup
Database
```
CREATE DATABASE urls CHARACTER SET utf8 COLLATE utf8_general_ci;
```


Setup
```
pip install -r req.txt
cp main/settings/dev.py.def evisa/settings/dev.py
```

`SECRET_KEY` in `settings_local.py`:
```
python -c 'import random; print("".join([random.SystemRandom().choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)]))'
```

Run migratins:
```
./manage.py migrate
```
