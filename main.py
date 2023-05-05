"""
Aplikasi Deteksi Gempa Terkini
"""


def ekstraksi_data():
    """
    Tanggal: 04 Mei 2023
    Waktu: 21:22:03 WIB
    Magnitudo: 3.6
    Kedalaman: 10 km
    lokasi: LS=10.52 - BT=121.70
    Pusat gempa: Pusat gempa berada di Laut 15 km BaratLaut Sabu Raijua
    Dirasakan: Dirasakan (Skala MMI): IV Sabu Raijua
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '04 Mei 2023'
    hasil['waktu'] = '21:22:03 WIB'
    hasil['magnitudo'] = 3.6
    hasil['lokasi'] = {'ls': 10.52, 'bt': 121.70}
    hasil['pusat'] = 'Pusat gempa berada di Laut 15 km BaratLaut Sabu Raijua'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): IV Sabu Raijua'

    return hasil


def tampilkan_data(result):
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi: LS= {result['lokasi']['ls']},BT={result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")



if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstraksi_data()
    tampilkan_data(result)
