import math
from math import sqrt
import pygame

inputFile = open("./text_3.txt", 'r')

def text_to_list():
	random_number = []
	list_of_word = []

	for lineOfText in inputFile:
		words = lineOfText.split()

		for word in words:

			for letters in word:
				list_of_word.append(letters)

	alphabetList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	
	list_of_letters = list(set(list_of_word).intersection(alphabetList))
	#print list_of_letters
	return list_of_letters


def rgb_value():

	letter_list = text_to_list()

	r_value = ['E','e','O','o','S','s','D','d','U','u','F','f','P','p','K','k','Q','q']
	g_value = ['T','t','I','i','H','h','L','l','M','m','G','g','B','b','J','j','Z','z']
	b_value = ['A','a','N','n','R','r','C','c','W','w','Y','y','V','v','X','x']
		
	r_cross_list = list(set(letter_list).intersection(r_value))
	g_cross_list = list(set(letter_list).intersection(g_value))
	b_cross_list = list(set(letter_list).intersection(b_value))

	#print len(r_cross_list), len(g_cross_list), len(b_cross_list)

	r_percentage = int (float(len(r_cross_list)) / float((len(r_cross_list)) + float(len(g_cross_list)) + float(len(b_cross_list))) * 100 * 2.55)
	g_percentage = int (float(len(g_cross_list)) / float((len(r_cross_list)) + float(len(g_cross_list)) + float(len(b_cross_list))) * 100 * 2.55)
	b_percentage = int (float(len(b_cross_list)) / float((len(r_cross_list)) + float(len(g_cross_list)) + float(len(b_cross_list))) * 100 * 2.55)

	#print int(2.55 * g_percentage)


	return (r_percentage,g_percentage,b_percentage)

rgb_color = rgb_value()

print rgb_color
myImage = pygame.Surface((500,500))
myImage.fill(rgb_color)
pygame.image.save(myImage,'./newcolor1.png')



