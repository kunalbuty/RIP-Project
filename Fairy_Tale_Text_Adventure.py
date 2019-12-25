def main():
	while(True):
		print("You are a young girl living in the early 1800s. Your father runs an import/export business, and has been largely successful. Consequently, you have been able to live lavishly. You have three older sisters, all of whom are very spoilt.  One day, your father makes a poor business decision, and your family's entire fortune is lost. You decide to:")
		print("1)Start working to help your family out:")
		print("2)do nothing. You have grown accustomed to living well, and aren't going to change your lifestyle just because your father made a mistake.")
		q1=eval(input())
		if(q1==1):
			print("You start waking up at the crack of dawn everyday to clean the house, and cook for your family. Although it is difficult. You:")
			print("1)take it in stride and quickly acclimatize to the change.")
			print("2)complain about it, but do it anyway.")
			q2=eval(input())
			print("As you sweep the floor, your sisters watch you scornfully. Your father walks in the room. He looks ecstatic. 'Good news, my daughters!', he says. 'One of my ships has returned, and it is filled with treasures. After selling them, I can bring each of you an item. What would you like?' You ask for:")
			print("1)A rose.")
			print("2)A nice pendant.")
			q3=eval(input())
			if(q3==1):
				print("Your sisters laugh at you for choosing such an invaluable object. They ask for diamonds and expensive clothing. However, your father looks at you and smiles. Your humility has yet again reinforced the idea that you are his favorite child.")
				print("A large storm creeps in over the mountains on the horizon. The wind bellows and rain pours down. Your father does not return that day, or the following one. You start to worry. Finally, on the third day, he returns. He is out of breath and terrified. 'My ship was robbed! Nothing of value was left by the time I got there.' Upon hearing this you:")
				print("1)comfort him on his loss")
				print("2)Bemoan your loss and scream at him for not being able to provide for your family")
				q4=eval(input())
				print("You start to speak, but before you finish, he cuts you off. 'I'm afraid that is not even the worst part!' He then explains to you that while picking a rose for you, he had been kidnapped by a horrible beast. He had only been able to come home because the beast had made a deal with him. Either he or one of his daughters must return to the beast's castle. Upon hearing this, you:")
				print("1)stay quiet. You know that if nothing is said, your father will return to the castle and you will be able to continue living in the village")
				print("2)suggest that you take his place and go to the castle")
				q5=eval(input())
				if(q5==2):
					print("You pack your bags, and your father guides you to the beast's home. He bids you farewell, and leaves before the beast can see him. Trembling, you knock on the castle door. Nobody answers. You explore the castle, and find a dining room, filled with delicious-smelling food. As you start to eat, the door opens, and the beast steps in. He is huge, with talons for nails, and has the teeth of a bear. Upon seeing him you:")
					print("1)wait and see what he does")
					print("2)scream and try to escape")
					q6=eval(input())
					if(q6==1):
						print("The beast walks in and politely asks if he may join you. You say yes, and he sits down at the table. The beast introduces himself to you and gives you a tour of the castle. It is a beautiful place, filled with grand chandeliers and high ceilings. Finally, the beast shows you to your bedroom, and bids you farewell. Once he closes the door, you:")
						print("1)decide that perhaps he is not the monster her father believed him to be.")
						print("2)suspect that the beast’s behavior is just a charade to trick you into trusting him so that he can eat you the next day.")
						q7=eval(input())
						if(q7==1):
							print("You lie down on your new bed. It is extremely comfortable, and soon you have fallen into a deep sleep. The next day you wake up, and a clean set of clothes has been left outside your room. You change into them, and proceed downstairs. The beast is waiting in the dining room. Breakfast is prepared. As you eat, a conversation begins, and you find that he has a pleasant personality. He is humble and polite. You find this to be:")
							print("1)genuine. You believe that he is a good person. You start to open up to him.")
							print("2)an act. You still suspect trickery, so you play along and bide your time.")
							q8=eval(input())
							if(q8==1):
								print("You spend the next few months together. You both have similar interests, and your personalities complement each other. He clearly loves you, and asks you to marry him many times, but each time you say no. You start to fall in love with him. Despite this, you miss your family, and sorely want to visit them. You are uncertain as to how the beast will react if you ask him. You decide to:")
								print("1)leave without telling him. It is your decision, and he doesn't need to know what you are doing.")
								print("2)inform him of your decision before leaving.")
								q9=eval(input())
								if(q9==2):
									print("The beast bids you farewell, and wishes you a safe journey. He also asks you to return after 7 days, which you promise to do. You return home, and are greeted enthusiastically by your father, who is delighted to see you. You tell your family about how amazing your life is at the castle, and that the beast is not a monster. Your sisters are very clearly jealous. On the day before you are set to return, your sisters drug you! Upon waking up, you realize that it has been 3 days, and that you are late to return. You decide to:")
									print("1)Return to the castle as soon as you can. You broke your promise, and you must return as soon as you can")
									print("2)Wait a few more days. Nothing bad has happened, and you're already late, so it doesn't really matter anymore.")
									q10=eval(input())
									if(q10==1):
										print("You hastily return to the castle. Upon entering, you see the beast lying on the floor. He is very sick, and near death. He had stopped eating since you left, and has not eaten in over a week. With tears in your eyes, you rush to him and beg him to wake up. He is just able to comprehend your words, but is too weak to respond. You:")
										print("1)rush to the kitchen to bring him food")
										print("2)profess your love to him and finally agree to marry him. He has to know how you feel about him.")
										q11=eval(input())
										if(q11==2):
											print("Upon uttering these words, the beast magically transforms into a handsome prince. He is no longer sick. You embrace him, and are full of joy. You have a beautiful wedding, and live happily ever after.")
										else:
											print("You bring him food, and slowly feed him. Over the course of the next few days, you nurse him back to health. When he is better, he yet again asks for your hand in marriage. You finally accept his request. Your wedding is beautiful, and you live happily ever after.")
									else:
										print("You spend two extra weeks with your family before returning to the castle. You walk in, and much to your horror, find the beast lying on the floor. He is dead. You realize that he must have thought you abandoned him, and had lost his will to live as a result. You wish you had just left on time. If you had, things might have turned out differently.")
								else:
									print("You pack your belongings, and leave the castle. You promise yourself that you will return by the end of the month. You return home, and are greeted enthusiastically by your father, who is delighted to see you. You tell your family about how amazing your life is at the castle, and that the beast is not a monster. Your sisters are very clearly jealous. You spend the month happily, and enjoy the company of your family. After the month is up, you return to the castle. Much to your horror, you find the beast lying on the floor. He is dead. You realize that he must have thought you abandoned him, and stopped eating as a result. You wish you could go back in time and just tell the beast that you were returning. If you had, things might have turned out differently.")
							else:
								print("You spend time together, and slowly gain the beast's trust. It is clear that he is smitten with you, and you plan on taking advantage of this. After months in the castle, you finally learn where the keys for the front door are kept. That night, you steal the keys and escape the castle. As you sneak through the grounds, you hear a mournful cry coming from the castle. It was the beast. You feel a pang of guilt, but proceed anyway. You finally get home, and your father is delighted to see you, and for a while, life is great. However, as time passes, you start to feel more and more guilty about taking advantage of the beast's feelings towards you. Finally, you can't take it anymore, and you return to the castle to find out the fate of the beast. Much to your horror, you learn that he died right after you left. You know that this occurred because of you, and taking different actions would have prevented this unfortunate situation.")
						else:
							print("You do not trust the beast, and decide to try and escape. The best route would be:")
							print("1)To climb out of the window")
							print("2)Exit the way you came.")
							q8=eval(input())
							if(q8==1):
								print("You exit through the window and balance precariously on the ledge below. You start to scale down the castle walls. After getting about half way down, you pause for a break. After you have gotten your breath back, you look for the next foothold, but it is out of reach. You can't reach the one above you either. You are stuck. After hours of waiting, your arms tire, and you fall. You are dead.")
							else:
								print("You quietly sneak through the castle. You make it to the front door, but realize that it is locked. With no other choice, you return to your room. The only other way out is through the window. You exit through it and balance precariously on the ledge below. You start to scale down the castle walls. After getting about half way down, you pause for a break. After you have gotten your breath back, you look for the next foothold, but it is out of reach. You can't reach the one above you either. You are stuck. After hours of waiting, your arms tire, and you fall. You are dead.")

					else:
						print("You race towards the exit, praying that the beast doesn't catch you. You turn a corner, but don't realize that there are stairs there. You trip and fall. Your head hits the stone floor. You are dead.")
				else:
					print("Your father returns to the castle, and a ball of guilt forms in your stomach. Days turn into weeks. You start to wonder if you made the right call. For all you know he could be dying. Finally, you decide to:")
					print("1)Forget about him")
					print("2)attempt to rescue him")
					q6=eval(input())
					if(q6==2):
						print("After months of research and preparation, you have finally decided on a plan of action. You are going to:")
						print("1)sneak into the castle in the middle of the night and save your father.")
						print("2)get all the village soldiers to storm the beast's castle.")
						q7=eval(input())
						if(q7==1):
							print("You wait outside the castle until it is dark, and then sneak into the castle. Where do you check first?")
							print("1)The dungeon")
							print("2)The guest rooms")
							q8=eval(input())
							if(q8==1):
								print("You enter the dungeon but it is deserted.")
							print("You decide to search the guest rooms. As you climb the stairs, you hear a noise. Much to your surprise, it is your father. He is laughing. Upon further investigation, you find him. He is in a grand bedroom, filled with beautiful art and comfortable looking furniture. He is reading a book. You decide to:")
							print("1)Leave him behind. He seems to be happy, and you don't want to risk confronting the beast.")
							print("2)Get his attention and try to save him.")
							q9=eval(input())
							if(q9==1):
								print("You sneak away as quietly as you can, and exit the castle. As you walk home, you think about what you just saw. Your father seemed to be living a very luxurious life. Upon returning home, you realize that your life is in shambles. With no source of income for the past month, your house has fallen apart and your family is starving. You decide to:")
								print("1)seduce a man and marry him. You have no skills of your own, and this seems to be your only option.")
								print("2)wait for someone else to do something. They will fix your problems.")
								q2a=eval(input())
								if(q2a==1):
									print("You make it your mission to find a suitable man to marry. After much consideration, you decide to marry:")
									print("1)the son of a noble")
									print("2)a random farmer")
									q3a=eval(input())
									if(q3a==1):
										print("No noble would allow their son to marry a homeless person. Your attempts fail. With no other choice left you marry the farmer.")
									print("The wedding is far from what you wanted. The flowers are dying and the food is barely edible. You spend the rest of your life just above the poverty line. Although you aren't starving, you certainly aren't living well. Your husband is not a good man, and treats you poorly. You look back on your life full of regret and bitterness, knowing that taking different actions would have led to a much happier life.")
								else:
									print("Unable or unwilling to do anything about your situation, you and your family slowly starve to death.")
							else:
								print("You enter the room. Your father looks up and sees you. He is so shocked that he is unable to formulate words. You hurriedly tell him that you are here to rescue him, but he tells you that there is no need. The beast is not horrible as he had previously thought. In fact, they have become friends. Upon hearing this, you:")
								print("1)Don't believe him. The beast must have brainwashed him.")
								print("2)ask if your father wants to come home.")
								q10=eval(input())
								if(q10==1):
									print("You decide that the only way to release your father from the spell is to kill the beast. To do this, you will:")
									print("1)Get a knife from the kitchen and stab the beast in his sleep.")
									print("2)Poison the beast's food.")
									q11=eval(input())
									if(q11==1):
										print("You get the knife, and proceed to the beasts personal quarters. The lights in his room are off. You approach the door with the knife gripped tightly in your hand. Suddenly you hear a noise. It came from behind you. You slowly turn around, and much to your horror, the beast is standing there. You close your eyes and wait for the inevitable. You are dead.")
									else:
										print("You enter the kitchen and find some rat poison. As you sprinkle it over some food, it gets in your eyes. Blinded by it and in pain, you stumble backwards, and trip. You hit your head against the floor, and hear a resounding crack. You are dead.")
								else:
									print("After asking your father if he wants to come home, he calmly explains that he is happy with his life. However, he regrets abandoning his children without any source of money. He asks you to come close; he wants to tell you the key to restarting and maintaining his business. After listening to this, you bid him farewell and tearfully return home. With the key to the business in your mind, you are able to restore your fathers business to its former glory. You and your siblings live out the rest of your days happily. Every so often, the beast permits your father to visit you. You look back on your life, and are relatively happy with how it played out. Although it wasn't perfect, it was far better than that of most.")
						else:
							print("Hundreds of villigers join the assault on the castle. Armed with torches, pitchforks, and swords, they march to the castle and break down the doors. Although the beast fights as hard as he can, he is eventually overcome and killed. You rush through the castle, looking for your father. You find him hiding inside a bedroom. You attempt to hug him, but he pushes you away. Tearfully, he explains that he and the beast was not a monster. Although he had a crusty exterior, he was a kind and generous person. You return home with him, but you can tell that he has not forgiven you, and have a feeling that you never will. The loot from the castle funds your family's expenses for years to come, but your relationship with your father is past fixing. You look back on your life and only see regret. Although you have all the money you need, you lost something far more valuable. If you hadn't just assumed that the beast was a monster, things could have turned out very differently.")
					else:
						print("With your father gone, you have no source of income, and cannot afford to pay rent. You are now homeless. You decide to: ")
						print("1)seduce a man and marry him. You have no skills of your own, and this seems to be your only option.")
						print("2)wait for someone else to do something. They will fix your problems.")
						q2a=eval(input())
						if(q2a==1):
							print("You make it your mission to find a suitable man to marry. After much consideration, you decide to marry:")
							print("1)the son of a noble")
							print("2)a random farmer")
							q3a=eval(input())
							if(q3a==1):
								print("No noble would allow their son to marry a homeless person. Your attempts fail. With no other choice left, you marry the farmer.")
							print("The wedding is far from what you wanted. The flowers are dying and the food is barely edible. You spend the rest of your life just above the poverty line. Although you aren't starving, you certainly aren't living well. Your husband is not a good man, and treats you poorly. You look back on your life full of regret and bitterness, knowing that taking different actions would have led to a much happier life.")	
			else:
				print("Your father wishes you farewell and departs. A large storm creeps in over the mountains on the horizon. The wind bellows and rain pours down. Your father does not return that day, or the following one. You start to worry. Finally, on the third day, he returns. He is out of breath and terrified. 'My ship was robbed! Nothing of value was left by the time I got there!' Upon hearing this you:")
				print("1)comfort him on his loss")
				print("2)Bemoan your loss and scream at him for not being able to provide for your family")
				q4=eval(input())
				if(q4==1):
					print("As your sisters scream at him in disappointment, you take his hand and tell him that it isn't his fault. You talk with him for hours, and help him come up with a plan to go forward. He asks you to help him run the business. You decide to:")
					print("1)join him")
					print("2)decline his offer")
					q5=eval(input())
					if(q5==1):
						print("With your collective brainpower, you are able to save his business from collapsing. Your family is able to live reasonably well, although they aren't considered to be wealthy. As you reach your 30's you decide to:")
						print("1)let your father retire and take over the business.")
						print("2)look for a good husband")
						q6=eval(input())
						if(q6==1):
							print("You take over the business, and restore it to its former glory. Soon you and your family are some of the richest people in the country, and you are known and respected by all. You look back on your life, and are delighted with your success. It was your hard work that brought you to this moment.")
						else:
							print("Although your family isn't wealthy, your business exploits are respected, and so many men are looking for your hand in marriage. After meeting almost fifty different men, you finally find one to your liking. You have a memorable wedding, and live out the rest of your days happily.")
					else:
						print("Although the business keeps afloat, it just barely provides enough to pay for your living expenses. You are forced to take a job as a servant, and live out the rest of your days cleaning and cooking for other families. You look back on your life and see only dissapointment. You know that if you had tried harder, your life could have been better.")
				else:
					print("Your father gives up on his business, and leaves the future of your family to fate. Shocked, you realize that your family has no form of income. Upon realizing this all your siblings leave and pursue their own futures. No matter how successful you might become now, you will never get to see your family again.")
		else:
			print("Your family can no longer afford servants, and your house becomes filthy to the point that you have to move out. You are now homeless. You decide to: ")
			print("1)seduce a man and marry him. You have no skills of your own, and this seems to be your only option.")
			print("2)wait for someone else to do something. They will fix your problems.")
			q2a=eval(input())
			if(q2a==1):
				print("You make it your mission to find a suitable man to marry. After much consideration, you decide to marry:")
				print("1)the son of a noble")
				print("2)a random farmer")
				q3a=eval(input())
				if(q3a==1):
					print("No noble would allow their son to marry a homeless person. Your attempts fail. With no other choice left you marry the farmer.")
				print("The wedding is far from what you wanted. The flowers are dying and the food is barely edible. You spend the rest of your life just above the poverty line. Although you aren't starving, you certainly aren't living well. Your husband is not a good man, and treats you poorly. You look back on your life full of regret and bitterness, knowing that taking different actions would have led to a much happier life.")
			else:
				print("Your father attempts to rebuild his business, but to no avail. Unable or unwilling to do anything about it, you and your family slowly starve to death.")
		print("Game Over. Press Enter to Restart")
		print("")
		print("")
main()
