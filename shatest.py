from hashlib import sha256

#this is 64 bit hexadecimal 
#print( SHA256("ABC"))

MAX_NONCE  = 1000000000

def SHA256(text):
	return(sha256(text.encode('ascii')).hexdigest())

def mine(block_number, transactions, previous_hash, prefix_zeros):
	for nonce in range(MAX_NONCE):
		text = str(block_number) + transactions + previous_hash + str(nonce)
		new_hash = SHA256(text)
		if new_hash.startswith(difficulty * '0'):
			print('______you receive bitcoins_______')
			print( new_hash)
			return
		print(new_hash)
	return new_hash




if __name__ == '__main__':
	transactions= '''
	Joe -> Molly -> 30,
	Growgoo -> Tom -> 20
	'''

	#number of prevailing 0's
	difficulty =4
	new_hash = mine(5,transactions,'958a96ccd2e2dc1d871449661c53eede51b84c6de14148dd1922612a75b103a3',difficulty )
	
	print(new_hash)
