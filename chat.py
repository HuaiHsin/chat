
#讀取檔案
def read_file(filename):
	chatlist = []
	with open(filename, "r", encoding= "utf-8-sig") as f:
		for line in f:
			chatlist.append(line.strip())
	return chatlist

#轉換對話
def convert_file(filename):
	list2 = []
	speaker = None
	for i in range(len(filename)):
		if filename[i] == "Allen":
			speaker = "Allen"
		elif filename[i] == "Tom":
			speaker = "Tom"
		elif filename[i] != "Allen" and filename[i] != "Tom":
			list2.append(speaker + ": " + filename[i])
	return list2

#寫入檔案
def write_file(filename, chatlist):
	with open(filename, "w", encoding= "utf-8-sig") as f:
		for i in chatlist:
			f.write(i + "\n")

def main():
	chatlist = read_file("input.txt")
	chatlist =  convert_file(chatlist)
	write_file("output.txt", chatlist)

main()