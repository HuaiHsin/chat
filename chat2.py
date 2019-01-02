
#讀取檔案
def read_file(filename):
	chatlist = []
	with open(filename, "r", encoding= "utf-8-sig") as f:
		for line in f:
			chatlist.append(line.strip())
	return chatlist

#轉換對話
def convert_file(filename):
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0
	for line in filename:
		s = line.split(" ")
		time = s[0]
		name = s[1]
		if name == "Allen":
			if s[2] == "貼圖":
				allen_sticker_count += 1
			elif s[2] == "圖片":
				allen_image_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == "Viki":
			if s[2] == "貼圖":
				viki_sticker_count += 1
			elif s[2] == "圖片":
				viki_image_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)

	print("Allen說了", allen_word_count, "個字")
	print("Allen傳了", allen_sticker_count, "個貼圖")
	print("Allen傳了", allen_image_count, "張圖片")
	print("Viki說了", viki_word_count, "個字")
	print("Viki傳了", viki_sticker_count, "個貼圖") 
	print("Viki傳了", viki_image_count, "張圖片")


#寫入檔案
def write_file(filename, chatlist):
	with open(filename, "w", encoding= "utf-8-sig") as f:
		for i in chatlist:
			f.write(i + "\n")


def main():
	chatlist = read_file("-LINE-Viki.txt")
	chatlist =  convert_file(chatlist)
	#write_file("output.txt", chatlist)


main()