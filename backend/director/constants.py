from enum import Enum


class RoleTypes(str, Enum):
    system = "system"
    user = "user"
    assistant = "assistant"


class DBType(str, Enum):
    SQLITE = "sqlite"
    TURSO = "turso"
    SQL = "sql"
    POSTGRES = "postgres"


class LLMType(str, Enum):
    """Enum for LLM types"""

    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    MISTRAL = "mistral"
    VIDEODB_PROXY = "videodb_proxy"


class EnvPrefix(str, Enum):
    """Enum for environment prefixes"""

    OPENAI_ = "OPENAI_"
    ANTHROPIC_ = "ANTHROPIC_"
    MISTRAL_ = "MISTRAL_"

DOWNLOADS_PATH="director/downloads"
