from PIL import Image
image_path = "profile picture.png"
image = Image.open(image_path)
new_width = 195  # عرض جدید تصویر (به صورت پیکسل)
new_height = 195  # ارتفاع جدید تصویر (به صورت پیکسل)
large_image = image.resize((new_width, new_height))
output_path = "large_profile_icon.png"
large_image.save(output_path)
