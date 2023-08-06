# Toolboks CLI tools

toolboks-cli is a bundle of command line tools utilising the toolboks library.

## Installation

Install with pip:

`pip install toolboks-cli`


### Requirements

- python >= 3.9
- toolboks

### Command line scripts
toolboks-cli will install the following commands:  

- tb-conf

## Usage

### tb-conf

`tb-conf <filename> <section> <key>` - Read configuration value from any configuration file on INI format  

Example:  

Having a ~/.gitconfig file with the following configuration:

```
[user]
    email = user@example.host
    name = Testy Test

[diff]
    tool = vimdiff

[difftool]
    prompt = false

[alias]
    d = difftool
```

Any value in the configuration file can be fetched with tb-conf:  

```
$ tb-conf ~/.gitconfig user email
user@example.host
$ tb-conf ~/.gitconfig diff tool
vimdiff
$ tb-conf ~/.gitconfig user name
Testy Test
```


## License

GPL-3.0-only
