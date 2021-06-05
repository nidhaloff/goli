from goli.cookiecutters import CookieCuttersTemplates

data: object = {
    "python": {
        "package": CookieCuttersTemplates.MODERN_PY_PACKAGE,
        "data-science": CookieCuttersTemplates.DATA_SCIENCE,
        "machine-learning": CookieCuttersTemplates.MACHINE_LEARNING,
        "flask": CookieCuttersTemplates.FLASK,
        "django": CookieCuttersTemplates.DJANGO,
        "fastapi": CookieCuttersTemplates.FASTAPI,
    },
    "kotlin": {"android": CookieCuttersTemplates.KOTLIN_ANDROID},
    "golang": {"package": CookieCuttersTemplates.GOLANG},
    "cpp": {"package": CookieCuttersTemplates.CPP},
    "java": {"package": CookieCuttersTemplates.JAVA},
    "swift": {
        "package": CookieCuttersTemplates.SWIFT,
        "ios": CookieCuttersTemplates.SWIFT_IOS,
    },
    "php": {"package": CookieCuttersTemplates.PHP},
}
