"""
This is implementation has some very rudimentary python bindings
"""
from pep440_rs import Version, VersionSpecifier


def test_pep440():
    assert Version("1.1a1").any_prerelease()
    assert Version("1.1.dev2").any_prerelease()
    assert not Version("1.1").any_prerelease()
    assert VersionSpecifier(">=1.0").contains(Version("1.1a1"))
    assert not VersionSpecifier(">=1.1").contains(Version("1.1a1"))
    assert Version("2.0") in VersionSpecifier("==2")
