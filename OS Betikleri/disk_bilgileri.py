import os

disk = input("Disk bilgisi [\"/dev/sda\",\"/dev/sdb\"] veya mounted fs [\"/mnt/nfs\",\"/root\"]: ")


class disk_bilgisi():
	def __init__(self, dizin):
		self.dizin = dizin

	def tum_bilgileri_getir(self):
		self.stat = os.statvfs(self.dizin)
		self.blok_sayisi = self.stat.f_blocks
		self.blok_boyutu = self.stat.f_bsize
		self.serbest_blok_sayisi = self.stat.f_bavail
		self.toplam_disk_alani = (self.blok_sayisi * self.blok_boyutu) / 2 ** 30
		self.serbest_disk_alani = (self.serbest_blok_sayisi * self.blok_boyutu) / 2 ** 30
		self.kullanilan_disk_alani = (self.toplam_disk_alani - self.serbest_disk_alani)
		print("""
		Toplam disk alanı\t\t: {:.2f}G
		Serbest disk alanı\t\t: {:.2f}G
		Kullanılan disk alanı\t: {:.2f}G
		""".format(self.toplam_disk_alani, self.serbest_disk_alani, self.kullanilan_disk_alani))

	def serbest_disk_alani(self):
		print(self.serbest_disk_alani)

disk_durum = disk_bilgisi(disk)
disk_durum.serbest_disk_alani()
"""
while True:

	print("""

#	1. Boş disk alanı
#	2. Kullanılan disk alanı
#	3. Toplam disk alanı
#	4. Tüm disk bilgileri
#
#	Çıkış [q] :
	""")
	secim = input("Seçiminiz > ")

	if secim == "q":
		break
	elif secim == "1":
		print("Boş disk alanı: %sG" % disk_durum.serbest_disk_alani())
		break



"""

#disk_durumu = disk_bilgisi(disk)

#disk_durumu.tum_bilgileri_getir()

# print(disk_durumu.bos_alan())
