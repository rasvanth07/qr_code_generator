import barcode

data = "23BCG059"
k = barcode.get_barcode_class('code128')
r = k(data)
r.save('barcode')