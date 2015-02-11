class ProjectPathAlreadyExists(Exception):
    """Base class for Project path already exists"""


class StaticPathAlreadyExists(Exception):
    """Base class for Static path already exists"""


class TemplatePathAlreadyExists(Exception):
    """Base class for Template path already exists"""


class ModulePathAlreadyExists(Exception):
    """Base class for Module path already exists"""


class InvalidProjectName(Exception):
    """Base class for Invalid project name"""


class InvalidModuleName(Exception):
    """Base class for Invalid module name"""


class TemplateModuleAlreadyExists(Exception):
    """Base class for Template Module Already exists"""
