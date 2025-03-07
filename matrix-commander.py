#!/usr/bin/env python3

r"""matrix-commander.py.

0123456789012345678901234567890123456789012345678901234567890123456789012345678
0000000000111111111122222222223333333333444444444455555555556666666666777777777

[![Built with matrix-nio](
https://img.shields.io/badge/built%20with-matrix--nio-brightgreen)](
https://github.com/poljar/matrix-nio)

![logo](logos/matrix-commander-logo.svg)

# matrix-commander

Simple but convenient CLI-based Matrix client app for sending, receiving,
creating rooms, inviting, verifying, and so much more.

- `matrix-commander` is a simple command-line [Matrix](https://matrix.org/)
  client.
- It is a simple but convenient app to
    - send Matrix text messages as well as text, image, audio, video or
      other arbitrary files
    - listen to and receive Matrix messages
    - perform Matrix emoji verification
    - create rooms
    - invite to rooms
- It exclusively offers a command-line interface (CLI).
- Hence the word-play: matrix-command(lin)er
- There is no GUI and there are no windows (except for pop-up windows in
  OS notification)
- It uses the [matrix-nio](https://github.com/poljar/matrix-nio/) SDK
- Both `matrix-nio` and `matrix-commander` are written in Python 3

# Summary

This program is a simple but convenient app to send and receive Matrix
messages from the CLI in various different ways.

Use cases for this program could be
- a bot or part of a bot,
- to send alerts,
- combine it with cron to publish periodic data,
- send yourself daily/weekly reminders via a cron job
- send yourself a daily song from your music collection
- a trivial way to fire off some instant messages from the command line
- to automate sending via programs and scripts
- a "blogger" who frequently sends messages and images to the same
  room(s) could use it
- a person could write a diary or run a gratitutde journal by
  sending messages to her/his own room
- as educational material that showcases the use of the `matrix-nio` SDK

# Give it a Star
If you like it, use it, fork it, make a Pull Request or contribute.
Please give it a :star: on Github right now so others find it more easily.
:heart:

# First Run, Set Up, Credentials File, End-to-end Encryption

This program on the first run creates a credentials.json file.
The credentials.json file stores: homeserver, user id,
access token, device id, and room id. On the first run
it asks some questions, creates the token and device id
and stores everything in the credentials.json file.

Since the credentials file holds an access token it
should be protected and secured. One can use different
credential files for different users or different rooms.

On creation the credentials file will always be created in the local
directory, so the users sees it right away. This is fine if you have
only one or a few credential files, but for better maintainability
it is suggested to place your credentials files into directory
$HOME/.config/matrix-commander/. When the program looks for
a credentials file it will first look in local directory and then
as secondary choice it will look in directory
$HOME/.config/matrix-commander/.

If you want to re-use an existing device id and an existing
access token, you can do so as well, just manually edit the
credentials file. However, for end-to-end encryption this will
NOT work.

End-to-end encryption (e2ee) is enabled by default. It cannot be turned off.
Wherever possible end-to-end encryption will be used. For e2ee to work
efficiently a `store` directory is needed to store e2ee data persistently.
The default location for the store directory is a local directory named
`store`. Alternatively, as a secondary choice the program looks for a store
directory in $HOME/.local/shared/matrix-commander/store/. The user can always
specify a different location via the --store argument. If needed the `store`
directory will be created on the first run.

From the second time the program is run, and on all
future runs it will use the homeserver, user id
and access token found in the credentials file to log
into the Matrix account. Now this program can be used
to easily send simple text messages, images, and so forth
to the preconfigured room.

# Sending

Messages to send can be provided
1) in the command line (-m or --message)
2) as input from the keyboard
3) through a pipe from stdin (|), i.e. piped in from another program.

For sending messages the program supports various text formats:
1) text: default
2) html:  HTML formated text
3) markdown: MarkDown formatted text
4) code: used a block of fixed-sized font, ideal for ASCII art or
   tables, bash outputs, etc.
5) notification
6) split: splits messages into multiple units at given pattern

Photos and images that can be sent. That includes files like
.jpg, .gif, .png or .svg.

Arbirtary files like .txt, .pdf, .doc, audio files like .mp3
or video files like .mp4 can also be sent.

# Listening, Receiving

One can listen to one or multiple rooms. Received messages will be displayed
on the screen. If desired, optionally, you can be notified of incoming
messages through the operating system standard notification system, usually a
small pop-up window.

Messages can be received or listened to various ways:
1) Forever: the program runs forever, listens forever, and prints all
   messages as they arrive in real-time.
2) Once: the program prints all the messages that are waiting in the queue,
   i.e. all messages that have been sent in, and after printing them the
   program terminates.
3) Tail: prints the last N read or unread messages of one or multiple
   specified rooms and after printing them the program terminates.

When listening to messages you can also choose to download and decrypt
media. Say, someone is sending a song. The mp3 file can be downloaded
and automatically decrypted for you.

# Verification

The program can accept verification request and verify other devices
via emojis. Do do so use the --verify option and the program will
await incoming verification request and act accordingly.

# Room Operations, Actions on Rooms

The program can create rooms, join, leave and forget rooms.
It can also send invitations to join rooms to
others (given that user has the appropriate permissions) as
well as ban, unban and kick other users from rooms.

# Summary, TLDR

This simple Matrix client written in Python allows you to send and
receive messages and verify other devices. End-to-end encryption is enabled
by default and cannot be turned off.

# Dependencies

- Python 3.8 or higher (3.7 will NOT work) installed
- libolm-dev must be installed as it is required by matrix-nio
  - libolm-dev on Debian/Ubuntu, libolm-devel on Fedora, libolm on MacOS
- matrix-nio must be installed, see https://github.com/poljar/matrix-nio
  - pip3 install --user --upgrade matrix-nio[e2e]
- python3 package markdown must be installed to support MarkDown format
  - pip3 install --user --upgrade markdown
- python3 package python_magic must be installed to support image sending
  - pip3 install --user --upgrade python_magic
- if (and only if) you want OS notification support, then the python3
  package notify2 and dbus-python should be installed
  - pip3 install --user --upgrade dbus-python # optional
  - pip3 install --user --upgrade notify2 # optional
- python3 package urllib must be installed to support media download
  - pip3 install --user --upgrade urllib
- the matrix-commander.py file must be installed, and should have
  execution permissions
  - chmod 755 matrix-commander.py
- for a full list or requirements look at the `requirements.txt` file
  - run `pip install -r requirements.txt` to automatically install
    all required Python packages
  - if you e.g. run on a headless server and don't want dbus-python and
    notify2, please remove the corresponding 2 lines from
    the `requirements.txt` file

# Examples of calling `matrix-commander`

```
$ matrix-commander.py #  first run; this will configure everything
$ # this created a credentials.json file, and a store directory
$ # optionally, if you want you can move credentials to app config directory
$ mkdir $HOME/.config/matrix-commander # optional
$ mv -i credentials.json $HOME/.config/matrix-commander/
$ # optionally, if you want you can move store to the app share directory
$ mkdir $HOME/.local/share/matrix-commander # optional
$ mv -i store $HOME/.local/share/matrix-commander/
$ # Now you are ready to run program for a second time
$ # Let us verify the device/room to where we want to send messages
$ # The other device will issue a "verify by emoji" request
$ matrix-commander.py --verify
$ # Now program is both configured and verified, let us send the first message
$ matrix-commander.py -m "First message!"
$ matrix-commander.py --debug # turn debugging on
$ matrix-commander.py --help # print help
$ matrix-commander.py # this will ask user for message to send
$ matrix-commander.py --message "Hello World!" # sends provided message
$ echo "Hello World" | matrix-commander.py # pipe input msg into program
$ matrix-commander.py -m msg1 -m msg2 # sends 2 messages
$ matrix-commander.py -m msg1 msg2 msg3 # sends 3 messages
$ df -h | matrix-commander.py --code # formatting for code/tables
$ matrix-commander.py -m "<b>BOLD</b> and <i>ITALIC</i>" --html
$ matrix-commander.py -m "- bullet1" --markdown
$ # take input from an RSS feed and split large RSS entries into multiple
$ # Matrix messages wherever the pattern "\n\n\n" is found
$ rssfeed | matrix-commander.py --split "\n\n\n"
$ matrix-commander.py --credentials usr1room2.json # select credentials file
$ matrix-commander.py --store /var/storage/ # select store directory
$ # Send to a specific room
$ matrix-commander.py -m "hi" --room '!YourRoomId:example.org'
$ # some shells require the ! of the room id to be escaped with \
$ matrix-commander.py -m "hi" --room "\!YourRoomId:example.org"
$ # Send to multiple rooms
$ matrix-commander.py -m "hi" -r '!r1:example.org' '!r2:example.org'
$ # Send to multiple rooms, another way
$ matrix-commander.py -m "hi" -r '!r1:example.org' -r '!r2:example.org'
$ # send 2 images and 1 text
$ matrix-commander.py -i photo1.jpg photo2.img -m "Do you like my 2 photos?"
$ # send 1 image and no text
$ matrix-commander.py -i photo1.jpg -m ""
$ # send 1 audio and 1 text to 2 rooms
$ matrix-commander.py -a song.mp3 -m "Do you like this song?" \
    -r '!someroom1:example.com' '!someroom2:example.com'
$ # send a .pdf file and a video with a text
$ matrix-commander.py -f example.pdf video.mp4 -m "Here are the promised files"
$ # listen forever, get msgs in real-time and notify me via OS
$ matrix-commander.py --listen forever --os-notify
$ # listen forever, and show me also my own messages
$ matrix-commander.py --listen forever --listen-self
$ # listen once, get any new messages and quit
$ matrix-commander.py --listen once --listen-self
$ matrix-commander.py --listen once --listen-self | process-in-other-app
$ # listen to tail, get the last N messages and quit
$ matrix-commander.py --listen tail --tail 10 --listen-self
$ # listen to tail, another way of specifying it
$ matrix-commander.py --tail 10 --listen-self | process-in-other-app
$ # get the very last message
$ matrix-commander.py --tail 1 --listen-self
$ # listen to (get) all messages, old and new, and process them in another app
$ matrix-commander.py --listen all | process-in-other-app
$ # listen to (get) all messages, including own
$ matrix-commander.py --listen all --listen-self
$ # rename device-name, sometimes also called display-name
$ matrix-commander.py --rename-device "my new name"
$ # download and decrypt media files like images, audio, PDF, etc.
$ # and store downloaded files in directory "mymedia"
$ matrix-commander.py --listen forever --listen-self --download-media mymedia
$ # create rooms without name and topic, just with alias, use a simple alias
$ matrix-commander.py --room-create roomAlias1
$ # don't use a well formed alias like '#roomAlias1:example.com' as it will
$ # confuse the server!
$ # BAD: matrix-commander.py --room-create roomAlias1 '#roomAlias1:example.com'
$ matrix-commander.py --room-create roomAlias2
$ # create rooms with name and topic
$ matrix-commander.py --room-create roomAlias3 --name 'Fancy Room' \
    --topic 'All about Matrix'
$ matrix-commander.py --room-create roomAlias4 roomAlias5 \
    --name 'Fancy Room 4' -name 'Cute Room 5' \
    --topic 'All about Matrix 4' 'All about Nio 5'
$ # join rooms
$ matrix-commander.py --room-join '!someroomId1:example.com' \
    '!someroomId2:example.com' '#roomAlias1:example.com'
$ # leave rooms
$ matrix-commander.py --room-leave '#roomAlias1:example.com' \
    '!someroomId2:example.com'
$ # forget rooms, you have to first leave a room before you forget it
$ matrix-commander.py --room-forget '#roomAlias1:example.com'
$ # invite users to rooms
$ matrix-commander.py --room-invite '#roomAlias1:example.com' \
    --user '@user1:example.com' '@user2:example.com'
$ # ban users from rooms
$ matrix-commander.py --room-ban '!someroom1:example.com' \
    '!someroom2:example.com' \
    --user '@user1:example.com' '@user2:example.com'
$ # unban users from rooms, remember after unbanning you have to invite again
$ matrix-commander.py --room-unban '!someroom1:example.com' \
    '!someroom2:example.com' \
    --user '@user1:example.com' '@user2:example.com'
$ # kick users from rooms
$ matrix-commander.py --room-kick '!someroom1:example.com' \
    '#roomAlias2:example.com' \
    --user '@user1:example.com' '@user2:example.com'
$ # set log levels, INFO for matrix-commander and ERROR for modules below
$ matrix-commander.py -m "test" --log-level INFO ERROR
```

# Usage
```
usage: matrix-commander.py [-h] [-d] [--log-level LOG_LEVEL [LOG_LEVEL ...]]
                           [-c CREDENTIALS] [-r ROOM [ROOM ...]]
                           [--room-create ROOM_CREATE [ROOM_CREATE ...]]
                           [--room-join ROOM_JOIN [ROOM_JOIN ...]]
                           [--room-leave ROOM_LEAVE [ROOM_LEAVE ...]]
                           [--room-forget ROOM_FORGET [ROOM_FORGET ...]]
                           [--room-invite ROOM_INVITE [ROOM_INVITE ...]]
                           [--room-ban ROOM_BAN [ROOM_BAN ...]]
                           [--room-unban ROOM_UNBAN [ROOM_UNBAN ...]]
                           [--room-kick ROOM_KICK [ROOM_KICK ...]]
                           [--user USER [USER ...]] [--name NAME [NAME ...]]
                           [--topic TOPIC [TOPIC ...]]
                           [-m MESSAGE [MESSAGE ...]] [-i IMAGE [IMAGE ...]]
                           [-a AUDIO [AUDIO ...]] [-f FILE [FILE ...]] [-w]
                           [-z] [-k] [-p SPLIT] [-j CONFIG] [--proxy PROXY]
                           [-n] [-e] [-s STORE] [-l [LISTEN]] [-t [TAIL]] [-y]
                           [--print-event-id] [-u [DOWNLOAD_MEDIA]] [-o]
                           [-v [VERIFY]] [-x RENAME_DEVICE] [--version]

Welcome to matrix-commander, a Matrix CLI client. ─── On first run this
program will configure itself. On further runs this program implements a
simple Matrix CLI client that can send messages, listen to messages, verify
devices, etc. It can send one or multiple message to one or multiple Matrix
rooms. The text messages can be of various formats such as "text", "html",
"markdown" or "code". Images, audio or arbitrary files can be sent as well.
For receiving there are three main options: listen forever, listen once and
quit, and get the last N messages and quit. Emoji verification is built-in
which can be used to verify devices. End-to-end encryption is enabled by
default and cannot be turned off. ─── See dependencies in source code or in
README.md on Github. For even more explications and examples also read the
documentation provided in the top portion of the source code and in the
GithubREADME.md file.

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Print debug information. If used once, only the log
                        level of matrix-commander is set to DEBUG. If used
                        twice ("-d -d" or "-dd") then log levels of both
                        matrix-commander and underlying modules are set to
                        DEBUG. "-d" is a shortcut for "--log-level DEBUG". See
                        also --log-level. "-d" takes precedence over "--log-
                        level".
  --log-level LOG_LEVEL [LOG_LEVEL ...]
                        Set the log level(s). Possible values are "DEBUG",
                        "INFO", "WARNING", "ERROR", and "CRITICAL". If
                        --log_level is used with one level argument, only the
                        log level of matrix-commander is set to the specified
                        value. If --log_level is used with two level argument
                        (e.g. "--log-level WARNING ERROR") then log levels of
                        both matrix-commander and underlying modules are set
                        to the specified values. See also --debug.
  -c CREDENTIALS, --credentials CREDENTIALS
                        On first run, information about homeserver, user, room
                        id, etc. will be written to a credentials file. By
                        default, this file is "credentials.json". On further
                        runs the credentials file is read to permit logging
                        into the correct Matrix account and sending messages
                        to the preconfigured room. If this option is provided,
                        the provided file name will be used as credentials
                        file instead of the default one.
  -r ROOM [ROOM ...], --room ROOM [ROOM ...]
                        Send to this room or these rooms. None, one or
                        multiple rooms can be specified. The default room is
                        provided in credentials file. If a room (or multiple
                        ones) is (or are) provided in the arguments, then it
                        (or they) will be used instead of the one from the
                        credentials file. The user must have access to the
                        specified room in order to send messages there.
                        Messages cannot be sent to arbitrary rooms. When
                        specifying the room id some shells require the
                        exclamation mark to be escaped with a backslash.
  --room-create ROOM_CREATE [ROOM_CREATE ...]
                        Create this room or these rooms. One or multiple room
                        aliases can be specified. The room (or multiple ones)
                        provided in the arguments will be created. The user
                        must be permitted to create rooms.Combine --room-
                        create with --name and --topic to add names and topics
                        to the room(s) to be created.
  --room-join ROOM_JOIN [ROOM_JOIN ...]
                        Join this room or these rooms. One or multiple room
                        aliases can be specified. The room (or multiple ones)
                        provided in the arguments will be joined. The user
                        must have permissions to join these rooms.
  --room-leave ROOM_LEAVE [ROOM_LEAVE ...]
                        Leave this room or these rooms. One or multiple room
                        aliases can be specified. The room (or multiple ones)
                        provided in the arguments will be left.
  --room-forget ROOM_FORGET [ROOM_FORGET ...]
                        After leaving a room you should (most likely) forget
                        the room. Forgetting a room removes the users' room
                        history. One or multiple room aliases can be
                        specified. The room (or multiple ones) provided in the
                        arguments will be forgotten. If all users forget a
                        room, the room can eventually be deleted on the
                        server.
  --room-invite ROOM_INVITE [ROOM_INVITE ...]
                        Invite one ore more users to join one or more rooms.
                        Specify the user(s) as arguments to --user. Specify
                        the rooms as arguments to this option, i.e. as
                        arguments to --room-invite. The user must have
                        permissions to invite users.
  --room-ban ROOM_BAN [ROOM_BAN ...]
                        Ban one ore more users from one or more rooms. Specify
                        the user(s) as arguments to --user. Specify the rooms
                        as arguments to this option, i.e. as arguments to
                        --room-ban. The user must have permissions to ban
                        users.
  --room-unban ROOM_UNBAN [ROOM_UNBAN ...]
                        Unban one ore more users from one or more rooms.
                        Specify the user(s) as arguments to --user. Specify
                        the rooms as arguments to this option, i.e. as
                        arguments to --room-unban. The user must have
                        permissions to unban users.
  --room-kick ROOM_KICK [ROOM_KICK ...]
                        Kick one ore more users from one or more rooms.
                        Specify the user(s) as arguments to --user. Specify
                        the rooms as arguments to this option, i.e. as
                        arguments to --room-kick. The user must have
                        permissions to kick users.
  --user USER [USER ...]
                        Specify one or multiple users. This option is only
                        meaningful in combination with options like --room-
                        invite, --room-ban, --room-unban, --room-kick. This
                        option --user specifies the users to be used with
                        these other room commands (like invite, ban, etc.)
  --name NAME [NAME ...]
                        Specify one or multiple names. This option is only
                        meaningful in combination with option --room-create.
                        This option --name specifies the names to be used with
                        the command --room-create.
  --topic TOPIC [TOPIC ...]
                        Specify one or multiple topics. This option is only
                        meaningful in combination with option --room-create.
                        This option --topic specifies the topics to be used
                        with the command --room-create.
  -m MESSAGE [MESSAGE ...], --message MESSAGE [MESSAGE ...]
                        Send this message. If not specified, and no input
                        piped in from stdin, then message will be read from
                        stdin, i.e. keyboard. This option can be used multiple
                        time to send multiple messages. If there is data is
                        piped into this program, then first data from the pipe
                        is published, then messages from this option are
                        published.
  -i IMAGE [IMAGE ...], --image IMAGE [IMAGE ...]
                        Send this image. This option can be used multiple time
                        to send multiple images. First images are send, then
                        text messages are send.
  -a AUDIO [AUDIO ...], --audio AUDIO [AUDIO ...]
                        Send this audio file. This option can be used multiple
                        time to send multiple audio files. First audios are
                        send, then text messages are send.
  -f FILE [FILE ...], --file FILE [FILE ...]
                        Send this file (e.g. PDF, DOC, MP4). This option can
                        be used multiple time to send multiple files. First
                        files are send, then text messages are send.
  -w, --html            Send message as format "HTML". If not specified,
                        message will be sent as format "TEXT". E.g. that
                        allows some text to be bold, etc. Only a subset of
                        HTML tags are accepted by Matrix.
  -z, --markdown        Send message as format "MARKDOWN". If not specified,
                        message will be sent as format "TEXT". E.g. that
                        allows sending of text formated in MarkDown language.
  -k, --code            Send message as format "CODE". If not specified,
                        message will be sent as format "TEXT". If both --html
                        and --code are specified then --code takes priority.
                        This is useful for sending ASCII-art or tabbed output
                        like tables as a fixed-sized font will be used for
                        display.
  -p SPLIT, --split SPLIT
                        If set, split the message(s) into multiple messages
                        wherever the string specified with --split occurs.
                        E.g. One pipes a stream of RSS articles into the
                        program and the articles are separated by three
                        newlines. Then with --split set to "\n\n\n" each
                        article will be printed in a separate message. By
                        default, i.e. if not set, no messages will be split.
  -j CONFIG, --config CONFIG
                        Location of a config file. By default, no config file
                        is used. If this option is provided, the provided file
                        name will be used to read configuration from.
  --proxy PROXY         Optionally specify a proxy for connectivity. By
                        default, i.e. if this option is not set, no proxy is
                        used. If this option is used a proxy URL must be
                        provided. The provided proxy URL will be used for the
                        HTTP connection to the server. The proxy supports
                        SOCKS4(a), SOCKS5, and HTTP (tunneling). Examples of
                        valid URLs are "http://10.10.10.10:8118" or
                        "socks5://user:password@127.0.0.1:1080".
  -n, --notice          Send message as notice. If not specified, message will
                        be sent as text.
  -e, --encrypted       Send message end-to-end encrypted. Encryption is
                        always turned on and will always be used where
                        possible. It cannot be turned off. This flag does
                        nothing as encryption is turned on with or without
                        this argument.
  -s STORE, --store STORE
                        Path to directory to be used as "store" for encrypted
                        messaging. By default, this directory is "./store/".
                        Since encryption is always enabled, a store is always
                        needed. If this option is provided, the provided
                        directory name will be used as persistent storage
                        directory instead of the default one. Preferably, for
                        multiple executions of this program use the same store
                        for the same device. The store directory can be shared
                        between multiple different devices and users.
  -l [LISTEN], --listen [LISTEN]
                        The --listen option takes one argument. There are
                        several choices: "never", "once", "forever", "tail",
                        and "all". By default, --listen is set to "never". So,
                        by default no listening will be done. Set it to
                        "forever" to listen for and print incoming messages to
                        stdout. "--listen forever" will listen to all messages
                        on all rooms forever. To stop listening "forever", use
                        Control-C on the keyboard or send a signal to the
                        process or service. The PID for signaling can be found
                        in a PID file in directory "/home/user/.run". "--
                        listen once" will get all the messages from all rooms
                        that are currently queued up. So, with "once" the
                        program will start, print waiting messages (if any)
                        and then stop. The timeout for "once" is set to 10
                        seconds. So, be patient, it might take up to that
                        amount of time. "tail" reads and prints the last N
                        messages from the specified rooms, then quits. The
                        number N can be set with the --tail option. With
                        "tail" some messages read might be old, i.e. already
                        read before, some might be new, i.e. never read
                        before. It prints the messages and then the program
                        stops. Messages are sorted, last-first. Look at --tail
                        as that option is related to --listen tail. The option
                        "all" gets all messages available, old and new. Unlike
                        "once" and "forever" that listen in ALL rooms, "tail"
                        and "all" listen only to the room specified in the
                        credentials file or the --room options. Furthermore,
                        when listening to messages, no messages will be sent.
                        Hence, when listening, --message must not be used and
                        piped input will be ignored.
  -t [TAIL], --tail [TAIL]
                        The --tail option reads and prints up to the last N
                        messages from the specified rooms, then quits. It
                        takes one argument, an integer, which we call N here.
                        If there are fewer than N messages in a room, it reads
                        and prints up to N messages. It gets the last N
                        messages in reverse order. It print the newest message
                        first, and the oldest message last. If --listen-self
                        is not set it will print less than N messages in many
                        cases because N messages are obtained, but some of
                        them are discarded by default if they are from the
                        user itself. Look at --listen as this option is
                        related to --tail.Furthermore, when tailing messages,
                        no messages will be sent. Hence, when tailing or
                        listening, --message must not be used and piped input
                        will be ignored.
  -y, --listen-self     If set and listening, then program will listen to and
                        print also the messages sent by its own user. By
                        default messages from oneself are not printed.
  --print-event-id      If set and listening, then program will print also the
                        event id foreach message or other event.
  -u [DOWNLOAD_MEDIA], --download-media [DOWNLOAD_MEDIA]
                        If set and listening, then program will download
                        received media files (e.g. image, audio, video, text,
                        PDF files). media will be downloaded to local
                        directory. By default, media will be downloaded to is
                        "./media/". You can overwrite default with your
                        preferred directory. If media is encrypted it will be
                        decrypted and stored decrypted. By default media files
                        will not be downloaded.
  -o, --os-notify       If set and listening, then program will attempt to
                        visually notify of arriving messages through the
                        operating system. By default there is no notification
                        via OS.
  -v [VERIFY], --verify [VERIFY]
                        Perform verification. By default, no verification is
                        performed. Possible values are: "emoji". If
                        verification is desired, run this program in the
                        foreground (not as a service) and without a pipe.
                        Verification questions will be printed on stdout and
                        the user has to respond via the keyboard to accept or
                        reject verification. Once verification is complete,
                        stop the program and run it as a service again. Don't
                        send messages or files when you verify.
  -x RENAME_DEVICE, --rename-device RENAME_DEVICE
                        Rename the current device to the new device name
                        provided. No other operations like sending, listening,
                        or verifying are allowed when renaming the device.
  --version             Print version information. After printing version
                        information program will continue to run. This is
                        useful for having version number in the log files.
```

# Features

- CLI, Command Line Interface
- Python 3
- Uses nio-template
- End-to-end encryption
- Storage for End-to-end encryption
- Storage of credentials
- Supports access token instead of password
- Sending messages
- Sending notices
- Sending formatted messages
- Sending MarkDown messages
- Message splitting before sending
- Sending Code-formatted messages
- Sending to one room
- Sending to multiple rooms
- Sending image files (photos, etc.)
- Sending of media files (music, videos, etc.)
- Sending of arbitrary files (PDF, xls, doc, txt, etc.)
- Receiving messages forever
- Receiving messages once
- Receiving last messages
- Receiving or skipping its own messages
- Receiving and downloading media files
  - including automatic decryption
- Creating new rooms
- Joining rooms
- Leaving rooms
- Forgetting rooms
- Inviting other users to rooms
- Banning from rooms
- Unbanning from rooms
- Kicking from rooms
- Supports renaming of device
- Supports notification via OS of received messages
- Supports periodic execution via crontab
- Supports room aliases
- Provides PID files
- Logging (at various levels)
- In-source documentation
- Can be run as a service

# For Developers

- Don't change tabbing, spacing, or formating as file is automatically
  sorted, linted and formated.
- `pylama:format=pep8:linters=pep8`
- first `isort` import sorter
- then `flake8` linter/formater
- then `black` linter/formater
- linelength: 79
  - isort matrix-commander.py
  - flake8 matrix-commander.py
  - python3 -m black --line-length 79 matrix-commander.py


# Things to do, Things missing

- help me add config file handling
- see Issues on Github

# Final Remarks

- Thanks to all of you who already have contributed! So appreciated!
- Enjoy!
- Pull requests are welcome  :heart:

"""

# automatically sorted by isort,
# then formatted by black --line-length 79
import argparse
import asyncio
import datetime
import getpass
import json
import logging
import os
import re  # regular expression
import select
import sys
import tempfile
import textwrap
import traceback
import urllib.request
import uuid
from urllib.parse import urlparse

import aiofiles
import aiofiles.os
import magic
from aiohttp import ClientConnectorError
from markdown import markdown
from nio import (
    AsyncClient,
    AsyncClientConfig,
    EnableEncryptionBuilder,
    JoinError,
    KeyVerificationCancel,
    KeyVerificationEvent,
    KeyVerificationKey,
    KeyVerificationMac,
    KeyVerificationStart,
    LocalProtocolError,
    LoginResponse,
    MatrixRoom,
    MessageDirection,
    ProfileGetAvatarResponse,
    RedactedEvent,
    RedactionEvent,
    RoomAliasEvent,
    RoomBanError,
    RoomCreateError,
    RoomEncryptedAudio,
    RoomEncryptedFile,
    RoomEncryptedImage,
    RoomEncryptedMedia,
    RoomEncryptedVideo,
    RoomEncryptionEvent,
    RoomForgetError,
    RoomInviteError,
    RoomKickError,
    RoomLeaveError,
    RoomMemberEvent,
    RoomMessage,
    RoomMessageAudio,
    RoomMessageEmote,
    RoomMessageFile,
    RoomMessageFormatted,
    RoomMessageImage,
    RoomMessageMedia,
    RoomMessageNotice,
    RoomMessagesError,
    RoomMessageText,
    RoomMessageUnknown,
    RoomMessageVideo,
    RoomNameEvent,
    RoomReadMarkersError,
    RoomResolveAliasError,
    RoomUnbanError,
    SyncError,
    SyncResponse,
    ToDeviceError,
    UnknownEvent,
    UpdateDeviceError,
    UploadResponse,
    crypto,
)
from PIL import Image

try:
    import notify2

    HAVE_NOTIFY = True
except ImportError:
    HAVE_NOTIFY = False


# version number
VERSION = "2021-March-14"
# matrix-commander
PROG_WITHOUT_EXT = os.path.splitext(os.path.basename(__file__))[0]
# matrix-commander.py
PROG_WITH_EXT = os.path.basename(__file__)
# file to store credentials in case you want to run program multiple times
CREDENTIALS_FILE_DEFAULT = "credentials.json"  # login credentials JSON file
# e.g. ~/.config/matrix-commander/
CREDENTIALS_DIR_LASTRESORT = (
    os.path.expanduser("~/.config/")
    + os.path.splitext(os.path.basename(__file__))[0]
)
# directory to be used by end-to-end encrypted protocol for persistent storage
STORE_DIR_DEFAULT = "./store/"
# e.g. ~/.local/share/matrix-commander/
# the STORE_PATH_LASTRESORT will be concatenated with a directory name
# like store to result in a final path of
# e.g. ~/.local/share/matrix-commander/store/ as actual persistent store dir
STORE_PATH_LASTRESORT = os.path.normpath(
    (
        os.path.expanduser("~/.local/share/")
        + os.path.splitext(os.path.basename(__file__))[0]
    )
)
# e.g. ~/.local/share/matrix-commander/store/
STORE_DIR_LASTRESORT = os.path.normpath(
    (os.path.expanduser(STORE_PATH_LASTRESORT + "/" + STORE_DIR_DEFAULT))
)
# directory to be used for downloading media files
MEDIA_DIR_DEFAULT = "./media/"
# usually there are no permissions for using: /run/matrix-commander.pid
# so instead local files like ~/.run/matrix-commander.some-uuid-here.pid will
# be used for storing the PID(s) for sending signals.
# There might be more than 1 process running in parallel, so there might be
# more than 1 PID at a given point in time.
PID_DIR_DEFAULT = os.path.normpath(os.path.expanduser("~/.run/"))
PID_FILE_DEFAULT = os.path.normpath(
    PID_DIR_DEFAULT + "/" + PROG_WITHOUT_EXT + "." + str(uuid.uuid4()) + ".pid"
)
EMOJI = "emoji"  # verification type
ONCE = "once"  # listening type
NEVER = "never"  # listening type
FOREVER = "forever"  # listening type
ALL = "all"  # listening type
TAIL = "tail"  # listening type
LISTEN_DEFAULT = NEVER
TAIL_UNUSED_DEFAULT = 0  # get 0 if --tail is not specified
TAIL_USED_DEFAULT = 10  # get the last 10 msgs by default with --tail
VERIFY_UNUSED_DEFAULT = None  # use None if --verify is not specified
VERIFY_USED_DEFAULT = "emoji"  # use emoji by default with --verify
RENAME_DEVICE_UNUSED_DEFAULT = None  # use None if -m is not specified


def choose_available_filename(filename):
    """Return next available filename.

    If filename (includes path) does not exist,
    then it returns filename. If file already
    exists it adds a counter at end, before
    extension, and increases counter until it
    finds a filename that does not yet exist.
    This avoids overwritting files when sources
    have same name.
    """
    if os.path.exists(filename):
        try:
            start, ext = filename.rsplit(".", 1)
        except ValueError:
            start, ext = (filename, "")
        i = 0
        while os.path.exists(f"{start}_{i}.{ext}"):
            i += 1
        return f"{start}_{i}.{ext}"
    else:
        return filename


async def download_mxc(client: AsyncClient, url: str):
    """Download MXC resource."""
    mxc = urlparse(url)
    response = await client.download(mxc.netloc, mxc.path.strip("/"))
    return response.body


class Callbacks(object):
    """Class to pass client to callback methods."""

    def __init__(self, client):
        """Store AsyncClient."""
        self.client = client

    # according to pylama: function too complex: C901 # noqa: C901
    async def message_callback(self, room: MatrixRoom, event):  # noqa: C901
        """Handle all events of type RoomMessage.

        Includes events like RoomMessageText, RoomMessageImage, etc.
        """
        try:
            logger.debug(
                f"message_callback(): for room {room} received this "
                f"event: type: {type(event)}, event_id: {event.event_id}, "
                f"event: {event}"
            )
            if not pargs.listen_self:
                if event.sender == self.client.user:
                    try:
                        logger.debug(
                            f"Skipping message sent by myself: {event.body}"
                        )
                    except AttributeError:  # does not have .body
                        logger.debug(
                            f"Skipping message sent by myself: {event}"
                        )
                    return

            # millisec since 1970
            logger.debug(f"event.server_timestamp = {event.server_timestamp}")
            timestamp = datetime.datetime.fromtimestamp(
                int(event.server_timestamp / 1000)
            )  # sec since 1970
            event_datetime = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            # e.g. 2020-08-06 17:30:18
            logger.debug(f"event_datetime = {event_datetime}")

            if isinstance(event, RoomMessageMedia):  # for all media events
                media_mxc = event.url
                media_url = await self.client.mxc_to_http(media_mxc)
                logger.debug(f"HTTP URL of media is : {media_url}")
                msg_url = " [" + media_url + "]"
                if pargs.download_media != "":
                    # download unencrypted media file
                    media_data = await download_mxc(self.client, media_mxc)
                    filename = choose_available_filename(
                        os.path.join(pargs.download_media, event.body)
                    )
                    async with aiofiles.open(filename, "wb") as f:
                        await f.write(media_data)
                        # Set atime and mtime of file to event timestamp
                        os.utime(
                            filename,
                            ns=((event.server_timestamp * 1000000,) * 2),
                        )
                    msg_url += f" [Downloaded media file to {filename}]"

            if isinstance(event, RoomEncryptedMedia):  # for all e2e media
                media_mxc = event.url
                media_url = await self.client.mxc_to_http(media_mxc)
                logger.debug(f"HTTP URL of media is : {media_url}")
                msg_url = " [" + media_url + "]"
                if pargs.download_media != "":
                    # download encrypted media file
                    media_data = await download_mxc(self.client, media_mxc)
                    filename = choose_available_filename(
                        os.path.join(pargs.download_media, event.body)
                    )
                    async with aiofiles.open(filename, "wb") as f:
                        await f.write(
                            crypto.attachments.decrypt_attachment(
                                media_data,
                                event.source["content"]["file"]["key"]["k"],
                                event.source["content"]["file"]["hashes"][
                                    "sha256"
                                ],
                                event.source["content"]["file"]["iv"],
                            )
                        )
                        # Set atime and mtime of file to event timestamp
                        os.utime(
                            filename,
                            ns=((event.server_timestamp * 1000000,) * 2),
                        )
                    msg_url += (
                        f" [Downloaded and decrypted media file to {filename}]"
                    )

            if isinstance(event, RoomMessageAudio):
                msg = "Received audio: " + event.body + msg_url
            elif isinstance(event, RoomMessageEmote):
                msg = "Received emote: " + event.body
            elif isinstance(event, RoomMessageFile):
                msg = "Received file: " + event.body + msg_url
            elif isinstance(event, RoomMessageFormatted):
                msg = event.body
            elif isinstance(event, RoomMessageImage):
                # Usually body is something like "image.svg"
                msg = "Received image: " + event.body + msg_url
            elif isinstance(event, RoomMessageNotice):
                msg = event.body  # Extract the message text
            elif isinstance(event, RoomMessageText):
                msg = event.body  # Extract the message text
            elif isinstance(event, RoomMessageUnknown):
                msg = "Received room message of unknown type: " + event.msgtype
            elif isinstance(event, RoomMessageVideo):
                msg = "Received video: " + event.body + msg_url
            elif isinstance(event, RoomEncryptedAudio):
                msg = "Received encrypted audio: " + event.body + msg_url
            elif isinstance(event, RoomEncryptedFile):
                msg = "Received encrypted file: " + event.body + msg_url
            elif isinstance(event, RoomEncryptedImage):
                # Usually body is something like "image.svg"
                msg = "Received encrypted image: " + event.body + msg_url
            elif isinstance(event, RoomEncryptedVideo):
                msg = "Received encrypted video: " + event.body + msg_url
            elif isinstance(event, RoomMessageMedia):
                # this should never be reached, this is a base class
                # it should be a audio, image, video, etc.
                # Put here at the end as defensive programming
                msg = "Received media: " + event.body + msg_url
            elif isinstance(event, RoomEncryptedMedia):
                # this should never be reached, this is a base class
                # it should be a audio, image, video, etc.
                # Put here at the end as defensive programming
                msg = "Received encrypted media: " + event.body + msg_url
            elif isinstance(event, RoomMemberEvent):
                msg = (
                    "Received room-member event: "
                    f"sender: {event.sender}, operation: {event.membership}"
                )
            elif isinstance(event, RoomEncryptionEvent):
                msg = (
                    "Received room-encryption event: "
                    f"sender: {event.sender}"
                )
            elif isinstance(event, RoomAliasEvent):
                msg = (
                    "Received room-alias event: sender: "
                    f"{event.sender}, alias: {event.canonical_alias}"
                )
            elif isinstance(event, RoomNameEvent):
                msg = (
                    "Received room-name event: sender: "
                    f"{event.sender}, room name: {event.name}"
                )
            elif isinstance(event, RedactedEvent):
                msg = (
                    "Received redacted event: "
                    f"sender: {event.sender}, "
                    f"type: {event.type}, redacter: {event.redacter}"
                )
            elif isinstance(event, RedactionEvent):
                msg = (
                    "Received redaction event: "
                    f"sender: {event.sender}, "
                    f"redacts: {event.redacts}"
                )
            elif isinstance(event, UnknownEvent):
                if event.type == "m.reaction":
                    msg = (
                        "Received a reaction, an emoji: "
                        f"{event.source['content']['m.relates_to']['key']}"
                    )
                else:
                    msg = f"Received unknown event: {event}"
            else:
                msg = f"Received unknown event: {event}"

            # if event['type'] == "m.room.message":
            #    if event['content']['msgtype'] == "m.text":
            #        content = event['content']['body']
            #    else:
            #        download_url = api.get_download_url(
            #            event['content']['url'])
            #        content = download_url
            # else:
            #    content = "\n{{ " + event['type'] + " event }}\n"
            logger.debug(f"type(msg) = {type(msg)}. msg is a string")
            sender_nick = room.user_name(event.sender)
            if not sender_nick:  # convert @foo:mat.io into foo
                sender_nick = event.sender.split(":")[0][1:]
            room_nick = room.display_name
            if not room_nick or room_nick == "Empty Room" or room_nick == "":
                room_nick = "Undetermined"
            if pargs.print_event_id:
                event_id_detail = f" | {event.event_id}"
            else:
                event_id_detail = ""
            complete_msg = (
                "Message received for room "
                f"{room_nick} [{room.room_id}] | "
                f"sender {sender_nick} "
                f"[{event.sender}] | {event_datetime}"
                f"{event_id_detail} | {msg}"
            )
            logger.debug(complete_msg)
            print(complete_msg, flush=True)
            if pargs.os_notify:
                avatar_url = await get_avatar_url(self.client, event.sender)
                notify(
                    f"From {room.user_name(event.sender)}",
                    msg[:160],
                    avatar_url,
                )

        except BaseException:
            logger.debug(traceback.format_exc())

    # according to linter: function is too complex, C901
    async def to_device_callback(self, event):  # noqa: C901
        """Handle events sent to device."""
        try:
            client = self.client

            if isinstance(event, KeyVerificationStart):  # first step
                """first step: receive KeyVerificationStart
                KeyVerificationStart(
                    source={'content':
                            {'method': 'm.sas.v1',
                             'from_device': 'DEVICEIDXY',
                             'key_agreement_protocols':
                                ['curve25519-hkdf-sha256', 'curve25519'],
                             'hashes': ['sha256'],
                             'message_authentication_codes':
                                ['hkdf-hmac-sha256', 'hmac-sha256'],
                             'short_authentication_string':
                                ['decimal', 'emoji'],
                             'transaction_id': 'SomeTxId'
                             },
                            'type': 'm.key.verification.start',
                            'sender': '@user2:example.org'
                            },
                    sender='@user2:example.org',
                    transaction_id='SomeTxId',
                    from_device='DEVICEIDXY',
                    method='m.sas.v1',
                    key_agreement_protocols=[
                        'curve25519-hkdf-sha256', 'curve25519'],
                    hashes=['sha256'],
                    message_authentication_codes=[
                        'hkdf-hmac-sha256', 'hmac-sha256'],
                    short_authentication_string=['decimal', 'emoji'])
                """

                if "emoji" not in event.short_authentication_string:
                    print(
                        "Other device does not support emoji verification "
                        f"{event.short_authentication_string}."
                    )
                    return
                resp = await client.accept_key_verification(
                    event.transaction_id
                )
                if isinstance(resp, ToDeviceError):
                    print(f"accept_key_verification failed with {resp}")

                sas = client.key_verifications[event.transaction_id]

                todevice_msg = sas.share_key()
                resp = await client.to_device(todevice_msg)
                if isinstance(resp, ToDeviceError):
                    print(f"to_device failed with {resp}")

            elif isinstance(event, KeyVerificationCancel):  # anytime
                """at any time: receive KeyVerificationCancel
                KeyVerificationCancel(source={
                    'content': {'code': 'm.mismatched_sas',
                                'reason': 'Mismatched authentication string',
                                'transaction_id': 'SomeTxId'},
                    'type': 'm.key.verification.cancel',
                    'sender': '@user2:example.org'},
                    sender='@user2:example.org',
                    transaction_id='SomeTxId',
                    code='m.mismatched_sas',
                    reason='Mismatched short authentication string')
                """

                # There is no need to issue a
                # client.cancel_key_verification(tx_id, reject=False)
                # here. The SAS flow is already cancelled.
                # We only need to inform the user.
                print(
                    f"Verification has been cancelled by {event.sender} "
                    f'for reason "{event.reason}".'
                )

            elif isinstance(event, KeyVerificationKey):  # second step
                """Second step is to receive KeyVerificationKey
                KeyVerificationKey(
                    source={'content': {
                            'key': 'SomeCryptoKey',
                            'transaction_id': 'SomeTxId'},
                        'type': 'm.key.verification.key',
                        'sender': '@user2:example.org'
                    },
                    sender='@user2:example.org',
                    transaction_id='SomeTxId',
                    key='SomeCryptoKey')
                """
                sas = client.key_verifications[event.transaction_id]

                print(f"{sas.get_emoji()}")

                yn = input("Do the emojis match? (Y/N) (C for Cancel) ")
                if yn.lower() == "y":
                    print(
                        "Match! The verification for this "
                        "device will be accepted."
                    )
                    resp = await client.confirm_short_auth_string(
                        event.transaction_id
                    )
                    if isinstance(resp, ToDeviceError):
                        print(f"confirm_short_auth_string failed with {resp}")
                elif yn.lower() == "n":  # no, don't match, reject
                    print(
                        "No match! Device will NOT be verified "
                        "by rejecting verification."
                    )
                    resp = await client.cancel_key_verification(
                        event.transaction_id, reject=True
                    )
                    if isinstance(resp, ToDeviceError):
                        print(f"cancel_key_verification failed with {resp}")
                else:  # C or anything for cancel
                    print("Cancelled by user! Verification will be cancelled.")
                    resp = await client.cancel_key_verification(
                        event.transaction_id, reject=False
                    )
                    if isinstance(resp, ToDeviceError):
                        print(f"cancel_key_verification failed with {resp}")

            elif isinstance(event, KeyVerificationMac):  # third step
                """Third step is to receive KeyVerificationMac
                KeyVerificationMac(
                    source={'content': {
                        'mac': {'ed25519:DEVICEIDXY': 'SomeKey1',
                                'ed25519:SomeKey2': 'SomeKey3'},
                        'keys': 'SomeCryptoKey4',
                        'transaction_id': 'SomeTxId'},
                        'type': 'm.key.verification.mac',
                        'sender': '@user2:example.org'},
                    sender='@user2:example.org',
                    transaction_id='SomeTxId',
                    mac={'ed25519:DEVICEIDXY': 'SomeKey1',
                         'ed25519:SomeKey2': 'SomeKey3'},
                    keys='SomeCryptoKey4')
                """
                sas = client.key_verifications[event.transaction_id]
                try:
                    todevice_msg = sas.get_mac()
                except LocalProtocolError as e:
                    # e.g. it might have been cancelled by ourselves
                    print(
                        f"Cancelled or protocol error: Reason: {e}.\n"
                        f"Verification with {event.sender} not concluded. "
                        "Try again?"
                    )
                else:
                    resp = await client.to_device(todevice_msg)
                    if isinstance(resp, ToDeviceError):
                        print(f"to_device failed with {resp}")
                    print(
                        f"sas.we_started_it = {sas.we_started_it}\n"
                        f"sas.sas_accepted = {sas.sas_accepted}\n"
                        f"sas.canceled = {sas.canceled}\n"
                        f"sas.timed_out = {sas.timed_out}\n"
                        f"sas.verified = {sas.verified}\n"
                        f"sas.verified_devices = {sas.verified_devices}\n"
                    )
                    print(
                        "Emoji verification was successful!\n"
                        "Hit Control-C to stop the program or "
                        "initiate another Emoji verification from "
                        "another device or room."
                    )
            else:
                print(
                    f"Received unexpected event type {type(event)}. "
                    f"Event is {event}. Event will be ignored."
                )
        except BaseException:
            print(traceback.format_exc())


def notify(title: str, content: str, image_url: str):
    """Notify OS of message receipt.

    If the system is running headless or any problem happens with
    operating system notifications, ignore it.
    """
    if not HAVE_NOTIFY:
        logger.warning(
            "notify2 or dbus is not installed. Notifications will not be "
            "displayed.\n"
            "Make sure that notify2 and dbus are installed or remove the "
            "--os-notify option."
        )
        return
    try:
        if image_url:
            notused, avatar_file = tempfile.mkstemp()
            urllib.request.urlretrieve(image_url, avatar_file)
            # TODO: cleanup temp files? in cleanup()?
        else:
            # Icon name "notification-message-IM" will work on Ubuntu
            # but not all platforms
            avatar_file = "notification-message-IM"
        notify2.init(PROG_WITHOUT_EXT)
        notify2.Notification(title, content, avatar_file).show()
        logger.debug(f"Showed notification for {title}.")
    except Exception:
        logger.debug(f"Showing notification for {title} failed.")
        print(traceback.format_exc())
        pass


def is_room_alias(room_id: str) -> bool:
    """Determine if room identifier is a room alias.

    Alias are of syntax: #somealias:someserver

    """
    if room_id and len(room_id) > 3 and room_id[0] == "#":
        return True
    else:
        return False


async def get_avatar_url(client: AsyncClient, user_id: str) -> str:
    """Get https avatar URL for user user_id.

    Returns URL or None if user has no avatar
    """
    avatar_url = None  # default
    resp = await client.get_avatar(user_id)
    if isinstance(resp, ProfileGetAvatarResponse):
        logger.debug(f"ProfileGetAvatarResponse. Response is: {resp}")
        avatar_mxc = resp.avatar_url
        logger.debug(f"avatar_mxc is {avatar_mxc}")
        if avatar_mxc:  # could be None if no avatar
            avatar_url = await client.mxc_to_http(avatar_mxc)
    else:
        logger.info(f"Failed getting avatar from server. {resp}")
    logger.debug(f"avatar_url is {avatar_url}")
    return avatar_url


def create_pid_file() -> None:
    """Write PID to disk.

    If possible create a PID file. This is not essential.
    So, if it fails there is no problem. The PID file can
    be helpful to send a kill signal or similar to the process.
    E.g. to stop listening.
    Because the user can start several processes at the same time,
    just having one PID file is not acceptable because a newly started
    process would overwrite the previous PID file. We use UUIDs to make
    each PID file unique.
    """
    try:
        if not os.path.exists(PID_DIR_DEFAULT):
            os.mkdir(PID_DIR_DEFAULT)
            logger.debug(f"Create directory {PID_DIR_DEFAULT} for PID file.")
        pid = os.getpid()
        logger.debug(f"Trying to create a PID file to store process id {pid}.")
        with open(PID_FILE_DEFAULT, "w") as f:  # overwrite
            f.write(str(pid))
            f.close()
        logger.debug(
            f'Successfully created PID file "{PID_FILE_DEFAULT}" '
            f"to store process id {pid}."
        )
    except Exception:
        logger.debug(
            f'Failed to create PID file "{PID_FILE_DEFAULT}" '
            f"to store process id {os.getpid()}."
        )


def delete_pid_file() -> None:
    """Remove PID file from disk.

    Clean up by removing PID file.
    It might not exist. So, ignore failures.
    """
    try:
        os.remove(PID_FILE_DEFAULT)
    except Exception:
        logger.debug(f'Failed to remove PID file "{PID_FILE_DEFAULT}".')


def cleanup() -> None:
    """Cleanup before quiting program."""
    logger.debug("Cleanup: cleaning up.")
    delete_pid_file()


def write_credentials_to_disk(
    homeserver, user_id, device_id, access_token, room_id, credentials_file
) -> None:
    """Write the required login details to disk.

    This file can later be used for logging in
    without using a password.

    Arguments:
    ---------
        homeserver : str
            URL of homeserver, e.g. "https://matrix.example.org"
        user_id : str
            full user id, e.g. "@user:example.org"
        device_id : str
            device id, 10 uppercase letters
        access_token : str
            access token, long cryptographic access token
        room_id : str
            name of room where message will be sent to,
            e.g. "!SomeRoomIdString:example.org"
            user must be member of the provided room
        credentials_file : str
            name/path of file where to store
            credentials information

    """
    # open the credentials file in write-mode
    with open(credentials_file, "w") as f:
        # write the login details to disk
        json.dump(
            {
                # e.g. "https://matrix.example.org"
                "homeserver": homeserver,
                # device ID, 10 uppercase letters
                "device_id": device_id,
                # e.g. "@user:example.org"
                "user_id": user_id,
                # e.g. "!SomeRoomIdString:example.org"
                "room_id": room_id,
                # long cryptographic access token
                "access_token": access_token,
            },
            f,
        )


def read_credentials_from_disk(credentials_file) -> dict:
    """Read the required login details from disk.

    It can then be used to log in without using a password.

    Arguments:
    ---------
    credentials_file : str
        name/path of file to read credentials information from

    """
    # open the file in read-only mode
    with open(credentials_file, "r") as f:
        return json.load(f)


def determine_credentials_file() -> str:
    """Determine the true filename of credentials file.

    Returns filename with full path or None.

    This function checks if a credentials file exists. If no, it will ask
    user questions regrading login, store the info in a newly created
    credentials file and exit.

    If a credentials file exists, it will read it, log into Matrix,
    send a message and exit.

    The credential file will be looked for the following way:
    a) if a path (e.g. "../cred.json") is specified with -t it will be looked
       for there. End of search.
    b) if only a filename without path (e.g. "cred.json") is specified
       first look in the current local directory, if found use it
    c) if only a filename without path (e.g. "cred.json") is specified
       and it cannot be found in the current local directory, then
       look for it in directory $HOME/.config/matrix-commander/
    TLDR: on first run it will be written to current local directory
       or to path specified with --credentials command line argument.
       On further reads, program will look in currently local directory
       or in path specified with --credentials command line argument.
       If not found there (and only filename without path given),
       as a secondary choice program will look for it in
       directory $HOME/.config/matrix-commander/

    """
    credentials_file = pargs.credentials  # default location
    if (not os.path.isfile(pargs.credentials)) and (
        pargs.credentials == os.path.basename(pargs.credentials)
    ):
        logger.debug(
            "Credentials file does not exist locally. "
            "File name has no path."
        )
        credentials_file = CREDENTIALS_DIR_LASTRESORT + "/" + pargs.credentials
        logger.debug(
            f'Trying path "{credentials_file}" as last resort. '
            "Suggesting to look for it there."
        )
        if os.path.isfile(credentials_file):
            logger.debug(
                "We found the file. It exists in the last resort "
                f'directory "{credentials_file}". '
                "Suggesting to use this one."
            )
        else:
            logger.debug(
                "File does not exists either in the last resort "
                "directory or the local directory. "
                "File not found anywhere. One will have to be "
                "created. So we suggest the local directory."
            )
            credentials_file = pargs.credentials
    else:
        if os.path.isfile(pargs.credentials):
            logger.debug(
                "Credentials file existed. "
                "So this is the one we suggest to use. "
                f"file: {credentials_file}"
            )
        else:
            logger.debug(
                "Credentials file was specified with full path. "
                "So we suggest that one. "
                f"file: {credentials_file}"
            )
    # The returned file (with or without path)  might or might not exist.
    # But if it does not exist, it is either a full path, or local.
    # We do not want to return the last resort path if it does not exist,
    # so that when it is created it is created where specifically specified
    # or in local dir (but not in last resort dir ~/.config/...)
    return credentials_file


def determine_store_dir() -> str:
    """Determine the true full directory name of store directory.

    Returns filename with full path (a dir) or None.

    For historic reasons:
    If -e encrypted is NOT turned on, return None.

    The store path will be looked for the following way:
    pargs.store provides either default value or user specified value
    a) First looked at default/specified value. If dir exists,
       use it, end of search.
    b) if last-resort store dir exists, use it, end of search.
    c) if only a dirname without path (e.g. "store") is specified
       and it cannot be found in the current local directory, then
       look for it in last-resort path.
    TLDR: The program will look in path specified with --store
       command line argument. If not found there in default
       local dir. If not found there in last-resort dir.
       If not found there (and only dirname without path given),
       as a final choice, the program will look for it in
       last resort path.
    If not found anywhere, it will return default/specified value.

    """
    if not pargs.store:
        return None
    if not pargs.encrypted:
        return None
    pargs_store_norm = os.path.normpath(pargs.store)  # normailzed for humans
    text2 = (
        "It will need to be verified.\n"
        "The store directory will be created in the "
        f'directory "{pargs_store_norm}". Optionally, consider moving '
        "the persistent storage directory files inside "
        f'"{pargs_store_norm}" into '
        f'the directory "{STORE_DIR_LASTRESORT}" '
        "for a more consistent experience."
    )
    if os.path.isdir(pargs.store):
        logger.debug(
            "Found an existing store in directory "
            f'"{pargs_store_norm}" (local or arguments). '
            "It will be used."
        )
        return pargs_store_norm
    if pargs.store != STORE_DIR_DEFAULT and pargs.store != os.path.basename(
        pargs.store
    ):
        text1 = (
            f'Store directory "{pargs_store_norm}" was specified by '
            "user, it is a directory with path, but it "
            "does not exist. Hence it will be created there. "
        )
        logger.info(text1 + text2)
        print(text1 + text2)
        return pargs_store_norm  # create in the specified, directory with path
    if pargs.store == STORE_DIR_DEFAULT and os.path.isdir(
        STORE_DIR_LASTRESORT
    ):
        logger.debug(
            "Store was not found in default local directory. "
            "But found an existing store directory in "
            f'"{STORE_DIR_LASTRESORT}" directory. '
            "It will be used."
        )
        return STORE_DIR_LASTRESORT

    if pargs.store == os.path.basename(pargs.store):
        logger.debug(
            f'Store directory "{pargs_store_norm}" is just a name '
            "without a path. Already looked locally, but not found "
            "locally. So now looking for it in last-resort path."
        )
        last_resort = os.path.normpath(
            STORE_PATH_LASTRESORT + "/" + pargs.store
        )
        if os.path.isdir(last_resort):
            logger.debug(
                "Found an existing store directory in "
                f'"{last_resort}" directory. It will be used.'
            )
            return last_resort
    text1 = (
        "Could not find existing store directory anywhere. "
        "A new one will be created. "
    )
    logger.debug(text1 + text2)
    print(textwrap.fill(textwrap.dedent(text1 + text2).strip(), width=79))
    return pargs_store_norm  # create in the specified, local dir without path


def determine_rooms(room_id) -> list:
    """Determine the room to send to.

    Arguments:
    ---------
    room_id : room from credentials file

    Look at room from credentials file and at rooms from command line
    and prepares a definite list of rooms.

    Return list of rooms to send to. Returned list is never empty.

    """
    if not pargs.room:
        logger.debug(
            "Room id was provided via credentials file. "
            "No rooms given in commands line.  "
            f'Setting rooms to "{room_id}".'
        )
        return [room_id]  # list of 1
    else:
        rooms = []
        for room in pargs.room:
            room_id = room.replace(r"\!", "!")  # remove possible escape
            rooms.append(room_id)
        logger.debug(
            "Room(s) were provided via command line. "
            "Overwriting room id from credentials file "
            f'with rooms "{rooms}" '
            "from command line."
        )
        return rooms


async def map_roomalias_to_roomid(client, alias) -> str:
    """Attempt to convert room alias to room_id.

    Arguments:
    ---------
    client : nio client
    alias : can be an alias in the form of '#someRoomALias:example.com'
        can also be a room_id in the form of '!someRoomId:example.com'

    room_id : room from credentials file

    If an alias try to get the corresponding room_id.
    If anything fails it returns the original input.

    Return corresponding room_id or on failure the original alias.

    """
    ret = alias
    if is_room_alias(alias):
        resp = await client.room_resolve_alias(alias)
        if isinstance(resp, RoomResolveAliasError):
            logger.error(
                f"room_resolve_alias for alias {alias} failed with {resp}. "
                f"Trying operation with input {alias} anyway. Might fail."
            )
        else:
            ret = resp.room_id
            logger.debug(
                f'Mapped room alias "{alias}" to room id "{ret}". '
                f"({resp.room_alias}, {resp.room_id})."
            )
    return ret


async def create_rooms(client, room_aliases, names, topics):
    """Create one or multiple rooms.

    Arguments:
    ---------
    client : nio client
    room_aliases : list of room aliases in the form of "sampleAlias"
            These aliases will then be used by the server and
            the server creates the definite alias in the form
            of "#sampleAlias:example.com" from it.
            Do not attempt to use "#sampleAlias:example.com"
            as it will confuse the server.
    names : list of names for rooms
    topics : list of room topics

    """
    try:
        index = 0
        for alias in room_aliases:
            alias = alias.replace(r"\!", "!")  # remove possible escape
            # alias is a true alias, not a room id
            # "alias1" will be converted into "#alias1:example.com"
            try:
                name = names[index]
            except IndexError:
                name = ""
            try:
                topic = topics[index]
            except IndexError:
                topic = ""
            logger.debug(
                f'Creating room with room alias "{alias}", '
                f'name "{name}", and topic "{topic}".'
            )
            resp = await client.room_create(
                alias=alias,
                name=name,  # room name
                topic=topic,  # room topic
                initial_state=[EnableEncryptionBuilder().as_dict()],
            )
            if isinstance(resp, RoomCreateError):
                logger.error(f"Room_create failed with {resp}")
            else:
                logger.info(f'Created room "{alias}".')
            index = index + 1
    except Exception:
        logger.error("Room creation failed. Sorry.")
        logger.debug("Here is the traceback.\n" + traceback.format_exc())


async def join_rooms(client, rooms):
    """Join one or multiple rooms."""
    try:
        for room_id in rooms:
            # room_id can be #roomAlias or !roomId
            room_id = room_id.replace(r"\!", "!")  # remove possible escape
            logger.debug(f'Joining room with room alias "{room_id}".')
            room_id = await map_roomalias_to_roomid(client, room_id)
            resp = await client.join(room_id)
            if isinstance(resp, JoinError):
                logger.error(f"join failed with {resp}")
            else:
                logger.info(f'Joined room "{room_id}" successfully.')
    except Exception:
        logger.error("Joining rooms failed. Sorry.")
        logger.debug("Here is the traceback.\n" + traceback.format_exc())


async def leave_rooms(client, rooms):
    """Leave one or multiple rooms."""
    try:
        for room_id in rooms:
            # room_id can be #roomAlias or !roomId
            room_id = room_id.replace(r"\!", "!")  # remove possible escape
            logger.debug(f'Leaving room with room alias "{room_id}".')
            room_id = await map_roomalias_to_roomid(client, room_id)
            resp = await client.room_leave(room_id)
            if isinstance(resp, RoomLeaveError):
                logger.error(f"Leave failed with {resp}")
            else:
                logger.info(f'Left room "{room_id}".')
    except Exception:
        logger.error("Room leave failed. Sorry.")
        logger.debug("Here is the traceback.\n" + traceback.format_exc())


async def forget_rooms(client, rooms):
    """Forget one or multiple rooms."""
    try:
        for room_id in rooms:
            # room_id can be #roomAlias or !roomId
            room_id = room_id.replace(r"\!", "!")  # remove possible escape
            logger.debug(f'Forgetting room with room alias "{room_id}".')
            room_id = await map_roomalias_to_roomid(client, room_id)
            resp = await client.room_forget(room_id)
            if isinstance(resp, RoomForgetError):
                logger.error(f"Forget failed with {resp}")
            else:
                logger.info(f'Forgot room "{room_id}".')
    except Exception:
        logger.error("Room forget failed. Sorry.")
        logger.debug("Here is the traceback.\n" + traceback.format_exc())


async def invite_to_rooms(client, rooms, users):
    """Invite one or multiple users to one or multiple rooms."""
    try:
        for room_id in rooms:
            # room_id can be #roomAlias or !roomId
            room_id = room_id.replace(r"\!", "!")  # remove possible escape
            room_id = await map_roomalias_to_roomid(client, room_id)
            for user in users:
                logger.debug(
                    f'Inviting user "{user}" to room with '
                    f'room alias "{room_id}".'
                )
                resp = await client.room_invite(room_id, user)
                if isinstance(resp, RoomInviteError):
                    logger.error(f"room_invite failed with {resp}")
                else:
                    logger.info(
                        f'User "{user}" was successfully invited '
                        f'to room "{room_id}".'
                    )
    except Exception:
        logger.error("User invite failed. Sorry.")
        logger.debug("Here is the traceback.\n" + traceback.format_exc())


async def ban_from_rooms(client, rooms, users):
    """Ban one or multiple users from one or multiple rooms."""
    try:
        for room_id in rooms:
            # room_id can be #roomAlias or !roomId
            room_id = room_id.replace(r"\!", "!")  # remove possible escape
            room_id = await map_roomalias_to_roomid(client, room_id)
            for user in users:
                logger.debug(
                    f'Banning user "{user}" from room with '
                    f'room alias "{room_id}".'
                )
                resp = await client.room_ban(room_id, user)
                if isinstance(resp, RoomBanError):
                    logger.error(f"room_ban failed with {resp}")
                else:
                    logger.info(
                        f'User "{user}" was successfully banned '
                        f'from room "{room_id}".'
                    )
    except Exception:
        logger.error("User ban failed. Sorry.")
        logger.debug("Here is the traceback.\n" + traceback.format_exc())


async def unban_from_rooms(client, rooms, users):
    """Unban one or multiple users from one or multiple rooms."""
    try:
        for room_id in rooms:
            # room_id can be #roomAlias or !roomId
            room_id = room_id.replace(r"\!", "!")  # remove possible escape
            room_id = await map_roomalias_to_roomid(client, room_id)
            for user in users:
                logger.debug(
                    f'Unbanning user "{user}" from room with '
                    f'room alias "{room_id}".'
                )
                resp = await client.room_unban(room_id, user)
                if isinstance(resp, RoomUnbanError):
                    logger.error(f"room_unban failed with {resp}")
                else:
                    logger.info(
                        f'User "{user}" was successfully unbanned '
                        f'from room "{room_id}".'
                    )
    except Exception:
        logger.error("User unban failed. Sorry.")
        logger.debug("Here is the traceback.\n" + traceback.format_exc())


async def kick_from_rooms(client, rooms, users):
    """Kick one or multiple users from one or multiple rooms."""
    try:
        for room_id in rooms:
            # room_id can be #roomAlias or !roomId
            room_id = room_id.replace(r"\!", "!")  # remove possible escape
            room_id = await map_roomalias_to_roomid(client, room_id)
            for user in users:
                logger.debug(
                    f'Kicking user "{user}" from room with '
                    f'room alias "{room_id}".'
                )
                resp = await client.room_kick(room_id, user)
                if isinstance(resp, RoomKickError):
                    logger.error(f"room_kick failed with {resp}")
                else:
                    logger.info(
                        f'User "{user}" was successfully kicked '
                        f'from room "{room_id}".'
                    )
    except Exception:
        logger.error("User kick failed. Sorry.")
        logger.debug("Here is the traceback.\n" + traceback.format_exc())


async def send_file(client, rooms, file):
    """Process file.

    Upload file to server and then send link to rooms.
    Works and tested for .pdf, .txt, .ogg, .wav.
    All these file types are treated the same.

    Do not use this function for images.
    Use the send_image() function for images.

    Matrix has types for audio and video (and image and file).
    See: "msgtype" == "m.image", m.audio, m.video, m.file

    Arguments:
    ---------
    client : Client
    rooms : list
        list of room_id-s
    file : str
        file name of file from --file argument

    This is a working example for a PDF file.
    It can be viewed or downloaded from:
    https://matrix.example.com/_matrix/media/r0/download/
        example.com/SomeStrangeUriKey
    {
        "type": "m.room.message",
        "sender": "@someuser:example.com",
        "content": {
            "body": "example.pdf",
            "info": {
                "size": 6301234,
                "mimetype": "application/pdf"
                },
            "msgtype": "m.file",
            "url": "mxc://example.com/SomeStrangeUriKey"
        },
        "origin_server_ts": 1595100000000,
        "unsigned": {
            "age": 1000,
            "transaction_id": "SomeTxId01234567"
        },
        "event_id": "$SomeEventId01234567789Abcdef012345678",
        "room_id": "!SomeRoomId:example.com"
    }

    """
    if not rooms:
        logger.info(
            "No rooms are given. This should not happen. "
            "This file is being droppend and NOT sent."
        )
        return
    if not os.path.isfile(file):
        logger.debug(
            f"File {file} is not a file. Doesn't exist or "
            "is a directory."
            "This file is being droppend and NOT sent."
        )
        return

    # # restrict to "txt", "pdf", "mp3", "ogg", "wav", ...
    # if not re.match("^.pdf$|^.txt$|^.doc$|^.xls$|^.mobi$|^.mp3$",
    #                os.path.splitext(file)[1].lower()):
    #    logger.debug(f"File {file} is not a permitted file type. Should be "
    #                 ".pdf, .txt, .doc, .xls, .mobi or .mp3 ... "
    #                 f"[{os.path.splitext(file)[1].lower()}]"
    #                 "This file is being droppend and NOT sent.")
    #    return

    # 'application/pdf' "plain/text" "audio/ogg"
    mime_type = magic.from_file(file, mime=True)
    # if ((not mime_type.startswith("application/")) and
    #        (not mime_type.startswith("plain/")) and
    #        (not mime_type.startswith("audio/"))):
    #    logger.debug(f"File {file} does not have an accepted mime type. "
    #                 "Should be something like application/pdf. "
    #                 f"Found mime type {mime_type}. "
    #                 "This file is being droppend and NOT sent.")
    #    return

    # first do an upload of file, see upload() documentation
    # http://matrix-nio.readthedocs.io/en/latest/nio.html#nio.AsyncClient.upload
    # then send URI of upload to room

    file_stat = await aiofiles.os.stat(file)
    async with aiofiles.open(file, "r+b") as f:
        resp, maybe_keys = await client.upload(
            f,
            content_type=mime_type,  # application/pdf
            filename=os.path.basename(file),
            filesize=file_stat.st_size,
        )
    if isinstance(resp, UploadResponse):
        logger.debug(
            f"File was uploaded successfully to server. Response is: {resp}"
        )
    else:
        logger.info(
            f"The program {PROG_WITH_EXT} failed to upload. "
            "Please retry. This could be temporary issue on "
            "your server. "
            "Sorry."
        )
        logger.info(
            f'file="{file}"; mime_type="{mime_type}"; '
            f'filessize="{file_stat.st_size}"'
            f"Failed to upload: {resp}"
        )

    # determine msg_type:
    if mime_type.startswith("audio/"):
        msg_type = "m.audio"
    elif mime_type.startswith("video/"):
        msg_type = "m.video"
    else:
        msg_type = "m.file"

    content = {
        "body": os.path.basename(file),  # descriptive title
        "info": {"size": file_stat.st_size, "mimetype": mime_type},
        "msgtype": msg_type,
        "url": resp.content_uri,
    }

    try:
        for room_id in rooms:
            await client.room_send(
                room_id, message_type="m.room.message", content=content
            )
            logger.info(f'This file was sent: "{file}" to room "{room_id}".')
    except Exception:
        logger.error(f"File send of file {file} failed. Sorry.")
        logger.debug("Here is the traceback.\n" + traceback.format_exc())


async def send_image(client, rooms, image):
    """Process image.

    Arguments:
    ---------
    client : Client
    rooms : list
        list of room_id-s
    image : str
        file name of image from --image argument

    This is a working example for a JPG image.
    It can be viewed or downloaded from:
    https://matrix.example.com/_matrix/media/r0/download/
        example.com/SomeStrangeUriKey
    {
        "type": "m.room.message",
        "sender": "@someuser:example.com",
        "content": {
            "body": "someimage.jpg",
            "info": {
                "size": 5420,
                "mimetype": "image/jpeg",
                "thumbnail_info": {
                    "w": 100,
                    "h": 100,
                    "mimetype": "image/jpeg",
                    "size": 2106
                },
                "w": 100,
                "h": 100,
                "thumbnail_url": "mxc://example.com/SomeStrangeThumbnailUriKey"
            },
            "msgtype": "m.image",
            "url": "mxc://example.com/SomeStrangeUriKey"
        },
        "origin_server_ts": 12345678901234576,
        "unsigned": {
            "age": 268
        },
        "event_id": "$skdhGJKhgyr548654YTr765Yiy58TYR",
        "room_id": "!JKHgyHGfytHGFjhgfY:example.com"
    }

    """
    if not rooms:
        logger.info(
            "No rooms are given. This should not happen. "
            "This image is being droppend and NOT sent."
        )
        return
    if not os.path.isfile(image):
        logger.debug(
            f"Image file {image} is not a file. Doesn't exist or "
            "is a directory."
            "This image is being droppend and NOT sent."
        )
        return

    # "bmp", "gif", "jpg", "jpeg", "png", "pbm", "pgm", "ppm", "xbm", "xpm",
    # "tiff", "webp", "svg",

    if not re.match(
        "^.jpg$|^.jpeg$|^.gif$|^.png$|^.svg$",
        os.path.splitext(image)[1].lower(),
    ):
        logger.debug(
            f"Image file {image} is not an image file. Should be "
            ".jpg, .jpeg, .gif, or .png. "
            f"[{os.path.splitext(image)[1].lower()}]"
            "This image is being droppend and NOT sent."
        )
        return

    # 'application/pdf' "image/jpeg"
    mime_type = magic.from_file(image, mime=True)
    if not mime_type.startswith("image/"):
        logger.debug(
            f"Image file {image} does not have an image mime type. "
            "Should be something like image/jpeg. "
            f"Found mime type {mime_type}. "
            "This image is being droppend and NOT sent."
        )
        return

    im = Image.open(image)
    (width, height) = im.size  # im.size returns (width,height) tuple

    # first do an upload of image, see upload() documentation
    # http://matrix-nio.readthedocs.io/en/latest/nio.html#nio.AsyncClient.upload
    # then send URI of upload to room

    file_stat = await aiofiles.os.stat(image)
    async with aiofiles.open(image, "r+b") as f:
        resp, maybe_keys = await client.upload(
            f,
            content_type=mime_type,  # image/jpeg
            filename=os.path.basename(image),
            filesize=file_stat.st_size,
        )
    if isinstance(resp, UploadResponse):
        logger.debug(
            "Image was uploaded successfully to server. "
            f"Response is: {resp}"
        )
    else:
        logger.info(
            f"The program {PROG_WITH_EXT} failed to upload. "
            "Please retry. This could be temporary issue on "
            "your server. "
            "Sorry."
        )
        logger.info(
            f'file="{image}"; mime_type="{mime_type}"; '
            f'filessize="{file_stat.st_size}"'
            f"Failed to upload: {resp}"
        )

    # TODO compute thumbnail, upload thumbnail to Server
    # TODO add thumbnail info to `content`

    content = {
        "body": os.path.basename(image),  # descriptive title
        "info": {
            "size": file_stat.st_size,
            "mimetype": mime_type,
            "thumbnail_info": None,  # TODO
            "w": width,  # width in pixel
            "h": height,  # height in pixel
            "thumbnail_url": None,  # TODO
            # "thumbnail_file": None,
        },
        "msgtype": "m.image",
        "url": resp.content_uri,
        # "file": {
        #    # image/jpeg
        #    "mimetype": mime_type,
        #    # e.g. "mxc://example.com/someStrangeUriKey",
        #    "url": resp.content_uri,
        #    "v": "v2"
    }

    try:
        for room_id in rooms:
            await client.room_send(
                room_id, message_type="m.room.message", content=content
            )
            logger.debug(
                f'This image file was sent: "{image}" to room "{room_id}".'
            )
    except Exception:
        logger.error(f"Image send of file {image} failed. Sorry.")
        logger.debug("Here is the traceback.\n" + traceback.format_exc())


# according to linter: function is too complex, C901
async def send_message(client, rooms, message):  # noqa: C901
    """Process message.

    Format messages according to instructions from command line arguments.
    Then send all messages to all rooms.

    Arguments:
    ---------
    client : Client
    rooms : list
        list of room_id-s
    message : str
        message to send as read from -m, pipe or keyboard
        message is without mime formatting

    """
    if not rooms:
        logger.info(
            "No rooms are given. This should not happen. "
            "This text message is being droppend and NOT sent."
        )
        return
    # remove leading AND trailing newlines to beautify
    message = message.strip("\n")

    if message == "" or message.strip() == "":
        logger.debug(
            "The message is empty. "
            "This message is being droppend and NOT sent."
        )
        return

    if pargs.notice:
        content = {"msgtype": "m.notice"}
    else:
        content = {"msgtype": "m.text"}

    if pargs.code:
        logger.debug('Sending message in format "code".')
        formatted_message = "<pre><code>" + message + "</code></pre>"
        content["format"] = "org.matrix.custom.html"  # add to dict
        content["formatted_body"] = formatted_message
    elif pargs.markdown:
        logger.debug(
            "Converting message from MarkDown into HTML. "
            'Sending message in format "markdown".'
        )
        # e.g. converts from "-abc" to "<ul><li>abc</li></ul>"
        formatted_message = markdown(message)
        content["format"] = "org.matrix.custom.html"  # add to dict
        content["formatted_body"] = formatted_message
    elif pargs.html:
        logger.debug('Sending message in format "html".')
        formatted_message = message  # the same for the time being
        content["format"] = "org.matrix.custom.html"  # add to dict
        content["formatted_body"] = formatted_message
    else:
        logger.debug('Sending message in format "text".')
    content["body"] = message

    try:
        for room_id in rooms:
            if is_room_alias(room_id):
                resp = await client.room_resolve_alias(room_id)
                if isinstance(resp, RoomResolveAliasError):
                    print(f"room_resolve_alias failed with {resp}")
                room_id = resp.room_id
                logger.debug(
                    f'Mapping room alias "{resp.room_alias}" to '
                    f'room id "{resp.room_id}".'
                )
            await client.room_send(
                room_id,
                message_type="m.room.message",
                content=content,
                ignore_unverified_devices=True,
            )
            logger.info(
                f'This message was sent: "{message}" to room "{room_id}".'
            )
    except Exception:
        logger.error("Message send failed. Sorry.")
        logger.debug("Here is the traceback.\n" + traceback.format_exc())


def get_messages_from_pipe() -> list:
    """Read input from pipe if available.

    Return [] if no input available on pipe stdin.
    Return ["some-msg"] if input is availble.
    Might also return [""] of course if "" was in pipe.
    Currently there is at most 1 msg in the returned list.
    """
    messages = []
    stdin_ready = select.select([sys.stdin,], [], [], 0.0)[  # noqa
        0
    ]  # noqa
    if not stdin_ready:
        logger.debug(
            "stdin is not ready. "
            "A pipe could be used, but pipe could be empty, "
            "stdin could also be a keyboard."
        )
    else:
        logger.debug(
            "stdin is ready. Something "
            "is definitely piped into program from stdin."
            "Reading message from stdin pipe."
        )
    if ((not stdin_ready) and (not sys.stdin.isatty())) or stdin_ready:
        if not sys.stdin.isatty():
            logger.debug(
                "Pipe was definitely used, but pipe might be empty. "
                "Trying to read from pipe in any case."
            )
        message = ""
        try:
            for line in sys.stdin:
                message += line
            logger.debug("Using data from stdin pipe as message.")
            messages.append(message)
        except EOFError:  # EOF when reading a line
            logger.debug(
                "Reading from stdin resulted in EOF. This can happen "
                "when a pipe was used, but the pipe is empty. "
                "No message will be generated."
            )
    return messages


def get_messages_from_keyboard() -> list:
    """Read input from keyboard but only if no other messages are available.

    If there is a message provided via --message argument, no message
    will be read from keyboard.
    If there is a message provided via stdin input pipe, no message
    will be read from keyboard.
    In short, we only read from keyboard as last resort, if no messages are
    specified or provided anywhere.

    Return [] if no input available on keyboard.
    Return ["some-msg"] if input is availble on keyboard.
    Might also return [""] of course if "" keyboard entry was empty.
    Currently there is at most 1 msg in the returned list.
    """
    messages = []
    if pargs.message:
        logger.debug(
            "Don't read from keyboard because there are "
            "messages provided in arguments with -m."
        )
        return messages  # return empty list because mesgs in -m
    stdin_ready = select.select([sys.stdin,], [], [], 0.0)[  # noqa
        0
    ]  # noqa
    if not stdin_ready:
        logger.debug(
            "stdin is not ready. "
            "A pipe could be used, but pipe could be empty, "
            "stdin could also be a keyboard."
        )
    else:
        logger.debug(
            "stdin is ready. Something "
            "is definitely piped into program from stdin."
            "Reading message from stdin pipe."
        )
    if (not stdin_ready) and (sys.stdin.isatty()):
        # because sys.stdin.isatty() is true
        logger.debug(
            "No pipe was used, so read input from keyboard. "
            "Reading message from keyboard"
        )
        try:
            message = input("Enter message to send: ")
            logger.debug("Using data from stdin keyboard as message.")
            messages.append(message)
        except EOFError:  # EOF when reading a line
            logger.debug(
                "Reading from stdin resulted in EOF. "
                "Reading from keyboard failed. "
                "No message will be generated."
            )
    return messages


async def send_messages_and_files(client, rooms, messages):
    """Send text messages and files.

    First images, audio, etc, then text messaged.

    Arguments:
    ---------
    client : Client
    rooms : list of room_ids
    messages : list of messages to send

    """
    if pargs.image:
        for image in pargs.image:
            await send_image(client, rooms, image)

    if pargs.audio:
        for audio in pargs.audio:
            # audio file can be sent like other files
            await send_file(client, rooms, audio)

    if pargs.file:
        for file in pargs.file:
            await send_file(client, rooms, file)

    for message in messages:
        await send_message(client, rooms, message)


async def process_arguments_and_input(client, rooms):
    """Process arguments and all input.

    Process all input: text messages, etc.
    Prepare a list of messages from all sources and then send them.

    Arguments:
    ---------
    client : Client
    rooms : list of room_ids

    """
    messages_from_pipe = get_messages_from_pipe()
    messages_from_keyboard = get_messages_from_keyboard()
    if not pargs.message:
        messages_from_commandline = []
    else:
        messages_from_commandline = pargs.message

    logger.debug(f"Messages from pipe:         {messages_from_pipe}")
    logger.debug(f"Messages from keyboard:     {messages_from_keyboard}")
    logger.debug(f"Messages from command-line: {messages_from_commandline}")

    messages_all = (
        messages_from_commandline + messages_from_pipe + messages_from_keyboard
    )  # keyboard at end

    # loop thru all msgs and split them
    if pargs.split:
        # pargs.split can have escape characters, it has to be de-escaped
        decoded_string = bytes(pargs.split, "utf-8").decode("unicode_escape")
        logger.debug(f'String used for splitting is: "{decoded_string}"')
        messages_all_split = []
        for m in messages_all:
            messages_all_split += m.split(decoded_string)
    else:  # not pargs.split
        messages_all_split = messages_all

    await send_messages_and_files(client, rooms, messages_all_split)


async def create_credentials_file(
    credentials_file: str, store_dir: str
) -> None:
    """Log in, create credentials file, log out and exit.

    Arguments:
    ---------
        credentials_file: str : location of credentials file
        store_dir: str : location of persistent storage store directory

    """
    text = f"""
            Credentials file \"{pargs.credentials}\" was not found.
            First time use? Setting up new credentials?
            Asking for homeserver, user, password and
            room id to create a credentials file."""
    print(textwrap.fill(textwrap.dedent(text).strip(), width=79))
    homeserver = "https://matrix.example.org"
    homeserver = input(f"Enter URL of your homeserver: [{homeserver}] ")
    if not (
        homeserver.startswith("https://") or homeserver.startswith("http://")
    ):
        homeserver = "https://" + homeserver
    user_id = "@user:example.org"
    user_id = input(f"Enter your full user ID: [{user_id}] ")
    device_name = PROG_WITHOUT_EXT
    device_name = input(f"Choose a name for this device: [{device_name}] ")
    if device_name == "":
        device_name = PROG_WITHOUT_EXT  # default
    room_id = "!SomeRoomIdString:example.org"
    room_id = input(f"Enter your room ID: [{room_id}] ")

    # Configuration options for the AsyncClient
    client_config = AsyncClientConfig(
        max_limit_exceeded=0,
        max_timeouts=0,
        store_sync_tokens=True,
        encryption_enabled=True,
    )

    if not os.path.exists(store_dir):
        os.makedirs(store_dir)
        logger.info(
            f"The persistent storage directory {store_dir} "
            "was created for you."
        )

    if pargs.proxy:
        logger.info(f"Proxy {pargs.proxy} will be used.")

    try:
        # Initialize the matrix client
        client = AsyncClient(
            homeserver,
            user_id,
            store_path=store_dir,
            config=client_config,
            proxy=pargs.proxy,
        )

        pw = getpass.getpass()
        resp = await client.login(pw, device_name=device_name)
        # check that we logged in succesfully
        if isinstance(resp, LoginResponse):
            # when writing, always write to primary location (e.g. .)
            write_credentials_to_disk(
                homeserver,
                resp.user_id,
                resp.device_id,
                resp.access_token,
                room_id,
                pargs.credentials,
            )
            text = f"""
                Log in using a password was successful.
                Credentials were stored in file \"{pargs.credentials}\".
                Run program \"{PROG_WITH_EXT}\" again to
                login with credentials and to send a message.
                If you plan on having many credential files, consider
                moving them to directory \"{CREDENTIALS_DIR_LASTRESORT}\"."""
            print(textwrap.fill(textwrap.dedent(text).strip(), width=79))
        else:
            logger.info(
                f"The program {PROG_WITH_EXT} failed. "
                "Most likely wrong credentials were entered."
                "Sorry."
            )
            logger.info(
                f'homeserver="{homeserver}"; user="{user_id}"; '
                f'room_id="{room_id}"'
                f"Failed to log in: {resp}"
            )
    finally:
        if client:
            await client.close()
    cleanup()
    sys.exit(1)


def login_using_credentials_file(
    credentials_file: str, store_dir: str
) -> (AsyncClient, dict):
    """Log in by using available credentials file.

    Arguments:
    ---------
        credentials_file: str : location of credentials file
        store_dir: str : location of persistent storage store directory

    Returns
    -------
        AsyncClient : the created NIO client
        dict : the credentials dictionary from the credentials file

    """
    credentials = read_credentials_from_disk(credentials_file)

    # Configuration options for the AsyncClient
    client_config = AsyncClientConfig(
        max_limit_exceeded=0,
        max_timeouts=0,
        store_sync_tokens=True,
        encryption_enabled=True,
    )
    # Initialize the matrix client based on credentials from file
    client = AsyncClient(
        credentials["homeserver"],
        credentials["user_id"],
        device_id=credentials["device_id"],
        store_path=store_dir,
        config=client_config,
        proxy=pargs.proxy,
    )
    client.restore_login(
        user_id=credentials["user_id"],
        device_id=credentials["device_id"],
        access_token=credentials["access_token"],
    )
    # room_id = credentials['room_id']
    logger.debug(
        "Logged in using stored credentials from "
        f'credentials file "{credentials_file}".'
    )
    if pargs.proxy:
        logger.debug(f"Proxy {pargs.proxy} will be used for connectivity.")
    logger.debug(f"Logged_in() = {client.logged_in}")
    return (client, credentials)


async def listen_forever(client: AsyncClient) -> None:
    """Listen forever or until Control-C."""
    # Set up event callbacks
    callbacks = Callbacks(client)
    client.add_event_callback(
        callbacks.message_callback,
        (
            RoomMessage,
            RedactedEvent,
            RedactionEvent,
        ),
    )
    print(
        "This program is ready and listening for its Matrix messages."
        " To stop program type Control-C on keyboard or send signal"
        f" to process {os.getpid()}. PID can also be found in "
        f'file "{PID_FILE_DEFAULT}".',
        flush=True,
    )
    # the sync_loop will be terminated by user hitting Control-C to stop
    await client.sync_forever(timeout=30000, full_state=True)


async def listen_once(client: AsyncClient) -> None:
    """Listen once, then quit.

    Get all the messages that are currently queued up and waiting.
    Print them. Then leave.
    """
    # Set up event callbacks
    callbacks = Callbacks(client)
    client.add_event_callback(callbacks.message_callback, (RoomMessage,))
    # We want to get out quickly, so we reduced timeout to 10 sec.
    # We want to get messages and quit, so we call sync() instead of
    # sync_forever().
    resp = await client.sync(timeout=10000, full_state=False)
    if isinstance(resp, SyncResponse):
        logger.debug(f"Sync successful. Response is: {resp}")
    else:
        logger.info(f"Sync failed. Error is: {resp}")
    # sync() forces the message_callback() to fire
    # for each new message presented in the sync().


async def listen_once_alternative(client: AsyncClient) -> None:
    """Listen once, then quit.

    Get all the messages that are currently queued up and waiting.
    Print them. Then leave.

    Alternative implementation of listen_once().
    We don't use any callbacks and we just call sync() and get all
    of the MessageEvents from the timeline of the reply provided by
    sync(). This is more work than listen_once() but it is interesting
    case study to understand sync().

    sync() response includes the member `rooms` (of class nio.responses.Rooms).
    Rooms have 3 top dicts.
    Rooms(invite={}, join={...}, leave={})
    join has a dict entry of type RoomInfo for
    each room. And the RoomInfo has a timeline (of class TimeLine) with
    all currently queued up events. So, timeline has a list of events
    such as RoomMessageText, RoomMessageNotice, etc. One can go through
    these timeline event lists and process each queued up message.

    This is an example Rooms object that is part of a sync() response.
    This example gives the details on 2 currently queued up messages.

    Rooms(
    invite={},
    join={'!SomeRoomId:example.org':
        RoomInfo(
        timeline=Timeline(
            events=[
                RoomMessageText(source={
                    'room_id': '!SomeRoomId:example.org',
                    'type': 'm.room.message',
                    'content': {'msgtype': 'm.text', 'body': 'Hi there'},
                    'event_id': 'SomeEventId1',
                    'sender': '@user1:example.org',
                    'origin_server_ts': 1591234896712},
                event_id='SomeEventId1',
                sender='@user1:example.org',
                server_timestamp=1591234896712,
                decrypted=True, verified=False,
                sender_key='SomeSenderKey1',
                session_id='SomeSessionId1',
                transaction_id=None,
                body='Hi there',
                formatted_body=None,
                format=None),

                RoomMessageNotice(source={'content': {'msgtype': 'm.notice',
                    'body': 'Hello',
                    'format': 'org.matrix.custom.html',
                    'formatted_body': '<p>Hello</p>'
                    },
                    'type': 'm.room.message',
                    'room_id': '!SomeRoomId:example.org',
                    'event_id': 'SomeEventId2',
                    'sender': '@user2:example.org',
                    'origin_server_ts': 1591234897079},
                event_id='SomeEventId2',
                sender='@user2:example.org',
                server_timestamp=1591234897079, decrypted=True, verified=False,
                sender_key='SomeSenderKey2',
                session_id='SomeSessionId2',
                transaction_id=None,
                body='<p>Hello</p>',
                format='org.matrix.custom.html')
            ],
            limited=False,
            prev_batch='s16650_264746_732_1234_8050_2_8260_439_1'),
        state=[],
        ephemeral=[TypingNoticeEvent(users=[]), ReceiptEvent(...)],
        account_data=[],
        summary=RoomSummary(...),
        unread_notifications=UnreadNotifications(...)
        )
    },
    leave={})

    """
    resp_s = await client.sync(timeout=10000, full_state=False)
    # this prints a summary of all new messages currently waiting in the queue
    logger.debug(f"sync response = {type(resp_s)} :: {resp_s}")
    logger.debug(f"sync next_batch = (str) {resp_s.next_batch}")
    logger.debug(f"sync rooms = (nio.responses.Rooms) {resp_s.rooms}")
    # Set up event callbacks
    callbacks = Callbacks(client)
    # Note: we are NOT registering a callback funtion!
    # Loop through the join dictionary
    for room_id, room_info in resp_s.rooms.join.items():
        event_list = room_info.timeline.events
        for event in event_list:
            logger.debug(f"sending event to callback = {event}.")
            # because of full_state=False in sync() the
            # rooms object is not fully populated and missing the
            # room names.
            room = client.rooms[room_id]
            await callbacks.message_callback(room, event)
        if event_list:  # list not empty
            last_event = event_list[-1]
            resp = await client.room_read_markers(
                room_id=room_id,
                fully_read_event=last_event.event_id,
                read_event=last_event.event_id,
            )
            if isinstance(resp, RoomReadMarkersError):
                logger.debug(
                    f"room_read_markers failed with response = {resp}."
                )


# according to pylama: function too complex: C901 # noqa: C901
async def listen_tail(  # noqa: C901
    client: AsyncClient, credentials: dict
) -> None:  # noqa: C901
    """Get the last N messages, then quit.

    Arguments:
    ---------
        client: AsyncClient : the created NIO client
        credentials: dict : credentials dictionary from the credentials file

    Get the last N messages. Some might be old, i.e. already
    read before, some might be new, i.e. never read before.
    Print them. Then leave.

    If there are less than N messages, get up to N.

    The function room_messages() is used to get
    the last N messages.

    """
    # we call sync() to get the next_batch marker
    # we set full_state=True to get all room_ids
    try:
        resp_s = await client.sync(timeout=10000, full_state=True)
    except ClientConnectorError:
        logger.info("sync() failed. Do you have connectivity to internet?")
        logger.debug(traceback.format_exc())
        return
    except Exception:
        logger.info("sync() failed.")
        logger.debug(traceback.format_exc())
        return
    if isinstance(resp_s, SyncError):
        logger.debug(f"sync failed with resp = {resp_s}")
        return
    # this prints a summary of all new messages currently waiting in the queue
    logger.debug(f"sync response = {type(resp_s)} :: {resp_s}")
    logger.debug(f"client.next_batch after = (str) {client.next_batch}")
    logger.debug(f"sync next_batch = (str) {resp_s.next_batch}")
    logger.debug(f"sync rooms = (nio.responses.Rooms) {resp_s.rooms}")
    logger.debug(f"client.rooms = {client.rooms}")
    if not resp_s.rooms.join:  # no Rooms!
        logger.debug(f"sync returned no rooms = {resp_s.rooms.join}")
        return

    # Set up event callbacks
    callbacks = Callbacks(client)
    # Note: we are NOT registering a callback funtion!

    # room_id = list(resp_s.rooms.join.keys())[0]  # first room_id from dict
    # alternative way of getting room_id, client.rooms is also a dict
    # room_id = list(client.rooms.keys())[0]  # first room_id from dict

    # get rooms as specified by the user thru args or credential file
    rooms = determine_rooms(credentials["room_id"])
    logger.debug(f"Rooms are: {rooms}")

    limit = pargs.tail
    # To loop over all rooms, one can loop through the join dictionary. i.e.
    # for room_id, room_info in resp_s.rooms.join.items():  # loop all rooms
    for room_id in rooms:  # loop only over user specified rooms
        resp = await client.room_messages(
            room_id, start=resp_s.next_batch, limit=limit
        )
        if isinstance(resp, RoomMessagesError):
            logger.debug("room_messages failed with resp = {resp}")
            continue  # skip this room
        logger.debug(f"room_messages response = {type(resp)} :: {resp}.")
        logger.debug(f"room_messages room_id = {resp.room_id}.")
        logger.debug(f"room_messages start = (str) {resp.start}.")
        logger.debug(f"room_messages end = (str) :: {resp.end}.")
        logger.debug(f"room_messages chunk = (list) :: {resp.chunk}.")
        # chunk is just a list of RoomMessage events like this example:
        # chunk=[RoomMessageText(...)]

        for event in resp.chunk:
            logger.debug(f"sending event to callback = {event}.")
            if client.rooms and client.rooms[room_id]:
                room = client.rooms[room_id]
            else:
                room = MatrixRoom(room_id, None, True)  # dummy_room
            await callbacks.message_callback(room, event)
        if resp.chunk:  # list not empty
            # order is reversed, first element is timewise the newest
            first_event = resp.chunk[1]
            resp = await client.room_read_markers(
                room_id=room_id,
                fully_read_event=first_event.event_id,
                read_event=first_event.event_id,
            )
            if isinstance(resp, RoomReadMarkersError):
                logger.debug(
                    f"room_read_markers failed with response = {resp}."
                )


async def read_all_events_in_direction(
    client: AsyncClient,
    room_id: str,
    start_token: str,
    direction: MessageDirection = MessageDirection.back,
) -> list:
    """Read all events from a given room in certain direction.

    Arguments:
    ---------
        client: AsyncClient : The created NIO client
        room_id: str : The room id of the room for which we
            would like to fetch the messages.
        start_token: str :  The token to start returning events from.
            This token can be obtained from a prev_batch token returned for
            each room by the sync() API, or from a start or end token returned
            by a previous request to room_messages().
        direction: MessageDirection (optional): The direction to return
            events from. Defaults to MessageDirection.back.

    Returns
    -------
        list: list of RoomMessage events, could be empty

    Read all messages of a room beginning from the past_token
    to oldest or newest message (depending on the direction).

    """
    all_events = []
    current_start_token = start_token
    while True:
        resp = await client.room_messages(
            room_id, current_start_token, limit=500, direction=direction
        )
        if isinstance(resp, RoomMessagesError):
            logger.debug("room_messages failed with resp = {resp}")
            break  # skip to end of function
        logger.debug(f"Received {len(resp.chunk)} events.")
        logger.debug(f"room_messages response = {type(resp)} :: {resp}.")
        logger.debug(f"room_messages room_id = {resp.room_id}.")
        logger.debug(f"room_messages start = (str) {resp.start}.")
        logger.debug(f"room_messages end = (str) :: {resp.end}.")
        logger.debug(f"room_messages chunk = (list) :: {resp.chunk}.")
        # resp.chunk is just a list of RoomMessage events like this example:
        # chunk=[RoomMessageText(...)]
        current_start_token = resp.end
        if len(resp.chunk) == 0:
            break
        all_events = all_events + resp.chunk
    return all_events


# according to pylama: function too complex: C901 # noqa: C901
async def listen_all(  # noqa: C901
    client: AsyncClient, credentials: dict
) -> None:  # noqa: C901
    """Get all messages, then quit.

    Arguments:
    ---------
        client: AsyncClient : the created NIO client
        credentials: dict : credentials dictionary from the credentials file

    Get all messages. Some might be old, i.e. already
    read before, some might be new, i.e. never read before.
    Print them. Then leave.

    The function room_messages() is used to get all messages.

    """
    # we call sync() to get the next_batch marker
    # we set full_state=True to get all room_ids
    try:
        resp_s = await client.sync(timeout=10000, full_state=True)
    except ClientConnectorError:
        logger.info("sync() failed. Do you have connectivity to internet?")
        logger.debug(traceback.format_exc())
        return
    except Exception:
        logger.info("sync() failed.")
        logger.debug(traceback.format_exc())
        return
    if isinstance(resp_s, SyncError):
        logger.debug(f"sync failed with resp = {resp_s}")
        return
    # this prints a summary of all new messages currently waiting in the queue
    logger.debug(f"sync response = {type(resp_s)} :: {resp_s}")
    logger.debug(f"client.next_batch after = (str) {client.next_batch}")
    logger.debug(f"sync next_batch = (str) {resp_s.next_batch}")
    logger.debug(f"sync rooms = (nio.responses.Rooms) {resp_s.rooms}")
    logger.debug(f"client.rooms = {client.rooms}")
    if not resp_s.rooms.join:  # no Rooms!
        logger.debug(f"sync returned no rooms = {resp_s.rooms.join}")
        return

    # Set up event callbacks
    callbacks = Callbacks(client)
    # Note: we are NOT registering a callback funtion!

    # room_id = list(resp_s.rooms.join.keys())[0]  # first room_id from dict
    # alternative way of getting room_id, client.rooms is also a dict
    # room_id = list(client.rooms.keys())[0]  # first room_id from dict

    # get rooms as specified by the user thru args or credential file
    rooms = determine_rooms(credentials["room_id"])
    logger.debug(f"Rooms are: {rooms}")

    # To loop over all rooms, one can loop through the join dictionary. i.e.
    # for room_id, room_info in resp_s.rooms.join.items():  # loop all rooms
    for room_id in rooms:  # loop only over user specified rooms
        prev_batch = resp_s.rooms.join[room_id].timeline.prev_batch
        back_events = await read_all_events_in_direction(
            client, room_id, prev_batch, MessageDirection.back
        )
        front_events = await read_all_events_in_direction(
            client, room_id, prev_batch, MessageDirection.front
        )

        # We have to reverse the first list since we are going backwards (but
        # we want to have a chronological order)
        all_events = back_events[::-1] + front_events

        for event in all_events:
            logger.debug(f"sending event to callback = {event}.")
            if client.rooms and client.rooms[room_id]:
                room = client.rooms[room_id]
            else:
                room = MatrixRoom(room_id, None, True)  # dummy_room
            await callbacks.message_callback(room, event)
        if all_events:  # list not empty
            last_event = all_events[-1]
            resp = await client.room_read_markers(
                room_id=room_id,
                fully_read_event=last_event.event_id,
                read_event=last_event.event_id,
            )
            if isinstance(resp, RoomReadMarkersError):
                logger.debug(
                    f"room_read_markers failed with response = {resp}."
                )


async def main_listen() -> None:
    """Use credentials to log in and listen."""
    credentials_file = determine_credentials_file()
    store_dir = determine_store_dir()
    if not os.path.isfile(credentials_file):
        logger.debug(
            "Credentials file must be created first before one can verify."
        )
        cleanup()
        sys.exit(1)
    logger.debug("Credentials file does exist.")
    try:
        client, credentials = login_using_credentials_file(
            credentials_file, store_dir
        )
        # Sync encryption keys with the server
        # Required for participating in encrypted rooms
        if client.should_upload_keys:
            await client.keys_upload()
        logger.debug(f"Listening type: {pargs.listen}")
        if pargs.listen == FOREVER:
            await listen_forever(client)
        elif pargs.listen == ONCE:
            await listen_once(client)
            # could use 'await listen_once_alternative(client)'
            # as an alternative implementation
        elif pargs.listen == TAIL:
            await listen_tail(client, credentials)
        elif pargs.listen == ALL:
            await listen_all(client, credentials)
        else:
            logger.error(
                f'Unrecognized listening type "{pargs.listen}". '
                "Closing client."
            )
    finally:
        if client:
            await client.close()


async def main_rename_device() -> None:
    """Use credentials to log in and rename the device name of itself."""
    credentials_file = determine_credentials_file()
    store_dir = determine_store_dir()
    if not os.path.isfile(credentials_file):
        logger.debug(
            "Credentials file must be created first before one can verify."
        )
        cleanup()
        sys.exit(1)
    logger.debug("Credentials file does exist.")
    try:
        client, credentials = login_using_credentials_file(
            credentials_file, store_dir
        )
        content = {"display_name": pargs.rename_device}
        resp = await client.update_device(credentials["device_id"], content)
        if isinstance(resp, UpdateDeviceError):
            logger.error(f"update_device failed with {resp}")
        else:
            logger.debug(f"update_device successful with {resp}")
    finally:
        if client:
            await client.close()


# according to pylama: function too complex: C901 # noqa: C901


async def main_room_actions() -> None:  # noqa: C901
    """Perform various room actions such as create, join, etc."""
    credentials_file = determine_credentials_file()
    store_dir = determine_store_dir()
    if not os.path.isfile(credentials_file):
        logger.debug(
            "Credentials file must be created first before one can verify."
        )
        cleanup()
        sys.exit(1)
    logger.debug("Credentials file does exist.")
    try:
        client, credentials = login_using_credentials_file(
            credentials_file, store_dir
        )
        if pargs.room_create:
            await create_rooms(
                client, pargs.room_create, pargs.name, pargs.topic
            )
        if pargs.room_join:
            await join_rooms(client, pargs.room_join)
        if pargs.room_leave:
            await leave_rooms(client, pargs.room_leave)
        if pargs.room_forget:
            await forget_rooms(client, pargs.room_forget)
        if pargs.room_invite and pargs.user:
            await invite_to_rooms(client, pargs.room_invite, pargs.user)
        if pargs.room_ban and pargs.user:
            await ban_from_rooms(client, pargs.room_ban, pargs.user)
        if pargs.room_unban and pargs.user:
            await unban_from_rooms(client, pargs.room_unban, pargs.user)
        if pargs.room_kick and pargs.user:
            await kick_from_rooms(client, pargs.room_kick, pargs.user)
        if (
            pargs.room_invite
            or pargs.room_ban
            or pargs.room_unban
            or pargs.room_kick
        ) and not pargs.user:
            logger.warning(
                "No room action(s) were performed because no users "
                "were specified. Use --user option to specify users."
            )
        logger.debug(
            "Room action(s) were performed or attempted. "
            "We close the client and quit"
        )
    finally:
        if client:
            await client.close()


async def main_verify() -> None:
    """Use credentials to log in and verify."""
    credentials_file = determine_credentials_file()
    store_dir = determine_store_dir()
    if not os.path.isfile(credentials_file):
        logger.debug(
            "Credentials file must be created first before one can verify."
        )
        cleanup()
        sys.exit(1)
    logger.debug("Credentials file does exist.")
    try:
        client, credentials = login_using_credentials_file(
            credentials_file, store_dir
        )
        # Set up event callbacks
        callbacks = Callbacks(client)
        client.add_to_device_callback(
            callbacks.to_device_callback, (KeyVerificationEvent,)
        )
        # Sync encryption keys with the server
        # Required for participating in encrypted rooms
        if client.should_upload_keys:
            await client.keys_upload()
        print(
            "This program is ready and waiting for the other party to "
            "initiate an emoji verification with us by selecting "
            '"Verify by Emoji"'
            "in their Matrix client."
        )
        # the sync_loop will be terminated by user hitting Control-C to stop
        await client.sync_forever(timeout=30000, full_state=True)
    finally:
        if client:
            await client.close()


async def main_send() -> None:
    """Create credentials, or use credentials to log in and send messages."""
    credentials_file = determine_credentials_file()
    store_dir = determine_store_dir()
    if not os.path.isfile(credentials_file):
        logger.debug("Credentials file does not exist.")
        await create_credentials_file(credentials_file, store_dir)
    logger.debug("Credentials file does exist.")
    try:
        client, credentials = login_using_credentials_file(
            credentials_file, store_dir
        )
        # a few more steps to prepare for sending messages
        rooms = determine_rooms(credentials["room_id"])
        logger.debug(f"Rooms are: {rooms}")
        # Sync encryption keys with the server
        # Required for participating in encrypted rooms
        if client.should_upload_keys:
            await client.keys_upload()
        # must sync first to get room ids for encrypted rooms
        # since we only send a msg and then stop we can use sync() instead of
        # sync_forever() (await client.sync_forever(30000, full_state=True))
        await client.sync(timeout=30000, full_state=True)
        # Now we can send messages as the user
        await process_arguments_and_input(client, rooms)
        logger.debug("Messages were sent. We close the client and quit")
    finally:
        if client:
            await client.close()


def is_download_media_dir_valid() -> bool:
    """Check if media download directory is correct."""
    if not pargs.download_media:
        return True  # "": that means no download of media, valid value
    # normailzed for humans
    dl = os.path.normpath(pargs.download_media)
    pargs.download_media = dl
    if os.path.isfile(dl):
        logger.error(
            f'"{dl}" cannot be used as media directory, because '
            f'"{dl}" is a file. Specify a different directory for downloading '
            "media."
        )
        return False
    if os.path.isdir(dl):
        if os.access(dl, os.W_OK):  # Check for write access
            return True
        else:
            logger.error(
                "Found an existing media download directory "
                f'"{dl}". But this directory is lacking write '
                "permissions. Add write permissions to it."
            )
            return False
    else:
        # not a file, not a directory, create directory
        mode = 0o777
        try:
            os.mkdir(dl, mode)
        except OSError as exc:
            logger.error(
                "Could not create media download directory "
                f"{dl} for you. ({exc})"
            )
            return False
        logger.debug(f'Created media download directory "{dl}" for you.')
        return True


def version() -> None:
    """Print version info."""
    version_info = (
        "\n"
        f"  _|      _|      _|_|_|    _|       {PROG_WITHOUT_EXT}\n"
        "  _|_|  _|_|    _|            _|     a Matrix CLI client\n"
        "  _|  _|  _|    _|              _|   \n"
        f"  _|      _|    _|            _|     version {VERSION}\n"
        "  _|      _|      _|_|_|    _|       enjoy and submit PRs\n"
        "\n"
    )
    print(version_info)
    logger.debug(version_info)


def initial_check_of_log_args() -> str:
    """Check logging related arguments."""
    if not pargs.log_level:
        return
    t = ""
    for i in range(len(pargs.log_level)):
        up = pargs.log_level[i].upper()
        pargs.log_level[i] = up
        if up not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
            t = (
                '--log-level only allows values "DEBUG", "INFO", "WARNING", '
                '"ERROR", or "CRITICAL". --log-level argument incorrect. '
                f"({up})"
            )
    if t == "":
        return
    else:
        logger.error(t)
        sys.exit(1)


# according to pylama: function too complex: C901 # noqa: C901
def initial_check_of_args() -> None:  # noqa: C901
    """Check arguments."""
    # First, the adjustments
    if not pargs.encrypted:
        pargs.encrypted = True  # force it on
        logger.debug("Encryption is always enabled. It cannot be turned off.")
    if not pargs.encrypted:  # just in case we ever go back disabling e2e
        pargs.store = None
    if pargs.listen:
        pargs.listen = pargs.listen.lower()
    if pargs.listen == NEVER and pargs.tail != 0:
        pargs.listen = TAIL  # --tail turns on --listen TAIL
        logger.debug('--listen set to "tail" because "--tail" is used.')
    if (
        pargs.room_create
        or pargs.room_join
        or pargs.room_leave
        or pargs.room_forget
        or pargs.room_invite
        or pargs.room_ban
        or pargs.room_unban
        or pargs.room_kick
    ):
        room_action = True
    else:
        room_action = False
    if pargs.proxy == "":
        pargs.proxy = None

    # Secondly, the checks
    if pargs.config:
        t = (
            "This feature is not implemented yet. "
            "Please help me implement it. If you feel motivated "
            "please write code and submit a Pull Request. "
            "Your contribution is appreciated. Thnx!"
        )
    elif (
        pargs.listen == FOREVER or pargs.listen == ONCE or pargs.listen == ALL
    ) and pargs.tail != 0:
        t = (
            "Don't use --listen forever, --listen once or --listen all "
            "together with --tail. It's one or the other."
        )
    # this is set by default anyway, just defensive programming
    elif pargs.encrypted and ((not pargs.store) or (pargs.store == "")):
        t = (
            "If --encrypt is used --store must be set too. "
            "Specify --store and run program again."
        )
    elif pargs.verify and (pargs.verify.lower() != EMOJI):
        t = f'For --verify currently only "{EMOJI}" is allowed ' "as keyword."
    elif pargs.verify and (
        pargs.message
        or pargs.image
        or pargs.audio
        or pargs.file
        or pargs.room
        or room_action
        or pargs.listen != NEVER
        or pargs.rename_device
    ):
        t = (
            "If --verify is specified, only verify can be done. "
            "No messages, images, or files can be sent."
            "No listening or tailing allowed. No renaming. "
            "No actions on rooms."
        )
    elif pargs.rename_device and (pargs.rename_device == ""):
        t = "Don't use an empty name for --rename_device."
    elif pargs.rename_device and (
        pargs.message
        or pargs.image
        or pargs.audio
        or pargs.file
        or pargs.room
        or room_action
        or pargs.listen != NEVER
        or pargs.verify
    ):
        t = (
            "If --rename_device is specified, only rename can be done. "
            "No messages, images, or files can be sent."
            "No listening or tailing allowed. No verification. "
            "No actions on rooms."
        )
    elif pargs.listen != NEVER and (
        pargs.message
        or pargs.image
        or pargs.audio
        or pargs.file
        or room_action
    ):
        t = (
            "If --listen is specified, only listening can be done. "
            "No messages, images, or files can be sent."
            "No room actions allowed."
        )
    elif (pargs.message or pargs.image or pargs.audio or pargs.file) and (
        pargs.listen != NEVER or room_action
    ):
        t = (
            "If sending (-m, -i, -a, -f) is specified, only sending can be "
            "done. No listening allowed. "
            "No room actions allowed."
        )
    elif (pargs.user) and not room_action:
        t = (
            "If --user is specified, only room action can be "
            "done. "
            "Specify a room option like --room-create or remove --user."
        )
    elif (pargs.listen == ONCE or pargs.listen == FOREVER) and pargs.room:
        t = (
            "If --listen once or --listen forever are specified, "
            "--room must not be specified because "
            "these options listen in ALL rooms."
        )
    elif (
        pargs.listen != NEVER
        and pargs.listen != FOREVER
        and pargs.listen != ONCE
        and pargs.listen != TAIL
        and pargs.listen != ALL
    ):
        t = (
            "If --listen is specified, only these choices are "
            f"possible: {ONCE}, {NEVER}, {FOREVER}, {TAIL} or {ALL}. "
            f'Found "{pargs.listen}".'
        )
    elif pargs.listen == NEVER and pargs.listen_self:
        t = (
            "If neither --listen nor --tail are used, "
            "then --listen-self must not be used "
            "either. Specify --listen or --tail "
            "and run program again."
        )
    elif pargs.listen == NEVER and (pargs.download_media != ""):
        t = (
            "If neither --listen nor --tail are used, "
            "then --download-media must not be used "
            "either. Specify --listen or --tail "
            f"and run program again. ({pargs.download_media})"
        )
    elif pargs.proxy and not (
        pargs.proxy.startswith("http://")
        or pargs.proxy.startswith("socks4://")
        or pargs.proxy.startswith("socks5://")
    ):
        t = (
            "Proxy is not correct. Proxy should start with "
            '"http://", "socks4://" or "socks5://". '
            f' Your proxy is set to "{pargs.proxy}".'
        )
    else:
        logger.debug("All arguments are valid. All checks passed.")
        return
    logger.error(t)
    sys.exit(1)


# according to linter: function is too complex, C901
if __name__ == "__main__":  # noqa: C901 # ignore mccabe if-too-complex
    logging.basicConfig(  # initialize root logger, a must
        format="{asctime}: {levelname:>8}: {name:>16}: {message}", style="{"
    )
    # set log level on root
    if "DEBUG" in os.environ:
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)

    # Construct the argument parser
    ap = argparse.ArgumentParser(
        description=(
            f"Welcome to {PROG_WITHOUT_EXT}, a Matrix CLI client. ─── "
            "On first run this program will configure itself. "
            "On further runs this program implements a simple Matrix CLI "
            "client that can send messages, listen to messages, verify "
            "devices, etc. It can send one or multiple message to one or "
            "multiple Matrix rooms. The text messages can be of various "
            'formats such as "text", "html", "markdown" or "code". '
            "Images, audio or arbitrary files can be sent as well. "
            "For receiving there are three main options: listen forever, "
            "listen once and quit, and get the last N messages "
            "and quit. Emoji verification is built-in which can be used "
            "to verify devices. End-to-end encryption is enabled by default "
            "and cannot be turned off.  ─── "
            "See dependencies in source code or in README.md on Github. "
            "For even more explications and examples also read the "
            "documentation provided in the top portion of the source code  "
            "and in the GithubREADME.md file."
        ),
        epilog="You are running "
        f"version {VERSION}. Enjoy, star on Github and contribute by "
        "submitting a Pull Request. ",
    )
    # Add the arguments to the parser
    ap.add_argument(
        "-d",
        "--debug",
        action="count",
        default=0,
        help="Print debug information. If used once, only the log level of "
        f"{PROG_WITHOUT_EXT} is set to DEBUG. "
        'If used twice ("-d -d" or "-dd") then '
        f"log levels of both {PROG_WITHOUT_EXT} and underlying modules are "
        'set to DEBUG. "-d" is a shortcut for "--log-level DEBUG". '
        'See also --log-level. "-d" takes precedence over "--log-level". ',
    )
    ap.add_argument(
        "--log-level",
        required=False,
        action="extend",
        nargs="+",
        type=str,
        help="Set the log level(s). Possible values are "
        '"DEBUG", "INFO", "WARNING", "ERROR", and "CRITICAL". '
        "If --log_level is used with one level argument, only the log level "
        f"of {PROG_WITHOUT_EXT} is set to the specified value. "
        "If --log_level is used with two level argument "
        '(e.g. "--log-level WARNING ERROR") then '
        f"log levels of both {PROG_WITHOUT_EXT} and underlying modules are "
        "set to the specified values. "
        "See also --debug.",
    )
    ap.add_argument(
        "-c",
        "--credentials",
        required=False,
        type=str,
        default=CREDENTIALS_FILE_DEFAULT,
        help="On first run, information about homeserver, "
        "user, room id, etc. will be written to a credentials "
        "file. By default, this file "
        f'is "{CREDENTIALS_FILE_DEFAULT}". '
        "On further runs the credentials file is read to "
        "permit logging into the correct Matrix account "
        "and sending messages to the preconfigured room. "
        "If this option is provided, the provided file name "
        "will be used as credentials file instead of the "
        "default one. ",
    )
    ap.add_argument(
        "-r",
        "--room",
        required=False,
        action="extend",
        nargs="+",
        type=str,
        help="Send to this room or these rooms. None, one or "
        "multiple rooms can be specified. "
        "The default room is provided "
        "in credentials file. If a room (or multiple ones) "
        "is (or are) provided in the arguments, then it "
        "(or they) will be used "
        "instead of the one from the credentials file. "
        "The user must have access to the specified room "
        "in order to send messages there. Messages cannot "
        "be sent to arbitrary rooms. When specifying the "
        "room id some shells require the exclamation mark "
        "to be escaped with a backslash.",
    )
    ap.add_argument(
        "--room-create",
        required=False,
        action="extend",
        nargs="+",
        type=str,
        help="Create this room or these rooms. One or multiple "
        "room aliases can be specified. The room (or multiple "
        "ones) provided in the arguments will be created. "
        "The user must be permitted to create rooms."
        "Combine --room-create with --name and --topic to add "
        "names and topics to the room(s) to be created.",
    )
    ap.add_argument(
        "--room-join",
        required=False,
        action="extend",
        nargs="+",
        type=str,
        help="Join this room or these rooms. One or multiple "
        "room aliases can be specified. The room (or multiple "
        "ones) provided in the arguments will be joined. "
        "The user must have permissions to join these rooms.",
    )
    ap.add_argument(
        "--room-leave",
        required=False,
        action="extend",
        nargs="+",
        type=str,
        help="Leave this room or these rooms. One or multiple "
        "room aliases can be specified. The room (or multiple "
        "ones) provided in the arguments will be left. ",
    )
    ap.add_argument(
        "--room-forget",
        required=False,
        action="extend",
        nargs="+",
        type=str,
        help="After leaving a room you should (most likely) forget the room. "
        "Forgetting a room removes the users' room history. "
        "One or multiple "
        "room aliases can be specified. The room (or multiple "
        "ones) provided in the arguments will be forgotten. "
        "If all users forget a room, the room can eventually be "
        "deleted on the server.",
    )
    ap.add_argument(
        "--room-invite",
        required=False,
        action="extend",
        nargs="+",
        type=str,
        help="Invite one ore more users to join one or more rooms. "
        "Specify the user(s) as arguments to --user. "
        "Specify the rooms as arguments to this option, i.e. "
        "as arguments to --room-invite. "
        "The user must have permissions to invite users.",
    )
    ap.add_argument(
        "--room-ban",
        required=False,
        action="extend",
        nargs="+",
        type=str,
        help="Ban one ore more users from one or more rooms. "
        "Specify the user(s) as arguments to --user. "
        "Specify the rooms as arguments to this option, i.e. "
        "as arguments to --room-ban. "
        "The user must have permissions to ban users.",
    )
    ap.add_argument(
        "--room-unban",
        required=False,
        action="extend",
        nargs="+",
        type=str,
        help="Unban one ore more users from one or more rooms. "
        "Specify the user(s) as arguments to --user. "
        "Specify the rooms as arguments to this option, i.e. "
        "as arguments to --room-unban. "
        "The user must have permissions to unban users.",
    )
    ap.add_argument(
        "--room-kick",
        required=False,
        action="extend",
        nargs="+",
        type=str,
        help="Kick one ore more users from one or more rooms. "
        "Specify the user(s) as arguments to --user. "
        "Specify the rooms as arguments to this option, i.e. "
        "as arguments to --room-kick. "
        "The user must have permissions to kick users.",
    )
    ap.add_argument(
        "--user",
        required=False,
        action="extend",
        nargs="+",
        type=str,
        help="Specify one or multiple users. This option is only meaningful "
        "in combination with options like --room-invite, --room-ban, "
        "--room-unban, --room-kick. This option --user specifies the users "
        "to be used with these other room commands (like invite, ban, etc.)",
    )
    ap.add_argument(
        "--name",
        required=False,
        action="extend",
        nargs="+",
        type=str,
        help="Specify one or multiple names. This option is only meaningful "
        "in combination with option --room-create. "
        "This option --name specifies the names "
        "to be used with the command --room-create.",
    )
    ap.add_argument(
        "--topic",
        required=False,
        action="extend",
        nargs="+",
        type=str,
        help="Specify one or multiple topics. This option is only meaningful "
        "in combination with option --room-create. "
        "This option --topic specifies the topics "
        "to be used with the command --room-create.",
    )
    # allow multiple messages , e.g. -m "m1" "m2" or -m "m1" -m "m2"
    # message is going to be a list of strings
    # e.g. message=[ 'm1', 'm2' ]
    ap.add_argument(
        "-m",
        "--message",
        required=False,
        action="extend",
        nargs="+",
        type=str,
        help="Send this message. If not specified, and no "
        "input piped in from stdin, then message "
        "will be read from stdin, i.e. keyboard. "
        "This option can be used multiple time to send "
        "multiple messages. If there is data is piped "
        "into this program, then first data from the "
        "pipe is published, then messages from this "
        "option are published.",
    )
    # allow multiple messages , e.g. -i "i1.jpg" "i2.gif"
    # or -m "i1.png" -i "i2.jpeg"
    # image is going to be a list of strings
    # e.g. image=[ 'i1.jpg', 'i2.png' ]
    ap.add_argument(
        "-i",
        "--image",
        required=False,
        action="extend",
        nargs="+",
        type=str,
        help="Send this image. "
        "This option can be used multiple time to send "
        "multiple images. First images are send, "
        "then text messages are send.",
    )
    # allow multiple audio files , e.g. -i "a1.mp3" "a2.wav"
    # or -m "a1.mp3" -i "a2.m4a"
    # audio is going to be a list of strings
    # e.g. audio=[ 'a1.mp3', 'a2.m4a' ]
    ap.add_argument(
        "-a",
        "--audio",
        required=False,
        action="extend",
        nargs="+",
        type=str,
        help="Send this audio file. "
        "This option can be used multiple time to send "
        "multiple audio files. First audios are send, "
        "then text messages are send.",
    )
    # allow multiple files , e.g. -i "a1.pdf" "a2.doc"
    # or -m "a1.pdf" -i "a2.doc"
    # file is going to be a list of strings
    # e.g. file=[ 'a1.pdf', 'a2.doc' ]
    ap.add_argument(
        "-f",
        "--file",
        required=False,
        action="extend",
        nargs="+",
        type=str,
        help="Send this file (e.g. PDF, DOC, MP4). "
        "This option can be used multiple time to send "
        "multiple files. First files are send, "
        "then text messages are send.",
    )
    # -h already used for --help, -w for "web"
    ap.add_argument(
        "-w",
        "--html",
        required=False,
        action="store_true",
        help="Send message as format "
        '"HTML". If not specified, message will be sent '
        'as format "TEXT". E.g. that allows some text '
        "to be bold, etc. Only a subset of HTML tags are "
        "accepted by Matrix.",
    )
    # -m already used for --message, -z because there were no letters left
    ap.add_argument(
        "-z",
        "--markdown",
        required=False,
        action="store_true",
        help="Send message as format "
        '"MARKDOWN". If not specified, message will be sent '
        'as format "TEXT". E.g. that allows sending of text '
        "formated in MarkDown language.",
    )
    #  -c is already used for --credentials, -k as it sounds like c
    ap.add_argument(
        "-k",
        "--code",
        required=False,
        action="store_true",
        help="Send message as format "
        '"CODE". If not specified, message will be sent '
        'as format "TEXT". If both --html and --code are '
        "specified then --code takes priority. This is "
        "useful for sending ASCII-art or tabbed output "
        "like tables as a fixed-sized font will be used "
        "for display.",
    )
    # -s is already used for --store, -i for sPlit
    ap.add_argument(
        "-p",
        "--split",
        required=False,
        type=str,
        help="If set, split the message(s) into multiple messages "
        "wherever the string specified with --split occurs. "
        "E.g. One pipes a stream of RSS articles into the "
        "program and the articles are separated by three "
        "newlines. "
        'Then with --split set to "\\n\\n\\n" each article '
        "will be printed in a separate message. "
        "By default, i.e. if not set, no messages will be split.",
    )
    # -c is already used for --credentials
    ap.add_argument(
        "-j",
        "--config",
        required=False,
        type=str,
        help="Location of a config file. By default, no "
        "config file is used. "
        "If this option is provided, the provided file name "
        "will be used to read configuration from. ",
    )
    # -p is already used for --split
    ap.add_argument(
        "--proxy",
        required=False,
        type=str,
        help="Optionally specify a proxy for connectivity. By default, "
        "i.e. if this option is not set, no proxy is used. "
        "If this option is used a proxy URL must be provided. "
        "The provided proxy URL "
        "will be used for the HTTP connection to the server. "
        "The proxy supports SOCKS4(a), SOCKS5, and HTTP (tunneling). "
        'Examples of valid URLs are "http://10.10.10.10:8118" '
        'or "socks5://user:password@127.0.0.1:1080". '
        'URLs with "https" or "socks4a" are not valid. Only '
        '"http", "socks4" and "socks5" are valid.',
    )
    ap.add_argument(
        "-n",
        "--notice",
        required=False,
        action="store_true",
        help="Send message as notice. "
        "If not specified, message will be sent as text.",
    )
    ap.add_argument(
        "-e",
        "--encrypted",
        required=False,
        action="store_true",
        help="Send message end-to-end "
        "encrypted. Encryption is always turned on and "
        "will always be used where possible. "
        "It cannot be turned off. This flag does nothing "
        "as encryption is turned on with or without this "
        "argument.",
    )
    # -n already used for --markdown, -e for "nOtice"
    ap.add_argument(
        "-s",
        "--store",
        required=False,
        type=str,
        default=STORE_DIR_DEFAULT,
        help="Path to directory to be "
        'used as "store" for encrypted messaging. '
        "By default, this directory "
        f'is "{STORE_DIR_DEFAULT}". '
        "Since encryption is always enabled, a store is "
        "always needed. "
        "If this option is provided, the provided directory name "
        "will be used as persistent storage directory instead of "
        "the default one. Preferably, for multiple executions "
        "of this program use the same store for the same device. "
        "The store directory can be shared between multiple "
        "different devices and users.",
    )
    ap.add_argument(
        "-l",
        "--listen",
        required=False,
        type=str,
        default=LISTEN_DEFAULT,  # when -l is not used
        nargs="?",  # makes the word optional
        const=FOREVER,  # when -l is used, but FOREVER is not added
        help="The --listen option takes one argument. There "
        f'are several choices: "{NEVER}", "{ONCE}", '
        f'"{FOREVER}", "{TAIL}", and "{ALL}". '
        f'By default, --listen is set to "{NEVER}".  So, by '
        "default no listening will be done. Set it to "
        f'"{FOREVER}" to listen for and print incoming messages '
        "to stdout. "
        f'"--listen {FOREVER}" will listen to all messages on '
        "all rooms forever. "
        f'To stop listening "{FOREVER}", use Control-C on '
        "the keyboard or send a signal to the process or service. "
        "The PID for signaling can be found in a PID file in "
        f'directory "{PID_DIR_DEFAULT}". '
        f'"--listen {ONCE}" will get all the messages from '
        "all rooms that are currently queued up. So, with "
        f'"{ONCE}" the program will start, print waiting '
        "messages (if any) and then stop. The timeout for "
        f'"{ONCE}" is set to 10 seconds. So, be patient, it '
        "might take up to that amount of time. "
        f'"{TAIL}" reads and prints the last N '
        "messages from the specified rooms, then quits. The "
        "number N can be set with the --tail option. With "
        f'"{TAIL}" some messages read might be old, '
        "i.e. already read before, some might be new, "
        "i.e. never read before. It prints the messages and then "
        f"the program stops. "
        "Messages are sorted, last-first. "
        "Look at --tail as that option is related "
        "to --listen tail. "
        f'The option "{ALL}" gets all messages available, '
        "old and new. "
        f'Unlike "{ONCE}" and '
        f'"{FOREVER}" that listen in ALL rooms, "{TAIL}" '
        f'and "{ALL}" listen '
        "only to the room specified in the credentials "
        "file or the --room options. "
        "Furthermore, when listening to messages, no messages "
        "will be sent. Hence, when listening, --message must not "
        "be used and piped input will be ignored. ",
    )
    ap.add_argument(
        "-t",
        "--tail",
        required=False,
        type=int,
        default=TAIL_UNUSED_DEFAULT,  # when -t is not used
        nargs="?",  # makes the word optional
        # when -t is used, but number is not added
        const=TAIL_USED_DEFAULT,
        help="The --tail option reads and prints up to the last N "
        "messages from the specified rooms, then quits. "
        "It takes one "
        "argument, an integer, "
        "which we call N here. If there are fewer than N messages "
        "in a room, it reads and prints up to N messages. "
        "It gets the last N messages in reverse order. "
        "It print the newest message first, and the "
        "oldest message last. "
        "If --listen-self is not set it will print less than "
        "N messages in many cases because N messages are "
        "obtained, but some of them are discarded by default if "
        "they are from the user itself. "
        "Look at --listen as this option is related to --tail."
        "Furthermore, when tailing messages, no messages "
        "will be sent. Hence, when tailing or listening, "
        "--message  must not be used and piped input will "
        "be ignored. ",
    )
    ap.add_argument(
        "-y",
        "--listen-self",
        required=False,
        action="store_true",
        help="If set and listening, "
        "then program will listen to and print also "
        "the messages sent by its own user. "
        "By default messages from oneself are not printed.",
    )
    ap.add_argument(
        # no single char flag
        "--print-event-id",
        required=False,
        action="store_true",
        help="If set and listening, "
        "then program will print also the event id for"
        "each message or other event.",
    )
    ap.add_argument(
        "-u",
        "--download-media",
        type=str,
        default="",  # if -u is not used
        action="store",
        nargs="?",  # makes the word optional
        const=MEDIA_DIR_DEFAULT,  # when -u is used, but no dir added
        help="If set and listening, "
        "then program will download "
        "received media files (e.g. image, audio, video, text, PDF files). "
        "media will be downloaded to local directory. "
        "By default, media will be downloaded to "
        f'is "{MEDIA_DIR_DEFAULT}". '
        "You can overwrite default with your preferred directory. "
        "If media is encrypted it will be decrypted and stored decrypted. "
        "By default media files will not be downloaded.",
    )
    ap.add_argument(
        "-o",
        "--os-notify",
        required=False,
        action="store_true",
        help="If set and listening, "
        "then program will attempt to visually notify of "
        "arriving messages through the operating system. "
        "By default there is no notification via OS.",
    )
    ap.add_argument(
        "-v",
        "--verify",
        required=False,
        type=str,
        default=VERIFY_UNUSED_DEFAULT,  # when -t is not used
        nargs="?",  # makes the word optional
        # when -v is used, but text is not added
        const=VERIFY_USED_DEFAULT,
        help="Perform verification. By default, no "
        "verification is performed. "
        f'Possible values are: "{EMOJI}". '
        "If verification is desired, run this program in the "
        "foreground (not as a service) and without a pipe. "
        "Verification questions "
        "will be printed on stdout and the user has to respond "
        "via the keyboard to accept or reject verification. "
        "Once verification is complete, stop the program and "
        "run it as a service again. Don't send messages or "
        "files when you verify. ",
    )
    ap.add_argument(
        "-x",
        "--rename-device",
        required=False,
        type=str,
        default=RENAME_DEVICE_UNUSED_DEFAULT,  # when -x isn't used
        help="Rename the current device to the new "
        "device name provided. No other operations like "
        "sending, listening, or verifying are allowed when "
        "renaming the device. ",
    )
    ap.add_argument(
        # no single char flag
        "--version",
        required=False,
        action="store_true",
        help="Print version information. After printing version information "
        "program will continue to run. This is useful for having version "
        "number in the log files.",
    )

    pargs = ap.parse_args()

    logger = logging.getLogger(PROG_WITHOUT_EXT)
    if pargs.log_level:
        initial_check_of_log_args()
        if len(pargs.log_level) > 0:
            if len(pargs.log_level) > 1:
                # set log level for EVERYTHING
                logging.getLogger().setLevel(pargs.log_level[1])
            # set log level for matrix-commander
            logger.setLevel(pargs.log_level[0])
            logger.debug(
                f"Log level is set for module {PROG_WITHOUT_EXT}. "
                f"log_level={pargs.log_level[0]}"
            )
            if len(pargs.log_level) > 1:
                # only now that local log level is set, we can log prev. info
                logger.debug(
                    f"Log level is set for modules below {PROG_WITHOUT_EXT}. "
                    f"log_level={pargs.log_level[1]}"
                )
    if pargs.debug > 0:
        if pargs.debug > 1:
            # turn on debug logging for EVERYTHING
            logging.getLogger().setLevel(logging.DEBUG)
        # turn on debug logging for matrix-commander
        logger.setLevel(logging.DEBUG)
        logger.debug(f"Debug is turned on. debug count={pargs.debug}")
        if pargs.log_level and len(pargs.log_level) > 0:
            logger.warning("Debug option -d overwrote option --log-level.")

    initial_check_of_args()
    if not is_download_media_dir_valid():
        sys.exit(1)
    create_pid_file()

    if pargs.version:
        version()  # continue execution

    try:
        if pargs.verify:
            asyncio.get_event_loop().run_until_complete(main_verify())
        elif pargs.rename_device:
            asyncio.get_event_loop().run_until_complete(main_rename_device())
        elif (
            pargs.listen == FOREVER
            or pargs.listen == ONCE
            or pargs.listen == TAIL
            or pargs.listen == ALL
        ):
            asyncio.get_event_loop().run_until_complete(main_listen())
        elif (
            pargs.room_create
            or pargs.room_join
            or pargs.room_leave
            or pargs.room_forget
            or pargs.room_invite
            or pargs.room_ban
            or pargs.room_unban
            or pargs.room_kick
        ):
            asyncio.get_event_loop().run_until_complete(main_room_actions())
        else:
            asyncio.get_event_loop().run_until_complete(main_send())
        logger.debug(f"The program {PROG_WITH_EXT} terminated successfully.")
    except TimeoutError:
        logger.info(
            f"The program {PROG_WITH_EXT} ran into a timeout. "
            "Most likely connectivity to internet was lost. "
            "If this happens frequently consider running this "
            "program as a service so it will restart automatically. "
            "Sorry. Here is the traceback."
        )
        logger.info(traceback.format_exc())
    except Exception:
        logger.info(
            f"The program {PROG_WITH_EXT} failed. "
            "Sorry. Here is the traceback."
        )
        logger.info(traceback.format_exc())
        # traceback.print_exc(file=sys.stdout)
    except KeyboardInterrupt:
        logger.debug("Keyboard interrupt received.")
    cleanup()
    sys.exit(1)

# EOF
