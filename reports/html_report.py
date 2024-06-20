from jinja2 import Template, Environment
from config import TEMPLATE_DIR, BASE_DIR
from webbrowser import open_new
from report import Report

result_list = [{'name': 'Faruk Şeker', 'title': 'Full Stack Developer', 'country': 'Netherlands', 'details': ['Freelencer, +2 more', 'Anadolu Üniversitesi, +1 more'], 'photograph': 'https://media.licdn.com/dms/image/D4D03AQH1Z2dg7iz7MQ/profile-displayphoto-shrink_200_200/0/1709814396783?e=2147483647&v=beta&t=kwoc1SJRo3B6dfAWOxAWppBSYvnUM2mB8x8QsVmybAU'}, {'name': 'Faruk Şeker', 'title': 'Boyaş Metal Kaplama şirketinde Production Chief', 'country': 'İzmit', 'details': ['Boyaş Metalize ve Metal Kaplama San. ve Tic. A.Ş.'], 'photograph': 'https://media.licdn.com/dms/image/D4D03AQHAl9r0oHS_-A/profile-displayphoto-shrink_200_200/0/1688489819382?e=2147483647&v=beta&t=1dT_-JpB_UMdKiAm8HAcTaQlEPxqfQIzWybiiLlEwJI'}, {'name': 'Şamil Faruk Şeker', 'title': 'Law student', 'country': 'Istanbul, Türkiye', 'details': ['Borsa İstanbul AŞ, +3 more', 'Kocaeli Üniversitesi'], 'photograph': 'https://media.licdn.com/dms/image/D4D03AQFeeAEHpkY85w/profile-displayphoto-shrink_200_200/0/1693059095498?e=2147483647&v=beta&t=Qt3iihYEwNEorP7SK67kOmflfj7gDg26ibAlolgASQQ'}, {'name': 'Faruk Seker', 'title': 'Şeker Tavukçuluk Gıd.Top. satış', 'country': 'Ankara, Türkiye', 'details': ['şeker piliç, +2 more'], 'photograph': 'https://media.licdn.com/dms/image/C5603AQGRC0u2Weg8-Q/profile-displayphoto-shrink_100_100/0/1651954089693?e=2147483647&v=beta&t=t-6yZxtpgBI-6xuAxPSNwLpfUewv8si0KO-CCUozs3Q'}, {'name': 'Ömer Faruk Şeker', 'title': 'General Manager & Tmt Makine Owner', 'country': 'Istanbul', 'details': ['Yuta Makina Müh. İnş. Bilg. San ve Tic. Ltd. Şti.', 'Atatürk Üniversitesi'], 'photograph': 'https://media.licdn.com/dms/image/C4D03AQG1o6nZDH7kbQ/profile-displayphoto-shrink_200_200/0/1611079063335?e=2147483647&v=beta&t=ygUvW19-xEVwdPfTfCv2EbbhcLLP2kvG0YixHQPiMrc'}, {'name': 'FARUK ŞEKER', 'title': 'PROJEKT MANAGER at SYG', 'country': 'Türkiye', 'details': ['SYG'], 'photograph': 'https://static.licdn.com/aero-v1/sc/h/1c5u578iilxfi4m4dvc4q810q'}, {'name': 'Faruk Şeker', 'title': 'Genel Müdür', 'country': 'Istanbul, Türkiye', 'details': ['Kanalsan'], 'photograph': 'https://media.licdn.com/dms/image/C4E03AQH_8d_oarDqZw/profile-displayphoto-shrink_200_200/0/1517479707491?e=2147483647&v=beta&t=LCSa18Fl_ZWhx_Yo1480pdM-jJRjVionoAyBVYCvKoo'}, {'name': 'Faruk Seker', 'title': 'Şu okulda öğrenci: Karadeniz Teknik Üniversitesi', 'country': 'Türkiye', 'details': [''], 'photograph': 'https://static.licdn.com/aero-v1/sc/h/1c5u578iilxfi4m4dvc4q810q'}, {'name': 'Ahmet Faruk Şeker', 'title': 'İstanbul Teknik Üniversitesi eğitim kurumunda öğrenci', 'country': 'İzmit', 'details': ['BMC Power, +3 more', 'İstanbul Teknik Üniversitesi, +2 more'], 'photograph': 'https://media.licdn.com/dms/image/C4D03AQEu8uvx9nh6Ug/profile-displayphoto-shrink_200_200/0/1647602635447?e=2147483647&v=beta&t=BB3Qjxp4Ed9ay136edJYqXd7V4dQNRgmh8tcZBTOxZI'}, {'name': 'Ömer Faruk Şeker', 'title': 'Psikolog', 'country': 'Kartal', 'details': ['Yetim Vakfı', 'İstanbul Üniversitesi'], 'photograph': 'https://media.licdn.com/dms/image/C4D03AQEmrqHUFXYRYA/profile-displayphoto-shrink_200_200/0/1596566429559?e=2147483647&v=beta&t=AEAIcQD7LaOzippR2zpG5YXwJveDKFv7awaDYrlfGuA'}, {'name': 'Ömer Faruk ŞEKER', 'title': 'Nanotechnology Engineer/Master Student of Physics/Research Assistant', 'country': 'Malatya, Türkiye', 'details': ['İnönü Üniversitesi, +1 more', 'İnönü Üniversitesi, +1 more'], 'photograph': 'https://static.licdn.com/aero-v1/sc/h/1c5u578iilxfi4m4dvc4q810q'}, {'name': 'Ömer Faruk Şeker', 'title': 'Manevi Danışman & Aile Danışmanı', 'country': 'Istanbul', 'details': ['Altınbaş Üniversitesi'], 'photograph': 'https://media.licdn.com/dms/image/D4D03AQHSxZj8RMtqnw/profile-displayphoto-shrink_200_200/0/1707171203532?e=2147483647&v=beta&t=GmUIWrAszOFWYHFjeVbjBk44UDbQSrbIVS4FuetP1cY'}, {'name': 'Faruk Şeker', 'title': '--', 'country': 'Elâzığ', 'details': None, 'photograph': 'https://media.licdn.com/dms/image/D4D03AQFCAOmFQm8MeA/profile-displayphoto-shrink_100_100/0/1705015480962?e=2147483647&v=beta&t=Im_J_NpdVn8eb5HrUwJW4z-sVne-YJEOBDTXnma4yfc'}, {'name': 'Faruk Şeker', 'title': '--', 'country': 'Şahinbey', 'details': None, 'photograph': 'https://static.licdn.com/aero-v1/sc/h/1c5u578iilxfi4m4dvc4q810q'}, {'name': 'Faruk Şeker', 'title': '--', 'country': 'İzmir', 'details': ['Aselsan'], 'photograph': 'https://media.licdn.com/dms/image/C4E03AQFFho1dGcgRjw/profile-displayphoto-shrink_100_100/0/1646159296878?e=2147483647&v=beta&t=FxhG_YDOGETQ6WI9Mc2h7XKkXZ0OvsqAVnHBuNq1zVo'}, {'name': 'Faruk ŞEKER', 'title': 'Erdemir şirketinde Müdür', 'country': 'Türkiye', 'details': ['Erdemir'], 'photograph': 'https://static.licdn.com/aero-v1/sc/h/1c5u578iilxfi4m4dvc4q810q'}, {'name': 'Faruk ŞEKER', 'title': 'Muhasebe / Finans / DİMER MERMER A.Ş', 'country': 'Türkiye', 'details': ['DİMER MERMER A.Ş'], 'photograph': 'https://static.licdn.com/aero-v1/sc/h/1c5u578iilxfi4m4dvc4q810q'}, {'name': 'Faruk ŞEKER', 'title': 'Warehouse and Logistics', 'country': 'Ankara', 'details': ['Smith & Nephew, +3 more', 'Anadolu Üniversitesi, +1 more'], 'photograph': 'https://media.licdn.com/dms/image/C5103AQEyZsMl7YldLg/profile-displayphoto-shrink_200_200/0/1517449971916?e=2147483647&v=beta&t=rF3ZrX3VP-hr8tL33IgqbIw1UdSL8ZSMU79i_0vO0Kg'}, {'name': 'Faruk Şeker', 'title': '--', 'country': 'Istanbul', 'details': ['Haffner Machinery'], 'photograph': 'https://static.licdn.com/aero-v1/sc/h/1c5u578iilxfi4m4dvc4q810q'}, {'name': 'Omer Faruk Seker', 'title': 'FARMED ESTETİK VE SAĞLIK HİZMETLERİ', 'country': 'Istanbul', 'details': ['Kendi işim, +3 more', 'Ondokuz Mayıs Üniversitesi'], 'photograph': 'https://media.licdn.com/dms/image/C4D03AQEEkGMF3uPwww/profile-displayphoto-shrink_200_200/0/1569767057982?e=2147483647&v=beta&t=Wr_q_vHSZ27ztYPfGU8zNDOjt0wgKVxBAAHfzNYP_DY'}, {'name': 'Faruk Şeker', 'title': 'Garson - Apple', 'country': 'Istanbul', 'details': ['Apple'], 'photograph': 'https://static.licdn.com/aero-v1/sc/h/1c5u578iilxfi4m4dvc4q810q'}, {'name': 'Ömer Faruk Seker', 'title': 'Student at Berlin University of Applied Sciences Berlin (BHT)', 'country': 'Berlin', 'details': ['REWE, +1 more', 'Berlin University of Applied Sciences Berlin (BHT), +2 more'], 'photograph': 'https://media.licdn.com/dms/image/D4E03AQGjFUrB5Z8Ajg/profile-displayphoto-shrink_200_200/0/1708008994211?e=2147483647&v=beta&t=hVr-QhzdVZXo7Gb3k9ygrEvxW_xAqBn70voP1HbQbTM'}, {'name': 'Umut Faruk Şeker', 'title': 'Boğaziçi Üniversitesi eğitim kurumunda öğrenci', 'country': 'Istanbul', 'details': ['Beyçelik Gestamp', 'Boğaziçi Üniversitesi'], 'photograph': 'https://media.licdn.com/dms/image/C4D03AQFlUzL408V6OQ/profile-displayphoto-shrink_200_200/0/1579280470254?e=2147483647&v=beta&t=csh_NHwHGmA1k_WP9CtqYJayUIhZQmYrZeIOwM6BIUA'}, {'name': 'Faruk Şeker', 'title': 'Veteriner hekimi / mast hayvancılık', 'country': 'Türkiye', 'details': ['mast hayvancılık'], 'photograph': 'https://static.licdn.com/aero-v1/sc/h/1c5u578iilxfi4m4dvc4q810q'}, {'name': 'Faruk Şeker', 'title': 'Devlet sekt şirketinde Officer', 'country': 'Türkiye', 'details': ['devlet sekt'], 'photograph': 'https://static.licdn.com/aero-v1/sc/h/1c5u578iilxfi4m4dvc4q810q'}, {'name': 'Ömer Faruk Şeker', 'title': '--', 'country': 'Haliliye', 'details': None, 'photograph': 'https://static.licdn.com/aero-v1/sc/h/1c5u578iilxfi4m4dvc4q810q'}, {'name': 'Ömer Faruk Şeker', 'title': 'İş Sağlığı ve İş Güvenliği - Elit Osgb', 'country': 'Istanbul, Türkiye', 'details': ['Elit Osgb, +4 more', 'Sakarya Üniversitesi'], 'photograph': 'https://media.licdn.com/dms/image/C4E03AQEZ8sXM9z_7wQ/profile-displayphoto-shrink_200_200/0/1517507533001?e=2147483647&v=beta&t=KkZzX8FPm0qUFfaJXf_Oo8hkb9V7xEc3zZ9XzRZzjp4'}, {'name': 'Ömer Faruk ŞEKER', 'title': 'Finans uzmanı', 'country': 'Şanlıurfa', 'details': ['Finansevim Tasarruf'], 'photograph': 'https://media.licdn.com/dms/image/C4E03AQHHDYpV0_3J4Q/profile-displayphoto-shrink_200_200/0/1606841063999?e=2147483647&v=beta&t=8f7ItJ_PtdONtDsgRkz0o1Pvi1l936IJRX1KNPN8NE4'}, {'name': 'Ömer Faruk ŞEKER', 'title': 'İnşaat Mühendisi', 'country': 'Türkiye', 'details': ['genç mühendislik', 'Karadeniz Teknik Üniversitesi'], 'photograph': 'https://static.licdn.com/aero-v1/sc/h/1c5u578iilxfi4m4dvc4q810q'}, {'name': 'Ömer Faruk Şeker', 'title': '--', 'country': 'Şanlıurfa', 'details': ['Kuveyt Türk Katılım Bankası'], 'photograph': 'https://static.licdn.com/aero-v1/sc/h/1c5u578iilxfi4m4dvc4q810q'}, {'name': 'Ömer Faruk Şeker', 'title': 'Şu okulda öğrenci: Çankırı Karatekin Üniversitesi', 'country': 'Osmaniye', 'details': ['Çankırı Karatekin Üniversitesi'], 'photograph': 'https://media.licdn.com/dms/image/C4D03AQG8m5Ju5ZiXeg/profile-displayphoto-shrink_200_200/0/1610809457405?e=2147483647&v=beta&t=IdWRWEZkTzJG9kBqMgN6T32EWOGRcRuwExqILWuIabc'}, {'name': 'Ömer Faruk Şeker', 'title': '--', 'country': 'Ankara, Türkiye', 'details': ['Türk Telekom Mesleki ve Teknik Anadolu Lisesi'], 'photograph': 'https://media.licdn.com/dms/image/C4E03AQFTPfJk99tbww/profile-displayphoto-shrink_200_200/0/1599255922334?e=2147483647&v=beta&t=1V0P1OYSwI23YKBAYqZk9KLsk1oakm2r0k1DXJsbFDk'}, {'name': 'Ömer Faruk ŞEKER', 'title': '--', 'country': 'Ankara', 'details': None, 'photograph': 'https://media.licdn.com/dms/image/D4D03AQF3ewRcgnY9WA/profile-displayphoto-shrink_100_100/0/1649372303463?e=2147483647&v=beta&t=06tvW8uf47CNfQnJlh_XpikPbw0pb-UstG9V5txvnbQ'}, {'name': 'Ahmet Faruk Şeker', 'title': 'Sportif danışmanlık şirketinde Sportif danışman', 'country': 'Şanlıurfa', 'details': ['Sportif danışmanlık'], 'photograph': 'https://static.licdn.com/aero-v1/sc/h/1c5u578iilxfi4m4dvc4q810q'}, {'name': 'Ömer Faruk Şeker', 'title': '--', 'country': 'Ankara', 'details': None, 'photograph': 'https://media.licdn.com/dms/image/C5603AQFYyKoFF31BLw/profile-displayphoto-shrink_100_100/0/1656111119480?e=2147483647&v=beta&t=WcIzaglh7VtalqfdA08EHhFozMS4C0ysAsIxCdLAUUU'}, {'name': 'Ömer Faruk Şeker', 'title': '--', 'country': 'Melikgazi', 'details': None, 'photograph': 'https://media.licdn.com/dms/image/C5603AQGgJZOLyeyVCw/profile-displayphoto-shrink_100_100/0/1650009877752?e=2147483647&v=beta&t=2Pz7ypV100LlUp5xDCJwlHNY1kGg6K8uz31S5JNtmIA'}, {'name': 'Ömer Faruk Şeker', 'title': '--', 'country': 'Şanlıurfa', 'details': None, 'photograph': 'https://media.licdn.com/dms/image/D4D03AQFJ37Ofl3P9tg/profile-displayphoto-shrink_100_100/0/1707654989488?e=2147483647&v=beta&t=uBjxIpZQm_Pws7uwFjVAzwjdNdaDix1zR9mnB5u0d3I'}, {'name': 'Ömer Faruk Şeker', 'title': None, 'country': 'Istanbul', 'details': None, 'photograph': 'https://static.licdn.com/aero-v1/sc/h/1c5u578iilxfi4m4dvc4q810q'}, {'name': 'ÖMER FARUK ŞEKER', 'title': '--', 'country': 'Istanbul', 'details': None, 'photograph': 'https://static.licdn.com/aero-v1/sc/h/1c5u578iilxfi4m4dvc4q810q'}, {'name': 'Ömer Faruk Şeker', 'title': 'Şu okulda öğrenci: Kocaeli Fen Lisesi', 'country': 'Kocaeli', 'details': ['Kocaeli Fen Lisesi'], 'photograph': 'https://static.licdn.com/aero-v1/sc/h/1c5u578iilxfi4m4dvc4q810q'}, {'name': 'Ömer Faruk ŞEKER', 'title': '--', 'country': 'Ankara', 'details': None, 'photograph': 'https://static.licdn.com/aero-v1/sc/h/1c5u578iilxfi4m4dvc4q810q'}, {'name': 'Ömer Faruk ŞEKER', 'title': 'İnşaat Profesyonel', 'country': 'Samsun, Türkiye', 'details': ['ışık yapı'], 'photograph': 'https://static.licdn.com/aero-v1/sc/h/1c5u578iilxfi4m4dvc4q810q'}, {'name': 'ÖMER FARUK ŞEKER', 'title': 'ALFAVET ECZA DEPOSU şirketinde MUHASEBE', 'country': 'Türkiye', 'details': ['ALFAVET ECZA DEPOSU'], 'photograph': 'https://static.licdn.com/aero-v1/sc/h/1c5u578iilxfi4m4dvc4q810q'}]


class HtmlReport(Report):
    output_settings: dict = {
        'defaultextension': '.html',
        'title': 'Save File',
        'initialfile': 'result.html',
        'filetypes': [("HTML files", "*.html"), ("All files", "*.*")]
    }

    def __init__(self, data):
        self.data = data
        self.load_report()

    def load_report(self):
        with open(TEMPLATE_DIR / 'person_search_list.html', encoding='utf-8') as template_file:
            template = Template(template_file.read())
            self.output = template.render({'persons': self.data})

    def save_report(self):
        output_path = self.asksaveasfilename()
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(self.output)


if __name__ == '__main__':
    html_report = HtmlReport(result_list)
    html_report.save_report()
