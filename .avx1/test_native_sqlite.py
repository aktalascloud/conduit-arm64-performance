"""Exercise the source-built SQLite amalgamation without touching user databases."""
import ctypes as c
import sys

db=c.c_void_p();lib=c.CDLL(sys.argv[1])
lib.sqlite3_open.argtypes=[c.c_char_p,c.POINTER(c.c_void_p)]
lib.sqlite3_exec.argtypes=[c.c_void_p,c.c_char_p,c.c_void_p,c.c_void_p,c.POINTER(c.c_char_p)]
lib.sqlite3_get_table.argtypes=[c.c_void_p,c.c_char_p,c.POINTER(c.POINTER(c.c_char_p)),c.POINTER(c.c_int),c.POINTER(c.c_int),c.POINTER(c.c_char_p)]
lib.sqlite3_free_table.argtypes=[c.POINTER(c.c_char_p)]
assert lib.sqlite3_open(b':memory:',c.byref(db))==0
def execute(sql):
    error=c.c_char_p();code=lib.sqlite3_exec(db,sql.encode(),None,None,c.byref(error))
    if code:raise RuntimeError('Source-built SQLite query failed: '+str(error.value))
def scalar(sql):
    table=c.POINTER(c.c_char_p)();rows=c.c_int();cols=c.c_int();error=c.c_char_p()
    assert lib.sqlite3_get_table(db,sql.encode(),c.byref(table),c.byref(rows),c.byref(cols),c.byref(error))==0
    try:return table[cols.value].decode()
    finally:lib.sqlite3_free_table(table)
try:
    execute("CREATE TABLE t(k INTEGER PRIMARY KEY,v TEXT); BEGIN; INSERT INTO t VALUES(1,'kept'); COMMIT; BEGIN; INSERT INTO t VALUES(2,'rolled back'); ROLLBACK;")
    assert scalar('SELECT count(*) FROM t')=='1'
    assert scalar("SELECT json_extract('{\"x\":7}', '$.x')")=='7'
    execute("CREATE VIRTUAL TABLE documents USING fts5(body); INSERT INTO documents VALUES('agent tool result');")
    assert scalar("SELECT count(*) FROM documents WHERE documents MATCH 'agent'")=='1'
    assert scalar('PRAGMA integrity_check')=='ok'
    print('SOURCE_SQLITE_TRANSACTIONS_FTS5_JSON_INTEGRITY_PASSED')
finally:lib.sqlite3_close(db)
