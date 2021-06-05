from typing import Mapping


class CookieCutterTemplates:
    MACHINE_LEARNING: str = "https://github.com/jeannefukumaru/cookiecutter-ml"
    DATA_SCIENCE: str = (
        "https://github.com/drivendata/cookiecutter-data-science"
    )
    DJANGO: str = "https://github.com/pydanny/cookiecutter-django"
    FASTAPI: str = "https://github.com/arthurhenrique/cookiecutter-fastapi"
    DJANGO_REST: str = "https://github.com/agconti/cookiecutter-django-rest"
    FLASK: str = "https://github.com/cookiecutter-flask/cookiecutter-flask"
    FLASK_REST: str = "https://github.com/karec/cookiecutter-flask-restful"
    PY_PACKAGE: str = "https://github.com/audreyfeldroy/cookiecutter-pypackage"
    PY_LIBRARY: str = "https://github.com/ionelmc/cookiecutter-pylibrary"
    MODERN_PY_PACKAGE: str = (
        "https://github.com/TezRomacH/python-package-template"
    )
    KOTLIN_ANDROID: str = (
        "https://github.com/general-mobile/kotlin-android-mvvm-starter"
    )
    DOCKER_DATA_SCIENCE: str = (
        "https://github.com/docker-science/cookiecutter-docker-science"
    )
    PY_CLI: str = "https://github.com/nvie/cookiecutter-python-cli"

    # golang:
    GOLANG: str = "https://github.com/lacion/cookiecutter-golang"

    FULL_STACK_FASTAPI_POSTGRES: str = (
        "https://github.com/tiangolo/full-stack-fastapi-postgresql"
    )

    CPP: str = "https://github.com/hbristow/cookiecutter-cpp"
    JAVA: str = "https://github.com/thomaslee/cookiecutter-java"

    SWIFT: str = "https://github.com/theodesp/cookiecutter-swift-library"
    SWIFT_IOS: str = "https://github.com/pmlbrito/cookiecutter-ios-template"

    PHP: str = "https://github.com/jeromegamez/cookiecutter-php"

    repos: Mapping[str, Mapping[str, str]] = {
        "python": {
            "package": MODERN_PY_PACKAGE,
            "data-science": DATA_SCIENCE,
            "machine-learning": MACHINE_LEARNING,
            "flask": FLASK,
            "django": DJANGO,
            "fastapi": FASTAPI,
        },
        "kotlin": {"android": KOTLIN_ANDROID},
        "golang": {"package": GOLANG},
        "cpp": {"package": CPP},
        "java": {"package": JAVA},
        "swift": {
            "package": SWIFT,
            "ios": SWIFT_IOS,
        },
        "php": {"package": PHP},
    }

    @classmethod
    def get_template(cls, lang: str, topic: str) -> str:
        return cls.repos[lang][topic]
