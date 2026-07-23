#!/usr/bin/env python

import crfsuite
import sys

def instances(fi):
    xseq = crfsuite.ItemSequence()
    fi = 'If the'
    fi = fi.split(' ')

    for line in fi:
        print "********************"
        line = line.strip('\n')
        if not line:
        	# An empty line presents an end of a sequence.
            yield xseq
            xseq = crfsuite.ItemSequence()
            continue

		# Split the line with TAB characters.
        fields = line.split('\t')
        item = crfsuite.Item()
        for field in fields[1:]:
            p = field.rfind(':')
            if p == -1:
            	# Unweighted (weight=1) attribute.
                item.append(crfsuite.Attribute(field))
            else:
            	# Weighted attribute
                item.append(crfsuite.Attribute(field[:p], float(field[p+1:])))

        # Append the item to the item sequence.
        xseq.append(item)

if __name__ == '__main__':
    fi = sys.stdin
    fo = sys.stdout

	# Create a tagger object.
    tagger = crfsuite.Tagger()
    
    # Load the model to the tagger.
    # tagger.open(sys.argv[1])
    tagger.open('/home/zelalem/crf/crfsuite-0.12/BuildDirect.model')

    for xseq in instances(fi):
    	# Tag the sequence.
        tagger.set(xseq)
        # Obtain the label sequence predicted by the tagger.
        yseq = tagger.viterbi()
        # Output the probability of the predicted label sequence.
        print tagger.probability(yseq)
        for t, y in enumerate(yseq):
        	# Output the predicted labels with their marginal probabilities.
            print '%s:%f' % (y, tagger.marginal(y, t))
        print
