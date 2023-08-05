from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()


long_description = (here / "README.md").read_text(encoding="utf-8")


setup(
    name="django4-recaptcha-admin-login",

    version="1.0",

    description="Will add an reCAPTCHA field to Django admin login page to provide a more secure page",

    long_description=long_description,

    long_description_content_type="text/markdown",

    url="https://github.com/lseparatio/Django4_reCAPTCHA_admin_login_page",

    author="Ionut Zapototchi",

    author_email="admin@ionutzapototchi.com",

    classifiers=[

        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 3.10",

        "Programming Language :: Python :: 3 :: Only",
    ],

    keywords="django, django4, recaptcha, django admin, django login",

    package_dir={"": "src"},

    packages=find_packages(where="src"),

    package_data= {
        'django4_recaptcha_admin_login': ['templates/admin/*']
    },

    python_requires=">=3.8, <4",

    install_requires=["django-recaptcha==3.0.0"],

    project_urls={
        "Bug Reports": "https://github.com/lseparatio/django4_recaptcha_admin_login/issues",
        "Source": "https://github.com/lseparatio/django4_recaptcha_admin_login",
    },
)
