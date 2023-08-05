### Enable Timescale Extension in Postgres
``` enable_timescale() ```<br/>
Returns ```True``` if enabled. Else Returns ```Error```

### Check Timescale Extension Enabled in Postgres
```check_timescale()```<br/>
Returns ```True``` if Enabled else ```False```
### Creating Table
```create_table(tablename,table_data)```

| Parameter    | Type     | Description                             |
|:-------------|:---------|:----------------------------------------|
| `tablename`  | `string` | **Required**. Table Name                |
| `table_data` | `list`   | **Required**. Column Name and Datatypes |

```python
table_data = [['id', 'bigint', 0], ["names", "varchar", 200], ['t_modified', 'timestamp', 0]]
```
#### Datatypes
```json
{
    "bigint": "BIGINT",
    "boolean": "BOOLEAN",
    "character": "CHAR",
    "varchar": "VARCHAR",
    "date": "DATE",
    "float": "FLOAT",
    "int": "INTEGER",
    "interval": "Interval",
    "json": "JSON",
    "numeric": "NUMERIC",
    "smallint": "SMALLINT",
    "text": "TEXT",
    "time": "TIME",
    "timestamp": "TIMESTAMP"
}
```

### Creating Index :
```create_index(table_name,columns)```

| Parameter    | Type     | Description                                       |
|:-------------|:---------|:--------------------------------------------------|
| `table_name`  | `string` | **Required**. Table Name                          |
| `columns`  | `list`   | **Required**. Column Name where you want to index |
```python
columns = ["c3","date_time"]
```
### Creating Hypertable :
```create_hypertable(table_name,column_name)```

| Parameter     | Type     | Description                                                                                  |
|:--------------|:---------|:---------------------------------------------------------------------------------------------|
| `table_name`  | `string` | **Required**. Table Name                                                                     |
| `column_name` | `string` | **Required**. On which Column you want to Create Hypertable. Should be TIMESTAMP column only |


### Select Data :

```selectgroupdata(select_type,group_by, start, end, where, orcondition, order_by,column_name,limit)```

| Parameter     | Type                | Description                                                                |
|:--------------|:--------------------|:---------------------------------------------------------------------------|
| `select_type` | `string`            | **Required**. Which type need to be selected. Sum / Average /Cols/All      |                                                                            
| `start`       | `string`/`datetime` | **Required**. Start Time                                                   |
| `end`         | `string`/`datetime` | **Required**. End Time                                                     |
| `where`       | `dictionary`        | **Required**. Add single or multiple conditions based on column and values |
| `orcondition` | `dictionary`        | **Required**. Adding OR conditions based on column and values              |
| `order_by`    | `list`              | **Required**. Order By Column Name ASC/DESC                                |
| `group_by`    | `string`            | **Required**. Group By Column Name                                         |
| `column_name` | `list`              | **Required**. Add extra Column Name                                        |
| `limit`       | `list`              | **Required**. For adding Limit. `[limit,offset]`                           |

```python
where = {"column_1":"value","column_2":"value2"}
orcondition = {"column_1":"value","column_2":"value2"}
order_by = ["column_name","desc"]
column_name = ["column_1","column_2","column_3"]
limit = ["limit","offset"]
```
### Insert Data :

```insert(dataset)```

| Parameter     | Type                | Description                                                     |
|:--------------|:--------------------|:----------------------------------------------------------------|
| `dataset`     | `dictionary`        | **Required**. Set of Data to be inserted. Format is given below |                                                                            
```python
dataset = [
                {
                    "c3": "site_100$line_4888$equipment_6888$tag_60888",
                    "c1": "site_123",
                    "c5": "tag_11111",
                    "l1": "site_888",
                    "l2": "line_4888",
                    "l3": "equipment_6888",
                    "value": "260",
                    "time_stamp": "1669022699000",
                    "date_time": "2022-11-21 14:54:57"
                },
                {
                    "c3": "site_400$line_4444$equipment_6444$tag_60444",
                    "c1": "site_456",
                    "c5": "tag_22222",
                    "l1": "site_444",
                    "l2": "line_4444",
                    "l3": "equipment_6888",
                    "value": "260",
                    "time_stamp": "1669022699000",
                    "date_time": "2022-11-21 14:54:57"
                }]
```

### Delete Data :

```delete(where)```

| Parameter | Type                | Description                                                                                     |
|:----------|:--------------------|:------------------------------------------------------------------------------------------------|
| `where`   | `dictionary`        | **Required**.  Add single or multiple conditions based on column and values. Format given below |

```python
where = {
            "column_1": "value_1",
            "column_2": "value_2"
        }
```
