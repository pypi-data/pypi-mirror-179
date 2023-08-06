watchpylint
===========

A simple utility script which watches for changes in the given Python files, and runs
`pylint` on them. It then groups the output together by message type and saves the output
to a file.

It will run lint processes in parallel (up to 8), and also has an option to wait for
output to be available before printing it. That allows you to set `watchpylint -w
lint.txt` as your editor's linter or compiler for easy browsing of the output.

Example
-------

```
cd ~/py/myproject
watchpylint *.py -o lint.txt
```

Then, in `emacs`:

```
M-x compile
watchpylint -w lint.txt
```
