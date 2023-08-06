from dataclasses import dataclass


@dataclass()
class Game:
    type: str | None = None
    name: str | None = None
    steam_appid: int | None = None
    required_age: int | None | str = None
    is_free: bool | None = None
    controller_support: str | None = None
    detailed_description: str | None = None
    short_description: str | None = None
    supported_languages: str | None = None
    header_image: str | None = None
    website: str | None = None
    pc_requirements: dict | list | None = None
    mac_requirements: dict | list | None = None
    linux_requirements: dict | list | None = None
    developers: list | None = None
    publishers: list | None = None
    packages: list | None = None
    package_groups: list | None = None
    platforms: dict | None = None
    metacritic: dict | None = None
    categories: list | None = None
    genres: list | None = None
    screenshots: list | None = None
    movies: list | None = None
    recommendations: dict | None = None
    achievements: dict | None = None
    release_date: dict | None = None
    support_info: dict | None = None
    background: str | None = None
    background_raw: str | None = None
    content_descriptors: dict | None = None
