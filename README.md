lord_is_coming
---

See who is coming to class.

## Dev env

- OS: macOS 10.14.3
- Python: 3.6.0
- Dependency package: see `./requirements.txt`

## Kick start

Create database use `./sql/members.create.sql`

```sql
DROP TABLE IF EXISTS members;
CREATE TABLE members (name text, times real);
INSERT INTO members VALUES ('xingze', 1000);
INSERT INTO members VALUES ('Barack Obama', 1000);
SELECT * FROM members;
```

Install Dependency

```shell
brew install cmake
git clone https://github.com/davisking/dlib.git
cd dlib
mkdir build
cd build
cmake ..
cmake --build .
cd ..
python3 setup.py install

pip install -r requirements.txt
npm install
```

Run it

```shell
make
```

```shell
npm run start
```