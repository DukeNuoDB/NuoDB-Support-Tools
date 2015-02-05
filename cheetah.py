from sys import argv
from collections import OrderedDict

# Find and catalog each log line that matches these strings
match_strings = [
	"NuoAgent version", "Assertion", "error", "failed", "INFO", "WARN",
	"SEVERE", "Local node", "Remote Node", "minorty partition",
	"heartbeat expired", "evict", "DIED", "exit code",
	"Database is inactive", "Node joined", "Node left"
]
# Don't print out every line that contains these strings,
# instead trucnate to the last N lines
summarize = ["error", "INFO", "WARN", "failed"]
summarize_length = 5

if len(argv) > 1:
	files = argv[1:]
else:
	print "ERROR: You must provide at least one log file to be processed."
	print "Example:"
	print "%s my.log" % argv[0]
	exit(2)

for filename in files:
	with open(filename) as f:
		data = f.read().splitlines()

		# Create data structure to handle results
		matches = OrderedDict()
		for string in match_strings:
			matches[string] = []

		for i, s in enumerate(data, 1):
			for string in match_strings:
				if string in s:
					matches[string].append('Line %03d: %s' % (i, s,))

		# There are always more INFO and WARN messages than are usable.
		# This returns the  most recent messages for each.
		for item in summarize:
			matches[
				"%s (last %d lines)" % (item, summarize_length)] = matches[item]
			[(summarize_length * -1):
		]

		nodemerge = matches['Node joined'] + matches['Node left']
		matches['nodes'] = nodemerge
		del matches['Node joined']
		del matches['Node left']
	print
	print "======================================"
	print "==Printing Analysis..."
	print "======================================"
	print
	print "======================================"
	print "==Total Message Counts"
	print "======================================"
	for string in matches:
		if " (last %d lines)" % summarize_length not in string:
			print "Total entires matching \"%s\": %d" % (string, len(matches[string]))
	print
	print "======================================"
	print "==Message Details"
	print "======================================"
	for string in matches:
		if string not in summarize:
			print "%s:" % string.upper()
			if len(matches[string]) > 0:
				print '\n'.join([str(myelement) for myelement in matches[string]])
			else:
				print "0 entries in the log."
			print
