"""
Sample script to test ad-hoc scanning by table drive.
This accepts a number with optional decimal part [0-9]+(\.[0-9]+)?

NOTE: suitable for optional matches
"""

def getchar(text,pos):
	""" returns char category at position `pos` of `text`,
	or None if out of bounds """
	
	if pos<0 or pos>=len(text): return None
	
	c = text[pos]
	
	# **Σημείο #3**: Προαιρετικά, προσθέστε τις δικές σας ομαδοποιήσεις
	
	#if c>='0' and c<='9': return 'DIGIT'	# 0..9 grouped together
	
	if c=='.': return 'DOT'	# dot as a category by itself
	
	return c	# anything else
	


def scan(text,transitions,accepts):
	""" scans `text` while transitions exist in
	'transitions'. After that, if in a state belonging to
	`accepts`, it returns the corresponding token, else ERROR_TOKEN.
	"""
	
	# initial state
	pos = 0
	state = 's0'
	# memory for last seen accepting states
	last_token = None
	last_pos = None
	
	
	while True:
		
		c = getchar(text,pos)	# get next char (category)
		
		if state in transitions and c in transitions[state]:
			state = transitions[state][c]	# set new state
			pos += 1	# advance to next char
			
			# remember if current state is accepting
			if state in accepts:
				last_token = accepts[state]
				last_pos = pos
			
		else:	# no transition found

			if last_token is not None:	# if an accepting state already met
				return last_token,last_pos
			
			# else, no accepting state met yet
			return 'ERROR_TOKEN',pos
			
	
# **Σημείο #1**: Αντικαταστήστε με το δικό σας λεξικό μεταβάσεων
transitions = { 's0': { '0':'s1','1':'s1','2':'s1','3':'s2' },
       			's1': { '0':'s3','1':'s3','2':'s3','3':'s3','4':'s3','5':'s3','6':'s3','7':'s3','8':'s3','9':'s3'},
       			's2': { '0' :'s3','1':'s3','2':'s3','3':'s3','4':'s3','5':'s3'},
			's3': { '0' : 's4'},
       			's4': { '0':'s5','1':'s5','2':'s5','3':'s5','4':'s5','5':'s5','6':'s5','7':'s5','8':'s5','9' :'s5' },
	       		's5': { '0':'s6','1':'s6','2':'s6','3':'s6','4':'s6','5':'s6','6':'s6','7':'s6','8':'s6','9' :'s6' },
	       		's6': { 'G':'s7','K':'s9' },
	       		's7': { '0':'s8','1':'s8','2':'s8','3':'s8','4':'s8','5':'s8','6':'s8','7':'s8','8':'s8','9':'s8' },
	       		's8': { '0':'s6','1':'s6','2':'s6','3':'s6','4':'s6','5':'s6','6':'s6','7':'s6','8':'s6','9' :'s6' },
	       		's9': { 'T':'s10'}
	       		
     		  } 

# **Σημείο #2**: Αντικαταστήστε με το δικό σας λεξικό καταστάσεων αποδοχής
accepts = { 's10':'WIND_TOKEN'	
     	  }


# get a string from input
text = input('give some input>')

# scan text until no more input
while text:		# i.e. len(text)>0
	# get next token and position after last char recognized
	token,pos = scan(text,transitions,accepts)
	if token=='ERROR_TOKEN':
		print('unrecognized input at position',pos,'of',text)
		print('ERROR_TOKEN')
		break
	print("token:",token,"text:",text[:pos])
	# new text for next scan
	text = text[pos:]
	
