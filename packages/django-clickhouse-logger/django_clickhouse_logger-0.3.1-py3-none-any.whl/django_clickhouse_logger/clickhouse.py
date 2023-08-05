import datetime
import io
import logging
import traceback
import shortuuid
import hashlib
from clickhouse_driver import Client as ClickHouseClient
from clickhouse_driver import connect
from clickhouse_driver.dbapi.extras import DictCursor
from django_clickhouse_logger.settings import DJANGO_CLICKHOUSE_LOGGER_HOST
from django_clickhouse_logger.settings import DJANGO_CLICKHOUSE_LOGGER_PORT
from django_clickhouse_logger.settings import DJANGO_CLICKHOUSE_LOGGER_USER
from django_clickhouse_logger.settings import DJANGO_CLICKHOUSE_LOGGER_PASSWORD
from django_clickhouse_logger.settings import DJANGO_CLICKHOUSE_LOGGER_REQUEST_EXTRA
from django_clickhouse_logger.settings import DJANGO_CLICKHOUSE_LOGGER_TTL_DAY


def format_exception(ei) -> str:
    sio = io.StringIO()
    tb = ei[2]
    traceback.print_exception(ei[0], ei[1], tb, None, sio)
    s = sio.getvalue()
    sio.close()
    if s[-1:] == "\n":
        s = s[:-1]
    return s


def proxy(record: logging.LogRecord = "") -> None:

    assert DJANGO_CLICKHOUSE_LOGGER_HOST, "Please specify DJANGO_CLICKHOUSE_LOGGER_HOST in your settings.py file"
    clickhouse_connect = connect(host=DJANGO_CLICKHOUSE_LOGGER_HOST, port=DJANGO_CLICKHOUSE_LOGGER_PORT, user=DJANGO_CLICKHOUSE_LOGGER_USER, password=DJANGO_CLICKHOUSE_LOGGER_PASSWORD)

    request = record.request
    exc_info = getattr(record, 'exc_info', "")

    if exc_info:
        exc_info = format_exception(exc_info)   

    clickhouse_dict = {}
    clickhouse_dict["uuid"] = shortuuid.uuid()
    clickhouse_dict["asctime"] = datetime.datetime.now()
    clickhouse_dict["exc_info"] = exc_info 
    clickhouse_dict["exc_hash"] = hashlib.md5(exc_info.encode()).hexdigest()
    clickhouse_dict["user"] = str(request.user)
    clickhouse_dict["user_id"] = request.user.id
    clickhouse_dict["request_extra"] = str(getattr(request, DJANGO_CLICKHOUSE_LOGGER_REQUEST_EXTRA, ""))
    clickhouse_dict["site"] = f"{request.get_host()}:{request.get_port()}"
    clickhouse_dict["scheme"] = str(request.scheme) 
    clickhouse_dict["body"] = str(request.body) 
    clickhouse_dict["path"] = str(request.path) 
    clickhouse_dict["method"] = str(request.method)  
    clickhouse_dict["GET"] = str(request.GET)  
    clickhouse_dict["POST"] = str(request.POST)  
    clickhouse_dict["headers"] = str(request.headers) 
    clickhouse_dict["args"] = str(request.resolver_match.args)
    clickhouse_dict["kwargs"] = str(request.resolver_match.kwargs)  
    clickhouse_dict["pathname"] = str(getattr(record, 'pathname', ""))
    clickhouse_dict["funcName"] = str(getattr(record, 'funcName', ""))
    clickhouse_dict["lineno"] = getattr(record, 'lineno', 0)
    clickhouse_dict["message"] = record.getMessage() 
    clickhouse_dict["exc_text"] = str(getattr(record, 'exc_text', ""))   
    clickhouse_dict["created"] = getattr(record, 'lineno', 0)
    clickhouse_dict["filename"] = str(getattr(record, 'filename', ""))  
    clickhouse_dict["levelname"] = str(getattr(record, 'levelname', ""))  
    clickhouse_dict["levelno"] = str(getattr(record, 'levelno', ""))  
    clickhouse_dict["module"] = str(getattr(record, 'module', ""))  
    clickhouse_dict["msecs"] = getattr(record, 'msecs', 0)  
    clickhouse_dict["msg"] = str(getattr(record, 'msg', ""))  
    clickhouse_dict["name"] = str(getattr(record, 'name', ""))  
    clickhouse_dict["process"] = str(getattr(record, 'process', ""))  
    clickhouse_dict["processName"] = str(getattr(record, 'processName', ""))  
    clickhouse_dict["relativeCreated"] = str(getattr(record, 'relativeCreated', ""))  
    clickhouse_dict["stack_info"] = str(getattr(record, 'stack_info', ""))  
    clickhouse_dict["thread"] = str(getattr(record, 'thread', ""))  
    clickhouse_dict["threadName"] = str(getattr(record, 'threadName', ""))  

    with clickhouse_connect.cursor(cursor_factory=DictCursor) as cursor:
        cursor.execute(
            """INSERT INTO django_clickhouse_logger.records (*)  VALUES""",
            [clickhouse_dict],
        )


def create_clickhouse_table() -> None:
    # python manage.py shell --command="import django_clickhouse_logger; django_clickhouse_logger.clickhouse.create_clickhouse_table()"

    assert DJANGO_CLICKHOUSE_LOGGER_HOST, "Please specify DJANGO_CLICKHOUSE_LOGGER_HOST in your settings.py file"
    assert isinstance(DJANGO_CLICKHOUSE_LOGGER_TTL_DAY, int), "DJANGO_CLICKHOUSE_LOGGER_TTL_DAY must be positive integer"

    clickhouse_client = ClickHouseClient(host=DJANGO_CLICKHOUSE_LOGGER_HOST, port=DJANGO_CLICKHOUSE_LOGGER_PORT, user=DJANGO_CLICKHOUSE_LOGGER_USER, password=DJANGO_CLICKHOUSE_LOGGER_PASSWORD)
    clickhouse_client.execute('CREATE DATABASE IF NOT EXISTS django_clickhouse_logger')
    clickhouse_client.execute('DROP TABLE IF EXISTS django_clickhouse_logger.records')
    clickhouse_client.execute(f'''
    CREATE TABLE django_clickhouse_logger.records (
    `uuid` String,
    `asctime` DateTime,     
    `exc_info` Nullable(String),
    `exc_hash` Nullable(String),
    `user` Nullable(String),
    `user_id` Nullable(UInt16),
    `request_extra` Nullable(String),
    `site` Nullable(String),   
    `scheme` Nullable(String),  
    `body` Nullable(String),  
    `path` Nullable(String),  
    `method` Nullable(String), 
    `GET`  Nullable(String),
    `POST`  Nullable(String),
    `headers`  Nullable(String),
    `args` Nullable(String),
    `kwargs` Nullable(String),    
    `pathname` Nullable(String),   
    `funcName` Nullable(String),   
    `lineno` Nullable(Int32),  
    `message` Nullable(String),  
    `exc_text` Nullable(String),      
    `created` Nullable(Float64),
    `filename` Nullable(String),  
    `levelname` Nullable(String),
    `levelno` Nullable(String),
    `module` Nullable(String),
    `msecs` Nullable(Float64),
    `msg` Nullable(String),
    `name` Nullable(String),
    `process` Nullable(String),
    `processName` Nullable(String),
    `relativeCreated` Nullable(String),
    `stack_info` Nullable(String),
    `thread` Nullable(String),  
    `threadName` Nullable(String)    
    ) 
    ENGINE = MergeTree() 
    PARTITION BY toDate(asctime)
    ORDER BY (asctime) 
    TTL asctime + INTERVAL {DJANGO_CLICKHOUSE_LOGGER_TTL_DAY} DAY
    SETTINGS min_bytes_for_wide_part = 0
    ''')
    print(f'success create table django_clickhouse_logger.records; log rotation {DJANGO_CLICKHOUSE_LOGGER_TTL_DAY} day')


def truncate_clickhouse_table() -> None:
    # python manage.py shell --command="import django_clickhouse_logger; django_clickhouse_logger.clickhouse.truncate_clickhouse_table()"
    
    assert DJANGO_CLICKHOUSE_LOGGER_HOST, "Please specify DJANGO_CLICKHOUSE_LOGGER_HOST in your settings.py file"
    assert isinstance(DJANGO_CLICKHOUSE_LOGGER_TTL_DAY, int), "DJANGO_CLICKHOUSE_LOGGER_TTL_DAY must be positive integer"

    clickhouse_client = ClickHouseClient(host=DJANGO_CLICKHOUSE_LOGGER_HOST, port=DJANGO_CLICKHOUSE_LOGGER_PORT, user=DJANGO_CLICKHOUSE_LOGGER_USER, password=DJANGO_CLICKHOUSE_LOGGER_PASSWORD)
    clickhouse_client.execute('TRUNCATE TABLE IF EXISTS django_clickhouse_logger.records')
    print(f'success truncate table django_clickhouse_logger.records')


