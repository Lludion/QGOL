"""
Generates this documentation, using pdoc

IMPORTANT MESSAGE : IF YOU WISH TO ADD A NEW FOLDER TO THE PROJECT, WRITE ITS NAME HERE in main.modules DOWN BELOW.

"""
import pdoc
import os

def recursive_htmls(mod):
    yield mod.name, mod.html()
    for submod in mod.submodules():
        yield from recursive_htmls(submod)

def repdot(x):
	""" replaces dots"""
	s = ""
	for i in range(len(x)):
		if x[i] != ".":
			s += x[i]
		else:
			s += "/"
	return s
def cutdot(x):
	""" cuts where there are dots"""
	s = ""
	li = []
	for i in range(len(x)):
		if x[i] != ".":
			s += x[i]
		else:
			li.append(s)
			s = ""
	li.append(s)
	return li


def isdir(path):
	if os.path.isdir(path):  
		return True
	elif os.path.isfile(path):  
		return False
	raise BaseException("Lmao")


def glof(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list(listOfFile)
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + glof(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

def main():
	modules = ['qgol',"obj","log","img","tst","efficient","obj.base",'ope']  # Public submodules are auto-imported
	for mod in modules:
		if mod != 'qgol':
			os.system('mkdir ' + os.path.join('doc',*cutdot(mod)))
	context = pdoc.Context()

	modules = [pdoc.Module(mod, context=context)
		       for mod in modules]
	pdoc.link_inheritance(context)

	for mod in modules:
		for module_name, html in recursive_htmls(mod):
			with open("doc/"+repdot(module_name)+".html","w") as file:
				file.write(html)

	#print("lkjlk")
	files = list(dict.fromkeys(glof("/home/urem/Desktop/work/ARTeQ/QGOL/")))
	#print("FILES:",files)

	for f in files:
		if f[-5:] == ".html":
			#print("FILENAME:",f)
			#print('type;',type(f))
			if [x for x in files if x == f[:-5]]:
				x = [x for x in files if x == f[:-5]][0]
				print(f)
				try:
					os.rename("doc/"+f,"doc/"+x+"/index.html")
					print("moved",f)
				except FileNotFoundError as e:
					print(e)
	incantation = """
<h3>Sub-modules</h3>
<ul>
<li><code><a title="tst" href="tst/index.html">tst</a></code></li>
<li><code><a title="obj" href="obj/index.html">obj</a></code></li>
<li><code><a title="img" href="img/index.html">img</a></code></li>
<li><code><a title="log" href="log/index.html">log</a></code></li>
<li><code><a title="efficient" href="efficient/index.html">efficient</a></code></li>
</ul>
		"""

	def add_supermod(x):
		s = "../qgol"
		if "base" in x:
			s = "../index"
		elif "qgol" in x and "test" not in x:
			return ""
		return '''
<h3>Super-modules</h3>
<ul>
<li><code><a title="super" href="'''+s+""".html">(super)</a></code></li></ul>
		"""
	
	def cleanf(f):
		""" Adding the right path to a file f"""
		try:
			with open(f,"r") as filen:
				pass
			return f
		except:
			#print("FILE:",f)
			if "log" in f:
				f = "doc/log/log.html"
			elif "qgol" in f and "test" not in f:
				f = "doc/"+f
			elif "index" in f:
				f = "doc/qgol.html"
			elif f[:-5] in ["qcubes","config","cube","cubes","index","partition","super","unit"]:
				f = "doc/obj/"+f
			elif len(f) > 15:
				f = f[:-5] + "/index.html"
			else:
				f = "doc/" + f[:-5] + "/index.html"
			return f

	def stistj(f,mark):
		""" Cutting the file f in half according to a mark.
		The mark is in the secondpart"""
		sti,stj,st = "","",f
		try:
			with open(f,"r") as filen:
				st = filen.read()
				sti = st
				for i in range(len(st)):
					if st[i:(i+len(mark))%len(st)] == mark:
						sti = st[:i]
						stj = st[i:]
						break
		except FileNotFoundError as e:
			print("problem:",e)
		return sti,stj,st

	for f in files:
		mark =""" <ul id="index">
<li>"""
		if "qgol.html" in f and not 'test' in f:
			
			f = cleanf(f)
			sti,stj,st = stistj(f,mark)
			
			
			try:
				if incantation not in st:
					with open(f,"w") as f:
						f.write(sti+incantation+stj)
				else:
					print("NO INCANTATION FOR",f)
			except BaseException as e:
				print("INCANTATION ERROR for ",f,e)
		
		elif ".html" in f and ".." not in f:
			f = cleanf(f)
			sm = add_supermod(f)
			sti,stj,st = stistj(f,mark)
			try:
				if "Super-modules" not in st and (sti or stj):
					print("SUPERMOD TO",f,sm)
					with open(f,"w") as f:
						f.write(sti+sm+stj)
			except: pass
	
	os.rename("doc/obj/base.html","doc/obj/base/index.html")

main()


