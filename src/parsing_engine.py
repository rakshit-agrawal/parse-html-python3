#!/usr/local/bin/python3

#--------------IMPORTS-------------#

from html.parser import HTMLParser



#------------CLASSES-------------#

#-----Class TagBox for the HTML Tree elements

class TagBox:

	tid = 0	
	tdepth = 0
	ttag_name = ''
	tattrib = None
	tdata = ''
	tparent = 0
	tchild = []
	tcounter = 0
	tcombined_name = ''

	def __init__(self,val):
		self.tid = val
		self.tchild = []
		TagBox.tcounter = TagBox.tcounter + 1

	def combined_name_creator(self) :
		self.tcombined_name = self.ttag_name
		for i in self.tattrib:
			if (i[0] == "id"):
				self.tcombined_name = self.tcombined_name + "#" + i[1]
			if (i[0] == "class"):
				self.tcombined_name = self.tcombined_name + "." + i[1]
			

#-----Class ParsingEngine is the Main HTML parser class. All parsing operations are handled by this class

class ParsingEngine(HTMLParser):
	
	ctr = 0		#Sequence counter
	depth = 0	#Stack dpeth
	gstack = []	#Stack of tags
	PageTree=[]	#Tree variable for main HTML tree

	ignore_list = ['link','meta','img','input','hr','br']





	def handle_starttag(self, tag, attrs):

		ParsingEngine.PageTree.append(TagBox(ParsingEngine.ctr))
		ParsingEngine.ctr = ParsingEngine.ctr + 1
		ParsingEngine.gstack.append(ParsingEngine.PageTree[-1].tid)
		ParsingEngine.PageTree[-1].depth = ParsingEngine.depth
		ParsingEngine.depth = ParsingEngine.depth + 1
		ParsingEngine.PageTree[-1].ttag_name = tag
		ParsingEngine.PageTree[-1].tattrib = attrs
		ParsingEngine.PageTree[-1].combined_name_creator()

		try:
			ParsingEngine.PageTree[-1].tparent = ParsingEngine.gstack[-2]
			ParsingEngine.PageTree[ParsingEngine.gstack[-2]].tchild.append(ParsingEngine.PageTree[-1].tid)
	
		except:
			print ("Error")

		
		if (tag in ParsingEngine.ignore_list):

			ParsingEngine.gstack.pop()
			ParsingEngine.depth = ParsingEngine.depth - 1
		'''		
		else:
			ParsingEngine.PageTree.append(TagBox(ParsingEngine.ctr))
			ParsingEngine.ctr = ParsingEngine.ctr + 1
			ParsingEngine.gstack.append(ParsingEngine.PageTree[-1].tid)
			ParsingEngine.PageTree[-1].depth = ParsingEngine.depth
			ParsingEngine.depth = ParsingEngine.depth + 1
			ParsingEngine.PageTree[-1].ttag_name = tag
			ParsingEngine.PageTree[-1].tattrib = attrs
			ParsingEngine.PageTree[-1].combined_name_creator()

			try:
				ParsingEngine.PageTree[-1].tparent = ParsingEngine.gstack[-2]
				ParsingEngine.PageTree[ParsingEngine.gstack[-2]].tchild.append(ParsingEngine.PageTree[-1].tid)
	
			except:
				print ("Error")
		'''

	def handle_endtag(self, tag):

		if (tag in ParsingEngine.ignore_list):
			no_problem = 1
			#print ("Link or Meta Found")
		
		else:
			ParsingEngine.gstack.pop()
			ParsingEngine.depth = ParsingEngine.depth - 1

	def handle_data(self, data):
		
		try:
			if (ParsingEngine.PageTree[-1].ttag_name in ParsingEngine.ignore_list):
				no_problem = 1
		
			else:
				try:
					ParsingEngine.PageTree[ParsingEngine.gstack[-1]].tdata = ParsingEngine.PageTree[ParsingEngine.gstack[-1]].tdata + data
	
				except:
					print ("Error")
					
			
		except:
			print("No problem")



	def printTree(self):
		for i in ParsingEngine.PageTree:
			print ("Tag : ",i.ttag_name," --- ID: ",i.tid)
			#print ("Data : ",i.tdata)
			print ("***Parent : ", i.tparent)
			print ("\tKids : ",i.tchild)
			#i.combined_name_creator()
			print ("Combined Name : ",i.tcombined_name) 
			print ("________________________________________________________________________")
			#print ("Data : ",i.tdata)

	
#---------OPERATIONS---------#
	

parser = ParsingEngine()

searcher = SearchRule()

#parser.initialize()

#	For reading from file directly

f= open('data001/bl_article_test.html','r')

parser.feed(f.read())

print("****************************************************")
print (parser)

	
print (parser.ctr)
print (parser.depth)
print("****************************************************")
print("****************************************************")
print("****************************************************")
parser.printTree()

print("****************************************************")


