# Statlink

An asyncio based multipurpose link explorer.

- Check broken links in websites.
- Headless browsers support (Chromium, Firefox, WebKit).
- Domain / URL Regex / status code filters.
- Incremental timeout.
- Panda dataframe / CSV output.
- Database store support.


## Get started

### Installation

    pip install statlink

With browser support:

    pip install statlink[chromium|fifefox|webkit|all]

## Usage

    Usage: statlink [OPTIONS] [SOURCES]...

    Options:
      -c, --concurrency INTEGER       Set the maximum number of concurrent
                                      requests.  [default: 20]
      --allow-external                Allow external URL to be checked.
      -d, --depth INTEGER             Recursion depth value for checking URLs,
                                      negative value will set it to infinity.
                                      [default: -1]
      -t, --timeout INTEGER           Set timeout for each requests.  [default:
                                      20]
      --engine [aiohttp|chromium|firefox|webkit]
                                      Engine that will be used to make requests.
                                      [default: aiohttp]
      --help                          Show this message and exit.


## Examples

Find the dead links for a https domain

    $ statlink https://google.com


Find the dead links in a text file

    $ statlink -d 0 bad_urls.txt


## Library


    from statlink.crawler import Crawler

    crawler = Crawler()
    crawler.add_url("https://google.com")
    crawler.start()
