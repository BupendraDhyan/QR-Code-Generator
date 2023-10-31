import qrcode

def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save(file_name)

# Example usage:
data_to_encode = "Hello, world!"
output_file = "qr_code.png"
generate_qr_code(data_to_encode, output_file)