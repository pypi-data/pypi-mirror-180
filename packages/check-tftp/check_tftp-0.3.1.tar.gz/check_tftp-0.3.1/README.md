check_tftp
===========

check_tftp is an [Icinga2]/[Nagios] plugin which monitors a TFTP server by downloading a file from the server and optionally verifying its contents.

Requires Python 3.6+

# Installation

You can install with [pip]:

```sh
python3 -m pip install check-tftp
```

Or install from source:

```sh
git clone https://gitlab.com/cspeterson/check_tftp.git check_tftp.git
pip install check_tftp.git
```

# Usage

```
usage: check_tftp [-h] [--checksum CHECKSUM | --pattern PATTERN]
                   [--critical CRITICAL] --hostname HOST [--port PORT]
                   [--timeout TIMEOUT] [--verbose] [--warning WARNING]
                   files

        check_tftp is an Icinga2/Nagios plugin that monitors a TFTP server by
        downloading a file from the server and optionally verifying its
        contents


positional arguments:
  files                 The remote path of the file to check

options:
  -h, --help            show this help message and exit
  --checksum CHECKSUM, -k CHECKSUM
                        MD5 checksum to verify the remote file
  --pattern PATTERN, -r PATTERN
                        Python regular expression to look for in the remote
                        file. The check will fail if the pattern is not
                        present.
  --critical CRITICAL, -c CRITICAL
                        Critical range for download duration in seconds
  --hostname HOST, -H HOST
                        The TFTP server address
  --port PORT, -p PORT  The TFTP server port
  --timeout TIMEOUT, -t TIMEOUT
                        Total transmission timeout for the file transfer.
  --verbose, -v         Set output verbosity (-v=warning, -vv=debug)
  --warning WARNING, -w WARNING
                        Warning range for download duration in seconds

examples:

        # Check that a file can be downloaded from a tftp server:

        check_tftp --hostname host.name.tld some.file

        # As above, but check for pattern in the file:

        check_tftp --hostname host.name.tld --pattern 'some text' some.file

        # Or verify the file by md5 checksum:

        check_tftp --hostname host.name.tld \
            --checksum 75170fc230cd88f32e475ff4087f81d9 some.file

        # WARN if download takes longer than 5s, CRIT if longer than 10s:

        check_tftp --hostname host.name.tld --warning 5 --critical 10 some.file

        # For more on how to set ranges for warning or critical, see Nagios
        # Plugin Development Guidelines:
        #
        # https://nagios-plugins.org/doc/guidelines.html#THRESHOLDFORMAT
```

## Icinga2

Here is an Icinga2 `CheckCommand` object for this plugin:

```
object CheckCommand "check_tftp" {
  command = [ PluginDir + "/check_tftp", ]
  arguments = {
    "--checksum" = {
      description = "MD5 checksum to verify the remote file"
      key = "--checksum"
      set_if = "$tftp_checksum$"
      value = "$tftp_checksum$"
    }
    "--critical" = {
      description = "Critical range for download duration in seconds"
      key = "--critical"
      set_if = "$tftp_critical$"
      value = "$tftp_critical$"
    }
    "--hostname" = {
      description = "The TFTP server address"
      key = "--hostname"
      value = "$tftp_hostname$"
    }
    "--pattern" = {
      description = "Python regular expression to look for in the remote file. The check will fail if the pattern is not present."
      key = "--pattern"
      set_if = "$tftp_pattern$"
      value = "$tftp_pattern$"
    }
    "--port" = {
      description = "The TFTP server port"
      key = "--port"      set_if = "$tftp_port$"
      value = "$tftp_port$"
    }
    "--timeout" = {
      description = "Total transmission timeout for the file transfer"
      key = "--timeout"
      set_if = "$tftp_timeout$"
      value = "$tftp_timeout$"
    }
    "--warning" = {
      description = "Warning range for download duration in seconds"
      key = "--warning"
      set_if = "$tftp_warning$"
      value = "$tftp_warning$"
    }
    file = {
      description = "The remote path of the file to check"
      required = true
      skip_key = true
      value = "$tftp_file$"
    }
  }
  vars.tftp_hostname = "$address$"
}
```

And a minimal example Icinga Service:

```
}
object Service "host.domain.tld_check" {
  import "generic-service"
  display_name = "TFTP server verify download"
  host_name = "host.domain.tld"
  check_command = "check_tftp"
  notes = "The `check_tftp` command is a custom plugin to monitor a TFTP server by downloading a file and verifying its contents"
  notes_url = "https://gitlab.com/cspeterson/check_tftp"

  vars.tftp_file = "any_file_name.txt"
  vars.tftp_warning = 5
  vars.tftp_critical = 10
  vars.tftp_pattern = "your.regex"
}
```

NOTE on the command path: the above Icinga2 configuration object points to the `check_tftp` command in Icinga2's configured `PluginDir`, but this can be configured however you like. For instance:

* point it to wherever it is installed by its full path
* symlink from the specified path to the actual script.
* or take the kludge route, leave it as-is, and copy `check_tftp/__main__.py` from this repo into `PluginDir + "/check_tftp"`

Up to you!


# Contributing

Pull/Merge requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

To run the test suite:

```bash
# Up to you to create virtual environments etc
# make dependencies
make
```

Please make sure to update tests as appropriate.

# License

[MIT]


[Icinga2]: https://en.wikipedia.org/wiki/Icinga
[MIT]: https://choosealicense.com/licenses/mit/
[Nagios]: https://en.wikipedia.org/wiki/Nagios
[pip]: https://pip.pypa.io/en/stable/
