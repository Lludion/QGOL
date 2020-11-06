"""
Generates this documentation, using pdoc
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
	modules = ['qgol',"obj","log","img","tst","efficient","obj.base"]  # Public submodules are auto-imported
	context = pdoc.Context()

	modules = [pdoc.Module(mod, context=context)
		       for mod in modules]
	pdoc.link_inheritance(context)

	for mod in modules:
		for module_name, html in recursive_htmls(mod):
			with open("doc/"+repdot(module_name)+".html","w") as file:
				file.write(html)

	#print("lkjlk")
	files = glof("/home/urem/Desktop/work/ARTeQ/QGOL/")
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
	for f in files:
		mark =""" <ul id="index">
<li>"""
		if "qgol.html" in f and not 'test' in f:
			sti = ""
			stj = ""
			with open(f,"r") as filen:
				st = filen.read()
				mkpos = 0
				for i in range(len(st)):
					if st[i:(i+len(mark))%len(st)] == mark:
						sti = st[:i]
						stj = st[i:]
			
			with open(f,"w") as f:
				f.write(sti+incantation+stj)	
			
		


main()


