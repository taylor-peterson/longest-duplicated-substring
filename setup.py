from setuptools import setup, find_packages
PACKAGES = find_packages(where="src", exclude="tst")

opts = dict(name="longest_duplicated_substring",
            maintainer="Taylor Peterson",
            maintainer_email="tayloredwardpeterson@gmail.com",
            description="Sample solutions for the longest duplicated substring interview question.",
            url="https://github.com/taylor-peterson/longest-duplicated-substring",
            download_url="https://github.com/taylor-peterson/longest-duplicated-substirng",
            license="MIT",
            packages=PACKAGES)


if __name__ == '__main__':
    setup(**opts)
