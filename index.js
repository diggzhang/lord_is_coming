const SqliteToJson = require('sqlite-to-json');
const sqlite3 = require('sqlite3');
const exporter = new SqliteToJson({
  client: new sqlite3.Database('./sign-in.db')
});
exporter.save('members', './signin.json', function (err) {
    console.error(err)
});
