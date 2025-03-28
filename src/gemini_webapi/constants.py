from enum import Enum


class Endpoint(Enum):
    INIT = "https://gemini.google.com/app"
    GENERATE = "https://gemini.google.com/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate"
    BATCH_EXECUTE = "https://gemini.google.com/_/BardChatUi/data/batchexecute"
    ROTATE_COOKIES = "https://accounts.google.com/RotateCookies"
    UPLOAD = "https://content-push.googleapis.com/upload"


class Headers(Enum):
    GEMINI = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
        "Host": "gemini.google.com",
        "Origin": "https://gemini.google.com",
        "Referer": "https://gemini.google.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "X-Same-Domain": "1",
    }
    ROTATE_COOKIES = {
        "Content-Type": "application/json",
    }
    UPLOAD = {"Push-ID": "feeds/mcudyrk2a4khkz"}


class Model(Enum):
    UNSPECIFIED = ("unspecified", {}, False)
    G_2_0_FLASH = (
        "gemini-2.0-flash",
        {"x-goog-ext-525001261-jspb": '[null,null,null,null,"f299729663a2343f"]'},
        False,
    )
    G_2_0_FLASH_EXP = (
        "gemini-2.0-flash-exp",
        {"x-goog-ext-525001261-jspb": '[null,null,null,null,"f299729663a2343f"]'},
        False,
    )  # Deprecated, should be removed in the future
    G_2_0_FLASH_THINKING = (
        "gemini-2.0-flash-thinking",
        {"x-goog-ext-525001261-jspb": '[null,null,null,null,"9c17b1863f581b8a"]'},
        False,
    )
    G_2_0_FLASH_THINKING_WITH_APPS = (
        "gemini-2.0-flash-thinking-with-apps",
        {"x-goog-ext-525001261-jspb": '[null,null,null,null,"f8f8f5ea629f5d37"]'},
        False,
    )  # Deprecated, should be removed in the future
    G_2_0_EXP_ADVANCED = (
        "gemini-2.0-exp-advanced",
        {"x-goog-ext-525001261-jspb": '[null,null,null,null,"b1e46a6037e6aa9f"]'},
        True,
    )
    G_1_5_FLASH = (
        "gemini-1.5-flash",
        {"x-goog-ext-525001261-jspb": '[null,null,null,null,"418ab5ea040b5c43"]'},
        False,
    )  # Deprecated, should be removed in the future
    G_1_5_PRO = (
        "gemini-1.5-pro",
        {"x-goog-ext-525001261-jspb": '[null,null,null,null,"9d60dfae93c9ff1f"]'},
        True,
    )  # Deprecated, should be removed in the future
    G_1_5_PRO_RESEARCH = (
        "gemini-1.5-pro-research",
        {"x-goog-ext-525001261-jspb": '[null,null,null,null,"e5a44cb1dae2b489"]'},
        True,
    )  # Deprecated, should be removed in the future
    G_2_0_FLASH_THINKING_RESEARCH = (
        "gemini-2.0-flash-thinking-research",
        {"x-goog-ext-525001261-jspb": '[null,null,null,null,"6cb69cd4b6cae77d"]'},
        True,
    )  # Deprecated, should be removed in the future

    def __init__(self, name, header, advanced_only):
        self.model_name = name
        self.model_header = header
        self.advanced_only = advanced_only

    @classmethod
    def from_name(cls, name: str):
        for model in cls:
            if model.model_name == name:
                return model
        raise ValueError(
            f"Unknown model name: {name}. Available models: {', '.join([model.model_name for model in cls])}"
        )
