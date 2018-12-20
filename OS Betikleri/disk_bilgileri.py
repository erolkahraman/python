import os

disk = input("Disk bilgisi [\"/dev/sda\",\"/dev/sdb\"] veya mounted fs [\"/mnt/nfs\",\"/root\"]: ")

print(disk)


class disk_bilgisi():
	def __init__(self,dizin):
		self.dizin = dizin
		
	def bilgileri_getir(self):
		self.stat = os.statvfs(self.dizin)
		self.blok_sayisi = self.stat.f_blocks
	
	def bos_alan(self):
		self.bilgileri_getir()
		return self.blok_sayisi * 1024

try:
	abc = disk_bilgisi(disk)
except OSError as oe:
	print(oe)
	#print("Belirttiginiz disk veya mounted fs bulunamadi...")

print(abc.bos_alan())
