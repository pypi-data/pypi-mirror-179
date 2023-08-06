#!/usr/bin/env python3
# coding=utf-8

from unittest.mock import Mock

import pytest

from bdfr.exceptions import SiteDownloaderError
from bdfr.resource import Resource
from bdfr.site_downloaders.imgur import Imgur


@pytest.mark.online
@pytest.mark.parametrize(
    ("test_url", "expected_gen_dict", "expected_image_dict"),
    (
        (
            "https://imgur.com/a/xWZsDDP",
            {"num_images": "1", "id": "xWZsDDP", "hash": "xWZsDDP"},
            [{"hash": "ypa8YfS", "title": "", "ext": ".png", "animated": False}],
        ),
        (
            "https://imgur.com/gallery/IjJJdlC",
            {"num_images": 1, "id": 384898055, "hash": "IjJJdlC"},
            [
                {
                    "hash": "CbbScDt",
                    "description": "watch when he gets it",
                    "ext": ".gif",
                    "animated": True,
                    "has_sound": False,
                }
            ],
        ),
        (
            "https://imgur.com/a/dcc84Gt",
            {"num_images": "4", "id": "dcc84Gt", "hash": "dcc84Gt"},
            [
                {"hash": "ylx0Kle", "ext": ".jpg", "title": ""},
                {"hash": "TdYfKbK", "ext": ".jpg", "title": ""},
                {"hash": "pCxGbe8", "ext": ".jpg", "title": ""},
                {"hash": "TSAkikk", "ext": ".jpg", "title": ""},
            ],
        ),
        (
            "https://m.imgur.com/a/py3RW0j",
            {
                "num_images": "1",
                "id": "py3RW0j",
                "hash": "py3RW0j",
            },
            [{"hash": "K24eQmK", "has_sound": False, "ext": ".jpg"}],
        ),
    ),
)
def test_get_data_album(test_url: str, expected_gen_dict: dict, expected_image_dict: list[dict]):
    result = Imgur._get_data(test_url)
    assert all([result.get(key) == expected_gen_dict[key] for key in expected_gen_dict.keys()])

    # Check if all the keys from the test dict are correct in at least one of the album entries
    assert any(
        [
            all([image.get(key) == image_dict[key] for key in image_dict.keys()])
            for image_dict in expected_image_dict
            for image in result["album_images"]["images"]
        ]
    )


@pytest.mark.online
@pytest.mark.parametrize(
    ("test_url", "expected_image_dict"),
    (
        ("https://i.imgur.com/dLk3FGY.gifv", {"hash": "dLk3FGY", "title": "", "ext": ".mp4", "animated": True}),
        (
            "https://imgur.com/65FqTpT.gifv",
            {"hash": "65FqTpT", "title": "", "description": "", "animated": True, "mimetype": "video/mp4"},
        ),
    ),
)
def test_get_data_gif(test_url: str, expected_image_dict: dict):
    result = Imgur._get_data(test_url)
    assert all([result.get(key) == expected_image_dict[key] for key in expected_image_dict.keys()])


@pytest.mark.parametrize("test_extension", (".gif", ".png", ".jpg", ".mp4"))
def test_imgur_extension_validation_good(test_extension: str):
    result = Imgur._validate_extension(test_extension)
    assert result == test_extension


@pytest.mark.parametrize(
    "test_extension",
    (
        ".jpeg",
        "bad",
        ".avi",
        ".test",
        ".flac",
    ),
)
def test_imgur_extension_validation_bad(test_extension: str):
    with pytest.raises(SiteDownloaderError):
        Imgur._validate_extension(test_extension)


@pytest.mark.online
@pytest.mark.parametrize(
    ("test_url", "expected_hashes"),
    (
        ("https://imgur.com/a/xWZsDDP", ("f551d6e6b0fef2ce909767338612e31b",)),
        (
            "https://imgur.com/gallery/IjJJdlC",
            ("740b006cf9ec9d6f734b6e8f5130bdab",),
        ),
        (
            "https://imgur.com/a/dcc84Gt",
            (
                "cf1158e1de5c3c8993461383b96610cf",
                "28d6b791a2daef8aa363bf5a3198535d",
                "248ef8f2a6d03eeb2a80d0123dbaf9b6",
                "029c475ce01b58fdf1269d8771d33913",
            ),
        ),
        (
            "https://imgur.com/a/eemHCCK",
            (
                "9cb757fd8f055e7ef7aa88addc9d9fa5",
                "b6cb6c918e2544e96fb7c07d828774b5",
                "fb6c913d721c0bbb96aa65d7f560d385",
            ),
        ),
        (
            "https://i.imgur.com/lFJai6i.gifv",
            ("01a6e79a30bec0e644e5da12365d5071",),
        ),
        (
            "https://i.imgur.com/ywSyILa.gifv?",
            ("56d4afc32d2966017c38d98568709b45",),
        ),
        (
            "https://imgur.com/ubYwpbk.GIFV",
            ("d4a774aac1667783f9ed3a1bd02fac0c",),
        ),
        (
            "https://i.imgur.com/j1CNCZY.gifv",
            ("58e7e6d972058c18b7ecde910ca147e3",),
        ),
        (
            "https://i.imgur.com/uTvtQsw.gifv",
            ("46c86533aa60fc0e09f2a758513e3ac2",),
        ),
        (
            "https://i.imgur.com/OGeVuAe.giff",
            ("77389679084d381336f168538793f218",),
        ),
        (
            "https://i.imgur.com/OGeVuAe.gift",
            ("77389679084d381336f168538793f218",),
        ),
        (
            "https://i.imgur.com/3SKrQfK.jpg?1",
            ("aa299e181b268578979cad176d1bd1d0",),
        ),
        (
            "https://i.imgur.com/cbivYRW.jpg?3",
            ("7ec6ceef5380cb163a1d498c359c51fd",),
        ),
        (
            "http://i.imgur.com/s9uXxlq.jpg?5.jpg",
            ("338de3c23ee21af056b3a7c154e2478f",),
        ),
    ),
)
def test_find_resources(test_url: str, expected_hashes: list[str]):
    mock_download = Mock()
    mock_download.url = test_url
    downloader = Imgur(mock_download)
    results = downloader.find_resources()
    assert all([isinstance(res, Resource) for res in results])
    [res.download() for res in results]
    hashes = set([res.hash.hexdigest() for res in results])
    assert hashes == set(expected_hashes)
