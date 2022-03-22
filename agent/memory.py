from agent.globals import *


class GroundedId:
    def __init__(self):
        self.name


class NonGroundedId:
    def __init__(self):
        self.name


class MainProgramNode:
    def __init__(self):
        self.name


class GroundingProgramNode:
    def __init__(self):
        self.name

class Statement:
    def __init__(self, id_name, area_global):
        self.id_name = id_name
        self.area_global = area_global

    def create_runnable_scetch(self):
        return runnable_scetch

class RunnableScetch:
    # todo 1.возможна проверка, являются для два скетча взаимноисключающими, и следовательно,
    #       того, являются ли два утвеждения противоречащими - база интеллекта!

    # todo 2. для этого надо понятие о взаимном исключении идов.
    # todo 3. возможна быстрая проверка потенциальной (не)выполнимости скетча в текущем
    #  глобальном контексте + уточнение неопределенности в скетче по записям в этом контексте

    def __init__(self):
        pass


class UniqNamesGenerator:
    def __init__(self):
        pass

class ProgramContext:
    pass

class GlobalContext:
    pass
