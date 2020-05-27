# Coded By WEYT.MM /*\ 28-05-2020
# https://github.com/WEYTMM/Jadwal-Kencan

from datetime import *
now = datetime.now()
hari_kencan = now.strftime("%A")
tanggal = date.today()


class main:
	def __init__(self, kencan):
		#Edit Sendiri Jadwal Kencan Kalian
		senin = """Gak ada jadwal kencan hari ini
		Doi lagi sibuk kegiatan ekskul nya disekolah
		Maklum lah cewe w kan aktif di organisasi
    """
		
		selasa = """Jam 15:30 • Jemput doi pulang sekolah
		Jam 16:30 • Bincang sore menunggu senja di rumah doi
		Jam 18:30 • Pamitan slurr gak enak maen sampe malem dirumah cewe
		Jam 21:00 • Tidur nyenyak hari ini"""
		
		rabu = """Libur dulu bos-Q lagi gak ada bensin buat kesono"""
		
		kamis = """Hari ini cuma jemput doi pulang sekolah doang
		Gak ada jadwal nge-date!!!"""
		
		jumat = """Gak ada jadwal nge-date bos-Q
		Padahal udah rindu berat ini:'("""
		
		sabtu = """Jam 15:30 • Jemput doi pulang sekolah
		Jam 16:10 • Makan sore dulu slurr
		Jam 16:30 • Jalan - jalan ke pinggir danau
		Jam 17:40 • Pulang ah udah mau Maghrib"""
		
		minggu = """Jam 08:00 • Mandi dulu bos-Q
		Jam 09:00 • Nyamper doi kerumahnya
		Jam 12:15 • Makan siang buat tenaga hari ini
		Jam 16:00 • Jalan - jalan di taman
		Jam 17:30 • Nganter doi pulang
		Jam 18:30 • Pamitan ke ortu doi w mau pulang
		Jam 21:00 • Tidur nyenyak hari ini"""
		
		if kencan == "Monday":
			kencan = senin
			hari = "Senin"
		elif kencan == "Tuesday":
			kencan = selasa
			hari = "Selasa"
		elif kencan == "Wednesday":
			kencan = rabu
			hari = "Rabu"
		elif kencan == "Thursday":
			kencan = kamis
			hari = "Kamis"
		elif kencan == "Friday":
			kencan = jumat
			hari = "Jum'at"
		elif kencan == "Saturday":
			kencan = sabtu
			hari = "Sabtu"
		elif kencan == "Sunday":
			kencan = minggu
			hari = "Minggu"
		
		self.kencan = kencan
		self.hari = hari
	
	def tampilkan(self):
		hasil = {}
		hasil['hari'] = self.hari
		hasil['kencan'] = self.kencan
		return hasil

def home():
	h = "\033[92m"
	p = "\033[0m"
	a = main(str(hari_kencan))
	b = a.tampilkan()
	print("Hari    : " + h + b['hari'] + p)
	print("Tanggal : " + h + str(tanggal) + p)
	print("\n\n\nJadwal Kencan Hari Ini :\n")
	for s in b['kencan'].replace('\t', '').splitlines():
		print("* " + s)

home()
