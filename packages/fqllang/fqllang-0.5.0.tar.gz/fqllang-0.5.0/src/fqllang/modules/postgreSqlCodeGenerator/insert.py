from fqllang.modules.sqlCodeGenerator.base import InsertSql, PreparedInsertSql
from fqllang.modules.sqlCodeGenerator.elements import Field, ColumnList


class InsertPostgreSql(InsertSql):
    def __init__(self, tableName:str, columns:ColumnList, fields:list[Field]) -> None:
        super().__init__(tableName, columns, fields)

    def _valuesList(self, fields:list[Field], columns:ColumnList):
        pass


class PreparedInsertPostgreSql(PreparedInsertSql):
    def __init__(self, tableName: str, columns: ColumnList) -> None:
        super().__init__(tableName, columns)

    def _placeholderList(self, columns:ColumnList):
        pass
