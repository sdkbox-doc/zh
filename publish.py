#!/usr/bin/python
# coding=utf-8

from argparse import ArgumentParser
import subprocess

parser = ArgumentParser(description="Build SDKBox documentation.")
parser.add_argument('-t', '--test', dest='test', action='store_true', default=False, help='Do not publish to docs.sdkbox.com')

(args, unknown) = parser.parse_known_args()
if len(unknown) > 0:
    print("unknown arguments: %s" % unknown)
    parser.print_help()

if args.test:
    subprocess.Popen(['git', 'checkout', 'master']).wait()
    subprocess.Popen(['git', 'pull']).wait()
    subprocess.Popen(['python', './src/doc.py', 'all']).wait()
    subprocess.Popen(['mkdocs', 'serve']).wait()
else:
    subprocess.Popen(["git", "fetch"]).wait()
    subprocess.Popen(["git", "checkout", "gh-pages "]).wait()
    subprocess.Popen(["git", "pull"]).wait()
    subprocess.Popen(["git", "checkout", "master"]).wait()
    subprocess.Popen(["git", "pull"]).wait()
    subprocess.Popen(["./src/doc.py", "all"]).wait()
    subprocess.Popen(["mkdocs", "gh-deploy", "--clean"]).wait()
