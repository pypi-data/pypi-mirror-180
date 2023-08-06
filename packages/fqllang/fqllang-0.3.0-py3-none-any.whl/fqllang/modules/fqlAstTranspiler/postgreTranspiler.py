from fqllang.dsl.utils import getClassName
from fqllang.modules.fqlAstTranspiler.transpiler import FqlAstSqlTranspiler
from fqllang.modules.postgreSqlCodeGenerator.create import CreatePostgreSql
from fqllang.modules.postgreSqlCodeGenerator.select import SelectPostgreSql, SelectWithCriteriaPostgreSql
from fqllang.modules.sqlCodeGenerator.elements import Column, ColumnList, Condition, Criteria, DataConstraint, DataType, Field, FieldList, convertFqlDataTypeToPostgreSqlDataType

class FqlAstPostgreSqlTranspiler(FqlAstSqlTranspiler):
    def __init__(self, fqlAstModel) -> None:
        super().__init__(fqlAstModel)

    def generate(self):
        return self.fqlStatementTranspiler(self.model)

    def __str__(self) -> str:
        return self.generate()

    def fqlStatementTranspiler(self, model):
        className = getClassName(model)
        if className == "CreateForm":
            return self.createFormTranspiler(model).generate()
        elif className == "CreateNew":
            return self.createNewTranspiler(model).generate()
        elif className == "ShowForms":
            return self.showFormsTranspiler(model).generate()
        elif className == "GetCase":
            return self.getCaseTranspiler(model).generate()
        raise Exception("Modelo incorrecto")

    def createFormTranspiler(self, createForm):
        formName = createForm.formName

        dataSpecList = map(lambda dataSpec: self.dataSpecTranspiler(dataSpec), createForm.dataSpecList)

        columnList = ColumnList.emptyColumnList()

        keyField = Field('FQL_ID', DataType.serial, DataConstraint.primaryKey)
        fieldList = FieldList(keyField, *list(dataSpecList))

        return CreatePostgreSql(formName, columnList, fieldList)

    def createNewTranspiler(self, createNew):
        pass

    def getCaseTranspiler(self, getCase):
        formName=getCase.formName
        conditions = self.extractConditions(getCase)
        if conditions:
            criteria = self.getCaseConditionsTranspiler(conditions)
            return SelectWithCriteriaPostgreSql(formName, ColumnList.emptyColumnList(), criteria)
        else:
            return SelectPostgreSql(formName)
        # extendedLabelsList = self.extractExtendedLabelsList(getCase)

    def getCaseConditionsTranspiler(self, conditions):
        conditionList = []
        for condition in conditions:
            className = getClassName(condition)
            if className == "ConditionTerminal":
                attribute = condition.attribute
                valueTerminal = condition.valueTerminal
                conditionList.append(Condition(attribute, valueTerminal))
        return Criteria(*conditionList)

    def extractConditions(self, getCase):
        try:
            return getCase.conditions
        except:
            return []

    # def extractExtendedLabelsList(self, getCase):
    #     try:
    #         return getCase.extendedLabelsList
    #     except:
    #         return []

    def showFormsTranspiler(self, showForms):
        pass

    def dataSpecTranspiler(self,dataSpec):
        className = getClassName(dataSpec)
        if className == 'DataDefinition':
            return self.dataDefinitionTranspiler(dataSpec)
        elif className == 'DataReference':
            return self.dataReferenceTranspiler(dataSpec)

    def dataDefinitionTranspiler(self, dataDefinition):
        dataName = dataDefinition.dataName
        dataType = convertFqlDataTypeToPostgreSqlDataType(dataDefinition.dataType)
        notNull = dataDefinition.notNull
        unique = dataDefinition.unique
        field = Field(dataName, dataType)
        if notNull: field.addDataConstraint(DataType.notNull)
        if unique: field.addDataConstraint(DataType.unique)
        return field

    def dataReferenceTranspiler(self, dataReference):
        pass
