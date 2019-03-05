lord_is_coming
---

See who is coming to class.

打开摄像头后扫描到教室学生脸部，标识出谁到场，然后给出勤的脸部加分，放到前端显示出勤情况。

![](./docs/frontend.png)

## Dev env

- OS: macOS 10.14.3
- Python: 3.6.0
- Dependency package: see `./requirements.txt`
- Core inspiration: [face_recognition](https://github.com/ageitgey/face_recognition)

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

Todo:

- [ ] 获取班级人像信息
- [ ] 动态加载面部特征数据库
- [ ] 自动化部署
