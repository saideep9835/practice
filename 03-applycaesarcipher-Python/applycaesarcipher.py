# A Caesar Cipher is a simple cipher that works by shifting each letter in 
# the given message by a certain number. For example, if we shift the message 
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given 
# message by shift letters. You are guaranteed that message is a string, and 
# that shift is an integer between -25 and 25. Capital letters should stay capital 
# and lowercase letters should stay lowercase, and non-letter characters should not be changed. 
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")

alpha= "abcdefghijklmnopqrstuvwxyz"
be = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ce = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def fun_applycaesarcipher(msg, shift):
	g=[]
	o = ""
	u = ""
	for i in range(len(msg)):
		if msg.islower():
			ch = msg[i]
			lo = alpha.find(ch)
			new_lo=(lo+shift)%26
			o += alpha[new_lo]
			
		elif msg.isupper():
			ch = msg[i]
			lo = be.find(ch)
			new_lo=(lo+shift)%26
			o += be[new_lo]
	
		else:
		
			ch = msg[i]
			lo = ce.find(ch)
			new_lo=(lo+shift)%52
			o += ce[new_lo]
			o=o.replace("a"," ")
	return o
	







