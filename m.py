try:
	import emojis

	while True:
		i=input('Enter Any Thing: ')
		if i=="q":
			break
			exit()
		print(f"You Entered {i}")
		print(emojis.encode("Nice :thumbs_up: :india:"))
except KeyboardInterrupt:
	print("Getting Exit")