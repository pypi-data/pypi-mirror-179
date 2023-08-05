[Build Status]

picta-dl - Download videos from Picta.cu Plataforma de Contenidos
Audiovisuales and Youtube.com

-   INSTALLATION
-   DESCRIPTION
-   OPTIONS
-   CONFIGURATION
-   OUTPUT TEMPLATE
-   FORMAT SELECTION
-   VIDEO SELECTION
-   FAQ
-   DEVELOPER INSTRUCTIONS
-   EMBEDDING YOUTUBE-DL
-   BUGS
-   COPYRIGHT



INSTALLATION


To install it right away for all UNIX users (Linux, macOS, etc.), type:

    sudo curl -L https://github.com/oleksis/picta-dl/releases/download/v2022.11.30/picta-dl -o /usr/local/bin/picta-dl
    sudo chmod a+rx /usr/local/bin/picta-dl

If you do not have curl, you can alternatively use a recent wget:

    sudo wget https://github.com/oleksis/picta-dl/releases/download/v2022.11.30/picta-dl -O /usr/local/bin/picta-dl
    sudo chmod a+rx /usr/local/bin/picta-dl

Windows users can download an .exe file and place it in any location on
their PATH except for %SYSTEMROOT%\System32 (e.g. DO NOT put in
C:\Windows\System32).

You can also use pip:

    sudo -H pip install --upgrade picta-dl

This command will update picta-dl if you have already installed it. See
the pypi page for more information.

macOS users can install picta-dl with Homebrew:

    brew tap oleksis/picta-dl
    brew install picta-dl

Or with MacPorts:

    sudo port install picta-dl


EXTRA

The users can install FFmpeg for join the Video and Audio.

    $ ffmpeg -i video.mp4 -i audio.m4a -c:v copy -c:a copy output.mp4

Alternatively, refer to the developer instructions for how to check out
and work with the git repository. For further options, including PGP
signatures, see the youtube-dl Download Page.



DESCRIPTION


PICTA-DL is a command-line program to download videos from YouTube.com
and Picta.cu Plataforma de Contenidos Audiovisuales. It requires the
Python interpreter, version 2.6, 2.7, or 3.2+, and it is not platform
specific. It should work on your Unix box, on Windows or on macOS. It is
released to the public domain, which means you can modify it,
redistribute it or use it however you like.

    picta-dl [OPTIONS] URL [URL...]



OPTIONS


    -h, --help                      Print this help text and exit
    --version                       Print program version and exit
    -U, --update                    Check if updates are available. You cannot
                                    update when running from source code; Use
                                    git to pull the latest changes
    --no-update                     Do not check for updates (default)
    -i, --ignore-errors             Ignore download and postprocessing errors.
                                    The download will be considered successful
                                    even if the postprocessing fails
    --no-abort-on-error             Continue with next video on download errors;
                                    e.g. to skip unavailable videos in a
                                    playlist (default)
    --abort-on-error                Abort downloading of further videos if an
                                    error occurs (Alias: --no-ignore-errors)
    --dump-user-agent               Display the current user-agent and exit
    --list-extractors               List all supported extractors and exit
    --extractor-descriptions        Output descriptions of all supported
                                    extractors and exit
    --use-extractors NAMES          Extractor names to use separated by commas.
                                    You can also use regexes, "all", "default"
                                    and "end" (end URL matching); e.g. --ies
                                    "holodex.*,end,youtube". Prefix the name
                                    with a "-" to exclude it, e.g. --ies
                                    default,-generic. Use --list-extractors for
                                    a list of extractor names. (Alias: --ies)
    --default-search PREFIX         Use this prefix for unqualified URLs. E.g.
                                    "gvsearch2:python" downloads two videos from
                                    google videos for the search term "python".
                                    Use the value "auto" to let yt-dlp guess
                                    ("auto_warning" to emit a warning when
                                    guessing). "error" just throws an error. The
                                    default value "fixup_error" repairs broken
                                    URLs, but emits an error if this is not
                                    possible instead of searching
    --ignore-config                 Don't load any more configuration files
                                    except those given by --config-locations.
                                    For backward compatibility, if this option
                                    is found inside the system configuration
                                    file, the user configuration is not loaded.
                                    (Alias: --no-config)
    --no-config-locations           Do not load any custom configuration files
                                    (default). When given inside a configuration
                                    file, ignore all previous --config-locations
                                    defined in the current file
    --config-locations PATH         Location of the main configuration file;
                                    either the path to the config or its
                                    containing directory ("-" for stdin). Can be
                                    used multiple times and inside other
                                    configuration files
    --flat-playlist                 Do not extract the videos of a playlist,
                                    only list them
    --no-flat-playlist              Extract the videos of a playlist
    --live-from-start               Download livestreams from the start.
                                    Currently only supported for YouTube
                                    (Experimental)
    --no-live-from-start            Download livestreams from the current time
                                    (default)
    --wait-for-video MIN[-MAX]      Wait for scheduled streams to become
                                    available. Pass the minimum number of
                                    seconds (or range) to wait between retries
    --no-wait-for-video             Do not wait for scheduled streams (default)
    --mark-watched                  Mark videos watched (even with --simulate)
    --no-mark-watched               Do not mark videos watched (default)
    --no-colors                     Do not emit color codes in output (Alias:
                                    --no-colours)
    --compat-options OPTS           Options that can help keep compatibility
                                    with youtube-dl or youtube-dlc
                                    configurations by reverting some of the
                                    changes made in yt-dlp. See "Differences in
                                    default behavior" for details
    --alias ALIASES OPTIONS         Create aliases for an option string. Unless
                                    an alias starts with a dash "-", it is
                                    prefixed with "--". Arguments are parsed
                                    according to the Python string formatting
                                    mini-language. E.g. --alias get-audio,-X
                                    "-S=aext:{0},abr -x --audio-format {0}"
                                    creates options "--get-audio" and "-X" that
                                    takes an argument (ARG0) and expands to
                                    "-S=aext:ARG0,abr -x --audio-format ARG0".
                                    All defined aliases are listed in the --help
                                    output. Alias options can trigger more
                                    aliases; so be careful to avoid defining
                                    recursive options. As a safety measure, each
                                    alias may be triggered a maximum of 100
                                    times. This option can be used multiple
                                    times


Network Options:

    --proxy URL                     Use the specified HTTP/HTTPS/SOCKS proxy. To
                                    enable SOCKS proxy, specify a proper scheme,
                                    e.g. socks5://user:pass@127.0.0.1:1080/.
                                    Pass in an empty string (--proxy "") for
                                    direct connection
    --socket-timeout SECONDS        Time to wait before giving up, in seconds
    --source-address IP             Client-side IP address to bind to
    -4, --force-ipv4                Make all connections via IPv4
    -6, --force-ipv6                Make all connections via IPv6


Geo-restriction:

    --geo-verification-proxy URL    Use this proxy to verify the IP address for
                                    some geo-restricted sites. The default proxy
                                    specified by --proxy (or none, if the option
                                    is not present) is used for the actual
                                    downloading
    --geo-bypass                    Bypass geographic restriction via faking
                                    X-Forwarded-For HTTP header (default)
    --no-geo-bypass                 Do not bypass geographic restriction via
                                    faking X-Forwarded-For HTTP header
    --geo-bypass-country CODE       Force bypass geographic restriction with
                                    explicitly provided two-letter ISO 3166-2
                                    country code
    --geo-bypass-ip-block IP_BLOCK  Force bypass geographic restriction with
                                    explicitly provided IP block in CIDR
                                    notation


Video Selection:

    -I, --playlist-items ITEM_SPEC  Comma separated playlist_index of the videos
                                    to download. You can specify a range using
                                    "[START]:[STOP][:STEP]". For backward
                                    compatibility, START-STOP is also supported.
                                    Use negative indices to count from the right
                                    and negative STEP to download in reverse
                                    order. E.g. "-I 1:3,7,-5::2" used on a
                                    playlist of size 15 will download the videos
                                    at index 1,2,3,7,11,13,15
    --min-filesize SIZE             Abort download if filesize is smaller than
                                    SIZE, e.g. 50k or 44.6M
    --max-filesize SIZE             Abort download if filesize if larger than
                                    SIZE, e.g. 50k or 44.6M
    --date DATE                     Download only videos uploaded on this date.
                                    The date can be "YYYYMMDD" or in the format 
                                    [now|today|yesterday][-N[day|week|month|year
                                    ]]. E.g. --date today-2weeks
    --datebefore DATE               Download only videos uploaded on or before
                                    this date. The date formats accepted is the
                                    same as --date
    --dateafter DATE                Download only videos uploaded on or after
                                    this date. The date formats accepted is the
                                    same as --date
    --match-filters FILTER          Generic video filter. Any "OUTPUT TEMPLATE"
                                    field can be compared with a number or a
                                    string using the operators defined in
                                    "Filtering Formats". You can also simply
                                    specify a field to match if the field is
                                    present, use "!field" to check if the field
                                    is not present, and "&" to check multiple
                                    conditions. Use a "\" to escape "&" or
                                    quotes if needed. If used multiple times,
                                    the filter matches if atleast one of the
                                    conditions are met. E.g. --match-filter
                                    !is_live --match-filter "like_count>?100 &
                                    description~='(?i)\bcats \& dogs\b'" matches
                                    only videos that are not live OR those that
                                    have a like count more than 100 (or the like
                                    field is not available) and also has a
                                    description that contains the phrase "cats &
                                    dogs" (caseless). Use "--match-filter -" to
                                    interactively ask whether to download each
                                    video
    --no-match-filter               Do not use generic video filter (default)
    --no-playlist                   Download only the video, if the URL refers
                                    to a video and a playlist
    --yes-playlist                  Download the playlist, if the URL refers to
                                    a video and a playlist
    --age-limit YEARS               Download only videos suitable for the given
                                    age
    --download-archive FILE         Download only videos not listed in the
                                    archive file. Record the IDs of all
                                    downloaded videos in it
    --no-download-archive           Do not use archive file (default)
    --max-downloads NUMBER          Abort after downloading NUMBER files
    --break-on-existing             Stop the download process when encountering
                                    a file that is in the archive
    --break-on-reject               Stop the download process when encountering
                                    a file that has been filtered out
    --break-per-input               --break-on-existing, --break-on-reject,
                                    --max-downloads, and autonumber resets per
                                    input URL
    --no-break-per-input            --break-on-existing and similar options
                                    terminates the entire download queue
    --skip-playlist-after-errors N  Number of allowed failures until the rest of
                                    the playlist is skipped


Download Options:

    -N, --concurrent-fragments N    Number of fragments of a dash/hlsnative
                                    video that should be downloaded concurrently
                                    (default is 1)
    -r, --limit-rate RATE           Maximum download rate in bytes per second,
                                    e.g. 50K or 4.2M
    --throttled-rate RATE           Minimum download rate in bytes per second
                                    below which throttling is assumed and the
                                    video data is re-extracted, e.g. 100K
    -R, --retries RETRIES           Number of retries (default is 10), or
                                    "infinite"
    --file-access-retries RETRIES   Number of times to retry on file access
                                    error (default is 3), or "infinite"
    --fragment-retries RETRIES      Number of retries for a fragment (default is
                                    10), or "infinite" (DASH, hlsnative and ISM)
    --retry-sleep [TYPE:]EXPR       Time to sleep between retries in seconds
                                    (optionally) prefixed by the type of retry
                                    (http (default), fragment, file_access,
                                    extractor) to apply the sleep to. EXPR can
                                    be a number, linear=START[:END[:STEP=1]] or
                                    exp=START[:END[:BASE=2]]. This option can be
                                    used multiple times to set the sleep for the
                                    different retry types, e.g. --retry-sleep
                                    linear=1::2 --retry-sleep fragment:exp=1:20
    --skip-unavailable-fragments    Skip unavailable fragments for DASH,
                                    hlsnative and ISM downloads (default)
                                    (Alias: --no-abort-on-unavailable-fragment)
    --abort-on-unavailable-fragment
                                    Abort download if a fragment is unavailable
                                    (Alias: --no-skip-unavailable-fragments)
    --keep-fragments                Keep downloaded fragments on disk after
                                    downloading is finished
    --no-keep-fragments             Delete downloaded fragments after
                                    downloading is finished (default)
    --buffer-size SIZE              Size of download buffer, e.g. 1024 or 16K
                                    (default is 1024)
    --resize-buffer                 The buffer size is automatically resized
                                    from an initial value of --buffer-size
                                    (default)
    --no-resize-buffer              Do not automatically adjust the buffer size
    --http-chunk-size SIZE          Size of a chunk for chunk-based HTTP
                                    downloading, e.g. 10485760 or 10M (default
                                    is disabled). May be useful for bypassing
                                    bandwidth throttling imposed by a webserver
                                    (experimental)
    --playlist-random               Download playlist videos in random order
    --lazy-playlist                 Process entries in the playlist as they are
                                    received. This disables n_entries,
                                    --playlist-random and --playlist-reverse
    --no-lazy-playlist              Process videos in the playlist only after
                                    the entire playlist is parsed (default)
    --xattr-set-filesize            Set file xattribute ytdl.filesize with
                                    expected file size
    --hls-use-mpegts                Use the mpegts container for HLS videos;
                                    allowing some players to play the video
                                    while downloading, and reducing the chance
                                    of file corruption if download is
                                    interrupted. This is enabled by default for
                                    live streams
    --no-hls-use-mpegts             Do not use the mpegts container for HLS
                                    videos. This is default when not downloading
                                    live streams
    --download-sections REGEX       Download only chapters whose title matches
                                    the given regular expression. Time ranges
                                    prefixed by a "*" can also be used in place
                                    of chapters to download the specified range.
                                    Needs ffmpeg. This option can be used
                                    multiple times to download multiple
                                    sections, e.g. --download-sections
                                    "*10:15-inf" --download-sections "intro"
    --downloader [PROTO:]NAME       Name or path of the external downloader to
                                    use (optionally) prefixed by the protocols
                                    (http, ftp, m3u8, dash, rstp, rtmp, mms) to
                                    use it for. Currently supports native,
                                    aria2c, avconv, axel, curl, ffmpeg, httpie,
                                    wget. You can use this option multiple times
                                    to set different downloaders for different
                                    protocols. E.g. --downloader aria2c
                                    --downloader "dash,m3u8:native" will use
                                    aria2c for http/ftp downloads, and the
                                    native downloader for dash/m3u8 downloads
                                    (Alias: --external-downloader)
    --downloader-args NAME:ARGS     Give these arguments to the external
                                    downloader. Specify the downloader name and
                                    the arguments separated by a colon ":". For
                                    ffmpeg, arguments can be passed to different
                                    positions using the same syntax as
                                    --postprocessor-args. You can use this
                                    option multiple times to give different
                                    arguments to different downloaders (Alias:
                                    --external-downloader-args)


Filesystem Options:

    -a, --batch-file FILE           File containing URLs to download ("-" for
                                    stdin), one URL per line. Lines starting
                                    with "#", ";" or "]" are considered as
                                    comments and ignored
    --no-batch-file                 Do not read URLs from batch file (default)
    -P, --paths [TYPES:]PATH        The paths where the files should be
                                    downloaded. Specify the type of file and the
                                    path separated by a colon ":". All the same
                                    TYPES as --output are supported.
                                    Additionally, you can also provide "home"
                                    (default) and "temp" paths. All intermediary
                                    files are first downloaded to the temp path
                                    and then the final files are moved over to
                                    the home path after download is finished.
                                    This option is ignored if --output is an
                                    absolute path
    -o, --output [TYPES:]TEMPLATE   Output filename template; see "OUTPUT
                                    TEMPLATE" for details
    --output-na-placeholder TEXT    Placeholder for unavailable fields in
                                    "OUTPUT TEMPLATE" (default: "NA")
    --restrict-filenames            Restrict filenames to only ASCII characters,
                                    and avoid "&" and spaces in filenames
    --no-restrict-filenames         Allow Unicode characters, "&" and spaces in
                                    filenames (default)
    --windows-filenames             Force filenames to be Windows-compatible
    --no-windows-filenames          Make filenames Windows-compatible only if
                                    using Windows (default)
    --trim-filenames LENGTH         Limit the filename length (excluding
                                    extension) to the specified number of
                                    characters
    -w, --no-overwrites             Do not overwrite any files
    --force-overwrites              Overwrite all video and metadata files. This
                                    option includes --no-continue
    --no-force-overwrites           Do not overwrite the video, but overwrite
                                    related files (default)
    -c, --continue                  Resume partially downloaded files/fragments
                                    (default)
    --no-continue                   Do not resume partially downloaded
                                    fragments. If the file is not fragmented,
                                    restart download of the entire file
    --part                          Use .part files instead of writing directly
                                    into output file (default)
    --no-part                       Do not use .part files - write directly into
                                    output file
    --mtime                         Use the Last-modified header to set the file
                                    modification time (default)
    --no-mtime                      Do not use the Last-modified header to set
                                    the file modification time
    --write-description             Write video description to a .description
                                    file
    --no-write-description          Do not write video description (default)
    --write-info-json               Write video metadata to a .info.json file
                                    (this may contain personal information)
    --no-write-info-json            Do not write video metadata (default)
    --write-playlist-metafiles      Write playlist metadata in addition to the
                                    video metadata when using --write-info-json,
                                    --write-description etc. (default)
    --no-write-playlist-metafiles   Do not write playlist metadata when using
                                    --write-info-json, --write-description etc.
    --clean-info-json               Remove some private fields such as filenames
                                    from the infojson. Note that it could still
                                    contain some personal information (default)
    --no-clean-info-json            Write all fields to the infojson
    --write-comments                Retrieve video comments to be placed in the
                                    infojson. The comments are fetched even
                                    without this option if the extraction is
                                    known to be quick (Alias: --get-comments)
    --no-write-comments             Do not retrieve video comments unless the
                                    extraction is known to be quick (Alias:
                                    --no-get-comments)
    --load-info-json FILE           JSON file containing the video information
                                    (created with the "--write-info-json"
                                    option)
    --cookies FILE                  Netscape formatted file to read cookies from
                                    and dump cookie jar in
    --no-cookies                    Do not read/dump cookies from/to file
                                    (default)
    --cookies-from-browser BROWSER[+KEYRING][:PROFILE][::CONTAINER]
                                    The name of the browser to load cookies
                                    from. Currently supported browsers are:
                                    brave, chrome, chromium, edge, firefox,
                                    opera, safari, vivaldi. Optionally, the
                                    KEYRING used for decrypting Chromium cookies
                                    on Linux, the name/path of the PROFILE to
                                    load cookies from, and the CONTAINER name
                                    (if Firefox) ("none" for no container) can
                                    be given with their respective seperators.
                                    By default, all containers of the most
                                    recently accessed profile are used.
                                    Currently supported keyrings are: basictext,
                                    gnomekeyring, kwallet
    --no-cookies-from-browser       Do not load cookies from browser (default)
    --cache-dir DIR                 Location in the filesystem where yt-dlp can
                                    store some downloaded information (such as
                                    client ids and signatures) permanently. By
                                    default ${XDG_CACHE_HOME}/yt-dlp
    --no-cache-dir                  Disable filesystem caching
    --rm-cache-dir                  Delete all filesystem cache files


Thumbnail Options:

    --write-thumbnail               Write thumbnail image to disk
    --no-write-thumbnail            Do not write thumbnail image to disk
                                    (default)
    --write-all-thumbnails          Write all thumbnail image formats to disk
    --list-thumbnails               List available thumbnails of each video.
                                    Simulate unless --no-simulate is used


Internet Shortcut Options:

    --write-link                    Write an internet shortcut file, depending
                                    on the current platform (.url, .webloc or
                                    .desktop). The URL may be cached by the OS
    --write-url-link                Write a .url Windows internet shortcut. The
                                    OS caches the URL based on the file path
    --write-webloc-link             Write a .webloc macOS internet shortcut
    --write-desktop-link            Write a .desktop Linux internet shortcut


Verbosity and Simulation Options:

    -q, --quiet                     Activate quiet mode. If used with --verbose,
                                    print the log to stderr
    --no-warnings                   Ignore warnings
    -s, --simulate                  Do not download the video and do not write
                                    anything to disk
    --no-simulate                   Download the video even if printing/listing
                                    options are used
    --ignore-no-formats-error       Ignore "No video formats" error. Useful for
                                    extracting metadata even if the videos are
                                    not actually available for download
                                    (experimental)
    --no-ignore-no-formats-error    Throw error when no downloadable video
                                    formats are found (default)
    --skip-download                 Do not download the video but write all
                                    related files (Alias: --no-download)
    -O, --print [WHEN:]TEMPLATE     Field name or output template to print to
                                    screen, optionally prefixed with when to
                                    print it, separated by a ":". Supported
                                    values of "WHEN" are the same as that of
                                    --use-postprocessor, and "video" (default).
                                    Implies --quiet. Implies --simulate unless
                                    --no-simulate or later stages of WHEN are
                                    used. This option can be used multiple times
    --print-to-file [WHEN:]TEMPLATE FILE
                                    Append given template to the file. The
                                    values of WHEN and TEMPLATE are same as that
                                    of --print. FILE uses the same syntax as the
                                    output template. This option can be used
                                    multiple times
    -j, --dump-json                 Quiet, but print JSON information for each
                                    video. Simulate unless --no-simulate is
                                    used. See "OUTPUT TEMPLATE" for a
                                    description of available keys
    -J, --dump-single-json          Quiet, but print JSON information for each
                                    url or infojson passed. Simulate unless
                                    --no-simulate is used. If the URL refers to
                                    a playlist, the whole playlist information
                                    is dumped in a single line
    --force-write-archive           Force download archive entries to be written
                                    as far as no errors occur, even if -s or
                                    another simulation option is used (Alias:
                                    --force-download-archive)
    --newline                       Output progress bar as new lines
    --no-progress                   Do not print progress bar
    --progress                      Show progress bar, even if in quiet mode
    --console-title                 Display progress in console titlebar
    --progress-template [TYPES:]TEMPLATE
                                    Template for progress outputs, optionally
                                    prefixed with one of "download:" (default),
                                    "download-title:" (the console title),
                                    "postprocess:",  or "postprocess-title:".
                                    The video's fields are accessible under the
                                    "info" key and the progress attributes are
                                    accessible under "progress" key. E.g.
                                    --console-title --progress-template
                                    "download-
                                    title:%(info.id)s-%(progress.eta)s"
    -v, --verbose                   Print various debugging information
    --dump-pages                    Print downloaded pages encoded using base64
                                    to debug problems (very verbose)
    --write-pages                   Write downloaded intermediary pages to files
                                    in the current directory to debug problems
    --print-traffic                 Display sent and read HTTP traffic


Workarounds:

    --encoding ENCODING             Force the specified encoding (experimental)
    --legacy-server-connect         Explicitly allow HTTPS connection to servers
                                    that do not support RFC 5746 secure
                                    renegotiation
    --no-check-certificates         Suppress HTTPS certificate validation
    --prefer-insecure               Use an unencrypted connection to retrieve
                                    information about the video (Currently
                                    supported only for YouTube)
    --add-header FIELD:VALUE        Specify a custom HTTP header and its value,
                                    separated by a colon ":". You can use this
                                    option multiple times
    --bidi-workaround               Work around terminals that lack
                                    bidirectional text support. Requires bidiv
                                    or fribidi executable in PATH
    --sleep-requests SECONDS        Number of seconds to sleep between requests
                                    during data extraction
    --sleep-interval SECONDS        Number of seconds to sleep before each
                                    download. This is the minimum time to sleep
                                    when used along with --max-sleep-interval
                                    (Alias: --min-sleep-interval)
    --max-sleep-interval SECONDS    Maximum number of seconds to sleep. Can only
                                    be used along with --min-sleep-interval
    --sleep-subtitles SECONDS       Number of seconds to sleep before each
                                    subtitle download


Video Format Options:

    -f, --format FORMAT             Video format code, see "FORMAT SELECTION"
                                    for more details
    -S, --format-sort SORTORDER     Sort the formats by the fields given, see
                                    "Sorting Formats" for more details
    --format-sort-force             Force user specified sort order to have
                                    precedence over all fields, see "Sorting
                                    Formats" for more details (Alias: --S-force)
    --no-format-sort-force          Some fields have precedence over the user
                                    specified sort order (default)
    --video-multistreams            Allow multiple video streams to be merged
                                    into a single file
    --no-video-multistreams         Only one video stream is downloaded for each
                                    output file (default)
    --audio-multistreams            Allow multiple audio streams to be merged
                                    into a single file
    --no-audio-multistreams         Only one audio stream is downloaded for each
                                    output file (default)
    --prefer-free-formats           Prefer video formats with free containers
                                    over non-free ones of same quality. Use with
                                    "-S ext" to strictly prefer free containers
                                    irrespective of quality
    --no-prefer-free-formats        Don't give any special preference to free
                                    containers (default)
    --check-formats                 Make sure formats are selected only from
                                    those that are actually downloadable
    --check-all-formats             Check all formats for whether they are
                                    actually downloadable
    --no-check-formats              Do not check that the formats are actually
                                    downloadable
    -F, --list-formats              List available formats of each video.
                                    Simulate unless --no-simulate is used
    --merge-output-format FORMAT    Containers that may be used when merging
                                    formats, separated by "/", e.g. "mp4/mkv".
                                    Ignored if no merge is required. (currently
                                    supported: avi, flv, mkv, mov, mp4, webm)


Subtitle Options:

    --write-subs                    Write subtitle file
    --no-write-subs                 Do not write subtitle file (default)
    --write-auto-subs               Write automatically generated subtitle file
                                    (Alias: --write-automatic-subs)
    --no-write-auto-subs            Do not write auto-generated subtitles
                                    (default) (Alias: --no-write-automatic-subs)
    --list-subs                     List available subtitles of each video.
                                    Simulate unless --no-simulate is used
    --sub-format FORMAT             Subtitle format; accepts formats preference,
                                    e.g. "srt" or "ass/srt/best"
    --sub-langs LANGS               Languages of the subtitles to download (can
                                    be regex) or "all" separated by commas, e.g.
                                    --sub-langs "en.*,ja". You can prefix the
                                    language code with a "-" to exclude it from
                                    the requested languages, e.g. --sub-langs
                                    all,-live_chat. Use --list-subs for a list
                                    of available language tags


Authentication Options:

    -u, --username USERNAME         Login with this account ID
    -p, --password PASSWORD         Account password. If this option is left
                                    out, yt-dlp will ask interactively
    -2, --twofactor TWOFACTOR       Two-factor authentication code
    -n, --netrc                     Use .netrc authentication data
    --netrc-location PATH           Location of .netrc authentication data;
                                    either the path or its containing directory.
                                    Defaults to ~/.netrc
    --video-password PASSWORD       Video password (vimeo, youku)
    --ap-mso MSO                    Adobe Pass multiple-system operator (TV
                                    provider) identifier, use --ap-list-mso for
                                    a list of available MSOs
    --ap-username USERNAME          Multiple-system operator account login
    --ap-password PASSWORD          Multiple-system operator account password.
                                    If this option is left out, yt-dlp will ask
                                    interactively
    --ap-list-mso                   List all supported multiple-system operators
    --client-certificate CERTFILE   Path to client certificate file in PEM
                                    format. May include the private key
    --client-certificate-key KEYFILE
                                    Path to private key file for client
                                    certificate
    --client-certificate-password PASSWORD
                                    Password for client certificate private key,
                                    if encrypted. If not provided, and the key
                                    is encrypted, yt-dlp will ask interactively


Post-Processing Options:

    -x, --extract-audio             Convert video files to audio-only files
                                    (requires ffmpeg and ffprobe)
    --audio-format FORMAT           Format to convert the audio to when -x is
                                    used. (currently supported: best (default),
                                    aac, alac, flac, m4a, mp3, opus, vorbis,
                                    wav). You can specify multiple rules using
                                    similar syntax as --remux-video
    --audio-quality QUALITY         Specify ffmpeg audio quality to use when
                                    converting the audio with -x. Insert a value
                                    between 0 (best) and 10 (worst) for VBR or a
                                    specific bitrate like 128K (default 5)
    --remux-video FORMAT            Remux the video into another container if
                                    necessary (currently supported: avi, flv,
                                    mkv, mov, mp4, webm, aac, aiff, alac, flac,
                                    m4a, mka, mp3, ogg, opus, vorbis, wav). If
                                    target container does not support the
                                    video/audio codec, remuxing will fail. You
                                    can specify multiple rules; e.g.
                                    "aac>m4a/mov>mp4/mkv" will remux aac to m4a,
                                    mov to mp4 and anything else to mkv
    --recode-video FORMAT           Re-encode the video into another format if
                                    necessary. The syntax and supported formats
                                    are the same as --remux-video
    --postprocessor-args NAME:ARGS  Give these arguments to the postprocessors.
                                    Specify the postprocessor/executable name
                                    and the arguments separated by a colon ":"
                                    to give the argument to the specified
                                    postprocessor/executable. Supported PP are:
                                    Merger, ModifyChapters, SplitChapters,
                                    ExtractAudio, VideoRemuxer, VideoConvertor,
                                    Metadata, EmbedSubtitle, EmbedThumbnail,
                                    SubtitlesConvertor, ThumbnailsConvertor,
                                    FixupStretched, FixupM4a, FixupM3u8,
                                    FixupTimestamp and FixupDuration. The
                                    supported executables are: AtomicParsley,
                                    FFmpeg and FFprobe. You can also specify
                                    "PP+EXE:ARGS" to give the arguments to the
                                    specified executable only when being used by
                                    the specified postprocessor. Additionally,
                                    for ffmpeg/ffprobe, "_i"/"_o" can be
                                    appended to the prefix optionally followed
                                    by a number to pass the argument before the
                                    specified input/output file, e.g. --ppa
                                    "Merger+ffmpeg_i1:-v quiet". You can use
                                    this option multiple times to give different
                                    arguments to different postprocessors.
                                    (Alias: --ppa)
    -k, --keep-video                Keep the intermediate video file on disk
                                    after post-processing
    --no-keep-video                 Delete the intermediate video file after
                                    post-processing (default)
    --post-overwrites               Overwrite post-processed files (default)
    --no-post-overwrites            Do not overwrite post-processed files
    --embed-subs                    Embed subtitles in the video (only for mp4,
                                    webm and mkv videos)
    --no-embed-subs                 Do not embed subtitles (default)
    --embed-thumbnail               Embed thumbnail in the video as cover art
    --no-embed-thumbnail            Do not embed thumbnail (default)
    --embed-metadata                Embed metadata to the video file. Also
                                    embeds chapters/infojson if present unless
                                    --no-embed-chapters/--no-embed-info-json are
                                    used (Alias: --add-metadata)
    --no-embed-metadata             Do not add metadata to file (default)
                                    (Alias: --no-add-metadata)
    --embed-chapters                Add chapter markers to the video file
                                    (Alias: --add-chapters)
    --no-embed-chapters             Do not add chapter markers (default) (Alias:
                                    --no-add-chapters)
    --embed-info-json               Embed the infojson as an attachment to
                                    mkv/mka video files
    --no-embed-info-json            Do not embed the infojson as an attachment
                                    to the video file
    --parse-metadata FROM:TO        Parse additional metadata like title/artist
                                    from other fields; see "MODIFYING METADATA"
                                    for details
    --replace-in-metadata FIELDS REGEX REPLACE
                                    Replace text in a metadata field using the
                                    given regex. This option can be used
                                    multiple times
    --xattrs                        Write metadata to the video file's xattrs
                                    (using dublin core and xdg standards)
    --concat-playlist POLICY        Concatenate videos in a playlist. One of
                                    "never", "always", or "multi_video"
                                    (default; only when the videos form a single
                                    show). All the video files must have same
                                    codecs and number of streams to be
                                    concatable. The "pl_video:" prefix can be
                                    used with "--paths" and "--output" to set
                                    the output filename for the concatenated
                                    files. See "OUTPUT TEMPLATE" for details
    --fixup POLICY                  Automatically correct known faults of the
                                    file. One of never (do nothing), warn (only
                                    emit a warning), detect_or_warn (the
                                    default; fix file if we can, warn
                                    otherwise), force (try fixing even if file
                                    already exists)
    --ffmpeg-location PATH          Location of the ffmpeg binary; either the
                                    path to the binary or its containing
                                    directory
    --exec [WHEN:]CMD               Execute a command, optionally prefixed with
                                    when to execute it (after_move if
                                    unspecified), separated by a ":". Supported
                                    values of "WHEN" are the same as that of
                                    --use-postprocessor. Same syntax as the
                                    output template can be used to pass any
                                    field as arguments to the command. After
                                    download, an additional field "filepath"
                                    that contains the final path of the
                                    downloaded file is also available, and if no
                                    fields are passed, %(filepath)q is appended
                                    to the end of the command. This option can
                                    be used multiple times
    --no-exec                       Remove any previously defined --exec
    --convert-subs FORMAT           Convert the subtitles to another format
                                    (currently supported: ass, lrc, srt, vtt)
                                    (Alias: --convert-subtitles)
    --convert-thumbnails FORMAT     Convert the thumbnails to another format
                                    (currently supported: jpg, png, webp). You
                                    can specify multiple rules using similar
                                    syntax as --remux-video
    --split-chapters                Split video into multiple files based on
                                    internal chapters. The "chapter:" prefix can
                                    be used with "--paths" and "--output" to set
                                    the output filename for the split files. See
                                    "OUTPUT TEMPLATE" for details
    --no-split-chapters             Do not split video based on chapters
                                    (default)
    --remove-chapters REGEX         Remove chapters whose title matches the
                                    given regular expression. The syntax is the
                                    same as --download-sections. This option can
                                    be used multiple times
    --no-remove-chapters            Do not remove any chapters from the file
                                    (default)
    --force-keyframes-at-cuts       Force keyframes at cuts when
                                    downloading/splitting/removing sections.
                                    This is slow due to needing a re-encode, but
                                    the resulting video may have fewer artifacts
                                    around the cuts
    --no-force-keyframes-at-cuts    Do not force keyframes around the chapters
                                    when cutting/splitting (default)
    --use-postprocessor NAME[:ARGS]
                                    The (case sensitive) name of plugin
                                    postprocessors to be enabled, and
                                    (optionally) arguments to be passed to it,
                                    separated by a colon ":". ARGS are a
                                    semicolon ";" delimited list of NAME=VALUE.
                                    The "when" argument determines when the
                                    postprocessor is invoked. It can be one of
                                    "pre_process" (after video extraction),
                                    "after_filter" (after video passes filter),
                                    "before_dl" (before each video download),
                                    "post_process" (after each video download;
                                    default), "after_move" (after moving video
                                    file to it's final locations), "after_video"
                                    (after downloading and processing all
                                    formats of a video), or "playlist" (at end
                                    of playlist). This option can be used
                                    multiple times to add different
                                    postprocessors


SponsorBlock Options:

    Make chapter entries for, or remove various segments (sponsor,
    introductions, etc.) from downloaded YouTube videos using the
    SponsorBlock API (https://sponsor.ajay.app)

    --sponsorblock-mark CATS        SponsorBlock categories to create chapters
                                    for, separated by commas. Available
                                    categories are sponsor, intro, outro,
                                    selfpromo, preview, filler, interaction,
                                    music_offtopic, poi_highlight, chapter, all
                                    and default (=all). You can prefix the
                                    category with a "-" to exclude it. See [1]
                                    for description of the categories. E.g.
                                    --sponsorblock-mark all,-preview [1] https:/
                                    /wiki.sponsor.ajay.app/w/Segment_Categories
    --sponsorblock-remove CATS      SponsorBlock categories to be removed from
                                    the video file, separated by commas. If a
                                    category is present in both mark and remove,
                                    remove takes precedence. The syntax and
                                    available categories are the same as for
                                    --sponsorblock-mark except that "default"
                                    refers to "all,-filler" and poi_highlight,
                                    chapter are not available
    --sponsorblock-chapter-title TEMPLATE
                                    An output template for the title of the
                                    SponsorBlock chapters created by
                                    --sponsorblock-mark. The only available
                                    fields are start_time, end_time, category,
                                    categories, name, category_names. Defaults
                                    to "[SponsorBlock]: %(category_names)l"
    --no-sponsorblock               Disable both --sponsorblock-mark and
                                    --sponsorblock-remove
    --sponsorblock-api URL          SponsorBlock API location, defaults to
                                    https://sponsor.ajay.app


Extractor Options:

    --extractor-retries RETRIES     Number of retries for known extractor errors
                                    (default is 3), or "infinite"
    --allow-dynamic-mpd             Process dynamic DASH manifests (default)
                                    (Alias: --no-ignore-dynamic-mpd)
    --ignore-dynamic-mpd            Do not process dynamic DASH manifests
                                    (Alias: --no-allow-dynamic-mpd)
    --hls-split-discontinuity       Split HLS playlists to different formats at
                                    discontinuities such as ad breaks
    --no-hls-split-discontinuity    Do not split HLS playlists to different
                                    formats at discontinuities such as ad breaks
                                    (default)
    --extractor-args IE_KEY:ARGS    Pass ARGS arguments to the IE_KEY extractor.
                                    See "EXTRACTOR ARGUMENTS" for details. You
                                    can use this option multiple times to give
                                    arguments for different extractors

See full documentation at https://github.com/yt-dlp/yt-dlp#readme



CONFIGURATION


You can configure picta-dl by placing any supported command line option
to a configuration file. On Linux and macOS, the system wide
configuration file is located at /etc/picta-dl.conf and the user wide
configuration file at ~/.config/picta-dl/config. On Windows, the user
wide configuration file locations are %APPDATA%\picta-dl\config.txt or
C:\Users\<user name>\picta-dl.conf. Note that by default configuration
file may not exist so you may need to create it yourself.

For example, with the following configuration file picta-dl will always
extract the audio, not copy the mtime, use a proxy and save all videos
under Movies directory in your home directory:

    # Lines starting with # are comments

    # Always extract audio
    -x

    # Do not copy the mtime
    --no-mtime

    # Use this proxy
    --proxy 127.0.0.1:3128

    # Save all videos under Movies directory in your home directory
    -o ~/Movies/%(title)s.%(ext)s

Note that options in configuration file are just the same options aka
switches used in regular command line calls thus there MUST BE NO
WHITESPACE after - or --, e.g. -o or --proxy but not - o or -- proxy.

You can use --ignore-config if you want to disable the configuration
file for a particular picta-dl run.

You can also use --config-location if you want to use custom
configuration file for a particular picta-dl run.

Authentication with .netrc file

You may also want to configure automatic credentials storage for
extractors that support authentication (by providing login and password
with --username and --password) in order not to pass credentials as
command line arguments on every picta-dl execution and prevent tracking
plain text passwords in the shell command history. You can achieve this
using a .netrc file on a per extractor basis. For that you will need to
create a .netrc file in your $HOME and restrict permissions to
read/write by only you:

    touch $HOME/.netrc
    chmod a-rwx,u+rw $HOME/.netrc

After that you can add credentials for an extractor in the following
format, where _extractor_ is the name of the extractor in lowercase:

    machine <extractor> login <login> password <password>

For example:

    machine youtube login myaccount@gmail.com password my_youtube_password
    machine twitch login my_twitch_account_name password my_twitch_password

To activate authentication with the .netrc file you should pass --netrc
to picta-dl or place it in the configuration file.

On Windows you may also need to setup the %HOME% environment variable
manually. For example:

    set HOME=%USERPROFILE%



OUTPUT TEMPLATE


The -o option allows users to indicate a template for the output file
names.

TL;DR: navigate me to examples.

The basic usage is not to set any template arguments when downloading a
single file, like in picta-dl -o funny_video.flv "https://some/video".
However, it may contain special sequences that will be replaced when
downloading each video. The special sequences may be formatted according
to python string formatting operations. For example, %(NAME)s or
%(NAME)05d. To clarify, that is a percent symbol followed by a name in
parentheses, followed by formatting operations. Allowed names along with
sequence type are:

-   id (string): Video identifier
-   title (string): Video title
-   url (string): Video URL
-   ext (string): Video filename extension
-   alt_title (string): A secondary title of the video
-   display_id (string): An alternative identifier for the video
-   uploader (string): Full name of the video uploader
-   license (string): License name the video is licensed under
-   creator (string): The creator of the video
-   release_date (string): The date (YYYYMMDD) when the video was
    released
-   timestamp (numeric): UNIX timestamp of the moment the video became
    available
-   upload_date (string): Video upload date (YYYYMMDD)
-   uploader_id (string): Nickname or id of the video uploader
-   channel (string): Full name of the channel the video is uploaded on
-   channel_id (string): Id of the channel
-   location (string): Physical location where the video was filmed
-   duration (numeric): Length of the video in seconds
-   view_count (numeric): How many users have watched the video on the
    platform
-   like_count (numeric): Number of positive ratings of the video
-   dislike_count (numeric): Number of negative ratings of the video
-   repost_count (numeric): Number of reposts of the video
-   average_rating (numeric): Average rating give by users, the scale
    used depends on the webpage
-   comment_count (numeric): Number of comments on the video
-   age_limit (numeric): Age restriction for the video (years)
-   is_live (boolean): Whether this video is a live stream or a
    fixed-length video
-   start_time (numeric): Time in seconds where the reproduction should
    start, as specified in the URL
-   end_time (numeric): Time in seconds where the reproduction should
    end, as specified in the URL
-   format (string): A human-readable description of the format
-   format_id (string): Format code specified by --format
-   format_note (string): Additional info about the format
-   width (numeric): Width of the video
-   height (numeric): Height of the video
-   resolution (string): Textual description of width and height
-   tbr (numeric): Average bitrate of audio and video in KBit/s
-   abr (numeric): Average audio bitrate in KBit/s
-   acodec (string): Name of the audio codec in use
-   asr (numeric): Audio sampling rate in Hertz
-   vbr (numeric): Average video bitrate in KBit/s
-   fps (numeric): Frame rate
-   vcodec (string): Name of the video codec in use
-   container (string): Name of the container format
-   filesize (numeric): The number of bytes, if known in advance
-   filesize_approx (numeric): An estimate for the number of bytes
-   protocol (string): The protocol that will be used for the actual
    download
-   extractor (string): Name of the extractor
-   extractor_key (string): Key name of the extractor
-   epoch (numeric): Unix epoch when creating the file
-   autonumber (numeric): Five-digit number that will be increased with
    each download, starting at zero
-   playlist (string): Name or id of the playlist that contains the
    video
-   playlist_index (numeric): Index of the video in the playlist padded
    with leading zeros according to the total length of the playlist
-   playlist_id (string): Playlist identifier
-   playlist_title (string): Playlist title
-   playlist_uploader (string): Full name of the playlist uploader
-   playlist_uploader_id (string): Nickname or id of the playlist
    uploader

Available for the video that belongs to some logical chapter or section:

-   chapter (string): Name or title of the chapter the video belongs to
-   chapter_number (numeric): Number of the chapter the video belongs to
-   chapter_id (string): Id of the chapter the video belongs to

Available for the video that is an episode of some series or programme:

-   series (string): Title of the series or programme the video episode
    belongs to
-   season (string): Title of the season the video episode belongs to
-   season_number (numeric): Number of the season the video episode
    belongs to
-   season_id (string): Id of the season the video episode belongs to
-   episode (string): Title of the video episode
-   episode_number (numeric): Number of the video episode within a
    season
-   episode_id (string): Id of the video episode

Available for the media that is a track or a part of a music album:

-   track (string): Title of the track
-   track_number (numeric): Number of the track within an album or a
    disc
-   track_id (string): Id of the track
-   artist (string): Artist(s) of the track
-   genre (string): Genre(s) of the track
-   album (string): Title of the album the track belongs to
-   album_type (string): Type of the album
-   album_artist (string): List of all artists appeared on the album
-   disc_number (numeric): Number of the disc or other physical medium
    the track belongs to
-   release_year (numeric): Year (YYYY) when the album was released

Each aforementioned sequence when referenced in an output template will
be replaced by the actual value corresponding to the sequence name. Note
that some of the sequences are not guaranteed to be present since they
depend on the metadata obtained by a particular extractor. Such
sequences will be replaced with NA.

For example for -o %(title)s-%(id)s.%(ext)s and an mp4 video with title
picta-dl test video and id BaW_jenozKcj, this will result in a
picta-dl test video-BaW_jenozKcj.mp4 file created in the current
directory.

For numeric sequences you can use numeric related formatting, for
example, %(view_count)05d will result in a string with view count padded
with zeros up to 5 characters, like in 00042.

Output templates can also contain arbitrary hierarchical path, e.g.
-o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' which will
result in downloading each video in a directory corresponding to this
path template. Any missing directory will be automatically created for
you.

To use percent literals in an output template use %%. To output to
stdout use -o -.

The current default template is %(title)s-%(id)s.%(ext)s.

In some cases, you don't want special characters such as 中, spaces, or
&, such as when transferring the downloaded filename to a Windows system
or the filename through an 8bit-unsafe channel. In these cases, add the
--restrict-filenames flag to get a shorter title:

Output template and Windows batch files

If you are using an output template inside a Windows batch file then you
must escape plain percent characters (%) by doubling, so that
-o "%(title)s-%(id)s.%(ext)s" should become
-o "%%(title)s-%%(id)s.%%(ext)s". However you should not touch %'s that
are not plain characters, e.g. environment variables for expansion
should stay intact: -o "C:\%HOMEPATH%\Desktop\%%(title)s.%%(ext)s".

Output template examples

Note that on Windows you may need to use double quotes instead of
single.

    $ picta-dl --get-filename -o '%(title)s.%(ext)s' BaW_jenozKc
    picta-dl test video ''_ä↭𝕐.mp4    # All kinds of weird characters

    $ picta-dl --get-filename -o '%(title)s.%(ext)s' BaW_jenozKc --restrict-filenames
    picta-dl_test_video_.mp4          # A simple file name

    # Download YouTube playlist videos in separate directory indexed by video order in a playlist
    $ picta-dl -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' https://www.youtube.com/playlist?list=PLwiyx1dc3P2JR9N8gQaQN_BCvlSlap7re

    # Download all playlists of YouTube channel/user keeping each playlist in separate directory:
    $ picta-dl -o '%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' https://www.youtube.com/user/TheLinuxFoundation/playlists

    # Download Udemy course keeping each chapter in separate directory under MyVideos directory in your home
    $ picta-dl -u user -p password -o '~/MyVideos/%(playlist)s/%(chapter_number)s - %(chapter)s/%(title)s.%(ext)s' https://www.udemy.com/java-tutorial/

    # Download entire series season keeping each series and each season in separate directory under C:/MyVideos
    $ picta-dl -o "C:/MyVideos/%(series)s/%(season_number)s - %(season)s/%(episode_number)s - %(episode)s.%(ext)s" https://videomore.ru/kino_v_detalayah/5_sezon/367617

    # Stream the video being downloaded to stdout
    $ picta-dl -o - BaW_jenozKc



FORMAT SELECTION


By default picta-dl tries to download the best available quality, i.e.
if you want the best quality you DON'T NEED to pass any special options,
picta-dl will guess it for you by DEFAULT.

But sometimes you may want to download in a different format, for
example when you are on a slow or intermittent connection. The key
mechanism for achieving this is so-called _format selection_ based on
which you can explicitly specify desired format, select formats based on
some criterion or criteria, setup precedence and much more.

The general syntax for format selection is --format FORMAT or shorter
-f FORMAT where FORMAT is a _selector expression_, i.e. an expression
that describes format or formats you would like to download.

TL;DR: navigate me to examples.

The simplest case is requesting a specific format, for example with
-f 22 you can download the format with format code equal to 22. You can
get the list of available format codes for particular video using
--list-formats or -F. Note that these format codes are extractor
specific.

You can also use a file extension (currently 3gp, aac, flv, m4a, mp3,
mp4, ogg, wav, webm are supported) to download the best quality format
of a particular file extension served as a single file, e.g. -f webm
will download the best quality format with the webm extension served as
a single file.

You can also use special names to select particular edge case formats:

-   best: Select the best quality format represented by a single file
    with video and audio.
-   worst: Select the worst quality format represented by a single file
    with video and audio.
-   bestvideo: Select the best quality video-only format (e.g. DASH
    video). May not be available.
-   worstvideo: Select the worst quality video-only format. May not be
    available.
-   bestaudio: Select the best quality audio only-format. May not be
    available.
-   worstaudio: Select the worst quality audio only-format. May not be
    available.

For example, to download the worst quality video-only format you can use
-f worstvideo.

If you want to download multiple videos and they don't have the same
formats available, you can specify the order of preference using
slashes. Note that slash is left-associative, i.e. formats on the left
hand side are preferred, for example -f 22/17/18 will download format 22
if it's available, otherwise it will download format 17 if it's
available, otherwise it will download format 18 if it's available,
otherwise it will complain that no suitable formats are available for
download.

If you want to download several formats of the same video use a comma as
a separator, e.g. -f 22,17,18 will download all these three formats, of
course if they are available. Or a more sophisticated example combined
with the precedence feature: -f 136/137/mp4/bestvideo,140/m4a/bestaudio.

You can also filter the video formats by putting a condition in
brackets, as in -f "best[height=720]" (or -f "[filesize>10M]").

The following numeric meta fields can be used with comparisons <, <=, >,
>=, = (equals), != (not equals):

-   filesize: The number of bytes, if known in advance
-   width: Width of the video, if known
-   height: Height of the video, if known
-   tbr: Average bitrate of audio and video in KBit/s
-   abr: Average audio bitrate in KBit/s
-   vbr: Average video bitrate in KBit/s
-   asr: Audio sampling rate in Hertz
-   fps: Frame rate

Also filtering work for comparisons = (equals), ^= (starts with), $=
(ends with), *= (contains) and following string meta fields:

-   ext: File extension
-   acodec: Name of the audio codec in use
-   vcodec: Name of the video codec in use
-   container: Name of the container format
-   protocol: The protocol that will be used for the actual download,
    lower-case (http, https, rtsp, rtmp, rtmpe, mms, f4m, ism,
    http_dash_segments, m3u8, or m3u8_native)
-   format_id: A short description of the format

Any string comparison may be prefixed with negation ! in order to
produce an opposite comparison, e.g. !*= (does not contain).

Note that none of the aforementioned meta fields are guaranteed to be
present since this solely depends on the metadata obtained by particular
extractor, i.e. the metadata offered by the video hoster.

Formats for which the value is not known are excluded unless you put a
question mark (?) after the operator. You can combine format filters, so
-f "[height <=? 720][tbr>500]" selects up to 720p videos (or videos
where the height is not known) with a bitrate of at least 500 KBit/s.

You can merge the video and audio of two formats into a single file
using -f <video-format>+<audio-format> (requires ffmpeg or avconv
installed), for example -f bestvideo+bestaudio will download the best
video-only format, the best audio-only format and mux them together with
ffmpeg/avconv.

Format selectors can also be grouped using parentheses, for example if
you want to download the best mp4 and webm formats with a height lower
than 480 you can use -f '(mp4,webm)[height<480]'.

Since the end of April 2015 and version 2015.04.26, picta-dl uses
-f bestvideo+bestaudio/best as the default format selection (see #5447,
#5456). If ffmpeg or avconv are installed this results in downloading
bestvideo and bestaudio separately and muxing them together into a
single file giving the best overall quality available. Otherwise it
falls back to best and results in downloading the best available quality
served as a single file. best is also needed for videos that don't come
from YouTube because they don't provide the audio and video in two
different files. If you want to only download some DASH formats (for
example if you are not interested in getting videos with a resolution
higher than 1080p), you can add
-f bestvideo[height<=?1080]+bestaudio/best to your configuration file.
Note that if you use picta-dl to stream to stdout (and most likely to
pipe it to your media player then), i.e. you explicitly specify output
template as -o -, picta-dl still uses -f best format selection in order
to start content delivery immediately to your player and not to wait
until bestvideo and bestaudio are downloaded and muxed.

If you want to preserve the old format selection behavior (prior to
youtube-dl 2015.04.26), i.e. you want to download the best available
quality media served as a single file, you should explicitly specify
your choice with -f best. You may want to add it to the configuration
file in order not to type it every time you run picta-dl.

Format selection examples

Note that on Windows you may need to use double quotes instead of
single.

    # Download best mp4 format available or any other best if no mp4 available
    $ picta-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'

    # Download best format available but no better than 480p
    $ picta-dl -f 'bestvideo[height<=480]+bestaudio/best[height<=480]'

    # Download best video only format but no bigger than 50 MB
    $ picta-dl -f 'best[filesize<50M]'

    # Download best format available via direct link over HTTP/HTTPS protocol
    $ picta-dl -f '(bestvideo+bestaudio/best)[protocol^=http]'

    # Download the best video format and the best audio format without merging them
    $ picta-dl -f 'bestvideo,bestaudio' -o '%(title)s.f%(format_id)s.%(ext)s'

Note that in the last example, an output template is recommended as
bestvideo and bestaudio may have the same file name.



VIDEO SELECTION


Videos can be filtered by their upload date using the options --date,
--datebefore or --dateafter. They accept dates in two formats:

-   Absolute dates: Dates in the format YYYYMMDD.
-   Relative dates: Dates in the format
    (now|today)[+-][0-9](day|week|month|year)(s)?

Examples:

    # Download only the videos uploaded in the last 6 months
    $ picta-dl --dateafter now-6months

    # Download only the videos uploaded on January 1, 1970
    $ picta-dl --date 19700101

    $ # Download only the videos uploaded in the 200x decade
    $ picta-dl --dateafter 20000101 --datebefore 20091231



FAQ


How do I update picta-dl?

If you've followed our manual installation instructions, you can simply
run picta-dl -U (or, on Linux, sudo picta-dl -U).

If you have used pip, a simple sudo pip install -U picta-dl is
sufficient to update.

If you have installed picta-dl using a package manager like _apt-get_ or
_yum_, use the standard system update mechanism to update. Note that
distribution packages are often outdated. As a rule of thumb, picta-dl
releases at least once a month, and often weekly or even daily. Simply
go to https://yt-dl.org to find out the current version. Unfortunately,
there is nothing we picta-dl developers can do if your distribution
serves a really outdated version. You can (and should) complain to your
distribution in their bugtracker or support forum.

As a last resort, you can also uninstall the version installed by your
package manager and follow our manual installation instructions. For
that, remove the distribution's package, with a line like

    sudo apt-get remove -y picta-dl

Afterwards, simply follow our manual installation instructions:

    sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
    sudo chmod a+rx /usr/local/bin/youtube-dl
    hash -r

Again, from then on you'll be able to update with sudo picta-dl -U.

picta-dl is extremely slow to start on Windows

Add a file exclusion for picta-dl.exe in Windows Defender settings.

I'm getting an error Unable to extract OpenGraph title on YouTube playlists

YouTube changed their playlist format in March 2014 and later on, so
you'll need at least picta-dl 2014.07.25 to download all YouTube videos.

If you have installed picta-dl with a package manager, pip, setup.py or
a tarball, please use that to update. Note that Ubuntu packages do not
seem to get updated anymore. Since we are not affiliated with Ubuntu,
there is little we can do. Feel free to report bugs to the Ubuntu
packaging people - all they have to do is update the package to a
somewhat recent version. See above for a way to update.

I'm getting an error when trying to use output template: error: using output template conflicts with using title, video ID or auto number

Make sure you are not using -o with any of these options -t, --title,
--id, -A or --auto-number set in command line or in a configuration
file. Remove the latter if any.

Do I always have to pass -citw?

By default, picta-dl intends to have the best options (incidentally, if
you have a convincing case that these should be different, please file
an issue where you explain that). Therefore, it is unnecessary and
sometimes harmful to copy long option strings from webpages. In
particular, the only option out of -citw that is regularly useful is -i.

Can you please put the -b option back?

Most people asking this question are not aware that picta-dl now
defaults to downloading the highest available quality as reported by
YouTube, which will be 1080p or 720p in some cases, so you no longer
need the -b option. For some specific videos, maybe YouTube does not
report them to be available in a specific high quality format you're
interested in. In that case, simply request it with the -f option and
picta-dl will try to download it.

I get HTTP error 402 when trying to download a video. What's this?

Apparently YouTube requires you to pass a CAPTCHA test if you download
too much. We're considering to provide a way to let you solve the
CAPTCHA, but at the moment, your best course of action is pointing a web
browser to the youtube URL, solving the CAPTCHA, and restart picta-dl.

Do I need any other programs?

picta-dl works fine on its own on most sites. However, if you want to
convert video/audio, you'll need avconv or ffmpeg. On some sites - most
notably YouTube - videos can be retrieved in a higher quality format
without sound. picta-dl will detect whether avconv/ffmpeg is present and
automatically pick the best option.

Videos or video formats streamed via RTMP protocol can only be
downloaded when rtmpdump is installed. Downloading MMS and RTSP videos
requires either mplayer or mpv to be installed.

I have downloaded a video but how can I play it?

Once the video is fully downloaded, use any video player, such as mpv,
vlc or mplayer.

I extracted a video URL with -g, but it does not play on another machine / in my web browser.

It depends a lot on the service. In many cases, requests for the video
(to download/play it) must come from the same IP address and with the
same cookies and/or HTTP headers. Use the --cookies option to write the
required cookies into a file, and advise your downloader to read cookies
from that file. Some sites also require a common user agent to be used,
use --dump-user-agent to see the one in use by picta-dl. You can also
get necessary cookies and HTTP headers from JSON output obtained with
--dump-json.

It may be beneficial to use IPv6; in some cases, the restrictions are
only applied to IPv4. Some services (sometimes only for a subset of
videos) do not restrict the video URL by IP address, cookie, or
user-agent, but these are the exception rather than the rule.

Please bear in mind that some URL protocols are NOT supported by
browsers out of the box, including RTMP. If you are using -g, your own
downloader must support these as well.

If you want to play the video on a machine that is not running picta-dl,
you can relay the video content from the machine that runs picta-dl. You
can use -o - to let picta-dl stream a video to stdout, or simply allow
the player to download the files written by picta-dl in turn.

ERROR: no fmt_url_map or conn information found in video info

YouTube has switched to a new video info format in July 2011 which is
not supported by old versions of picta-dl. See above for how to update
picta-dl.

ERROR: unable to download video

YouTube requires an additional signature since September 2012 which is
not supported by old versions of picta-dl. See above for how to update
picta-dl.

Video URL contains an ampersand and I'm getting some strange output [1] 2839 or 'v' is not recognized as an internal or external command

That's actually the output from your shell. Since ampersand is one of
the special shell characters it's interpreted by the shell preventing
you from passing the whole URL to picta-dl. To disable your shell from
interpreting the ampersands (or any other special characters) you have
to either put the whole URL in quotes or escape them with a backslash
(which approach will work depends on your shell).

For example if your URL is
https://www.youtube.com/watch?t=4&v=BaW_jenozKc you should end up with
following command:

picta-dl 'https://www.youtube.com/watch?t=4&v=BaW_jenozKc'

or

picta-dl https://www.youtube.com/watch?t=4\&v=BaW_jenozKc

For Windows you have to use the double quotes:

picta-dl "https://www.youtube.com/watch?t=4&v=BaW_jenozKc"

ExtractorError: Could not find JS function u'OF'

In February 2015, the new YouTube player contained a character sequence
in a string that was misinterpreted by old versions of picta-dl. See
above for how to update picta-dl.

HTTP Error 429: Too Many Requests or 402: Payment Required

These two error codes indicate that the service is blocking your IP
address because of overuse. Usually this is a soft block meaning that
you can gain access again after solving CAPTCHA. Just open a browser and
solve a CAPTCHA the service suggests you and after that pass cookies to
picta-dl. Note that if your machine has multiple external IPs then you
should also pass exactly the same IP you've used for solving CAPTCHA
with --source-address. Also you may need to pass a User-Agent HTTP
header of your browser with --user-agent.

If this is not the case (no CAPTCHA suggested to solve by the service)
then you can contact the service and ask them to unblock your IP
address, or - if you have acquired a whitelisted IP address already -
use the --proxy or --source-address options to select another IP
address.

SyntaxError: Non-ASCII character

The error

    File "picta-dl", line 2
    SyntaxError: Non-ASCII character '\x93' ...

means you're using an outdated version of Python. Please update to
Python 2.6 or 2.7.

What is this binary file? Where has the code gone?

Since June 2012 (#342) picta-dl is packed as an executable zipfile,
simply unzip it (might need renaming to picta-dl.zip first on some
systems) or clone the git repository, as laid out above. If you modify
the code, you can run it by executing the __main__.py file. To recompile
the executable, run make picta-dl.

The exe throws an error due to missing MSVCR100.dll

To run the exe you need to install first the Microsoft Visual C++ 2010
Redistributable Package (x86).

On Windows, how should I set up ffmpeg and picta-dl? Where should I put the exe files?

If you put picta-dl and ffmpeg in the same directory that you're running
the command from, it will work, but that's rather cumbersome.

To make a different directory work - either for ffmpeg, or for picta-dl,
or for both - simply create the directory (say, C:\bin, or
C:\Users\<User name>\bin), put all the executables directly in there,
and then set your PATH environment variable to include that directory.

From then on, after restarting your shell, you will be able to access
both picta-dl and ffmpeg (and picta-dl will be able to find ffmpeg) by
simply typing picta-dl or ffmpeg, no matter what directory you're in.

How do I put downloads into a specific folder?

Use the -o to specify an output template, for example
-o "/home/user/videos/%(title)s-%(id)s.%(ext)s". If you want this for
all of your downloads, put the option into your configuration file.

How do I download a video starting with a -?

Either prepend https://www.youtube.com/watch?v= or separate the ID from
the options with --:

    picta-dl -- -wNyEUrxzFU
    picta-dl "https://www.youtube.com/watch?v=-wNyEUrxzFU"

How do I pass cookies to picta-dl?

Use the --cookies option, for example
--cookies /path/to/cookies/file.txt.

In order to extract cookies from browser use any conforming browser
extension for exporting cookies. For example, cookies.txt (for Chrome)
or cookies.txt (for Firefox).

Note that the cookies file must be in Mozilla/Netscape format and the
first line of the cookies file must be either # HTTP Cookie File or
# Netscape HTTP Cookie File. Make sure you have correct newline format
in the cookies file and convert newlines if necessary to correspond with
your OS, namely CRLF (\r\n) for Windows and LF (\n) for Unix and
Unix-like systems (Linux, macOS, etc.). HTTP Error 400: Bad Request when
using --cookies is a good sign of invalid newline format.

Passing cookies to picta-dl is a good way to workaround login when a
particular extractor does not implement it explicitly. Another use case
is working around CAPTCHA some websites require you to solve in
particular cases in order to get access (e.g. YouTube, CloudFlare).

How do I stream directly to media player?

You will first need to tell picta-dl to stream media to stdout with
-o -, and also tell your media player to read from stdin (it must be
capable of this for streaming) and then pipe former to latter. For
example, streaming to vlc can be achieved with:

    picta-dl -o - "https://www.youtube.com/watch?v=BaW_jenozKcj" | vlc -

How do I download only new videos from a playlist?

Use download-archive feature. With this feature you should initially
download the complete playlist with
--download-archive /path/to/download/archive/file.txt that will record
identifiers of all the videos in a special file. Each subsequent run
with the same --download-archive will download only new videos and skip
all videos that have been downloaded before. Note that only successful
downloads are recorded in the file.

For example, at first,

    picta-dl --download-archive archive.txt "https://www.youtube.com/playlist?list=PLwiyx1dc3P2JR9N8gQaQN_BCvlSlap7re"

will download the complete PLwiyx1dc3P2JR9N8gQaQN_BCvlSlap7re playlist
and create a file archive.txt. Each subsequent run will only download
new videos if any:

    picta-dl --download-archive archive.txt "https://www.youtube.com/playlist?list=PLwiyx1dc3P2JR9N8gQaQN_BCvlSlap7re"

Should I add --hls-prefer-native into my config?

When picta-dl detects an HLS video, it can download it either with the
built-in downloader or ffmpeg. Since many HLS streams are slightly
invalid and ffmpeg/picta-dl each handle some invalid cases better than
the other, there is an option to switch the downloader if needed.

When picta-dl knows that one particular downloader works better for a
given website, that downloader will be picked. Otherwise, picta-dl will
pick the best downloader for general compatibility, which at the moment
happens to be ffmpeg. This choice may change in future versions of
picta-dl, with improvements of the built-in downloader and/or ffmpeg.

In particular, the generic extractor (used when your website is not in
the list of supported sites by youtube-dl cannot mandate one specific
downloader.

If you put either --hls-prefer-native or --hls-prefer-ffmpeg into your
configuration, a different subset of videos will fail to download
correctly. Instead, it is much better to file an issue or a pull request
which details why the native or the ffmpeg HLS downloader is a better
choice for your use case.

Can you add support for this anime video site, or site which shows current movies for free?

As a matter of policy (as well as legality), picta-dl does not include
support for services that specialize in infringing copyright. As a rule
of thumb, if you cannot easily find a video that the service is quite
obviously allowed to distribute (i.e. that has been uploaded by the
creator, the creator's distributor, or is published under a free
license), the service is probably unfit for inclusion to picta-dl.

A note on the service that they don't host the infringing content, but
just link to those who do, is evidence that the service should NOT be
included into picta-dl. The same goes for any DMCA note when the whole
front page of the service is filled with videos they are not allowed to
distribute. A "fair use" note is equally unconvincing if the service
shows copyright-protected videos in full without authorization.

Support requests for services that DO purchase the rights to distribute
their content are perfectly fine though. If in doubt, you can simply
include a source that mentions the legitimate purchase of content.

How can I speed up work on my issue?

(Also known as: Help, my important issue not being solved!) The picta-dl
core developer team is quite small. While we do our best to solve as
many issues as possible, sometimes that can take quite a while. To speed
up your issue, here's what you can do:

First of all, please do report the issue at our issue tracker. That
allows us to coordinate all efforts by users and developers, and serves
as a unified point. Unfortunately, the picta-dl project has grown too
large to use personal email as an effective communication channel.

Please read the bug reporting instructions below. A lot of bugs lack all
the necessary information. If you can, offer proxy, VPN, or shell access
to the picta-dl developers. If you are able to, test the issue from
multiple computers in multiple countries to exclude local censorship or
misconfiguration issues.

If nobody is interested in solving your issue, you are welcome to take
matters into your own hands and submit a pull request (or coerce/pay
somebody else to do so).

Feel free to bump the issue from time to time by writing a small comment
("Issue is still present in picta-dl version ...from France, but fixed
from Belgium"), but please not more than once a month. Please do not
declare your issue as important or urgent.

How can I detect whether a given URL is supported by picta-dl?

For one, have a look at the list of supported sites. Note that it can
sometimes happen that the site changes its URL scheme (say, from
https://example.com/video/1234567 to https://example.com/v/1234567 ) and
picta-dl reports an URL of a service in that list as unsupported. In
that case, simply report a bug.

It is _not_ possible to detect whether a URL is supported or not. That's
because picta-dl contains a generic extractor which matches ALL URLs.
You may be tempted to disable, exclude, or remove the generic extractor,
but the generic extractor not only allows users to extract videos from
lots of websites that embed a video from another service, but may also
be used to extract video from a service that it's hosting itself.
Therefore, we neither recommend nor support disabling, excluding, or
removing the generic extractor.

If you want to find out whether a given URL is supported, simply call
picta-dl with it. If you get no videos back, chances are the URL is
either not referring to a video or unsupported. You can find out which
by examining the output (if you run picta-dl on the console) or catching
an UnsupportedError exception if you run it from a Python program.



WHY DO I NEED TO GO THROUGH THAT MUCH RED TAPE WHEN FILING BUGS?


Before we had the issue template, despite our extensive bug reporting
instructions, about 80% of the issue reports we got were useless, for
instance because people used ancient versions hundreds of releases old,
because of simple syntactic errors (not in picta-dl but in general shell
usage), because the problem was already reported multiple times before,
because people did not actually read an error message, even if it said
"please install ffmpeg", because people did not mention the URL they
were trying to download and many more simple, easy-to-avoid problems,
many of whom were totally unrelated to picta-dl.

picta-dl is an open-source project manned by too few volunteers, so we'd
rather spend time fixing bugs where we are certain none of those simple
problems apply, and where we can be reasonably confident to be able to
reproduce the issue without asking the reporter repeatedly. As such, the
output of picta-dl -v YOUR_URL_HERE is really all that's required to
file an issue. The issue template also guides you through some basic
steps you can do, such as checking that your version of picta-dl is
current.



DEVELOPER INSTRUCTIONS


Most users do not need to build picta-dl and can download the builds or
get them from their distribution.

To run picta-dl as a developer, you don't need to build anything either.
Simply execute

    python -m picta_dl

To run the test, simply invoke your favorite test runner, or execute a
test file directly; any of the following work:

    python -m unittest discover
    python test/test_download.py
    nosetests

See item 6 of new extractor tutorial for how to run extractor specific
test cases.

If you want to create a build of picta-dl yourself, you'll need

-   python
-   make (only GNU make is supported)
-   pandoc
-   zip
-   nosetests

Adding support for a new site

If you want to add support for a new site, first of all MAKE SURE this
site is NOT DEDICATED TO COPYRIGHT INFRINGEMENT. picta-dl does NOT
SUPPORT such sites thus pull requests adding support for them WILL BE
REJECTED.

After you have ensured this site is distributing its content legally,
you can follow this quick list (assuming your service is called
yourextractor):

1.  Fork this repository
2.  Check out the source code with:

         git clone git@github.com:YOUR_GITHUB_USERNAME/youtube-dl.git

3.  Start a new git branch with

         cd youtube-dl
         git checkout -b yourextractor

4.  Start with this simple template and save it to
    youtube_dl/extractor/yourextractor.py:

        # coding: utf-8
        from __future__ import unicode_literals

        from .common import InfoExtractor


        class YourExtractorIE(InfoExtractor):
            _VALID_URL = r'https?://(?:www\.)?yourextractor\.com/watch/(?P<id>[0-9]+)'
            _TEST = {
                'url': 'https://yourextractor.com/watch/42',
                'md5': 'TODO: md5 sum of the first 10241 bytes of the video file (use --test)',
                'info_dict': {
                    'id': '42',
                    'ext': 'mp4',
                    'title': 'Video title goes here',
                    'thumbnail': r're:^https?://.*\.jpg$',
                    # TODO more properties, either as:
                    # * A value
                    # * MD5 checksum; start the string with md5:
                    # * A regular expression; start the string with re:
                    # * Any Python type (for example int or float)
                }
            }

            def _real_extract(self, url):
                video_id = self._match_id(url)
                webpage = self._download_webpage(url, video_id)

                # TODO more code goes here, for example ...
                title = self._html_search_regex(r'<h1>(.+?)</h1>', webpage, 'title')

                return {
                    'id': video_id,
                    'title': title,
                    'description': self._og_search_description(webpage),
                    'uploader': self._search_regex(r'<div[^>]+id="uploader"[^>]*>([^<]+)<', webpage, 'uploader', fatal=False),
                    picta_dl
                }

5.  Add an import in youtube_dl/extractor/extractors.py.
6.  Run python test/test_download.py TestDownload.test_YourExtractor.
    This _should fail_ at first, but you can continually re-run it until
    you're done. If you decide to add more than one test, then rename
    _TEST to _TESTS and make it into a list of dictionaries. The tests
    will then be named TestDownload.test_YourExtractor,
    TestDownload.test_YourExtractor_1,
    TestDownload.test_YourExtractor_2, etc. Note that tests with
    only_matching key in test's dict are not counted in.
7.  Have a look at youtube_dl/extractor/common.py for possible helper
    methods and a detailed description of what your extractor should and
    may return. Add tests and code for as many as you want.
8.  Make sure your code follows youtube-dl coding conventions and check
    the code with flake8:

         $ flake8 youtube_dl/extractor/yourextractor.py

9.  Make sure your code works under all Python versions claimed
    supported by youtube-dl, namely 2.6, 2.7, and 3.2+.
10. When the tests pass, add the new files and commit them and push the
    result, like this:

        $ git add youtube_dl/extractor/extractors.py
        $ git add youtube_dl/extractor/yourextractor.py
        $ git commit -m '[yourextractor] Add new extractor'
        $ git push origin yourextractor

11. Finally, create a pull request. We'll then review and merge it.

In any case, thank you very much for your contributions!


picta-dl coding conventions

This section introduces a guide lines for writing idiomatic, robust and
future-proof extractor code.

Extractors are very fragile by nature since they depend on the layout of
the source data provided by 3rd party media hosters out of your control
and this layout tends to change. As an extractor implementer your task
is not only to write code that will extract media links and metadata
correctly but also to minimize dependency on the source's layout and
even to make the code foresee potential future changes and be ready for
that. This is important because it will allow the extractor not to break
on minor layout changes thus keeping old picta-dl versions working. Even
though this breakage issue is easily fixed by emitting a new version of
picta-dl with a fix incorporated, all the previous versions become
broken in all repositories and distros' packages that may not be so
prompt in fetching the update from us. Needless to say, some non rolling
release distros may never receive an update at all.

Mandatory and optional metafields

For extraction to work picta-dl relies on metadata your extractor
extracts and provides to picta-dl expressed by an information dictionary
or simply _info dict_. Only the following meta fields in the _info dict_
are considered mandatory for a successful extraction process by
picta-dl:

-   id (media identifier)
-   title (media title)
-   url (media download URL) or formats

In fact only the last option is technically mandatory (i.e. if you can't
figure out the download location of the media the extraction does not
make any sense). But by convention picta-dl also treats id and title as
mandatory. Thus the aforementioned metafields are the critical data that
the extraction does not make any sense without and if any of them fail
to be extracted then the extractor is considered completely broken.

Any field apart from the aforementioned ones are considered OPTIONAL.
That means that extraction should be TOLERANT to situations when sources
for these fields can potentially be unavailable (even if they are always
available at the moment) and FUTURE-PROOF in order not to break the
extraction of general purpose mandatory fields.

Example

Say you have some source dictionary meta that you've fetched as JSON
with HTTP request and it has a key summary:

    meta = self._download_json(url, video_id)

Assume at this point meta's layout is:

    {
        ...
        "summary": "some fancy summary text",
        ...
    }

Assume you want to extract summary and put it into the resulting info
dict as description. Since description is an optional meta field you
should be ready that this key may be missing from the meta dict, so that
you should extract it like:

    description = meta.get('summary')  # correct

and not like:

    description = meta['summary']  # incorrect

The latter will break extraction process with KeyError if summary
disappears from meta at some later time but with the former approach
extraction will just go ahead with description set to None which is
perfectly fine (remember None is equivalent to the absence of data).

Similarly, you should pass fatal=False when extracting optional data
from a webpage with _search_regex, _html_search_regex or similar
methods, for instance:

    description = self._search_regex(
        r'<span[^>]+id="title"[^>]*>([^<]+)<',
        webpage, 'description', fatal=False)

With fatal set to False if _search_regex fails to extract description it
will emit a warning and continue extraction.

You can also pass default=<some fallback value>, for example:

    description = self._search_regex(
        r'<span[^>]+id="title"[^>]*>([^<]+)<',
        webpage, 'description', default=None)

On failure this code will silently continue the extraction with
description set to None. That is useful for metafields that may or may
not be present.

Provide fallbacks

When extracting metadata try to do so from multiple sources. For example
if title is present in several places, try extracting from at least some
of them. This makes it more future-proof in case some of the sources
become unavailable.

Example

Say meta from the previous example has a title and you are about to
extract it. Since title is a mandatory meta field you should end up with
something like:

    title = meta['title']

If title disappears from meta in future due to some changes on the
hoster's side the extraction would fail since title is mandatory. That's
expected.

Assume that you have some another source you can extract title from, for
example og:title HTML meta of a webpage. In this case you can provide a
fallback scenario:

    title = meta.get('title') or self._og_search_title(webpage)

This code will try to extract from meta first and if it fails it will
try extracting og:title from a webpage.

Regular expressions

Don't capture groups you don't use

Capturing group must be an indication that it's used somewhere in the
code. Any group that is not used must be non capturing.

Example

Don't capture id attribute name here since you can't use it for anything
anyway.

Correct:

    r'(?:id|ID)=(?P<id>\d+)'

Incorrect:

    r'(id|ID)=(?P<id>\d+)'

Make regular expressions relaxed and flexible

When using regular expressions try to write them fuzzy, relaxed and
flexible, skipping insignificant parts that are more likely to change,
allowing both single and double quotes for quoted values and so on.

Example

Say you need to extract title from the following HTML code:

    <span style="position: absolute; left: 910px; width: 90px; float: right; z-index: 9999;" class="title">some fancy title</span>

The code for that task should look similar to:

    title = self._search_regex(
        r'<span[^>]+class="title"[^>]*>([^<]+)', webpage, 'title')

Or even better:

    title = self._search_regex(
        r'<span[^>]+class=(["\'])title\1[^>]*>(?P<title>[^<]+)',
        webpage, 'title', group='title')

Note how you tolerate potential changes in the style attribute's value
or switch from using double quotes to single for class attribute:

The code definitely should not look like:

    title = self._search_regex(
        r'<span style="position: absolute; left: 910px; width: 90px; float: right; z-index: 9999;" class="title">(.*?)</span>',
        webpage, 'title', group='title')

Long lines policy

There is a soft limit to keep lines of code under 80 characters long.
This means it should be respected if possible and if it does not make
readability and code maintenance worse.

For example, you should NEVER split long string literals like URLs or
some other often copied entities over multiple lines to fit this limit:

Correct:

    'https://www.youtube.com/watch?v=FqZTN594JQw&list=PLMYEtVRpaqY00V9W81Cwmzp6N6vZqfUKD4'

Incorrect:

    'https://www.youtube.com/watch?v=FqZTN594JQw&list='
    'PLMYEtVRpaqY00V9W81Cwmzp6N6vZqfUKD4'

Inline values

Extracting variables is acceptable for reducing code duplication and
improving readability of complex expressions. However, you should avoid
extracting variables used only once and moving them to opposite parts of
the extractor file, which makes reading the linear flow difficult.

Example

Correct:

    title = self._html_search_regex(r'<title>([^<]+)</title>', webpage, 'title')

Incorrect:

    TITLE_RE = r'<title>([^<]+)</title>'
    # ...some lines of code...
    title = self._html_search_regex(TITLE_RE, webpage, 'title')

Collapse fallbacks

Multiple fallback values can quickly become unwieldy. Collapse multiple
fallback values into a single expression via a list of patterns.

Example

Good:

    description = self._html_search_meta(
        ['og:description', 'description', 'twitter:description'],
        webpage, 'description', default=None)

Unwieldy:

    description = (
        self._og_search_description(webpage, default=None)
        or self._html_search_meta('description', webpage, default=None)
        or self._html_search_meta('twitter:description', webpage, default=None))

Methods supporting list of patterns are: _search_regex,
_html_search_regex, _og_search_property, _html_search_meta.

Trailing parentheses

Always move trailing parentheses after the last argument.

Example

Correct:

        lambda x: x['ResultSet']['Result'][0]['VideoUrlSet']['VideoUrl'],
        list)

Incorrect:

        lambda x: x['ResultSet']['Result'][0]['VideoUrlSet']['VideoUrl'],
        list,
    )

Use convenience conversion and parsing functions

Wrap all extracted numeric data into safe functions from
picta_dl/utils.py: int_or_none, float_or_none. Use them for string to
number conversions as well.

Use url_or_none for safe URL processing.

Use try_get for safe metadata extraction from parsed JSON.

Use unified_strdate for uniform upload_date or any YYYYMMDD meta field
extraction, unified_timestamp for uniform timestamp extraction,
parse_filesize for filesize extraction, parse_count for count meta
fields extraction, parse_resolution, parse_duration for duration
extraction, parse_age_limit for age_limit extraction.

Explore picta_dl/utils.py for more useful convenience functions.

More examples

Safely extract optional description from parsed JSON

    description = try_get(response, lambda x: x['result']['video'][0]['summary'], compat_str)

Safely extract more optional metadata

    video = try_get(response, lambda x: x['result']['video'][0], dict) or {}
    description = video.get('summary')
    duration = float_or_none(video.get('durationMs'), scale=1000)
    view_count = int_or_none(video.get('views'))



EMBEDDING YOUTUBE-DL


picta-dl makes the best effort to be a good command-line program, and
thus should be callable from any programming language. If you encounter
any problems parsing its output, feel free to create a report.

From a Python program, you can embed picta-dl in a more powerful
fashion, like this:

    from __future__ import unicode_literals
    import picta_dl

    ydl_opts = {}
    with picta_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])

Most likely, you'll want to use various options. For a list of options
available, have a look at picta_dl/YoutubeDL.py. For a start, if you
want to intercept picta-dl's output, set a logger object.

Here's a more complete example of a program that outputs only errors
(and a short message after the download is finished), and
downloads/converts the video to an mp3 file:

    from __future__ import unicode_literals
    import picta_dl


    class MyLogger(object):
        def debug(self, msg):
            pass

        def warning(self, msg):
            pass

        def error(self, msg):
            print(msg)


    def my_hook(d):
        if d['status'] == 'finished':
            print('Done downloading, now converting ...')


    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
    }
    with picta_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])



BUGS


Bugs and suggestions should be reported at:
https://github.com/oleksis/picta-dl/issues. Unless you were prompted to
or there is another pertinent reason (e.g. GitHub fails to accept the
bug report), please do not send bug reports via personal email. For
discussions, join us in the IRC channel #youtube-dl on freenode
(webchat).

PLEASE INCLUDE THE FULL OUTPUT OF PICTA-DL WHEN RUN WITH -v, i.e. ADD -v
flag to YOUR COMMAND LINE, copy the WHOLE output and post it in the
issue body wrapped in ``` for better formatting. It should look similar
to this:

    $ picta-dl -v <your command line>
    [debug] System config: []
    [debug] User config: []
    [debug] Command-line args: [u'-v', u'https://www.youtube.com/watch?v=BaW_jenozKcj']
    [debug] Encodings: locale cp1251, fs mbcs, out cp866, pref cp1251
    [debug] picta-dl version 2015.12.06
    [debug] Git HEAD: 135392e
    [debug] Python version 2.6.6 - Windows-2003Server-5.2.3790-SP2
    [debug] exe versions: ffmpeg N-75573-g1d0487f, ffprobe N-75573-g1d0487f, rtmpdump 2.4
    [debug] Proxy map: {}
    ...

DO NOT POST SCREENSHOTS OF VERBOSE LOGS; ONLY PLAIN TEXT IS ACCEPTABLE.

The output (including the first lines) contains important debugging
information. Issues without the full output are often not reproducible
and therefore do not get solved in short order, if ever.

Please re-read your issue once again to avoid a couple of common
mistakes (you can and should use this as a checklist):

Is the description of the issue itself sufficient?

We often get issue reports that we cannot really decipher. While in most
cases we eventually get the required information after asking back
multiple times, this poses an unnecessary drain on our resources. Many
contributors, including myself, are also not native speakers, so we may
misread some parts.

So please elaborate on what feature you are requesting, or what bug you
want to be fixed. Make sure that it's obvious

-   What the problem is
-   How it could be fixed
-   How your proposed solution would look like

If your report is shorter than two lines, it is almost certainly missing
some of these, which makes it hard for us to respond to it. We're often
too polite to close the issue outright, but the missing info makes
misinterpretation likely. As a committer myself, I often get frustrated
by these issues, since the only possible way for me to move forward on
them is to ask for clarification over and over.

For bug reports, this means that your report should contain the
_complete_ output of picta-dl when called with the -v flag. The error
message you get for (most) bugs even says so, but you would not believe
how many of our bug reports do not contain this information.

If your server has multiple IPs or you suspect censorship, adding
--call-home may be a good idea to get more diagnostics. If the error is
ERROR: Unable to extract ... and you cannot reproduce it from multiple
countries, add --dump-pages (warning: this will yield a rather large
output, redirect it to the file log.txt by adding >log.txt 2>&1 to your
command-line) or upload the .dump files you get when you add
--write-pages somewhere.

SITE SUPPORT REQUESTS MUST CONTAIN AN EXAMPLE URL. An example URL is a
URL you might want to download, like
https://www.youtube.com/watch?v=BaW_jenozKc. There should be an obvious
video present. Except under very special circumstances, the main page of
a video service (e.g. https://www.youtube.com/) is _not_ an example URL.

Are you using the latest version?

Before reporting any issue, type picta-dl -U. This should report that
you're up-to-date. About 20% of the reports we receive are already
fixed, but people are using outdated versions. This goes for feature
requests as well.

Is the issue already documented?

Make sure that someone has not already opened the issue you're trying to
open. Search at the top of the window or browse the GitHub Issues of
this repository. If there is an issue, feel free to write something
along the lines of "This affects me as well, with version 2015.01.01.
Here is some more information on the issue: ...". While some issues may
be old, a new post into them often spurs rapid activity.

Why are existing options not enough?

Before requesting a new feature, please have a quick peek at the list of
supported options. Many feature requests are for features that actually
exist already! Please, absolutely do show off your work in the issue
report and detail how the existing similar options do _not_ solve your
problem.

Is there enough context in your bug report?

People want to solve problems, and often think they do us a favor by
breaking down their larger problems (e.g. wanting to skip already
downloaded files) to a specific request (e.g. requesting us to look
whether the file exists before downloading the info page). However, what
often happens is that they break down the problem into two steps: One
simple, and one impossible (or extremely complicated one).

We are then presented with a very complicated request when the original
problem could be solved far easier, e.g. by recording the downloaded
video IDs in a separate file. To avoid this, you must include the
greater context where it is non-obvious. In particular, every feature
request that does not consist of adding support for a new site should
contain a use case scenario that explains in what situation the missing
feature would be useful.

Does the issue involve one problem, and one problem only?

Some of our users seem to think there is a limit of issues they can or
should open. There is no limit of issues they can or should open. While
it may seem appealing to be able to dump all your issues into one
ticket, that means that someone who solves one of your issues cannot
mark the issue as closed. Typically, reporting a bunch of issues leads
to the ticket lingering since nobody wants to attack that behemoth,
until someone mercifully splits the issue into multiple ones.

In particular, every site support request issue should only pertain to
services at one site (generally under a common domain, but always using
the same backend technology). Do not request support for vimeo user
videos, White house podcasts, and Google Plus pages in the same issue.
Also, make sure that you don't post bug reports alongside feature
requests. As a rule of thumb, a feature request does not include outputs
of picta-dl that are not immediately related to the feature at hand. Do
not post reports of a network error alongside the request for a new
video service.

Is anyone going to need the feature?

Only post features that you (or an incapacitated friend you can
personally talk to) require. Do not post features because they seem like
a good idea. If they are really useful, they will be requested by
someone who requires them.

Is your question about picta-dl?

It may sound strange, but some bug reports we receive are completely
unrelated to picta-dl and relate to a different, or even the reporter's
own, application. Please make sure that you are actually using picta-dl.
If you are using a UI for picta-dl, report the bug to the maintainer of
the actual application providing the UI. On the other hand, if your UI
for picta-dl fails in some way you believe is related to picta-dl, by
all means, go ahead and report the bug.



COPYRIGHT


picta-dl is released into the public domain by the copyright holders.

This README file was originally written by Daniel Bolton and is likewise
released into the public domain.
