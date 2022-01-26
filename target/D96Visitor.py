# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#concoac.
    def visitConcoac(self, ctx:D96Parser.ConcoacContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classUse.
    def visitClassUse(self, ctx:D96Parser.ClassUseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mainClass.
    def visitMainClass(self, ctx:D96Parser.MainClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor.
    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor.
    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute.
    def visitAttribute(self, ctx:D96Parser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var.
    def visitVar(self, ctx:D96Parser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#val.
    def visitVal(self, ctx:D96Parser.ValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#calculators.
    def visitCalculators(self, ctx:D96Parser.CalculatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#calculator.
    def visitCalculator(self, ctx:D96Parser.CalculatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#typeNumber.
    def visitTypeNumber(self, ctx:D96Parser.TypeNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classType.
    def visitClassType(self, ctx:D96Parser.ClassTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#math.
    def visitMath(self, ctx:D96Parser.MathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrayType.
    def visitArrayType(self, ctx:D96Parser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#declaration.
    def visitDeclaration(self, ctx:D96Parser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#listParams.
    def visitListParams(self, ctx:D96Parser.ListParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#param.
    def visitParam(self, ctx:D96Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#blockStatement.
    def visitBlockStatement(self, ctx:D96Parser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statement.
    def visitStatement(self, ctx:D96Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#foreach.
    def visitForeach(self, ctx:D96Parser.ForeachContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#ifElse.
    def visitIfElse(self, ctx:D96Parser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if1.
    def visitIf1(self, ctx:D96Parser.If1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#else1.
    def visitElse1(self, ctx:D96Parser.Else1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elseIf.
    def visitElseIf(self, ctx:D96Parser.ElseIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#call.
    def visitCall(self, ctx:D96Parser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#invocation.
    def visitInvocation(self, ctx:D96Parser.InvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#number.
    def visitNumber(self, ctx:D96Parser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrayIndex.
    def visitArrayIndex(self, ctx:D96Parser.ArrayIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#booleanType.
    def visitBooleanType(self, ctx:D96Parser.BooleanTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#integerType.
    def visitIntegerType(self, ctx:D96Parser.IntegerTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#floatType.
    def visitFloatType(self, ctx:D96Parser.FloatTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stringType.
    def visitStringType(self, ctx:D96Parser.StringTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arithmeticOperators.
    def visitArithmeticOperators(self, ctx:D96Parser.ArithmeticOperatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#booleanOperators.
    def visitBooleanOperators(self, ctx:D96Parser.BooleanOperatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stringOperators.
    def visitStringOperators(self, ctx:D96Parser.StringOperatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#relationalOperators.
    def visitRelationalOperators(self, ctx:D96Parser.RelationalOperatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operators.
    def visitOperators(self, ctx:D96Parser.OperatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expressions.
    def visitExpressions(self, ctx:D96Parser.ExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instanceAttribute.
    def visitInstanceAttribute(self, ctx:D96Parser.InstanceAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#staticAttribute.
    def visitStaticAttribute(self, ctx:D96Parser.StaticAttributeContext):
        return self.visitChildren(ctx)



del D96Parser